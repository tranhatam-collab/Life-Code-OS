import {ensure,enumValue,integer} from '../legacy_v2/src/errors.mjs';
import {result} from '../legacy_v2/src/canonical.mjs';
import {normalizeName} from '../legacy_v2/src/names.mjs';
import {root,reduction,digitSum} from '../legacy_v2/src/numbers.mjs';
import {parseDate,birthNumbers} from '../legacy_v2/src/time.mjs';
const value=c=>(c.charCodeAt(0)-65)%9+1;
function lettersProfile(raw,yPolicy,policy){
 const n=normalizeName(raw), letters=[...n.latin.replace(/ /g,'')];
 const counts=Object.fromEntries(Array.from({length:9},(_,i)=>[String(i+1),0]));
 for(const c of letters)counts[value(c)]++;
 const parts=n.latin.split(' ').map(token=>({token,sum:[...token].reduce((s,c)=>s+value(c),0)}));
 const total=parts.reduce((s,p)=>s+p.sum,0), unresolvedY=yPolicy==='unknown'&&letters.includes('Y');
 const vowelSet=yPolicy==='vowel'?'AEIOUY':'AEIOU';
 const vowelSum=unresolvedY?null:letters.filter(c=>vowelSet.includes(c)).reduce((s,c)=>s+value(c),0);
 const consonantSum=unresolvedY?null:total-vowelSum;
 const initialSum=parts.reduce((s,p)=>s+value(p.token[0]),0);
 const freq=Object.values(counts),max=Math.max(...freq);
 return {...n,parts,total,expression:reduction(total,policy),vowel_sum:vowelSum,
 heart_desire:vowelSum===null?null:reduction(vowelSum,policy),consonant_sum:consonantSum,
 personality:consonantSum===null?null:reduction(consonantSum,policy),y_unresolved:unresolvedY,
 counts,initial_sum:initialSum,balance:reduction(initialSum,'single_digit'),
 missing_values:Object.keys(counts).filter(k=>counts[k]===0).map(Number),
 hidden_passion:Object.keys(counts).filter(k=>counts[k]===max).map(Number),
 distinct_count:freq.filter(x=>x>0).length};
}
function providedSpans(spans){
 ensure(Array.isArray(spans)&&spans.length===3,'INVALID_PERIOD_SPANS','Ba phạm vi phải được cung cấp cùng nhau.');
 let next=0;
 return spans.map((s,i)=>{
  integer(s.start_age,0,150,'start_age');ensure(s.start_age===next,'NONCONTIGUOUS_SPANS','Phạm vi tuổi phải liên tiếp từ 0.');
  if(i===2){ensure(s.end_age_exclusive===null,'INVALID_PERIOD_END','Phạm vi cuối dùng end_age_exclusive=null, không dự đoán tuổi thọ.');}
  else {integer(s.end_age_exclusive,s.start_age+1,150,'end_age_exclusive');next=s.end_age_exclusive;}
  return {start_age:s.start_age,end_age_exclusive:s.end_age_exclusive};
 });
}
export function fullNumerology(input){
 const {full_name,birth_date,common_name=null,given_name=null,y_policy='unknown',reduction_policy='preserve_11_22_33',life_path_variant='all_digits',pinnacle_boundary_policy='last_integer_age_inclusive',challenge_span_policy='unmapped',period_span_policy='unmapped'}=input;
 enumValue(y_policy,['unknown','vowel','consonant'],'y_policy');
 enumValue(reduction_policy,['single_digit','preserve_11_22_33'],'reduction_policy');
 enumValue(pinnacle_boundary_policy,['last_integer_age_inclusive','unmapped'],'pinnacle_boundary_policy');
 enumValue(challenge_span_policy,['unmapped','follow_pinnacles'],'challenge_span_policy');
 enumValue(period_span_policy,['unmapped','provided'],'period_span_policy');
 const d=parseDate(birth_date),full=lettersProfile(full_name,y_policy,reduction_policy);
 const minor=common_name===null?null:lettersProfile(common_name,y_policy,reduction_policy);
 const given=given_name===null?null:lettersProfile(given_name,y_policy,reduction_policy);
 const b=birthNumbers({birth_date,reduction_policy,variant:life_path_variant}).calculation;
 const M=root(d.month),D=root(d.day),Y=root(digitSum(String(d.year)));
 const P1=reduction(M+D,reduction_policy),P2=reduction(D+Y,reduction_policy),P3=reduction(P1.value+P2.value,reduction_policy),P4=reduction(M+Y,reduction_policy);
 const C1=Math.abs(M-D),C2=Math.abs(D-Y),Cs=[C1,C2,Math.abs(C1-C2),Math.abs(M-Y)];
 const boundary=36-b.reduction.root;
 const bands=pinnacle_boundary_policy==='unmapped'?null:[{start_age:0,end_age_exclusive:boundary+1},{start_age:boundary+1,end_age_exclusive:boundary+10},{start_age:boundary+10,end_age_exclusive:boundary+19},{start_age:boundary+19,end_age_exclusive:null}];
 const maturity=reduction(b.reduction.value+full.expression.value,reduction_policy);
 const rational=given===null?null:reduction(given.total+d.day,reduction_policy);
 const named={life_path:b.reduction,birthday:reduction(d.day,reduction_policy),expression:full.expression,minor_expression:minor?.expression??null,heart_desire:full.heart_desire,minor_heart_desire:minor?.heart_desire??null,personality:full.personality,minor_personality:minor?.personality??null,maturity,rational_thought:rational,balance:full.balance,month_component:b.components.month,day_component:b.components.day,year_component:b.components.year,pinnacle_1:P1,pinnacle_2:P2,pinnacle_3:P3,pinnacle_4:P4};
 const debtMarkers=Object.entries(named).flatMap(([key,v])=>v===null?[]:v.path.filter(x=>[13,14,16,19].includes(x)).map(x=>({component:key,number:x,meaning:'historical_label_only_no_moral_inference'})));
 const periodSpans=period_span_policy==='provided'?(ensure(typeof input.period_source_note==='string'&&input.period_source_note.trim(),'PERIOD_SOURCE_REQUIRED','Cần ghi nguồn/chính sách cho phạm vi tuổi chu kỳ.'),providedSpans(input.period_spans)):null;
 const components={
 life_path:b.reduction,birthday:{day:d.day,...reduction(d.day,reduction_policy)},karmic_debt_markers:debtMarkers,
 expression:full.expression,minor_expression:minor?.expression??null,heart_desire:full.heart_desire,minor_heart_desire:minor?.heart_desire??null,
 compound_numbers:Object.fromEntries(Object.entries(named).map(([k,v])=>[k,v?.path??null])),personality:full.personality,minor_personality:minor?.personality??null,
 maturity,rational_thought:rational,karmic_lessons:full.missing_values,balance:full.balance,hidden_passion:full.hidden_passion,
 subconscious_confidence:{distinct_name_values:full.distinct_count,scale_max:9,probability:null},
 challenges:Cs,challenge_spans:challenge_span_policy==='follow_pinnacles'?bands:null,
 pinnacles:[P1,P2,P3,P4],pinnacle_spans:bands,
 life_path_periods:{values:[M,D,Y],spans:periodSpans,source_note:period_span_policy==='provided'?input.period_source_note:null},
 life_expression_bridge:Math.abs(b.reduction.root-full.expression.root),
 heart_personality_bridge:full.heart_desire===null?null:Math.abs(full.heart_desire.root-full.personality.root)
 };
 const warnings=['Các chỉ số là kết quả của quy ước; không đo nhân cách, trí tuệ, sức khỏe, giàu nghèo hoặc số phận.'];
 if(full.y_unresolved||minor?.y_unresolved)warnings.push('Chữ Y chưa phân loại: giữ tổng tên; tổng nguyên âm/phụ âm và cầu nối tương ứng là null.');
 if(!given)warnings.push('Chưa xác nhận tên riêng; Rational Thought=null. Không tự lấy từ đầu hoặc cuối tên.');
 if(!periodSpans)warnings.push('Chu kỳ tháng–ngày–năm có giá trị nhưng chưa gán phạm vi tuổi. Không dùng phạm vi Pinnacles thay thế.');
 return result('LCV3-NUM23','3.0',input,{table:'LATIN_CYCLE_1_9',y_policy,reduction_policy,life_path_variant,pinnacle_component_policy:'single_digit_components',pinnacle_boundary_policy,challenge_span_policy,period_span_policy},{components,full_name_profile:full,common_name_profile:minor,given_name_profile:given,birth_trace:b},[{step:'Chuẩn hóa tên không phá bản gốc.'},{step:'Tính 23 thành phần; giữ số ghép, phần thiếu và chính sách riêng.'}],warnings);
}
export function nameVariantComparison(input){
 ensure(Array.isArray(input.variants)&&input.variants.length>=2&&input.variants.length<=12,'INVALID_VARIANTS','Cần 2–12 cách ghi tên có nhãn riêng.');
 const ids=new Set();const rows=input.variants.map(v=>{ensure(typeof v.id==='string'&&!ids.has(v.id),'DUPLICATE_VARIANT','Mã cách ghi tên phải khác nhau.');ids.add(v.id);return {id:v.id,result:fullNumerology({...input.base,full_name:v.name,common_name:null})};});
 return result('LCV3-NAME-COMPARE','3.0',input,{ranking:'none'}, {variants:rows,preferred:null},[],['Không xếp người hoặc tên tốt/xấu; chỉ so phép tính và dữ liệu đã nhập.']);
}
