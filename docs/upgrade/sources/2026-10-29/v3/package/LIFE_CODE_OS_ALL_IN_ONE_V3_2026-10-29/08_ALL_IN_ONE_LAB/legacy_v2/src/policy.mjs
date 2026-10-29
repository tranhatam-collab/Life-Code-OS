import {ensure,enumValue,record,integer} from './errors.mjs';
export function authorize(input){
 const {principal,resource,grant,purpose,action,now,entitled=true,needs_entitlement=false}=input;
 const no=reason=>({allowed:false,reason});
 if(!principal?.authenticated || principal.state!=='active')return no('UNAUTHENTICATED');
 if(typeof principal.id!=='string'||!principal.id.trim())return no('INVALID_PRINCIPAL');
 if(!resource||resource.state!=='active')return no('RESOURCE_UNAVAILABLE');
 if(!grant||grant.state!=='active')return no('GRANT_INACTIVE');
 if(![resource.tenant_id,resource.subject_id,grant.tenant_id,grant.subject_id,grant.grantee_id,purpose,action].every(x=>typeof x==='string'&&x.trim().length>0))return no('INVALID_SCOPE');
 if(!Number.isSafeInteger(resource.permission_revision)||resource.permission_revision<1||!Number.isSafeInteger(grant.permission_revision)||grant.permission_revision<1)return no('INVALID_PERMISSION_REVISION');
 if(!Number.isFinite(Date.parse(now)))return no('INVALID_CLOCK');
 if(!Number.isFinite(Date.parse(grant.expires_at))||Date.parse(grant.expires_at)<=Date.parse(now))return no('GRANT_EXPIRED');
 if(grant.grantee_id!==principal.id||grant.tenant_id!==resource.tenant_id||grant.subject_id!==resource.subject_id)return no('SCOPE_MISMATCH');
 if(grant.purpose!==purpose)return no('PURPOSE_MISMATCH');
 if(!Array.isArray(grant.actions)||!grant.actions.includes(action))return no('ACTION_DENIED');
 if(grant.permission_revision!==resource.permission_revision)return no('STALE_PERMISSION');
 if(input.processing_basis_valid!==true)return no('PROCESSING_BASIS_REQUIRED');
 if(needs_entitlement&&entitled!==true)return no('ENTITLEMENT_REQUIRED');
 return {allowed:true,reason:'AUTHORIZED_FOR_THIS_RESOURCE_AND_PURPOSE'};
}
export function validateClaim(c,registry={}){
 record(c,'claim');const types=['fact','self_report','observation','symbolic_interpretation','derived_metric','model_probability'];enumValue(c.type,types,'claim.type');
 ensure(typeof c.text==='string'&&c.text.length>0&&c.text.length<=4000,'INVALID_CLAIM','Nhận định cần nội dung trong giới hạn.');
 ensure(Array.isArray(c.evidence_ids)&&c.evidence_ids.length>0&&c.evidence_ids.every(x=>typeof x==='string'&&x.trim().length>0),'EVIDENCE_REQUIRED','Mọi nhận định phải có ID căn cứ.');
 if(c.type==='model_probability'){
  ensure(Number.isFinite(c.probability)&&c.probability>=0&&c.probability<=1,'INVALID_PROBABILITY','Xác suất nằm ngoài miền.');
  const m=registry[c.model_release_id];
  ensure(m?.state==='approved'&&m.target===c.target&&m.horizon===c.horizon,'MODEL_NOT_APPROVED','Không chỉ tin model ID do client nhập.');
 } else ensure(c.probability===null||c.probability===undefined,'PROBABILITY_NOT_ALLOWED','Không gán xác suất cho nội dung không phải mô hình xác suất.');
 const prohibited=['health_from_numbers','personality_from_face','death_date','employment_symbolic_ranking','minor_destiny_label'];
 ensure(!prohibited.includes(c.use_case),'PROHIBITED_INFERENCE','Nhận định vượt phạm vi sản phẩm.');
 return {valid:true,type:c.type};
}
// Single-process reference only. A Map is not a substitute for DB constraints/transactions.
export class DemoLedger {
 constructor(){this.records=new Map();}
 async run({tenant,operation,key,digest},fn){
  ensure([tenant,operation,key,digest].every(x=>typeof x==='string'&&x.length>0),'INVALID_IDEMPOTENCY','Khóa thiếu thành phần.');
  const id=JSON.stringify([tenant,operation,key]);const prior=this.records.get(id);
  if(prior){ensure(prior.digest===digest,'IDEMPOTENCY_CONFLICT','Cùng khóa nhưng nội dung khác.');return prior.promise;}
  const rec={digest,promise:null};rec.promise=Promise.resolve().then(fn);this.records.set(id,rec);
  try{return await rec.promise;}catch(e){if(this.records.get(id)===rec)this.records.delete(id);throw e;}
 }
}
export function transition(kind,current,event){
 const tables={order:{draft:{submit:'pending_payment'},pending_payment:{verified_payment:'paid',cancel:'cancelled'},paid:{start_fulfillment:'fulfilling',request_refund:'refund_pending'},fulfilling:{complete:'fulfilled',request_refund:'refund_pending'},fulfilled:{request_refund:'refund_pending'},refund_pending:{verified_refund:'refunded'}},run:{queued:{validate:'validating',cancel:'cancelled'},validating:{calculate:'calculating',fail:'failed'},calculating:{draft:'drafting',fail:'failed',cancel:'cancelled'},drafting:{review:'reviewing',fail:'failed'},reviewing:{approve:'completed',reject:'failed',revoke:'cancelled'}},deletion:{requested:{verify:'verified'},verified:{restrict:'restricted'},restricted:{erase:'erasing',hold:'on_hold'},erasing:{confirm:'completed',retry:'erasing'},on_hold:{release:'restricted'}}};
 const next=tables[kind]?.[current]?.[event];ensure(Boolean(next),'INVALID_STATE_TRANSITION',`Không cho phép ${kind}: ${current} → ${event}.`);return {kind,previous:current,event,next};
}
export function optimisticUpdate(expected,current,patch){integer(expected,1,Number.MAX_SAFE_INTEGER-1,'expected_version');integer(current,1,Number.MAX_SAFE_INTEGER-1,'current_version');record(patch,'patch');ensure(expected===current,'VERSION_CONFLICT','Phiên bản đã thay đổi; cần đọc lại trước khi cập nhật.');return {version:current+1,patch};}
