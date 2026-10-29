"""Export all local planning sources/docs plus helpers; verify the extracted bundle."""
import hashlib,json,shutil,subprocess,tempfile,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
NAME='Life_Code_OS_Integrated_Dev_Handoff_2026-10-29'
DEST=ROOT/'docs/upgrade/deliverables';ZIP=DEST/(NAME+'.zip');RECEIPT=DEST/(NAME+'_Receipt.json')
def sha(data):return hashlib.sha256(data).hexdigest()
def main():
 DEST.mkdir(parents=True,exist_ok=True);files={}
 for base in [ROOT/'docs',ROOT/'tools/planning']:
  for p in base.rglob('*'):
   if not p.is_file() or p.is_symlink():continue
   rel=p.relative_to(ROOT).as_posix()
   if any(x in ['node_modules','__pycache__','.git'] for x in p.parts):continue
   if p.parent==DEST and p.name.startswith(NAME):continue
   if p.name in ['.DS_Store'] and 'sources' not in p.parts:continue
   files[rel]=p.read_bytes()
 for name in ['README.md','PROJECT_STATUS_MASTER.md']:files[name]=(ROOT/name).read_bytes()
 files['BUNDLE_README.md']=('''# Life Code OS — Planning and DEV handoff bundle 2026-10-29

This is the complete local planning/document bundle, including original sources,
the immutable local r2 plan, the new integrated plan, artifact QA and helpers.
It is not a checkout of application code and does not authorize deployment.

Start at docs/upgrade/2026-10-29/START_HERE.md or the Word/PDF/Excel exports.
From this extracted root, verify without executing attached importers or SQL:

    python3 -B tools/planning/oct29/verify_final.py --portable

Application development must use the exact reviewed repository candidate and
accepted work order. Source ZIPs, historical receipts and absolute paths inside
receipts retain their original identity; they are not the current runtime.

BUNDLE_MANIFEST.json excludes itself. The external delivery receipt records the
ZIP hash and the manifest hash, preventing receipt/manifest self-reference cycles.
''').encode()
 manifest={'format':'lifecode-planning-bundle/1','version':'2026-10-29.r1','application_source_included':False,'self_excluded':True,'files':[{'path':k,'bytes':len(v),'sha256':sha(v)} for k,v in sorted(files.items())]}
 manifestbytes=(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode();files['BUNDLE_MANIFEST.json']=manifestbytes
 tempzip=ZIP.with_suffix('.zip.tmp')
 with zipfile.ZipFile(tempzip,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for k,v in sorted(files.items()):z.writestr(NAME+'/'+k,v)
 tempzip.replace(ZIP)
 temp=Path(tempfile.mkdtemp(prefix='lc-os-planning-portable-'));extract=temp/NAME
 with zipfile.ZipFile(ZIP) as z:
  assert z.testzip() is None
  for i in z.infolist():
   p=Path(i.filename);assert not p.is_absolute() and '..' not in p.parts and '\\' not in i.filename
  z.extractall(temp)
 for r in manifest['files']:
  raw=(extract/r['path']).read_bytes();assert len(raw)==r['bytes'] and sha(raw)==r['sha256']
 run=subprocess.run([__import__('sys').executable,'-B','tools/planning/oct29/verify_final.py','--portable'],cwd=extract,text=True,capture_output=True,timeout=60)
 assert run.returncode==0,run.stdout+run.stderr
 result={'version':'2026-10-29.r1','zip_path':str(ZIP.relative_to(ROOT)),'zip_bytes':ZIP.stat().st_size,'zip_sha256':sha(ZIP.read_bytes()),'bundle_manifest_sha256':sha(manifestbytes),'manifest_entries_excluding_self':len(manifest['files']),'archive_entries':len(files),'portable_extraction':str(extract),'portable_verification_exit':run.returncode,'portable_verification_output':run.stdout.strip(),'zip_crc':'PASS','all_bundle_manifest_hashes':'PASS','commit_push_deploy_performed':False,'scope':'Planning/documents/sources/helpers only; no application source checkout or runtime approval'}
 RECEIPT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False))
if __name__=='__main__':main()
