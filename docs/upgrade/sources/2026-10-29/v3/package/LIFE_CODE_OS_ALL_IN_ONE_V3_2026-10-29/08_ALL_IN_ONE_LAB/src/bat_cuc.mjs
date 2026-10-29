import {readFileSync} from 'node:fs';
import {ensure,enumValue} from '../legacy_v2/src/errors.mjs';
import {result} from '../legacy_v2/src/canonical.mjs';
import {normalizePhone,digitSum,root} from '../legacy_v2/src/numbers.mjs';
const rows=JSON.parse(readFileSync(new URL('../data/BAT_CUC_64_PAIRS.json',import.meta.url),'utf8'));
const map=Object.fromEntries(rows.map(r=>[r.pair,r]));
const rules=JSON.parse(readFileSync(new URL('../data/BAT_CUC_TRANSITION_8X8.json',import.meta.url),'utf8'));
const ruleMap=Object.fromEntries(rules.map(r=>[r.transition_id,r]));
const known=/^[12346789]$/;
function canonicalDigits(input){
 const context=input.context??'generic_sequence';
 enumValue(context,['phone_vn','generic_sequence','identifier_suffix4'],'context');
 if(context==='phone_vn')return {context,digits:normalizePhone(input.sequence).canonical};
 if(context==='identifier_suffix4'){ensure(typeof input.sequence==='string'&&/^\d{4}$/.test(input.sequence),'SUFFIX_ONLY','Định danh chỉ nhận bốn số cuối, không nhận toàn bộ số căn cước.');return {context,digits:input.sequence};}
 ensure(typeof input.sequence==='string'&&/^\d{2,32}$/.test(input.sequence),'INVALID_SEQUENCE','Dãy tham chiếu cần 2–32 chữ số; không nhập PIN, OTP hoặc mật khẩu.');return {context,digits:input.sequence};
}
export function batCuc(input){
 const {policy='strict_adjacent_v3'}=input;
 enumValue(policy,['strict_adjacent_v3','bridge_single_0_5_diagnostic_v3'],'policy');
 const {context,digits}=canonicalDigits(input);
 const pairs=Array.from({length:digits.length-1},(_,i)=>{const p=digits.slice(i,i+2),r=map[p];return {index:i,span:[i,i+2],pair:p,group_id:r?.group_id??null,name_vi:r?.name_vi??null,status:r?'mapped':'unresolved_0_or_5',intensity:null};});
 const transitions=[];for(let i=0;i<pairs.length-1;i++){const a=pairs[i],b=pairs[i+1];const rule=a.group_id&&b.group_id?ruleMap[`${a.group_id}_${b.group_id}`]:null;transitions.push({index:i,triple:digits.slice(i,i+3),from:a.group_id,to:b.group_id,question:rule?.reflection_question??null,status:rule?'editorial_question_only':'unresolved',prediction:null});}
 const matrix=Object.fromEntries(rules.map(r=>[r.transition_id,0]));for(const t of transitions)if(t.from&&t.to)matrix[`${t.from}_${t.to}`]++;
 const bridges=[];if(policy==='bridge_single_0_5_diagnostic_v3')for(let i=1;i<digits.length-1;i++)if(/[05]/.test(digits[i])&&known.test(digits[i-1])&&known.test(digits[i+1])){const p=digits[i-1]+digits[i+1];bridges.push({span:[i-1,i+2],original:digits.slice(i-1,i+2),modifier:digits[i],pair:p,group_id:map[p].group_id,status:'diagnostic_not_approved',multiplier:null});}
 const unresolvedRuns=[...digits.matchAll(/[05]{2,}/g)].map(m=>({span:[m.index,m.index+m[0].length],digits:m[0],status:'no_silent_deletion'}));
 const repetitions=[...digits.matchAll(/(\d)\1+/g)].map(m=>({span:[m.index,m.index+m[0].length],digit:m[1],length:m[0].length,group_id:map[m[1].repeat(2)]?.group_id??null}));
 const counts=Object.fromEntries(['SK','TY','DN','PV','TM','NQ','LS','HH'].map(g=>[g,0]));for(const p of pairs)if(p.group_id)counts[p.group_id]++;
 const conflictingExamples=['876','678'].filter(s=>digits.includes(s));
 return result('LCV3-BC-COMPOSE','3.0',input,{context,policy,pair_table:'source_reference_64_v3',transition_text:'original_editorial_draft',intensity_policy:'unconfigured'}, {canonical_sequence:digits,pairs,counts,known_pair_count:pairs.filter(p=>p.group_id).length,total_pairs:pairs.length,coverage:{numerator:pairs.filter(p=>p.group_id).length,denominator:pairs.length},transitions,transition_matrix:matrix,diagnostic_bridges:bridges,unresolved_modifier_runs:unresolvedRuns,repetitions,ending_pairs:pairs.slice(-2),digit_sum:digitSum(digits),digit_root:root(digitSum(digits)),source_conflicting_examples:conflictingExamples,personal_fit:null},[{step:'Giữ nguyên dãy và vị trí gốc; chỉ chuẩn hóa điện thoại theo context.'},{step:'Cặp, tổ hợp, phần chưa biết và cầu chẩn đoán là các trường riêng.'}],['Không chuyển nhãn truyền thống thành kết luận sức khỏe, tính cách, tai họa hoặc thu nhập.','Cầu qua số 0/5 không phải hệ số năng lượng và không xóa cặp gốc.','Các câu hỏi ma trận 8×8 là biên tập HNH mới chờ duyệt, không phải bảng cổ truyền đã xác minh.']);
}
export function compareNumbers(input){
 ensure(Array.isArray(input.sequences)&&input.sequences.length>=2&&input.sequences.length<=20,'INVALID_COMPARISON','Cần 2–20 dãy để đối chiếu.');
 const ids=new Set();const items=input.sequences.map(s=>{ensure(typeof s.id==='string'&&!ids.has(s.id),'DUPLICATE_ITEM','Mã dãy phải duy nhất.');ids.add(s.id);return {id:s.id,result:batCuc({sequence:s.sequence,context:s.context??input.context??'phone_vn',policy:input.policy??'strict_adjacent_v3'})};});
 const equivalent=[];for(let i=0;i<items.length;i++)for(let j=i+1;j<items.length;j++){const a=items[i].result.calculation,b=items[j].result.calculation;if(JSON.stringify(a.counts)===JSON.stringify(b.counts)&&a.digit_root===b.digit_root)equivalent.push([items[i].id,items[j].id]);}
 return result('LCV3-NUM-COMPARE','3.0',input,{ranking:'none_without_explicit_utility_policy'},{items,equal_counts_and_root:equivalent,recommended:null},[],['Không tự xếp SIM hợp người; giá và quyền sử dụng chưa được xác minh.']);
}
