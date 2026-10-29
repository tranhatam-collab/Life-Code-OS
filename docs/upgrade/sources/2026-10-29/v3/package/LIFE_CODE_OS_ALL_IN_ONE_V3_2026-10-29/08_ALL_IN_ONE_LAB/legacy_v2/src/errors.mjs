export class DomainError extends Error {
  constructor(code, message, status=422, detail={}) { super(message); this.name='DomainError'; this.code=code; this.status=status; this.detail=detail; }
}
export function ensure(ok, code, message, detail={}) { if(!ok) throw new DomainError(code,message,422,detail); }
export function integer(value, min, max, name) { ensure(Number.isSafeInteger(value)&&value>=min&&value<=max,'INVALID_INTEGER',`${name}: yêu cầu số nguyên từ ${min} đến ${max}.`);return value; }
export function record(value, name='input') {ensure(value!==null&&typeof value==='object'&&!Array.isArray(value),'INVALID_OBJECT',`${name} phải là một đối tượng.`);return value;}
export function enumValue(value, allowed, name) {ensure(allowed.includes(value),'UNSUPPORTED_POLICY',`${name} chưa được hỗ trợ.`,{allowed});return value;}
