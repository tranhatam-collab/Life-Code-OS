import {ensure,enumValue} from '../legacy_v2/src/errors.mjs';
import {result} from '../legacy_v2/src/canonical.mjs';
import {parseDate,ageTimeline,personalCycle} from '../legacy_v2/src/time.mjs';
const domains=['identity','learning','work','resources','relationships','family','home','community','body','daily_rhythm','meaning','creativity','mobility','caregiving','later_life','legacy','life_changes','digital_life'];
export function lifetimeMap(input){
 const {birth_date,as_of,leap_policy='feb28',events=[],plans=[],cycle_years=3}=input;
 ensure(Array.isArray(events)&&events.length<=300,'TOO_MANY_EVENTS','Tối đa 300 sự kiện trong demo.');ensure(Array.isArray(plans)&&plans.length<=100,'TOO_MANY_PLANS','Tối đa 100 kế hoạch trong demo.');
 ensure(Number.isInteger(cycle_years)&&cycle_years>=1&&cycle_years<=10,'INVALID_CYCLE_RANGE','Chu kỳ tham khảo từ 1 đến 10 năm.');
 const t=ageTimeline({birth_date,as_of,leap_policy,max_age:99}).calculation;const ids=new Set();
 const history=events.map(e=>{ensure(typeof e.id==='string'&&!ids.has(e.id),'DUPLICATE_EVENT','Sự kiện cần mã duy nhất.');ids.add(e.id);parseDate(e.date);ensure(e.date>=birth_date&&e.date<=as_of,'INVALID_HISTORY_DATE','Sự kiện lịch sử phải nằm từ ngày sinh đến ngày đối chiếu; không tự chuyển dự định thành quá khứ.');ensure(typeof e.title==='string'&&e.title.trim()&&e.title.length<=500,'INVALID_EVENT_TITLE','Sự kiện cần tiêu đề ngắn.');enumValue(e.domain,domains,'domain');return {...e,claim_type:'self_report'};});
 const intentions=plans.map(p=>{parseDate(p.target_date);ensure(p.target_date>=as_of,'PAST_PLAN','Kế hoạch mới không có hạn trước ngày đối chiếu.');ensure(typeof p.title==='string'&&p.title.trim()&&p.title.length<=500,'INVALID_PLAN','Cần nội dung kế hoạch.');enumValue(p.domain,domains,'domain');return {...p,claim_type:'user_intention',prediction:false};});
 for(const e of history){const interval=t.intervals.find(x=>e.date>=x.start&&e.date<x.end_exclusive);if(interval)interval.events.push(e.id);}
 const year=parseDate(as_of).year;ensure(year+cycle_years-1<=2500,'DATE_RANGE','Chu kỳ vượt miền ngày hỗ trợ.');
 const cycles=Array.from({length:cycle_years},(_,i)=>({year:year+i,personal_year:personalCycle({birth_date,year:year+i}).calculation.personal_year,claim_type:'symbolic_interpretation',events_predicted:[]}));
 return result('LCV3-LIFETIME','3.0',input,{age_interval:'[birthday,next_birthday)',leap_policy,cycle_boundary:'calendar',max_age:99}, {age_at_as_of:t.age_at_as_of,age_intervals:t.intervals,history,plans:intentions,symbolic_cycles:cycles,probabilistic_forecasts:[],domains,age_limit_meaning:'navigation_not_life_expectancy'},[],['100 khoảng tuổi chỉ là công cụ tổ chức lịch; không khẳng định tuổi thọ.','Không điền sự kiện vào những năm người dùng chưa kể.','Mọi chu kỳ biểu tượng tách riêng lịch sử và dự định.']);
}
