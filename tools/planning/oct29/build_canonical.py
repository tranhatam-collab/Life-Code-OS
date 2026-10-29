"""Merge planning registries without changing source inputs or application code."""
import copy,csv,hashlib,json,re
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
P=ROOT/'docs/upgrade/2026-10-29'
OLD=ROOT/'docs/upgrade/2026-10-20'
S=ROOT/'docs/upgrade/sources/2026-10-29'
V3=S/'v3/package/LIFE_CODE_OS_ALL_IN_ONE_V3_2026-10-29'
def read(p):return json.loads(p.read_text())
def dump(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def rel(p):return p.relative_to(ROOT).as_posix()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def refs(v):return v if isinstance(v,list) else [s for s in re.split(r'[;,\s]+',v or '') if s]
def source(p,record):return {'package':('LOCAL_R2' if OLD in p.parents else 'V3_INCOMING'),'path':rel(p),'sha256':sha(p),'record_id':record}
def csvout(p,rows,headers):
 with p.open('w',newline='',encoding='utf-8-sig') as f:
  w=csv.DictWriter(f,fieldnames=headers);w.writeheader()
  for row in rows:w.writerow({k:json.dumps(row.get(k),ensure_ascii=False) if isinstance(row.get(k),(list,dict)) else row.get(k) for k in headers})
def dag(rows):
 by={r['task_id']:r for r in rows};order=[];vis=set();active=set()
 def visit(k):
  assert k in by,('missing',k)
  if k in vis:return
  assert k not in active,('cycle',k);active.add(k)
  for d in by[k]['task_dependencies']:visit(d)
  active.remove(k);vis.add(k);order.append(k)
 for k in by:visit(k)
 return order
def main():
 oldpath=OLD/'08_Thuc_thi_Kinh_doanh/EXECUTION_BACKLOG.json';incomingpath=V3/'09_EXECUTION/BACKLOG_UNIFIED.json'
 old=read(oldpath);incoming=read(incomingpath);local={r['task_id']:r for r in old};remote={r['task_id']:r for r in incoming}
 oldcontracts={r['task_id']:r for r in read(OLD/'08_Thuc_thi_Kinh_doanh/TASK_EXECUTION_CONTRACTS.json')}
 assert len(local)==156 and len(remote)==280
 tasks=[];corrections=[]
 for k in dict.fromkeys([r['task_id'] for r in incoming]+[r['task_id'] for r in old]):
  chosen=copy.deepcopy(local.get(k,remote.get(k)));r=copy.deepcopy(chosen)
  rawrefs=refs(chosen.get('dependencies'));ts=[x for x in rawrefs if x in local or x in remote];qs=[x for x in rawrefs if re.fullmatch('Q[0-9]+',x)];gs=[x for x in rawrefs if re.fullmatch('G[0-9]+',x)]
  assert len(ts)+len(qs)+len(gs)==len(rawrefs),(k,rawrefs)
  if k in local and k in remote and refs(local[k].get('dependencies'))!=refs(remote[k].get('dependencies')):corrections.append({'task_id':k,'retained_local_dependencies':refs(local[k].get('dependencies')),'incoming_dependencies':refs(remote[k].get('dependencies')),'reason':'Preserve local P0 containment/source authority order; incoming raw edge retained for audit'})
  prov=[]
  if k in local:prov.append({**source(oldpath,k),'raw_record':local[k]})
  if k in remote:prov.append({**source(incomingpath,k),'raw_record':remote[k]})
  rich=oldcontracts.get(k,{})
  effective_qs=list(dict.fromkeys(qs+rich.get('decision_dependencies',[])))
  effective_gs=list(dict.fromkeys(gs+refs(chosen.get('gates'))+rich.get('custom_gate_ids',[])))
  r.update({'canonical_version':'2026-10-29.r1','origin':chosen.get('origin','LOCAL_R2'),'task_dependencies':ts,'decision_dependencies':effective_qs,'gate_dependencies':effective_gs,'dependency_predicate_basis':'Union typed backlog predicates with preserved richer local task contract predicates; original records remain raw','source_records':prov,'current_execution_evidence':'NOT_CHECKED','assignee_name':None,'reviewer_name':None,'integration_work_order_ids':[],'production_authorized':False})
  tasks.append(r)
 assert len(tasks)==296
 workorders=read(P/'execution/INTEGRATION_WORK_ORDERS.json')
 for r in tasks:r['integration_work_order_ids']=[w['task_id'] for w in workorders if r['task_id'] in w['source_task_ids']]
 for w in workorders:
  r=copy.deepcopy(w);r.update({'canonical_version':'2026-10-29.r1','origin':'INTEGRATION_REFINEMENT','current_execution_evidence':'NOT_CHECKED','production_authorized':False,'source_records':[{'package':'LOCAL_2026_10_29','path':rel(P/'execution/INTEGRATION_WORK_ORDERS.json'),'sha256':sha(P/'execution/INTEGRATION_WORK_ORDERS.json'),'record_id':w['task_id']} ]});tasks.append(r)
 order=dag(tasks)
 dump(P/'execution/BACKLOG_UNIFIED.json',tasks)
 csvout(P/'execution/BACKLOG_UNIFIED.csv',tasks,['task_id','origin','phase','workstream','title','owner','owner_role','assignee_name','status','current_execution_evidence','task_dependencies','decision_dependencies','gate_dependencies','integration_work_order_ids','effort_low_person_days','effort_high_person_days','estimate_rollup','acceptance','deliverable','production_authorized'])
 dump(P/'execution/TASK_DEPENDENCY_GRAPH.json',{'version':'2026-10-29.r1','node_count':len(tasks),'scope':'task edges only; decisions/gates checked separately, never treated as completed task nodes','topological_order':order,'nodes':[{'task_id':r['task_id'],'task_dependencies':r['task_dependencies'],'decision_dependencies':r['decision_dependencies'],'gate_dependencies':r['gate_dependencies']} for r in tasks],'missing_task_edges':[],'cycles':[],'retained_dependency_corrections':corrections})
 methods=read(P/'backend/FORMULA_METHOD_EXECUTION_MATRIX.json')['rows']
 source_methods=read(V3/'03_KNOWLEDGE/METHOD_INTEGRATION_REGISTER_V3.json')
 if isinstance(source_methods,dict):source_methods=source_methods.get('methods',source_methods.get('rows',[]))
 methodtask={f'V3-MTH-{i+1:03}':r for i,r in enumerate(source_methods)}
 contracts=[]
 for r in tasks:
  k=r['task_id'];base=copy.deepcopy(oldcontracts.get(k,{}));mapped=[w for w in workorders if w['task_id'] in r.get('integration_work_order_ids',[])];m=methodtask.get(k);special=[]
  if m:
   matched=next((x for x in methods if x['method_id']==m.get('method_id')),None)
   if matched:special=[{'registry':'backend/FORMULA_METHOD_EXECUTION_MATRIX.json','record_id':matched['method_id'],'exact_contract':matched}]
  role=r.get('owner_role',r.get('owner','Tech Lead + QA'));wself=next((w for w in workorders if w['task_id']==k),None)
  context=mapped+([wself] if wself else [])
  acceptance=[r.get('acceptance')] if r.get('acceptance') else r.get('acceptance_criteria',[])
  positive=list(dict.fromkeys([x for w in context for x in w['tests']['positive']]+acceptance))
  negative=list(dict.fromkeys([x for w in context for x in w['tests']['negative']]))
  if not negative:negative=['Missing required data or permission must fail with a typed reason; stale versions must not overwrite; retry must not duplicate the scoped business effect.']
  if not positive:positive=[r['title']+'; independent reviewer compares delivered result with source scope and acceptance.']
  paths=['workers/life-code-api/src/','workers/life-code-api/tests/','docs/schemas/'] if any(x in role.lower() for x in ['backend','method','security','platform','data']) else ['docs/','site-templates/','docs/report-templates/']
  if any(x in role.lower() for x in ['frontend','ux','web','mobile']):paths=['app.js','dashboard.html','bat-dau.html','account.html','style.css']
  if k in oldcontracts:base['preserved_local_source_contract']=copy.deepcopy(oldcontracts[k])
  base.update({'task_id':k,'handoff_version':'2026-10-29.r1','source_record_refs':[{x:y for x,y in s.items() if x!='raw_record'} for s in r['source_records']],'accountable_owner_role':role,'assignee_name':None,'independent_reviewer_role':r.get('reviewer_role',r.get('independent_reviewer_role',r.get('reviewer','Independent QA + relevant functional owner'))),'reviewer_name':None,'task_dependencies':r['task_dependencies'],'decision_dependencies_2026_10_29':r['decision_dependencies'],'gate_dependencies_2026_10_29':r['gate_dependencies'],'integration_contract_refs':[w['task_id'] for w in context],'method_contracts':special,'scope_title':r['title'],'acceptance_2026_10_29':positive,'negative_acceptance_2026_10_29':negative,'existing_repository_paths_for_scoped_review':paths,'proposed_new_paths':['packages/method-core/','apps/web/','services/report-renderer/'] if m else [],'path_authority':'Review targets only; exact file allowlist must be accepted on a clean candidate before edits. No application edits authorized by this plan.','evidence_path_2026_10_29':f'evidence/{k}/<candidate-digest>/receipt.json','required_evidence_2026_10_29':['repo/branch/HEAD + worktree diff digest','source+artifact+configuration digests','commands,exit codes,pass/fail/skip and environment','positive+negative contract tests','independent reviewer and scoped decision/gate receipt','rollback verification or fail-closed disablement'],'rollback_2026_10_29':(wself or {}).get('rollback_plan','Revert only the scoped candidate diff; do not restore unsafe data/auth paths or resurrect deleted data. Migration requires separate rehearsal and reconciliation.'),'dispatch_state':'NOT_DISPATCHED','implementation_evidence_status':'NOT_CHECKED','production_permission':False,'production_permission_normalization':'Explicit false for this planning handoff; original SEPARATE_APPROVAL_REQUIRED remains in preserved_local_source_contract where applicable'})
  contracts.append(base)
 dump(P/'execution/TASK_DEV_CONTRACTS.json',contracts)
 # Source requirements retain their own IDs and raw records. Expanded registry rows are design trace, never execution proof.
 traces=[]
 for r in read(OLD/'08_Thuc_thi_Kinh_doanh/REQUIREMENT_TRACE_MATRIX.json'):
  traces.append({'trace_id':'LOCAL_R2:'+r['requirement_id'],'origin':'LOCAL_R2','requirement':r['requirement_statement'],'task_ids':r['task_ids'],'registry_ref':r.get('screen_ids') or r.get('product_ids'),'raw_record':r,'evidence_status':'NOT_CHECKED'})
 reqwork={1:1,2:2,3:5,4:9,5:7,6:8,7:8,8:8,9:8,10:8,11:8,12:6,13:7,14:9,15:9,16:9,17:14,18:17,19:15,20:10,21:16,22:19,23:3,24:4,25:5,26:13,27:15,28:1,29:11,30:20}
 for r in read(V3/'02_RECONCILIATION/REQUIREMENTS_TRACE_V3.json'):
  n=int(r['request_id'][-3:]);w=7 if 31<=n<=53 else 14 if n>=54 else reqwork[n]
  traces.append({'trace_id':'INCOMING_V3:'+r['request_id'],'origin':'INCOMING_V3','requirement':r['requirement'],'task_ids':[f'INT29-{w:03}'],'registry_ref':rel(V3/r['artifact']),'raw_record':r,'evidence_status':'NOT_CHECKED'})
 for p,idkey,w in [(P/'product/PRODUCT_EXECUTION_CONTRACTS.json','product_id',17),(P/'product/SCREEN_EXECUTION_CONTRACTS.json','screen_id',15)]:
  for r in read(p):traces.append({'trace_id':idkey.upper()+':'+r[idkey],'origin':'CANONICAL_REGISTRY','requirement':'Complete execution contract for '+r[idkey],'task_ids':[f'INT29-{w:03}'],'registry_ref':rel(p)+'#'+r[idkey],'evidence_status':'NOT_CHECKED'})
 for m in methods:traces.append({'trace_id':'METHOD:'+m['method_id'],'origin':'CANONICAL_REGISTRY','requirement':m['name_vi'],'task_ids':['INT29-005',next(k for k,v in methodtask.items() if v['method_id']==m['method_id'])],'registry_ref':'backend/FORMULA_METHOD_EXECUTION_MATRIX.json#'+m['method_id'],'evidence_status':'NOT_CHECKED'})
 api=read(P/'backend/OPENAPI_UNIFIED_TARGET.json')
 for path,item in api['paths'].items():
  for verb,r in item.items():
   if verb.lower() not in ['get','post','put','patch','delete','head','options','trace']:continue
   traces.append({'trace_id':'API:'+r['operationId'],'origin':'CANONICAL_REGISTRY','requirement':verb.upper()+' '+path,'task_ids':['INT29-010'],'registry_ref':'backend/OPENAPI_UNIFIED_TARGET.json#'+r['operationId'],'evidence_status':'NOT_CHECKED'})
 ids={r['task_id'] for r in tasks};assert all(set(t['task_ids'])<=ids for t in traces)
 assert len({t['trace_id'] for t in traces})==len(traces)
 dump(P/'execution/REQUIREMENT_TRACE_UNIFIED.json',traces);csvout(P/'execution/REQUIREMENT_TRACE_UNIFIED.csv',traces,['trace_id','origin','requirement','task_ids','registry_ref','evidence_status'])
 backward=[]
 for r in tasks:
  c=next(x for x in contracts if x['task_id']==r['task_id']);direct=[t['trace_id'] for t in traces if r['task_id'] in t['task_ids']]
  backward.append({'task_id':r['task_id'],'source_requirement_kind':'SOURCE_BACKLOG_SCOPE_AND_ACCEPTANCE' if r['origin']!='INTEGRATION_REFINEMENT' else 'SOURCE_TASK_INTEGRATION_REFINEMENT','source_requirement_text':r['title'],'source_acceptance_text':r.get('acceptance',r.get('acceptance_criteria')),'source_record_refs':c['source_record_refs'],'dev_contract_ref':'execution/TASK_DEV_CONTRACTS.json#'+r['task_id'],'direct_formal_requirement_trace_ids':direct,'integration_work_order_ids':r.get('integration_work_order_ids',[]),'scope_trace_status':'EXACT_SOURCE_SCOPE_RETAINED','formal_requirement_trace_status':'DIRECT_LINK_PRESENT' if direct else 'REVIEW_BEFORE_FEATURE_DISPATCH','receipt_status':'NOT_CHECKED','dispatch_rule':'Retained source task scope is reviewable. Before feature implementation dispatch, reviewer must accept exact requirement/contract/test linkage; a thematic or parent work-order link is not independent proof.'})
 dump(P/'execution/TASK_BACKWARD_TRACE.json',backward)
 csvout(P/'execution/TASK_BACKWARD_TRACE.csv',backward,['task_id','source_requirement_kind','source_requirement_text','source_acceptance_text','dev_contract_ref','direct_formal_requirement_trace_ids','integration_work_order_ids','scope_trace_status','formal_requirement_trace_status','receipt_status'])
 dump(P/'execution/ESTIMATE_MODEL.json',{'rules':['No additive portfolio total until parent/refinement scope and capacity are accepted','V1 historical ranges preserved, not repriced','V2 68 records refine parent tasks; not additive','V3 72 records require estimate','Local16 preserved; INT20 refine integration scope, not additive','Calendar durations need actual available role capacity, dependency constraints, parallelism and contingency','Unknown rates/currency/quotes remain null; never automatically convert USD to VND'],'groups':dict(Counter(r['origin'] for r in tasks)),'portfolio_total_person_days':None,'committed_delivery_date':None,'budget':None,'budget_currency':None,'approval_status':'PENDING'})
 census=read(S/'extracted/SOURCE_CENSUS.json');cross=[]
 for r in census['files']:
  path=r['path'];target='MASTER_PLAN.md';work='INT29-020'
  for needle,dest,wi in [('BACKLOG','execution/BACKLOG_UNIFIED.json','INT29-003'),('DECISION','execution/DECISION_EXECUTION_PACKETS.json','INT29-004'),('METHOD','backend/FORMULA_METHOD_EXECUTION_MATRIX.json','INT29-005'),('BACKEND','backend/BACKEND_DEV_HANDOFF.md','INT29-010'),('DEMO','backend/BACKEND_DEV_HANDOFF.md','INT29-013'),('NUMBERS','backend/FORMULA_METHOD_EXECUTION_MATRIX.json','INT29-008'),('LIFETIME','MASTER_PLAN.md','INT29-009'),('PRODUCT','product/PRODUCT_UX_REPORT_HANDOFF.md','INT29-015'),('ACADEMY','product/AI_REPORT_ACADEMY_HANDOFF.md','INT29-019')]:
   if needle.lower() in path.lower():target=dest;work=wi;break
  cross.append({**r,'canonical_destination':'docs/upgrade/2026-10-29/'+target,'work_order_id':work,'integration_action':'Preserve exact bytes; use canonical contract and trace for implementation','source_text_is_execution_authority':False})
 dump(P/'evidence/SOURCE_TO_CANONICAL_CROSSWALK.json',cross)
 csvout(P/'evidence/SOURCE_TO_CANONICAL_CROSSWALK.csv',cross,['path','sha256','bytes','read_status','canonical_destination','work_order_id','integration_action'])
 dump(P/'evidence/CANONICAL_BUILD_RECEIPT.json',{'source_tasks':296,'integration_refinements':20,'total_planning_records':len(tasks),'source_counts':dict(Counter(r['origin'] for r in tasks)),'task_contracts':len(contracts),'trace_rows':len(traces),'trace_origins':dict(Counter(t['origin'] for t in traces)),'task_cycles':0,'missing_task_refs':0,'dependency_corrections':corrections,'release_status':'HOLD','application_modified_by_builder':False})
 print(json.dumps({'tasks':len(tasks),'contracts':len(contracts),'traces':len(traces),'corrections':len(corrections)},ensure_ascii=False))
if __name__=='__main__':main()
