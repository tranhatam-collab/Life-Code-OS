"""Verify integrated planning artifacts. Pure stdlib; no packaged code execution.

--record writes the review receipt; --seal additionally seals canonical files.
Default is read-only. --portable skips Git/protected application-file checks in
the planning-only export; all delivered planning/source bytes remain checked.
"""
import argparse,csv,hashlib,json,re,subprocess
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

ROOT=Path(__file__).resolve().parents[3]
P=ROOT/'docs/upgrade/2026-10-29';S=ROOT/'docs/upgrade/sources/2026-10-29';O=ROOT/'docs/upgrade/2026-10-20'
CHECKS=[]
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def check(k,v,details=None):CHECKS.append({'check':k,'passed':bool(v),'details':details})
def rows(p):
 d=read(p)
 if isinstance(d,list):return d
 for k in ['rows','entries','files']:
  if isinstance(d.get(k),list):return d[k]
 return []
def main():
 a=argparse.ArgumentParser();a.add_argument('--record',action='store_true');a.add_argument('--seal',action='store_true');a.add_argument('--portable',action='store_true');a.add_argument('--preflight',action='store_true');args=a.parse_args()
 intake=read(S/'SOURCE_RECEIPT.json')
 if not args.portable:
  git=lambda *x:subprocess.check_output(['git',*x],cwd=ROOT,text=True).strip()
  check('exact repository identity',git('rev-parse','--show-toplevel')==str(ROOT) and git('remote','get-url','origin')==intake['remote'] and git('branch','--show-current')==intake['branch'] and git('rev-parse','HEAD')==intake['head'])
  for r in intake['protected_runtime_worktree_files']:
   p=ROOT/r['path'];check('protected runtime unchanged '+r['path'],p.is_file() and sha(p)==r['sha256'])
 for key,records in intake['files'].items():
  base=S/key/'package';actual={p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()}
  check('exact source ZIP file set '+key,actual=={r['path'] for r in records})
  for r in records:
   p=base/r['path'];check('source byte '+key+'/'+r['path'],p.is_file() and not p.is_symlink() and sha(p)==r['sha256'] and p.stat().st_size==r['bytes'])
 for r in intake['archives']:
  p=S/'archives'/Path(r['supplied_path']).name;check('supplied archive preserved '+r['id'],sha(p)==r['source_zip_sha256'])
 for r in intake['messages']:check('handoff message preserved '+r['path'],sha(S/r['path'])==r['sha256'])
 check('old216 exact file set',{p.relative_to(ROOT).as_posix() for p in O.rglob('*') if p.is_file()}=={r['path'] for r in intake['existing_r2_files']})
 for r in intake['existing_r2_files']:check('old216 byte '+r['path'],sha(ROOT/r['path'])==r['sha256'])
 tasks=read(P/'execution/BACKLOG_UNIFIED.json');contracts=read(P/'execution/TASK_DEV_CONTRACTS.json');graph=read(P/'execution/TASK_DEPENDENCY_GRAPH.json');traces=read(P/'execution/REQUIREMENT_TRACE_UNIFIED.json');back=read(P/'execution/TASK_BACKWARD_TRACE.json');wo=read(P/'execution/INTEGRATION_WORK_ORDERS.json');dec=read(P/'execution/DECISION_EXECUTION_PACKETS.json')
 ids={r['task_id'] for r in tasks};by={r['task_id']:r for r in tasks};cs={r['task_id']:r for r in contracts};nodes={r['task_id']:r for r in graph['nodes']};decs={r['decision_id'] for r in dec}
 check('316 unique backlog/contract/backward IDs',len(tasks)==len(contracts)==len(back)==len(ids)==316 and set(cs)==ids=={r['task_id'] for r in back})
 check('296 source tasks +20 integration orders',len([r for r in tasks if r['origin']!='INTEGRATION_REFINEMENT'])==296 and len(wo)==20)
 check('45 decision IDs',decs=={f'Q{i}' for i in range(1,46)})
 oldcontracts=read(O/'08_Thuc_thi_Kinh_doanh/TASK_EXECUTION_CONTRACTS.json');qcount=0
 for old in oldcontracts:
  k=old['task_id'];qcount+=len(old['decision_dependencies'])
  check('old contract snapshot exact '+k,cs[k].get('preserved_local_source_contract')==old)
  check('rich decision predicates retained '+k,set(old['decision_dependencies'])<=set(by[k]['decision_dependencies']) and set(old['decision_dependencies'])<=set(cs[k]['decision_dependencies_2026_10_29']) and set(old['decision_dependencies'])<=set(nodes[k]['decision_dependencies']))
 check('674 local decision predicates counted',qcount==674)
 order=graph['topological_order'];positions={k:i for i,k in enumerate(order)}
 check('DAG complete and no cycles',set(order)==ids and len(order)==316 and all(positions[d]<positions[r['task_id']] for r in tasks for d in r['task_dependencies']))
 check('all task/decision/gate refs resolve',all(set(r['task_dependencies'])<=ids and set(r['decision_dependencies'])<=decs and set(r['gate_dependencies'])<={f'G{i:02}' for i in range(1,13)} for r in tasks))
 check('all316 deployment permissions false',all(r.get('production_authorized') is False for r in tasks) and all(r.get('production_permission') is False for r in contracts))
 pointererrors=[]
 for r in tasks:
  for s in r['source_records']:
   p=ROOT/s['path'];items=rows(p)
   if not p.is_file() or sha(p)!=s.get('sha256') or not any(x.get('task_id')==s['record_id'] for x in items):pointererrors.append([r['task_id'],s])
 check('all task source record hashes and IDs current',not pointererrors,pointererrors[:3])
 methods=read(P/'backend/FORMULA_METHOD_EXECUTION_MATRIX.json')['rows'];mi={r['method_id']:r for r in methods}
 check('62 unique method contracts',len(methods)==len(mi)==62)
 check('62 task method snapshots exact',sum(bool(c['method_contracts']) for c in contracts)==62 and all(m['exact_contract']==mi[m['record_id']] for c in contracts for m in c['method_contracts']))
 check('407 unique trace records/validtaskrefs',len(traces)==len({r['trace_id'] for r in traces})==407 and all(set(r['task_ids'])<=ids for r in traces))
 formal={k for r in traces for k in r['task_ids']};check('backward trace differentiates direct and source-scope links',len(formal)==149 and all(bool(r['direct_formal_requirement_trace_ids'])==(r['task_id'] in formal) for r in back))
 olddec=read(O/'08_Thuc_thi_Kinh_doanh/DECISION_EXECUTION_PACKETS.json');di={r['decision_id']:r for r in dec};check('Q1-Q20 object exact',all(di[r['decision_id']]==r for r in olddec))
 for current,prior,key,n in [('product/PRODUCT_EXECUTION_CONTRACTS.json','01_Chien_luoc_San_pham/PRODUCT_EXECUTION_EXTENSION.json','product_id',28),('product/SCREEN_EXECUTION_CONTRACTS.json','05_Frontend_UI/SCREEN_EXECUTION_EXTENSION.json','screen_id',69),('product/NINE_LEVEL_REPORT_CONTRACTS.json','06_AI_Bao_cao/NINE_LEVEL_REPORT_CONTRACTS.json','level',9)]:
  cur=read(P/current);prev=read(O/prior)
  if key=='level' and key not in cur[0]:key='level_id' if 'level_id' in cur[0] else 'report_id'
  try:
   ci={r[key]:r for r in cur};check('registry count/preserved fields '+current,len(cur)==len(ci)==n and all(all(ci[r[key]].get(k)==v for k,v in r.items()) for r in prev))
  except KeyError:check('registry keys '+current,False,list(cur[0]))
 api=read(P/'backend/OPENAPI_UNIFIED_TARGET.json');oldapi=read(O/'04_Backend_API/openapi.resolved.json');ops=[];refs=[]
 def walk(x):
  if isinstance(x,dict):
   for k,v in x.items():
    if k=='$ref':refs.append(v)
    else:walk(v)
  elif isinstance(x,list):
   for v in x:walk(v)
 walk(api);badrefs=[]
 for ref in refs:
  if not ref.startswith('#/'):badrefs.append(ref);continue
  cur=api
  try:
   for s in ref[2:].split('/'):cur=cur[s.replace('~1','/').replace('~0','~')]
  except (KeyError,TypeError):badrefs.append(ref)
 for path,item in api['paths'].items():
  for verb,op in item.items():
   if verb in ['get','post','put','patch','delete','head','options','trace']:ops.append((path,verb,op))
 check('99 unique API operation IDs;68schemas',len(ops)==len({x[2]['operationId'] for x in ops})==99 and len(api['components']['schemas'])==68)
 check('API internal refs close',not badrefs,badrefs)
 check('API no double version prefix',not any(p.startswith('/api/v2') for p,_,_ in ops))
 check('9 local canonical schemas exact',all(api['components']['schemas'][name]==oldapi['components']['schemas'][name] for name in ['Claim','Metric','ProfileVersion','MethodRelease','MethodResult','JobEnvelope','ReportSnapshot','ReleaseReceipt','Tail80Result']))
 for stem,key in [('BACKLOG_UNIFIED','task_id'),('REQUIREMENT_TRACE_UNIFIED','trace_id'),('TASK_BACKWARD_TRACE','task_id')]:
  with (P/'execution'/f'{stem}.csv').open(encoding='utf-8-sig',newline='') as f:csvrows=list(csv.DictReader(f))
  js=read(P/'execution'/f'{stem}.json');check('CSV ID parity '+stem,[r[key] for r in csvrows]==[r[key] for r in js])
 cross=read(P/'evidence/SOURCE_TO_CANONICAL_CROSSWALK.json');check('827 source-to-canonical paths resolve',len(cross)==827 and all((ROOT/r['canonical_destination']).is_file() and (ROOT/r['path']).is_file() and sha(ROOT/r['path'])==r['sha256'] for r in cross))
 badlinks=[]
 for p in P.rglob('*.md'):
  for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',p.read_text()):
   target=target.strip('<>');target=target.split('#')[0]
   if not target or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',target):continue
   resolved=p.parent/unquote(target)
   if resolved.resolve()==(P/'evidence/FINAL_VERIFICATION.json').resolve() and (args.record or args.seal):continue
   if not resolved.exists():badlinks.append({'file':str(p.relative_to(P)),'target':target})
 check('canonical markdown local links resolve',not badlinks,badlinks)
 for p in P.rglob('*.json'):
  try:read(p)
  except Exception as e:check('JSON parse '+str(p),False,str(e))
 if not args.preflight:
  for name in ['DOCUMENT_QA.json','WORKBOOK_QA.json','FINAL_PROGRAM_QA.json']:
   p=P/'evidence'/name;check('QA receipt exists '+name,p.is_file())
   if p.is_file():check('QA receipt completed PASS '+name,read(p).get('status')=='PASS')
  for name,fields in [('DOCUMENT_QA.json',['docx','pdf']),('WORKBOOK_QA.json',['workbook'])]:
   p=P/'evidence'/name
   if p.is_file():
    q=read(p)
    for field in fields:
     item=q.get(field,{})
     if item.get('path') and item.get('sha256'):check('QA exact export hash '+field,(ROOT/item['path']).is_file() and sha(ROOT/item['path'])==item['sha256'])
    if q.get('artifact_path') and q.get('artifact_sha256'):check('QA exact export hash flat '+name,sha(ROOT/q['artifact_path'])==q['artifact_sha256'])
    for item in q.get('sources',[]):
     if item.get('path') and item.get('sha256'):check('document source hash '+item['path'],sha(ROOT/item['path'])==item['sha256'])
    def visual_hashes(x):
     if isinstance(x,dict):
      if x.get('delivered_png'):check('delivered render hash '+x['delivered_png'],sha(ROOT/x['delivered_png'])==x.get('png_sha256',x.get('sha256')))
      for v in x.values():visual_hashes(v)
     elif isinstance(x,list):
      for v in x:visual_hashes(v)
    visual_hashes(q.get('visual_review',{}))
  coverage=read(P/'evidence/READ_COVERAGE_UNIFIED.json')
  check('all827 source entries have read receipts',coverage['files_with_read_receipt']==827 and coverage['unique_sha256']==447 and not coverage['missing_read_receipt_paths'])
  ledgers={x['receipt']:x['receipt_sha256'] for r in coverage['files'] for x in r['read_receipts']}
  check('read coverage receipts current',all(sha(ROOT/path)==digest for path,digest in ledgers.items()))
  packets=read(P/'execution/WORK_ORDER_DRAFT_PACKETS.json');admission=read(P/'evidence/WORK_ORDER_ADMISSION_REVIEW.json')
  check('20 concrete drafts remain proposed not falsely admitted',len(packets)==20 and admission['schema_valid_packets']==20 and admission['ready_for_scoped_dev']==0 and all(r['status']=='PROPOSED_NOT_DISPATCHED' and r['release']['production_permission'] is False for r in packets))
  for ext in ['docx','pdf']:
   p=P/'exports'/f'Life_Code_OS_Master_Dev_Handoff_2026-10-29.{ext}';check('final export present '+ext,p.is_file() and p.stat().st_size>1000)
  p=P/'exports/Life_Code_OS_Dev_Execution_Board_2026-10-29.xlsx';check('final workbook present',p.is_file() and p.stat().st_size>1000)
 manifest=P/'MANIFEST.json'
 if manifest.exists() and not args.record and not args.seal:
  records=read(manifest)['files'];actual={p.relative_to(P).as_posix() for p in P.rglob('*') if p.is_file() and p!=manifest}
  check('canonical sealed file set exact',actual=={r['path'] for r in records})
  for r in records:check('sealed hash '+r['path'],sha(P/r['path'])==r['sha256'])
 summary={'checked_on':'2026-10-29','scope':'LOCAL_PLANNING_INTEGRATION_ONLY' if not args.portable else 'PORTABLE_PLANNING_BUNDLE_ONLY','passed':sum(r['passed'] for r in CHECKS),'failed':sum(not r['passed'] for r in CHECKS),'source_zip_entries':827,'old_planning_files':216,'protected_runtime_files_checked':0 if args.portable else 6,'tasks':316,'formal_trace_rows':407,'formal_trace_direct_tasks':149,'backward_source_scope_tasks':316,'checks':CHECKS,'release_status':'HOLD','app_code_or_deployment_verified':False}
 if args.record or args.seal:dump(P/'evidence/FINAL_VERIFICATION.json',summary)
 if args.seal and not summary['failed']:
  files=[{'path':p.relative_to(P).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(P.rglob('*')) if p.is_file() and p!=manifest]
  dump(manifest,{'format':'lifecode-integrated-planning-manifest/1','version':'2026-10-29.r1','self_excluded':True,'files':files})
 print(json.dumps({k:v for k,v in summary.items() if k!='checks'},ensure_ascii=False));
 for x in CHECKS:
  if not x['passed']:print('FAIL',json.dumps(x,ensure_ascii=False))
 return bool(summary['failed'])
if __name__=='__main__':raise SystemExit(main())
