import {createHash} from 'node:crypto';
import {ensure} from './errors.mjs';
// Deliberately narrower than RFC 8785: finite safe integers, strings, booleans,
// null, arrays, plain objects. Not a full JCS implementation; version every change.
export function canonical(value, depth=0) {
  ensure(depth<=24,'MAX_DEPTH','Dữ liệu lồng quá sâu.');
  if(value===null || typeof value==='boolean') return JSON.stringify(value);
  if(typeof value==='string') {ensure(!/[\uD800-\uDBFF](?![\uDC00-\uDFFF])|(?<![\uD800-\uDBFF])[\uDC00-\uDFFF]/u.test(value),'INVALID_UNICODE','Chuỗi chứa surrogate không ghép cặp.');return JSON.stringify(value);}
  if(typeof value==='number'){ensure(Number.isSafeInteger(value),'UNSAFE_NUMBER','Digest chỉ nhận số nguyên an toàn; số đo thập phân phải dùng chuỗi hoặc cấu trúc phân số.');return JSON.stringify(value);}
  if(Array.isArray(value)) return '['+value.map(v=>canonical(v,depth+1)).join(',')+']';
  ensure(typeof value==='object'&&Object.getPrototypeOf(value)===Object.prototype,'INVALID_CANONICAL_TYPE','Không hỗ trợ kiểu dữ liệu này trong canonical JSON.');
  return '{'+Object.keys(value).sort().map(k=>JSON.stringify(k)+':'+canonical(value[k],depth+1)).join(',')+'}';
}
export function digest(value){return createHash('sha256').update(canonical(value)).digest('hex');}
export function result(methodId, version, input, configuration, calculation, trace=[], warnings=[]) {
 const basis={canonical_version:'lc-safe-json-1',method_id:methodId,method_version:version,input,configuration};
 return {method_id:methodId,method_version:version,status:'REFERENCE_ONLY',claim_type:'derived_metric',input_digest:digest(basis),digest_scope:'LOCAL_DEMO_NOT_ANONYMIZATION',configuration,calculation,trace,warnings,score:null,confidence:null,probability:null,limitations:['Không phải dự báo tính cách, sức khỏe, tài lộc hoặc số phận.','Không được mở production chỉ dựa vào demo.']};
}
