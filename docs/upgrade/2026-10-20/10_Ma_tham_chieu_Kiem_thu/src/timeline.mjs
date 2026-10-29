/** Civil-date age intervals; never interprets date-only input through a timezone. */
function leap(year){return year%4===0&&(year%100!==0||year%400===0);}
function daysInMonth(year,month){return [31,leap(year)?29:28,31,30,31,30,31,31,30,31,30,31][month-1]??0;}
export function parseCivilDate(value){
  const match=typeof value==='string'&&/^(\d{4})-(\d{2})-(\d{2})$/.exec(value);
  if(!match) throw new TypeError('Ngày phải ở dạng YYYY-MM-DD.');
  const year=Number(match[1]),month=Number(match[2]),day=Number(match[3]);
  if(year<1||month<1||month>12||day<1||day>daysInMonth(year,month)) throw new RangeError('Ngày Gregorian không hợp lệ.');
  return {year,month,day};
}
function format({year,month,day}){return String(year).padStart(4,'0')+'-'+String(month).padStart(2,'0')+'-'+String(day).padStart(2,'0');}
export function anniversary(birthDate,age,{leapDayPolicy='feb28'}={}){
  const birth=parseCivilDate(birthDate);
  if(!Number.isInteger(age)||age<0||age>199) throw new RangeError('Tuổi phải là số nguyên 0–199.');
  if(!['feb28','mar01'].includes(leapDayPolicy)) throw new TypeError('Leap-day policy chưa hỗ trợ.');
  const year=birth.year+age;
  if(year>9999) throw new RangeError('Năm kết quả vượt miền bốn chữ số.');
  if(birth.month===2&&birth.day===29&&!leap(year)) return format({year,month:leapDayPolicy==='feb28'?2:3,day:leapDayPolicy==='feb28'?28:1});
  return format({year,month:birth.month,day:birth.day});
}
export function ageInterval(birthDate,age,options={}){
  return {age,start:anniversary(birthDate,age,options),end_exclusive:anniversary(birthDate,age+1,options),interval_notation:'[start,end)',content_kind:'civil_age_interval_not_forecast'};
}
export function ageTimeline(birthDate,{fromAge=0,toAge=99,leapDayPolicy='feb28'}={}){
  if(!Number.isInteger(fromAge)||!Number.isInteger(toAge)||fromAge<0||toAge<fromAge||toAge>198) throw new RangeError('Khoảng tuổi không hợp lệ.');
  return Array.from({length:toAge-fromAge+1},(_,i)=>ageInterval(birthDate,fromAge+i,{leapDayPolicy}));
}

