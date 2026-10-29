#!/usr/bin/env python3
"""Verify delivery integrity and internal contracts. Does not deploy or call live APIs."""
from pathlib import Path
import argparse, hashlib, json, re, sys
ROOT=Path(__file__).resolve().parent
checks=[]
def check(label,condition,details=''):
    checks.append({'check':label,'passed':bool(condition),'details':details})
def load(path): return json.loads((ROOT/path).read_text(encoding='utf-8'))
def h(path):
    dig=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):dig.update(b)
    return dig.hexdigest()
def subset(actual,expected):
    if isinstance(expected,dict):return isinstance(actual,dict) and all(k in actual and subset(actual[k],v) for k,v in expected.items())
    if isinstance(expected,list):return actual==expected
    return actual==expected

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--report',type=Path);ap.add_argument('--strict-schema',action='store_true');ap.add_argument('--preflight-no-manifest',action='store_true',help='For assembly only; not a final integrity verification.')
    args=ap.parse_args()
    pres=load('01_BASELINE/PRESERVATION.json')
    check('149 baseline records',len(pres['files'])==149)
    for x in pres['files']:
        p=ROOT/x['preserved_path'];check('baseline '+x['path'],p.is_file() and h(p)==x['sha256'])
    oldzip=ROOT/'01_BASELINE'/pres['source_archive'];check('original ZIP',h(oldzip)==pres['source_sha256'])
    for p in ROOT.rglob('*.json'):
        try:json.loads(p.read_text(encoding='utf-8'));check('JSON '+str(p.relative_to(ROOT)),True)
        except Exception as e:check('JSON '+str(p.relative_to(ROOT)),False,str(e))
    base_products=load('03_PRODUCT/PRODUCT_CATALOG_BASELINE.json');products=load('03_PRODUCT/PRODUCT_CATALOG_V2.json')
    check('all 23 original products',len(products)==23 and {x['product_id']for x in products}=={x['product_id']for x in base_products})
    base_tasks=load('08_EXECUTION/BACKLOG_BASELINE_140.json');new_tasks=load('08_EXECUTION/BACKLOG_V2_ADDITIONS.json')
    ids={t['task_id']for t in base_tasks}|{t['task_id']for t in new_tasks}
    check('140 baseline + 68 refinements',len(base_tasks)==140 and len(new_tasks)==68 and len(ids)==208)
    for t in new_tasks:
        check('task parent '+t['task_id'],t['parent_task_id']in ids)
        deps=[d.strip()for d in t['dependencies'].split(',')if d.strip()]
        check('dependencies '+t['task_id'],all(d in ids and d!=t['task_id']for d in deps))
        check('no false production completion '+t['task_id'],t['production_status']=='NOT_STARTED')
    cases=load('06_DEMO_LAB/data/demo-cases.json');receipts=load('06_DEMO_LAB/receipts/demo-results.json');index={e['id']:e for e in receipts['receipts']}
    check('90 unique fixtures',len(cases)==90 and len({x['id']for x in cases})==90)
    for c in cases:
        e=index.get(c['id'],{});error=e.get('error')
        if c.get('expected_error'):
            code=error.get('code')if isinstance(error,dict)else error
            check('fixture '+c['id'],code==c['expected_error'],str(code))
        else:check('fixture '+c['id'],error is None and subset(e.get('result'),c.get('expected_subset',{})))
    formulas=load('05_BACKEND/FORMULA_CATALOG.json');check('32 catalog entries',len(formulas)==32)
    for f in formulas:
        if f.get('implementation_path'):check('implementation '+f['formula_id'],(ROOT/f['implementation_path']).is_file())
        check('formula fixture links '+f['formula_id'],all(x in index for x in f.get('demo_ids',[])))
    api=load('05_BACKEND/openapi.target.v2.json');baseapi=load('05_BACKEND/openapi.baseline.json');verbs={'get','post','patch','put','delete','head','options'}
    ops=[(path,m,o.get('operationId')) for path,item in api['paths'].items()for m,o in item.items()if m in verbs]
    oldops={(path,m,o.get('operationId')) for path,item in baseapi['paths'].items()for m,o in item.items()if m in verbs}
    check('83 target operations',len(ops)==83)
    check('64 original operations retained',len(oldops)==64 and oldops.issubset(set(ops)))
    check('operation IDs unique',len({x[2]for x in ops})==len(ops))
    def refs(v):
        if isinstance(v,dict):
            for k,a in v.items():
                if k=='$ref' and isinstance(a,str) and a.startswith('#/'):
                    cur=api
                    try:
                        for part in a[2:].split('/'):cur=cur[part.replace('~1','/').replace('~0','~')]
                        check('OpenAPI ref '+a,True)
                    except:check('OpenAPI ref '+a,False)
                else:refs(a)
        elif isinstance(v,list):
            for a in v:refs(a)
    refs(api)
    schema_state='NOT_RUN'
    try:
        import jsonschema
        from jsonschema import Draft202012Validator, FormatChecker
        for p in sorted((ROOT/'05_BACKEND/schemas').glob('*.schema.json')):
            s=json.loads(p.read_text());Draft202012Validator.check_schema(s);sample=ROOT/'05_BACKEND/examples'/p.name.replace('.schema.json','.json')
            errors=list(Draft202012Validator(s,format_checker=FormatChecker()).iter_errors(json.loads(sample.read_text())))
            check('schema example '+p.name,not errors,'; '.join(e.message for e in errors)[:600])
        schema_state='EXECUTED_JSONSCHEMA_2020_12'
    except ImportError:
        schema_state='SKIPPED_JSONSCHEMA_NOT_INSTALLED'
        if args.strict_schema:check('schema validator installed',False,'Install jsonschema to run strict schema checks.')
    ui=load('06_DEMO_LAB/receipts/browser-ui.json')
    check('90 browser cases',len(ui['cases'])==90 and all(c['rendered']for c in ui['cases']))
    check('browser errors empty',not ui['errors'])
    check('four widths no horizontal overflow',len(ui['viewports'])==4 and all(not v['horizontal_overflow']for v in ui['viewports']))
    check('zero policy UI',ui['custom_zero_unmapped'])
    tap=(ROOT/'06_DEMO_LAB/receipts/tests.tap').read_text();check('Node TAP 125 pass',bool(re.search(r'^# pass 125$',tap,re.M)) and bool(re.search(r'^# fail 0$',tap,re.M)))
    oldtap=(ROOT/'10_QA/BASELINE_TEST_RERUN.tap').read_text();check('Baseline TAP 83 pass',bool(re.search(r'^# pass 83$',oldtap,re.M)) and bool(re.search(r'^# fail 0$',oldtap,re.M)))
    source_map=load('02_REVIEW/NO_LOSS_UPGRADE_MATRIX.json');check('149 no-loss mappings',len(source_map)==149)
    mpath=ROOT/'MANIFEST.json';manifest_state='NOT_PRESENT_ASSEMBLY'
    if mpath.exists()and not args.preflight_no_manifest:
        manifest=load('MANIFEST.json');expected={x['path']:x for x in manifest['files']};actual={str(p.relative_to(ROOT))for p in ROOT.rglob('*')if p.is_file()and p!=mpath}
        check('manifest exact file set',set(expected)==actual)
        for rel,row in expected.items():
            p=ROOT/rel;check('manifest '+rel,p.is_file()and not p.is_symlink()and h(p)==row['sha256'])
        manifest_state='VERIFIED'
    elif not args.preflight_no_manifest:check('manifest present',False)
    forbidden=[str(p.relative_to(ROOT))for p in ROOT.rglob('*')if p.is_file()and (p.suffix.lower()in{'.ttf','.otf','.woff','.woff2'} or p.name in{'.env','id_rsa','id_ed25519'})]
    check('no font or secret files bundled',not forbidden,str(forbidden))
    summary={'as_of':'2026-10-20','scope':'package integrity, local reference receipts and structural checks; not production or scientific validation','passed':sum(c['passed']for c in checks),'failed':sum(not c['passed']for c in checks),'schema_checks':schema_state,'manifest':manifest_state,'checks':checks}
    if args.report:
        # Reports inside an already sealed package would change its manifest; caller should use /tmp.
        args.report.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in summary.items()if k!='checks'},ensure_ascii=False,indent=2))
    for c in checks:
        if not c['passed']:print('FAILED',c['check'],c['details'])
    return int(summary['failed']>0)
if __name__=='__main__':
    raise SystemExit(main())
