# Life Code OS — Kế hoạch điều hành DEV hợp nhất 29/10/2026

Phiên bản: 2026-10-29.r1. Phạm vi: nâng cấp tổng kế hoạch và chuẩn bị bàn giao DEV trong đúng repository Life-Code-OS. Đây là tài liệu đề xuất thực thi có điều kiện. Không có quyết định nào được tự ký, không có quyền production phát sinh từ gói đính kèm hoặc từ việc tạo tài liệu này.

## 1. Kết luận và cách sử dụng

Đã có đủ cấu trúc để giao việc chuẩn bị, đặc tả và kiểm thử synthetic theo từng work order. Trạng thái phát hành vẫn **HOLD**: chưa có receipt hiện hành chứng minh candidate sạch, nhà cung cấp, identity/quyền, staging, quyền nguồn từng phương pháp, phục hồi, pháp nhân/thương mại, cohort và người duyệt đúng phạm vi. Các gói V2/V3 là nguồn thiết kế và reference; chúng không chứng minh backend production đã có 99 operation, 62 phương pháp được phép phát hành hoặc 28 sản phẩm đang bán.

Dùng thứ tự sau: đọc đối chiếu nguồn → chọn scope/cohort → quyết định chức năng → work order → đặc tả và implementation trên candidate riêng → test và review độc lập → staging/recovery → biên bản pilot/release. Làm tài liệu và fixture synthetic có thể tiến hành trong khi các quyết định còn pending; hành vi phụ thuộc quyết định chỉ được dispatch khi có receipt đúng capability.

Tài liệu đi cùng:

- [Tổng kế hoạch](../MASTER_PLAN.md) và [điểm bắt đầu](../START_HERE.md).
- [Backlog316](BACKLOG_UNIFIED.json), [DAG có kiểu](TASK_DEPENDENCY_GRAPH.json), [trace hợp nhất](REQUIREMENT_TRACE_UNIFIED.json) và [DEV contracts](TASK_DEV_CONTRACTS.json).
- [20 work order tích hợp](INTEGRATION_WORK_ORDERS.json): nhiệm vụ có scope, vai trò, dependencies, acceptance, positive/negative tests, rollback, estimate proposal và evidence.
- [45 decision packets](DECISION_EXECUTION_PACKETS.json): giữ nguyên toàn bộ 20 packet local hiện có, bổ sung 25 packet Q21–Q45; tất cả chưa có approval mới.
- [Hợp đồng work order](WORK_ORDER_TEMPLATE.json): JSON Schema và quy tắc admission trước DEV.
- [Biên nhận đối chiếu program](../evidence/PROGRAM_RECONCILIATION.json) và [phạm vi đọc có SHA](../evidence/READ_COVERAGE_PROGRAM.json).
- Các bản V1/local20/10, V2, V3 được giữ nguyên trong vùng nguồn; mọi khác biệt có hiệu lực phải được giải thích trong overlay và conflict ledger.

## 2. Baseline, nguồn và thứ tự hiệu lực

Repository làm việc: `/Users/tranhatam/Library/Mobile Documents/com~apple~CloudDocs/Documents/Devnewproject/Life-Code-OS`. Remote ghi nhận lúc intake: `git@github.com:tranhatam-collab/Life-Code-OS.git`; branch `codex/complete-upgrade-plan-2026-10-20`; HEAD `336ef35a8386a744c6de18a7f7c6e268e89e6dac`. Đây là nhận dạng lúc intake, không thay thế việc kiểm lại trước khi dispatch DEV hoặc staging.

Worktree có thay đổi sẵn của người dùng. Giữ nguyên các thay đổi ấy; không reset, stash, commit, push, merge, chạy migration hoặc deploy. Việc cập nhật tài liệu mới trong `docs/upgrade/2026-10-29/` là phạm vi người dùng đã yêu cầu; không có bằng chứng supplied importer đã apply thành công vào worktree này.

Các lớp nguồn:

