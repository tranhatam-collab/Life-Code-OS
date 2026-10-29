import {ensure} from './errors.mjs';
import {digest} from './canonical.mjs';
import {nameNumbers} from './names.mjs';
import {birthNumbers,personalCycle,ageTimeline,localTimeCandidates,compareHypotheses,parseDate} from './time.mjs';
import {inputCoverage} from './metrics.mjs';

// Reference orchestration only. Production authorization must happen before this function.
export function profilePipeline(input){
 const {subject_alias='Hồ sơ tổng hợp A',profile={},goal='Hoàn thành một dự án nhỏ trong 30 ngày.',as_of='2026-10-20',hypotheses=[]}=input;
 ensure(typeof subject_alias==='string'&&subject_alias.length<=80&&typeof goal==='string'&&goal.length<=500,'INVALID_PIPELINE','Tên hoặc mục tiêu không hợp lệ.');
 ensure(profile&&typeof profile==='object'&&!Array.isArray(profile),'INVALID_PIPELINE','Hồ sơ cần là đối tượng.');
 parseDate(as_of);ensure(Array.isArray(hypotheses)&&hypotheses.length<=5,'INVALID_HYPOTHESES','Tối đa năm phương án.');
 const goalSentence=goal.trim().replace(/[.!?…]+$/u,'')+'.';
 const results=[],valid=[],missing=[],warnings=[];
 if(profile.full_name){results.push(nameNumbers({name:profile.full_name,y_policy:'exclude'}));valid.push('name');}else missing.push('full_name');
 if(hypotheses.length){results.push(compareHypotheses({hypotheses}));missing.push('selected_birth_hypothesis');warnings.push('Ngày sinh còn nhiều phương án; chưa chạy chu kỳ hoặc timeline chung.');}
 else if(profile.birth_date){results.push(birthNumbers({birth_date:profile.birth_date}));results.push(personalCycle({birth_date:profile.birth_date,year:Number(as_of.slice(0,4)),boundary:'calendar'}));results.push(ageTimeline({birth_date:profile.birth_date,as_of}));valid.push('birth_date');
 if(profile.birth_time&&profile.time_zone)results.push(localTimeCandidates({date:profile.birth_date,time:profile.birth_time,time_zone:profile.time_zone}));
 else {if(!profile.birth_time)missing.push('birth_time');if(!profile.time_zone)missing.push('time_zone');}
 }else missing.push('birth_date');
 if(goal.trim())valid.push('goal');else missing.push('goal');
 const coverage=inputCoverage({product_release:'self-signal.demo.2',valid_field_ids:valid});
 const n=results.find(x=>x.method_id==='LCF-05')?.calculation;
 const b=results.find(x=>x.method_id==='LCF-07')?.calculation;
 const cy=results.find(x=>x.method_id==='LCF-08')?.calculation;
 const sections=[
 {id:'identity',title:'Dữ liệu được sử dụng',block:'identity',content_role:'input_summary',text:`${subject_alias} là hồ sơ tổng hợp dùng để kiểm tra luồng. Mục tiêu do người dùng lựa chọn: ${goalSentence} Không nhận diện người thật hoặc suy đoán giới tính.`,evidence_ids:['input.profile','input.goal']},
 {id:'analysis',title:'Kết quả tính và cách đọc',block:'analysis',content_role:'method_explanation',text:[n?`Theo bảng Latin demo, tổng tên là ${n.sum}.`: 'Chưa có tên hợp lệ để tính.',b?`Tổng chữ số ngày sinh là ${b.raw_digit_sum}; chuỗi rút gọn: ${b.reduction.path.join(' → ')}.`:'Ngày sinh chưa được khóa; không điền một ngày giả.', 'Những kết quả này là phép quy đổi theo cấu hình, không đo trí tuệ, đạo đức, sức khỏe hoặc giá trị con người.'].join(' '),evidence_ids:results.map(x=>x.method_id)},
 {id:'timeline',title:'Thời gian và phạm vi',block:'timeline',content_role:'symbolic_context',text:cy?`Chu kỳ số theo năm dương lịch đang cho mã ${cy.personal_year} ở năm ${cy.effective_year}. Mã được trình bày riêng với lịch hành động, không biến thành năm thành công hoặc tai họa. Khung tuổi chỉ là các khoảng lịch không kèm biến cố.`:'Chưa tạo chu kỳ hoặc dòng thời gian cá nhân vì ngày sinh thiếu hoặc còn nhiều phương án.',evidence_ids:cy?['LCF-08','LCF-06']:['input.profile']},
 {id:'action',title:'Một bước thực tế trong 30 ngày',block:'action',content_role:'planning_guidance',text:`Tuần 1: viết đầu ra cụ thể của mục tiêu “${goal}”. Tuần 2: chọn lịch thực hiện vừa sức. Tuần 3: ghi việc đã làm và điều cản trở. Tuần 4: xem lại kết quả theo tiêu chí tự chọn; sửa kế hoạch thay vì cố làm cho trải nghiệm khớp một lời luận.`,evidence_ids:['input.goal']}
 ];
 return {pipeline_version:'2.0.reference',level:1,subject_alias,state:hypotheses.length?'NEEDS_INPUT_CHOICE':missing.length?'PARTIAL_REFERENCE':'DRAFT_REFERENCE_ONLY',input_digest:digest(input),sections,method_results:results,data_coverage:coverage.calculation,missing_inputs:missing,warnings,score:null,confidence:null,probability:null,production_ready:false};
}
