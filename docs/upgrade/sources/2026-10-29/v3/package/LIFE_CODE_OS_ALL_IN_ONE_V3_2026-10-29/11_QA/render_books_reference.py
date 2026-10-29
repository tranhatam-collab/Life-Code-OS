from pathlib import Path
import re, json
from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
R=Path(__file__).resolve().parents[1]
TEAL='155B57';DARK='17373B';GRAY='53686C';GOLD='A77B31'

def shade(cell,color):
 tcPr=cell._tc.get_or_add_tcPr();sh=OxmlElement('w:shd');sh.set(qn('w:fill'),color);tcPr.append(sh)
def font(run,size=None,bold=None,color=None):
 run.font.name='Noto Sans'
 rp=run._element.get_or_add_rPr();rf=rp.rFonts
 if rf is None: rf=OxmlElement('w:rFonts');rp.insert(0,rf)
 for k in ['ascii','hAnsi','eastAsia','cs']:rf.set(qn('w:'+k),'Noto Sans')
 if size:run.font.size=Pt(size)
 if bold is not None:run.bold=bold
 if color:run.font.color.rgb=RGBColor.from_string(color)
def field(p,code):
 r=OxmlElement('w:r');b=OxmlElement('w:fldChar');b.set(qn('w:fldCharType'),'begin');r.append(b);p._p.append(r)
 r=OxmlElement('w:r');t=OxmlElement('w:instrText');t.set(qn('xml:space'),'preserve');t.text=' '+code+' ';r.append(t);p._p.append(r)
 r=OxmlElement('w:r');b=OxmlElement('w:fldChar');b.set(qn('w:fldCharType'),'end');r.append(b);p._p.append(r)
def inline(p,text,size=None):
 for part in re.split(r'(\*\*.*?\*\*|`[^`]+`)',text):
  if not part:continue
  if part.startswith('**') and part.endswith('**'):run=p.add_run(part[2:-2]);font(run,size,True)
  elif part.startswith('`') and part.endswith('`'):run=p.add_run(part[1:-1]);font(run,(size or 10.5)-.4,color=TEAL)
  else:run=p.add_run(part);font(run,size)
def bookmark(p,name,id):
 start=OxmlElement('w:bookmarkStart');start.set(qn('w:id'),str(id));start.set(qn('w:name'),name)
 end=OxmlElement('w:bookmarkEnd');end.set(qn('w:id'),str(id));p._p.insert(0,start);p._p.append(end)
def link(p,title,anchor):
 h=OxmlElement('w:hyperlink');h.set(qn('w:anchor'),anchor)
 r=OxmlElement('w:r');pr=OxmlElement('w:rPr');c=OxmlElement('w:color');c.set(qn('w:val'),TEAL);pr.append(c);r.append(pr)
 t=OxmlElement('w:t');t.text=title;r.append(t);h.append(r);p._p.append(h)
def table(doc,lines):
 rows=[]
 for ln in lines:
  rr=[x.strip() for x in ln.strip().strip('|').split('|')]
  if all(re.fullmatch(r':?-{2,}:?',x) for x in rr):continue
  rows.append(rr)
 if not rows:return
 n=max(map(len,rows));t=doc.add_table(rows=1,cols=n);t.autofit=False;t.style='Table Grid'
 # weighted by type/content rather than unconstrained autofit
 widths=[1]*n
 if n==2:widths=[.30,.70]
 elif n==3:widths=[.19,.32,.49]
 elif n==4:widths=[.12,.18,.28,.42]
 elif n==5:widths=[.11,.20,.23,.23,.23]
 total=sum(widths)
 for i,c in enumerate(t.columns):c.width=Cm(17.0*widths[i]/total)
 for ri,rr in enumerate(rows):
  cells=t.rows[0].cells if ri==0 else t.add_row().cells
  for ci,cell in enumerate(cells):
   cell.width=Cm(17.0*widths[ci]/total)
   p=cell.paragraphs[0];p.paragraph_format.space_after=Pt(4);p.paragraph_format.space_before=Pt(3);p.paragraph_format.line_spacing=1.08
   inline(p,rr[ci] if ci<len(rr) else '',9.0 if n>=4 else 9.5)
   if ri==0:
    shade(cell,TEAL)
    for run in p.runs:font(run,9.0 if n>=4 else 9.5,True,'FFFFFF')
   elif ri%2==0:shade(cell,'F0F5F3')
   cell.vertical_alignment=0
   tcPr=cell._tc.get_or_add_tcPr();mar=OxmlElement('w:tcMar')
   for side in ['top','left','bottom','right']:
    el=OxmlElement('w:'+side);el.set(qn('w:w'),'80');el.set(qn('w:type'),'dxa');mar.append(el)
   tcPr.append(mar)
  trPr=t.rows[ri]._tr.get_or_add_trPr();ns=OxmlElement('w:cantSplit');trPr.append(ns)
  if ri==0:hd=OxmlElement('w:tblHeader');trPr.append(hd)
 doc.add_paragraph().paragraph_format.space_after=Pt(3)

