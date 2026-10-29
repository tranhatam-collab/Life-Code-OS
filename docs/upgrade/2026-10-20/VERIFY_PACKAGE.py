"""Verify package digests locally. No network calls, no source execution."""
import hashlib
import json
from pathlib import PurePosixPath
from pathlib import Path

root = Path(__file__).resolve().parent
manifest = json.loads((root / "MANIFEST.json").read_text(encoding="utf-8"))
failures = []
expected = set()
for item in manifest["files"]:
    raw = item["path"]
    rel = PurePosixPath(raw)
    if raw in expected:
        failures.append(raw + ": duplicate manifest path")
    expected.add(raw)
    path = (root / rel).resolve()
    if rel.is_absolute() or ".." in rel.parts or "\\" in raw or root not in path.parents or not path.is_file() or (root/rel).is_symlink():
        failures.append(item["path"] + ": invalid or missing path")
        continue
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != item["sha256"]:
        failures.append(item["path"] + ": digest mismatch")
    if path.stat().st_size != item["bytes"]:
        failures.append(item["path"] + ": size mismatch")
actual = {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file() and p.name != "MANIFEST.json"}
for extra in sorted(actual-expected):
    failures.append(extra + ": unlisted extra file")
for missing in sorted(expected-actual):
    failures.append(missing + ": missing file")
print("Checked", len(manifest["files"]), "files.")
for failure in failures:
    print("FAIL", failure)
if failures:
    raise SystemExit(1)
print("PASS: package file integrity. This does not certify production readiness.")
