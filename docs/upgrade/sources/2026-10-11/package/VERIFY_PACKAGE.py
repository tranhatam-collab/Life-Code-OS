"""Verify package digests locally. No network calls, no source execution."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
manifest = json.loads((root / "MANIFEST.json").read_text(encoding="utf-8"))
failures = []
for item in manifest["files"]:
    rel = Path(item["path"])
    path = (root / rel).resolve()
    if rel.is_absolute() or root not in path.parents or not path.is_file():
        failures.append(item["path"] + ": invalid or missing path")
        continue
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != item["sha256"]:
        failures.append(item["path"] + ": digest mismatch")
print("Checked", len(manifest["files"]), "files.")
for failure in failures:
    print("FAIL", failure)
if failures:
    raise SystemExit(1)
print("PASS: package file integrity. This does not certify production readiness.")
