import {performance} from 'node:perf_hooks';
import {writeFileSync} from 'node:fs';
import os from 'node:os';
import {execute} from '../src/engine.mjs';
const cases=[['tail80',{suffix:'6789'}],['pairs',{digits:'0900000001'}],['name',{name:'Demo An'}],['birth',{birth_date:'1990-06-15'}],['timeline',{birth_date:'1990-06-15',as_of:'2026-10-20'}],['time',{date:'2026-10-25',time:'02:30',time_zone:'Europe/Berlin'}],['profile_pipeline',{subject_alias:'Hồ sơ tổng hợp A',profile:{full_name:'Demo An',birth_date:'1990-06-15',birth_time:'07:30',time_zone:'Asia/Ho_Chi_Minh'},goal:'Lập một kế hoạch',as_of:'2026-10-20'}]];
const rows=[];
for(const [method,input]of cases){for(let i=0;i<10;i++)execute(method,input);const n=['time','profile_pipeline'].includes(method)?50:250;const times=[];for(let i=0;i<n;i++){const t=performance.now();execute(method,input);times.push(performance.now()-t);}times.sort((a,b)=>a-b);rows.push({method,iterations:n,p50_ms:+times[Math.floor(n*.5)].toFixed(4),p95_ms:+times[Math.ceil(n*.95)-1].toFixed(4),max_ms:+times.at(-1).toFixed(4)});}
const receipt={generated_at:new Date().toISOString(),scope:'single_process_local_reference_no_network_no_db_no_ai',node:process.version,icu:process.versions.icu,tzdb:process.versions.tz,cpu_model:os.cpus()[0]?.model,platform:os.platform(),results:rows,limitations:['Không phải load test hoặc SLA production.','Không có dữ liệu thật, PostgreSQL, IdP, thanh toán, R2 hoặc mô hình AI.']};
writeFileSync(new URL('../receipts/benchmark.json',import.meta.url),JSON.stringify(receipt,null,2)+'\n');console.log(JSON.stringify(receipt,null,2));
