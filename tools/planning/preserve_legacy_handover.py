"""Copy prior local planning files as historical references without modifying that lane."""
import hashlib
import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OTHER = Path('/Users/tranhatam/Library/Mobile Documents/com~apple~CloudDocs/Documents/Devnewproject/Life-Code-OS-team-dev/live-clone')
OUT = ROOT / 'docs/upgrade/sources/phase-1.5'
SHA = '4df9b6efa6601bc113bc51956ed83e076da75657'

def git(*args):
    return subprocess.run(['git','--no-optional-locks','-C',str(OTHER),*args],check=True,capture_output=True).stdout

records=[]
for name in git('ls-tree','-r','--name-only',SHA,'_handover').decode().splitlines():
    data=git('show',f'{SHA}:{name}')
    dest=OUT/'committed'/name
    dest.parent.mkdir(parents=True,exist_ok=True)
    if dest.exists() and dest.read_bytes()!=data:
        raise RuntimeError(f'Historical snapshot changed: {dest}')
    dest.write_bytes(data)
    records.append({'path':str(dest.relative_to(OUT)),'source_commit':SHA,'status':'VERIFIED_HEAD_ONLY','sha256':hashlib.sha256(data).hexdigest()})
for name in ['_handover/bilingual/PHASE_1_5_PROGRESS.md','_handover/bilingual/01_CRAWL_INVENTORY.csv','_handover/bilingual/01_CRAWL_INVENTORY.summary.json']:
    source=OTHER/name
    if source.is_file():
        dest=OUT/'uncommitted'/name
        dest.parent.mkdir(parents=True,exist_ok=True)
        if dest.exists() and dest.read_bytes()!=source.read_bytes():
            raise RuntimeError(f'Uncommitted snapshot changed: {dest}')
        shutil.copy2(source,dest)
        records.append({'path':str(dest.relative_to(OUT)),'source_commit':None,'status':'VERIFIED_WORKTREE_ONLY','sha256':hashlib.sha256(dest.read_bytes()).hexdigest()})
(OUT/'SOURCE_RECEIPT.json').write_text(json.dumps({'scope':'Historical reference only; do not infer Founder approval or production state','files':records},ensure_ascii=False,indent=2)+'\n')
print(f'Preserved {len(records)} legacy handover artifacts; source checkout unchanged.')
