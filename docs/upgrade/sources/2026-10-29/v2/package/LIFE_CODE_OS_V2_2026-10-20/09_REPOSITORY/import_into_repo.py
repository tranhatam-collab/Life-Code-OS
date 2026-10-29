#!/usr/bin/env python3
"""Add the reviewed delivery under docs/. Default: verify and report only.
No network, deletion, overwrite, git add, commit, push or deployment.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

TARGET = Path('docs/upgrades/2026-10-20-v2')
EXPECTED_REPO = 'tranhatam-collab/life-code-os'

class ImportRejected(ValueError):
    pass

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

def git(repo: Path, *args: str) -> str:
    result = subprocess.run(['git', '-C', str(repo), *args], capture_output=True, text=True)
    if result.returncode:
        raise ImportRejected('Không đọc được Git: ' + ' '.join(args))
    return result.stdout.strip()

def normalize_remote(remote: str) -> str:
    if re.fullmatch(r'git@github\.com:[^/]+/[^/]+(?:\.git)?', remote):
        value = remote.split(':', 1)[1]
    elif re.fullmatch(r'https://github\.com/[^/]+/[^/]+(?:\.git)?/?', remote):
        value = remote.removeprefix('https://github.com/').rstrip('/')
    else:
        raise ImportRejected('Remote không thuộc dạng GitHub SSH/HTTPS được hỗ trợ.')
    return value.removesuffix('.git').lower()

def assert_no_symlink(path: Path, boundary: Path) -> None:
    current = path
    while True:
        if current.is_symlink():
            raise ImportRejected('Phát hiện symbolic link trong đường đích: ' + str(current))
        if current == boundary:
            break
        if boundary not in current.parents:
            raise ImportRejected('Đường dẫn ra ngoài thư mục repository.')
        current = current.parent

def manifest_files(package: Path) -> list[dict]:
    manifest = package / 'MANIFEST.json'
    if not manifest.is_file():
        raise ImportRejected('Thiếu MANIFEST.json; không nhập gói chưa được chốt.')
    try:
        data = json.loads(manifest.read_text(encoding='utf-8'))
        rows = data['files']
    except (ValueError, KeyError, TypeError) as exc:
        raise ImportRejected('Manifest không hợp lệ.') from exc
    if not isinstance(rows, list) or not rows:
        raise ImportRejected('Manifest không có danh sách tệp.')
    seen = set()
    for row in rows:
        rel = Path(row['path'])
        if rel.is_absolute() or '..' in rel.parts or '.git' in rel.parts or str(rel) in seen:
            raise ImportRejected('Đường dẫn manifest không an toàn hoặc bị trùng.')
        seen.add(str(rel))
        src = package / rel
        assert_no_symlink(src, package)
        if not src.is_file() or sha256(src) != row['sha256']:
            raise ImportRejected('Checksum không khớp: ' + str(rel))
    actual = {str(p.relative_to(package)) for p in package.rglob('*') if p.is_file() and p.name != 'MANIFEST.json'}
    # Only the root manifest is excluded. A baseline manifest is a regular preserved file.
    actual = {str(p.relative_to(package)) for p in package.rglob('*') if p.is_file() and p != manifest}
    if actual != seen:
        raise ImportRejected('Danh sách tệp thực tế khác manifest; hãy dùng gói nguyên vẹn.')
    return rows + [{'path': 'MANIFEST.json', 'sha256': sha256(manifest)}]

def import_package(repo: Path, package: Path, apply: bool = False) -> dict:
    repo, package = repo.resolve(), package.resolve()
    if normalize_remote(git(repo, 'remote', 'get-url', 'origin')) != EXPECTED_REPO:
        raise ImportRejected('Sai dự án. Chỉ cho phép tranhatam-collab/Life-Code-OS.')
    branch = git(repo, 'symbolic-ref', '--short', 'HEAD')
    if branch in {'main', 'master', 'production'}:
        raise ImportRejected('Không nhập trực tiếp vào nhánh chính/production.')
    if git(repo, 'status', '--porcelain'):
        raise ImportRejected('Worktree chưa sạch. Bảo toàn thay đổi hiện có trước khi nhập.')
    rows = manifest_files(package)
    destination = repo / TARGET
    pending, identical, conflicts = [], [], []
    for row in rows:
        dst = destination / row['path']
        assert_no_symlink(dst, repo)
        if dst.exists():
            if dst.is_file() and sha256(dst) == row['sha256']:
                identical.append(row['path'])
            else:
                conflicts.append(row['path'])
        else:
            pending.append(row['path'])
    if conflicts:
        raise ImportRejected('Có tệp đích khác nội dung; không ghi đè: ' + ', '.join(conflicts[:10]))
    if apply:
        for rel in pending:
            dst = destination / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            # Recheck immediately before write; still requires an exclusive local worktree.
            assert_no_symlink(dst, repo)
            if dst.exists():
                raise ImportRejected('Đích thay đổi trong lúc nhập; dừng để đối soát: ' + rel)
            with (package / rel).open('rb') as source, dst.open('xb') as target:
                shutil.copyfileobj(source, target)
        for row in rows:
            if sha256(destination / row['path']) != row['sha256']:
                raise ImportRejected('Đối soát sau nhập thất bại: ' + row['path'])
    return {'repository': EXPECTED_REPO, 'branch': branch, 'target': str(TARGET),
            'mode': 'APPLIED_FILES_ONLY' if apply else 'DRY_RUN',
            'verified_files': len(rows), 'new_files': len(pending), 'identical_files': len(identical),
            'overwritten_files': 0, 'deleted_files': 0, 'committed': False, 'pushed': False, 'deployed': False}

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', required=True, type=Path)
    parser.add_argument('--package', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--apply', action='store_true', help='Chỉ sao chép sau khi toàn bộ preflight đạt.')
    args = parser.parse_args()
    try:
        result = import_package(args.repo, args.package, args.apply)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ImportRejected, OSError, KeyError, TypeError) as exc:
        print(json.dumps({'status':'REJECTED', 'message':str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2

if __name__ == '__main__':
    raise SystemExit(main())
