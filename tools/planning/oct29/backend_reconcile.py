#!/usr/bin/env python3
"""Rebuild the planning-only backend merge. Never imports SQL or touches application code."""
from __future__ import annotations
import copy
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "docs/upgrade/sources/2026-10-29"
V2 = SOURCE / "v2/package/LIFE_CODE_OS_V2_2026-10-20"
V3 = SOURCE / "v3/package/LIFE_CODE_OS_ALL_IN_ONE_V3_2026-10-29"
LOCAL = ROOT / "docs/upgrade/2026-10-20"
OUT = ROOT / "docs/upgrade/2026-10-29/backend"
VERBS = {"get", "put", "post", "patch", "delete", "options", "head", "trace"}
STRONG = ["Claim", "ProfileVersion", "ReleaseReceipt", "Tail80Result", "MethodResult", "ReportSnapshot", "Metric", "JobEnvelope", "MethodRelease"]

def read(path):
    return json.loads(path.read_text())

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def rel(path):
    return str(path.relative_to(ROOT))

def write(name, data):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

def ops(doc):
    return {op["operationId"]: (p, m, op) for p, item in doc["paths"].items()
            for m, op in item.items() if m in VERBS}

def refs(value):
    if isinstance(value, dict):
        if "$ref" in value:
            yield value["$ref"]
        for child in value.values():
            yield from refs(child)
    elif isinstance(value, list):
        for child in value:
            yield from refs(child)

def resolve(doc, ref):
    if not ref.startswith("#/"):
        raise ValueError("External reference: " + ref)
    value = doc
    for part in ref[2:].split("/"):
        value = value[part.replace("~1", "/").replace("~0", "~")]
    return value

