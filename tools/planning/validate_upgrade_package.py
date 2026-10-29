"""Offline checks for the development planning package; writes one local QA receipt.

Output is a local artifact receipt, never a production/release verdict.
"""
import csv
import hashlib
import json
import re
import sys
import warnings
from pathlib import Path
from collections import Counter
import yaml
warnings.filterwarnings('ignore', category=DeprecationWarning)
from jsonschema import Draft202012Validator, RefResolver
ROOT = Path(__file__).resolve().parents[2]
P = ROOT / 'docs/upgrade/2026-10-20'
SOURCE = ROOT / 'docs/upgrade/sources/2026-10-11/package'
CHECKS = []

def check(name, condition, detail=''):
    CHECKS.append({'check':name,'passed':bool(condition),'detail':str(detail)})

def load(rel, base=P):
    return json.loads((base / rel).read_text())

def ids(rows, key):
    return [r[key] for r in rows]

def normalize(v):
    if v is None: return ''
    if isinstance(v, bool): return str(v).lower()
    if isinstance(v, (list, dict)): return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':'))
    if isinstance(v, (int,float)): return str(v)
    if v in ['True','False','true','false']: return v.lower()
    try:
        parsed=json.loads(v)
        if isinstance(parsed,(list,dict)): return normalize(parsed)
    except (ValueError, TypeError):
        pass
    return str(v)

