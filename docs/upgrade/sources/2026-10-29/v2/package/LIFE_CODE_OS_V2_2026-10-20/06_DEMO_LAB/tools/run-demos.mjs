import {readFileSync,writeFileSync} from 'node:fs';
import {execute} from '../src/engine.mjs';
const cases=JSON.parse(readFileSync(new URL('../data/demo-cases.json',import.meta.url),'utf8'));
const receipts=cases.map(c=>{try{return {id:c.id,method:c.method,synthetic:true,result:execute(c.method,c.input),error:null};}catch(e){return {id:c.id,method:c.method,synthetic:true,result:null,error:{code:e.code??'INTERNAL',message:e.message}};}});
writeFileSync(new URL('../receipts/demo-results.json',import.meta.url),JSON.stringify({generated_at:new Date().toISOString(),node:process.versions.node,icu:process.versions.icu,tzdb:process.versions.tz,case_count:cases.length,production_calls:0,receipts},null,2));
console.log(`Đã tạo ${receipts.length} kết quả demo. Không gọi API production.`);
