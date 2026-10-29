"""Build reviewable governance data for the planning package, never production."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / 'docs/upgrade/2026-10-20'
ORIGINAL = ROOT / 'docs/upgrade/sources/2026-10-11/package'

def write(relative, data):
    path = P / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

def csv_write(relative, rows):
    fields = list(dict.fromkeys(k for r in rows for k in r))
    with (P / relative).open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v for k,v in r.items()})

def main():
    gates = [
        ('RG0','Source and baseline',['G01'],'Tech Lead','Path/remote/branch/full SHA/clean-tree; artifact digest; exact environment'),
        ('RG1','Governance product and business',['G04','G06','G12'],'Founder + Product + Legal','Charter; requirement acceptance; Q decisions; rights; scope/budget/service entity'),
        ('RG2','Architecture design and brand',['G01','G06','G08'],'Architect + UX + Founder','Approved ADRs; data flow; accessibility; brand and public claim review'),
        ('RG3','AI system',['G06','G08'],'AI Lead + Method Lead + Security','Model/prompt/source versions; evals; ACL retrieval; costs; kill switch; human escalation'),
        ('RG4','Infrastructure and environments',['G01','G10'],'Platform + SRE','Resource/account/region/bindings; isolation; secrets controls; backup; cost caps'),
        ('RG5','Development and DevOps',['G01','G11'],'Tech Lead + QA','Protected branch; required checks; pinned build; artifact allowlist; no dirty deploy'),
        ('RG6','Documentation',['G04','G06','G12'],'Product + Docs Owner','Authority/supersession; runbooks; API/schema; user/support docs; read coverage'),
        ('RG7','Implementation data integration',['G02','G03','G05','G06','G07','G09'],'Backend + Data + QA','Object/tenant grants; method golden cases; migrations/reconciliation; payment and deletion'),
        ('RG8','Verification and security',['G02','G03','G08','G11'],'Independent QA + Security','Unit/property/contract/browser/e2e; negative auth; pentest/retest; counts and skips'),
        ('RG9','Staging and rehearsal',['G01','G07','G09','G10'],'Release Lead + SRE','Staging RC; auth/payment sandbox; load; restore/rollback; immutable rehearsal receipt'),
        ('RG10','Production authorization',['G01','G04','G12'],'Founder + Release Authority','Exact RC and scope; functional approvals; authorized operator/change window'),
        ('RG11','Post deploy verification',['G01','G02','G03','G10'],'SRE + QA','Provider deployment IDs map digest; domain routes; allowlisted smoke and failure paths'),
        ('RG12','Cleanup and handoff',['G05','G07','G12'],'SRE + Support + Privacy','Temporary access removed; legacy disposition; support/escalation; cost/monitor/DR ownership'),
        ('RG13','Founder domain sign off',['G01','G04','G12'],'Founder','Domain + exact release/capabilities + environment receipt + explicit decision'),
    ]
    mapping = [{'fpos_gate_id':i,'title':t,'custom_gate_ids':c,'owner_role':o,'evidence_required':e,
                'status':'NOT_CHECKED','receipt_ref':None,'applicability':'Scope must be decided before RC; no automatic N/A'}
               for i,t,c,o,e in gates]
    write('07_Bao_mat_Van_hanh/FPOS_GATE_MAPPING.json', mapping)
    text = '# Life Code OS Ánh xạ cổng phát hành FPOS\n\nNgày 20/10/2026. Giữ G01–G12 để truy vết; RG0–RG13 là gate workspace có authority. Mỗi dòng cần receipt riêng, mapping không đóng gate.\n\n'
    text += '| FPOS | Gate cũ | Chủ trì dự kiến | Evidence bắt buộc |\n|---|---|---|---|\n'
    text += '\n'.join(f"| {r['fpos_gate_id']} {r['title']} | {', '.join(r['custom_gate_ids'])} | {r['owner_role']} | {r['evidence_required']} |" for r in mapping)
    text += '\n\nRelease hiện HOLD. Tất cả gate production trong bảng là NOT_CHECKED. Applicability hoặc waiver phải nêu scope, lý do, rủi ro, người duyệt và thời hạn; không kế thừa một approved gate sang capability mới.\n'
    (P / '07_Bao_mat_Van_hanh/FPOS_GATE_MAPPING.md').write_text(text)
    services = [
        ('SVC-PUBLIC','Public web','Frontend','Static allowlisted assets','Synthetic pages; no private cache'),
        ('SVC-APP','User web and BFF','Frontend + Backend','Session and user-scoped API','A/B browser and denied routes'),
        ('SVC-IDENTITY','Identity and sessions','Security + Backend','Managed OIDC/session adapter','Issuer/audience/expiry/revoke/recovery/CSRF'),
        ('SVC-METHOD','Method core','Method Lead + Backend','Pure versioned computation','Golden vectors and missing-input outputs'),
        ('SVC-DB','PostgreSQL proposal','Data + SRE','Versioned domain store','RLS role/pool/transaction tests; restore'),
        ('SVC-JOBS','Outbox and job worker','Backend + SRE','Durable state transitions','Duplicate/reorder/replay/revoke/idempotency'),
        ('SVC-REPORT','Private objects and rendering','Backend + SRE','Immutable content snapshot with revocable access','SSRF/quota/download/revoke/export parity'),
        ('SVC-AI','AI gateway','AI Lead + Security','Scoped retrieval and generation','Injection/ACL/budget/degrade tests'),
        ('SVC-OPS','Observability and support','SRE + Support','Metrics and minimal redacted logs','Alert routing/incident/DR/support drill'),
    ]
    write('07_Bao_mat_Van_hanh/SERVICE_CATALOG.json', [
        {'service_id':i,'name':n,'owner_role':o,'named_owner':None,'backup_owner':None,'responsibility':r,
         'acceptance':a,'provider':None,'region':None,'environment_inventory_ref':None,
         'status':'NOT_CHECKED','design_status':'PROPOSED','launch_blocker_if_missing_owner':True}
        for i,n,o,r,a in services])
    write('07_Bao_mat_Van_hanh/OPERATIONS_ACCEPTANCE.json', {
        'version':'2026-10-20.r2','design_status':'PROPOSED','measured':False,
        'objectives':[
            {'id':'SLO-AVAIL','target':0.995,'window':'rolling_30_days','numerator':'successful_eligible_requests','denominator':'all_eligible_requests','empty_population':'UNAVAILABLE','include_failures':['timeout','5xx','resource_overload_429','eligible_provider_failure'],'owner':'SRE'},
            {'id':'SLO-API','target_p95_ms':800,'scope':'eligible ordinary API end-to-end; separate generation','required_dimensions':['sample_count','region','route_mix','cache','cold_start','payload_bytes'],'owner':'Backend + SRE'},
            {'id':'SLO-L1-REPORT','target_fraction':0.95,'threshold_seconds':300,'start':'job accepted','end':'artifact available','failed_jobs_count_against_target':True,'owner':'Report Lead'},
            {'id':'DR-RPO','maximum_seconds':3600,'scope':'business data actual restored recovery point','owner':'Data + SRE'},
            {'id':'DR-RTO','maximum_seconds':14400,'scope':'safe service including deletion/revocation replay','owner':'SRE'},
        ],
        'alerts':[
            {'id':'ALT-AUTH','trigger':'one confirmed cross-owner/tenant/private cache failure','severity':'P0','owner':'Incident Commander + Security + Privacy','action':'contain surface and preserve minimum evidence'},
            {'id':'ALT-BURN-FAST','trigger':'burn >14.4 in 5m AND 1h; >=20 eligible each','severity':'P1','owner':'SRE','action':'check deploy/provider/latency and reduce impact'},
            {'id':'ALT-BURN-SLOW','trigger':'burn >6 in 30m AND 6h; >=20 eligible each','severity':'P2','owner':'SRE','action':'ticket and capacity/error-budget review'},
            {'id':'ALT-QUEUE','trigger':'oldest age >60sec for 5min OR DLQ age >10min','severity':'P1','owner':'Backend + SRE','action':'stop unsafe replay; inspect redacted job state'},
            {'id':'ALT-POOL','trigger':'DB pool saturation >80% for 10min','severity':'P2','owner':'Data + SRE','action':'inspect scoped connections and backpressure'},
            {'id':'ALT-BUDGET','trigger':'50/75/90/100 percent of approved cap','severity':'P2','owner':'Finance + AI Lead','action':'degrade optional AI at cap; preserve data rights'},
        ],
        'load_profiles':{'concurrency':[1,10,50],'ramp_minutes':5,'steady_minutes':15,'recovery_minutes':5,'data':'synthetic_only','cost_permission':'bounded staging scope required'},
        'drills':['pre-pilot restore','before major migration','after backup/key/provider change','quarterly restore proposal','revocation during render','DLQ after subject deletion','provider outage degradation','rollback without revoked method'],
        'evidence_status':'NOT_CHECKED','receipt_ref':None,
    })
    legal = [
        ('LEGAL-SERVICE','All service','Legal entity/controller/processor/merchant and scope','Founder + Legal','Q14','Service charter + entity and duties memo'),
        ('LEGAL-DATA','Intake and profiling','Purpose/lawful basis/data flow/retention/vendor transfer by activity','Privacy + Legal','Q9;Q14;Q15','Activity processing register + notice + impact/filing assessment'),
        ('LEGAL-AI','AI use','Classify each function and role under applicable AI rules','AI Lead + Legal','Q16','Function inventory + classification + controls + policy versions'),
        ('LEGAL-COMMERCE','Paid reports/subscriptions','Merchant/platform role/refund/consumer/tax/invoice and current ecommerce rules','Commerce + Legal','Q14;Q15;Q20','Sandbox flow + terms/refund + applicability memo'),
        ('LEGAL-METHOD','Source and formula release','Edition/source/license/translation/commercial redistribution permissions','Method Lead + Rights','Q3;Q12','One source-rights receipt per release'),
        ('LEGAL-SENSITIVE','Children/health/biometrics','Separate legal and professional review plus data minimization','Privacy + Legal + qualified specialist','Q8;Q18','Explicit additional scope approval; default feature disabled'),
        ('LEGAL-INTERNATIONAL','Country rollout and franchise','Country-specific contracts/privacy/trademark/disclosure/support','Legal + Partnerships','Q19','Country pack signed for exact offering/territory'),
        ('LEGAL-INCIDENT','Suspected/confirmed incident','Assess facts, obligations and time limits for actual jurisdiction','Incident Commander + Legal','Q9','Incident decision log + notifications assessment'),
    ]
    write('07_Bao_mat_Van_hanh/LEGAL_ACTIVITY_MATRIX.json',[
        {'activity_id':i,'activity':a,'question':q,'owner_role':o,'decision_dependencies':d.split(';'),'acceptance_artifact':e,'status':'BLOCKED','blocker':'Applicable review and named authority receipt not supplied','approval_ref':None}
        for i,a,q,o,d,e in legal])
    rows = json.loads((ORIGINAL / '09_Doi_chieu_Bang_chung/EVIDENCE_LEDGER.json').read_text())
    for row in rows:
        row['original_status'] = row['status']
        row['status'] = 'REPORTED_UNVERIFIED'
        row['review_note'] = 'Historical 11/10 observation preserved; do not treat as re-run production evidence'
    rows.extend([
        {'id':'EV20','surface':'package_ingestion','observation':'149 files ZIP/folder byte parity and 148 original manifest digests','status':'VERIFIED_WORKTREE_ONLY','source_ids':'SOURCE_RECEIPT.json','limitation':'Integrity only; no release approval','checked_date':'2026-10-20'},
        {'id':'EV21','surface':'source_identity','observation':'remote main99b4027 and plan336ef35a matched; isolated codex branch from plan','status':'VERIFIED_CURRENT','source_ids':'git ls-remote + local Git','limitation':'Remote/source only, not deployed SHA','checked_date':'2026-10-20'},
        {'id':'EV22','surface':'production_release','observation':'Provider deployment mapping, staging and Founder RC approval missing','status':'BLOCKED','source_ids':'baseline receipt','limitation':'All production gates remain unclosed','checked_date':'2026-10-20'},
    ])
    write('09_Doi_chieu_Bang_chung/EVIDENCE_LEDGER.json', rows)
    csv_write('09_Doi_chieu_Bang_chung/EVIDENCE_LEDGER.csv', rows)
    baseline = json.loads((ORIGINAL / '09_Doi_chieu_Bang_chung/BASELINE_LOCK.json').read_text())
    baseline.update({'document_baseline':'2026-10-20.r2','planning_branch':'codex/complete-upgrade-plan-2026-10-20',
                     'repo_root':str(ROOT),'canonical_remote':'git@github.com:tranhatam-collab/Life-Code-OS.git',
                     'source_receipt':'../sources/2026-10-11/SOURCE_RECEIPT.json','runtime_status':'BLOCKED',
                     'release_verdict':'HOLD','local_planning_update_authorized':True,
                     'source_identity_checked_at':'2026-10-20','working_tree':'planning changes; not committed',
                     'source_zip_sha256':'55ec5c5234d4a046e5f47d845066117d477f78730bfc94f63a85c454d6cd8ff3'})
    write('09_Doi_chieu_Bang_chung/BASELINE_LOCK.json', baseline)
    for rel,extra in {
        '07_Bao_mat_Van_hanh/01_P0_CONTAINMENT.md':'P0 được tách thành containment code, negative tests, rollout receipt và incident/data review. Auth source đã xác nhận thiếu owner checks tại baseline; chưa có runtime exploit hoặc breach receipt. Xem SECURITY_AND_PRIVACY_ACCEPTANCE.md.',
        '07_Bao_mat_Van_hanh/02_PRIVACY_AND_DELETION.md':'Áp dụng activity-level legal matrix và data-system inventory; test deletion gồm jobs đang chạy, DLQ, provider, cache và restore. Mọi retention chưa được ký vẫn là proposal. Xem SECURITY_AND_PRIVACY_ACCEPTANCE.md.',
        '07_Bao_mat_Van_hanh/03_SECURITY_THREAT_MODEL.md':'Bổ sung pool reuse/failed transaction, field redaction, service worker cache, renderer isolation và metadata enumeration vào test scope. Source/model/document content không cấp quyền tool. Xem SECURITY_AND_PRIVACY_ACCEPTANCE.md.',
        '07_Bao_mat_Van_hanh/04_OPERATIONS_SRE_AND_COST.md':'SLI denominator, alert thresholds, service ownership, DR drill, capacity profiles và budget actions được đặc tả trong OPERATIONS_ACCEPTANCE_RUNBOOK.md và OPERATIONS_ACCEPTANCE.json; chưa là số đo hiện tại.',
        '07_Bao_mat_Van_hanh/05_VIETNAM_LEGAL_READINESS.md':'Metadata chính thức về Luật AI134/2025, NĐ142/2026, Luật TMĐT122/2025, NĐ248/2026 và Luật91/2025 đã được đọc lại20/10. Không đồng nhất metadata với full-text applicability. LEGAL_ACTIVITY_MATRIX.json khóa từng hoạt động và owner; RESEARCH_UPDATE_2026-10-20.json ghi phạm vi đã đọc.',
        '07_Bao_mat_Van_hanh/06_RELEASE_GATES.md':'G01–G12 là nhóm gate sản phẩm. FPOS_GATE_MAPPING.json ánh xạ đầy đủ RG0–RG13 và là bảng dùng khi review RC. Verdict hiện HOLD; BLOCKED là evidence/gate state. Các nhãn pass cũ không chuyển thành VERIFIED_CURRENT.',
        '07_Bao_mat_Van_hanh/CI_RELEASE_POLICY.md':'Bộ kế hoạch đang được đưa vào repo chứa build script denylist cũ. Trước deploy, DEV phải thực hiện public artifact allowlist và test không lộ ZIP/docs/SQL/fixtures; không chạy production workflow chỉ để kiểm tra tài liệu.',
        '07_Bao_mat_Van_hanh/P0_PACKET/00_SCOPE_AND_AUTHORITY.md':'Yêu cầu mới20/10 cho phép nâng cấp, copy và kiểm thử bộ kế hoạch cục bộ. Runbook bên trong gói vẫn không tự cấp authority cho thao tác production.',
        '07_Bao_mat_Van_hanh/P0_PACKET/05_DEPLOYMENT_AND_ROLLBACK.md':'Evidence label chuẩn là BLOCKED khi thiếu receipt, kèm reason_code DEPLOYMENT_RECEIPT_MISSING. Không dùng BLOCKED_RECEIPT như claim status. Trình tự drill và SLI nằm trong OPERATIONS_ACCEPTANCE_RUNBOOK.md.',
        '07_Bao_mat_Van_hanh/P0_PACKET/06_LEGACY_AND_INCIDENT_TRIAGE.md':'Thêm reconciliation bucket cho source không đủ quyền và account/subject ambiguous. Mỗi row rejected có reason và owner xử lý trong kho riêng tư; raw legacy output không chuyển thành observed fact.',
        '09_Doi_chieu_Bang_chung/01_CURRENT_STATE_AUDIT.md':'Những câu mô tả không truy cập Mac/tool lỗi ở trên là ghi nhận lịch sử11/10. Ngày20/10 đã xác minh repo mới trong Life-Code-OS, remote main/plan, bảo toàn checkout phase dirty và nhập đủ149 tệp. Label cũ được normalize trong EVIDENCE_LEDGER; deployment và approval vẫn BLOCKED. Xem BASELINE_LOCK.json.',
    }.items():
        original = (ORIGINAL / rel).read_text()
        (P / rel).write_text(original + '\n\n## Bổ sung ngày 20 tháng 10 năm 2026\n\n' + extra + '\n')
    p0 = json.loads((ORIGINAL / '07_Bao_mat_Van_hanh/P0_PACKET/01_EVIDENCE_BASELINE.json').read_text())
    p0.update({'status':'REPORTED_UNVERIFIED','scope':'Historical source observations with current vocabulary; not P0 completion','evidence':rows,'revision':'2026-10-20.r2'})
    write('07_Bao_mat_Van_hanh/P0_PACKET/01_EVIDENCE_BASELINE.json',p0)
    review = json.loads((ORIGINAL / '07_Bao_mat_Van_hanh/P0_PACKET/07_EXIT_REVIEW.json').read_text())
    review.update({'decision':'HOLD','reason':'P0 implementation/deployment/independent acceptance receipts missing','revision':'2026-10-20.r2','fpos_mapping':'../FPOS_GATE_MAPPING.json'})
    write('07_Bao_mat_Van_hanh/P0_PACKET/07_EXIT_REVIEW.json',review)
    surfaces = list(csv.DictReader((ORIGINAL / '07_Bao_mat_Van_hanh/P0_PACKET/02_SURFACE_INVENTORY.csv').open(encoding='utf-8-sig')))
    for r in surfaces:
        r['original_status']=r['status']; r['status']='NOT_CHECKED'; r['last_observation_date']='2026-10-11'
        r['scope_note']='Inventory candidate; current provider/runtime check required before change'
    csv_write('07_Bao_mat_Van_hanh/P0_PACKET/02_SURFACE_INVENTORY.csv',surfaces)
    research = [
        ('R20-01','Vietnam AI Law134/2025','https://vanban.chinhphu.vn/?docid=216334&orggroupid=1&pageid=27160','Metadata; effective2026-03-01','Metadata verified; full applicability not reviewed'),
        ('R20-02','Vietnam Decree142/2026','https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-142-2026-nd-cp-469480/64703.htm','Metadata; effective2026-05-01','97-page document linked; full text not read in this research pass'),
        ('R20-03','Vietnam Ecommerce Law122/2025','https://congbao.chinhphu.vn/van-ban-dang-cong-bao/luat-l13/trang-6.htm','Gazette metadata; effective2026-07-01','Counsel must retrieve signed text and transition rules'),
        ('R20-04','Vietnam Decree248/2026','https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-248-2026-nd-cp-469983.htm','Metadata; effective2026-07-01','93-page document linked; full applicability not reviewed'),
        ('R20-05','Vietnam Personal Data Law91/2025','https://vanban.chinhphu.vn/?docid=214590&pageid=27160','Metadata; effective2026-01-01','No compliance conclusion from metadata'),
        ('R20-06','EU AI Act Commission guidance','https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai','Risk-based application overview','Recheck consolidated law, amendments and timetable per country launch'),
        ('R20-07','PostgreSQL18 Row Security','https://www.postgresql.org/docs/18/ddl-rowsecurity.html','Technical RLS behavior and bypass roles','Does not verify project DB, provider or SQL execution'),
        ('R20-08','Cloudflare Queues delivery','https://developers.cloudflare.com/queues/reference/delivery-guarantees/','At-least-once delivery design basis','No account provisioning or runtime receipt'),
    ]
    write('09_Doi_chieu_Bang_chung/RESEARCH_UPDATE_2026-10-20.json',[
        {'id':i,'title':t,'url':u,'access_date':'2026-10-20','scope_read':s,'limitation':l,'status':'VERIFIED_CURRENT','type':'primary_source_metadata_or_technical_document','project_design_approval':False}
        for i,t,u,s,l in research])
    print('Governance registries built: 14 FPOS gates,9 services,8 legal activities,8 current research receipts.')

if __name__ == '__main__':
    main()
