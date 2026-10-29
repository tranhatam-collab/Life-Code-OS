"""Preserve the exact reviewed PNGs so visual QA remains inspectable after temp cleanup."""
import hashlib,json,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];P=ROOT/'docs/upgrade/2026-10-29'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def copy(src,dest,digest):
 assert sha(src)==digest;dest.parent.mkdir(parents=True,exist_ok=True)
 if dest.exists():assert sha(dest)==digest
 else:shutil.copyfile(src,dest)
 return dest.relative_to(ROOT).as_posix()
def main():
 p=P/'evidence/DOCUMENT_QA.json';d=json.loads(p.read_text())
 for r in d['visual_review']['pages']:r['delivered_png']=copy(Path(r['png']),P/'evidence/document-render'/f"page-{r['page']:03}.png",r['png_sha256'])
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
 p=P/'evidence/WORKBOOK_QA.json';d=json.loads(p.read_text());items=d['visual_review'].get('renders',d['visual_review'].get('images',[]))
 if not items:items=next(v for v in d['visual_review'].values() if isinstance(v,list) and v and isinstance(v[0],dict) and 'file' in v[0])
 for r in items:r['delivered_png']=copy(Path(r['file']),P/'evidence/workbook-render'/Path(r['file']).name,r['sha256'])
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'document_pages':50,'workbook_ranges':len(items),'mode':'Exact byte copies; no image editing or new visual claim'}))
if __name__=='__main__':main()
