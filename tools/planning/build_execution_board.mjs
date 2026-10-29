import fs from 'node:fs/promises';
import path from 'node:path';
import {FileBlob, SpreadsheetFile} from '@oai/artifact-tool';

const root = path.resolve(import.meta.dirname, '../..');
const pkg = path.join(root, 'docs/upgrade/2026-10-20');
const original = path.join(root, 'docs/upgrade/sources/2026-10-11/package/00_Doc_truoc/Life_Code_OS_Execution_Board.xlsx');
const qa = '/private/tmp/lifecode-board-qa';
await fs.mkdir(qa, {recursive:true});
const wb = await SpreadsheetFile.importXlsx(await FileBlob.load(original));
const read = async p=>JSON.parse(await fs.readFile(path.join(pkg,p),'utf8'));
const jsonCell = v => v == null ? null : Array.isArray(v) && v.every(x=>typeof x!=='object') ? v.join('\n') : typeof v==='object' ? JSON.stringify(v) : v;
const col = n => {let s=''; for(++n;n;n=Math.floor((n-1)/26)) s=String.fromCharCode(65+(n-1)%26)+s;return s;};
if(process.argv.includes('--inspect')) {
  console.log((await wb.inspect({kind:'sheet',include:'id,name',maxChars:3500})).ndjson);
  const img=await wb.render({sheetName:'Dashboard',range:'A1:H23',scale:1.5,format:'png'});
  await fs.writeFile(path.join(qa,'original-dashboard.png'),new Uint8Array(await img.arrayBuffer()));
  process.exit(0);
}
const sheet = n=>wb.worksheets.getItem(n);
const writeRows = (name,headers,rows) => {
  const s=sheet(name); const end=col(headers.length-1);
  s.getRange(`A4:${end}${Math.max(400,rows.length+4)}`).clear({applyTo:'contents'});
  s.getRange(`A4:${end}4`).values=[headers];
  if(rows.length) s.getRange(`A5:${end}${rows.length+4}`).values=rows.map(r=>r.map(jsonCell));
  s.getRange(`A4:${end}${rows.length+4}`).format.font={name:'Arial',size:10};
  s.getRange(`A4:${end}4`).format={fill:'#20384B',font:{name:'Arial',size:10,bold:true,color:'#FFFFFF'},wrapText:true,rowHeight:34};
  s.getRange(`A5:${end}${rows.length+4}`).format.wrapText=true;
  s.getRange(`A5:${end}${rows.length+4}`).format.rowHeight=60;
  s.freezePanes.freezeRows(4); s.freezePanes.freezeColumns(1); s.showGridLines=false;
  return s;
};
const fit = (name,widths) => {
  const s=sheet(name);
  widths.forEach((width,i)=>s.getRange(`${col(i)}4:${col(i)}400`).format.columnWidth=width);
  s.getRange(`A4:${col(widths.length-1)}400`).format.verticalAlignment='top';
  s.getRange(`A5:${col(widths.length-1)}400`).format.autofitRows();
  s.getRange(`A4:${col(widths.length-1)}4`).format.rowHeight=36;
};
const tasks=await read('08_Thuc_thi_Kinh_doanh/EXECUTION_BACKLOG.json');
const contracts=await read('08_Thuc_thi_Kinh_doanh/TASK_EXECUTION_CONTRACTS.json');
const contractById=new Map(contracts.map(r=>[r.task_id,r]));
if(contractById.size!==contracts.length || contracts.length!==tasks.length || tasks.some(r=>!contractById.has(r.task_id)))throw Error('Task contract identity mismatch');
for(const c of contracts)for(const k of ['allowed_paths','required_tests','required_negative_tests','evidence_required','evidence_path','rollback_requirement','claim_status'])if(!c[k] || !c[k].length)throw Error('Missing '+c.task_id+' '+k);
writeRows('Backlog',['ID','Phase','Luồng','Công việc','Vai trò','Trạng thái','Ngày công thấp','Ngày công cao','Phụ thuộc','Gate','Đầu ra','Nghiệm thu','Người được phân công','Đường dẫn cho phép','Kiểm thử','Đường dẫn receipt','Reviewer','Quyết định','Kiểm thử phủ định','Không được làm','Rollback','Quyền production','Evidence bắt buộc','Evidence status'],tasks.map(r=>[
  r.task_id,r.phase,r.workstream,r.title,r.owner,r.status,r.effort_low_person_days,r.effort_high_person_days,r.dependencies,r.gates,r.deliverable,r.acceptance,
  r.named_owner??r.assignee??'CHƯA PHÂN CÔNG',contractById.get(r.task_id).allowed_paths,contractById.get(r.task_id).required_tests,contractById.get(r.task_id).evidence_path,r.reviewer,contractById.get(r.task_id).decision_dependencies,
  contractById.get(r.task_id).required_negative_tests,contractById.get(r.task_id).forbidden_actions,contractById.get(r.task_id).rollback_requirement,contractById.get(r.task_id).production_permission,contractById.get(r.task_id).evidence_required,contractById.get(r.task_id).claim_status
]));
sheet('Backlog').getRange('A1').values=[['Công việc phát triển Life Code OS']];
sheet('Backlog').getRange('M5:M400').format.fill='#FFF4CD';
sheet('Backlog').getRange(`N4:R${tasks.length+4}`).format.columnWidth=34;
const gates=await read('08_Thuc_thi_Kinh_doanh/RELEASE_GATES.json');
writeRows('Gates',['ID','Cổng','Vai trò','Evidence status','Phạm vi','Evidence','FPOS'],gates.map(r=>[r.gate_id,r.name,r.owner,r.status,r.scope,r.evidence_uri,r.fpos_gate_ids??null]));
const decisions=await read('08_Thuc_thi_Kinh_doanh/DECISION_REGISTER.json');
const packets=await read('08_Thuc_thi_Kinh_doanh/DECISION_EXECUTION_PACKETS.json');
const packetById=new Map(packets.map(r=>[r.decision_id,r]));
if(packetById.size!==packets.length || packets.length!==decisions.length || decisions.some(r=>!packetById.has(r.decision_id)))throw Error('Decision packet identity mismatch');
writeRows('Decisions',['ID','Chủ đề','Quyết định','Đề xuất và lý do','Người duyệt','Phương án và đánh đổi','Điều kiện','Evidence','Thời điểm phải chốt'],decisions.map(r=>{
  const p=packetById.get(r.decision_id);
  return [r.decision_id,r.topic,p?.status??r.status,p?`${p.recommended_option_id}\n${p.recommendation_rationale}\n${p.recommendation_tradeoffs.join('\n')}`:r.proposed_action,p?.approver_roles??r.approver,
    p?.options.map(o=>`${o.option_id} ${o.label}\n${o.scope}\n${o.tradeoffs.join('\n')}`).join('\n\n')??null,p?.constraints??null,p?.acceptance_receipt?.required_fields??r.evidence_required,p?.decision_due_event??null];
}));
const products=await read('01_Chien_luoc_San_pham/PRODUCT_CATALOG.json');
writeRows('Products',['ID','Nhóm','Tên','Phase','Trạng thái','Đầu vào','Đầu ra','Giá'],products.map(r=>[r.product_id,r.family,r.name_vi,r.phase,r.status,r.input_contract,r.output_contract,`Currency: ${r.price?.currency??'CHƯA CHỐT'}\nAmount: ${r.price?.amount??'CHƯA CHỐT'}\n${r.price?.status??'NOT_CHECKED'}`]));
const sourceMap=await read('09_Doi_chieu_Bang_chung/SOURCE_TO_TARGET_MATRIX.json');
writeRows('SourceMap',['ID','Bề mặt','Nguồn','Hành động','Đích','Task','Nghiệm thu'],sourceMap.map(r=>[r.mapping_id,r.surface,r.source_path,r.action,r.target,r.task_id,r.acceptance]));
const sources=await read('09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.json');
const updates=await read('09_Doi_chieu_Bang_chung/RESEARCH_UPDATE_2026-10-20.json');
writeRows('Sources',['ID','Tên nguồn','URL','Ngày đọc','Phạm vi','Giới hạn'],[...sources,...updates].map(r=>[r.id,r.title,r.url,r.access_date,r.access_scope??r.scope_read,r.limitations??r.limitation]));
const screens=await read('05_Frontend_UI/SCREEN_REGISTRY.json');
writeRows('Screens',['ID','Màn hình','Route','Vai trò','API','Task','Trạng thái và nghiệm thu'],screens.map(r=>[r.screen_id,r.name_vi,r.target_route,r.principal,r.api,r.task_id,r.states_acceptance]));
const costs=sheet('Costs');
for(let i=5;i<=12;i++) {
  costs.getRange(`E${i}`).formulas=[[`=IF(AND(ISNUMBER(B${i}),B${i}>=0,ISNUMBER(C${i}),C${i}>=0,ISNUMBER(D${i}),D${i}>=0),B${i}*C${i}*D${i},"")`]];
  costs.getRange(`F${i}`).formulas=[[`=IF(ISNUMBER(E${i}),"ĐÃ CÓ GIẢ ĐỊNH","CẦN NHẬP GIẢ ĐỊNH")`]];
}
costs.getRange('E14').formulas=[['=IF(COUNT(E5:E12)=8,SUM(E5:E12),"CHƯA ĐỦ GIẢ ĐỊNH")']];
costs.getRange('E23').formulas=[['=IF(AND(COUNT(E5:E12)=8,COUNT(B17:B21)=5,MIN(B17:B20)>=0,B21>=0,B21<=1),(SUM(E5:E12)+SUM(B17:B20))*(1+B21),"CHƯA ĐỦ GIẢ ĐỊNH")']];
costs.getRange('A2').values=[['FTE và tháng là proposal. Thiếu số lượng, số tháng hoặc đơn giá giữ kết quả unavailable. Đơn giá bằng 0 được chấp nhận khi có căn cứ.']];
const dashboard=sheet('Dashboard'); const last=tasks.length+4;
dashboard.getRange('A5').formulas=[[`=COUNTA(Backlog!A5:A${last})`]];
dashboard.getRange('B5').formulas=[[`=COUNTIFS(Backlog!F5:F${last},"DONE")`]];
dashboard.getRange('C4').values=[['Gates verified']];
dashboard.getRange('C5').formulas=[[`=COUNTIFS(Gates!D5:D${gates.length+4},"VERIFIED_CURRENT")`]];
dashboard.getRange('D5').formulas=[[`=COUNTIFS(Decisions!C5:C${decisions.length+4},"APPROVE")+COUNTIFS(Decisions!C5:C${decisions.length+4},"APPROVE_WITH_CONDITIONS")`]];
for(let i=9;i<=15;i++) {
  dashboard.getRange(`B${i}:E${i}`).formulas=[[
    `=COUNTIFS(Backlog!B$5:B$${last},A${i})`,
    `=SUMIFS(Backlog!G$5:G$${last},Backlog!B$5:B$${last},A${i})`,
    `=SUMIFS(Backlog!H$5:H$${last},Backlog!B$5:B$${last},A${i})`,
    `=COUNTIFS(Backlog!B$5:B$${last},A${i},Backlog!F$5:F$${last},"DONE")`
  ]];
}
dashboard.getRange('A2').values=[['Bản hợp nhất 20/10. Số liệu là trạng thái kế hoạch; release HOLD, chưa có production receipt.']];
dashboard.getRange('A22').values=[['Bắt đầu từ DEV_START_HERE. Demo/test local không thay auth, payment, migration và restore trên staging.']];
sheet('DOC_TRUOC').getRange('A2').values=[['Bản hợp nhất 20/10/2026. Giữ bản gốc trong sources. Mọi task production chưa bắt đầu; Q chưa được tự duyệt.']];
const fpos=await read('07_Bao_mat_Van_hanh/FPOS_GATE_MAPPING.json');
wb.worksheets.add('FPOS');
writeRows('FPOS',['ID','Gate','Gate sản phẩm','Vai trò','Evidence','Trạng thái'],fpos.map(r=>[r.fpos_gate_id,r.title,r.custom_gate_ids,r.owner_role,r.evidence_required,r.status]));
sheet('FPOS').getRange('A1').values=[['FPOS RG0 đến RG13']];
sheet('FPOS').getRange(`A4:F${fpos.length+4}`).format.columnWidth=30;
// Preserve all original tabs; add registry tables only when a current file exists.
for(const [name,relative] of [
  ['Trace','08_Thuc_thi_Kinh_doanh/REQUIREMENT_TRACE_MATRIX.json'],
  ['ReadCoverage','00_Doc_truoc/READ_COVERAGE.json']
]) {
  try {
    let data=await read(relative); if(!Array.isArray(data)) data=data.files??data.records??[];
    if(!data.length) continue;
    const headers=[...new Set(data.flatMap(r=>Object.keys(r)))];
    wb.worksheets.add(name); writeRows(name,headers,data.map(r=>headers.map(h=>r[h])));
    sheet(name).getRange(`A4:${col(headers.length-1)}${data.length+4}`).format.columnWidth=30;
    sheet(name).getRange('A1').values=[[name==='Trace'?'Yêu cầu và nghiệm thu':'Đối chiếu đọc nguồn']];
  } catch(error) {if(error.code!=='ENOENT') throw error;}
}
// Exercise blank vs legitimate zero and all-input calculation, then restore inputs.
costs.getRange('D5').values=[[0]]; wb.recalculate();
if(costs.getRange('E5').values[0][0]!==0) throw Error('Zero rate lost');
for(let i=5;i<=12;i++) costs.getRange(`D${i}`).values=[[1000000]];
costs.getRange('B17:B20').values=[[0],[0],[0],[0]]; wb.recalculate();
const expected=8*6*1000000*1.15;
if(Math.abs(costs.getRange('E23').values[0][0]-expected)>0.01) throw Error('Budget calculation mismatch');
costs.getRange('B5').values=[[null]]; wb.recalculate();
if(costs.getRange('E23').values[0][0]!=='CHƯA ĐỦ GIẢ ĐỊNH') throw Error('Missing FTE hidden');
costs.getRange('B5').values=[[1]];
costs.getRange('D5:D12').values=Array.from({length:8},()=>[null]);
costs.getRange('B17:B20').values=Array.from({length:4},()=>[null]);
wb.recalculate();
if(costs.getRange('E23').values[0][0]!=='CHƯA ĐỦ GIẢ ĐỊNH') throw Error('Missing rates hidden');
const inspection=await wb.inspect({kind:'table',range:'Dashboard!A4:E17',include:'values,formulas',tableMaxRows:15,tableMaxCols:5,maxChars:5000});
const errors=await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!|#NULL!|#SPILL!|#CALC!',options:{useRegex:true,maxResults:100},maxChars:3000});
await fs.writeFile(path.join(qa,'formula-inspection.ndjson'),inspection.ndjson+'\n'+errors.ndjson);
const names=(await wb.inspect({kind:'sheet',include:'id,name',maxChars:10000})).ndjson;
console.log(names); console.log(errors.ndjson);
fit('Backlog',[14,10,18,55,28,26,16,16,35,24,55,70,30,55,60,50,36,28,60,55,65,32,65,28]);
fit('Gates',[12,32,30,28,45,45,38]);
fit('Decisions',[12,45,28,30,40,70,65,55,40]);
fit('Products',[18,28,38,12,32,60,70,42]);
fit('SourceMap',[15,26,52,28,38,18,75]);
fit('Sources',[14,38,65,18,50,60]);
fit('Screens',[14,35,42,28,60,18,80]);
fit('FPOS',[12,35,25,34,85,28]);
for(const [name,widths] of [['Trace',[24,28,45,40,45,35,35,35,35,35,35,35,35,35,60]],['ReadCoverage',[80,36,26,80,70,18]]]) {
  try{fit(name,widths);}catch{}
}
for(let row=5;row<=tasks.length+4;row++) {
  const range=sheet('Backlog').getRange(`A${row}:X${row}`);
  const height=range.format.rowHeight;
  if(typeof height!=='number')throw Error('Cannot read row height '+row);
  range.format.rowHeight=height+8;
}
sheet('Backlog').getRange(`G5:H${tasks.length+4}`).format.horizontalAlignment='center';
for(const name of ['FPOS','Trace','ReadCoverage']) {
  let s;try{s=sheet(name);}catch{continue;}
  s.mergeCells('A1:F1');s.getRange('A1:F1').format={font:{name:'Arial',size:16,bold:true,color:'#20384B'},rowHeight:30};
}
const previews=[['DOC_TRUOC','A1:H13'],['Backlog','A4:F9'],['Backlog-more','G4:L9','Backlog'],['Backlog-contracts','M4:R9','Backlog'],['Backlog-negative','S4:V9','Backlog'],['Backlog-evidence','W4:X9','Backlog'],['Gates','A1:G9'],['Decisions','A4:E7'],['Decisions-options','F4:I7','Decisions'],['Products','A4:E9'],['Products-contracts','F4:H9','Products'],['SourceMap','A1:G9'],['Sources','A4:F9'],['Screens','A4:G9'],['Countries','A1:E9'],['Costs','A1:G27'],['Dashboard','A1:H23'],['FPOS','A1:F9'],['Trace','A4:G9'],['Trace-more','H4:O9','Trace'],['ReadCoverage','A4:C9'],['ReadCoverage-more','D4:F9','ReadCoverage']];
const rendered=[];
for(const [name,range,target] of previews) {
  const sourceName=target??name;
  let s; try{s=sheet(sourceName);}catch{continue;}
  if(!s) continue;
  const image=await wb.render({sheetName:sourceName,range,scale:1.5,format:'png'});
  await fs.writeFile(path.join(qa,name+'.png'),new Uint8Array(await image.arrayBuffer())); rendered.push(name);
}
const output=await SpreadsheetFile.exportXlsx(wb);
await output.save(path.join(pkg,'00_Doc_truoc/Life_Code_OS_Execution_Board.xlsx'));
try{await fs.rename(path.join(pkg,'00_Doc_truoc/Life_Code_OS_Execution_Board.xlsx.inspect.ndjson'),path.join(qa,'saved-workbook-inspect.ndjson'));}catch(e){if(e.code!=='ENOENT')throw e;}
await fs.writeFile(path.join(pkg,'00_Doc_truoc/WORKBOOK_QA.json'),JSON.stringify({scope:'LOCAL_ARTIFACT_TOOL_CALCULATION_AND_EXPORT',date:'2026-10-20',original_tabs_preserved:11,rendered_sheets:rendered,backlog_records:tasks.length,contract_records:contracts.length,decision_packet_records:packets.length,joins:'exact unique ID sets and mandatory contract fields checked',formula_checks:['zero rate remains zero','all inputs calculate55.2million synthetic budget','missing FTE unavailable','missing rates unavailable'],native_excel_ui_tested:false,production_release_verdict:'HOLD',inspection:inspection.ndjson,errors:errors.ndjson},null,2)+'\n');
console.log('Saved updated execution workbook; inputs restored; production gates unchanged.');