| Lớp | Nội dung | Cách dùng |
|---|---|---|
| V1 11/10 | 149 tệp gốc đã bảo toàn trong các baseline | Giữ lịch sử, nguồn yêu cầu và ý định sản phẩm |
| Local 20/10 | 216 tệp kế hoạch hiện có; 156 task, 20 packet, 87 trace, 14 FPOS mapping | Giữ mọi mở rộng UPG và sửa P0 đã làm |
| V2 ZIP | 307 tệp, gồm thư mục core304 và ba tệp rời đã bảo toàn | Thêm68 task refinement, Q21–Q30, reference backend/demo |
| V3 ZIP | 520 tệp; có baseline V2 và phần mới | Thêm72 task, Q31–Q45, 62 requirement V3, method/product/UI mở rộng |
| Overlay29/10 | Nội dung nối mới và biên bản đối chiếu | Canonical planning view; không viết lại byte nguồn |

Không dùng quy tắc “file mới hơn luôn thắng”. Khi cùng một ID có khác biệt:

1. Giữ source record và SHA của từng bản.
2. Giữ ID cũ; ghép provenance theo `package_id + source_path + source_sha256 + source_record_id`.
3. Giữ sửa chữa có bằng chứng của local20/10, đặc biệt dependency P0.
4. Đưa phần mới V2/V3 vào namespace hiện có; thay đổi semantic còn tranh chấp là pending decision.
5. Quyền phát hành phụ thuộc receipt Method/Privacy/Legal/QA/Release theo phạm vi; đề xuất trong tài liệu không tự có authority.

Đường đích canonical của lần này là `docs/upgrade/2026-10-29/` (singular). Đường `docs/upgrades/2026-10-29-v3/` trong importer đính kèm là đích của công cụ tham chiếu, không phải đích đã chạy. Không tự đổi source importer, không auto-run mã nguồn đính kèm. Các chỉ dẫn AGENTS cũ đã được người dùng thu hồi; giữ các bảng gate làm dữ liệu kiểm toán kế hoạch, không viện dẫn AGENTS đã thu hồi để tạo quyền hoặc bắt người dùng duyệt lại công việc tài liệu đã được yêu cầu.

## 3. Số lượng hợp nhất và chống bỏ sót

| Chỉ mục | Đối chiếu đúng |
|---|---|
| Task nguồn hiện có | 156 =140 V1 +16 UPG |
| Task V2 mới | 68 refinement |
| Task V3 mới | 72 =62 method +10 integration |
| Union nguồn | **296 ID duy nhất**, không collision giữa ba nhóm |
| Work order29/10 | 20 INT29-001…INT29-020; liên kết nguồn, không thay/xóa ID cũ |
| View điều hành | **316 ID** nếu đưa cả20 INT vào backlog; không có nghĩa316việc độc lập về effort |
| Decision | 45 =20 rich local giữ nguyên +10 V2 +15 V3 |
| Trace nguồn | 87local và62 V3 là hai tập nguồn cần crosswalk; không lấy phép cộng làm chứng minh coverage mọi task |
| Gate | G01–G12 giữ nguyên; RG0–RG13 giữ mapping14dòng, receipt riêng |
| Product/screen | 23 sản phẩm, 45 màn hình local được bảo toàn; đích V3 là28 sản phẩm, 69 màn hình |
| Method/API/demo | 62 adapter, 99 operation thiết kế, 167 demo V3 là các grain khác nhau |

V3 gọi backlog280 “unified”, nhưng tập này chỉ có140 V1 +68 V2 +72 V3, thiếu16UPG của local20/10. Phải đưa lại `UPG-AI-001…002`, `UPG-BE-001…007`, `UPG-PM-001…002`, `UPG-PRD-001…002`, `UPG-UX-001…003`. Không thay156local bằng280V3 một cách mù quáng.

87trace cũ phủ forward các23product, 45 screen và9 report level theo thiết kế cũ, nhưng chỉ trực tiếp nhắc69task khác nhau. Không được diễn đạt là156 task đều có trace riêng. Trace mới phải bổ sung backward view để phát hiện orphan task/claim/test, ghi rõ gap chứ không chế link cho đủ số.

## 4. Dependency và DAG đúng kiểu

Task dùng nguyên ID nguồn: `P0-xx`, cácworkstream V1, `UPG-*`, `V2-*`, `V3-MTH-*`, `V3-INT-*` và `INT29-*`. Không đổi tên chỉ để đồng bộ format.

Mỗi record tách:

- `task_dependencies`: công việc thực sự là predecessor trong DAG.
- `decision_dependencies`: Q1–Q45, phải có option/receipt tương ứng khi dispatch phần bị chặn.
- `gate_dependencies`: G01–G12 hoặc RG0–RG13, predicate có evidence cho scope.
- `parent_task_id/rollup`: quan hệ refinement/effort; không tự là completion edge.
- `raw_source_dependencies`: giữ nguyên bản nguồn và lý do overlay.
- `dependency_scope`: capability/cohort/candidate cụ thể; hoàn tất phần đang phát hành, không ép xong cả portfolio.

