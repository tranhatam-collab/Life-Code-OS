/** Pure domain examples only. Must be backed by verified identity, DB isolation and transactions. */
export function coverage(requirements, values) {
 if (!Array.isArray(requirements) || !values || typeof values!=='object' || Array.isArray(values) || new Set(requirements.map(r=>r.id)).size!==requirements.length) throw new TypeError('Yêu cầu server phải duy nhất và values phải là object.');
 let total=0, valid=0;
 for (const r of requirements) {
   if (typeof r.id!=='string' || !Number.isFinite(r.weight) || r.weight<=0) throw new TypeError('Weight không hợp lệ.');
   total+=r.weight;
   if (Object.hasOwn(values,r.id) && values[r.id]===true) valid+=r.weight;
 }
 return {ratio:total===0?null:valid/total,completed_weight:valid,total_weight:total,meaning:'input_coverage_not_accuracy'};
}
const RFC3339=/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?(?:Z|[+-]\d{2}:\d{2})$/;
export function allowed({authenticated,principal,tenant,subject,grant,purpose,now,action='read',resourceState='active',accountState='active',permissionRevision=null}) {
 if (!authenticated || !principal || !grant || typeof grant!=='object' || !Number.isFinite(now) || resourceState!=='active' || accountState!=='active') return false;
 if (typeof grant.expires_at!=='string' || !RFC3339.test(grant.expires_at)) return false;
 const expiry=Date.parse(grant.expires_at);
 if (!Number.isFinite(expiry) || expiry<=now) return false;
 if (grant.not_before!==undefined) {
   if (typeof grant.not_before!=='string' || !RFC3339.test(grant.not_before)) return false;
   const notBefore=Date.parse(grant.not_before);
   if (!Number.isFinite(notBefore) || notBefore>now) return false;
 }
 if (!Array.isArray(grant.permissions) || !grant.permissions.every(x=>typeof x==='string')) return false;
 if (permissionRevision!==null && (!Number.isSafeInteger(permissionRevision) || grant.permission_revision!==permissionRevision)) return false;
 return grant.state==='active' && grant.grantee===principal && grant.tenant===tenant && grant.subject===subject && grant.purpose===purpose && grant.permissions.includes(action);
}
export function eligible({authorized,purposeAllowed,entitlementValid,methodReleased,inputsValid,countryAllowed}) {
 return [authorized,purposeAllowed,entitlementValid,methodReleased,inputsValid,countryAllowed].every(x=>x===true);
}
export function assertClaim(c) {
 const kinds=['fact','self_report','observation','symbolic_interpretation','derived_metric','model_probability'];
 if (!kinds.includes(c.type)) throw new TypeError('Loại nhận định chưa hỗ trợ.');
 if (c.type==='model_probability') {
   const required=['model_release_id','target_event','horizon','population','evaluation_receipt_id'];
   if (!Number.isFinite(c.probability)||c.probability<0||c.probability>1||required.some(k=>typeof c[k]!=='string'||!c[k])||c.applicability_check!=='passed') throw new TypeError('Thiếu model release, phạm vi đánh giá hoặc xác suất hợp lệ.');
 } else if (c.probability!==null && c.probability!==undefined) throw new TypeError('Không tạo xác suất cho nhận định không phải model.');
 return true;
}
export function goalProgress(actions) {
 if (!Array.isArray(actions)) throw new TypeError('Danh sách nhiệm vụ không hợp lệ.');
 if (!actions.every(a=>a&&['open','done','cancelled'].includes(a.state))) throw new TypeError('Trạng thái nhiệm vụ không hợp lệ.');
 const required=actions.filter(a=>a.state!=='cancelled');
 if (!required.length) return {value:null,reason:'no_scheduled_actions'};
 return {value:required.filter(a=>a.state==='done').length/required.length,reason:null};
}

export function methodReleaseGate(release) {
 const reasons=[];
 if (!release || typeof release!=='object') return {allowed:false,reasons:['invalid_release']};
 const nonEmpty=(key)=>Array.isArray(release[key])&&release[key].length>0;
 const digest=(key)=>typeof release[key]==='string'&&/^[a-f0-9]{64}$/.test(release[key]);
 if (release.release_state!=='permitted_for_product') reasons.push('release_state_not_permitted');
 if (!['deterministic','symbolic','observational','validated_model'].includes(release.computation_kind)) reasons.push('invalid_computation_kind');
 if (release.rights_status!=='permitted') reasons.push('rights_not_permitted');
 for (const key of ['source_links','allowed_product_ids','allowed_country_packs','golden_cases']) if (!nonEmpty(key)) reasons.push('missing_'+key);
 for (const key of ['rule_spec_digest','configuration_digest','input_schema_digest','output_schema_digest']) if (!digest(key)) reasons.push('invalid_'+key);
 for (const key of ['test_receipt_id','independent_review_receipt_id','approval_receipt_id']) if (typeof release[key]!=='string'||!release[key]) reasons.push('missing_'+key);
 if (!Array.isArray(release.allowed_claim_types)||release.allowed_claim_types.length===0) reasons.push('missing_allowed_claim_types');
 if (release.computation_kind!=='validated_model' && release.allowed_claim_types?.includes('model_probability')) reasons.push('probability_for_non_model');
 if (release.computation_kind==='validated_model' && (typeof release.evaluation_receipt_id!=='string'||!release.evaluation_receipt_id)) reasons.push('missing_evaluation_receipt_id');
 return {allowed:reasons.length===0,reasons};
}
export class ReceiptLedger {
 constructor(){this.items=new Map();}
 apply(namespace,key,digest,fn){
   const k=namespace+'\u0000'+key;
   if(this.items.has(k)){const prior=this.items.get(k);if(prior.digest!==digest)throw new Error('IDEMPOTENCY_CONFLICT');return prior.result;}
   const result=fn();this.items.set(k,{digest,result});return result;
 }
}
