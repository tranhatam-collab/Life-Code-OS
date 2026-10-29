"""Optional GET-only allowlist collector; disabled unless --run explicitly passed.
No auth tokens, profiles, report IDs or production mutations. Network failures are NOT outages.
"""
import argparse,datetime,hashlib,json,urllib.request
from pathlib import Path
URLS=['https://lifecode.iai.one/','https://lifecode.iai.one/chinh-sach-bao-mat','https://life-code-api.tranhatam.workers.dev/health']
p=argparse.ArgumentParser();p.add_argument('--run',action='store_true');p.add_argument('--output',default='public_evidence.json');a=p.parse_args()
if not a.run:raise SystemExit('Chưa chạy. Cần --run với phạm vi GET công khai được cho phép.')
rows=[]
for url in URLS:
 item={'url':url,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'LifeCode-readonly-evidence/0.1'})
  with urllib.request.urlopen(req,timeout=15) as res:
   body=res.read(2_000_001)
   if len(body)>2_000_000:raise ValueError('response_too_large')
   item.update(status=res.status,final_url=res.url,sha256=hashlib.sha256(body).hexdigest(),content_type=res.headers.get('Content-Type'),evidence_type='READ_ONLY_GET')
 except Exception as e:item.update(status=None,error_type=type(e).__name__,evidence_type='PROBE_BLOCKED_OR_FAILED_NOT_OUTAGE_PROOF')
 rows.append(item)
Path(a.output).write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