def build(md,name,title,subtitle,tag):
 doc=Document();sec=doc.sections[0];sec.page_width=Cm(21);sec.page_height=Cm(29.7)
 sec.top_margin=Cm(1.9);sec.bottom_margin=Cm(1.8);sec.left_margin=Cm(2);sec.right_margin=Cm(2)
 sec.header_distance=Cm(.8);sec.footer_distance=Cm(.8)
 normal=doc.styles['Normal'];normal.font.name='Noto Sans';normal.font.size=Pt(10.5);normal.paragraph_format.line_spacing=1.16;normal.paragraph_format.space_after=Pt(7)
 for sn,size,col in [('Title',30,DARK),('Subtitle',15,GRAY),('Heading 1',19,TEAL),('Heading 2',13,TEAL),('Heading 3',11,DARK)]:
  st=doc.styles[sn];st.font.name='Noto Sans';st.font.size=Pt(size);st.font.bold=sn!='Subtitle';st.font.color.rgb=RGBColor.from_string(col)
  st.paragraph_format.space_before=Pt(13);st.paragraph_format.space_after=Pt(7);st.paragraph_format.keep_with_next=True
 doc.core_properties.title=title;doc.core_properties.subject=subtitle;doc.core_properties.author='Life Code OS — Bản trình duyệt';doc.core_properties.keywords='Life Code OS; Huyền Nhân Học; All-in-One; V3; 2026-10-29';doc.core_properties.comments='Bản kế hoạch và mã tham chiếu; không phải hồ sơ đã triển khai production.'
 update=OxmlElement('w:updateFields');update.set(qn('w:val'),'true');doc.settings.element.append(update)
 hp=sec.header.paragraphs[0];font(hp.add_run('LIFE CODE OS  /  HUYỀN NHÂN HỌC'),8,True,TEAL)
 hp.alignment=WD_ALIGN_PARAGRAPH.LEFT
 fp=sec.footer.paragraphs[0];fp.alignment=WD_ALIGN_PARAGRAPH.RIGHT;font(fp.add_run('www.lifecode.iai.one  •  V3 / 29.10.2026  •  '),8,color=GRAY);field(fp,'PAGE')
 doc.add_paragraph('\n\n')
 p=doc.add_paragraph();font(p.add_run(tag.upper()),10,True,GOLD)
 doc.add_paragraph(title,'Title');doc.add_paragraph(subtitle,'Subtitle')
 p=doc.add_paragraph('Huyền Nhân Học · Mật Mã Đời Người · Đồng nhịp sống');p.paragraph_format.space_before=Pt(14)
 p=doc.add_paragraph();inline(p,'Nhà sáng lập: **Trần Hà Tâm**\nNgày khóa bản bàn giao: **29/10/2026**')
 p=doc.add_paragraph();p.paragraph_format.space_before=Pt(20)
 inline(p,'**GIỮ NGUYÊN V1 VÀ V2**\nBản nâng cấp tích hợp, đặc tả và phòng thử tham chiếu. Không tự phê duyệt phương pháp; không xác nhận production đã sẵn sàng.')
 p=doc.add_paragraph();inline(p,'Nguồn công khai được chỉ dẫn bằng [Rxx]. Nội dung đã đọc, phạm vi chưa tiếp cận, mã chạy cục bộ và công việc còn phải thực hiện được phân biệt trong tài liệu.',9.5)
 lines=md.splitlines();heads=[(i,l[2:]) for i,l in enumerate(lines) if l.startswith('# ')][1:]
 doc.add_page_break();doc.add_heading('Mục lục điều hướng',1)
 doc.add_paragraph('Chọn tên phần để chuyển đến nội dung. Các bảng JSON, CSV, mã tham chiếu và kiểm thử nằm trong gói đi kèm.',style=None)
 for hi,(pos,label) in enumerate(heads):
  p=doc.add_paragraph();p.paragraph_format.space_after=Pt(5);link(p,label,'section_'+str(hi))
 # Begin chapters, skipping markdown cover block
 start=heads[0][0];i=start;h=0;first=True
 while i<len(lines):
  ln=lines[i]
  if not ln.strip():i+=1;continue
  if ln.startswith('# '):
   
   chapter_match=re.match(r'# (\d+)\.',ln); chapter=int(chapter_match.group(1)) if chapter_match else None
   starts={1,7,12,18} if 'Master' in name else {1,3,6,10}
   if chapter in starts:doc.add_page_break()
   p=doc.add_heading(ln[2:],1);bookmark(p,'section_'+str(h),h+1);h+=1;i+=1;continue
  if ln.startswith('## '):doc.add_heading(ln[3:],2);i+=1;continue
  if ln.startswith('### '):doc.add_heading(ln[4:],3);i+=1;continue
  if ln.startswith('```'):
   code=[];i+=1
   while i<len(lines) and not lines[i].startswith('```'):code.append(lines[i]);i+=1
   p=doc.add_paragraph();p.paragraph_format.line_spacing=1.0
   sh=OxmlElement('w:shd');sh.set(qn('w:fill'),'EEF3F3');p._p.get_or_add_pPr().append(sh)
   run=p.add_run('\n'.join(code));run.font.name='DejaVu Sans Mono';run.font.size=Pt(8)
   i+=1;continue
  if ln.startswith('|'):
   ls=[]
   while i<len(lines) and lines[i].startswith('|'):ls.append(lines[i]);i+=1
   table(doc,ls);continue
  if re.fullmatch(r'[-*_]{3,}',ln.strip()):i+=1;continue
  if ln.startswith('> '):
   p=doc.add_paragraph();p.paragraph_format.left_indent=Cm(.5);inline(p,ln[2:]);
   for run in p.runs:run.italic=True;run.font.color.rgb=RGBColor.from_string(TEAL)
   i+=1;continue
  # single physical line is a paragraph in authored manuscripts
  p=doc.add_paragraph();text=re.sub(r'^[-*] ', '• ',ln)
  if text.startswith('[') and 'https://' in text:
   p.paragraph_format.space_after=Pt(8);inline(p,text,8.5)
  else:inline(p,text)
  i+=1
 dest=R/'00_START'/f'{name}.docx';doc.save(dest);print(dest)

build((R/'00_START/Life_Code_All_In_One_Master_V3.md').read_text(),'Life_Code_All_In_One_Master_V3','LIFE CODE OS\nALL-IN-ONE V3','Kế hoạch tích hợp toàn hệ\nSản phẩm · Tri thức · Backend · Trải nghiệm · Vận hành','Tập 1 / Kế hoạch hợp nhất')
build((R/'00_START/Life_Code_Numbers_Names_Bat_Cuc_Atlas_V3.md').read_text(),'Life_Code_Numbers_Names_Bat_Cuc_Atlas_V3','ATLAS SỐ, TÊN\n& BÁT CỰC LINH SỐ','Công thức · Ma trận · Tổ hợp · Dòng thời gian\nNguồn · Giới hạn · Bộ thử tham chiếu','Tập 2 / Chuyên khảo triển khai')
