"""Finalize local checksums and assemble the portable planning handoff, no network."""
import hashlib
import json
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
UPGRADE=ROOT/'docs/upgrade'
P=UPGRADE/'2026-10-20'
OUT=UPGRADE/'deliverables'

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    OUT.mkdir(exist_ok=True)
    names=sorted({p.relative_to(P).as_posix() for p in P.rglob('*') if p.is_file()}|{'manifest.txt','MANIFEST.json'})
    (P/'manifest.txt').write_text('Life Code OS 2026-10-20.r2\nCurrent local planning package file list\nOriginal 149 source files are separately preserved under docs/upgrade/sources/2026-10-11.\nSHA-256 and size: see MANIFEST.json (self excluded). This is not release approval.\n\n'+'\n'.join(names)+'\n')
    # Refresh embedded TXT/navigation before freezing hashes; no output hash is
    # embedded in the portal, so this does not create a checksum cycle.
    subprocess.run([sys.executable,str(ROOT/'tools/planning/build_package_indices.py')],check=True)
    paths=sorted(p for p in P.rglob('*') if p.is_file() and p.name!='MANIFEST.json')
    if any(p.is_symlink() or '__pycache__' in p.parts or 'node_modules' in p.parts for p in paths):
        raise RuntimeError('Unexpected symlink/cache/runtime dependency in portable package')
    manifest={'version':'2026-10-20.r2','scope':'LOCAL_PLANNING_PACKAGE_INTEGRITY_NOT_RELEASE_APPROVAL','algorithm':'SHA-256','self_excluded':'MANIFEST.json','files':[{'path':p.relative_to(P).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in paths]}
    (P/'MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    subprocess.run([sys.executable,str(P/'VERIFY_PACKAGE.py')],check=True)
    entries=[]
    for p in sorted(P.rglob('*')):
        if p.is_file():entries.append((p,p.relative_to(ROOT).as_posix()))
    for p in sorted((UPGRADE/'sources').rglob('*')):
        if p.is_file():entries.append((p,p.relative_to(ROOT).as_posix()))
    for p in sorted((ROOT/'tools/planning').rglob('*')):
        if p.is_file() and not p.is_symlink() and 'node_modules' not in p.parts and '__pycache__' not in p.parts:
            entries.append((p,'tools/planning/'+p.relative_to(ROOT/'tools/planning').as_posix()))
    for p in sorted((ROOT/'docs').rglob('*')):
        if p.is_file() and UPGRADE not in p.parents:entries.append((p,p.relative_to(ROOT).as_posix()))
    for p in sorted((ROOT/'site-templates').glob('*.md')):
        entries.append((p,p.relative_to(ROOT).as_posix()))
    for p in [UPGRADE/'README.md',ROOT/'README.md',ROOT/'PROJECT_STATUS_MASTER.md']:
        entries.append((p,p.relative_to(ROOT).as_posix()))
    names=[name for _,name in entries]
    if len(names)!=len(set(names)):raise RuntimeError('Duplicate archive paths')
    target=OUT/'Life_Code_OS_Complete_Upgrade_Package_2026-10-20.zip'
    with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for path,name in entries:z.write(path,name)
        z.writestr('OPEN_FIRST.html','''<!doctype html><html lang="vi"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Life Code OS Bộ kế hoạch 20/10/2026</title><body style="max-width:800px;margin:60px auto;padding:24px;font:18px/1.7 system-ui;background:#f8f8f5;color:#23313b"><h1>Life Code OS</h1><p>Bộ kế hoạch hợp nhất ngày 20/10/2026. Đây là hồ sơ chuẩn bị phát triển và demo tổng hợp, không phải ứng dụng đã triển khai.</p><p><a href="docs/upgrade/2026-10-20/INDEX.html">Mở cổng đọc và tìm kiếm toàn bộ kế hoạch</a></p><p><a href="docs/upgrade/2026-10-20/00_Doc_truoc/Life_Code_OS_Master_Upgrade_Plan.pdf">Master PDF</a> · <a href="docs/upgrade/2026-10-20/00_Doc_truoc/Life_Code_OS_Execution_Board.xlsx">Bảng điều hành Excel</a> · <a href="docs/upgrade/2026-10-20/10_Ma_tham_chieu_Kiem_thu/demo.html">Demo Lab</a></p><p>149 tệp gốc, ZIP và lời bàn giao được giữ trong docs/upgrade/sources. Kế hoạch cũ của repository nằm trong docs và site-templates. Layout archive giữ đúng đường dẫn repository; không phải full application source hoặc Git history. Clone canonical remote theo BASELINE_LOCK để phát triển ứng dụng.</p><p>Release HOLD. Source rights, phương pháp, ngân sách, quyết định Founder và các gate runtime vẫn cần receipt riêng. Không chạy lệnh deploy trong tài liệu lịch sử chỉ vì chúng xuất hiện trong archive.</p></body></html>''')
    with zipfile.ZipFile(target) as z:
        if z.testzip() is not None:raise RuntimeError('ZIP CRC failure')
        for p,name in entries:
            if hashlib.sha256(z.read(name)).hexdigest()!=sha(p):raise RuntimeError('ZIP parity failure '+name)
    receipt={'version':'2026-10-20.r2','scope':'PORTABLE_LOCAL_HANDOFF_NOT_PRODUCTION_APPROVAL','file':target.name,'sha256':sha(target),'bytes':target.stat().st_size,'archive_entries':len(entries)+1,'current_package_files':len(paths)+1,'current_manifest_sha256':sha(P/'MANIFEST.json'),'original_attachment_files_preserved':149,'integrity_verifier_exit':0,'zip_crc_and_source_entry_sha256_parity':True,'generated_archive_only_entry':'OPEN_FIRST.html','production_release_verdict':'HOLD'}
    (OUT/'DELIVERY_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(receipt,ensure_ascii=False))

if __name__=='__main__':main()