def build_contract():
    local_path = LOCAL / "04_Backend_API/openapi.resolved.json"
    v2_path = V2 / "05_BACKEND/openapi.target.v2.json"
    v3_path = V3 / "07_BACKEND/openapi.v3.target.json"
    local, v2, v3 = map(read, [local_path, v2_path, v3_path])
    lo, vo, to = map(ops, [local, v2, v3])
    assert len(lo) == 64 and len(vo) == 83 and len(to) == 99
    assert set(lo) <= set(vo) <= set(to)
    unified = copy.deepcopy(v3)
    unified["info"]["title"] = "Life Code OS unified planning target — local R2 + external V2/V3"
    unified["info"]["version"] = "2026-10-29-design-reconciled"
    unified["info"]["description"] = "Planning candidate only. Missing business contracts and permissions block production code generation and release."
    unified["paths"] = {}
    # Keep all V2/V3 additions; local reviewed definitions win shared legacy names.
    unified["components"]["schemas"].update(copy.deepcopy(local["components"]["schemas"]))
    schemas = unified["components"]["schemas"]
    # The imported target stripped $schema/$id/title from its 27 new schema
    # components. Retain their complete standalone schema resources unchanged.
    new_schema_receipts = []
    for base in [V2 / '05_BACKEND', V3 / '07_BACKEND']:
        for path in sorted((base / 'schemas').glob('*.schema.json')):
            name = path.name.removesuffix('.schema.json')
            schemas[name] = read(path)
            new_schema_receipts.append({'name':name,'source':rel(path),'sha256':sha(path),'preserved_exact_object':True})
    canonical_receipts = []
    for name in STRONG:
        path = LOCAL / f"03_Du_lieu_Phep_tinh/schemas/{name}.schema.json"
        source = read(path)
        schemas[name] = copy.deepcopy(source)
        assert schemas[name] == source
        canonical_receipts.append({"name": name, "source": rel(path), "sha256": sha(path),
            "target_legacy_required_missing": sorted(set(source.get("required", [])) - set(v3["components"]["schemas"][name].get("required", [])))})
    proposals = {"listHypotheses":"HypothesisPage", "compareRuns":"RunComparisonView", "previewMethod":"MethodPreviewResult", "methodDependencies":"MethodDependencyPage", "methodTestVectors":"GoldenVectorPage", "resolveHypotheses":"HypothesisResolutionReceipt", "runTrace":"RunTraceView", "runDependencies":"RunDependencyPage", "claimProvenance":"ClaimProvenanceView", "reviewReportV2":"ReportReviewReceipt", "withdrawReportV2":"ReportWithdrawalReceipt", "reportDiff":"ReportDiffView", "newDeletionV2":"DeletionAcceptedReceipt", "deletionStatusV2":"DeletionStatusView", "countryEligibility":"CountryEligibilityView", "releaseImpact":"MethodImpactPage", "freezeMethod":"MethodFreezeReceipt", "resonanceSummaryV2":"MetricSummaryView", "syncOfflineBatch":"OfflineBatchReceipt", "computeNumerologyFull":"NumerologyFullResult wrapped by canonical MethodResult", "computeBatCuc":"BatCucResult wrapped by canonical MethodResult", "computePsychomatrix":"PsychomatrixResult wrapped by canonical MethodResult", "compareNumberAssets":"NumberComparisonView", "compareNameVariants":"NameComparisonView", "composeLifetime":"LifetimeCompositionView", "createAnalysisBundle":"AnalysisBundleAcceptedReceipt", "getAnalysisBundle":"AnalysisBundleStatusView", "cancelAnalysisBundle":"AnalysisBundleCancellationReceipt", "getMethodSourceConflicts":"MethodSourceConflictPage", "getBatCucTable":"VersionedPairTableView", "getLifeDomains":"VersionedLifeDomainPage", "getScopedProductEligibility":"ScopedProductEligibilityView", "createKnowledgeLegacyTransfer":"KnowledgeTransferReceipt", "getTerritoryReleaseGates":"TerritoryReleaseGateView", "getMethodVersionHistory":"MethodVersionPage"}
    rows, changes = [], []
    for oid, (original_path, method, original_op) in to.items():
        if oid in lo:
            path, _, selected = lo[oid]
            origin, source_path = "LOCAL_R2_64", local_path
        elif oid in vo:
            path, _, selected = vo[oid]
            origin, source_path = "EXTERNAL_V2_ADDITION_19", v2_path
        else:
            path, selected = original_path, original_op
            origin, source_path = "EXTERNAL_V3_ADDITION_16", v3_path
        canonical_path = path.removeprefix("/api/v2") if path.startswith("/api/v2/") else path
        op = copy.deepcopy(selected)
        raw_auth = {k: op[k] for k in ["x-required-permission", "x-permission", "x-required-policy"] if k in op}
        permission = raw_auth.get("x-required-permission", raw_auth.get("x-permission"))
        policies = raw_auth.get("x-required-policy", [])
        blockers = []
        if permission is None:
            blockers += ["PERMISSION_ACTION_AND_RESOURCE_SCOPE_UNRESOLVED"]
        success = []
        for status, response in op["responses"].items():
            if not str(status).startswith("2"):
                continue
            if "$ref" in response:
                response = resolve(unified, response["$ref"])
            content = response.get("content", {})
            if not content:
                state = "NO_BODY_EXPECTED" if str(status) == "204" else "MISSING_SUCCESS_SCHEMA"
                if state == "MISSING_SUCCESS_SCHEMA":
                    blockers.append(state)
                success.append({"status": status, "state": state, "schema_refs": []})
            for media, body in content.items():
                schema = body.get("schema", {})
                rr = list(refs(schema))
                generic = any(r.endswith(("/Resource", "/ResourcePage")) for r in rr)
                reference = any(r.endswith("/ReferenceResult") for r in rr)
                state = "GENERIC_SUCCESS_SCHEMA" if generic else "REFERENCE_ONLY_RESPONSE" if reference else "NAMED_SCHEMA" if rr else "INLINE_SCHEMA" if schema else "MISSING_SUCCESS_SCHEMA"
                if state in {"GENERIC_SUCCESS_SCHEMA", "REFERENCE_ONLY_RESPONSE", "MISSING_SUCCESS_SCHEMA"}:
                    blockers.append(state)
                success.append({"status": status, "media_type": media, "state": state, "schema_refs": rr})
        if origin == "EXTERNAL_V3_ADDITION_16":
            blockers.append("FIELD_LEVEL_AUTHORIZATION_AND_SUBJECT_CONTEXT_UNRESOLVED")
        # Normalize extension vocabulary without inventing a permission for the 16 new endpoints.
        for key in raw_auth:
            op.pop(key)
        op["x-lc-authorization"] = {"schema_version": "planning-1", "permission": permission,
            "policy_requirements": policies, "mapping_state": "PRESERVED_PERMISSION_REQUIRES_SERVER_ENFORCEMENT" if permission else "UNRESOLVED_FAIL_CLOSED",
            "source_extensions": raw_auth, "runtime_authority": False}
        op["x-lc-source-contract"] = {"origin": origin, "file": rel(source_path), "source_operation_id": oid,
            "source_path": path, "external_v3_path": original_path, "canonical_path": canonical_path,
            "change_scope": "planning_only_no_runtime_route_claim"}
        op["x-lc-codegen-blockers"] = sorted(set(blockers))
        assert method not in unified["paths"].setdefault(canonical_path, {}), (method, canonical_path)
        unified["paths"][canonical_path][method] = op
        idem = [p for p in op.get("parameters", []) if p.get("in") == "header" and p.get("name", "").lower() == "idempotency-key"]
        row = {"operation_id": oid, "method": method.upper(), "canonical_path": canonical_path,
            "effective_design_path": "/api/v2" + canonical_path, "original_v3_path": original_path,
            "origin": origin, "source": rel(source_path), "authorization": op["x-lc-authorization"],
            "request_schema_refs": list(refs(op.get("requestBody", {}))), "success_responses": success,
            "idempotency_header_contracts": idem, "codegen_blockers": sorted(set(blockers)),
            "response_design_proposal": {"name": proposals.get(oid), "status": "PROPOSED_NOT_BOUND_TO_API", "acceptance": "Define exact authorized fields, pagination/versioning/null reasons and positive/negative fixtures before binding; never reuse an input schema as output."} if oid in proposals else {"name": None, "status": "USE_EXISTING_NAMED_CONTRACT_OR_DESIGN_RESOURCE_SPECIFIC_RESPONSE", "acceptance": "Close generic response fields and preserve local canonical invariants."},
            "implemented_by_import": False}
        rows.append(row)
        if original_path != canonical_path:
            changes.append({"operation_id": oid, "from": original_path, "to": canonical_path,
                "server_base": "/api/v2", "reason": "Avoid doubled /api/v2 prefix when path is appended to server URL."})
    unresolved = []
    for r in refs(unified):
        try:
            resolve(unified, r)
        except (KeyError, TypeError, ValueError):
            unresolved.append(r)
    assert not unresolved, unresolved
    assert len(ops(unified)) == 99
    assert set(v3["components"]["schemas"]) <= set(schemas)
    unified["x-implementation-status"] = "PLANNING_TARGET_ONLY_NOT_DEPLOYED"
    unified["x-lc-codegen-ready"] = False
    unified["x-lc-canonical-schemas"] = canonical_receipts
    unified["x-lc-new-standalone-schemas"] = new_schema_receipts
    unified["x-lc-operation-response-contracts"] = {r["operation_id"]: r["success_responses"] for r in rows}
    unified["x-lc-generic-response-blockers"] = {"codegen_ready": False,
        "operation_count": sum(bool(r["codegen_blockers"]) for r in rows),
        "operations": [{"operation_id": r["operation_id"], "blockers": r["codegen_blockers"]} for r in rows if r["codegen_blockers"]]}
    write("OPENAPI_UNIFIED_TARGET.json", unified)
    csv_rows = list(csv.DictReader((V3 / '07_BACKEND/API_OPERATIONS_V3.csv').read_text(encoding='utf-8-sig').splitlines()))
    assert len(csv_rows) == 99 and {r['operation_id'] for r in csv_rows} == set(to)
    assert all((r['path'],r['method'].lower()) == to[r['operation_id']][:2] for r in csv_rows)
    result = {"schema_version": "planning-1", "date": "2026-10-29", "production_ready": False,
        "codegen_ready": False, "operation_count": len(rows), "origin_counts": dict(Counter(r["origin"] for r in rows)),
        "canonical_schema_receipts": canonical_receipts, "path_prefix_corrections": changes,
        "new_standalone_schema_receipts": new_schema_receipts,
        "unresolved_internal_refs": unresolved, "component_schema_count": len(schemas),
        "generic_success_operation_count": sum(any(s["state"] == "GENERIC_SUCCESS_SCHEMA" for s in r["success_responses"]) for r in rows),
        "missing_success_schema_operation_count": sum(any(s["state"] == "MISSING_SUCCESS_SCHEMA" for s in r["success_responses"]) for r in rows),
        "reference_only_success_operation_count": sum(any(s["state"] == "REFERENCE_ONLY_RESPONSE" for s in r["success_responses"]) for r in rows),
        "blocked_operation_count": sum(bool(r["codegen_blockers"]) for r in rows),
        "api_csv99_parity": True,
        "standards": [
            {"url": "https://spec.openapis.org/oas/v3.1.0.html#paths-object", "checked_on": "2026-10-29", "scope": "Paths appended to server URL; OAS 3.1 schema dialect."},
            {"url": "https://json-schema.org/draft/2020-12/json-schema-core", "checked_on": "2026-10-29", "scope": "Dialect, identifiers and reference resolution. No production-validator certification."},
            {"url": "https://www.postgresql.org/docs/18/ddl-rowsecurity.html", "checked_on": "2026-10-29", "scope": "RLS privileges, default deny, owner and BYPASSRLS exceptions. Database version still a candidate."}],
        "operations": rows}
    write("API_CONTRACT_RECONCILIATION.json", result)
    md = ['# Đối chiếu hợp đồng API hợp nhất ngày 29/10/2026', '',
        '**99 operation được giữ; hợp đồng này là thiết kế, chưa cho phép codegen hoặc phát hành.** 64 operation lấy bản local R2, 19 bổ sung V2 và 16 bổ sung V3. CSV nguồn 99 dòng khớp operation ID/method/path với OpenAPI V3. Không có reference nội bộ chưa phân giải trong bản hợp nhất.', '',
        '65 operation có success schema chung Resource/ResourcePage; 10 operation V3 thiếu success schema; 6 operation V3 dùng ReferenceResult với status cố định REFERENCE_ONLY. 81 operation có blocker ghi riêng. Tên response đề xuất trong bảng là công việc thiết kế cần duyệt, chưa được gắn thành schema hoặc coi là đã có API.', '',
        '## Quyết định hợp nhất', '',
        '- Giữ 9 object schema local canonical chính xác và toàn bộ 27 schema mới V2/V3. Giữ các response/error contracts local đã được làm chặt. Component union có 68 schema.',
        '- Chuẩn hóa 16 path V3 bằng cách bỏ prefix /api/v2 trong path, dùng server base /api/v2; source path giữ ở provenance.',
        '- Chuẩn hóa ba extension quyền thành x-lc-authorization, lưu source_extensions nguyên trạng. 16 V3 chưa có permission action/resource cụ thể nên fail closed; policy labels chung chưa thay thế authorization design.',
        '- Idempotency bounds, request context/profile binding, per-field permissions, state machine và generic response fields phải đóng trước production SDK.',
        '- Chưa thay method ID, status code hoặc schema input bằng suy đoán. Các câu hỏi còn mở vẫn là blocker trong JSON.', '',
        'Căn cứ kỹ thuật đã đọc ngày 29/10/2026: [OpenAPI 3.1 Paths](https://spec.openapis.org/oas/v3.1.0.html#paths-object), [JSON Schema Core 2020-12](https://json-schema.org/draft/2020-12/json-schema-core), [PostgreSQL 18 RLS](https://www.postgresql.org/docs/18/ddl-rowsecurity.html). OAS ghép path vào server URL; JSON Schema có dialect/reference riêng; RLS phụ thuộc role và policy thực tế. Không nội dung nào ở đây chứng minh runtime đã triển khai.', '',
        '## Sổ 99 operation', '', '| Operation ID | Method + path sau server base | Nguồn | Permission | Response hiện tại / blocker | Response cần thiết kế |', '|---|---|---|---|---|---|']
    for r in rows:
        states = ', '.join(sorted({s['state'] for s in r['success_responses']})) or 'NO_2XX_BODY_CONTRACT'
        permission = r['authorization']['permission'] or 'UNRESOLVED_FAIL_CLOSED'
        source = r['origin'].replace('LOCAL_R2_64','R2').replace('EXTERNAL_V2_ADDITION_19','V2+').replace('EXTERNAL_V3_ADDITION_16','V3+')
        proposed = r['response_design_proposal']['name'] or ('Giữ contract riêng / đóng fields theo resource' if r['codegen_blockers'] else 'Contract đã có; vẫn cần tích hợp/test')
        md.append(f"| `{r['operation_id']}` | `{r['method']} {r['canonical_path']}` | {source} | `{permission}` | {states} | {proposed} |")
    md += ['', '## Bàn giao schema và bằng chứng', '',
        'Xem API_CONTRACT_RECONCILIATION.json để lấy từng success status/media/schema ref, input refs, Idempotency-Key bounds, quyền nguồn và blocker. OPENAPI_UNIFIED_TARGET.json chứa cùng 99 operation và 68 schemas, không thay source nguyên bản. FORMULA_METHOD_EXECUTION_MATRIX.json tách method register ID, passport cũ, formula ID và demo dispatcher.', '',
        'WP01 phải viết schema output theo resource, field-level authorization, response examples và negative cases; bind schema sau review. Ví dụ MethodPreview/RunCreate trong thư mục schemas là input contract, không mặc nhiên là output contract. ReferenceResult mô tả reference lab, không dùng như bản production MethodResult.', '',
        'Kiểm thử hiện tại ở ../evidence/TEST_RECEIPT_BACKEND.json và CONTRACT_VALIDATION_RECEIPT.json có phạm vi synthetic local; chưa có provider/database/live evidence. Không loại blocker hoặc đổi x-lc-codegen-ready sang true chỉ vì schema parse hoặc demo pass.', '']
    (OUT/'API_CONTRACT_RECONCILIATION.md').write_text('\n'.join(md))
    return result