V3 gán62MTH cùng `Q31,Q32,G06` và10 INT cùng `Q31,G01`: tổng206non-task edges =134decision +72 gate. Nếu coi tất cả là task ID thì báo72task “missingdependency” sai nghĩa. Khi tách kiểu, source task graph296 có0unknown dependency và0cycle trong kiểm tra hiện tại. Điều này chỉ chứng minh tính toàn vẹn cấu trúc; chưa chứng minh sequencing hay effort đủ thực tế.

Giữ dependency P0 local đã sửa:

| Task | Dependency local được giữ | Incoming V3 lịch sử |
|---|---|---|
| P0-02 | P0-08 | P0-01 |
| P0-05 | P0-03 | P0-04 |
| P0-06 | P0-03 | P0-05 |
| P0-07 | P0-02 | P0-06 |
| P0-08 | P0-01 | P0-07 |
| P0-10 | P0-03; P0-04; P0-05; P0-06; P0-07; P0-09 | P0-09 |

Không thêm parent-complete → child và child-complete → parent đồng thời. Parent là summary node cho deliverable/acceptance và effort; work order chọn các leaf cần thiết. V2 serialize68task thành7chuỗi theo workstream; giữ raw graph để truy vết, nhưng proposal dispatch nên cho tên/Unicode, thời gian và arithmetic core chạy song song sau khi schema/input contract đủ. Mọi bỏ/đổi edge phải có lý do và review; không tự xóa dependency để làm DAG đẹp.

Decision mapping bổ sung cần theo đúng phương pháp: time/calendar→Q24; numerology→Q32/Q38; BátCực→Q33/Q34; đuôi80→Q35; Psychomatrix→Q36; life map→Q37; products/reports→Q40/Q41; Academy→Q42; territory→Q43; AI→Q44; import→Q30/Q45. Q31 chỉ khóa preservation/version authority, không phê duyệt phép tính.

## 5. Phạm vi đầu tiên và làn nghiên cứu dài hạn

Cohort đề xuất đầu tiên: người trưởng thành tự sử dụng, profile của chính họ, một lãnh thổ đã có pháp nhân/Privacy/Legal và một số capability đủ passport; L1/Numbers có giải thích giới hạn và kế hoạch hành động30ngày. Đây vẫn là đề xuất chờ Q decisions, chưa xác nhận mở pilot hoặc mở bán.

Giữ đầy đủ trong tổng kế hoạch nhưng chưa đưa vào cohort ban đầu khi chưa đủ điều kiện:

- Trẻ em, sức khỏe, ảnh tay/mặt/giọng/dáng, đánh giá nhạy cảm hoặc quyết định có tác động cao.
-62 adapter chưa đủ edition/rights/nguồn quy tắc/native reviewer/golden tests.
- L2–L9, nội dung150–600trang và LivingBook chưa đủ nguồn và nhu cầu dữ liệu.
- Native mobile/desktop installer, privacy/offline sync nâng cao.
- Practitioner/org/multi-subject, Academy certification, license/franchise và thị trường mới.
- Provider thương mại/AI chưa chọn, chưa có cost caps và thỏa thuận xử lý dữ liệu.

Không cắt chúng khỏi kế hoạch. Mỗi item có owner role, missing-input register, research/release state và điều kiện quay lại. Đi trước ở mức research/synthetic không cho phép ship năng lực chưa đủ nguồn hoặc quyền.

## 6. Cấu trúc backend ưu tiên

Kiến trúc đề xuất tiếp tục là modular monolith + API gateway/BFF; không chia microservice cho từng môn. Lõi phương pháp độc lập khỏi UI, AI và payment. PostgreSQL/R2/queue/outbox là thiết kế cần ADR và provider decision; không mặc nhiên chuyển kiến trúc runtime hiện có hoặc chạy migration từ bộ kế hoạch.

Các hợp đồng phải chốt trước code có side effects:

