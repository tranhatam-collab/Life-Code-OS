import http from 'node:http';
import {readFileSync} from 'node:fs';
import {randomUUID} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {execute} from './src/engine.mjs';
const demos=JSON.parse(readFileSync(new URL('./data/demo-cases.json',import.meta.url),'utf8'));
const files=new Map([['/',['index.html','text/html; charset=utf-8']],['/index.html',['index.html','text/html; charset=utf-8']],['/app.js',['app.js','text/javascript; charset=utf-8']],['/style.css',['style.css','text/css; charset=utf-8']]]);
export function createDemoServer(){return http.createServer(async(req,res)=>{
 const id=randomUUID();const send=(status,data,type='application/json; charset=utf-8')=>{res.writeHead(status,{'Content-Type':type,'Cache-Control':'no-store','X-Content-Type-Options':'nosniff','Referrer-Policy':'no-referrer','Content-Security-Policy':"default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'; form-action 'self'",'X-Request-ID':id});res.end(typeof data==='string'?data:JSON.stringify(data));};
 const allowedHosts=['localhost','127.0.0.1'];let base;try{base=new URL('http://'+req.headers.host);if(!allowedHosts.includes(base.hostname))return send(403,{code:'LOCAL_HOST_ONLY'});}catch{return send(400,{code:'INVALID_HOST'});}
 const url=new URL(req.url,base);if(req.headers.origin&&req.headers.origin!==base.origin)return send(403,{code:'ORIGIN_DENIED'});
 if(req.method==='GET'&&files.has(url.pathname)){const [name,mime]=files.get(url.pathname);return send(200,readFileSync(new URL('./public/'+name,import.meta.url),'utf8'),mime);}
 if(req.method==='GET'&&url.pathname==='/api/demo/catalog')return send(200,{mode:'LOCAL_SYNTHETIC_DEMO',production_ready:false,cases:demos});
 if(req.method==='GET'&&url.pathname==='/health')return send(200,{ok:true,service:'lifecode-reference-lab',mode:'local_only',production_ready:false});
 if(req.method==='POST'&&url.pathname==='/api/demo/run'){
  if(!(req.headers['content-type']??'').startsWith('application/json'))return send(415,{code:'JSON_REQUIRED'});
  let chunks=[],bytes=0,tooLarge=false;try{for await(const buf of req){bytes+=buf.length;if(bytes>65536){tooLarge=true;break;}chunks.push(buf);}if(tooLarge)return send(413,{code:'BODY_LIMIT'});
   const payload=JSON.parse(Buffer.concat(chunks).toString('utf8'));const started=performance.now();const value=execute(payload.method,payload.input);return send(200,{request_id:id,mode:'LOCAL_SYNTHETIC_DEMO',duration_ms:Number((performance.now()-started).toFixed(3)),data:value});
  }catch(e){return send(e.status??(e instanceof SyntaxError?400:422),{type:'urn:lifecode:problem:invalid-demo-request',title:'Không thể thực hiện với đầu vào này',status:e.status??(e instanceof SyntaxError?400:422),code:e.code??'INVALID_REQUEST',detail:e.message,instance:id},'application/problem+json');}
 }
 return send(404,{code:'NOT_FOUND'});
});}
if(process.argv[1]===fileURLToPath(import.meta.url)){const port=Number(process.env.PORT??8788);if(!Number.isInteger(port)||port<1024||port>65535)throw Error('PORT cần nằm trong 1024–65535.');createDemoServer().listen(port,'127.0.0.1',()=>console.log(`Life Code Reference Lab: http://127.0.0.1:${port}\nChỉ dữ liệu giả; không đăng nhập, không thanh toán, không gọi production.`));}
