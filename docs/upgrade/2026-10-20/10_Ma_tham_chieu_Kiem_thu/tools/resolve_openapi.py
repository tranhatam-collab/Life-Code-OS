#!/usr/bin/env python3
"""Materialize the local Life Code OS OpenAPI overlay without network access.

The generator is deterministic: it has no clock, network, environment or random
inputs.  It validates the JSON/YAML base pair, applies the supported Overlay 1.2
targets, bundles the nine canonical JSON Schemas, and writes semantically equal
JSON/YAML artifacts.  Use --check in CI to prove the committed outputs are fresh.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as error:  # pragma: no cover - exercised by developer setup
    raise SystemExit("PyYAML is required for the planning-only OpenAPI resolver") from error


RELEASE_ROOT = Path(__file__).resolve().parents[2]
BACKEND_DIR = RELEASE_ROOT / "04_Backend_API"
SCHEMA_DIR = RELEASE_ROOT / "03_Du_lieu_Phep_tinh" / "schemas"
BASE_JSON = BACKEND_DIR / "openapi.json"
BASE_YAML = BACKEND_DIR / "openapi.yaml"
OVERLAY_YAML = BACKEND_DIR / "openapi.upgrade.overlay.yaml"
OUTPUT_JSON = BACKEND_DIR / "openapi.resolved.json"
OUTPUT_YAML = BACKEND_DIR / "openapi.resolved.yaml"
OPERATION_REGISTRY = BACKEND_DIR / "API_OPERATIONS.json"
RESOLVER_SOURCE = Path(__file__).resolve()
RESOLVER_REQUIREMENTS = RELEASE_ROOT / "10_Ma_tham_chieu_Kiem_thu" / "requirements-openapi-resolver.txt"

HTTP_METHODS = {"get", "put", "post", "delete", "options", "head", "patch", "trace"}
CANONICAL_SCHEMAS = (
    "Claim",
    "JobEnvelope",
    "MethodRelease",
    "MethodResult",
    "Metric",
    "ProfileVersion",
    "ReleaseReceipt",
    "ReportSnapshot",
    "Tail80Result",
)


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8-sig"))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def merge_object(target: dict[str, Any], update: dict[str, Any]) -> None:
    """Apply Overlay object update semantics for this package's object updates."""

    for key, value in update.items():
        if isinstance(value, dict) and isinstance(target.get(key), dict):
            merge_object(target[key], value)
        else:
            target[key] = copy.deepcopy(value)


def operation_items(document: dict[str, Any]):
    for route, path_item in document["paths"].items():
        for method, operation in path_item.items():
            if method in HTTP_METHODS:
                yield route, method, operation


def apply_action(document: dict[str, Any], action: dict[str, Any]) -> None:
    target = action["target"]
    update = action.get("update")
    remove = action.get("remove") is True

    if target == "$.info":
        if remove:
            raise ValueError("The info object cannot be removed")
        merge_object(document["info"], update)
        return

    if target == "$.paths.*.*":
        if remove:
            raise ValueError("Wildcard operation removal is not supported")
        for _route, _method, operation in operation_items(document):
            merge_object(operation, update)
        return

    wildcard_method = re.fullmatch(r"\$\.paths\.\*\.(get|put|post|delete|options|head|patch|trace)", target)
    if wildcard_method:
        method = wildcard_method.group(1)
        for path_item in document["paths"].values():
            if method in path_item:
                if remove:
                    del path_item[method]
                else:
                    merge_object(path_item[method], update)
        return

    exact_operation = re.fullmatch(r"\$\.paths\['(.+)'\]\.(get|put|post|delete|options|head|patch|trace)", target)
    if exact_operation:
        route, method = exact_operation.groups()
        operation = document["paths"][route][method]
        if remove:
            del document["paths"][route][method]
        else:
            merge_object(operation, update)
        return

    if target == "$.components.schemas":
        if remove:
            raise ValueError("The schema registry cannot be removed")
        merge_object(document["components"]["schemas"], update)
        return

    exact_schema = re.fullmatch(r"\$\.components\.schemas\.([A-Za-z][A-Za-z0-9_]*)", target)
    if exact_schema:
        name = exact_schema.group(1)
        schemas = document["components"]["schemas"]
        if remove:
            schemas.pop(name, None)
        else:
            if name not in schemas:
                schemas[name] = {}
            merge_object(schemas[name], update)
        return

    raise ValueError(f"Unsupported overlay target: {target}")


def json_pointer(document: Any, pointer: str) -> Any:
    if not pointer.startswith("#/"):
        raise ValueError(f"Not a local JSON Pointer: {pointer}")
    value = document
    for raw in pointer[2:].split("/"):
        token = raw.replace("~1", "/").replace("~0", "~")
        if isinstance(value, list):
            value = value[int(token)]
        else:
            value = value[token]
    return value