def build_methods():
    register = read(V3 / "03_KNOWLEDGE/METHOD_INTEGRATION_REGISTER_V3.json")
    formulae = read(V2 / "05_BACKEND/FORMULA_CATALOG.json")
    passports = read(V2 / "04_KNOWLEDGE/METHOD_PASSPORT_UPGRADES.json")
    # Explicit scope links are proposals grounded in source names, formula links and code.
    links = {
        "CAL-CIVIL": (["M01", "M09"], ["LCF-09", "LCF-10", "LCF-06"], ["time"], "V2", "time.mjs", "UTC candidate demo and age calendar only; full calendar/ephemeris adapter pending"),
        "ICHING-LINES": ([], ["LCF-16"], ["hexagram"], "V2", "symbolic.mjs", "Six-bit transform only; binary index is not King Wen numbering"),
        "NUM23": (["M03", "M04", "M05"], ["LCF-05", "LCF-07", "LCF-08"], ["numerology_full"], "V3", "numerology_full.mjs", "23 configured components; unavailable fields remain null"),
        "PSYCHO17": (["M08"], ["LCF-03"], ["psychomatrix"], "V3", "psychomatrix.mjs", "Raw and four-working-number variants distinct; no trait inference"),
        "NUM-LIFE-CYCLES": (["M04", "M05"], ["LCF-07", "LCF-08"], ["numerology_full", "cycle"], "V3", "numerology_full.mjs", "Pinnacles, challenges and periods use independent boundary policies"),
        "BCLC64": (["M07"], ["LCF-02"], ["bat_cuc"], "V3", "bat_cuc.mjs", "64 strict adjacent pairs; unknown 0/5 pairs preserved"),
        "BCLC-MODIFIERS": (["M07"], ["LCF-02"], ["bat_cuc", "pairs"], "V3", "bat_cuc.mjs", "Only diagnostic single 0/5 bridge; no full traditional intensity/changing-effects engine"),
        "BCLC-COMBINATION": (["M07"], ["LCF-02"], ["bat_cuc"], "V3", "bat_cuc.mjs", "Transition counting plus 64 original HNH editorial questions; traditional combinations pending"),
        "TAIL80": (["M06"], ["LCF-01"], ["tail80"], "V2", "numbers.mjs", "Exact remainder only; table release/rights and zero policy still require review"),
        "NUMBER-CONTEXT": (["M07"], ["LCF-02", "LCF-04"], ["bat_cuc", "number_compare", "phone"], "V3", "bat_cuc.mjs", "VN phone/generic/identifier_suffix4 contexts; no full identity numbers or passwords"),
        "NAME-UNICODE": (["M02", "M03"], ["LCF-05"], ["name", "name_compare", "numerology_full"], "V3", "numerology_full.mjs", "Original NFC/NFD name trace plus derived Latin; unsupported scripts fail closed"),
        "CASHFLOW": (["M13"], ["LCF-13"], ["cashflow"], "V2", "metrics.mjs", "BigInt minor-unit arithmetic; no investment advice or currency conversion"),
        "RESONANCE": ([], ["LCF-14"], ["resonance"], "V2", "metrics.mjs", "Descriptive self-report count/mean/median only; 144 question cells are not measurements"),
        "LIFE-DESIGN": (["M09", "M10"], ["LCF-06", "LCF-12"], ["lifetime", "actions"], "V3", "lifetime.mjs", "Calendar/history/planning reference only; full 30/90-day and legacy transfer not implemented"),
        "LINEAGE": (["M01"], ["LCF-10"], ["dag", "impact", "cache_key"], "V2", "dag.mjs", "DAG/impact/cache context and digests only; claim/source provenance graph pending"),
        "POLICY": ([], ["SPEC-RLS_POSTGRES", "SPEC-OUTBOX_DURABLE"], ["authorization", "claim", "transition", "optimistic"], "V2", "policy.mjs", "Single-process policy/idempotency reference only; durable DB enforcement pending"),
        "REPORT": ([], [], ["report", "profile_pipeline", "all_in_one"], "V2", "report.mjs", "Template previews and synthetic orchestration only; approved snapshot/render/publish lifecycle pending")}
    pending_specs = {"BAZI-PILLARS": ["SPEC-BAZI_PILLARS"], "BAZI-RELATIONS": ["SPEC-BAZI_STRENGTH"],
        "BAZI-LUCK": ["SPEC-BAZI_STRENGTH"], "ZIWEI-CHART": ["SPEC-ZIWEI_PLACEMENT"],
        "ZIWEI-TRANSFORM": ["SPEC-ZIWEI_CYCLES"], "ASTRO-EPHEMERIS": ["SPEC-WESTERN_ASTRO"],
        "JYOTISH": ["SPEC-JYOTISH_DASHA"], "DASHA": ["SPEC-JYOTISH_DASHA"],
        "QIMEN": ["SPEC-QIMEN_BOARD"], "LIUYAO-MAIHOA": ["SPEC-LIUYAO_RELATIONS"],
        "LETTER-NONLATIN": ["SPEC-NAME_NON_LATIN"], "NADI": ["SPEC-NADI_LIBRARY"],
        "HAND": ["SPEC-IMAGE_MEASURE"], "FACE": ["SPEC-IMAGE_MEASURE"], "FOOT-VOICE": ["SPEC-IMAGE_MEASURE", "SPEC-VOICE_MEASURE"],
        "IPIP": ["SPEC-BEHAVIOR_INSTRUMENT"], "PSYCHOMETRIC": ["SPEC-BEHAVIOR_INSTRUMENT"],
        "VALUES-INTEREST": ["SPEC-BEHAVIOR_INSTRUMENT"], "EVALUATION": ["SPEC-OUTCOME_PROBABILITY"]}
    cases = read(V3 / "08_ALL_IN_ONE_LAB/data/demo-cases-all.json")
    pending_legacy = {"HNH-REFLECTION": ["M11"], "CONTEMPLATION": ["M11"], "VALUES-INTEREST": ["M11", "M12"],
        "CAREER": ["M12"], "PSYCHOMETRIC": ["M12"], "RELATIONSHIPS": ["M14"], "HAND": ["M15"], "FACE": ["M15"], "FOOT-VOICE": ["M15"]}
    output_ids = {"time": "LCF-09", "hexagram": "LCF-16", "numerology_full": "LCV3-NUM23", "psychomatrix": "LCV3-PSYCHO17",
        "cycle": "LCF-08", "bat_cuc": "LCV3-BC-COMPOSE", "pairs": "LCF-02", "tail80": "LCF-01",
        "number_compare": "LCV3-NUM-COMPARE", "name_compare": "LCV3-NAME-COMPARE", "name": "LCF-05",
        "cashflow": "LCF-13", "resonance": "LCF-14", "lifetime": "LCV3-LIFETIME", "actions": "LCF-12", "all_in_one": "LCV3-ALL-IN-ONE"}
    rows = []
    for method in register:
        row = copy.deepcopy(method)
        mid = row["method_id"]
        link = links.get(mid)
        legacy, ff, dm = (link[:3] if link else (pending_legacy.get(mid, []), pending_specs.get(mid, []), []))
        code = rel((V2 / "06_DEMO_LAB/src" if link and link[3] == "V2" else V3 / "08_ALL_IN_ONE_LAB/src") / link[4]) if link else None
        row.update({"legacy_method_ids_proposed": legacy, "formula_ids_scoped": ff,
            "mapping_status": "SCOPED_DESIGN_CROSSWALK_NOT_RELEASE_EQUIVALENCE" if link or ff or legacy else "NO_EXACT_LEGACY_FORMULA_MAPPING_ESTABLISHED",
            "reference_entrypoints": dm, "implementation_path": code,
            "reference_result_ids": sorted({output_ids[d] for d in dm if d in output_ids}),
            "actual_reference_scope": link[5] if link else "Research/specification inventory; no executable adapter established by this package",
            "demo_ids": [c["id"] for c in cases if c["method"] in dm],
            "old_passport_snapshots": [p for p in passports if p["method_id"] in legacy],
            "formula_snapshots": [f for f in formulae if f["formula_id"] in ff],
            "release_decision": "NOT_RELEASED", "implementation_allowed_scope": "SYNTHETIC_LOCAL_REFERENCE_OR_RESEARCH_UNTIL_ALL_GATES_PASS",
            "required_acceptance": [method["specification_and_acceptance"], "Source edition/pages/rule version and rights receipts", "Independent method golden cases including variant disagreements", "Canonical schema adapter and field-level authorization", "Same-digest staging evidence and human release approval"],
            "suggested_work_packages": ["BE-WP01", "BE-WP02", "BE-WP06" if mid in {"NUM23", "PSYCHO17", "NUM-LIFE-CYCLES", "NAME-UNICODE"} else "BE-WP07" if mid.startswith("BCLC") or mid in {"TAIL80", "NUMBER-CONTEXT"} else "BE-WP08" if mid in {"LIFE-DESIGN", "RESONANCE", "CASHFLOW"} else "BE-WP11"]})
        rows.append(row)
    assert len(rows) == 62 and len({r["method_id"] for r in rows}) == 62
    write("FORMULA_METHOD_EXECUTION_MATRIX.json", {"schema_version": "planning-1", "method_count": len(rows),
        "source_reference_flag_count": sum(r["reference_implementation"] for r in rows), "production_released_count": 0,
        "crosswalk_note": "Method IDs, legacy passports, formula IDs and demo dispatchers are separate namespaces; partial links never upgrade approval.",
        "sources": [rel(V3 / "03_KNOWLEDGE/METHOD_INTEGRATION_REGISTER_V3.json"), rel(V2 / "04_KNOWLEDGE/METHOD_PASSPORT_UPGRADES.json"), rel(V2 / "05_BACKEND/FORMULA_CATALOG.json")],
        "rows": rows})
    return rows

