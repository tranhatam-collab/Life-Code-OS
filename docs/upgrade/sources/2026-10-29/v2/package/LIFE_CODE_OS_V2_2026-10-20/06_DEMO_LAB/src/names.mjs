import {ensure,enumValue} from './errors.mjs';
import {result} from './canonical.mjs';
import {reduction} from './numbers.mjs';
export function normalizeName(raw){
 ensure(typeof raw==='string'&&raw.trim().length>0&&raw.length<=200,'INVALID_NAME','Tên phải có nội dung và không dài quá 200 ký tự.');
 ensure(!/[\u0000-\u001F\u007F]/.test(raw),'INVALID_NAME','Tên có ký tự điều khiển.');
 const nfc=raw.normalize('NFC').trim().replace(/\s+/g,' ');
 const latin=nfc.normalize('NFD').replace(/\p{M}/gu,'').replace(/[đĐ]/g,'D').toUpperCase();
 ensure(/^[A-Z ]+$/.test(latin),'UNSUPPORTED_SCRIPT','Chính sách VI-Latin chưa hỗ trợ văn tự hoặc dấu câu này; không đoán cách chuyển tự.');
 return {original:raw,nfc,latin,transliteration_policy:'VI_LATIN_EXPLICIT_1'};
}
export function nameNumbers(input){
 const {name,reduction_policy='single_digit',y_policy='exclude'}=input;
 enumValue(y_policy,['exclude','include'],'y_policy'); const n=normalizeName(name);
 const val=c=>(c.charCodeAt(0)-65)%9+1;
 const parts=n.latin.split(' ').map(p=>({text:p,letters:[...p].map(c=>({letter:c,value:val(c)})),sum:[...p].reduce((s,c)=>s+val(c),0)}));
 const letters=[...n.latin.replace(/ /g,'')],vowels=y_policy==='include'?'AEIOUY':'AEIOU';
 const sum=parts.reduce((s,p)=>s+p.sum,0),vowelSum=letters.filter(c=>vowels.includes(c)).reduce((s,c)=>s+val(c),0);
 return result('LCF-05','2.0',input,{table:'LATIN_CYCLE_1_9',reduction_policy,y_policy},{...n,parts,sum,reduction:reduction(sum,reduction_policy),vowel_sum:vowelSum,consonant_sum:sum-vowelSum,initial_sum:parts.reduce((s,p)=>s+val(p.text[0]),0)},[{step:'Giữ tên gốc; tạo chuỗi quy đổi độc lập.'}],['Ý nghĩa của tên cần nguồn gia đình hoặc ngữ nghĩa xác nhận; không suy từ con số.','Y được xử lý theo cấu hình hiển thị, không có mặc định phổ quát cho mọi tên.']);
}
