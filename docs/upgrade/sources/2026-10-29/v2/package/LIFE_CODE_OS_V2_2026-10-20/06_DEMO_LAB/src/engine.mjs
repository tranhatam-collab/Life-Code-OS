import {readFileSync} from 'node:fs';
import {record,ensure} from './errors.mjs';
import {tail80,pairAnalysis,digitMatrix,sequenceFeatures,normalizePhone} from './numbers.mjs';
import {nameNumbers} from './names.mjs';
import {ageTimeline,birthNumbers,personalCycle,localTimeCandidates,compareHypotheses} from './time.mjs';
import {inputCoverage,goalProgress,cashflow,resonanceSummary,preferenceMatrix} from './metrics.mjs';
import {hexagramTransform,blockedMethod} from './symbolic.mjs';
import {authorize,validateClaim,transition,optimisticUpdate} from './policy.mjs';
import {assembleReport} from './report.mjs';
import {profilePipeline} from './pipeline.mjs';
import {planDag,impactClosure,buildCacheKey} from './dag.mjs';
export const TABLE=JSON.parse(readFileSync(new URL('../data/tail80_table.json',import.meta.url),'utf8'));
export const METHODS=Object.freeze({tail80:i=>tail80(i,TABLE),pairs:pairAnalysis,digit_matrix:digitMatrix,sequence:sequenceFeatures,name:nameNumbers,birth:birthNumbers,cycle:personalCycle,timeline:ageTimeline,time:localTimeCandidates,hypotheses:compareHypotheses,coverage:inputCoverage,actions:goalProgress,cashflow,resonance:resonanceSummary,preference:preferenceMatrix,hexagram:hexagramTransform,blocked:blockedMethod,phone:i=>normalizePhone(i.raw),authorization:authorize,claim:i=>validateClaim(i.claim,i.registry??{}),transition:i=>transition(i.kind,i.current,i.event),optimistic:i=>optimisticUpdate(i.expected,i.current,i.patch),report:assembleReport,profile_pipeline:profilePipeline,dag:planDag,impact:impactClosure,cache_key:buildCacheKey});
export function execute(method,input){record(input);ensure(Object.hasOwn(METHODS,method),'UNKNOWN_METHOD','Phương pháp không nằm trong danh sách demo.');const json=JSON.stringify(input);ensure(json.length<=60000,'INPUT_TOO_LARGE','Gói dữ liệu quá lớn.');return METHODS[method](input);}