def refs_in(value: Any):
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "$ref" and isinstance(child, str):
                yield child
            yield from refs_in(child)
    elif isinstance(value, list):
        for child in value:
            yield from refs_in(child)


def success_contract(operation: dict[str, Any], status: int) -> tuple[str | None, str | None]:
    response = operation.get("responses", {}).get(str(status), {})
    content = response.get("content", {})
    if not content:
        return None, None
    media_type = "application/json" if "application/json" in content else sorted(content)[0]
    schema = content[media_type].get("schema", {})
    return media_type, schema.get("$ref") if isinstance(schema, dict) else None


def request_schema_ref(operation: dict[str, Any]) -> str | None:
    content = operation.get("requestBody", {}).get("content", {})
    if not content:
        return None
    media_type = "application/json" if "application/json" in content else sorted(content)[0]
    schema = content[media_type].get("schema", {})
    return schema.get("$ref") if isinstance(schema, dict) else None


def route_namespace(route: str) -> str:
    return next((part for part in route.strip("/").split("/") if part and not part.startswith("{")), "root")


def materialize() -> dict[str, Any]:
    base_json = load_json(BASE_JSON)
    base_yaml = load_yaml(BASE_YAML)
    if base_json != base_yaml:
        raise ValueError("openapi.json and openapi.yaml are not semantically equal")

    overlay = load_yaml(OVERLAY_YAML)
    if overlay.get("overlay") != "1.2.0":
        raise ValueError("Expected OpenAPI Overlay 1.2.0")
    if overlay.get("extends") != "./openapi.yaml":
        raise ValueError("Overlay must extend the preserved local YAML base")
    if len(overlay.get("actions", [])) != 17:
        raise ValueError("Expected exactly 17 reviewed overlay actions")

    document = copy.deepcopy(base_json)
    for action in overlay.get("actions", []):
        apply_action(document, action)

    canonical_documents: dict[str, Any] = {}
    for name in CANONICAL_SCHEMAS:
        schema_path = SCHEMA_DIR / f"{name}.schema.json"
        canonical_documents[name] = load_json(schema_path)
        document["components"]["schemas"][name] = copy.deepcopy(canonical_documents[name])

    generic_consumers: list[dict[str, Any]] = []
    response_contracts: dict[str, Any] = {}
    registry = load_json(OPERATION_REGISTRY)
    registry_by_id = {row["operation_id"]: row for row in registry}
    if len(registry) != 64 or len(registry_by_id) != 64:
        raise ValueError("Operation registry must contain exactly 64 unique operation_id values")
    operations = list(operation_items(document))
    if len(operations) != 64 or len({op[2].get("operationId") for op in operations}) != 64:
        raise ValueError("Resolved contract must contain exactly 64 unique operationId values")

    for route, method, operation in operations:
        operation_id = operation["operationId"]
        row = registry_by_id.get(operation_id)
        if row is None or row["path"] != route or row["method"].lower() != method:
            raise ValueError(f"Operation registry mismatch: {operation_id}")
        if operation.get("x-required-permission") != row["permission"]:
            raise ValueError(f"Operation permission mismatch: {operation_id}")
        if request_schema_ref(operation) != row["request_schema"]:
            raise ValueError(f"Operation request schema mismatch: {operation_id}")
        media_type, schema_ref = success_contract(operation, row["success"])
        if schema_ref != row["response_schema"]:
            raise ValueError(f"Operation response schema mismatch: {operation_id}")
        if schema_ref in ("#/components/schemas/Resource", "#/components/schemas/ResourcePage"):
            typing_state = "TRANSITIONAL_GENERIC_BLOCKER"
            blocker = {
                "operation_id": operation_id,
                "method": method.upper(),
                "path": route,
                "success_status": row["success"],
                "generic_schema_ref": schema_ref,
                "route_namespace": route_namespace(route),
            }
            generic_consumers.append(blocker)
            operation["x-lc-response-contract-status"] = typing_state
            operation["x-lc-codegen-ready"] = False
            operation["x-lc-route-namespace"] = blocker["route_namespace"]
        elif schema_ref:
            typing_state = "NAMED_SCHEMA"
        elif media_type:
            typing_state = "INLINE_OR_UNSPECIFIED_SCHEMA"
        else:
            typing_state = "NO_RESPONSE_BODY_SCHEMA"
        response_contracts[operation_id] = {
            "success_status": row["success"],
            "media_type": media_type,
            "schema_ref": schema_ref,
            "typing_state": typing_state,
        }

    resource = document["components"]["schemas"]["Resource"]
    resource["x-lc-contract-status"] = "TRANSITIONAL_GENERIC_BLOCKER"
    resource["x-lc-codegen-ready"] = False
    resource["x-lc-generic-consumer-operation-ids"] = [row["operation_id"] for row in generic_consumers if row["generic_schema_ref"].endswith("/Resource")]
    attributes = resource["properties"]["attributes"]
    attributes["additionalProperties"] = True
    attributes["description"] = "Intentionally untyped transition field. Do not generate a production domain model until this operation has a named response schema and field-level authorization review."
    attributes["x-lc-contract-status"] = "TRANSITIONAL_GENERIC_BLOCKER"

    resource_page = document["components"]["schemas"]["ResourcePage"]
    resource_page["description"] = "Transitional page of generic Resource objects. NOT codegen-ready for a production domain contract."
    resource_page["x-lc-contract-status"] = "TRANSITIONAL_GENERIC_BLOCKER"
    resource_page["x-lc-codegen-ready"] = False
    resource_page["x-lc-generic-consumer-operation-ids"] = [row["operation_id"] for row in generic_consumers if row["generic_schema_ref"].endswith("/ResourcePage")]

    document["info"].update(
        {
            "x-lc-canonical-current-contract": "./openapi.resolved.yaml",
            "x-lc-json-semantic-mirror": "./openapi.resolved.json",
            "x-lc-generated-by": "../10_Ma_tham_chieu_Kiem_thu/tools/resolve_openapi.py",
            "x-lc-resolution-mode": "LOCAL_DETERMINISTIC_OVERLAY_AND_CANONICAL_SCHEMA_BUNDLE",
            "x-lc-applied-overlay-action-count": len(overlay["actions"]),
            "x-lc-input-sha256": {
                "openapi.json": digest(BASE_JSON),
                "openapi.yaml": digest(BASE_YAML),
                "openapi.upgrade.overlay.yaml": digest(OVERLAY_YAML),
                "API_OPERATIONS.json": digest(OPERATION_REGISTRY),
                "../10_Ma_tham_chieu_Kiem_thu/tools/resolve_openapi.py": digest(RESOLVER_SOURCE),
                "../10_Ma_tham_chieu_Kiem_thu/requirements-openapi-resolver.txt": digest(RESOLVER_REQUIREMENTS),
                **{f"../03_Du_lieu_Phep_tinh/schemas/{name}.schema.json": digest(SCHEMA_DIR / f"{name}.schema.json") for name in CANONICAL_SCHEMAS},
            },
        }
    )
    document["x-lc-operation-response-contracts"] = response_contracts
    document["x-lc-generic-response-blockers"] = {
        "count": len(generic_consumers),
        "codegen_ready": False,
        "resolution_requirement": "Replace each generic success schema with a named schema after field-level authorization and implementation review.",
        "operations": generic_consumers,
    }

    all_refs = list(refs_in(document))
    external_refs = sorted({ref for ref in all_refs if not ref.startswith("#/")})
    if external_refs:
        raise ValueError(f"Resolved contract still has external refs: {external_refs}")
    for ref in all_refs:
        json_pointer(document, ref)
    for name, canonical in canonical_documents.items():
        if document["components"]["schemas"][name] != canonical:
            raise ValueError(f"Canonical schema drift after bundling: {name}")

    document["info"]["x-lc-local-ref-count"] = len(all_refs)
    document["info"]["x-lc-generic-response-blocker-count"] = len(generic_consumers)
    return document


