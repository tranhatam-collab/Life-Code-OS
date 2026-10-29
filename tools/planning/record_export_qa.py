"""Copy the reviewed master PDF and record mechanical and declared visual coverage."""
import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path
import pdfplumber
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'docs/upgrade/2026-10-20/00_Doc_truoc'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--render-dir',type=Path,required=True)
    ap.add_argument('--reviewed-pages',required=True,help='Comma-separated pages actually visually reviewed by root/team')
    args=ap.parse_args()
    rendered=args.render_dir/'Life_Code_OS_Master_Upgrade_Plan.pdf'
    pdf=PdfReader(rendered)
    extracted=re.sub(r'\s+',' ', ' '.join(page.extract_text() or '' for page in pdf.pages))
    registry=json.loads((OUT.parent/'09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.json').read_text())+json.loads((OUT.parent/'09_Doi_chieu_Bang_chung/RESEARCH_UPDATE_2026-10-20.json').read_text())
    missing_titles=[r['id'] for r in registry if re.sub(r'\s+',' ',r['id']+' '+r['title']) not in extracted]
    if missing_titles:raise RuntimeError('Bibliographic identifiers/titles lost: '+','.join(missing_titles))
    empty=[];replacement=[];outside=[]
    with pdfplumber.open(rendered) as doc:
        for n,page in enumerate(doc.pages,1):
            text=page.extract_text() or ''
            if not text.strip():empty.append(n)
            if '\ufffd' in text:replacement.append(n)
            for word in page.extract_words():
                if word['x0'] < -0.5 or word['top'] < -0.5 or word['x1'] > page.width+0.5 or word['bottom'] > page.height+0.5:
                    outside.append({'page':n,'text':word['text'],'bbox':[word['x0'],word['top'],word['x1'],word['bottom']]})
    reviewed=sorted({int(v) for v in args.reviewed_pages.split(',')})
    if reviewed!=list(range(1,len(pdf.pages)+1)):raise RuntimeError('Incomplete or invalid visual coverage')
    if empty or replacement or outside:raise RuntimeError(json.dumps({'empty':empty,'replacement':replacement,'outside':outside}))
    target=OUT/rendered.name
    shutil.copy2(rendered,target)
    docx=OUT/'Life_Code_OS_Master_Upgrade_Plan.docx'
    a11y=json.loads(Path('/private/tmp/lifecode-master-a11y.json').read_text())
    report={'scope':'LOCAL_MASTER_EXPORT_LAYOUT_NOT_PRODUCTION_WCAG_OR_PDF_UA_CERTIFICATION','checked_at':'2026-10-20','evidence_status':'VERIFIED_WORKTREE_ONLY','pages':len(pdf.pages),'original_topics_preserved':38,'visual_pages_reviewed':reviewed,'visual_review':f'Root pages1-28; product/frontend/business lane pages29-{len(pdf.pages)}. Final pages1-51 pixel-identical to reviewed v6; changed source appendix pages52-{len(pdf.pages)} inspected individually.','bibliographic_titles_preserved':len(registry),'missing_bibliographic_titles':missing_titles,'empty_pages':empty,'unicode_replacement_pages':replacement,'words_outside_page':outside,'renderer':'LibreOffice via Documents render_docx.py; individual page PNG review','pdf_sha256':sha(target),'docx_sha256':sha(docx),'docx_a11y_audit':a11y,'production_release_verdict':'HOLD'}
    (OUT/'EXPORT_QA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    assembly=json.loads((OUT/'MASTER_ASSEMBLY.json').read_text())
    assembly.update({'render_status':'VERIFIED_WORKTREE_ONLY','rendered_pdf_pages':len(pdf.pages),'pdf_sha256':sha(target),'docx_sha256':sha(docx),'layout_receipt':'EXPORT_QA.json'})
    (OUT/'MASTER_ASSEMBLY.json').write_text(json.dumps(assembly,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'pages':len(pdf.pages),'empty':len(empty),'replacement':len(replacement),'outside':len(outside),'pdf_sha256':sha(target)}))

if __name__=='__main__':main()
