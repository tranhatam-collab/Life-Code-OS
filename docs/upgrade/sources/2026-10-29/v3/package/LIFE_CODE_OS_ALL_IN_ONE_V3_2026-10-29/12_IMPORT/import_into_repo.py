#!/usr/bin/env python3
"""Add a verified delivery to the correct clean review repository. Dry-run by default."""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,re,shutil,subprocess,sys
from pathlib import Path
sys.dont_write_bytecode = True
TARGET='docs/upgrades/2026-10-29-v3'
EXPECTED='tranhatam-collab/Life-Code-OS'

def git(repo:Path,*args:str)->str:
    r=subprocess.run(['git','-C',str(repo),*args],capture_output=True,text=True,timeout=20)
    if r.returncode:raise ValueError('Git check failed: '+r.stderr.strip())
    return r.stdout.strip()

def remote_name(url:str)->str:
    u=url.rstrip('/')
    if u.endswith('.git'):u=u[:-4]
    m=re.fullmatch(r'(?:git@github\.com:|https://github\.com/|ssh://git@github\.com/)([^/]+/[^/]+)',u)
    if not m:raise ValueError('Unsupported GitHub remote URL; no credentials or alternate hosts allowed.')
    return m.group(1)

def preflight(package:Path,repo:Path)->dict:
    if package.is_symlink() or repo.is_symlink():raise ValueError('Root symlinks are not allowed.')
    package=package.resolve();repo=repo.resolve()
    spec=importlib.util.spec_from_file_location('lc_manifest_verify',package/'VERIFY_PACKAGE.py')
    if spec is None or spec.loader is None:raise ValueError('Verifier not found.')
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    report=mod.verify(package)
    if report['status']!='PASS':raise ValueError('Package integrity failed: '+json.dumps(report['errors'][:5]))
    top=Path(git(repo,'rev-parse','--show-toplevel')).resolve()
    if repo!=top:raise ValueError('--repo must point to the repository root.')
    if remote_name(git(repo,'remote','get-url','origin'))!=EXPECTED:raise ValueError('Incorrect project remote.')
    branch=git(repo,'branch','--show-current')
    if not branch or branch.lower() in {'main','master','production'}:raise ValueError('A named review branch is required; protected release branches are refused.')
    if git(repo,'status','--porcelain'):raise ValueError('Repository must be clean before import.')
    if package==repo or repo in package.parents:raise ValueError('Use a package outside the target repository.')
    dest=repo/TARGET
    for p in [dest,*dest.parents]:
        if p.is_symlink():raise ValueError('Destination contains a symlink.')
        if p==repo:break
    manifest=json.loads((package/'MANIFEST.json').read_text())
    entries=manifest['files']+[{'path':'MANIFEST.json','sha256':hashlib.sha256((package/'MANIFEST.json').read_bytes()).hexdigest(),'bytes':(package/'MANIFEST.json').stat().st_size}]
    plan=[]
    for e in entries:
        mod.safe_relative(e['path']);src=package/e['path'];dst=dest/e['path']
        for p in [dst,*dst.parents]:
            if p.is_symlink():raise ValueError('Destination contains a symlink: '+str(p))
            if p==repo:break
        state='ADD'
        if dst.exists():
            if not dst.is_file() or hashlib.sha256(dst.read_bytes()).hexdigest()!=e['sha256']:raise ValueError('Refusing differing existing file: '+str(dst))
            state='IDENTICAL_SKIP'
        plan.append({'path':e['path'],'action':state,'sha256':e['sha256'],'bytes':e['bytes']})
    return {'project':EXPECTED,'branch':branch,'head':git(repo,'rev-parse','HEAD'),'target':TARGET,'plan':plan,'files':len(plan)}

def apply(package:Path,repo:Path,plan:dict)->dict:
    # Re-run all checks immediately before write; no overwrite operation exists.
    fresh=preflight(package,repo)
    if fresh!=plan:raise ValueError('Preflight changed; review again.')
    dest=repo/TARGET;added=skipped=0
    for row in plan['plan']:
        src=package/row['path'];dst=dest/row['path']
        if row['action']=='IDENTICAL_SKIP':skipped+=1;continue
        dst.parent.mkdir(parents=True,exist_ok=True)
        with src.open('rb') as fi,dst.open('xb') as fo:shutil.copyfileobj(fi,fo)
        if hashlib.sha256(dst.read_bytes()).hexdigest()!=row['sha256']:raise ValueError('Post-copy hash mismatch: '+str(dst))
        added+=1
    return {'status':'COPIED_NOT_COMMITTED','added':added,'identical_skipped':skipped,'target':str(dest),'commit':False,'push':False,'deploy':False}

def main()->int:
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--repo',required=True,type=Path);ap.add_argument('--package',type=Path,default=Path(__file__).resolve().parents[1]);ap.add_argument('--apply',action='store_true')
    a=ap.parse_args()
    try:
        plan=preflight(a.package,a.repo)
        result=apply(a.package.resolve(),a.repo.resolve(),plan) if a.apply else {'status':'DRY_RUN','project':plan['project'],'branch':plan['branch'],'head':plan['head'],'target':plan['target'],'files':plan['files'],'add':sum(x['action']=='ADD' for x in plan['plan']),'identical_skip':sum(x['action']=='IDENTICAL_SKIP' for x in plan['plan']),'sample_paths':[x['path'] for x in plan['plan'][:12]],'writes':False}
        print(json.dumps(result,ensure_ascii=False,indent=2));return 0
    except Exception as e:print(json.dumps({'status':'REFUSED','error':str(e)},ensure_ascii=False,indent=2));return 1
if __name__=='__main__':sys.exit(main())
