/** Pure domain examples only. Must be backed by verified identity, DB isolation and transactions. */
export function coverage(requirements, values) {
 if (!Array.isArray(requirements) || new Set(requirements.map(r=>r.id)).size!==requirements.length) throw new TypeError('Yêu cầu server phải duy nhất.');
 let total=0, valid=0;
 for (const r of requirements) {
   if (typeof r.id!=='string' || !Number.isFinite(r.weight) || r.weight<=0) throw new TypeError('Weight không hợp lệ.');
   total+=r.weight;
   if (Object.hasOwn(values,r.id) && values[r.id]===true) valid+=r.weight;
 }
 return {ratio:total===0?null:valid/total,completed_weight:valid,total_weight:total,meaning:'input_coverage_not_accuracy'};
}
export function allowed({authenticated,principal,tenant,subject,grant,purpose,now,resourceState='active'}) {
 if (!authenticated || !principal || !grant || !Number.isFinite(now) || resourceState!=='active') return false;
 const expiry=Date.parse(grant.expires_at);
 return Number.isFinite(expiry) && expiry>now && grant.state==='active' && grant.grantee===principal && grant.tenant===tenant && grant.subject===subject && grant.purpose===purpose && grant.permissions.includes('read');
}
export function eligible({authorized,purposeAllowed,entitlementValid,methodReleased,inputsValid,countryAllowed}) {
 return [authorized,purposeAllowed,entitlementValid,methodReleased,inputsValid,countryAllowed].every(x=>x===true);
}
export function assertClaim(c) {
 const kinds=['fact','self_report','observation','symbolic_interpretation','derived_metric','model_probability'];
 if (!kinds.includes(c.type)) throw new TypeError('Loại nhận định chưa hỗ trợ.');
 if (c.type==='model_probability') {
   if (!Number.isFinite(c.probability)||c.probability<0||c.probability>1||!c.model_release_id) throw new TypeError('Thiếu model release hoặc xác suất hợp lệ.');
 } else if (c.probability!==null && c.probability!==undefined) throw new TypeError('Không tạo xác suất cho nhận định không phải model.');
 return true;
}
export function goalProgress(actions) {
 if (!Array.isArray(actions)) throw new TypeError('Danh sách nhiệm vụ không hợp lệ.');
 const required=actions.filter(a=>a.state!=='cancelled');
 if (!required.length) return {value:null,reason:'no_scheduled_actions'};
 return {value:required.filter(a=>a.state==='done').length/required.length,reason:null};
}
export class ReceiptLedger {
 constructor(){this.items=new Map();}
 apply(namespace,key,digest,fn){
   const k=namespace+'\u0000'+key;
   if(this.items.has(k)){const prior=this.items.get(k);if(prior.digest!==digest)throw new Error('IDEMPOTENCY_CONFLICT');return prior.result;}
   const result=fn();this.items.set(k,{digest,result});return result;
 }
}