| Miền | Đầu ra bắt buộc | Failure/negative quan trọng |
|---|---|---|
| Canonical input | raw+normalized+schema+calendar/timezone+uncertainty+hypothesis version | DST gap/fold, leap day, Unicode equivalent, tên/Y không rõ, dữ liệu thiếu |
| Method release | edition/rights/config/golden/source digest/limits/reviewer | source conflict, variant mismatch, unknown thành0, rule không có quyền |
| Task calculation DAG | typed nodes, topo, resource caps, partial/error/null states, invalidation | cycle, missingnode, duplicatednode, runaway dependency, không sửa snapshot cũ |
| Claims | kind/source lineage/input lineage/uncertainty/contraindications | cùngDOB không thành3nguồn; sao chép cùng sách không là nguồn độc lập |
| API/schema | request/response/error, principal, tenant+subjectFK, purpose, schema revision | forgeduser_id, massassignment, crosstenant, staleprofile, moneyfloat |
| Rights/privacy | account≠subject≠payer≠practitioner, purpose grants/revoke/delete/export | revoke sauenqueue, workerpublish sau delete, signedURLreplay, RAGACLbypass |
| Jobs | run+outbox+idempotency transaction; lease/retry/DLQ/reconciliation | duplicate/reorder/crash, samekeydifferentpayload, cancel race, provider timeout |
| Cache | tenant/subject/purpose/accessrevision/inputdigest/method/source/locale | PIIhash không ẩn danh; không cache chung theoDOB |
| Reports | immutable snapshot/content tree, sandbox export, Web/PDF/Word version | URL/localfile injection, table/font overflow, stale rights, filler content |
| Commerce | orders/payment/entitlement/jobs/fulfillment/refund khácstate | webhookreplay/saiamount/currency, paidnhưng khôngconsent, refund/retryduplicate |
| Operations | exact RC/schema/providerreceipt/caps/restore+tombstones | backupkhôi phục dữliệu đãxóa, dirtydeploy, artifactlộdocs/SQL/ZIP |

99 operation =83 V2+16 V3 là contract inventory. Mỗi operation phải được nối tới implementation path và test receipt; trường chưa có implementation giữ `DESIGN_ONLY/NOT_CHECKED`. Demo chỉ health/catalog/run không làm99operation thành hoàn tất.

Formula registry là dữ liệu có schema, không nhận JavaScript tùy ý của editor. Tính chính xác dùng integer/fraction/decimal string theo contract; số dư80 là integer; tiền gắncurrency và minor units. Thiếu mẫu số, dữ liệu, quyền hoặc phép tính thì null+reason. AI không được lấp chỗ trống bằng một kết quả tưởng tượng.

## 7. Gói demo và trải nghiệm đa thiết bị

167 demo cần được nhập như fixture/versioned catalog với expectedresult, method/source/configdigest, loại dữ liệu và category. Bộ đủ phải có: normal, thiếu input, nhiều giả thuyết/xung đột, boundary, unsupported/unreleased, unauthorized/revoked, stale, timeout/cancel/failure, export/layout, locale và performanceclass. Không dùng nhiều biến thể cùng fixture để phóng đại coverage độc lập.

Các nhóm bắt buộc trước claim “dễ dùng, nhanh, đầy đủ”:

1. Intake từng bước trên360/390px: cần gì hỏi nấy, giải thích vì sao cần dữ liệu, cho unknown/skip.
2. Result trace: raw→normalization→rule→output→claim, thấy rõ partial/unreleased và sửa input không mất raw.
3. Matrix/table: horizontal handling có nhãn, key information readable trên mobile; desktopweb có compare/filter rõ.
4. Timeline: age/event boundary, quan sát thật và symbolic khác loại, không gán sự kiện đời thật để đủ trang.
5. Reports: sharedcontenttree, PDF/Word font/table/pagebreak, privacy download và snapshotversion.
6. Permission/consent: payer không tự xem profile; revoke/cancel/delete phản hồi dễ hiểu.
7. Responsive keyboard/zoom/screenreader, contrast, focus và reducedmotion phù hợp.
8. Performance đo riêng calculation, profile aggregation, export, retrieval vàAI; công bố môi trường, percentile/sample, resourcecaps. Benchmarklocal không làSLA.

Receipt browser của V3 dùng Chromium `set_content`/mock fetch; HTTP navigation bị administrator chặn. Nó là bằng chứng offline fixture và bốnviewport, không phải integrated browser HTTP E2E, WCAG certification hoặc native app. Cần lần kiểm thật sau với candidate đang bàn giao. Node HTTP và browser HTTP là hai receipt riêng.

