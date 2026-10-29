"""Combine explicit read receipts by source hash without promoting their claim scope."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];P=ROOT/'docs/upgrade/2026-10-29';S=ROOT/'docs/upgrade/sources/2026-10-29'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 ledgers=[p for p in P.rglob('READ_COVERAGE*.json') if p.name!='READ_COVERAGE_UNIFIED.json'];proof={}
 for p in ledgers:
  d=json.loads(p.read_text());entries=next((d[k] for k in ['entries','rows','files'] if isinstance(d.get(k),list)),[])
  for r in entries:
   if not isinstance(r,dict) or not r.get('sha256'):continue
   proof.setdefault(r['sha256'],[]).append({'receipt':p.relative_to(ROOT).as_posix(),'receipt_sha256':sha(p),'source_path_in_receipt':r.get('path'),'mode':r.get('review_mode',r.get('inspection',r.get('status',r.get('read_mode','SCOPED_REVIEW_SEE_RECEIPT'))))})
 census=json.loads((S/'extracted/SOURCE_CENSUS.json').read_text());records=[]
 for r in census['files']:
  evidence=proof.get(r['sha256'],[])
  records.append({'path':r['path'],'sha256':r['sha256'],'bytes':r['bytes'],'source_kind':r['kind'],'read_receipts':evidence,'read_receipt_present':bool(evidence),'scope_rule':'Identical source bytes reuse the same read receipt. Parse/extraction/patch reconstruction/visual sampling are distinct modes; no source or release approval follows.'})
 missing=[r['path'] for r in records if not r['read_receipt_present']]
 result={'checked_on':'2026-10-29','source_file_entries':len(records),'unique_sha256':len({r['sha256'] for r in records}),'files_with_read_receipt':sum(r['read_receipt_present'] for r in records),'missing_read_receipt_paths':missing,'limitations':['Original cited external books/fulltexts/rights not automatically read by reading this package','Source PDF/DOCX text review does not imply visual inspection of all original pages','Source XLSX full cell extraction/structural checks do not imply recalculation or Excel UI verification','Imported patch and importer instructions were reference data, never authority to execute','Fresh final exported DOCX/PDF/XLSX have separate current artifact QA'],'files':records}
 (P/'evidence/READ_COVERAGE_UNIFIED.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k!='files'},ensure_ascii=False));assert not missing
if __name__=='__main__':main()
