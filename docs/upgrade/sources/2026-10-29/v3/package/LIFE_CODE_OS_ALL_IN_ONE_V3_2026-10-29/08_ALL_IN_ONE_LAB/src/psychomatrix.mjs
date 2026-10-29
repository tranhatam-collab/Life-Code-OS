import {ensure,enumValue} from '../legacy_v2/src/errors.mjs';
import {parseDate} from '../legacy_v2/src/time.mjs';
import {digitSum} from '../legacy_v2/src/numbers.mjs';
import {result} from '../legacy_v2/src/canonical.mjs';
const axes=[[1,4,7],[2,5,8],[3,6,9],[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7]];
export function psychomatrix(input){
 const {birth_date,variant='raw_birth_digits'}=input;const d=parseDate(birth_date);
 enumValue(variant,['raw_birth_digits','four_working_subtractive'],'variant');
 const birthDigits=birth_date.replace(/-/g,''),rawCounts=Object.fromEntries(Array.from({length:10},(_,i)=>[i,0]));
 for(const c of birthDigits)rawCounts[c]++;
 let working=null,all=birthDigits;
 if(variant==='four_working_subtractive'){
  const w1=digitSum(birthDigits),w2=digitSum(String(w1)),firstDayDigit=Number(String(d.day)[0]),w3=w1-2*firstDayDigit;
  ensure(w3>=0,'NEGATIVE_WORKING_NUMBER','Biến thể bốn số phụ này không hỗ trợ số thứ ba âm; không tự lấy trị tuyệt đối.');
  const w4=digitSum(String(w3));working={w1,w2,w3,w4,first_day_digit:firstDayDigit};all+=[w1,w2,w3,w4].join('');
 }
 const counts=Object.fromEntries(Array.from({length:9},(_,i)=>[i+1,0]));for(const c of all)if(c!=='0')counts[c]++;
 const cells=Object.entries(counts).map(([digit,count])=>({digit:Number(digit),count,display:digit.repeat(count)||'—'}));
 const lines=axes.map(ds=>({digits:ds,count:ds.reduce((s,x)=>s+counts[x],0),public_label:`Trục ${ds.join('–')}`,trait_inference:null}));
 return result('LCV3-PSYCHO17','3.0',input,{variant,zero_policy:'kept_in_trace_not_cells',day_leading_zero:'not_used_for_first_day_digit'}, {birth_digits:birthDigits,raw_counts:rawCounts,working_numbers:working,cells,axes:lines},[],['Không suy ra trí nhớ, sức khỏe, khả năng học, đạo đức hay đời sống riêng tư từ số lượng chữ số.','Bản bốn số phụ là một cấu hình được khai báo; không đại diện tất cả trường phái hoặc biến thể sau năm 2000.']);
}