def main():
    receipt=load('docs/upgrade/sources/2026-10-11/SOURCE_RECEIPT.json',ROOT)
    for item in receipt['files']:
        path=SOURCE/item['path']
        check('source preserved '+item['path'],path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest()==item['sha256'])
        check('current counterpart '+item['path'],(P/item['path']).is_file())
    for f in sorted(P.rglob('*.json')):
        try: json.loads(f.read_text()); check('JSON '+str(f.relative_to(P)),True)
        except Exception as e: check('JSON '+str(f.relative_to(P)),False,e)
    registries=[
        ('01_Chien_luoc_San_pham/PRODUCT_CATALOG.json','product_id'),
        ('01_Chien_luoc_San_pham/NINE_LEVELS.json','level'),
        ('02_Tri_thuc_HNH/METHOD_FAMILIES.json','family_id'),
        ('03_Du_lieu_Phep_tinh/DATA_FIELD_REGISTRY_120.json','field_id'),
        ('05_Frontend_UI/SCREEN_REGISTRY.json','screen_id'),
        ('08_Thuc_thi_Kinh_doanh/EXECUTION_BACKLOG.json','task_id'),
        ('08_Thuc_thi_Kinh_doanh/DECISION_REGISTER.json','decision_id'),
        ('08_Thuc_thi_Kinh_doanh/RELEASE_GATES.json','gate_id'),
        ('09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.json','id'),
        ('09_Doi_chieu_Bang_chung/SOURCE_TO_TARGET_MATRIX.json','mapping_id'),
    ]
    for rel,key in registries:
        current=load(rel); original=load(rel,SOURCE)
        if key not in current[0] or key not in original[0]:
            candidates=[k for k in original[0] if k in current[0] and ('id' in k or k=='level')]
            key=candidates[0]
        original_ids=set(ids(original,key)); current_ids=ids(current,key)
        check('No lost IDs '+rel,original_ids.issubset(set(current_ids)))
        check('Unique IDs '+rel,len(current_ids)==len(set(current_ids)))
    for csv_path in sorted(P.rglob('*.csv')):
        json_path=csv_path.with_suffix('.json')
        if not json_path.is_file(): continue
        rows=json.loads(json_path.read_text())
        if not isinstance(rows,list) or (rows and not isinstance(rows[0],dict)): continue
        csv_rows=list(csv.DictReader(csv_path.open(encoding='utf-8-sig')))
        check('CSV count '+str(csv_path.relative_to(P)),len(rows)==len(csv_rows))
        if len(rows)==len(csv_rows):
            errors=[]
            for i,(a,b) in enumerate(zip(rows,csv_rows)):
                for k in b:
                    if k in a and normalize(a[k])!=normalize(b[k]):
                        errors.append(f'row{i+1}:{k}')
            check('CSV values '+str(csv_path.relative_to(P)),not errors,','.join(errors[:15]))
    spec=load('04_Backend_API/openapi.json')
    yspec=yaml.safe_load((P/'04_Backend_API/openapi.yaml').read_text())
    check('OpenAPI JSON YAML parity',spec==yspec)
    methods={'get','post','put','patch','delete','options','head','trace'}
    ops=[(path,method,op) for path,definition in spec['paths'].items() for method,op in definition.items() if method in methods]
    opids=[o['operationId'] for _,_,o in ops]
    oldspec=load('04_Backend_API/openapi.json',SOURCE)
    oldids={o['operationId'] for d in oldspec['paths'].values() for m,o in d.items() if m in methods}
    check('All original64 API operations preserved',oldids.issubset(set(opids)),f'{len(oldids)} original; {len(opids)} current')
    check('Unique OpenAPI operationId',len(opids)==len(set(opids)))
    def walk(node):
        if isinstance(node,dict):
            if '$ref' in node and node['$ref'].startswith('#/'):
                at=spec
                try:
                    for part in node['$ref'][2:].split('/'): at=at[part.replace('~1','/').replace('~0','~')]
                except KeyError: check('OpenAPI unresolved reference',False,node['$ref'])
            for v in node.values(): walk(v)
        elif isinstance(node,list):
            for v in node: walk(v)
    walk(spec)
    for path,method,op in ops:
        check(f'API responses {method} {path}',bool(op.get('responses')))
    for schema_path in sorted((P/'03_Du_lieu_Phep_tinh/schemas').glob('*.schema.json')):
        schema=json.loads(schema_path.read_text())
        try:
            Draft202012Validator.check_schema(schema)
            check('Schema meta '+schema_path.name,True)
            sample=P/'03_Du_lieu_Phep_tinh/examples'/schema_path.name.replace('.schema.','.example.')
            if sample.exists():
                resolver=RefResolver(base_uri=schema_path.as_uri(),referrer=schema,
                    handlers={'http':lambda uri: (_ for _ in ()).throw(RuntimeError('Network schema disabled: '+uri)),
                              'https':lambda uri: (_ for _ in ()).throw(RuntimeError('Network schema disabled: '+uri))})
                errors=list(Draft202012Validator(schema,resolver=resolver).iter_errors(json.loads(sample.read_text())))
                check('Schema example '+sample.name,not errors,';'.join(e.message for e in errors[:3]))
        except Exception as e: check('Schema '+schema_path.name,False,e)
    tasks=load('08_Thuc_thi_Kinh_doanh/EXECUTION_BACKLOG.json')
    taskids={r['task_id'] for r in tasks}
    graph={}
    for row in tasks:
        deps=row.get('dependencies',[])
        if isinstance(deps,str): deps=[x.strip() for x in deps.split(';') if x.strip()]
        graph[row['task_id']]=deps
        check('Task dependency exists '+row['task_id'],set(deps).issubset(taskids),deps)
        check('No self dependency '+row['task_id'],row['task_id'] not in deps)
    visited=set(); active=set(); cycle=[]
    def visit(i):
        if i in active: cycle.append(i); return
        if i in visited or i not in graph: return
        active.add(i)
        for d in graph[i]: visit(d)
        active.remove(i); visited.add(i)
    for i in graph: visit(i)
    check('Backlog acyclic',not cycle,cycle)
    contracts=load('08_Thuc_thi_Kinh_doanh/TASK_EXECUTION_CONTRACTS.json')
    check('Exact task contract ID set',len(contracts)==len(tasks) and {r['task_id'] for r in contracts}==taskids)
    for row in contracts:
        check('Task contract dependency parity '+row['task_id'],row['dependencies']==graph[row['task_id']])
        check('Task contract acceptance fields '+row['task_id'],all(row.get(k) for k in ['allowed_paths','required_tests','required_negative_tests','evidence_required','evidence_path','rollback_requirement','claim_status']))
    packets=load('08_Thuc_thi_Kinh_doanh/DECISION_EXECUTION_PACKETS.json')
    decisions=load('08_Thuc_thi_Kinh_doanh/DECISION_REGISTER.json')
    check('Exact20 decision packets',len(packets)==20 and {r['decision_id'] for r in packets}=={r['decision_id'] for r in decisions})
    for row in packets:
        check('Decision options and unapproved state '+row['decision_id'],len(row['options'])>=2 and row['recommended_option_id'] in {o['option_id'] for o in row['options']} and row['approval'] is None and row['status']=='PENDING_FOUNDER' and row['production_permission'] is False)
        expected={c['task_id'] for c in contracts if row['decision_id'] in c['decision_dependencies']}
        check('Decision exact affected task set '+row['decision_id'],set(row['affected_task_ids'])==expected)
    patch=list(csv.DictReader((P/'07_Bao_mat_Van_hanh/P0_PACKET/03_PATCH_PLAN.csv').open(encoding='utf-8-sig')))
    for row in patch:
        check('P0 packet current dependency parity '+row['task_id'],set(filter(None,row['dependencies'].split(';')))==set(graph[row['task_id']]))
    sources={r['id'] for r in load('09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.json')}
    for row in tasks:
        refs=row.get('source_refs',[])
        if isinstance(refs,str):refs=refs.split(';')
        check('Task source refs '+row['task_id'],set(refs).issubset(sources))
    resolved=load('04_Backend_API/openapi.resolved.json')
    check('Resolved OpenAPI YAML JSON parity',resolved==yaml.safe_load((P/'04_Backend_API/openapi.resolved.yaml').read_text()))
    resolved_ops=[op for d in resolved['paths'].values() for m,op in d.items() if m in methods]
    check('Resolved preserves all64 unique operations',len(resolved_ops)==64 and {op['operationId'] for op in resolved_ops}==oldids)
    response_packets=load('04_Backend_API/API_RESPONSE_DESIGN_PACKETS.json')
    check('Exact46 generic response design packets',len(response_packets['packets'])==46 and {r['operation_id'] for r in response_packets['packets']}=={r['operation_id'] for r in resolved['x-lc-generic-response-blockers']['operations']})
    check('Response proposals not falsely codegen approved',response_packets['codegen_ready_count']==0 and all(r['named_response_proposal']['codegen_ready'] is False and r['named_response_proposal']['included_in_resolved_openapi'] is False for r in response_packets['packets']))
    for row in response_packets['packets']:
        check('Response packet task refs '+row['operation_id'],set(row['dependencies']['task_ids']).issubset(taskids))
    coverage=load('00_Doc_truoc/READ_COVERAGE.json')
    check('Read coverage exact149 source paths',coverage['read_file_count']==149 and {r['path'] for r in coverage['files']}=={r['path'] for r in receipt['files']})
    fpos=load('07_Bao_mat_Van_hanh/FPOS_GATE_MAPPING.json')
    check('FPOS RG0-RG13 exact coverage',{r['fpos_gate_id'] for r in fpos}=={f'RG{i}' for i in range(14)})
    evidence=load('09_Doi_chieu_Bang_chung/EVIDENCE_LEDGER.json')
    allowed={'VERIFIED_CURRENT','VERIFIED_HEAD_ONLY','VERIFIED_WORKTREE_ONLY','REPORTED_UNVERIFIED','CONTRADICTED','NOT_CHECKED','BLOCKED','NOT_APPLICABLE'}
    check('FPOS evidence statuses',all(r['status'] in allowed for r in evidence))
    check('No invented production approval',load('09_Doi_chieu_Bang_chung/BASELINE_LOCK.json')['production_deploy_authorized'] is False)
    total=len(CHECKS); failed=[r for r in CHECKS if not r['passed']]
    report={'checked_at':'2026-10-20','scope':'LOCAL_PLANNING_ARTIFACT_ONLY','total':total,'passed':total-len(failed),'failed':len(failed),'checks':CHECKS,'production_release_verdict':'HOLD'}
    (P/'00_Doc_truoc/PACKAGE_QA.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='checks'},ensure_ascii=False))
    for item in failed: print(json.dumps(item,ensure_ascii=False))
    return bool(failed)

if __name__=='__main__':
    sys.exit(main())
