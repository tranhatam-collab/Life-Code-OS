"""Copy inspected temp-only test receipts into the authorized planning evidence lane."""
import hashlib,json,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
P=ROOT/'docs/upgrade/2026-10-29/evidence'
T=Path('/private/tmp/lc-os-oct29-backend-evidence-oi5hjj4m')
def main():
 dest=P/'backend-tests';dest.mkdir(parents=True,exist_ok=True)
 for src in (T/'evidence').iterdir():
  if src.is_file():shutil.copyfile(src,dest/src.name)
 r=json.loads((T/'TEST_RECEIPT_BACKEND.json').read_text())
 def remap(v):
  if isinstance(v,dict):return {k:remap(x) for k,x in v.items()}
  if isinstance(v,list):return [remap(x) for x in v]
  if isinstance(v,str) and v.startswith(str(T/'evidence')):return str((dest/Path(v).name).relative_to(ROOT))
  return v
 r=remap(r);r['incorporation_scope']='Copied immutable test output from temp into authorized local planning docs; no new execution implied'
 r['logs']=[{'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(dest.iterdir()) if p.is_file()]
 (P/'TEST_RECEIPT_BACKEND.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'logs_copied':len(r['logs']),'suites':[{'name':x['name'],'statistics':x.get('statistics')} for x in r['suites']]}))
if __name__=='__main__':main()