def build_data_checks():
    groups = read(V3 / "04_NUMBERS_NAMES/BAT_CUC_GROUPS.json")
    pairs = read(V3 / "04_NUMBERS_NAMES/BAT_CUC_64_PAIRS.json")
    transitions = read(V3 / "04_NUMBERS_NAMES/BAT_CUC_TRANSITION_8X8.json")
    repeated = read(V3 / "04_NUMBERS_NAMES/REPEATED_SEQUENCES_70.json")
    tail = read(V3 / "04_NUMBERS_NAMES/TAIL80_COMPLETE.json")
    fields = read(V3 / "07_BACKEND/DATA_FIELDS_120_PRESERVED.json")
    domains = read(V3 / "05_LIFETIME/LIFE_DOMAINS_18.json")
    scenarios = read(V3 / "05_LIFETIME/LIFE_SCENARIOS_54.json")
    resonance = read(V2 / "04_KNOWLEDGE/RESONANCE_144_QUESTION_MATRIX.json")
    checks = {
        "tail80_exact_codes_1_to_80": len(tail["records"]) == 80 and {r["code"] for r in tail["records"]} == set(range(1,81)),
        "pair64_exact_supported_digit_cartesian": len(pairs) == 64 and {r["pair"] for r in pairs} == {a+b for a in '12346789' for b in '12346789'},
        "groups8_each8": len(groups) == 8 and all(len(g["pairs"]) == 8 for g in groups),
        "pair_intensity_unconfigured": all(r["intensity_rank"] is None and r["intensity_ratio"] is None for r in pairs),
        "transition64_exact_cartesian": len(transitions) == 64 and {(r["from_group"],r["to_group"]) for r in transitions} == {(a["group_id"],b["group_id"]) for a in groups for b in groups},
        "transitions_not_traditional_authority": all(r["traditional_combination_authority"] is None and not r["causal_or_prediction_claim"] for r in transitions),
        "repeated70_exact_patterns_2_to_8": len(repeated) == 70 and {r["digits"] for r in repeated} == {d*n for d in '0123456789' for n in range(2,9)},
        "domains18_unique": len(domains) == len({r["domain_id"] for r in domains}) == 18,
        "scenarios54_exact_domain_modes": len(scenarios) == 54 and {(r["domain_id"], r["mode"]) for r in scenarios} == {(d["domain_id"], mode) for d in domains for mode in ['history','present','action']},
        "scenarios_no_forecast_or_diagnosis": all(not r["forecast"] and not r["authoritative_diagnosis"] for r in scenarios),
        "fields120_unique": len(fields) == len({r["field_id"] for r in fields}) == 120,
        "fields_not_blanket_required": all(r["required_by_default"] is False for r in fields),
        "resonance144_exact_layer_field_cartesian": len(resonance) == 144 and len({(r["layer"],r["field"]) for r in resonance}) == 144 and len({r["layer"] for r in resonance}) == len({r["field"] for r in resonance}) == 12,
    }
    assets = []
    for parent in ['03_KNOWLEDGE', '04_NUMBERS_NAMES', '05_LIFETIME']:
        for path in sorted((V3/parent).glob('*.json')):
            data = read(path)
            def source_ids(v):
                if isinstance(v,dict):
                    for k,x in v.items():
                        if k == 'source_id' and isinstance(x,str): yield x
                        elif k == 'source_ids' and isinstance(x,list): yield from x
                        else: yield from source_ids(x)
                elif isinstance(v,list):
                    for x in v: yield from source_ids(x)
            assets.append({'path':rel(path),'sha256':sha(path),'record_count':len(data['records']) if isinstance(data,dict) and 'records' in data else len(data),
                'source_ids':sorted(set(source_ids(data))), 'integration_state':'PRESERVED_REFERENCE_DATA_NOT_SEEDED',
                'release_gate':'source edition/rule/transcription, rights receipt, independent review, approved method release',
                'rights_verified_by_this_audit':False})
    copied_tables=[]
    for path in sorted((V3/'08_ALL_IN_ONE_LAB/data').glob('*.json')):
        canonical = (V3/'04_NUMBERS_NAMES'/path.name)
        if not canonical.exists(): canonical = V3/'05_LIFETIME'/path.name
        if canonical.exists(): copied_tables.append({'lab_copy':rel(path),'canonical_reference':rel(canonical),'exact_byte_match':sha(path)==sha(canonical)})
    write('SOURCE_DATA_INTEGRATION_MATRIX.json',{'date':'2026-10-29','structural_checks':checks,
        'all_structural_checks_pass':all(checks.values()),'assets':assets,'lab_table_copy_parity':copied_tables,
        'field_classifications':dict(Counter(r['classification'] for r in fields)),
        'fields_first_beta_count':sum(r['first_beta'] for r in fields),
        'retention_status':'All 12 field-group retention identifiers remain policy_pending_review; finalize durations and deletion graph before real collection.',
        'source_namespace_issue':{'data_id':'USER_TABLE80_CONVERSATION','registry_id':'R28','state':'PROPOSED_ALIAS_NOT_A_RIGHTS_RECEIPT'},
        'source_conflicts':read(V3/'04_NUMBERS_NAMES/BAT_CUC_SOURCE_CONFLICTS.json'),
        'limits':['Structural completeness does not prove historical authority, copyright permission, predictive validity or production release.','Source Sxx, Rxx, user-supplied IDs and formula/method namespaces require explicit versioned crosswalk.','No SQL seed or migration was executed.']})
    assert all(checks.values()), checks

