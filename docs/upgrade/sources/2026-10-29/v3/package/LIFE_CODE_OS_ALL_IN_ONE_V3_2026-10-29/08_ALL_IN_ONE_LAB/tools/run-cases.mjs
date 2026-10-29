import {readFileSync,writeFileSync} from 'node:fs';
import {execute} from '../src/router.mjs';
const cases=JSON.parse(readFileSync(new URL('../data/demo-cases-all.json',import.meta.url)));
const start=performance.now();const receipts=cases.map(c=>{try{return {id:c.id,origin:c.origin,method:c.method,synthetic:true,result:execute(c.method,c.input),error:null};}catch(e){return {id:c.id,origin:c.origin,method:c.method,synthetic:true,result:null,error:{code:e.code??'INTERNAL',message:e.message}};}});
writeFileSync(new URL('../receipts/demo-results-v3.json',import.meta.url),JSON.stringify({generated_at:new Date().toISOString(),node:process.versions.node,icu:process.versions.icu,tzdb:process.versions.tz,case_count:cases.length,duration_ms:Math.round(performance.now()-start),production_calls:0,receipts},null,2));
console.log(`${receipts.length} receipts created; external calls=0. These are reference calculations, not production readiness.`);
