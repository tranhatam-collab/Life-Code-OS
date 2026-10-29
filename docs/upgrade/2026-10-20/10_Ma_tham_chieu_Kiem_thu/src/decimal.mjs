/** Exact rational-to-decimal demonstrator. Not a financial or production engine. */
function asInteger(value, label) {
  if (typeof value==='bigint') return value;
  if (Number.isSafeInteger(value)) return BigInt(value);
  throw new TypeError(label+' phải là bigint hoặc số nguyên an toàn.');
}

function renderFixed(units, scale, negative) {
  let digits=units.toString();
  if (scale===0) return (negative&&units!==0n?'-':'')+digits;
  digits=digits.padStart(scale+1,'0');
  const split=digits.length-scale;
  return (negative&&units!==0n?'-':'')+digits.slice(0,split)+'.'+digits.slice(split);
}

export function ratioDecimal(numerator,denominator,{scale=6,rounding='half_even'}={}) {
  const n=asInteger(numerator,'Tử số'),d=asInteger(denominator,'Mẫu số');
  if (!Number.isInteger(scale)||scale<0||scale>12) throw new RangeError('Scale phải trong miền 0–12.');
  if (!['half_even','half_up','floor','ceiling','truncate'].includes(rounding)) throw new TypeError('Rounding mode chưa hỗ trợ.');
  if (d===0n) return {value:null,scale,rounding,missing_reason:'division_by_zero'};
  const negative=(n<0n)!==(d<0n),a=n<0n?-n:n,b=d<0n?-d:d,factor=10n**BigInt(scale);
  let units=(a*factor)/b;
  const remainder=(a*factor)%b;
  let increment=false;
  if (rounding==='half_up') increment=remainder*2n>=b;
  if (rounding==='half_even') increment=remainder*2n>b||(remainder*2n===b&&units%2n===1n);
  if (rounding==='floor') increment=negative&&remainder!==0n;
  if (rounding==='ceiling') increment=!negative&&remainder!==0n;
  if (increment) units+=1n;
  return {value:renderFixed(units,scale,negative),scale,rounding,missing_reason:null};
}

