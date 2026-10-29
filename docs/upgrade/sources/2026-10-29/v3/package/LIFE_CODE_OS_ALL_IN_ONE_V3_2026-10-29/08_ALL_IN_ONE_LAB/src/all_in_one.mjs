import {ensure} from '../legacy_v2/src/errors.mjs';
import {result} from '../legacy_v2/src/canonical.mjs';
import {fullNumerology} from './numerology_full.mjs';
import {psychomatrix} from './psychomatrix.mjs';
import {batCuc} from './bat_cuc.mjs';
import {lifetimeMap} from './lifetime.mjs';
export function allInOne(input){
 ensure(input.profile&&typeof input.profile==='object','PROFILE_REQUIRED','Cần hồ sơ đầu vào.');
 const {profile,as_of,selected=['numerology','raw_matrix','lifetime'],goal=null}=input;
 ensure(Array.isArray(selected)&&selected.length<=8&&new Set(selected).size===selected.length,'INVALID_SELECTION','Chọn các mô-đun duy nhất.');
 const supported=['numerology','raw_matrix','working_matrix','bat_cuc','lifetime'];
 ensure(selected.every(x=>supported.includes(x)),'METHOD_NOT_RELEASED','Demo chỉ chạy các mô-đun được liệt kê; không tự tạo kết quả cho phương pháp chưa có.');
 const results={},missing=[];function add(key,condition,fn,required){if(condition)results[key]=fn();else missing.push({module:key,missing:required});}
 for(const x of selected){
  if(x==='numerology')add(x,profile.full_name&&profile.birth_date,()=>fullNumerology({...profile,y_policy:profile.y_policy??'unknown'}),['full_name','birth_date']);
  if(x==='raw_matrix'||x==='working_matrix')add(x,profile.birth_date,()=>psychomatrix({birth_date:profile.birth_date,variant:x==='raw_matrix'?'raw_birth_digits':'four_working_subtractive'}),['birth_date']);
  if(x==='bat_cuc')add(x,input.number_sequence,()=>batCuc({sequence:input.number_sequence,context:'phone_vn',policy:input.bat_cuc_policy??'strict_adjacent_v3'}),['number_sequence']);
  if(x==='lifetime')add(x,profile.birth_date&&as_of,()=>lifetimeMap({birth_date:profile.birth_date,as_of,events:input.events??[],plans:input.plans??[],cycle_years:input.cycle_years??3}),['birth_date','as_of']);
 }
 if(goal!==null)ensure(typeof goal==='string'&&goal.trim()&&goal.length<=800,'INVALID_GOAL','Mục tiêu phải là câu ngắn do người dùng cung cấp.');
 const sections=[
 {id:'identity',title:'Dữ liệu gốc và phạm vi',text:`Hồ sơ dùng tên và ngày do người nhập cung cấp. ${profile.birth_time?'Giờ được lưu để tham chiếu; chưa dùng cho các phép tính này.':'Giờ sinh chưa được cung cấp; không tự điền.'}`,type:'self_report'},
 {id:'analysis',title:'Kết quả và giới hạn',text:`Đã tính ${Object.keys(results).length} mô-đun tham chiếu. Các tổng, cặp số và ma trận là phép biến đổi dữ liệu, không phải bằng chứng về nội tâm hoặc biến cố.`,type:'derived_metric'},
 {id:'timeline',title:'Dòng đời',text:'Lịch sử do người dùng kể, chu kỳ biểu tượng và kế hoạch được giữ thành các đường riêng. Các khoảng trống không được viết thành chuyện đời.',type:'guidance'},
 {id:'action',title:'Bước tiếp theo',text:goal?`Mục tiêu được nhập: ${goal}. Hãy chọn một bước có thể hoàn thành, thời hạn và cách tự xem lại.`:'Chưa có mục tiêu: báo cáo không tự quyết định nhiệm vụ cuộc đời. Người dùng chọn một vấn đề muốn làm rõ trước.',type:'guidance'}
 ];
 const levelStates=Array.from({length:9},(_,i)=>({level:i+1,product_state:'DESIGN_CONTRACT_NOT_FULLY_IMPLEMENTED',report_in_this_demo:i===0?'FOUR_BLOCK_REFERENCE_PREVIEW':'NOT_GENERATED',production_eligibility:'NOT_EVALUATED'}));
 return result('LCV3-ALL-IN-ONE','3.0',input,{mode:'LOCAL_REFERENCE_NO_STORAGE',selected},{method_results:results,missing_inputs:missing,report_sections:sections,level_states:levelStates,life_code_index:null,personal_fate_prediction:null},[],['Bản xem trước dùng mẫu biên tập cố định, không gọi AI hoặc mở khóa chín sản phẩm sản xuất.','Hash phục vụ tái lập trong demo; không phải mã ẩn danh và không được công bố cùng dữ liệu cá nhân.']);
}
