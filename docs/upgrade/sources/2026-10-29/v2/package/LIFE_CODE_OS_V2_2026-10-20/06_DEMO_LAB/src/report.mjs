import {ensure,integer} from './errors.mjs';
import {digest} from './canonical.mjs';
export const LEVELS=['Self Signal','Inner Architecture','Behavior Code','Work & Wealth Code','Relationship Field','Life Timeline','Body Intelligence','Mission Path','Full Life Code'];
export function assembleReport(input){
 const {level=1,subject_alias='Hồ sơ minh họa',method_results=[],goal='Chọn một việc có thể hoàn thành trong 30 ngày.'}=input;integer(level,1,9,'level');
 ensure(typeof subject_alias==='string'&&subject_alias.length<=80&&typeof goal==='string'&&goal.length<=500,'INVALID_REPORT_INPUT','Tên hiển thị hoặc mục tiêu quá dài.');
 ensure(Array.isArray(method_results)&&method_results.length<=20,'INVALID_RESULTS','Tối đa 20 kết quả cho bản minh họa.');
 const missing={1:[],2:['values_and_real_examples'],3:['behavior_journal'],4:['work_and_cashflow_data'],5:['each_subject_sharing_grant'],6:['verified_event_history'],7:['specialist_scope_and_image_permission'],8:['chosen_values_and_service_experiment'],9:['approved_relevant_level_outputs']}[level];
 const sections=[
 {id:'identity',title:'Dữ liệu căn cứ',block:'identity',content_role:'input_summary',text:`${subject_alias} là tên giả trong môi trường thử. Mục tiêu đang chọn: ${goal}`,evidence_ids:['demo.input']},
 {id:'analysis',title:'Kết quả và giới hạn',block:'analysis',content_role:'method_explanation',text:`Có ${method_results.length} kết quả tham chiếu. Các phép tính được trình bày riêng, không hợp nhất thành điểm số phận.`,evidence_ids:method_results.map((_,i)=>`method.${i}`)},
 {id:'timeline',title:'Hiện tại và bước tiếp theo',block:'timeline',content_role:'scope_explanation',text:'Lịch hành động do người dùng lựa chọn. Chưa có mô hình dự báo biến cố; không tạo năm rủi ro hoặc thời điểm sứ mệnh.',evidence_ids:['demo.input']},
 {id:'action',title:'Kế hoạch 30 ngày',block:'action',content_role:'planning_guidance',text:'Tuần 1: ghi dữ liệu ban đầu. Tuần 2: chọn một thay đổi nhỏ. Tuần 3: thực hiện và ghi nhận. Tuần 4: xem lại điều phù hợp và điều cần đổi.',evidence_ids:['demo.input']}
 ];
 return {report_schema_version:'2.0',level,level_name:LEVELS[level-1],subject_alias,state:missing.length?'BLOCKED_TEMPLATE_PREVIEW':'DRAFT_REFERENCE_ONLY',content_digest:digest({level,subject_alias,goal,method_input_digests:method_results.map(r=>r.input_digest??r.method_id)}),sections,method_results,missing_requirements:missing,score:null,probability:null,production_ready:false};
}
