#!/usr/bin/env python3
"""Verify an unmodified Life Code delivery; never executes packaged code."""
from __future__ import annotations
import argparse, hashlib, json, sys
from pathlib import Path, PurePosixPath

def safe_relative(value: str) -> PurePosixPath:
    p=PurePosixPath(value)
    if not value or p.is_absolute() or '..' in p.parts or '\\' in value or p.as_posix()!=value:
        raise ValueError(f'Unsafe manifest path: {value!r}')
    return p

def verify(root: Path, *, reject_unlisted: bool=True) -> dict:
    root=root.resolve()
    manifest_path=root/'MANIFEST.json'
    if manifest_path.is_symlink(): raise ValueError('Manifest must not be a symlink.')
    data=json.loads(manifest_path.read_text(encoding='utf-8'))
    expected={};errors=[]
    for entry in data['files']:
        rel=safe_relative(entry['path']).as_posix()
        if rel in expected: raise ValueError(f'Duplicate manifest path: {rel}')
        expected[rel]=entry
        p=root/rel
        if any(x.is_symlink() for x in [p,*p.parents] if x!=root.parent):
            errors.append({'path':rel,'error':'symlink'});continue
        if not p.is_file():errors.append({'path':rel,'error':'missing'});continue
        raw=p.read_bytes()
        if len(raw)!=entry['bytes'] or hashlib.sha256(raw).hexdigest()!=entry['sha256']:
            errors.append({'path':rel,'error':'hash_or_size_mismatch'})
    actual=set()
    for p in root.rglob('*'):
        if p.is_symlink():errors.append({'path':str(p.relative_to(root)),'error':'symlink'})
        elif p.is_file() and p.relative_to(root).as_posix()!='MANIFEST.json':actual.add(p.relative_to(root).as_posix())
    if reject_unlisted:
        for rel in sorted(actual-set(expected)): errors.append({'path':rel,'error':'unlisted'})
    return {'status':'PASS' if not errors else 'FAIL','files_expected':len(expected),'files_present':len(actual),'errors':errors,'manifest_excluded_from_self_hash':True}

def main()->int:
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parent)
    a=ap.parse_args()
    try:r=verify(a.root)
    except Exception as e:print(json.dumps({'status':'FAIL','error':str(e)},ensure_ascii=False));return 1
    print(json.dumps(r,ensure_ascii=False,indent=2));return 0 if r['status']=='PASS' else 1
if __name__=='__main__':sys.exit(main())
