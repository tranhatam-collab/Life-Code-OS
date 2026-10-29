#!/usr/bin/env python3
"""Read-only validation of planning contracts; writes only its own new receipt."""
import hashlib
import json
import argparse
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker
import yaml

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "docs/upgrade/2026-10-29/backend"
S = ROOT / "docs/upgrade/sources/2026-10-29"
V2 = S / "v2/package/LIFE_CODE_OS_V2_2026-10-20"
V3 = S / "v3/package/LIFE_CODE_OS_ALL_IN_ONE_V3_2026-10-29"

def read(path): return json.loads(path.read_text())
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def rel(path): return str(path.relative_to(ROOT))

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--replay-receipt',type=Path,default=ROOT/'docs/upgrade/2026-10-29/evidence/backend-tests/v3_demo_results_current.json')
    args=parser.parse_args()
    doc = read(OUT / 'OPENAPI_UNIFIED_TARGET.json')
    components=[]
    for name,schema in doc['components']['schemas'].items():
        Draft202012Validator.check_schema(schema)
        components.append({'name':name,'schema_syntax':'PASS'})
    standalone=[]
    for label,base in [('V2',V2/'05_BACKEND'),('V3',V3/'07_BACKEND')]:
        for schema_path in sorted((base/'schemas').glob('*.schema.json')):
            schema=read(schema_path)
            assert doc['components']['schemas'][schema_path.stem.replace('.schema','')] == schema
            example_path=base/'examples'/schema_path.name.replace('.schema','')
            errors=[]
            if example_path.exists():
                errors=[{'path':list(e.path),'message':e.message} for e in Draft202012Validator(schema,format_checker=FormatChecker()).iter_errors(read(example_path))]
            standalone.append({'source':label,'schema':rel(schema_path),'preserved_exact_object':True,
                'example_status':'FAIL' if errors else 'PASS' if example_path.exists() else 'NO_SUPPLIED_EXAMPLE','errors':errors})
    canonical=[]
    for name in ['Claim','ProfileVersion','ReleaseReceipt','Tail80Result','MethodResult','ReportSnapshot','Metric','JobEnvelope','MethodRelease']:
        path=ROOT/f'docs/upgrade/2026-10-20/03_Du_lieu_Phep_tinh/schemas/{name}.schema.json'
        assert doc['components']['schemas'][name] == read(path)
        canonical.append({'name':name,'path':rel(path),'sha256':sha(path),'exact_object_match':True})
    # Explicitly read the current, temp-executed replay supplied by the verifier.
    replay_path=args.replay_receipt.resolve()
    replay=read(replay_path)
    result_by_id={r['id']:r for r in replay['receipts']}
    mapping={'bat_cuc':'BatCucInput','number_compare':'NumberCompareInput','name_compare':'NameCompareInput','numerology_full':'NumerologyFullInput','psychomatrix':'PsychomatrixInput','lifetime':'LifetimeInput','all_in_one':'AllInOneInput'}
    reference=Draft202012Validator(read(V3/'07_BACKEND/schemas/ReferenceResult.schema.json'),format_checker=FormatChecker())
    cases=[]
    for case in read(V3/'08_ALL_IN_ONE_LAB/data/demo-cases-all.json'):
        if case['method'] not in mapping: continue
        name=mapping[case['method']]
        validator=Draft202012Validator(read(V3/f'07_BACKEND/schemas/{name}.schema.json'),format_checker=FormatChecker())
        input_errors=[e.message for e in validator.iter_errors(case['input'])]
        result=result_by_id[case['id']]
        output_errors=[e.message for e in reference.iter_errors(result['result'])] if not result['error'] else []
        cases.append({'case_id':case['id'],'dispatcher':case['method'],'input_schema':name,'expected_error':case.get('expected_error'),
            'runtime_error':result['error']['code'] if result['error'] else None,'structural_input_errors':input_errors,
            'reference_output_errors':output_errors,'status':'EXPECTED_DOMAIN_OR_STRUCTURAL_REJECTION' if result['error'] else 'FAIL' if input_errors or output_errors else 'PASS_REFERENCE_CONTRACT'})
    yaml_parity=yaml.safe_load((V2/'05_BACKEND/openapi.target.v2.yaml').read_text())==read(V2/'05_BACKEND/openapi.target.v2.json')
    assert yaml_parity
    assert not any(r['status']=='FAIL' for r in cases)
    assert not any(r['example_status']=='FAIL' for r in standalone)
    receipt={'date':'2026-10-29','scope':'PLANNING_CONTRACT_AND_SYNTHETIC_REFERENCE_ONLY','validator':'jsonschema 4.26.0 Draft202012Validator + FormatChecker; PyYAML 6.0.3 safe_load',
        'unified_component_schemas_checked':len(components),'component_schema_checks':components,'local_canonical_schemas':canonical,
        'standalone_source_schemas_checked':len(standalone),'standalone_preservation_and_examples':standalone,'v2_json_yaml_parity':yaml_parity,
        'v3_dispatcher_cases_crosschecked':len(cases),'positive_reference_contract_pass':sum(r['status']=='PASS_REFERENCE_CONTRACT' for r in cases),
        'expected_rejections':sum(r['status']=='EXPECTED_DOMAIN_OR_STRUCTURAL_REJECTION' for r in cases),'case_rows':cases,
        'replay_source':str(replay_path),'replay_sha256':sha(replay_path),'codegen_ready':False,'production_ready':False,
        'limits':['Syntax and fixture conformance are not a full OpenAPI implementation or authorization proof.','Expected runtime rejection can express domain rules beyond structural JSON Schema.','No hidden test fixtures or independent scientific/source validation is implied.']}
    (OUT/'CONTRACT_VALIDATION_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in receipt.items() if isinstance(v,(int,bool))},ensure_ascii=False))

if __name__=='__main__': main()