def rendered(document: dict[str, Any]) -> tuple[str, str]:
    json_text = json.dumps(document, ensure_ascii=False, indent=2) + "\n"
    yaml_text = yaml.safe_dump(
        document,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=120,
    )
    return json_text, yaml_text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="verify committed resolved artifacts without writing")
    args = parser.parse_args()
    document = materialize()
    json_text, yaml_text = rendered(document)

    if args.check:
        stale = []
        for path, expected in ((OUTPUT_JSON, json_text), (OUTPUT_YAML, yaml_text)):
            if not path.exists() or path.read_text(encoding="utf-8") != expected:
                stale.append(path.name)
        if stale:
            print("STALE: " + ", ".join(stale), file=sys.stderr)
            return 1
    else:
        OUTPUT_JSON.write_text(json_text, encoding="utf-8")
        OUTPUT_YAML.write_text(yaml_text, encoding="utf-8")

    print(
        json.dumps(
            {
                "status": "CURRENT" if args.check else "WRITTEN",
                "canonical": OUTPUT_YAML.name,
                "operation_count": 64,
                "canonical_schema_count": len(CANONICAL_SCHEMAS),
                "local_ref_count": document["info"]["x-lc-local-ref-count"],
                "generic_response_blocker_count": document["info"]["x-lc-generic-response-blocker-count"],
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
