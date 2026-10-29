import {execute as legacyExecute,METHODS as legacyMethods} from '../legacy_v2/src/engine.mjs';
import {ensure,record} from '../legacy_v2/src/errors.mjs';
import {fullNumerology,nameVariantComparison} from './numerology_full.mjs';
import {psychomatrix} from './psychomatrix.mjs';
import {batCuc,compareNumbers} from './bat_cuc.mjs';
import {lifetimeMap} from './lifetime.mjs';
import {allInOne} from './all_in_one.mjs';
export const NEW_METHODS={numerology_full:fullNumerology,name_compare:nameVariantComparison,psychomatrix,bat_cuc:batCuc,number_compare:compareNumbers,lifetime:lifetimeMap,all_in_one:allInOne};
export const METHOD_NAMES=[...Object.keys(legacyMethods),...Object.keys(NEW_METHODS)];
export function execute(method,input){record(input);ensure(JSON.stringify(input).length<=60000,'INPUT_TOO_LARGE','Dữ liệu demo tối đa 60.000 ký tự.');return NEW_METHODS[method]?NEW_METHODS[method](input):legacyExecute(method,input);}