Web responsive phục vụ mobile browser và desktopweb. PWA có điều kiện cache/sync, privateoffline tắt mặc định. Nativeapp là track riêng sau quyết định budget/platform; không đánh dấu native hoàn thành từ responsive/PWA.

## 8. Báo cáo, AI và biên tập

Mỗi9report level có purpose, audience, minimum data, section contract, missing data behavior, allowed claim types, source policy và example đủ/thiếu/xung đột. Bốn khối nội dung dùng cùng snapshot; không dựa số trang để đánh giá chất lượng. 30–600trang là budget editorial có điều kiện, không yêu cầu viết cho đủ.

AI pipeline: admissible claim assembler → writer → independent reviewer → human release theo scope. ACL phải lọc trước retrieval; prompt và tài liệu truy xuất là dữ liệu không phải lệnh gọi tool. Mỗirun gắn model/prompt/source/claim policy, quota/cost caps và fallback có cùng giới hạn dữ liệu/quyền. Không tự tăng ngân sách hoặc đổi provider vì lỗi. Feedback người dùng không tự phê duyệt công thức.

A0 gợi ý, A1 đọc, A2 bản nháp có thể đảo ngược, A3 playbook có điều kiện; chỉ A3 được chọn rõ mới có tool actions trong scope. Đổi quyền, dùng secret, công bố, charge, migration vàdeploy vẫn cần authority/receipt riêng.

## 9. Nguồn lực và effort không cộng trùng

Các khoảng ước lượng lịch sử:

- 140 task V1: 361–852 person-days.
- 16 task UPG: 91–187 person-days; local156 là452–1039 person-days.
- 68 task V2: 130–396 person-days. Đây là các phần refinement, **không tự cộng với parent**.
- 72 task V3: chưa có estimate, giữ null; không được coi là0.
- 20 work order INT: 16 proposal có khoảng50–103 person-days và bốn work order chưa có estimate. Chúng cũng có thể chồng phạm vi task nguồn, **không tự cộng vào ngân sách296 task**.

Chưa thể tính tổng ngân sách hoặc ngày hoàn thành toàn portfolio từ các số này. Cần bảng rollup chọn parent hoặc leaf cho cùng deliverable, ghi phần delta thực sự và phạm vi nghiệm thu. Không xóa estimate gốc. Lưu `estimate_origin, overlap_group, rollup_disposition, approved_by, approved_at`. Parent có thể là envelope hoặc summary, nhưng không đồng thời tính phí parent và child cho cùng đầu ra.

Bố trí đề xuất6–8FTE core, chưa phải cam kết tuyển hoặc phê duyệt chi phí:

| Vai trò | Năng lực dự kiến | Ràng buộc |
|---|---|---|
| Tech/Backend Lead |1 FTE | Chốt source, schema, security; cần người khác review độc lập |
| Backend/Method Engineer |1–2 FTE | Calculation, versioning, API và jobs |
| Frontend/UX |1 FTE | Mobile/desktop web, trạng thái và report view |
| Method/Source Reviewer |1 FTE | Có thể cần reviewer bản địa theo từng họ phương pháp |
| AI/Editorial |0.5–1 FTE | Claim contracts và report corpus |
| QA/Security |1 FTE | Độc lập implementation; browser, negative và contract tests |
| Platform/SRE |0.5–1 FTE | Staging, tải và phục hồi; chuẩn bị contract trước khi có provider |
| Founder/Product/Finance/Legal | Capacity theo lịch cụ thể, chưa quy đổiFTE | Chọn scope, nguồn/quyền, entity, country, budget và partner |

18 productive person-days/FTE/month là giả định lập kế hoạch, chưa là thông số đã đo. Capacity danh nghĩa108–144 person-days/month không loại bỏ thời gian chờ quyền nguồn, review độc lập, pháp lý hoặc staging. Không chuyển452–1039 hay491–1248 thành lời hứa4–6 tháng cho toàn portfolio. Mốc paid beta4–6 tháng chỉ là đề xuất có điều kiện, cần cohort, requirements, nguồn lực và lead time phê duyệt được kiểm chứng rồi reforecast. Các khoảng12–18/12–24+tháng trong tầm nhìn cũ không là ngày giao hàng cam kết.

