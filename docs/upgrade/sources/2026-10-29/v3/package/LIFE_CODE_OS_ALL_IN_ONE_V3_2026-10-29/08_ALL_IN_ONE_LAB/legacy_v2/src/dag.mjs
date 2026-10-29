import {ensure} from './errors.mjs';
import {digest} from './canonical.mjs';
export function planDag(input){
 const {nodes}=input;ensure(Array.isArray(nodes)&&nodes.length<=64,'INVALID_DAG','Tối đa 64 nút phương pháp.');
 const byId=new Map();for(const n of nodes){ensure(n&&typeof n.id==='string'&&n.id.length>0&&Array.isArray(n.depends_on),'INVALID_NODE','Mỗi nút cần ID và danh sách phụ thuộc.');ensure(!byId.has(n.id),'DUPLICATE_NODE','ID nút bị trùng.');ensure(new Set(n.depends_on).size===n.depends_on.length,'DUPLICATE_DEPENDENCY','Một phụ thuộc không được lặp.');byId.set(n.id,n);}
 for(const n of nodes)for(const dep of n.depends_on)ensure(byId.has(dep),'MISSING_DEPENDENCY',`Thiếu nút phụ thuộc: ${dep}`);
 const active=new Set(),done=new Set(),order=[];function visit(id){ensure(!active.has(id),'DAG_CYCLE','Phụ thuộc tạo chu trình.');if(done.has(id))return;active.add(id);for(const dep of [...byId.get(id).depends_on].sort())visit(dep);active.delete(id);done.add(id);order.push(id);}
 for(const id of [...byId.keys()].sort())visit(id);
 const depth=new Map();for(const id of order)depth.set(id,byId.get(id).depends_on.length?1+Math.max(...byId.get(id).depends_on.map(d=>depth.get(d))):0);
 const waves=[];for(const id of order)(waves[depth.get(id)]??=[]).push(id);
 return {order,waves,graph_digest:digest(nodes),status:'REFERENCE_PLAN_ONLY',production_ready:false};
}
export function impactClosure(input){const plan=planDag(input);const changed=input.changed??[];ensure(Array.isArray(changed)&&changed.every(x=>plan.order.includes(x)),'INVALID_CHANGED_NODE','Nút thay đổi không nằm trong đồ thị.');const impacted=new Set(changed);for(const id of plan.order){const n=input.nodes.find(x=>x.id===id);if(n.depends_on.some(x=>impacted.has(x)))impacted.add(id);}return {impacted:plan.order.filter(x=>impacted.has(x)),unchanged:plan.order.filter(x=>!impacted.has(x)),recalculation_policy:'recheck_authorization_before_execution'};}
export function buildCacheKey(input){for(const k of ['tenant_id','subject_id','input_digest','method_release','rule_digest','purpose','locale_release'])ensure(typeof input[k]==='string'&&input[k].length>0,'INVALID_CACHE_CONTEXT',`Thiếu ${k}`);ensure(Number.isSafeInteger(input.access_revision)&&input.access_revision>0,'INVALID_CACHE_REVISION','Cần phiên bản quyền.');return {cache_key:'lc2:'+digest(input),scope:'tenant_subject_purpose_version',notice:'SHA-256 demo; production cần keyed pseudonymization và retention phù hợp.'};}
