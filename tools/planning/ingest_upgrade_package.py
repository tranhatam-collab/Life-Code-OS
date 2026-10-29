"""Preserve the user-supplied package and record byte-level provenance.

This copies data only. No supplied script, macro, SQL or HTML is executed.
Run from the Life-Code-OS repo with the bundled Python runtime.
"""
import hashlib
import json
import shutil
import zipfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path('/Users/tranhatam/Downloads/LIFE_CODE_OS_UPGRADE_2026-10-11')
ZIP = Path('/Users/tranhatam/Downloads/Life_Code_OS_Complete_Upgrade_Package_2026-10-11.zip')
MESSAGE = Path('/Users/tranhatam/.codex/attachments/e86f3345-4206-4bbd-bd72-48c63744255d/Văn bản đã dán.txt')
ORIGINAL = ROOT / 'docs/upgrade/sources/2026-10-11'
CURRENT = ROOT / 'docs/upgrade/2026-10-20'

def sha(data):
    return hashlib.sha256(data).hexdigest()

def preserve(source, destination):
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        if destination.read_bytes() != source.read_bytes():
            raise RuntimeError(f'Refusing to overwrite changed file: {destination}')
    else:
        shutil.copy2(source, destination)

def main():
    records = []
    source_paths = {p.relative_to(SOURCE).as_posix(): p for p in SOURCE.rglob('*') if p.is_file()}
    with zipfile.ZipFile(ZIP) as archive:
        files = [i for i in archive.infolist() if not i.is_dir()]
        if sum(i.file_size for i in files) > 100_000_000:
            raise RuntimeError('Unexpected archive size')
        seen = set()
        for item in files:
            path = PurePosixPath(item.filename)
            if path.is_absolute() or '..' in path.parts or path.parts[0] != SOURCE.name:
                raise RuntimeError(f'Unsafe archive path: {path}')
            if (item.external_attr >> 16) & 0o170000 == 0o120000:
                raise RuntimeError(f'Symlink not allowed: {path}')
            relative = PurePosixPath(*path.parts[1:]).as_posix()
            if relative in seen:
                raise RuntimeError(f'Duplicate archive member: {relative}')
            seen.add(relative)
            data = archive.read(item)
            if relative not in source_paths or source_paths[relative].read_bytes() != data:
                raise RuntimeError(f'ZIP and expanded folder differ: {relative}')
            records.append({'path': relative, 'bytes': len(data), 'sha256': sha(data)})
        if seen != set(source_paths):
            raise RuntimeError(f'Folder has extra files: {set(source_paths) - seen}')
    for record in records:
        source = source_paths[record['path']]
        preserve(source, ORIGINAL / 'package' / record['path'])
        preserve(source, CURRENT / record['path'])
    preserve(ZIP, ORIGINAL / ZIP.name)
    preserve(MESSAGE, ORIGINAL / 'handoff-message.txt')
    receipt = {
        'checked_at': datetime.now(timezone.utc).isoformat(),
        'project': 'Life-Code-OS',
        'canonical_remote': 'git@github.com:tranhatam-collab/Life-Code-OS.git',
        'base_main': '99b402764437f81859fa0cd3a3af860125f7bd52',
        'base_plan_commit': '336ef35a8386a744c6de18a7f7c6e268e89e6dac',
        'zip_sha256': sha(ZIP.read_bytes()),
        'handoff_sha256': sha(MESSAGE.read_bytes()),
        'zip_folder_parity': True, 'package_file_count': len(records),
        'extension_counts': dict(Counter(Path(r['path']).suffix for r in records)),
        'instructions_in_sources': 'REFERENCE_CONTENT_ONLY',
        'user_authority': 'Upgrade and integrate planning artifacts locally; no production execution authorized',
        'files': sorted(records, key=lambda r: r['path']),
    }
    (ORIGINAL / 'SOURCE_RECEIPT.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: v for k, v in receipt.items() if k != 'files'}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