Tiền, currency, đơn giá và vendor quotes giữ null đến khi Finance duyệt. Các khoản cần tính gồm quyền nguồn, reviewer bản địa, cloud/runtime/AI, hỗ trợ, pháp lý theo lãnh thổ, render/storage/egress và phục hồi. Contingency cần cơ sở và người duyệt; không tự cộng phí hoặc quy đổiUSD/VND.

## 10. Wave và đường găng có điều kiện

Các wave áp dụng theo capability và cohort. Không bắt hoàn thành62 phương pháp hay28 sản phẩm để mở một pilot nhỏ.

| Wave | Work order chính | Điều kiện kết thúc |
|---|---|---|
| W0 — Bảo toàn và authority |INT29-001…004 | Source receipts; 296+20 ID; typed DAG; sổ conflict/decision; phần chưa ký vẫn pending |
| W1 — Method/input/contracts |005…010 | Passport cho method được chọn; canonical input; biến thể số/timeline; schema/API crosswalk |
| W2 — Trust/jobs/UX/AI |011…016 | Tenant/purpose/consent; jobs/cache; demo được admission; template/report và responsive states; AI contracts |
| W3 — Commerce/reliability |017…018 | Entity/currency/provider decisions; sandbox reconciliation; exact RC staging/security/recovery |
| W4 — Pilot/handoff |020 | Trace hai chiều; gate evidence; support/kill switch/cost caps; receipt người duyệt và cohort |
| W5 — Expansion |019 và scope mở rộng | Phát hành territory/Academy/practitioner/native/method/level riêng |

Đường găng logic: source/candidate identity → quyết định về scope, quyền nguồn, schema và permission → input contract của method được chọn → tenant/purpose/auth → API/jobs/snapshot → report/mobile flows → QA độc lập → staging migration/RLS/recovery → quyết định pilot theo cohort.

Commerce là đường găng của paid pilot. Chưa có entity/currency/provider thì chỉ làm synthetic hoặc phạm vi phi thương mại được duyệt. AI có thể giữ unreleased nếu cohort không dùng AI. Các quyền nguồn, auth và privacy cốt lõi vẫn phải được kiểm chứng.

Các làn song song sau foundation: Product/Method/Rights; Trust/Data; API/Frontend; AI/Editorial/Reports; Commerce/SRE; Legal/Academy/Territory. Người author không tự đóng vai reviewer độc lập cho receipt của mình. Mỗi người giữ WIP limit một việc chính và một lượt review. Effort và lịch phải tính theo capacity thực tế đã nhận việc.

## 11. Dispatch mười ngày làm việc đầu

Đây là cửa sổ điều phối, **không phải cam kết hoàn tất20 work order trong mười ngày**. Ngày1 là ngày đội ngũ được chỉ định và nhận scope. Ngày nghỉ, lead time và thời gian chờ duyệt không tự trở thành capacity. Quyết định còn pending vẫn chưa được duyệt.

| Cửa sổ | Điều phối | Đầu ra kiểm tra được |
|---|---|---|
| Ngày1 | Program/Tech/QA ràINT29-001…003; khóa scope, giữ dirty work; Founder/Product xemQ1/Q31/Q40 | Identity receipt, preservation result, 296+20 catalog, conflict list và capacity từng vai trò |
| Ngày2 | Data/QA kiểm typedFK/DAG/rollup; Program chuẩn45packet; Method mở rights register | Graph receipt, no-lossUPG/P0diff, 45 pending packet và cohort đề xuất |
| Ngày3–4 | Backend/Method làmINT29-006 và schemaINT29-010; UX làm flow synthetic; Method/Legal làmINT29-005 theo method được chọn | Ví dụ tên/thời gian/giả thuyết, API schema/error, source/rights gaps và crosswalk69screen |
| Ngày5 | Review point1: chốt phần đủ điều kiện, giữ pending phần còn thiếu; QA chọn golden/negative corpus | Option receipt nếu được duyệt thực; blocked queue có owner; không tự mark done |
| Ngày6–7 | Backend/Security chuẩnINT29-011…012; Method007…009 theo passport; Editorial014; UX015 chạy fixture | Permission matrix, job state plan, calculation goldens, missing-data preview và mobile/state design |
| Ngày8 | QA/Security review chéo; AI016 và Commerce017 làm contract/sandbox plan nếu chưa đủ quyết định | Negative cases, eval/cost caps, entity/currency gaps và các blocker về source/rights/schema/cohort |
| Ngày9 | SRE/QA chuẩnINT29-018 đúng candidate; Program nối traceINT29-020; chưa chạy provider action | Staging/recovery test plan, artifact allowlist, trace gaps và trạng thái READY/BLOCKED theo scope |
| Ngày10 | Review point2: giao DEV batch tiếp, ước lượng leaf theo capacity và pilot exit criteria | Handoff cho scope đủ điều kiện; pending work có owner/revisit event; reforecast có căn cứ |