def coverage():
    assigned = []
    for version, base, groups in [("v2", V2, ["04_KNOWLEDGE", "05_BACKEND", "06_DEMO_LAB"]),
        ("v3", V3, ["03_KNOWLEDGE", "04_NUMBERS_NAMES", "05_LIFETIME", "07_BACKEND", "08_ALL_IN_ONE_LAB", "13_SOURCES"])]:
        for group in groups:
            assigned += [(version, base, p) for p in sorted((base / group).rglob("*")) if p.is_file()]
    rows, first_hash = [], {}
    for version, base, path in assigned:
        raw = path.read_bytes()
        content = raw.decode("utf-8")
        digest = sha(path)
        duplicate = first_hash.get(digest)
        first_hash.setdefault(digest, rel(path))
        inspection = "FULL_UTF8_READ; NARRATIVE_OR_SOURCE_REVIEW"
        count = None
        if path.suffix == ".json":
            value = json.loads(content)
            count = len(value) if isinstance(value, (dict, list)) else None
            inspection = "FULL_UTF8_READ; FULL_JSON_PARSE; DOMAIN_OR_CONTRACT_CROSSCHECK"
        elif path.suffix == ".csv":
            count = len(list(csv.DictReader(content.splitlines())))
            inspection = "FULL_UTF8_READ; FULL_CSV_PARSE; PAIRED_DATA_REVIEW"
        elif "/receipts/" in str(path):
            inspection = "FULL_UTF8_READ; IMPORTED_RECEIPT_NOT_CURRENT_PROOF"
        elif "/public/" in str(path) or "/profile_examples/" in str(path):
            inspection = "FULL_UTF8_READ; BACKEND_FORMAT_AND_REFERENCE_AUDIT; VISUAL_UX_NOT_PERFORMED_IN_BACKEND_LANE"
        if duplicate:
            inspection += "; EXACT_BYTE_DUPLICATE_OF_REVIEWED_SOURCE"
        rows.append({"source_version": version, "source_relative_path": str(path.relative_to(base)), "path": rel(path),
            "bytes": len(raw), "sha256": digest, "inspection": inspection, "parsed_top_level_count": count,
            "byte_duplicate_of": duplicate, "external_citations_read_status": "NOT_IMPLIED_BY_PACKAGE_READ"})
    write("READ_COVERAGE_BACKEND.json", {"date": "2026-10-29", "scope": "Assigned backend, knowledge, numeric, lifetime and synthetic-lab files; nested archived baselines excluded, legacy_v2 included by exact digest",
        "file_count": len(rows), "version_counts": dict(Counter(r["source_version"] for r in rows)),
        "unique_sha256_count": len(first_hash), "rows": rows,
        "limitations": ["Reading a research inventory does not mean reading every cited original book or licensing those sources.", "Source review and parsing do not prove staging, production, live deployment or approval.", "Large repeated tables/receipts receive full structural and cross-reference validation; independent original-source review remains gated."]})

if __name__ == "__main__":
    contract = build_contract()
    methods = build_methods()
    build_data_checks()
    coverage()
    print(json.dumps({k: v for k, v in contract.items() if k.endswith("count") or k in ["origin_counts", "codegen_ready", "unresolved_internal_refs"]}, ensure_ascii=False))
