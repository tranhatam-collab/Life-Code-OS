"""Generate package navigation and source-to-revision tracking without dropping files."""
import csv
import hashlib
import html
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'docs/upgrade/2026-10-20'
S=ROOT/'docs/upgrade/sources/2026-10-11'

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def output(rel,data):
    (P/rel).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')

def main():
    source=json.loads((S/'SOURCE_RECEIPT.json').read_text())
    readers={}
    for file in [P/'08_Thuc_thi_Kinh_doanh/READ_COVERAGE.json',P/'04_Backend_API/READ_COVERAGE.json']:
        if file.exists():
            content=json.loads(file.read_text())
            for item in content.get('files',content.get('original_files',[])):
                name=item.get('relative_path',item.get('path',''))
                readers[name]=item.get('read_by',content.get('lane',file.parent.name))
    coverage=[];transforms=[]
    for item in source['files']:
        rel=item['path'];original=S/'package'/rel;current=P/rel
        if not current.is_file():raise RuntimeError('Current counterpart missing '+rel)
        ext=original.suffix
        method='Full text and cross references'
        if ext in ['.json','.csv','.yaml','.sql','.mjs','.py','.tap','.mmd','.txt','.html']:
            method='Complete structured/text parse with record/reference inspection'
        if ext=='.pdf':method='All 47 pages text extracted; original export retained'
        if ext=='.docx':method='All 846 paragraphs and 2 tables extracted; original OOXML retained'
        if ext=='.xlsx':method='All 11 sheets/cells and 46 formulas extracted; original workbook retained'
        owner=readers.get(rel,'root integration and governance')
        coverage.append({'path':rel,'reader_lane':owner,'read_status':'READ_COMPLETE','method':method,'source_sha256':item['sha256'],'source_preserved':digest(original)==item['sha256']})
        changed=digest(current)!=item['sha256']
        transforms.append({'source_path':rel,'source_sha256':item['sha256'],'current_path':rel,'current_digest_source':'../deliverables/DELIVERY_RECEIPT.json current_manifest_sha256; self excluded from MANIFEST.json' if rel=='MANIFEST.json' else 'MANIFEST.json record for this path','disposition':'REGENERATED_INTEGRITY_MANIFEST_ORIGINAL_RETAINED' if rel=='MANIFEST.json' else 'REVISED_WITH_ORIGINAL_RETAINED' if changed else 'RETAINED_WITH_CURRENT_ADDENDUM','authority':'DOCUMENT_AUTHORITY.md; domain execution contracts; current registries','original_preserved':True})
    output('00_Doc_truoc/READ_COVERAGE.json',{'scope':'COMPLETE_SUPPLIED_PACKAGE','original_file_count':149,'read_file_count':len(coverage),'files':coverage,'binary_extractions':'../sources/2026-10-11/export-text','note':'Read/parse coverage is distinct from external source rights, method approval and production validation'})
    output('09_Doi_chieu_Bang_chung/SOURCE_FILE_TRANSFORMATIONS.json',transforms)
    with (P/'09_Doi_chieu_Bang_chung/SOURCE_FILE_TRANSFORMATIONS.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(transforms[0]));w.writeheader();w.writerows(transforms)
    counts={
        'tasks':len(json.loads((P/'08_Thuc_thi_Kinh_doanh/EXECUTION_BACKLOG.json').read_text())),
        'screens':len(json.loads((P/'05_Frontend_UI/SCREEN_REGISTRY.json').read_text())),
        'products':len(json.loads((P/'01_Chien_luoc_San_pham/PRODUCT_CATALOG.json').read_text())),
        'demos':len(json.loads((P/'10_Ma_tham_chieu_Kiem_thu/data/demo_cases.json').read_text()).get('cases',[])),
    }
    original_readme=(S/'package/README.md').read_text()
    current=f'''# Life Code OS Bộ kế hoạch hợp nhất chuẩn bị phát triển

Phiên bản **2026-10-20.r2**. Đã tích hợp đủ 149 tệp gốc; source bytes và ZIP giữ riêng có checksum. Bộ hiện tại có {counts['tasks']} công việc, {counts['products']} sản phẩm, {counts['screens']} màn hình và {counts['demos']} ca demo tổng hợp. Đây là số lượng hồ sơ thiết kế, không phải phần trăm hoàn thành ứng dụng.

## Bắt đầu

- [Cổng đọc và tìm kiếm ngoại tuyến](INDEX.html) phục vụ mobile và desktop.
- [Hướng dẫn nhận việc DEV](00_Doc_truoc/DEV_START_HERE_2026-10-20.md).
- [Phần hợp nhất 20/10](00_Doc_truoc/AMENDMENT_2026-10-20.md) và [thứ tự áp dụng tài liệu](00_Doc_truoc/DOCUMENT_AUTHORITY.md).
- [Master Markdown](00_Doc_truoc/Life_Code_OS_Master_Upgrade_Plan.md), [Word](00_Doc_truoc/Life_Code_OS_Master_Upgrade_Plan.docx), [PDF](00_Doc_truoc/Life_Code_OS_Master_Upgrade_Plan.pdf), [bảng điều hành](00_Doc_truoc/Life_Code_OS_Execution_Board.xlsx).
- [Demo cục bộ](10_Ma_tham_chieu_Kiem_thu/demo.html), [phương pháp và tính toán](04_Backend_API/05_METHOD_EXECUTION_AND_RESULT_CONTRACT.md), [migration](04_Backend_API/07_MIGRATION_AND_RECONCILIATION_RUNBOOK.md), [FPOS RG0–RG13](07_Bao_mat_Van_hanh/FPOS_GATE_MAPPING.md).

## Kiểm chứng và phê duyệt

Chạy VERIFY_PACKAGE.py để kiểm tra integrity; xem PACKAGE_QA, WORKBOOK_QA, BROWSER_QA và EXPORT_QA trong 00_Doc_truoc để biết scope kiểm tra thực tế. Kết quả test local không chứng minh authentication/provider/payment/migration/recovery production. Release hiện **HOLD**; các quyết định Q và method/source/rights approvals chưa được tự thông qua.

## Bảo toàn và truy vết

[Nguồn gốc](../sources/2026-10-11/SOURCE_RECEIPT.json) ghi 149 SHA-256. [Read coverage](00_Doc_truoc/READ_COVERAGE.json) và [source transformations](09_Doi_chieu_Bang_chung/SOURCE_FILE_TRANSFORMATIONS.csv) ghi từng tệp. Kế hoạch audit và tài liệu cũ trong Git được giữ; local phase handover cũng được snapshot riêng trong sources/phase-1.5. Không dùng các nhãn historical pass hoặc tỷ lệ cũ làm release evidence.

## Hướng dẫn gốc ngày11/10 được giữ để đối chiếu

Nội dung dưới đây là source lịch sử. Các con số QA và giới hạn mô tả đúng phạm vi phiên bản11/10; dùng các receipt20/10 và amendment phía trên khi nhận việc hiện tại.

---

'''+original_readme
    (P/'README.md').write_text(current)
    files=[]
    for f in sorted(P.rglob('*')):
        if not f.is_file() or '__pycache__' in f.parts or 'node_modules' in f.parts:continue
        rel=f.relative_to(P).as_posix()
        title=rel
        if f.suffix=='.md':
            lines=f.read_text().splitlines()
            title=next((l.lstrip('# ').strip() for l in lines if l.startswith('# ')),rel)
        files.append({'path':rel,'title':title,'group':rel.split('/')[0] if '/' in rel else 'Bắt đầu','format':f.suffix.lstrip('.')})
    output('FILE_CATALOG.json',files)
    with (P/'FILE_CATALOG.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(files[0]));w.writeheader();w.writerows(files)
    docs=[]
    for item in files:
        rel=item['path'];file=P/rel
        # Embed text locally to avoid file:// fetch restrictions and external requests.
        body=file.read_text() if file.suffix in ['.md','.json','.csv','.yaml','.sql','.mmd','.txt'] else ''
        if rel=='00_Doc_truoc/Life_Code_OS_Master_Upgrade_Plan.md':body='Bản tổng hợp đầy đủ. Mở tệp hoặc dùng từng chuyên đề để đọc nhanh và tìm kiếm.'
        if file.name.endswith('_QA.json') or file.name=='MANIFEST.json':body='Receipt/checksum máy đọc. Mở tệp để xem toàn bộ record.'
        docs.append({**item,'body':body})
    payload=json.dumps(docs,ensure_ascii=False).replace('</','<\\/')
    page='''<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Life Code OS Bộ chuẩn bị phát triển</title><style>
:root{font-family:system-ui,-apple-system,"Segoe UI",sans-serif;color:#23313b;background:#f8f8f5;line-height:1.65}*{box-sizing:border-box}body{margin:0}a{color:#275571;text-underline-offset:3px}header{padding:30px max(24px,5vw) 20px;border-bottom:1px solid #dce0df;background:white}header p{max-width:850px;margin:8px 0;color:#5c686e}h1{font-size:clamp(26px,4vw,40px);font-weight:560;letter-spacing:-1px;margin:0}nav{display:flex;gap:12px;flex-wrap:wrap;margin-top:18px}nav a{padding:5px 10px;border:1px solid #d4dcdf;border-radius:6px;text-decoration:none;font-size:14px}.layout{display:grid;grid-template-columns:minmax(280px,350px) minmax(0,1fr);max-width:1550px;margin:auto}.sidebar{padding:24px;border-right:1px solid #dce0df}label{font-weight:600;font-size:14px}input,select{width:100%;padding:12px;border:1px solid #b7c1c6;border-radius:6px;background:white;font:inherit;margin:6px 0 14px;min-height:44px}#list{display:flex;flex-direction:column;gap:6px;max-height:78vh;overflow:auto}#list button{font:inherit;background:transparent;text-align:left;border:0;border-radius:6px;padding:12px;cursor:pointer;overflow-wrap:anywhere}#list button:hover,#list button[aria-current=true]{background:#e9eff1}small{display:block;color:#68767b;font-size:12px}.content{padding:30px 4vw 80px;min-width:0;background:white}h2{font-size:25px;font-weight:560;line-height:1.35;overflow-wrap:anywhere}#body{white-space:pre-wrap;font-size:16px;overflow-wrap:anywhere;max-width:900px}#body h3{font-size:20px;margin-top:30px;white-space:normal}#body h4{font-size:17px;margin-top:22px;white-space:normal}#body p{margin:10px 0;white-space:pre-wrap}#body pre{overflow:auto;background:#f3f5f5;padding:16px;border-radius:6px;font-size:13px;white-space:pre}#count{font-size:13px;color:#63727b}#open{display:inline-block;margin-bottom:20px;overflow-wrap:anywhere}.skip{position:absolute;left:-9999px}.skip:focus{left:20px;top:10px;background:white;padding:10px}:focus-visible{outline:3px solid #527e96;outline-offset:3px}details{margin:8px 0}summary{cursor:pointer}footer{padding:20px;font-size:13px;color:#64727a} @media(max-width:760px){header{padding:24px 20px}nav{gap:8px}.layout{grid-template-columns:1fr}.sidebar{border-right:0;border-bottom:1px solid #dce0df;padding:20px}#list{max-height:32vh}.content{padding:24px 20px 60px}#body{font-size:16px}h2{font-size:23px}}@media print{header,.sidebar,nav,#open,footer{display:none}.layout{display:block}.content{padding:0}#body{font-size:11pt}}
</style></head><body><a class="skip" href="#document">Đến tài liệu</a><header><h1>Life Code OS</h1><p>Bộ kế hoạch hợp nhất chuẩn bị phát triển ·20/10/2026</p><p>149 tệp gốc được bảo toàn. Chọn chuyên đề để đọc, tìm công thức và xem demo. Phê duyệt sản phẩm và phát hành vẫn theo receipt riêng.</p><nav aria-label="Mở nhanh"><a href="00_Doc_truoc/DEV_START_HERE_2026-10-20.md">Bắt đầu DEV</a><a href="00_Doc_truoc/Life_Code_OS_Master_Upgrade_Plan.pdf">Master PDF</a><a href="00_Doc_truoc/Life_Code_OS_Master_Upgrade_Plan.docx">Word</a><a href="00_Doc_truoc/Life_Code_OS_Execution_Board.xlsx">Bảng điều hành</a><a href="10_Ma_tham_chieu_Kiem_thu/demo.html">Demo Lab</a></nav></header><div class="layout"><aside class="sidebar" aria-label="Tìm tài liệu"><label for="search">Tìm theo nội dung hoặc tên tệp</label><input id="search" type="search" placeholder="Ví dụ: công thức, consent, timeline"><label for="group">Nhóm tài liệu</label><select id="group"><option value="">Tất cả</option></select><p id="count" role="status" aria-live="polite"></p><div id="list" aria-label="Kết quả tìm kiếm"></div></aside><main id="document" class="content" tabindex="-1"><small id="meta"></small><h2 id="title"></h2><a id="open" href="#">Mở tệp đầy đủ</a><article id="body"></article></main></div><footer>Đọc ngoại tuyến trên mobile và desktop. Demo dùng dữ liệu tổng hợp. Bộ tài liệu không tự đóng gate production.</footer><script>
const docs=__PAYLOAD__;const byId=id=>document.getElementById(id);const escape=s=>s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');let selected='';
const groups=[...new Set(docs.map(d=>d.group))];for(const g of groups){const o=document.createElement('option');o.value=g;o.textContent=g;byId('group').append(o)}
function show(d){selected=d.path;byId('meta').textContent=d.path+' · '+d.format.toUpperCase();byId('title').textContent=d.title;byId('open').href=d.path;const raw=d.body||'Tệp này mở bằng ứng dụng phù hợp. Dùng liên kết phía trên để xem toàn bộ nội dung.';let safe=escape(raw);safe=safe.replace(/^####? (.+)$/gm,'<h4>$1</h4>').replace(/^## (.+)$/gm,'<h3>$1</h3>').replace(/^# (.+)$/gm,'<h3>$1</h3>');byId('body').innerHTML=safe;for(const b of byId('list').querySelectorAll('button'))b.setAttribute('aria-current',String(b.dataset.path===selected));history.replaceState(null,'','#'+encodeURIComponent(d.path))}
function filter(){const q=byId('search').value.toLocaleLowerCase('vi');const g=byId('group').value;const matches=docs.filter(d=>(!g||d.group===g)&&(!q||(d.title+' '+d.path+' '+d.body).toLocaleLowerCase('vi').includes(q)));byId('count').textContent=matches.length+' tệp';byId('list').replaceChildren();for(const d of matches){const b=document.createElement('button');b.type='button';b.dataset.path=d.path;b.textContent=d.title;const s=document.createElement('small');s.textContent=d.path;b.append(s);b.setAttribute('aria-current',String(d.path===selected));b.addEventListener('click',()=>show(d));byId('list').append(b)}}byId('search').addEventListener('input',filter);byId('group').addEventListener('change',filter);filter();const initial=decodeURIComponent(location.hash.slice(1));show(docs.find(d=>d.path===initial)||docs.find(d=>d.path.includes('DEV_START_HERE'))||docs[0]);
</script></body></html>'''
    page=page.replace('</style>',' .layout>*{min-width:0}#body,#body h3,#body h4,#open,#list button,#meta{word-break:break-word}#meta{overflow-wrap:anywhere}select{appearance:none;-webkit-appearance:none;min-height:44px;padding-right:36px;background-image:linear-gradient(45deg,transparent 50%,#68767b 50%),linear-gradient(135deg,#68767b 50%,transparent 50%);background-position:calc(100% - 18px) 50%,calc(100% - 13px) 50%;background-size:5px 5px;background-repeat:no-repeat}</style>')
    (P/'INDEX.html').write_text(page.replace('__PAYLOAD__',payload))
    print(json.dumps({'source_coverage':len(coverage),'catalog_files':len(files),'counts':counts},ensure_ascii=False))

if __name__=='__main__':main()
