import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {digitalRoot,digitSum,nameCycle,tail80,analyzePairs} from '../src/numbers.mjs';
import {ratioDecimal} from '../src/decimal.mjs';
import {ageInterval} from '../src/timeline.mjs';
import {coverage,allowed,assertClaim,methodReleaseGate} from '../src/policies.mjs';

const suite=JSON.parse(fs.readFileSync(new URL('../data/demo_cases.json',import.meta.url),'utf8'));
const tailTable=JSON.parse(fs.readFileSync(new URL('../data/tail80_table.json',import.meta.url),'utf8'));

function subset(actual,expected){
  for(const [key,value] of Object.entries(expected)) assert.deepEqual(actual[key],value,'field '+key);
}

const authBase={authenticated:true,principal:'account-A',tenant:'tenant-A',subject:'subject-A',purpose:'report',action:'read',permissionRevision:7,now:Date.parse('2026-10-20T00:00:00Z'),grant:{grantee:'account-A',tenant:'tenant-A',subject:'subject-A',purpose:'report',permissions:['read'],permission_revision:7,state:'active',expires_at:'2026-11-01T00:00:00Z'}};
function authVariant(variant){
  if(variant==='allow'||variant==='revision_match') return authBase;
  if(variant==='wrong_subject') return {...authBase,subject:'subject-B'};
  if(variant==='wrong_action') return {...authBase,action:'write'};
  if(variant==='future_grant') return {...authBase,grant:{...authBase.grant,not_before:'2026-10-21T00:00:00Z'}};
  if(variant==='malformed_permissions') return {...authBase,grant:{...authBase.grant,permissions:'read'}};
  if(variant==='revision_mismatch') return {...authBase,permissionRevision:8};
  throw new Error('Unknown auth variant '+variant);
}

const hex='a'.repeat(64);
const releaseBase={release_state:'permitted_for_product',computation_kind:'deterministic',rights_status:'permitted',source_links:['source-edition-locator-rights'],allowed_product_ids:['synthetic-product'],allowed_country_packs:['synthetic-country'],golden_cases:['fixture-D001'],rule_spec_digest:hex,configuration_digest:hex,input_schema_digest:hex,output_schema_digest:hex,test_receipt_id:'test-synthetic',independent_review_receipt_id:'review-synthetic',approval_receipt_id:'approval-synthetic',allowed_claim_types:['derived_metric']};
function releaseVariant(variant){
  if(variant==='all_gates') return releaseBase;
  if(variant==='research_only') return {...releaseBase,release_state:'research_only'};
  if(variant==='rights_pending') return {...releaseBase,rights_status:'pending'};
  if(variant==='missing_source') return {...releaseBase,source_links:[]};
  if(variant==='symbolic_probability') return {...releaseBase,computation_kind:'symbolic',allowed_claim_types:['symbolic_interpretation','model_probability']};
  throw new Error('Unknown release variant '+variant);
}

function execute(c){
  if(c.kind==='digital_root') return digitalRoot(c.input);
  if(c.kind==='digit_sum') return digitSum(c.input);
  if(c.kind==='tail80') return tail80(c.input.suffix,{zeroPolicy:c.input.zeroPolicy,table:tailTable});
  if(c.kind==='name_cycle') return nameCycle(c.input);
  if(c.kind==='pairs') {const result=analyzePairs(c.input);return {...result,groups:result.pairs.map(p=>p.group)};}
  if(c.kind==='ratio_decimal') return ratioDecimal(c.input.numerator,c.input.denominator,{scale:c.input.scale,rounding:c.input.rounding});
  if(c.kind==='age_interval') return ageInterval(c.input.birthDate,c.input.age,{leapDayPolicy:c.input.leapDayPolicy});
  if(c.kind==='coverage') return coverage(c.input.requirements,c.input.values);
  if(c.kind==='authorization') return allowed(authVariant(c.variant));
  if(c.kind==='release_gate') return methodReleaseGate(releaseVariant(c.variant));
  if(c.kind==='claim_model_probability') return assertClaim(c.input);
  if(c.kind==='digital_root_error') return digitalRoot(c.input);
  if(c.kind==='digit_sum_error') return digitSum(c.input);
  if(c.kind==='tail80_error') return tail80(c.input.suffix,{zeroPolicy:c.input.zeroPolicy,table:tailTable});
  if(c.kind==='name_cycle_error') return nameCycle(c.input);
  if(c.kind==='age_interval_error') return ageInterval(c.input.birthDate,c.input.age,{leapDayPolicy:c.input.leapDayPolicy});
  throw new Error('Unknown demo kind '+c.kind);
}

test('demo manifest is exactly 64 unique sequential synthetic cases',()=>{
  assert.equal(suite.synthetic_only,true);
  assert.equal(suite.personal_claims,false);
  assert.equal(suite.case_count,64);
  assert.equal(suite.cases.length,64);
  assert.equal(new Set(suite.cases.map(c=>c.id)).size,64);
  assert.deepEqual(suite.cases.map(c=>c.id),Array.from({length:64},(_,i)=>'D'+String(i+1).padStart(3,'0')));
});

for(const c of suite.cases)test(c.id+' '+c.kind,()=>{
  if(c.expected_error){
    let caught=null;
    try{execute(c);}catch(error){caught=error;}
    assert.ok(caught,'expected an error');
    assert.equal(caught.constructor.name,c.expected_error);
    return;
  }
  const actual=execute(c);
  if(c.expected_reason){assert.equal(actual.allowed,false);assert.ok(actual.reasons.includes(c.expected_reason));return;}
  if(c.expected&&typeof c.expected==='object'&&!Array.isArray(c.expected)){subset(actual,c.expected);return;}
  assert.deepEqual(actual,c.expected);
});

