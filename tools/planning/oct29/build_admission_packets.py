"""Prepare concrete, schema-valid work-order drafts; never marks DEV admission ready."""
import hashlib,json
from pathlib import Path
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[3];P=ROOT/'docs/upgrade/2026-10-29';E=P/'execution'
def read(p):return json.loads(p.read_text())
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def main():
 schema=read(E/'WORK_ORDER_TEMPLATE.json');Draft202012Validator.check_schema(schema);validator=Draft202012Validator(schema)
 intake=read(ROOT/'docs/upgrade/sources/2026-10-29/SOURCE_RECEIPT.json');tasks={r['task_id']:r for r in read(E/'BACKLOG_UNIFIED.json')};packets=[];admission=[]
 for w in read(E/'INTEGRATION_WORK_ORDERS.json'):
  k=w['task_id'];refs=[]
  for tid in [k]+w['source_task_ids']:
   for r in tasks[tid]['source_records']:
    s={'package_id':r['package'],'path':r['path'],'sha256':r['sha256'],'source_record_id':r['record_id']}
    if s not in refs:refs.append(s)
  p={'work_order_id':k,'source_task_ids':w['source_task_ids'],'title':w['title'],'status':'PROPOSED_NOT_DISPATCHED',
   'scope':{'capabilities':[w['scope']],'cohort':'SYNTHETIC_PREPARATION_ONLY; actual product cohort pending acceptance','environment':'DOCUMENTATION','purpose':'Chuẩn bị đặc tả, tiêu chí và bằng chứng cho work order; chưa cấp quyền sửa ứng dụng hoặc tích hợp provider','data_classes':['public_planning_sources','synthetic_fixture_design']},
   'exclusions':['application/runtime edits until a scoped candidate work order is accepted','production/provider/database writes','real personal data','implicit approval of methods/pricing/territory'],
   'owner':{'role':w['owner_role'],'name':None,'accepted_at':None},'reviewer':{'role':w['independent_reviewer_role'],'name':None,'accepted_at':None},
   'authority':{'work_scope_authorized':True,'decision_receipts':[],'provider_access_authorized':False,'production_action_authorized':False},
   'baseline':{'repo_root':intake['repo_root'],'remote':intake['remote'],'branch':intake['branch'],'full_head_sha':intake['head'],'worktree_status_receipt':'docs/upgrade/sources/2026-10-29/SOURCE_RECEIPT.json','candidate_artifact_sha256':None,'source_bundle_receipt':'docs/upgrade/sources/2026-10-29/SOURCE_RECEIPT.json','target_environment':'DOCUMENTATION_ONLY_UNTIL_SCOPED_DISPATCH'},
   'source_refs':refs,'dependencies':{'task_dependencies':w['task_dependencies'],'decision_dependencies':w['decision_dependencies'],'gate_dependencies':w['gate_dependencies'],'parent_rollup_ids':w['source_task_ids'],'raw_source_dependencies':w['source_refs'],'scoped_completion_rule':w['dependency_scope_rule']},
   'version_bundle':{x:None for x in schema['properties']['version_bundle']['required']},
   'deliverables':[{'path':w['evidence_path'],'artifact_kind':'scoped work-order receipt + spec/diff/tests','review_method':'Compare acceptance with source, positive/negative cases, independent review and rollback evidence'}],
   'acceptance':[{'criterion':s,'expected_result':s,'source_or_decision_ref':'execution/INTEGRATION_WORK_ORDERS.json#'+k} for s in w['acceptance_criteria']],
   'tests':{'positive':w['tests']['positive'],'negative':w['tests']['negative'],'boundary':['Check missing/ambiguous/stale input within this exact work-order scope; final fixture IDs selected at dispatch'],'privacy_and_auth':['Synthetic data only in preparation; permission-negative scenarios required before integration'],'failure_and_recovery':[w['rollback_plan']],'performance_class':None,'fixture_provenance':'Source corpus versions preserved; new fixtures must carry synthetic label, source/rule/config digest and expected result','skips_with_reasons':[]},
   'evidence':{'directory':w['evidence_path'],'receipt_fields':['candidate SHA','artifact/source/config digests','commands/env/exit status','pass/fail/skip and expected/actual','independent reviewer','decision/gate scope','rollback proof'],'independent_review_receipt':None,'status':'NOT_CHECKED'},
   'rollback':{'trigger':'Acceptance, authorization, source identity or reconciliation fails','operator_role':w['owner_role'],'procedure':w['rollback_plan'],'data_reconciliation':'Record exact affected scope; quarantine unknown records; never merge only by name/DOB','restore_deletion_barrier':'Apply deletion/revocation tombstones before restored private data can be accessed','verification':'Independent reviewer checks rollback on the same scoped candidate or synthetic fixture'},
   'estimate':{'low_person_days':w.get('effort_low_person_days'),'high_person_days':w.get('effort_high_person_days'),'status':'PROPOSAL_NOT_APPROVED' if w.get('effort_low_person_days') is not None else 'UNKNOWN','rollup_policy':w['estimate_rollup'],'overlaps_source_task_ids':w['source_task_ids'],'currency':None,'monetary_value':None},
   'release':{'production_permission':False,'approver_names':None,'gate_receipts':[],'expires_or_revisit':'Before any change from documentation preparation to scoped DEV/staging'}}
  validator.validate(p);packets.append(p)
  admission.append({'work_order_id':k,'schema_valid':True,'ready_for_scoped_dev':False,'reasons':['named owner/reviewer not assigned','exact clean candidate/artifact and file allowlist not accepted','required scoped decisions/rights/schema/cohort receipts pending','version bundle and fixture/test commands need final scope binding'],'preparation_authority':'Current user request for local planning preparation only; no application or provider action authorized'})
 dump(E/'WORK_ORDER_DRAFT_PACKETS.json',packets)
 dump(P/'evidence/WORK_ORDER_ADMISSION_REVIEW.json',{'schema_valid_packets':len(packets),'ready_for_scoped_dev':0,'approval_fabricated':False,'records':admission})
 print(json.dumps({'schema_valid_drafts':len(packets),'ready_for_scoped_dev':0}))
if __name__=='__main__':main()
