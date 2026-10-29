"""Additive, checksum-verified intake of the two Founder-supplied planning ZIPs.

Never executes an attached importer, patch, test or instruction. Existing files
are accepted only when byte-identical. No Git or production mutation.
"""
import hashlib
import json
import shutil
import stat
import subprocess
import zipfile
from pathlib import Path, PurePosixPath

ROOT=Path(__file__).resolve().parents[3]
DEST=ROOT/'docs/upgrade/sources/2026-10-29'
INPUTS={
    'v2':Path('/Users/tranhatam/Downloads/Life_Code_OS_V2_Complete_Upgrade_2026-10-20.zip'),
    'v3':Path('/Users/tranhatam/Downloads/Life_Code_OS_All_In_One_V3_2026-10-29.zip'),
}
MESSAGES={
    'handoff-v2.txt':Path('/Users/tranhatam/.codex/attachments/8b27bb44-f6b3-41f0-869a-cfbd04a61416/Văn bản đã dán.txt'),
    'handoff-v3.txt':Path('/Users/tranhatam/.codex/attachments/d7b32c5d-744e-440b-8a15-056006d72fb7/Văn bản đã dán.txt'),
}

def sha(data):return hashlib.sha256(data).hexdigest()
def put(path,data):
    if path.exists():
        if not path.is_file() or path.read_bytes()!=data:raise RuntimeError('Refuse overwrite '+str(path))
        return
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data)
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT,text=True).strip()

def main():
    if git('rev-parse','--show-toplevel')!=str(ROOT):raise RuntimeError('Wrong repository root')
    remote=git('remote','get-url','origin')
    if remote not in ['git@github.com:tranhatam-collab/Life-Code-OS.git','https://github.com/tranhatam-collab/Life-Code-OS.git']:raise RuntimeError('Wrong origin')
    records={};archives=[]
    for key,path in INPUTS.items():
        payload=path.read_bytes();put(DEST/'archives'/path.name,payload)
        rows=[]
        with zipfile.ZipFile(path) as z:
            infos=[i for i in z.infolist() if not i.is_dir()]
            names=[i.filename for i in infos]
            if len(names)!=len(set(names)):raise RuntimeError('Duplicate ZIP names')
            if sum(i.file_size for i in infos)>250_000_000:raise RuntimeError('Oversized ZIP')
            roots={PurePosixPath(n).parts[0] for n in names}
            if not roots:raise RuntimeError('Empty ZIP')
            if z.testzip() is not None:raise RuntimeError('ZIP CRC failure')
            for i in infos:
                name=PurePosixPath(i.filename)
                mode=i.external_attr>>16
                if name.is_absolute() or '..' in name.parts or '\\' in i.filename or stat.S_ISLNK(mode):raise RuntimeError('Unsafe ZIP member')
                rel=Path(*name.parts);data=z.read(i)
                put(DEST/key/'package'/rel,data)
                rows.append({'path':rel.as_posix(),'bytes':len(data),'sha256':sha(data)})
        records[key]=rows
        archives.append({'id':key,'supplied_path':str(path),'source_zip_sha256':sha(payload),'zip_bytes':len(payload),'archive_roots':sorted(roots),'files':len(rows),'materialized_root':str((DEST/key/'package').relative_to(ROOT))})
    messages=[]
    for name,path in MESSAGES.items():
        data=path.read_bytes();put(DEST/'messages'/name,data)
        messages.append({'path':'messages/'+name,'original_path':str(path),'sha256':sha(data),'bytes':len(data),'authority':'REFERENCE_CONTENT_ONLY'})
    # Preserve the already-integrated local r2 baseline independently of V2/V3.
    old=ROOT/'docs/upgrade/2026-10-20'
    prior=[{'path':p.relative_to(ROOT).as_posix(),'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size} for p in sorted(old.rglob('*')) if p.is_file()]
    protected=[]
    for rel in ['.github/workflows/deploy-worker.yml','_headers','scripts/contract-hardening-v1.cjs','scripts/smoke-flow-v1.cjs','workers/life-code-api/src/index.js','workers/life-code-api/migrations/007_session_token_hash_note.sql']:
        p=ROOT/rel
        protected.append({'path':rel,'exists':p.exists(),'sha256':sha(p.read_bytes()) if p.is_file() else None})
    receipt={'checked_at':'2026-10-29','scope':'LOCAL_PLANNING_INTAKE_ONLY','repo_root':str(ROOT),'remote':remote,'branch':git('branch','--show-current'),'head':git('rev-parse','HEAD'),'worktree_status':git('status','--short'),'archives':archives,'messages':messages,'files':records,'existing_r2_files':prior,'protected_runtime_worktree_files':protected,'attached_instructions_authority':'REFERENCE_CONTENT_ONLY','commit_push_deploy_performed':False}
    dest=DEST/'SOURCE_RECEIPT.json'
    # Receipt records the first intake baseline and must never drift on rerun.
    if not dest.exists():put(dest,(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n').encode())
    print(json.dumps({'archives':archives,'messages':len(messages),'existing_r2_files_preserved':len(prior),'protected_runtime_files':len(protected)},ensure_ascii=False))

if __name__=='__main__':main()