Khi đã đủ approval, có thể bắt đầu candidate synthetic song song theo work-order contract. Khi chưa đủ, tiếp tục fixtures, schema, trace và nghiên cứu quyền nguồn. Không lấy việc đợi phê duyệt làm lý do bỏ kiểm tra hoặc tự mở hành vi đang bị chặn.

## 12. Definition of Ready và Done

Ready for DEV cần task ID/source SHA; title/scope/exclusions; người thật đã nhận vai trò; baseline/candidate; typed dependencies; quyết định, quyền nguồn, schema và cohort đủ cho capability; version bundle; deliverables; positive/negative/boundary/permission/failure tests; evidence path; reviewer độc lập; rollback và capacity/estimate policy. Tên người, provider, quyền nguồn hoặc budget chưa biết phải để null và ghi blocker.

Done for local cần implementation/diff/spec đúng scope; test receipt có pass/fail/skip, command và environment; reviewer receipt; acceptance đạt; artifact digest; mọi gap có disposition được duyệt. Chỉ claim `VERIFIED_LOCAL_ONLY` ở đúng lớp bằng chứng.

Done for staging cần thêm exact RC deployment mapping, migration/RLS bằng role thực, sandbox provider/payment nếu áp dụng, browser HTTP flows, performance caps, recovery/rollback/tombstones và review receipt. Local test không thay staging.

Done for release/pilot cần quyền theo product/method/territory/cohort; entity/pricing/provider constraints; đủ gate evidence áp dụng; operator/window/rollback/support/cost caps và human release authorization. Phê duyệt cho scope nhỏ không lan sang scope khác.

Mỗi receipt ghi receipt ID; full source/candidate SHA và artifact SHA256; package version; command/env/role; số test và skip reason; expected/actual; đầu ra; thời gian; actor/reviewer; failures/limits; nội dung đã che vì riêng tư; decision/gate IDs; expiry/revisit event. Không chứa secret, hồ sơ riêng tư hoặc download token.

## 13. Gate, QA claim và vận hành

G01 Source/Release; G02 Authentication; G03 Authorization; G04 Legal/Purpose; G05 Retention/Deletion; G06 Methods/Claims; G07 Legacy/Migration; G08 Reports/AI; G09 Commerce; G10 Reliability; G11 Security Review; G12 Operations/Pilot.

RG0–RG13 được giữ làm chỉ mục các lớp source, governance, architecture, AI, infra, DEV, docs, integration, QA, staging, authorization, post-deploy, handoff và Founder. Mapping không đóng gate. Không lấy trung bình để bù một core gate thất bại.

Các lớp bằng chứng được phân biệt:

- Unit/reference/demo/importer tests của V1/V2/V3 là receipt của package và lần chạy nguồn. Chỉ gọi verified current khi chạy lại đúng current bytes trong bản sao và giữ record.
- Manifest V3 hiện hành có519 entry cho520tệp vì tự loại chính nó. Chênh lệch này phù hợp scope, không phải lỗi thiếu tệp. `FULL_IMPORT_REHEARSAL` vẫn là temp-fixture receipt lịch sử, không chứng minh importer đã chạy vào worktree này.
- PDF/doc receipt nguồn nói đã xem contact sheet toàn trang và một số trang dày ở full size. Không nâng thành claim mọi trang đã được đọc full size trong lần này.
- Workbook V3 thực có21 sheet: `Tong quan` và20 sheet chi tiết.24 formula gồm19COUNTA và năm cost formula; 19 headline count khớp các dòng dữ liệu hiện tại. Không có error cell lưu sẵn trong XML. Đây là kiểm cấu trúc/formula/cached values, chưa chạy recalculation trong Excel hoặc kiểm visual hiện hành.
- Workbook V2 giữ nguyên11sheet của V1 ở mức dữ liệu ô, rồi thêm chín sheet. Ba workbook có tổng52sheet, 122 formula và18.704ô không rỗng trong extraction. Không coi số formula hoặc ô là điểm chất lượng sản phẩm.
-13 binary extraction đã được đọc/parse toàn bộ và đối chiếu nội dung/chính sách theo phạm vi: 2.260DOCX paragraph, 15 table và152 PDF page. Đối chiếu text/cell không thay kiểm layout, clipping hoặc đọc visual từng trang.
- Không dùng403 hoặc GitHub SHA cũ để kết luận quyền remote hiện tại. Không thử ghi remote trong phạm vi này.
- Public artifact dùng allowlist, loại docs/SQL/ZIP/fixture/private assets. Source, build artifact và HTTP served content cần receipt riêng.

