import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const here=path.dirname(fileURLToPath(import.meta.url));
const root=path.resolve(here,'..');
const backend=path.resolve(root,'../04_Backend_API');
const data=path.resolve(root,'../03_Du_lieu_Phep_tinh');
const knowledge=path.resolve(root,'../02_Tri_thuc_HNH');
const readJson=file=>JSON.parse(fs.readFileSync(file,'utf8').replace(/^\uFEFF/,''));

function operationsFromOpenApi(openapi){
  const verbs=new Set(['get','post','put','patch','delete','options','head','trace']);
  return Object.entries(openapi.paths).flatMap(([route,item])=>Object.entries(item).filter(([verb])=>verbs.has(verb)).map(([verb,operation])=>({route,verb:verb.toUpperCase(),operation_id:operation.operationId})));
}

function refsFrom(value,out=[]){
  if(Array.isArray(value)) for(const item of value) refsFrom(item,out);
  else if(value&&typeof value==='object') for(const [key,item] of Object.entries(value)){
    if(key==='$ref'&&typeof item==='string') out.push(item);
    refsFrom(item,out);
  }
  return out;
}

function resolvePointer(document,pointer){
  assert.match(pointer,/^#\//);
  return pointer.slice(2).split('/').reduce((value,raw)=>value[raw.replaceAll('~1','/').replaceAll('~0','~')],document);
}

test('OpenAPI and operation registry preserve exactly 64 unique operations',()=>{
  const openapi=readJson(path.join(backend,'openapi.json'));
  const registry=readJson(path.join(backend,'API_OPERATIONS.json'));
  const actual=operationsFromOpenApi(openapi);
  assert.equal(actual.length,64);
  assert.equal(registry.length,64);
  assert.equal(new Set(actual.map(x=>x.operation_id)).size,64);
  assert.equal(new Set(registry.map(x=>x.operation_id)).size,64);
  assert.deepEqual(actual.map(x=>[x.verb,x.route,x.operation_id]),registry.map(x=>[x.method,x.path,x.operation_id]));
  for(const row of registry){
    const operation=openapi.paths[row.path][row.method.toLowerCase()];
    assert.equal(operation['x-required-permission'],row.permission,`${row.operation_id}: permission`);
    const requestContent=operation.requestBody?.content??{};
    const requestType=requestContent['application/json']?'application/json':Object.keys(requestContent).sort()[0];
    const requestRef=requestType?(requestContent[requestType].schema?.$ref??null):null;
    assert.equal(requestRef,row.request_schema,`${row.operation_id}: request_schema`);
    const response=operation.responses[String(row.success)];
    assert.ok(response,`${row.operation_id}: success ${row.success}`);
    const responseContent=response.content??{};
    const responseType=responseContent['application/json']?'application/json':Object.keys(responseContent).sort()[0];
    const responseRef=responseType?(responseContent[responseType].schema?.$ref??null):null;
    assert.equal(responseRef,row.response_schema,`${row.operation_id}: response_schema`);
  }
});

test('all 64 operations resolve to one declared permission policy',()=>{
  const registry=readJson(path.join(backend,'API_OPERATIONS.json'));
  const matrix=readJson(path.join(backend,'AUTHORIZATION_POLICY_MATRIX.json'));
  assert.equal(matrix.expected_operation_count,64);
  assert.equal(Object.keys(matrix.policies).length,34);
  for(const op of registry){
    assert.ok(matrix.policies[op.permission],`${op.operation_id}: missing ${op.permission}`);
    assert.ok(matrix.templates[matrix.policies[op.permission].template],`${op.operation_id}: missing template`);
  }
  assert.deepEqual([...new Set(registry.map(x=>x.permission))].sort(),Object.keys(matrix.policies).sort());
});

test('OpenAPI local component refs resolve',()=>{
  const openapi=readJson(path.join(backend,'openapi.json'));
  const refs=[];
  const walk=value=>{if(Array.isArray(value))for(const item of value)walk(item);else if(value&&typeof value==='object')for(const [key,item] of Object.entries(value)){if(key==='$ref'&&typeof item==='string')refs.push(item);walk(item);}};
  walk(openapi);
  const schemas=openapi.components.schemas;
  for(const ref of refs.filter(x=>x.startsWith('#/components/schemas/'))) assert.ok(schemas[ref.split('/').at(-1)],ref);
});

test('overlay delegates all nine duplicated schemas and does not add paths',()=>{
  const overlay=fs.readFileSync(path.join(backend,'openapi.upgrade.overlay.yaml'),'utf8');
  const names=['Claim','JobEnvelope','MethodRelease','MethodResult','Metric','ProfileVersion','ReleaseReceipt','ReportSnapshot','Tail80Result'];
  assert.match(overlay,/^overlay: 1\.2\.0/m);
  assert.match(overlay,/x-lc-required-operation-count: 64/);
  assert.doesNotMatch(overlay,/^\s+paths:/m);
  for(const name of names){
    assert.match(overlay,new RegExp(`schemas\\.${name}`));
    assert.match(overlay,new RegExp(`schemas/${name}\\.schema\\.json`));
    assert.ok(fs.existsSync(path.join(data,'schemas',name+'.schema.json')));
  }
});

test('resolved OpenAPI materializes overlay and bundles all canonical schemas',()=>{
  const base=readJson(path.join(backend,'openapi.json'));
  const resolved=readJson(path.join(backend,'openapi.resolved.json'));
  const registry=readJson(path.join(backend,'API_OPERATIONS.json'));
  const names=['Claim','JobEnvelope','MethodRelease','MethodResult','Metric','ProfileVersion','ReleaseReceipt','ReportSnapshot','Tail80Result'];
  assert.equal(resolved.info['x-lc-canonical-current-contract'],'./openapi.resolved.yaml');
  assert.equal(resolved.info['x-lc-resolution-mode'],'LOCAL_DETERMINISTIC_OVERLAY_AND_CANONICAL_SCHEMA_BUNDLE');
  assert.equal(resolved.info['x-lc-applied-overlay-action-count'],17);
  assert.equal(operationsFromOpenApi(resolved).length,64);
  assert.deepEqual(operationsFromOpenApi(resolved),operationsFromOpenApi(base));
  assert.equal(Object.keys(resolved['x-lc-operation-response-contracts']).length,64);
  assert.deepEqual(Object.keys(resolved['x-lc-operation-response-contracts']).sort(),registry.map(x=>x.operation_id).sort());
  for(const name of names){
    const canonical=readJson(path.join(data,'schemas',name+'.schema.json'));
    assert.deepEqual(resolved.components.schemas[name],canonical,name);
  }
  const refs=refsFrom(resolved);
  assert.equal(refs.length,resolved.info['x-lc-local-ref-count']);
  assert.ok(refs.every(ref=>ref.startsWith('#/')));
  for(const ref of refs) assert.doesNotThrow(()=>resolvePointer(resolved,ref),ref);
});

test('resolved OpenAPI exposes every generic response as a non-codegen blocker',()=>{
  const resolved=readJson(path.join(backend,'openapi.resolved.json'));
  const blockers=resolved['x-lc-generic-response-blockers'];
  assert.equal(blockers.count,46);
  assert.equal(blockers.codegen_ready,false);
  assert.equal(blockers.operations.length,46);
  assert.equal(new Set(blockers.operations.map(x=>x.operation_id)).size,46);
  for(const row of blockers.operations){
    const operation=resolved.paths[row.path][row.method.toLowerCase()];
    assert.equal(operation['x-lc-response-contract-status'],'TRANSITIONAL_GENERIC_BLOCKER');
    assert.equal(operation['x-lc-codegen-ready'],false);
    assert.equal(operation['x-lc-route-namespace'],row.route_namespace);
  }
  for(const name of ['Resource','ResourcePage']){
    assert.equal(resolved.components.schemas[name]['x-lc-contract-status'],'TRANSITIONAL_GENERIC_BLOCKER');
    assert.equal(resolved.components.schemas[name]['x-lc-codegen-ready'],false);
  }
  assert.equal(resolved.components.schemas.Resource.properties.attributes.additionalProperties,true);
});

test('all 46 generic responses have fail-closed design packets',()=>{
  const resolved=readJson(path.join(backend,'openapi.resolved.json'));
  const design=readJson(path.join(backend,'API_RESPONSE_DESIGN_PACKETS.json'));
  const markdown=fs.readFileSync(path.join(backend,'API_RESPONSE_DESIGN_PACKETS.md'),'utf8');
  const registry=readJson(path.join(backend,'API_OPERATIONS.json'));
  const registryById=new Map(registry.map(x=>[x.operation_id,x]));
  const blockers=resolved['x-lc-generic-response-blockers'].operations;
  const blockerIds=blockers.map(x=>x.operation_id).sort();
  const blockerById=new Map(blockers.map(x=>[x.operation_id,x]));
  assert.equal(design.operation_count,46);
  assert.equal(design.proposal_count,46);
  assert.equal(design.codegen_ready_count,0);
  assert.equal(design.source_model_gap_count,9);
  assert.equal(design.overlay_inclusion,'NONE_BY_DESIGN_UNTIL_PER_PACKET_APPROVAL');
  assert.equal(design.packets.length,46);
  assert.deepEqual(design.packets.map(x=>x.operation_id).sort(),blockerIds);
  assert.equal(new Set(design.packets.map(x=>x.packet_id)).size,46);
  for(const packet of design.packets){
    const blocker=blockerById.get(packet.operation_id);
    const operation=resolved.paths[packet.path][packet.method.toLowerCase()];
    const registryRow=registryById.get(packet.operation_id);
    assert.equal(packet.method,blocker.method,packet.operation_id);
    assert.equal(packet.path,blocker.path,packet.operation_id);
    assert.equal(packet.success_status,blocker.success_status,packet.operation_id);
    assert.equal(packet.current_generic_response_schema,blocker.generic_schema_ref,packet.operation_id);
    assert.equal(packet.read_scoping.permission,registryRow.permission,packet.operation_id);
    assert.deepEqual(packet.failure_cases.openapi_declared_non_success.map(x=>String(x.status)).sort(),Object.keys(operation.responses).filter(x=>x!==String(packet.success_status)).sort(),packet.operation_id);
    assert.equal(packet.packet_status,'PROPOSED_FIELD_REVIEW_REQUIRED_NOT_CODEGEN_READY',packet.operation_id);
    assert.equal(packet.named_response_proposal.proposed_only,true,packet.operation_id);
    assert.equal(packet.named_response_proposal.included_in_resolved_openapi,false,packet.operation_id);
    assert.equal(packet.named_response_proposal.codegen_ready,false,packet.operation_id);
    assert.ok(packet.named_response_proposal.schema_name,packet.operation_id);
    for(const key of ['required','public_projection','authorized_private_projection','server_only_never_return']) assert.ok(Array.isArray(packet.field_whitelist[key]),`${packet.operation_id}: ${key}`);
    const allowed=new Set([...packet.field_whitelist.public_projection,...packet.field_whitelist.authorized_private_projection]);
    for(const field of packet.field_whitelist.required) assert.ok(allowed.has(field),`${packet.operation_id}: required field not allowed: ${field}`);
    for(const field of packet.field_whitelist.server_only_never_return) assert.ok(!allowed.has(field),`${packet.operation_id}: server-only field allowed: ${field}`);
    assert.equal(packet.read_scoping.client_identity_fields_authoritative,false,packet.operation_id);
    assert.ok(packet.dependencies.task_ids.includes('UPG-BE-006'),packet.operation_id);
    assert.ok(packet.dependencies.approval_receipts.length>=2,packet.operation_id);
    assert.ok(packet.dependencies.approval_receipts.every(x=>x.status==='MISSING'),packet.operation_id);
    assert.match(markdown,new RegExp(`^### ${packet.packet_id} ${packet.operation_id}$`,'m'));
    if(packet.source_model_status==='BLOCKED_SOURCE_MODEL_GAP') assert.ok(packet.open_questions.length>0,packet.operation_id);
  }
  const methodPacket=design.packets.find(x=>x.operation_id==='methodReleaseDraft');
  const canonicalMethod=readJson(path.join(data,'schemas','MethodRelease.schema.json'));
  assert.deepEqual(methodPacket.field_whitelist.required,canonicalMethod.required);
  assert.deepEqual(methodPacket.field_whitelist.authorized_private_projection,canonicalMethod.required);
});

test('resolved overlay binds authorization and preserves the signed-webhook CSRF exception',()=>{
  const resolved=readJson(path.join(backend,'openapi.resolved.json'));
  const operationRows=[];
  for(const [route,item] of Object.entries(resolved.paths)) for(const [verb,operation] of Object.entries(item)){
    if(!['get','post','put','patch','delete','options','head','trace'].includes(verb)) continue;
    operationRows.push({route,verb,operation});
    assert.equal(operation['x-lc-authorization-source'],'./AUTHORIZATION_POLICY_MATRIX.json',operation.operationId);
    assert.equal(operation['x-lc-object-authorization'],'server_resolved',operation.operationId);
  }
  assert.equal(operationRows.length,64);
  const webhook=resolved.paths['/webhooks/payments/{providerId}'].post;
  assert.equal(webhook['x-lc-csrf-default'],'not_applicable');
  assert.equal(webhook['x-lc-authenticator'],'provider_signature_over_raw_body');
  assert.equal(webhook['x-lc-idempotent-effect'],true);
  for(const {route,verb,operation} of operationRows){
    if((verb==='post'||verb==='delete')&&route!=='/webhooks/payments/{providerId}'){
      assert.equal(operation['x-lc-csrf-default'],'required_for_cookie_session',operation.operationId);
    }
  }
});

test('20 family readiness records are complete and do not imply release',()=>{
  const file=path.join(knowledge,'METHOD_FAMILY_READINESS.json');
  assert.ok(fs.existsSync(file),'METHOD_FAMILY_READINESS.json not created');
  const doc=readJson(file);
  const rows=Array.isArray(doc)?doc:doc.families;
  assert.equal(rows.length,20);
  assert.deepEqual(rows.map(x=>x.family_id),Array.from({length:20},(_,i)=>'K'+String(i+1).padStart(2,'0')));
  for(const row of rows) assert.ok(['taxonomy_only','research_only','method_drafts_only','mixed_drafts_only','normalization_reference_only','calculation_reference_only','content_review_required','instrument_review_required'].includes(row.readiness_state),row.family_id);
  const releases=readJson(path.join(knowledge,'METHOD_RELEASE_REGISTRY_V2.json')).releases;
  const rights=readJson(path.join(knowledge,'SOURCE_RIGHTS_REGISTER.json')).sources;
  const formulas=readJson(path.join(data,'FORMULA_CATALOG.json')).formulas;
  assert.equal(releases.length,15);
  assert.ok(releases.every(x=>x.release_state==='blocked'));
  assert.ok(rights.every(x=>x.rights_state!=='permitted'));
  assert.ok(formulas.every(x=>x.release_state==='blocked'));
});

test('demo manifest and offline explorer are side-effect free',()=>{
  const suite=readJson(path.join(root,'data/demo_cases.json'));
  assert.equal(suite.case_count,64);
  assert.equal(suite.cases.length,64);
  const html=fs.readFileSync(path.join(root,'demo.html'),'utf8');
  assert.doesNotMatch(html,/\bfetch\s*\(|XMLHttpRequest|WebSocket|EventSource|localStorage|sessionStorage|document\.cookie/);
  assert.doesNotMatch(html,/https?:\/\//);
  assert.match(html,/aria-live="polite"/);
  assert.match(html,/Ctrl\/⌘\+Enter|Ctrl\/⌘ \+ Enter/);
});

test('migration matrix names only the six baseline D1 tables',()=>{
  const csv=fs.readFileSync(path.join(backend,'MIGRATION_RECONCILIATION_MATRIX.csv'),'utf8');
  const names=['user_profiles','life_code_results','user_sessions','rate_limits','account_audit_logs','alert_dispatch_logs'];
  for(const name of names) assert.equal((csv.match(new RegExp(`,${name},`,'g'))??[]).length,1,name);
  assert.match(csv,/99b402764437f81859fa0cd3a3af860125f7bd52/);
  assert.doesNotMatch(csv,/,READY|,PASS|,DONE/);
});

