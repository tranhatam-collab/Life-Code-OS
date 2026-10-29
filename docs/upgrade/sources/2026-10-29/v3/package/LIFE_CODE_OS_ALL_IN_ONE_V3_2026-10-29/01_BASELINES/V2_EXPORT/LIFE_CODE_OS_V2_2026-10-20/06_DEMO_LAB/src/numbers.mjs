import {ensure,integer,enumValue} from './errors.mjs';
import {result} from './canonical.mjs';
export const GROUPS=Object.freeze({SK:['14','41','67','76','39','93','28','82'],TY:['13','31','68','86','49','94','27','72'],DN:['19','91','78','87','34','43','26','62'],PV:['11','22','33','44','66','77','88','99'],TM:['12','21','69','96','48','84','37','73'],NQ:['18','81','79','97','36','63','24','42'],LS:['16','61','47','74','38','83','29','92'],HH:['17','71','89','98','46','64','23','32']});
export const PAIRS=Object.freeze(Object.fromEntries(Object.entries(GROUPS).flatMap(([g,ps])=>ps.map(p=>[p,g]))));
export function digitSum(text){ensure(typeof text==='string'&&/^[0-9]{1,256}$/.test(text),'INVALID_DIGITS','Cần chuỗi từ 1 đến 256 chữ số ASCII.');return [...text].reduce((s,c)=>s+Number(c),0);}
export function root(n){integer(n,0,Number.MAX_SAFE_INTEGER,'n');return n===0?0:1+(n-1)%9;}
export function reduction(n,policy='single_digit') {
 integer(n,0,Number.MAX_SAFE_INTEGER,'n');enumValue(policy,['single_digit','preserve_11_22_33'],'reduction_policy');
 const path=[n];while(n>9 && !(policy==='preserve_11_22_33'&&[11,22,33].includes(n))){n=digitSum(String(n));path.push(n);}return {value:n,path,root:root(n)};
}
export function normalizePhone(raw){
 ensure(typeof raw==='string'&&raw.length<=40,'INVALID_PHONE','Số điện thoại quá dài hoặc sai kiểu.');
 ensure(/^[+0-9 .()-]+$/.test(raw),'INVALID_PHONE','Không nhập máy lẻ, chữ hoặc ký tự không hỗ trợ.');
 let s=raw.replace(/[ .()-]/g,'');
 if(s.startsWith('+84')) s='0'+s.slice(3);else if(s.startsWith('0084'))s='0'+s.slice(4);
 ensure(/^0[0-9]{9}$/.test(s),'INVALID_PHONE','Cần chuỗi nội địa Việt Nam 10 chữ số hoặc dạng +84 tương ứng.');
 return {raw,canonical:s,policy:'VN_DOMESTIC_10_V1',assigned_number_verified:false};
}
export function tail80(input, table){
 const {suffix,zero_policy='unmapped'}=input;
 ensure(typeof suffix==='string'&&/^[0-9]{4}$/.test(suffix),'INVALID_SUFFIX','Nhập đúng bốn chữ số, giữ số 0 ở đầu.');
 enumValue(zero_policy,['unmapped','as80'],'zero_policy');
 const n=Number(suffix),r=n%80,code=r===0?(zero_policy==='as80'?80:null):r;
 const rec=code===null?null:table.records.find(x=>x.code===code);
 ensure(code===null||Boolean(rec),'MISSING_TABLE_ROW','Bảng nghĩa thiếu mã cần tra.');
 const out=result('LCF-01','2.0',input,{zero_policy,table_version:table.table_version},{suffix,quotient:Math.floor(n/80),remainder:r,lookup_code:code,source_label:rec?.source_label??null,is_personalized:false},[{formula:'N = 80*q + r',substitution:`${n} = 80*${Math.floor(n/80)} + ${r}`}],r===0&&code===null?['ZERO_POLICY_NOT_APPROVED']:[]);
 out.symbolic_source_text=rec?.source_text??rec?.original_text??null; return out;
}
export function pairAnalysis(input){
 const {digits,policy='strict'}=input;ensure(typeof digits==='string'&&/^[0-9]{2,32}$/.test(digits),'INVALID_DIGITS','Cần 2–32 chữ số.');enumValue(policy,['strict','bridge5_diagnostic'],'policy');
 const strict=[...digits.slice(0,-1)].map((_,i)=>({index:i,pair:digits.slice(i,i+2),group:PAIRS[digits.slice(i,i+2)]??null}));
 const mapped=policy==='strict'?digits:digits.replace(/5/g,'');
 const evaluated=policy==='strict'?strict:[...mapped.slice(0,-1)].map((_,i)=>({index:i,pair:mapped.slice(i,i+2),group:PAIRS[mapped.slice(i,i+2)]??null}));
 const counts=Object.fromEntries(Object.keys(GROUPS).map(k=>[k,evaluated.filter(p=>p.group===k).length]));
 return result('LCF-02','2.0',input,{policy,table_version:'legacy64-preserved-v1'},{original_digits:digits,evaluated_digits:mapped,pairs:evaluated,strict_pairs:strict,counts,known:evaluated.filter(p=>p.group!==null).length,total:evaluated.length,unresolved:evaluated.filter(p=>p.group===null)},[{step:'Tách cặp liền nhau có chồng lấn; vị trí tính từ 0.'}],policy==='strict'?(evaluated.some(p=>p.group===null)?['ZERO_FIVE_UNRESOLVED']:[]):['DIAGNOSTIC_ONLY_NOT_AN_APPROVED_TRADITIONAL_RULE']);
}
export function digitMatrix(input){
 const {digits}=input;ensure(typeof digits==='string'&&/^[0-9]{1,64}$/.test(digits),'INVALID_DIGITS','Cần 1–64 chữ số.');
 const counts=Object.fromEntries('0123456789'.split('').map(k=>[k,[...digits].filter(c=>c===k).length]));
 const axes=[[1,4,7],[2,5,8],[3,6,9],[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7]].map(a=>({digits:a,count:a.reduce((s,d)=>s+counts[d],0)}));
 return result('LCF-03','2.0',input,{policy:'raw_frequency_only'},{counts,axes,zero_count:counts['0']},[],['Không tạo số phụ Psychomatrix khi chưa khóa trường phái.','Ô trống không có nghĩa thiếu trí nhớ, sức khỏe, may mắn hoặc đạo đức.']);
}
export function sequenceFeatures(input){const {digits}=input;ensure(typeof digits==='string'&&/^[0-9]{1,64}$/.test(digits),'INVALID_DIGITS','Cần chuỗi chữ số.');const runs=digits.match(/(.)\1*/g).map(s=>({digit:s[0],length:s.length}));return result('LCF-04','2.0',input,{policy:'descriptive'},{length:digits.length,unique_digits:new Set(digits).size,palindrome:digits===[...digits].reverse().join(''),runs,digit_sum:digitSum(digits),root:root(digitSum(digits))},[],['Không suy khả năng ghi nhớ của người dùng từ đặc điểm chuỗi.']);}