Chiến lược test gồm unit/property/method goldens; schema/API contract; task/decisionDAG; object/tenant/purpose/revocation negatives; jobs/webhook/idempotency/races; real DB migration/RLS; report layout/sandbox; browser HTTP/mobile keyboard; load/cost caps; restore/rollback và security retest độc lập. Không cộng167demo +125 V2 +83 V1 +192 V3 thành “567test độc lập”. Các suite và demo có grain chồng lấp, cần test ID và provenance.

## 14. Điểm cần con người quyết định, không chặn công việc chuẩn bị

| Input chưa có | Vai trò cung cấp | Trước sự kiện nào |
|---|---|---|
| Cohort/capability/L1 scope và lãnh thổ đầu | Founder + Product + Legal/Privacy | Pilot hoặc public promise |
| Nguồn, edition/quyền và native reviewer từng method | Method + Rights/Legal | Admission/release method |
| Option cho Y/reduction/timezone/leap/0/5/zero80/cycle boundary | Method + Domain QA | Triển khai behavior bị ảnh hưởng |
| Schema/candidate/IdP/datastore/queue/storage/AI providers | Tech + Security + Privacy + Finance | Staging integration hoặc provider access |
| Entity/controller/merchant/currency/pricing/refund/tax | Founder + Legal + Finance | Nhận thanh toán/cấp paid entitlement |
| Danh sách người thật, capacity và review độc lập | Program + Tech + QA | READY FOR DEV/dispatch |
| Chi phí source/vendor/cloud/AI/support/contingency | Finance + Vendor/Functional Owner | Approved budget hoặc paid pilot |
| Staging/operator/window/recovery/SLO/support | Release + SRE + QA | Rehearsal/pilot |
| Local counsel/certification/territory/partnership | Legal + Academy + Partnerships | Mở thị trường, chứng nhận hoặc đối tác |

Trong khi đợi, có thể làm preservation/crosswalk, schema samples, synthetic negative/golden fixtures, API/UI states, report preview, estimate-overlap map và release checklists. Công việc tài liệu/synthetic reversible trong yêu cầu hiện tại không cần xin lại quyền.

## 15. Bàn giao và nhịp điều hành

Mỗi DEV batch chọn5–10 leaf/work order theo capability vừa capacity. Không giao toàn296task vào một sprint. Đầu batch ghi scope, readiness, source/candidate, owner/reviewer và evidence path. Cuối batch so expected/actual, review gap và reforecast. Số file hoặc tỷ lệ task done không phải quality score.

Board dùng PROPOSED → READY_FOR_SCOPED_DEV → IN_PROGRESS → INDEPENDENT_REVIEW → VERIFIED_LOCAL/STAGING → CLOSED_FOR_SCOPE. BLOCKED luôn ghi reason, owner, receipt cần có và revisit event. Plan/catalog completeness, implementation readiness, staging readiness và commercial release là bốn trạng thái riêng.

Bộ bàn giao gồm canonical catalog/typed DAG; 45 decision packets; 20 work orders; source/rights passports; formula/schema/API/result contracts; demo catalog/goldens; product/screen/report crosswalk; estimate-overlap/capacity; bidirectional trace; test/evidence/gate indexes; release/recovery/support playbooks. Giữ danh sách phần chưa có để DEV không phải tự đoán.

**Điểm bàn giao hiện tại: ** tổng kế hoạch và hợp đồng chuẩn bị DEV đã được mở rộng có truy vết. Phát hành vẫn cần chứng cứ và quyết định theo đúng scope. Bộ chuẩn bị này chưa xác nhận app production đã nâng cấp hoặc phương pháp đã được chứng minh.
