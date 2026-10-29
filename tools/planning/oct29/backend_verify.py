#!/usr/bin/env python3
"""Run supplied reference suites in isolated copies and record bounded evidence."""
from __future__ import annotations
import datetime as dt
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "docs/upgrade/sources/2026-10-29"
V2 = SOURCE / "v2/package/LIFE_CODE_OS_V2_2026-10-20"
V3 = SOURCE / "v3/package/LIFE_CODE_OS_ALL_IN_ONE_V3_2026-10-29"
# Verification always writes outside the repository. The documentation lane may
# separately copy reviewed receipts into its authorized output directory.
OUT = Path(tempfile.mkdtemp(prefix="lc-os-oct29-backend-evidence-", dir="/private/tmp"))
NODE = Path("/Users/tranhatam/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node")

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def run(name, args, cwd):
    try:
        result = subprocess.run(args, cwd=cwd, text=True, capture_output=True, timeout=30)
        text = result.stdout + result.stderr
        exit_code = result.returncode
    except subprocess.TimeoutExpired as error:
        text = (error.stdout or b"").decode() if isinstance(error.stdout, bytes) else (error.stdout or "")
        text += "\nTIMEOUT: isolated verification process exceeded 30 seconds.\n"
        exit_code = 124
    (OUT / "evidence" / f"{name}.log").write_text(text)
    stats = {k: int(v) for k, v in re.findall(r"^# (tests|pass|fail|cancelled|skipped|todo) (\d+)$", text, re.M)}
    return {"name": name, "command": [str(x) for x in args], "cwd": str(cwd), "exit_code": exit_code,
        "statistics": stats, "log": str(OUT / "evidence" / f"{name}.log"),
        "scope": "LOCAL_SYNTHETIC_REFERENCE_ONLY", "production_calls": 0}

def schema_examples():
    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ImportError:
        return {"status": "NOT_RUN_DEPENDENCY_UNAVAILABLE", "example_count": 27, "note": "Never substitute hand-rolled subset checks for JSON Schema validation."}
    rows = []
    for label, base in [("V2", V2 / "05_BACKEND"), ("V3", V3 / "07_BACKEND")]:
        for schema_path in sorted((base / "schemas").glob("*.schema.json")):
            schema = json.loads(schema_path.read_text())
            Draft202012Validator.check_schema(schema)
            example_path = base / "examples" / schema_path.name.replace(".schema", "")
            if not example_path.is_file():
                rows.append({"source": label, "schema": str(schema_path.relative_to(ROOT)), "status": "NO_SUPPLIED_EXAMPLE"})
                continue
            example = json.loads(example_path.read_text())
            validator = Draft202012Validator(schema, format_checker=FormatChecker())
            errors = sorted(validator.iter_errors(example), key=lambda x: str(x.path))
            rows.append({"source": label, "schema": str(schema_path.relative_to(ROOT)), "example": str(example_path.relative_to(ROOT)),
                "status": "FAIL" if errors else "PASS", "errors": [{"path": list(e.path), "validator": e.validator, "message": e.message} for e in errors]})
    return {"status": "EXECUTED", "validator": "jsonschema Draft202012Validator with FormatChecker", "rows": rows,
        "passed_examples": sum(r["status"] == "PASS" for r in rows), "failed_examples": sum(r["status"] == "FAIL" for r in rows),
        "missing_examples": sum(r["status"] == "NO_SUPPLIED_EXAMPLE" for r in rows)}

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "evidence").mkdir(exist_ok=True)
    before = {str(p): digest(p) for b in [V2 / "06_DEMO_LAB", V3 / "08_ALL_IN_ONE_LAB"] for p in b.rglob("*") if p.is_file()}
    work = Path(tempfile.mkdtemp(prefix="lc-os-oct29-backend-", dir="/private/tmp"))
    for name, source in [("v2", V2 / "06_DEMO_LAB"), ("v3", V3 / "08_ALL_IN_ONE_LAB")]:
        shutil.copytree(source, work / name)
    suites = []
    for name, target in [("v2_supplied", "v2"), ("v3_supplied", "v3")]:
        cwd = work / target
        suites.append(run(name, [str(NODE), "--test", "--test-reporter=tap", "--test-timeout=15000", *[str(p.relative_to(cwd)) for p in sorted((cwd / "tests").glob("*.test.mjs"))]], cwd))
    suites.append(run("v3_legacy_supplied", [str(NODE), "--test", "--test-reporter=tap", "--test-timeout=15000", *[str(p.relative_to(work / "v3")) for p in sorted((work / "v3/legacy_v2/tests").glob("*.test.mjs"))]], work / "v3"))
    suites.append(run("v2_demo_replay", [str(NODE), "tools/run-demos.mjs"], work / "v2"))
    suites.append(run("v3_demo_replay", [str(NODE), "tools/run-cases.mjs"], work / "v3"))
    receipt_files = [(work / "v2/receipts/demo-results.json", "v2_demo_results_current.json"),
        (work / "v3/receipts/demo-results-v3.json", "v3_demo_results_current.json")]
    replay_receipts = []
    for path, target in receipt_files:
        shutil.copy2(path, OUT / "evidence" / target)
        replay_receipts.append({"path": str(OUT / "evidence" / target), "sha256": digest(path)})
    mutation = [path for path, prior in before.items() if digest(Path(path)) != prior]
    receipt = {"checked_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(), "node": subprocess.check_output([str(NODE), "--version"], text=True).strip(),
        "temp_directory": str(work), "source_files_checked_unchanged": len(before), "source_mutation_paths": mutation,
        "suites": suites, "schema_examples": schema_examples(), "replay_receipts": replay_receipts,
        "production_ready": False, "evidence_scope": "Fresh local synthetic test execution; no database, provider, production, source licensing or predictive validity evidence.",
        "earlier_attempt": {"status": "TIMED_OUT", "scope": "Initial combined V2 core/http invocation under restricted sandbox", "timeout_seconds": 90, "detail": "Core-only follow-up passed 118/118. Initial combined HTTP result was not accepted as a pass. Final execution is bounded with explicit TAP reporter."},
        "not_run": ["Production/staging database migrations", "Real runtime RLS/tenant isolation", "Queue crash/recovery and durable idempotency", "AI provider or payment integration", "Independent method source review", "Device/browser visual or load/SLA tests"]}
    (OUT / "TEST_RECEIPT_BACKEND.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
    assert not mutation, mutation
    assert all(s["exit_code"] == 0 for s in suites), suites
    print(json.dumps({"receipt_directory": str(OUT), "suites": [{"name": s["name"], "exit_code": s["exit_code"], "statistics": s["statistics"]} for s in suites], "schema_examples": {k:v for k,v in receipt["schema_examples"].items() if k != "rows"}, "source_mutations": len(mutation)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
