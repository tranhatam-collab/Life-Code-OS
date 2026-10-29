/** Deterministic reference. Not a prediction model or production service. */
export function digitalRoot(n) {
  if (!Number.isSafeInteger(n) || n < 0) throw new TypeError('Yêu cầu số nguyên an toàn không âm.');
  return n === 0 ? 0 : 1 + ((n - 1) % 9);
}
export function digitSum(s) {
  if (typeof s !== 'string' || !/^[0-9]+$/.test(s)) throw new TypeError('Chuỗi chỉ gồm chữ số.');
  return [...s].reduce((a,c)=>a+Number(c),0);
}
export function normalizeVietnameseName(s) {
  if (typeof s !== 'string' || !s.trim() || s.length > 200) throw new TypeError('Tên không hợp lệ.');
  const original = s;
  const nfc = s.normalize('NFC').trim().replace(/\s+/g,' ');
  const latin = nfc.normalize('NFD').replace(/\p{M}/gu,'').replace(/[đĐ]/g,'D').toUpperCase();
  if (!/^[A-Z ]+$/.test(latin)) throw new TypeError('Chính sách Latin này chưa hỗ trợ văn tự/ký hiệu trong tên.');
  return {original,nfc,latin,policy:'VI_NFC_LATIN_0.1'};
}
export function nameCycle(s) {
  const n=normalizeVietnameseName(s);
  const parts=n.latin.split(' ').map(part=>({part,sum:[...part].reduce((a,c)=>a+((c.charCodeAt(0)-65)%9+1),0)}));
  const sum=parts.reduce((a,p)=>a+p.sum,0);
  return {...n,parts,sum,root:digitalRoot(sum),prediction:false};
}
export function tail80(suffix,{zeroPolicy='unmapped',table=null}={}) {
  if (typeof suffix!=='string' || !/^[0-9]{4}$/.test(suffix)) throw new TypeError('Nhập đúng bốn chữ số.');
  if (!['unmapped','as80'].includes(zeroPolicy)) throw new TypeError('Quy tắc số dư 0 chưa hợp lệ.');
  const n=Number(suffix),remainder=n%80,lookup=remainder===0?(zeroPolicy==='as80'?80:null):remainder;
  const row=lookup===null?null:table?.records.find(r=>r.code===lookup);
  return {method_id:'lc_tail4_mod80',suffix,quotient:Math.floor(n/80),remainder,lookup_code:lookup,zero_policy:zeroPolicy,table_version:table?.table_version??'not_loaded',source_label:row?.source_label??null,is_personalized:false,probability:null};
}
const groups={
  SK:['14','41','67','76','39','93','28','82'],TY:['13','31','68','86','49','94','27','72'],DN:['19','91','78','87','34','43','26','62'],PV:['11','22','33','44','66','77','88','99'],TM:['12','21','69','96','48','84','37','73'],NQ:['18','81','79','97','36','63','24','42'],LS:['16','61','47','74','38','83','29','92'],HH:['17','71','89','98','46','64','23','32']
};
export const pairMap=Object.freeze(Object.fromEntries(Object.entries(groups).flatMap(([k,v])=>v.map(p=>[p,k]))));
export function analyzePairs(s) {
  if (typeof s!=='string' || !/^[0-9]{2,32}$/.test(s)) throw new TypeError('Cần chuỗi từ 2 đến 32 chữ số.');
  const pairs=[...s.slice(0,-1)].map((_,i)=>({index:i,pair:s.slice(i,i+2),group:pairMap[s.slice(i,i+2)]??null}));
  return {pairs,known:pairs.filter(p=>p.group!==null).length,total:pairs.length,unresolved:pairs.filter(p=>p.group===null),prediction:false};
}
