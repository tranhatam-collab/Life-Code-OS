# Life Code OS Kế hoạch hợp nhất chuẩn bị phát triển

Phiên bản 2026-10-20.r2. Release HOLD.



---

# Life Code OS Phần hợp nhất bổ sung ngày 20 tháng 10 năm 2026

Phiên bản 2026-10-20.r2. Phần này bổ sung bộ 149 tệp ngày 11/10 và kế hoạch audit tại 336ef35a. Bảo toàn 9 cấp, 12 lớp, 12 trường Đồng nhịp sống, 20 họ nghiên cứu, 23 sản phẩm, 45 màn hình và 140 task gốc. Các registry mở rộng nêu riêng số record mới và liên kết record cũ.

## Mục tiêu của lần nâng cấp

Bộ tài liệu phải cho DEV biết xây gì, đầu vào nào hợp lệ, tính theo nguồn nào, kết quả nào được phép xuất, ai có quyền đọc, demo nào minh họa và test nào nghiệm thu. Hướng sản phẩm là tự hiểu, ghi nhận trải nghiệm và thiết kế hành động. Những nhận định biểu tượng phải được trình bày đúng loại, không biến thành xác suất bệnh, số phận hoặc đảm bảo lợi nhuận.

## Khóa nguồn và bảo toàn

Canonical remote là tranhatam-collab/Life-Code-OS. Main 99b402764437f81859fa0cd3a3af860125f7bd52 và plan 336ef35a8386a744c6de18a7f7c6e268e89e6dac được đối chiếu remote ngày 20/10. Checkout mới nằm trong đúng thư mục Life-Code-OS, nhánh codex/complete-upgrade-plan-2026-10-20, bắt đầu từ plan commit. Checkout dirty phase-1.5 được giữ nguyên.

ZIP gốc và thư mục giải nén có 149 tệp cùng bytes. Manifest gốc có 148 checksum không tự băm chính nó. Nguồn được lưu tại `../sources/2026-10-11`, có receipt riêng; file Word/PDF/Excel gốc được giữ. Kế hoạch audit và source cũ nằm trong baseline Git. Không gộp origin source, worktree, demo, provider và runtime thành một lớp verified.

## Backend là trục tích hợp

Backend có bốn phần hợp đồng: domain/account/subject/grants; input normalization và method core; job/report/payment; operations/provenance. API nhận intent và data hợp lệ, không nhận identity/score/weight tự khai làm authority. Mỗi query chứa tenant/subject/owner constraints; mọi job recheck quyền khi bắt đầu và trước publish. Frontend nhận kết quả, phép giải thích và reason codes từ cùng lõi.

Mỗi phương pháp có method ID và release version, edition/trường phái, source cụ thể, quyền sử dụng, input schema, normalization, formula/rule table, unit/range, assumptions, missing-data behavior, golden vectors, forbidden claims, reviewer và kill switch. Trường cần nghiên cứu được ghi là thiếu nguồn hoặc chưa duyệt. Không viết công thức tiên đoán để lấp một khoảng trống tài liệu.

Công thức biểu tượng, đo lường có validation, dữ liệu tự báo cáo, kết quả tính xác định và kịch bản giả định có nhãn riêng. Tính xác định chỉ chứng minh cùng input/version cho cùng kết quả; nó không chứng minh khả năng tiên đoán. Chứng cứ nội dung và quyền nguồn là prerequisite của phát hành method.

## Ma trận dữ liệu và độ đầy đủ

120 trường là catalog tùy chọn. Mỗi use case chỉ yêu cầu tập trường tối thiểu của phương pháp đã chọn. Input cần provenance, độ chính xác, locale, timezone/calendar version, time uncertainty và purpose. Unknown, refused, not-collected, not-applicable và measured-zero phải được giữ khác nhau. Không đưa null thành zero để tạo biểu đồ đầy.

Coverage dùng expected-input registry do server version hóa, không dùng denominator do client đưa. Coverage không bằng confidence hay xác suất đúng. Không gộp mọi trường phái thành một điểm LCI duy nhất khi chưa có measurement model, validation và phê duyệt ngôn ngữ. LCI legacy và timeline sin nằm trong experimental_legacy, không làm ground truth hoặc training truth.

## Demo phục vụ học và nghiệm thu

Các demo dùng dữ liệu tổng hợp, hiển thị input, version, trace từng bước và expected output. Cần đủ ca hợp lệ, thiếu dữ liệu, sai kiểu, biên miền, Unicode, ngày nhuận, giờ không biết, DST ambiguity, thay phương pháp, quyền bị rút, retry/trùng job, schema conflict và report export. Demo phương pháp chưa duyệt hiển thị lý do chặn cùng artifact còn thiếu.

Demo local có thể hoạt động nhanh mà không gọi provider. API, SQL/RLS, thanh toán, recovery và load tests vẫn cần môi trường thực riêng để chứng minh. Một policy function trong bộ nhớ không thay query authorization hoặc transaction durability. Demo UI phải đọc được trên mobile và desktop, có keyboard và giải thích thuật ngữ bằng tiếng Việt.

## Trải nghiệm đa thiết bị

Một API và model nội dung phục vụ public web, mobile web/PWA và desktop web. Điện thoại ưu tiên từng bước nhập, progress rõ, lưu nháp có quyền và lỗi cạnh trường; desktop có danh sách/chi tiết/so sánh và phím tắt không cản screen reader. Kết quả không thay đổi theo kích thước màn hình. Cấu trúc Web/PDF/Word dùng cùng report snapshot.

PWA chỉ cache app shell, tài nguyên công khai đã version hóa và nội dung được policy cho phép. Không cache báo cáo cá nhân, token hoặc raw intake mặc định. Khi offline, giải thích chức năng khả dụng; lệnh ghi không âm thầm enqueue nếu chưa có conflict/revocation contract. Logout và chuyển account phải xóa dữ liệu cache trong scope thiết bị.

## Architecture và migration

Giữ modular monolith và TypeScript/Node method core như phương án đề xuất. Astro/React/Worker/PostgreSQL/R2/Queues là lựa chọn cần ADR và vendor review, không là hợp đồng đã ký. Không thay runtime trong P0 containment. Chọn version và region theo khả năng hỗ trợ, workload, latency, quyền dữ liệu và chi phí.

Migration D1 sang PostgreSQL cần inventory raw/derived/unknown-owner, mapping theo key và type, duplicate policy, consent/provenance, counts/checksums, rejection ledger, dry run, compatibility window, freeze/cutover, reconciliation và rollback an toàn. Không đưa output legacy vào fact tables. Chưa có inventory/provider receipt thì thiết kế migration vẫn có thể hoàn tất, chạy production vẫn bị chặn.

## Bảo mật và sự cố

Source baseline xác nhận những route profile/session/life-code-data/report chưa khóa object owner. Điều đó chưa chứng minh đã có breach. P0 phải có server-side containment và negative tests trên hai account synthetic. Token lifecycle, session recovery, CSRF, tenant/field/grant và download đều có test riêng. CORS và noindex không thay authentication.

Kho tài liệu gốc, artifact export và số liệu QA không được tự trở thành public build assets. Build chỉ nhận allowlist; receipt liên kết full source SHA, artifact digest, schema/method versions, provider deployment IDs và environment. Bản rollback không được mở lại lỗi hoặc method đã revoked.

## Operations và tiền

Beta objectives giữ mục tiêu ban đầu để đo: availability 99,5%, API p95 800 ms, Level 1 background report 5 phút, RPO 1 giờ, RTO 4 giờ. Đây là proposed targets. Runbook mới quy định numerator/denominator, timeout, alert owner, drill và acceptance evidence; cần measurement trước cam kết SLA.

Chi phí phải gồm labor, hạ tầng, AI, egress/storage, hỗ trợ, quyền nguồn, pháp lý và security. Thiếu quote/merchant/rate giữ unavailable. Không biến workbook blank thành tổng ngân sách bằng zero. Thử tải phải tính queue wait, cold start, retry amplification, report size và concurrent users; p95 đo bằng workload và thời gian đã ghi.

## Pháp lý và quốc tế

Đã kiểm tra lại metadata chính thức của Luật AI 134/2025, Nghị định 142/2026, Luật TMĐT 122/2025, Nghị định 248/2026 và Luật bảo vệ dữ liệu cá nhân 91/2025. Registry nghiên cứu ngày 20/10 ghi URL và phạm vi đã đọc. Không coi metadata là ý kiến áp dụng toàn văn. Pháp nhân, merchant, controller/processor, data flow, nghĩa vụ AI, consumer và country packs vẫn phải được chức năng liên quan chốt.

Giữ đầy đủ Academy, practitioner, family, tổ chức, API, license và franchise trong roadmap. Mỗi nhánh có gate riêng về quyền dữ liệu, năng lực, nguồn, hỗ trợ và quốc gia; một beta cá nhân không cấp approval cho các nhánh này. Vai trò người trả tiền không tự cấp quyền xem đời sống riêng của thành viên.

## Thực thi và điều kiện bắt đầu

Giữ ID task cũ, bổ sung dependency/allowed paths/test/evidence và task integration. Ước lượng không thành deadline trước khi có capacity. Q1–Q20 giữ trạng thái chờ quyết định; packet mới phải trình bày alternatives, impact, chi phí và phụ thuộc để Founder review cụ thể. Gate G01–G12 ánh xạ đầy đủ RG0–RG13, không tạo bộ authority thay FPOS.

Đội có thể chuẩn bị branch, schema, adapter, test và demo synthetic theo task được giao. Mở pilot và mọi thao tác production cần đầy đủ receipt và người có thẩm quyền trên exact RC. Bản kế hoạch nâng cấp không làm tăng maturity hoặc đóng một release gate chỉ bằng số lượng tệp.


---


# Mục lục chuyên đề

D02 Đối chiếu nguồn, nội dung công khai và trạng thái vận hành — `09_Doi_chieu_Bang_chung/01_CURRENT_STATE_AUDIT.md`

D03 P0: chặn rủi ro trong 48–72 giờ và bảo toàn chứng cứ — `07_Bao_mat_Van_hanh/01_P0_CONTAINMENT.md`

D01 Life Code OS: tầm nhìn, giới hạn và cấu trúc hợp nhất — `01_Chien_luoc_San_pham/01_MASTER_VISION.md`

D04 Chuỗi sản phẩm từ miễn phí tới doanh nghiệp và đối tác — `01_Chien_luoc_San_pham/02_FREE_TO_ENTERPRISE.md`

D05 Hợp đồng chín cấp Life Code và cách trưởng thành hồ sơ — `01_Chien_luoc_San_pham/03_NINE_LEVEL_CONTRACT.md`

D06 Hành trình người dùng, trạng thái trống và tiêu chí giá trị — `01_Chien_luoc_San_pham/04_USER_JOURNEYS.md`

D07 Học thuyết HNH và ngữ pháp đời sống có cấu trúc — `02_Tri_thuc_HNH/01_HNH_DOCTRINE.md`

D08 20 họ tri thức: cách khảo cứu, tích hợp và phát hành — `02_Tri_thuc_HNH/02_METHOD_RESEARCH_PROTOCOL.md`

D37 Chương trình nghiên cứu chuyên sâu K01–K20 và cách tạo Code HNH — `02_Tri_thuc_HNH/04_DEEP_RESEARCH_SYLLABUS.md`

D09 Đồng nhịp sống và thiết kế đời sống: đặc tả dữ liệu và thực hành — `02_Tri_thuc_HNH/03_RESONANCE_AND_LIFE_DESIGN.md`

D10 Mô hình miền: tài khoản, chủ thể, quyền và dữ liệu nhiều giả thuyết — `03_Du_lieu_Phep_tinh/01_DOMAIN_MODEL.md`

D11 Hợp đồng kết quả, chỉ số và cách xử lý điều chưa biết — `03_Du_lieu_Phep_tinh/02_METHOD_CONTRACT_AND_METRICS.md`

D12 Bộ số: quy tắc độc lập, trường hợp biên và Mã đuôi 80 — `03_Du_lieu_Phep_tinh/03_NUMBERS_AND_TAIL80.md`

D13 Dòng thời gian 0–99: lịch sử, chu kỳ, kế hoạch và kịch bản — `03_Du_lieu_Phep_tinh/04_TIMELINE_AND_SCENARIOS.md`

D14 Backend: modular monolith, ranh giới tin cậy và lựa chọn công nghệ — `04_Backend_API/01_TARGET_ARCHITECTURE.md`

D15 Danh tính, phiên, chia sẻ và kiểm soát đối tượng — `04_Backend_API/02_AUTH_AND_AUTHORIZATION.md`

D16 Tác vụ nền, thanh toán và tính nhất quán nghiệp vụ — `04_Backend_API/03_JOBS_IDEMPOTENCY_AND_COMMERCE.md`

D17 API v2, tương thích và migration D1 sang PostgreSQL — `04_Backend_API/04_API_AND_MIGRATION.md`

D18 Frontend: điều hướng, trang công khai và không gian ứng dụng — `05_Frontend_UI/01_INFORMATION_ARCHITECTURE.md`

D19 Thiết kế giao diện, ngôn ngữ Việt và khả năng tiếp cận — `05_Frontend_UI/02_DESIGN_SYSTEM_AND_A11Y.md`

D20 Nâng cấp nội dung live và SEO không phá đường dẫn — `05_Frontend_UI/03_PUBLIC_COPY_AND_SEO_MIGRATION.md`

D21 AI hỗ trợ: học, hỏi, viết và kiểm soát hành động — `06_AI_Bao_cao/01_AI_ORCHESTRATION.md`

D22 Tự động hóa có giới hạn: giảm thao tác, không bỏ trách nhiệm — `06_AI_Bao_cao/02_AUTONOMY_AND_ADMIN_MINIMIZATION.md`

D23 Nhà máy báo cáo: một nội dung chuẩn cho Web, PDF và Word — `06_AI_Bao_cao/03_REPORT_FACTORY.md`

D24 Chuẩn tiếng Việt, cấu trúc bài đọc và chất lượng học liệu — `06_AI_Bao_cao/04_EDITORIAL_AND_EDUCATIONAL_STANDARD.md`

D38 Chuẩn bài đọc người dùng: từ dữ liệu đến lựa chọn — `06_AI_Bao_cao/05_USER_VALUE_AND_SAMPLE_NARRATIVE.md`

D25 Dữ liệu cá nhân: mục đích, lưu giữ, xóa và khôi phục — `07_Bao_mat_Van_hanh/02_PRIVACY_AND_DELETION.md`

D26 Mô hình đe dọa và ranh giới bảo vệ — `07_Bao_mat_Van_hanh/03_SECURITY_THREAT_MODEL.md`

D27 Vận hành, quan sát, khôi phục và kiểm soát chi phí — `07_Bao_mat_Van_hanh/04_OPERATIONS_SRE_AND_COST.md`

D28 Pháp lý Việt Nam và phạm vi dịch vụ phải rà soát — `07_Bao_mat_Van_hanh/05_VIETNAM_LEGAL_READINESS.md`

D29 Cấp phép quốc tế và nhượng quyền Huyền Nhân Học — `08_Thuc_thi_Kinh_doanh/01_INTERNATIONAL_AND_FRANCHISE.md`

D30 Academy, đào tạo giảng viên và không gian chuyên gia — `01_Chien_luoc_San_pham/05_ACADEMY_AND_PRACTITIONERS.md`

D31 Tổ chức, gia đình và quyền cá nhân không thể bị hòa tan — `01_Chien_luoc_San_pham/06_ORGANIZATION_AND_FAMILY.md`

D32 Mô hình thương mại, chi phí và tính bền vững của miễn phí — `08_Thuc_thi_Kinh_doanh/02_COMMERCIAL_MODEL_AND_UNIT_ECONOMICS.md`

D33 Lộ trình, phân công và quản trị phụ thuộc — `08_Thuc_thi_Kinh_doanh/03_ROADMAP_AND_RACI.md`

D34 Mười hai cổng phát hành và yêu cầu bằng chứng — `07_Bao_mat_Van_hanh/06_RELEASE_GATES.md`

D35 Quyết định Q1–Q20: nền cũ và phạm vi mở rộng — `08_Thuc_thi_Kinh_doanh/04_FOUNDER_DECISIONS.md`

D36 Giao việc cho AI và DEV: bối cảnh, lệnh thực hiện và báo cáo — `08_Thuc_thi_Kinh_doanh/05_AI_DEV_HANDOVER_PROTOCOL.md`


---


# Các chuyên đề hợp nhất



---

# Đối chiếu nguồn, nội dung công khai và trạng thái vận hành

Mã tài liệu: **D02** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Tech Lead + Security + QA. Nguồn đối chiếu: G01, G02, G04, G09, G10, S01, S03, S05, S06. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Baseline có thể tái kiểm tra
Remote main: `99b402764437f81859fa0cd3a3af860125f7bd52`. Nhánh kế hoạch mới: `audit/lifecode-os-comprehensive-upgrade-plan-2026-10-11`, SHA `336ef35a8386a744c6de18a7f7c6e268e89e6dac`. Đây là tài liệu chờ Team Audit; không xem việc tồn tại commit là Founder đã phê duyệt Q1–Q12.
Nguồn audit khai báo local phase HEAD `4df9b6efa6601bc113bc51956ed83e076da75657`; phiên này không truy cập máy Mac hoặc xác nhận worktree. Public home, chín tầng, Bắt đầu, Dashboard, Privacy và Engine Lab đọc được qua công cụ web; thông tin crawler không chứng minh byte-level live match. URL `.html` và probe `/health` gặp lỗi từ công cụ. Container không phân giải được các host. Điều này không chứng minh website ngừng hoạt động.
Không có Worker version, Pages deployment ID hay receipt runtime hiện hành. Vì vậy tách VERIFIED_SOURCE, VERIFIED_PUBLIC_CONTENT, REPORTED_BY_PRIOR_AUDIT, NOT_CHECKED và BLOCKED. Không sao chép nhãn VERIFIED_CURRENT của audit cũ sang mọi bảng mới.
## 2. Phát hiện kế thừa
API đọc profile theo ID chưa có kiểm tra session trong nhánh xử lý đã đọc. Session start nhận `user_id` từ payload và ghi hồ sơ. Report đọc result ID chưa khóa theo principal. Frontend gửi điểm cố định, session token lưu client-side. Timeline dùng tín hiệu từ seed/sin thay dữ liệu đánh giá. Những lỗi này được ghi theo SHA source; không tuyên bố đã khai thác hoặc đã xảy ra lộ dữ liệu.
Coverage cũ chia phần hợp lệ cho phần do client gửi nên một mảng nhỏ có thể đạt full. Một nhánh mission trừ 0,25 khỏi phần lẻ nhưng đòi ngưỡng 0,78 không thể kích hoạt theo công thức hiện có. Cách sửa là cách ly mô hình, không hạ ngưỡng cho xuất hiện thêm năm sứ mệnh.
## 3. Phát hiện cần bổ sung
Script Pages dùng rsync với denylist, không loại trừ tổng quát `api/`, `engine/`, `.env*` hoặc mọi loại tệp sẽ được bổ sung sau này. Chưa thấy secret bị lộ; đây là rủi ro thiết kế bundle. Phải chuyển sang public allowlist và kiểm tra artifact trước deploy.
Workflow Pages đọc được có `--commit-dirty=true`, bước tạo project dùng `|| true` và không có chuỗi gate đầy đủ trong workflow này. Không xóa cờ rồi tuyên bố chuỗi cung ứng đã an toàn: phải liên kết SHA, artifact hash, test run và deployment receipt.
## 4. Kết luận vận hành
NO_GO cho mở rộng dữ liệu sâu và báo cáo dựa trên điểm legacy. CONDITIONAL_GO cho trang giới thiệu đã sửa copy và công cụ dùng dữ liệu tổng hợp rõ nhãn. Không quy đổi trạng thái này thành 25%, 90% hoặc một con số cảm tính. Trạng thái từng cổng nằm trong release register; những cổng chưa thực hiện ghi NOT_CHECKED, không ghi pass.


## Bổ sung ngày 20 tháng 10 năm 2026

Những câu mô tả không truy cập Mac/tool lỗi ở trên là ghi nhận lịch sử11/10. Ngày20/10 đã xác minh repo mới trong Life-Code-OS, remote main/plan, bảo toàn checkout phase dirty và nhập đủ149 tệp. Label cũ được normalize trong EVIDENCE_LEDGER; deployment và approval vẫn BLOCKED. Xem BASELINE_LOCK.json.


---

# P0: chặn rủi ro trong 48–72 giờ và bảo toàn chứng cứ

Mã tài liệu: **D03** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Incident Commander + Backend + Security. Nguồn đối chiếu: G04, G05, G06, G07, G08, G11, S07, S08. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Thẩm quyền và giới hạn
Đây là runbook đề xuất, không phải lệnh đã thực hiện. Chủ trì P0 phải được chỉ định; duyệt danh sách môi trường và kênh liên lạc. Không thực hiện dò ID người thật, trích hồ sơ production hoặc truy cập dữ liệu bằng token không thuộc mình. Mốc 48–72 giờ là mục tiêu chặn rủi ro, không phải thời gian xây xong toàn bộ hệ danh tính.
## 2. Trình tự
### Trình tự phụ thuộc hiện hành ngày 20/10/2026

Trình tự dưới đây thay thứ tự tuần tự ngầm của backlog 11/10 nhưng không thay quyền thực hiện. P0-01 phải chốt scope, môi trường, người chỉ huy và authority trước. P0-08 xác minh clean clone, remote, branch, full SHA và tính toàn vẹn nguồn ngay sau P0-01. Chỉ sau baseline này, P0-02 mới lập inventory bề mặt/runtime; P0-03 bắt đầu containment server-side. Từ control point đó, P0-04 thu hồi luồng danh tính cũ; P0-05 khóa Engine Lab; P0-06 cách ly output legacy; P0-07 bảo toàn/phân loại dữ liệu có thể chạy theo dependency ghi trong `P0_PACKET/03_PATCH_PLAN.csv`; P0-09 dựng và quét artifact allowlist từ clean baseline. P0-10 là bước cuối, phụ thuộc P0-03/04/05/06/07/09 và vẫn cần approval production gắn exact SHA/artifact/environment/rollback.

Mốc 48–72 giờ chỉ là mục tiêu phản ứng cho **containment subset đã được cấp quyền** khi đã có Incident Commander, clean baseline, quyền provider và đủ người thực hiện. Đây không phải lời hứa hoàn tất cả mười task, phân loại dữ liệu, independent review, deploy provider và rollback evidence trong 72 giờ. Khi chưa có authority/capacity thật, effort vẫn là planning range và có thể phải giữ static maintenance thay vì deploy.

### Các dải giờ phản ứng lịch sử

Các dải giờ sau mô tả nhịp phản ứng mong muốn, không ghi đè dependency hiện hành hoặc tự cấp quyền production.

Trong 0–4 giờ: ghi domain, Workers route, Pages preview, bindings, queue, storage và phiên bản deploy có thể truy cập. Bảo toàn bản source và bằng chứng tối thiểu ở kho riêng tư. Không commit PII vào GitHub public.
Trong 4–12 giờ: chặn server-side các route profile/report/session legacy chưa an toàn; khóa mọi đường vòng workers.dev, preview, custom domain và tác vụ nền. Có thể trả trạng thái dịch vụ tạm ngưng với mã lỗi an toàn. `noindex`, CORS và việc ẩn Engine Lab không thay authentication.
Cùng thời gian: dừng cấp session theo client user_id; vô hiệu token legacy; dừng intake ảnh, trẻ em, sức khỏe và thanh toán báo cáo sâu. Hạ nội dung chỉ số và cảnh báo giả về trạng thái nghiên cứu. Không xóa chứng cứ trước khi đánh giá sự cố.
Trong 12–36 giờ: tái hiện bằng hai tài khoản tổng hợp ở staging; viết negative tests; kiểm tra old token, ID chéo, result ID chéo, grant vừa bị thu hồi và job còn trong queue. Bản vá tối thiểu phải giới hạn phạm vi để dễ kiểm tra.
Trong 36–72 giờ: deploy bản đã duyệt, giữ receipt, kiểm tra bên ngoài ở các bề mặt allowlisted. Nếu chưa sửa chắc, duy trì chế độ giới thiệu/bảo trì thay vì mở lại vì áp lực lịch.
## 3. Điều kiện kết thúc
Tất cả route intake nguy hiểm đã bị chặn hoặc sửa có kiểm thử; phiên cũ bị từ chối; không còn đầu ra số phận giả lập trong phạm vi public; source/artifact/runtime được liên kết; dữ liệu legacy có chủ trì xử lý; đã định nghĩa rollback an toàn. Bản rollback không được chứa lại lỗi gốc. Chưa có bản an toàn thì rollback về trang tĩnh không nhập dữ liệu.
## 4. Lưu ý về tài khoản legacy
Tên, ngày sinh hoặc ID cũ không đủ khôi phục quyền sở hữu. Session cấp bởi luồng cũ không tự là bằng chứng quyền hợp pháp. Phân loại hồ sơ chưa rõ quyền; chỉ chuyển khi có quy trình xác minh phù hợp. Không tự gán email mới cho hồ sơ dựa vào việc người dùng biết thông tin phổ biến.
## 5. Biên bản bắt buộc
Mỗi hành động ghi thời điểm UTC, người thao tác, môi trường, request/change ID, tác động, bằng chứng và người duyệt. Nhật ký kỹ thuật chỉ giữ thông tin cần thiết; báo cáo công khai không chứa payload người dùng. Cửa đóng P0 do kỹ thuật, bảo mật và người có thẩm quyền sản phẩm cùng quyết định, không dựa vào một lần `/health` trả 200.


## Bổ sung ngày 20 tháng 10 năm 2026

P0 được tách thành containment code, negative tests, rollout receipt và incident/data review. Auth source đã xác nhận thiếu owner checks tại baseline; chưa có runtime exploit hoặc breach receipt. Xem SECURITY_AND_PRIVACY_ACCEPTANCE.md.


---

# Life Code OS: tầm nhìn, giới hạn và cấu trúc hợp nhất

Mã tài liệu: **D01** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Founder + Product Lead. Nguồn đối chiếu: G02, S01, S02. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Quyết định kiến trúc
Life Code là nền tảng tự hiểu và thiết kế đời sống. Huyền Nhân Học giữ triết lý và ngôn ngữ tổng hợp của Trần Hà Tâm; Life Code OS giữ dữ liệu, phương pháp, quyền và sản phẩm; Đồng nhịp sống đọc quan hệ giữa cá nhân với môi trường; hệ hành động biến nội dung thành lựa chọn có thể xem lại. AI là công cụ hỗ trợ, không phải nguồn dữ kiện độc lập về con người.
Bộ này giữ chín cấp sản phẩm, mười hai lớp và bốn phần Identity–Analysis–Timeline–Action đã công bố. Bổ sung đường vào miễn phí, không gian chuyên gia, tổ chức, đào tạo, xuất bản/API và cấp phép quốc tế. Mỗi dòng có hợp đồng riêng. Không gọi 12×12 ô liên hệ là 144 năng lượng đo được; không gọi 120 trường dữ liệu là 120 năng lực bẩm sinh đã xác nhận.
## 2. Giá trị dành cho người dùng
Người dùng bắt đầu bằng một nhu cầu thực: hiểu một lựa chọn, tổ chức công việc, theo dõi nhịp sống hoặc xây kế hoạch. Hệ trả dữ liệu đã dùng, phần chưa biết, cách tính, câu hỏi và bước hành động. Họ có thể phản bác nhận định, sửa dữ liệu, rút chia sẻ hoặc rời dịch vụ mà không bị đe dọa bởi nhãn số xấu.
Một hồ sơ là tài sản do người dùng kiểm soát theo quyền hợp pháp, không phải hàng hóa để bán lại. Nhà sáng lập sở hữu phần sáng tạo và quyền thương hiệu được xác lập; không sở hữu cuộc đời, dữ liệu riêng tư hoặc quyền lựa chọn của khách hàng.
## 3. Phạm vi sản phẩm đầu tiên
Sau containment và Trust Core: người trưởng thành tự tạo hồ sơ; công cụ số minh bạch; Level 1; nhật ký mục tiêu không lâm sàng; kế hoạch 30 ngày; PDF/Word có phiên bản. Free Essentials là lõi hữu ích thực sự, không phải một trang hù dọa để dẫn mua bản trả phí. Giai đoạn đầu không thu ảnh mặt/tay/chân, dữ liệu bệnh, hồ sơ trẻ hoặc thông tin người thứ ba.
Các lĩnh vực sâu không bị xóa khỏi tầm nhìn. Chúng nằm trong registry với trạng thái nghiên cứu, nguồn và điều kiện mở. Một chương trình có thể hoàn tất về thiết kế trong khi phương pháp cụ thể vẫn chưa đủ điều kiện phát hành.
## 4. Đầu ra nghiệm thu
Chuỗi trải nghiệm phải chạy trọn: chọn nhu cầu → giải thích dữ liệu cần dùng → xác nhận hồ sơ → tính phương pháp đã duyệt → đọc báo cáo → chọn hành động → ghi kết quả → cập nhật. Không coi chọn được Level 9 trên giao diện là sản phẩm Level 9 đã có. Mỗi lần xuất phải chỉ ra product release, profile version, method releases và quyền đã kiểm tra.
## 5. Định vị và lời công bố
Lời công bố đề xuất: “Hiểu dữ liệu của mình, khám phá những góc nhìn có nguồn và xây hành động phù hợp với đời sống.” Không dùng “gần như tuyệt đối”, “mở khóa mọi bí mật”, “biết tâm can từ ảnh” hoặc “không cần kiểm chứng”. Những câu này không phải cơ sở phát hành hay cơ sở định giá.

## Bổ sung thực thi 2026-10-20
Tầm nhìn trên được giữ nguyên. Điều kiện stage, success/kill metric, authority, chi phí và decision packet được chuẩn hóa tại `07_PRODUCT_EXECUTION_CHARTER_2026-10-20.md`; 23 product ID được đối chiếu một-một trong `PRODUCT_EXECUTION_EXTENSION.json/.csv`. Bổ sung này có trạng thái evidence `NOT_CHECKED` và không tự mở release.


---

# Chuỗi sản phẩm từ miễn phí tới doanh nghiệp và đối tác

Mã tài liệu: **D04** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Product + Finance + Support. Nguồn đối chiếu: G02, S02. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Danh mục thương mại độc lập với cấp nội dung
Level là độ sâu một phạm vi, không phải bậc giá cố định. Catalog có các dòng: Guest Tools, Free Essentials, Personal Growth, Expert Review, Practitioner Studio, Academy, Organization Workspace, Publisher/API và Regional Partner. Người dùng không cần mua đủ các cấp không liên quan để tiếp cận một mục tiêu.
## 2. Free Essentials: hữu ích ngay nhưng kiểm soát chi phí
Guest Tools tính đuôi bốn số hoặc minh họa tên tại thiết bị; không bắt tạo tài khoản và không gửi nội dung nhập vào analytics. Không tuyên bố không có bất cứ metadata mạng nào: hạ tầng có thể có log kết nối theo chính sách. Với tài khoản miễn phí sau Trust Core: một hồ sơ tự quản, một mục tiêu đang hoạt động, nhật ký văn bản theo giới hạn dung lượng, thư viện phương pháp công khai, bản Snapshot ngắn và quyền tải/xóa dữ liệu. Giới hạn sử dụng phải minh bạch; chức năng xuất dữ liệu riêng tư không bị đặt sau paywall.
Đề xuất hạn mức AI ban đầu là 10 lượt giải thích ngắn/tháng, một yêu cầu cùng lúc, giới hạn output và ngân sách tài khoản. Đây là tham số thử nghiệm trong catalog, không phải giá hoặc quota đã công bố. Khi hết ngân sách, vẫn cho xem hồ sơ, phép tính xác định và kế hoạch; không làm mất dữ liệu hay dùng lời hù dọa để bán thêm.
## 3. Các gói trả phí
Personal Growth mở report theo phạm vi, lưu bản cập nhật và công cụ theo dõi sâu hơn. Expert Review thêm một phiên người thực hành rà soát: số lượt, thời lượng, trách nhiệm, lịch hẹn, hủy và hoàn tiền phải rõ. Practitioner Studio cấp seat, case management và template, không cấp quyền đọc mọi khách hàng của hệ.
Workspace bán công cụ phối hợp mục tiêu, năng lực có minh chứng và cách làm việc. Không bán xếp hạng nhân viên theo số mệnh. Tổ chức không mặc nhiên xem dữ liệu sức khỏe, tín ngưỡng, quan hệ hoặc nhật ký cá nhân dù họ thanh toán tài khoản.
## 4. Cơ chế mở khóa
Eligibility gồm entitlement, subject access, purpose/lawful basis, method release, input readiness, market và age rules. Mỗi điều kiện thất bại có reason code và cách xử lý. “Chưa có ngày sinh” không chặn một công cụ lập kế hoạch không dùng ngày sinh. “Đã mua” không biến dữ liệu thiếu thành đủ.
## 5. Nghiệm thu
Mỗi SKU chỉ tới product release bất biến. Người mua xem phạm vi, dữ liệu cần, định dạng, số lần sửa, hạn dùng, giá thuế/phí và policy trước trả tiền. Payment success, entitlement active, report ready là ba trạng thái khác. Không định giá bằng độ may mắn, nhãn Hung hoặc số trang được AI kéo dài.

## Bổ sung thực thi 2026-10-20
Chuỗi 23 sản phẩm, train mở dần, surface responsive/PWA, decision/gate và success/kill metric được ghi tại `07_PRODUCT_EXECUTION_CHARTER_2026-10-20.md` và `PRODUCT_EXECUTION_EXTENSION.*`. Tiền tệ, mức giá và loaded rate vẫn chờ Q14/Q15/Q20; thiếu input không được ghi thành 0.


---

# Hợp đồng chín cấp Life Code và cách trưởng thành hồ sơ

Mã tài liệu: **D05** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Product + Method Council. Nguồn đối chiếu: G03, S02. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Giữ tên, sửa điều kiện và đầu ra
L1 Self Signal: tên/ngày sinh theo phương pháp tự chọn, mục tiêu và phạm vi. Trả dữ liệu gốc, phép tính, chủ đề tự quan sát, phần chưa biết và hành động 30 ngày; không tự gán bẩm sinh đã xác minh.
L2 Inner Architecture: nhu cầu, giá trị, vai trò và 3–5 tình huống do người dùng kể. Trả bản đồ xung đột và lựa chọn, có câu xác nhận/không phù hợp; không “đọc tâm can” từ ảnh.
L3 Behavior Code: nhật ký và bảng hỏi phù hợp. Trả hành vi theo bối cảnh, mức duy trì và thử nghiệm thay đổi, không chẩn đoán lâm sàng.
L4 Work & Wealth: kỹ năng, lịch sử làm việc, mục tiêu và nguồn lực. Trả so sánh vai trò, dòng tiền và kịch bản giả định; không khuyến nghị đầu tư từ chu kỳ số.
L5 Relationship Field: nhu cầu, thỏa thuận, xung đột được kể và quyền chia sẻ từng bên. Trả kế hoạch đối thoại; không phán chung thủy hoặc định mệnh hôn nhân.
L6 Life Timeline: sự kiện thật có thời gian/nguồn, symbolic cycles tách riêng, kế hoạch và scenarios. Tương lai trống được giữ trống; 0–99 là khoảng tuổi, không tuổi thọ.
L7 Body Intelligence: chỉ mô tả hình thái và nhật ký môi trường được phép; cần thẩm định riêng. Không suy hormone, đạo đức hoặc bệnh từ tay/mặt.
L8 Mission Path: giá trị tự chọn, năng lực có minh chứng, hướng phụng sự muốn thử, trách nhiệm và nguồn lực. Trả vài phương án và kế hoạch 90 ngày; không thiên mệnh duy nhất.
L9 Full Life Code: hợp nhất các phần đã được phép và dữ liệu liên quan; loại lặp, chỉ ra khác biệt giữa phiên bản và bàn giao hệ hành động. Full là đầy đủ theo phạm vi, không biết tất cả bí mật.
## 2. Đồ thị thay cho chiếc thang
L4 cần dữ liệu công việc và mục tiêu; không bắt mua L5. L8 không cần ảnh chân. Một hồ sơ L9 có thể có L7 “không sử dụng”; chỉ rõ nguyên nhân, không trừ điểm phẩm chất. Người dùng được quyền từ chối trường hợp nhạy cảm mà vẫn dùng phần không liên quan.
## 3. Nội dung và trang
Ngân sách biên tập giữ tham chiếu cũ: L1 30–50; L2 40–60; L3 50–70; L4/L5 50–80; L6 60–100; L7 60–120; L8 80–150; L9 150–600. Đây không phải yêu cầu filler hoặc bằng chứng độ chính xác. Nội dung cá nhân, hướng dẫn chung, bảng tra, bài tập và nguồn phải có nhãn phân biệt.
## 4. Mỗi cấp phải có năm dạng đầu ra
Một summary đọc trong ba phút; các phần thuyết minh có căn cứ; bảng phép tính/quan sát; action plan; change log từ lần trước. Template không tự ép một số lượng risk hoặc strengths khi không có dữ liệu. Phần không có bằng chứng trả lời “chưa có dữ liệu để nhận định”, kèm lựa chọn bổ sung phù hợp.
## 5. Nghiệm thu
Dữ liệu đầu vào mới phải làm thay đổi những phần được phép, không làm đảo toàn bộ báo cáo ngẫu nhiên. Khi chỉ sửa cách viết tên, lịch sử sự kiện không được đổi. Khi mất entitlement, người dùng vẫn có quyền tiếp cận dữ liệu cá nhân theo chính sách và nghĩa vụ; không dùng việc khóa sản phẩm để khóa quyền chủ thể.

## Bổ sung thực thi 2026-10-20
Hợp đồng input, vai trò AI, reviewer, rejection và fixture khác nhau cho từng cấp nằm tại `../06_AI_Bao_cao/06_NINE_LEVEL_AI_REPORT_CONTRACTS_2026-10-20.md` và `NINE_LEVEL_REPORT_CONTRACTS.*`. Ngân sách trang vẫn là biên biên tập, không phải chỉ tiêu filler.


---

# Hành trình người dùng, trạng thái trống và tiêu chí giá trị

Mã tài liệu: **D06** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: UX Lead + QA. Nguồn đối chiếu: Yêu cầu của Nhà sáng lập và thiết kế đề xuất trong bộ này. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Người mới miễn phí
Trang đầu đưa ba lối: tìm hiểu phương pháp, thử công cụ không lưu hồ sơ, hoặc xây kế hoạch. Chọn công cụ số thì chỉ hỏi dữ liệu phép tính cần. Kết quả có “cách tính”, “nguồn bảng” và “điều kết quả không nói”. CTA tiếp theo là ghi một câu hỏi hoặc mục tiêu, không phải mua để tránh vận xấu.
## 2. Người tạo hồ sơ cá nhân
Trước nhập, chọn ai là chủ thể và mục đích. Trong beta chỉ cho “chính tôi, từ 18 tuổi”; ủy quyền và trẻ em chưa mở. Bản nháp có thể lưu; ngày sinh cho phép không biết giờ. Người dùng thấy từng dữ kiện gắn tự khai/đã xác nhận/giả thuyết. Trước chạy, màn hình xác nhận phạm vi và những phần không thể thực hiện.
## 3. Người nhận báo cáo
Report bắt đầu bằng mục tiêu, điều đã biết và một hành động. Các claim có thể bung để xem dữ liệu/cách tính. Bên cạnh nhận định có phản hồi “đúng với tình huống”, “không phù hợp”, “cần sửa dữ kiện”; phản hồi không tự huấn luyện engine. Bản report đã phát hành giữ nguyên snapshot, chỉnh sửa tạo phiên bản khác.
## 4. Người làm với chuyên gia
Chọn practitioner theo năng lực, ngôn ngữ và phạm vi; xem lịch, phí và quy tắc. Chia sẻ chỉ những phần cần cho ca. Trước buổi hẹn, chuyên gia chỉ thấy phần đã cấp. Sau buổi, ghi chú phân biệt khách hàng nói và chuyên gia đề xuất. Hết ca hoặc thu hồi grant chặn truy cập mới; file đã tải không thể được hứa thu hồi vật lý.
## 5. Người thuộc tổ chức
SSO có thể cho đăng nhập workspace, không tự cấp quyền vào nhật ký cá nhân. Màn hình luôn chỉ rõ đang ở vùng cá nhân hay công việc. Quản lý nhìn mục tiêu đã chia sẻ và kết quả cộng tác; không thấy thần số, quan hệ riêng hoặc nội dung tự thuật không thuộc công việc. Không có bảng xếp hạng nhân viên theo LCI.
## 6. Trường hợp lỗi và khả năng tiếp cận
Input invalid chỉ lỗi ngay field, không xóa form. Job lâu có progress và lựa chọn xem lại, không spinner vô hạn. Thiếu quyền trả thông báo không lộ sự tồn tại của hồ sơ khác. Thanh toán đang chờ không hiện đã cấp dịch vụ. Báo cáo thiếu dữ liệu phải rõ hơn chứ không trắng hoàn toàn. Mạng gián đoạn giữ draft được phép, có TTL và nút xóa; không cache nội dung riêng trong service worker mặc định.
## 7. Đánh giá giá trị
Pilot theo dõi tỷ lệ hiểu được khác biệt dữ kiện/biểu tượng, số người chọn được hành động, tỷ lệ hoàn thành tự khai và lỗi cần sửa. Không lấy đánh giá “thấy đúng” làm bằng chứng tiên đoán. Chỉ thu analytics dạng sự kiện có whitelist; không gửi trường form, report text, mã số hay câu hỏi riêng vào sự kiện sản phẩm.

## Bổ sung thực thi 2026-10-20
Mười hai luồng demo synthetic và adverse path được định nghĩa tại `../05_Frontend_UI/05_DEMO_USABILITY_FLOWS_2026-10-20.md`. Mỗi luồng phải có phone/desktop, keyboard/screen-reader và recovery evidence; video hoặc happy path đơn lẻ không đủ nghiệm thu.


---

# Học thuyết HNH và ngữ pháp đời sống có cấu trúc

Mã tài liệu: **D07** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Founder + Method Council. Nguồn đối chiếu: Yêu cầu của Nhà sáng lập và thiết kế đề xuất trong bộ này. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Hạt nhân được bảo toàn
Tư tưởng của Nhà sáng lập xem con người trong quan hệ với nghề, gia đình, tên gọi, thời gian, thiên nhiên và môi trường. Điều “ăn quanh nhà, sống quanh nơi làm” được lưu như định hướng thiết kế đời sống, không tự là quy luật chữa bệnh. Tu tập là thực hành quan sát, giới hạn, học hỏi, trách nhiệm và buông dính mắc; không bắt người dùng theo tôn giáo, tin tiền kiếp hoặc lệ thuộc thầy.
## 2. Code là cấu trúc quan hệ
Hồ sơ Life Code gồm dữ kiện nhận diện, hồ sơ sinh, bản đồ biểu tượng, quan sát theo thời gian, bối cảnh, nhật ký đồng nhịp, hành động và nguồn. Không nén mọi thứ thành một căn số hoặc một điểm người. Một phát hiện đúng từ nhật ký có giá trị mà không cần “trùng” tử vi. Một bảng tượng nghĩa có thể được đọc như văn hóa ngay khi chưa có khả năng dự báo.
## 3. Sáu quan hệ sáng tạo HNH
Nuôi dưỡng: điều gì hỗ trợ một hành động hoặc giá trị? Cản trở: ràng buộc nào đã quan sát? Bù đắp: năng lực/người/công cụ nào có thể giúp? Xung đột: hai trách nhiệm hoặc giá trị nào không thể tối ưu cùng lúc? Chuyển tiếp: điều kiện nào đang thay đổi? Lựa chọn: phương án nào có thể thực hiện trong phạm vi hiện tại?
Mỗi quan hệ phải ghi nguồn và loại: biểu tượng, tự thuật, quan sát hay suy luận có điều kiện. Không chuyển “tương sinh” thành nhân quả sinh học. Không dùng ba công cụ cùng nhận ngày sinh để nói có ba nguồn độc lập xác nhận.
## 4. Cách thuyết minh
Từ bối cảnh thật, nêu vấn đề người dùng muốn giải quyết. Nếu có biểu tượng, giới thiệu như góc nhìn tham khảo. Đưa câu hỏi có thể trả lời “không phù hợp”. Chỉ khi người dùng cung cấp ví dụ mới chuyển sang kế hoạch. Ngôn từ rõ ràng, không gán “năng lượng thấp”, “khắc vợ”, “trẻ khó dạy”, “người không có phúc”.
Một đoạn đạt chuẩn: “Anh tự ghi nhận ba cam kết chậm trong tháng. Hướng xem lại là tải việc và quyền từ chối. Bảng số có chủ đề trách nhiệm, nhưng đề xuất giảm một cam kết được xây từ lịch thực tế, không từ căn số.”
## 5. Kế thừa và trách nhiệm
Ghi nhận Trần Hà Tâm là người sáng lập và chủ trì HNH theo khai báo. Các tư tưởng, mã nguồn, nội dung nguyên bản có thể được quản lý quyền. Bảng tra, bản dịch và phương pháp có nguồn khác không được đổi tên để xóa nguồn. Council giữ sổ bất đồng; người phản biện không bị loại vì kết quả nghiên cứu không như kỳ vọng.


---

# 20 họ tri thức: cách khảo cứu, tích hợp và phát hành

Mã tài liệu: **D08** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Research Lead + Linguists + Method Council. Nguồn đối chiếu: G02, S15, S16, S38, S39. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Phạm vi mở, tiến độ phải hữu hạn và có trạng thái
Registry bao phủ K01 lịch pháp; K02 Bát tự; K03 Tử vi; K04 Dịch học; K05 Tam thức/trạch nhật; K06 phong thủy/Vastu; K07 Jyotish/Nadi; K08 chiêm tinh phương Tây; K09 lịch khu vực; K10 thần số/Psychomatrix; K11 dãy số; K12 danh học; K13 hình thái; K14 chiêm nghiệm; K15 hệ tổng hợp hiện đại; K16 triết học/nội tâm; K17 đo lường cá nhân; K18 hành vi/nghề/xã hội; K19 sinh hoạt/môi trường; K20 toán/dữ liệu/AI.
Có registry không đồng nghĩa đã đọc mọi sách. Từng bản thảo và bản dịch mang trạng thái riêng: identified, metadata_read, excerpt_read, full_text_read, rules_extracted, calculation_checked, product_permitted. Không ghi “nghiên cứu toàn thế giới đã xong”.
## 2. Quy trình sách và đa ngôn ngữ
Ghi bìa, tác giả/biên soạn, ISBN nếu có, lần in, năm, nguồn truy cập và quyền. Ảnh bìa không đủ xác nhận nội dung nâng cao. Văn bản quét cần đối chiếu bằng người đọc ngôn ngữ; OCR chỉ là bước hỗ trợ. Giữ trang gốc, bản chép, bản dịch sát, chú giải và bản thuyết minh HNH riêng.
Hai bản dịch cùng nguồn không tính thành hai bằng chứng. Thuật ngữ như khí, mệnh, linh hồn, năng lượng, từ trường phải ghi nghĩa trong nguồn; không mặc nhiên là đại lượng vật lý. Bảng tên Latin, Hán tự, Abjad và Gematria dùng adapter riêng; không áp bảng A–Z lên mọi hệ chữ.
## 3. Đặc tả quy tắc
Mỗi method passport có ID, family, input/output schema, configuration, zero/null behavior, độ chính xác thời gian, version bảng, ví dụ gốc, điều kiện không áp dụng, claim được phép và phê duyệt. Luật trùng/khác ghi vào contradiction ledger. Không chọn cách luận thuận lợi để hợp kết quả mong muốn.
## 4. Hai chương trình kiểm tra độc lập
Reproduction kiểm tra tính đúng phương pháp bằng ví dụ và trường hợp biên. Outcome evaluation kiểm tra giá trị ứng dụng hoặc dự báo trên mục tiêu xác định. Pass chương trình đầu không tự pass chương trình sau. Dữ liệu nổi tiếng dễ bị rò thông tin tiểu sử, thiên lệch chọn mẫu và hậu nghiệm; không dùng làm bộ chuẩn duy nhất. Nếu nghiên cứu, khóa dữ liệu trước thời điểm dự báo, giữ holdout và baseline không dùng biểu tượng.
## 5. Phát hành từng phương pháp
Candidate paid beta chỉ gồm phép tính lịch/tên/số rõ, bảng nghĩa đủ quyền, nội dung phản tư đã duyệt và hành động không lâm sàng. Bát tự, Nadi, hình thái và các hệ phức tạp vẫn có chỗ trong registry nhưng chưa mở tự động nếu thiếu nguồn hoặc quy tắc. IPIP và O*NET là đầu mối công cụ có cấu trúc, không tự chứng minh bản dịch mới đã đo đúng người Việt.

## Amendment 2026-10-20 — readiness, nguồn và quyền

1. Danh mục K01–K20 chỉ chứng minh taxonomy đã được đặt tên; không chứng minh đã có method, source, rights, implementation, test hay product approval. Trạng thái từng family phải đọc từ `METHOD_FAMILY_READINESS.json`.
2. Mỗi bản phát hành phải tách `computation_kind`, `evidence_class` và `release_state`. Tính tái lập của phép tính không được nâng thành bằng chứng dự báo hay quyền thương mại.
3. `source_id` chỉ hợp lệ khi tra được trong `SOURCE_RIGHTS_REGISTER.json`. Thiếu edition/page, full-text review, license/permission receipt hoặc phạm vi sử dụng thì giữ `unknown`/`pending`; không suy `permitted` từ việc người dùng cung cấp bảng.
4. Mọi method phải liên kết bằng ID tới field đầu vào, formula/rule version, result contract, source-rights receipt, golden/negative cases và product/country scope. Chuỗi mô tả tự do không thay các liên kết này.
5. Family hoặc method không đủ bằng chứng mặc định `research_only` hoặc `blocked`; không có fallback tự sinh diễn giải. Chỉ Founder/Method Council theo gate hiện hành mới có thể nâng `release_state` trên đúng artifact digest.


---

# Chương trình nghiên cứu chuyên sâu K01–K20 và cách tạo Code HNH

Mã: **D37** | Phiên bản: **2026-10-11.r1** | **ĐỀ XUẤT / CHỜ PHÊ DUYỆT**

Chủ trì: Method Council + Ngôn ngữ + Data Science. Nguồn đã tiếp cận: G02, S15, S16, S38, S39. Các nhóm văn bản khác bên dưới là danh mục cần nghiên cứu, không được hiểu là đã đọc toàn văn.


## Mục tiêu và trạng thái
Đây là bản thiết kế nghiên cứu theo từng họ, không tuyên bố đã sở hữu tri thức tất cả các nền văn minh. Mỗi nhóm có hai đường: tái lập phương pháp đúng nguồn và tìm giá trị ứng dụng phù hợp. Không suy rằng tái lập đúng phép tính đồng nghĩa giải mã chính xác kiếp người. Học thuyết HNH có thể giữ ngôn ngữ triết lý, nhưng engine phải phân biệt biểu tượng với dữ kiện.
## K01. Thời gian và lịch
Khóa loại lịch gốc, vùng địa lý, timezone lịch sử, độ chính xác giờ và quy tắc quy đổi. Thiếu địa điểm không tự dùng timezone Việt Nam cho mọi hồ sơ. Tách ngày dân dụng, ngày theo phương pháp và giờ Mặt Trời khi trường phái yêu cầu. Mỗi lần quy đổi lưu tzdb/library version và các giả định. Golden corpus phải có ngày nhuận, ranh giới nửa đêm, giờ trùng/không tồn tại khi chuyển giờ mùa hè và dữ liệu chỉ có năm. Đây là phần nền có thể tính chính xác hơn qua đặc tả, không tạo ra prediction về con người.
## K02. Bát tự/Tứ trụ
Nghiên cứu nguồn và chú giải trước khi khóa cách an bốn trụ, ranh giới năm/tháng/ngày, giờ sinh và khởi vận. Các cách dùng nguyệt lệnh, tàng can, vượng–suy, dụng thần, hợp–xung–hình–hại phải có adapter riêng. Một cấu hình không được dùng ưu điểm của trường phái A rồi lặng lẽ đổi sang B khi lời luận không khớp. Corpus gồm cùng dữ liệu nhưng khác cấu hình để người dùng thấy khác biệt. Không chuyển “Mộc vượng” thành hormone, bệnh hoặc năng lực lãnh đạo.
## K03. Tử vi và mệnh bàn
Đặc tả thứ tự an cung/sao, các quy tắc tháng nhuận, cách tính tuổi và hệ hạn theo edition. Giữ tên thuật ngữ nguồn, chữ gốc và bản dịch. Dùng bản đồ lĩnh vực như chất liệu tự soi chiếu, không tự đếm anh chị em, con cái hoặc viết quá khứ. Những nhánh Hà Lạc/Thiết Bản, nếu tiếp nhận, có method ID và input riêng. Nhiệm vụ nghiên cứu là làm rõ khác biệt của sơ đồ, không ép mọi mệnh bàn thành cùng một Life Code Index.
## K04. Kinh Dịch và các cách lấy quẻ
Tách nghiên cứu văn bản với gieo quẻ. Lưu câu hỏi, thời điểm, cách tạo quẻ, hào động và quy tắc quẻ biến. Randomness nếu dùng để tạo quẻ phải công khai và không mô tả là dữ liệu vận mệnh. Mai Hoa, Lục Hào và chú giải Chu Dịch là các phương pháp liên quan nhưng không dùng chung rules mặc định. HNH có thể tạo sáu câu hỏi tình huống: đang hình thành gì, đang vướng gì, hỗ trợ nào có thật, lựa chọn nào có thể thử, giới hạn nào cần giữ và khi nào xem lại.
## K05. Tam thức và trạch nhật
Kỳ Môn, Lục Nhâm, Thái Ất cùng hệ chọn thời điểm cần schema khác nhau. Khóa điều kiện lịch, phương pháp lập cục và bảng nguồn; thử các thời điểm biên và sai số đầu vào. Luận thời điểm nằm trong symbolic track, bên cạnh lịch thực, nguồn lực, thời hạn và an toàn. Không khuyên trì hoãn khám bệnh, bỏ nghĩa vụ pháp lý hoặc giao dịch quan trọng chỉ vì thời điểm biểu tượng. Sản phẩm phát hành sau nguồn đầy đủ và nội dung phù hợp.
## K06. Phong thủy/Vastu và nơi sống
Tách hình thế, hướng đo, bảng phương vị, thời điểm xây/sửa theo từng trường phái. Ghi phương pháp đo hướng, thiết bị, sai số và phiên bản mặt bằng. Song song là quan sát thực: ánh sáng, tiếng ồn, thông khí, an toàn, riêng tư, access và đi lại. Bản HNH có thể giúp người dùng lựa chọn cách bố trí trong ngân sách, nhưng không gọi căn nhà là nguyên nhân chắc chắn của bệnh/tai nạn hoặc buộc mua vật phẩm.
## K07. Jyotish và Nadi
Tạo adapters cho hệ hoàng đạo, ayanāṃśa, nhà, phân đồ và chu kỳ được nguồn quy định. Bảng thuật ngữ giữ Sanskrit và bản dịch, có review ngôn ngữ. Phương pháp tính gọi là Nadi khác việc xác thực một bản thảo lá cọ dành cho người cụ thể. Không dựng văn bản lá Nadi từ tên/ngày sinh rồi trình bày như cổ bản tìm được. Quyền số hóa/dịch bản thảo và nguồn lưu trữ cần xác nhận.
## K08. Chiêm tinh phương Tây
Tính vị trí thiên thể là một loại tính toán; suy luận tâm lý từ vị trí là loại nhận định khác. Khóa hệ nhà, hệ hoàng đạo, orb, vị trí địa lý và time standard trong release. Golden fixtures cần có đối chiếu với nguồn ephemeris được cấp phép và các trường hợp vùng cực/giờ sinh thiếu. Trình diễn lá số không phải chứng nhận một người có tính cách cố định. Lời giải thích phải có mode biểu tượng được người dùng lựa chọn.
## K09. Lịch và truyền thống khu vực
Tây Tạng, Nhật, Hàn, Thái, Myanmar, Weton/Pawukon và lịch Maya cần researcher/người bản ngữ phù hợp. Không gộp các truyền thống vào một bảng “Đông–Tây chung”. Kiểm tra lịch dùng, bối cảnh văn hóa và cách cộng đồng mong muốn tri thức được sử dụng. Có lịch ngày không có nghĩa có quyền luận mọi người bằng nó. Product locale được duyệt độc lập với nguồn nghiên cứu locale.
## K10. Thần số và Psychomatrix
Bảng chữ–số, thứ tự cộng, giữ master numbers, cách tạo working numbers và cách lập chu kỳ phải được ghi đủ. Giữ cả số trung gian và căn rút gọn để so sánh. Hai phương pháp cùng trả3 không có nghĩa lời luận cùng được chứng minh. Không dùng thiếu3/4/9 để gán kém logic, sức khỏe yếu hoặc trí nhớ kém; không suy nghề/lãnh đạo/tình dục từ chart. Một Psychomatrix chưa khóa variant phải trả method_not_supported, không viết bảng theo trí nhớ.
## K11. Bộ số định danh
Mã đuôi80 có hàm dư rõ nhưng bảng nghĩa và quy tắc0 cần phiên bản. Bát Cực phân loại cặp chồng lấn, số0/5 và chuỗi, không thể thay bằng digital root. Phone số quốc tế/nội địa phải có normalization policy và giữ raw form; kết quả khác do ký hiệu không được gọi là “tần số vật lý”. Kiểm thử đồng hạng, cùng đuôi, duplicatepairs và chữ viết không rõ. Cấm thu mật khẩu/PIN/OTP; chỉ bốn số cuối khi method cần như vậy.
## K12. Tên và ngôn ngữ
Tên gốc, chữ gốc nếu có, cách phát âm, nguồn gia đình và ý nghĩa tự nhận là những trường riêng. Không tự biến họ Trần thành “bụi trần” hoặc tên Hà thành “sông” như định nghĩa chắc chắn. Name semantics phải cho nhiều khả năng và câu hỏi xác nhận. Transliteration phụ thuộc ngôn ngữ; không dùng bảng Latin làm phép phổ quát cho Trung/Nhật/Ả Rập. Kiểm thử ký tự ghép, dấu, thứ tự họ/tên và đổi tên có lịch sử.
## K13. Hình thái
Ảnh trước hết là dữ liệu cần consent và chất lượng. Lưu camera condition, bên trái/phải, xoay, che khuất, blur và phép đo. Các dấu hiệu như nếp gấp, hướng ngón hoặc cấu trúc hình học được mô tả; không gán tính cách, bệnh, đạo đức, tài lộc, giới hay phẩm chất. Thư viện tướng học truyền thống nếu dùng chỉ ở khu giáo dục có nhãn, không tạo lời phán riêng về người trong ảnh. Level 7 phải qua thẩm định riêng.
## K14. Chiêm nghiệm biểu tượng
Tarot, Rune, Ifá, giải mộng và các công cụ kể chuyện có phương pháp và bối cảnh văn hóa riêng. Lưu người tạo biểu tượng, phương pháp chọn, câu hỏi và cách người dùng diễn giải. Không kết luận người thứ ba đã ngoại tình, có ác ý hoặc sắp chết từ một lá bài. Người dùng được quyền nói biểu tượng không phù hợp. HNH dùng nó để mở câu hỏi, không bắt mọi trải nghiệm khớp lời luận.
## K15. Các hệ tổng hợp hiện đại
Human Design, Gene Keys và các hệ mới có tên thương hiệu, nội dung, bản quyền và thuật toán riêng. Nghiên cứu kiến trúc tích hợp, cách trải nghiệm và các tuyên bố tự công bố; không tái đặt tên thành HNH rồi coi nguồn bị xóa. Những thuật ngữ gene/energy/quantum nếu chỉ dùng biểu tượng phải giữ nhãn đó. Quyền sử dụng tài liệu và tạo sản phẩm thương mại cần rà soát.
## K16. Nội tâm và triết học
Kho thực hành cần phân biệt văn bản gốc, dịch, chú giải và trải nghiệm người dạy. Tập trung tự quan sát, trách nhiệm, không dính mắc, giới hạn và lòng trắc ẩn. Tu tập không yêu cầu người dùng chấp nhận một tín ngưỡng; không dùng khổ đau để đổ lỗi “thiếu phúc”. Bài tập ngắn có quyền dừng, không áp các thực hành cường độ cao cho mọi người. Tình trạng cần chuyên môn được chuyển hướng phù hợp.
## K17. Đo lường tâm lý
Chỉ dùng instrument có phiên bản, scoring, license, ngôn ngữ và đối tượng phù hợp. Kho IPIP công khai không biến mọi bản dịch hoặc bộ câu hỏi tự ghép thành validscale. Cần nghiên cứu reliability, cấu trúc, bias và sự phù hợp tại Việt Nam. Bản hỏi120 câu HNH có thể được gọi là tự quan sát, nhưng chưa mang nhãn chẩn đoán. Không dùng birthchart để thay response thật.
## K18. Hành vi, nghề và nguồn lực
Bắt đầu từ việc đã làm, kỹ năng có minh chứng, thời gian, chi phí, trách nhiệm và lựa chọn. Hướng nghiệp cần cả hứng thú lẫn môi trường, kỹ năng và điều kiện. Dữ liệu O*NET là nguồn tham khảo cấu trúc nghề, không bản đồ định mệnh. Finance scenarios dùng giả định rõ, số tiền có currency/as_of và mức thiếu dữ liệu. Lịch sử thành công/khó khăn do người dùng xác nhận, không được AI viết để khớp tuổi.
## K19. Môi trường và sinh hoạt
Ghi nhận thực phẩm, giờ ăn, nơi ở, di chuyển, âm thanh, nhịp làm và phản ứng chủ quan. Những phép đo thiết bị phải có đơn vị, thiết bị và độ tin cậy riêng. Thử nghiệm nhỏ, có quyền dừng, tránh can thiệp y khoa. “Phù hợp với tôi” không tự là tương quan nhân quả; nhiều thay đổi cùng lúc được ghi để tránh quy hết kết quả cho một việc. Không dùng số để chọn thuốc hoặc chế độ ăn điều trị.
## K20. Toán, dữ liệu và AI
Lập knowledge graph với source/edition/rule/claim/purpose; đơn vị lưu trữ là nhận định có loại, không phải những đoạn văn vô hạn. Tái lập method và đánh giá outcome là hai chương trình khác nhau. Corpus người nổi tiếng chỉ hợp nghiên cứu lịch sử có giới hạn và quyền; không dùng hindsight để tuyên bố tiên đoán. Mọi probability cần target/horizon/model/evaluation. Hệ không có mô hình phù hợp sẽ trả scenario, không tự tạo phần trăm.
## Đầu ra của một chu kỳ nghiên cứu
Bản corpus manifest; glossary; method passport; rule spec; input/output schema; golden fixtures; log tranh luận; hạn chế; biên tập VI; rights decision; release recommendation. Mỗi nguồn có trạng thái chưa tiếp cận/đã đọc một phần/đã đọc toàn văn/đã đối chiếu. Không đưa một phạm vi nghiên cứu dài thành quảng cáo “Life Code đã hiểu toàn bộ nhân loại”.


---

# Đồng nhịp sống và thiết kế đời sống: đặc tả dữ liệu và thực hành

Mã tài liệu: **D09** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: HNH Council + Product + Privacy. Nguồn đối chiếu: Yêu cầu của Nhà sáng lập và thiết kế đề xuất trong bộ này. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Không tạo Layer 13
Resonance là quan hệ xuyên 12 lớp, gồm thực phẩm, nước, thời gian, nơi sống, thiên nhiên, giọng nói/âm thanh, con người, công việc, vận động, ngủ/phục hồi, môi trường số và ý nghĩa. Ma trận 144 ô chỉ tổ chức câu hỏi. Không bắt một người điền đủ 144 ô hoặc suy ra giá trị bằng ngày sinh.
## 2. Observation tối thiểu
Ghi subject, field, occurred_at, local timezone nếu có, context, input tự khai, response tự khai, optional measurement, source, data_class, purpose và phiên bản câu hỏi. Mức “thấy nhẹ hơn” là self_report ordinal có nhãn; không gọi là tần số đo bằng hertz. Các đo lường từ thiết bị phải lưu đơn vị, thiết bị và điều kiện, không giả định tương đương với cảm nhận.
## 3. Thử nghiệm nhỏ
Người dùng chọn mục tiêu như giảm gián đoạn lúc viết. Giai đoạn quan sát bảy ngày ghi lịch tự khai. Giai đoạn thử bảy ngày tắt một nhóm thông báo hoặc đổi giờ làm nếu họ chọn. Hệ hiển thị dữ liệu trước–sau và những thay đổi đồng thời. Không kết luận nhân quả từ nhật ký không đối chứng, không nói “cây đã chữa stress” hoặc “SIM tạo tập trung”.
Thay đổi có dấu hiệu gây hại, xung đột trách nhiệm hoặc vấn đề sức khỏe thì dừng và khuyến nghị nguồn hỗ trợ phù hợp; AI không thiết kế nhịn ăn, bỏ thuốc, ngủ ít hoặc trị liệu không chuyên môn.
## 4. Thiết kế đời sống
Life Design nối goal → constraints → options → selected_action → due_date → self_reported_outcome. Mỗi phương án có điều kiện, chi phí thời gian và người chịu ảnh hưởng. Không biến kế hoạch 90 ngày thành 28 nhiệm vụ bắt buộc. Chọn tối đa ba hành động ưu tiên; việc bổ sung mới phải hiển thị phần đánh đổi.
## 5. Bảo mật
Trường “con người” không yêu cầu họ tên đầy đủ của người thứ ba. Dùng bí danh quan hệ; không lập hồ sơ tâm lý bí mật cho họ. Trường thực phẩm/sleep có thể trở thành dữ liệu sức khỏe tùy mục đích và bối cảnh; beta giới hạn nhật ký không lâm sàng và kiểm tra phân loại pháp lý trước mở.
## 6. Nghiệm thu
Tất cả observation sửa được bằng phiên bản, export/xóa được; không có hành vi âm thầm bật tracking. Dashboard tách measurement và tự khai. Khi mẫu ít hoặc dữ liệu ngắt quãng, trả “chưa đủ để nhận xu hướng” cùng số ngày đã ghi, không ép đường trend đẹp.


---

# Mô hình miền: tài khoản, chủ thể, quyền và dữ liệu nhiều giả thuyết

Mã tài liệu: **D10** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Data Architect + Privacy. Nguồn đối chiếu: S09, S15, S16. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Tách tài khoản khỏi con người
Account xác định người đăng nhập; Subject là người được phân tích; Organization là đơn vị hợp tác; Membership chỉ cho quyền công việc trong organization. Không suy từ membership rằng được đọc hồ sơ riêng. Account có thể là chủ thể, người được ủy quyền hoặc người thực hành; mỗi vai cần grant có resource, action, purpose, expiry và trạng thái.
Chủ thể không nhất thiết có account ngay, nhưng việc tạo hồ sơ người thứ ba cần luồng ủy quyền được phát hành. Beta adult-self không mở thao tác ấy. Quan hệ người giám hộ, nhiều bên và quan hệ doanh nghiệp chỉ mở sau review riêng. Founder không có quyền thường trực đọc tất cả dữ liệu; break-glass có lý do, thời hạn và phê duyệt.
## 2. Dữ liệu gốc và dữ liệu dẫn xuất
Profile version là snapshot không sửa âm thầm. Dữ liệu tự khai được lưu với nguồn khai, thời điểm, mức chính xác và ngôn ngữ. Ngày sinh giấy tờ, ngày được gia đình nhớ lại và giờ ước tính là data hypotheses; không ghi đè lẫn nhau và không tự lấp tháng/ngày. Hypothesis có field_path, candidate_value, provenance và trạng thái selected/alternative/unresolved.
Chuỗi tên nguyên bản giữ Unicode NFC; chuỗi bỏ dấu là derivative kèm normalization_version. Không tự chọn ý nghĩa Hán Việt hoặc giới tính từ tên. Thời gian có date_precision, time_precision, time_range, place_text, tọa độ đã xác nhận hay chưa và tzdb_version. Không lấy timezone hiện tại thay timezone lịch sử.
## 3. Quan hệ dữ liệu
Analysis run tham chiếu một profile version, selected hypotheses, product release, purpose và bộ method release. Mỗi method result chỉ về run. Claim chỉ về result hoặc observation liên quan; dependencies tạo đồ thị không chu trình. Report snapshot gom claim đã được phép, không trỏ tùy ý sang dữ liệu live. Export artifact có hash, format, storage key, retention và trạng thái revoked/deleted.
Action plan là dữ liệu sống tách report: người dùng sửa kế hoạch tạo history, không sửa PDF đã xuất. Outcome tự khai vẫn mang self_report. Một nhận định cũ do AI viết không được nhập ngược thành “sự kiện đời thật”.
## 4. Toàn vẹn và phạm vi tenant
Mỗi đối tượng nghiệp vụ có subject_id hoặc owner_account_id phù hợp và tenant_id nếu là dữ liệu tổ chức. Composite foreign keys bảo đảm child không chỉ tới parent ở tenant/subject khác. Tất cả bảng private deny-by-default; API dùng session-derived identity. Idempotency key có namespace account + operation; không dùng khóa global chỉ theo chuỗi client gửi.
## 5. Dữ liệu dẫn xuất và quyền thu hồi
Lineage phải chỉ được report nào dùng observation nào để xóa/sửa chính xác. Khi dữ liệu bị thu hồi, chặn job mới, hủy job chưa phát hành và cập nhật trạng thái artifact. Đã tải về thiết bị ngoài hệ không thể được hứa thu hồi vật lý. Sau khôi phục backup phải áp lại deletion ledger trước phục vụ lưu lượng.
## 6. Nghiệm thu
Schema phải chặn liên kết chéo chủ thể, mục đích không hỗ trợ và version không tồn tại. E2E phải kiểm thử concurrent update với If-Match, profile version đã xóa, grant hết hạn và report đang render. DDL trong bộ này là tham chiếu thiết kế; chỉ được gọi migration sản xuất sau khi chạy PostgreSQL isolated và diễn tập dữ liệu tổng hợp.


---

# Hợp đồng kết quả, chỉ số và cách xử lý điều chưa biết

Mã tài liệu: **D11** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Method Engineering + Data. Nguồn đối chiếu: G05, S14. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Sáu loại nội dung
fact: dữ kiện có nguồn và phạm vi xác nhận; self_report: người dùng kể; observation: quan sát của công cụ/người kèm điều kiện; symbolic_interpretation: tượng nghĩa theo phương pháp; derived_metric: đại lượng tính có định nghĩa; model_probability: xác suất từ mô hình được phép. Kết quả phép chia có thể là derived_metric; lời “mã 71 gợi giữ thành quả” là symbolic_interpretation. Hai loại không được gộp.
## 2. Optional không có nghĩa tùy tiện
score có thể không xuất hiện hoặc null. Khi có phải kèm metric_id, scale_min/max, direction, unit, formula_version và observation_window. Confidence phải có confidence_kind: extraction, data_quality hoặc model_calibration; không dùng một 0,9 chung cho mọi thứ. Probability chỉ được khác null khi result_type=model_probability và có approved_model_release, target_event, horizon, population, evaluation_receipt và applicability check.
Schema là lớp đầu; server còn phải tra model registry để xác nhận version thực sự đã được phê duyệt. Một client tự điền model_release_id không đủ mở cổng. Unknown và zero là khác nhau: không có dữ liệu tài chính không bằng tài chính 0 điểm.
## 3. Coverage không do client định nghĩa
Mẫu số do product release khai báo yêu cầu. Chỉ tính trường phù hợp mục đích và được phép sử dụng. Server bỏ qua mảng weight hoặc score do client tự gửi. Hiển thị riêng input_coverage và method_coverage. Một method có ba cặp không xử lý phải trả unresolved_pairs; không loại chúng khỏi giao diện để làm điểm đẹp.
## 4. Cách ly LCI cũ
raw_lci/normalized_lci/adjusted_lci cũ chỉ tồn tại trong compatibility object experimental_legacy. Không dùng nó để unlock, quyết định giá, xếp người hoặc tạo risk. Báo cáo mới không yêu cầu một điểm toàn đời. Nếu nghiên cứu LCI mới, cần định nghĩa cấu trúc cần đo, data requirements, tính trùng, xử lý missingness và đối tượng sử dụng trước.
## 5. Chỉ số thực hành có thể mở sớm
Task completion = completed_due_tasks / due_tasks với cửa sổ và quy tắc hủy rõ; mẫu số 0 trả null. Observation coverage = observed_days / planned_days. Cashflow = inflows minus outflows theo đơn vị tiền và kỳ tự khai, không so sánh hai tiền tệ nếu không có tỷ giá và ngày. Không gọi những chỉ số này là vận mệnh.
## 6. Sửa sai
Result bất biến theo method release; chỉnh công thức tạo result mới. Diff giải thích field nào đổi và vì sao. Chấm “không phù hợp” giữ trong feedback, không tự tăng/giảm trọng số chung. Không làm đẹp score trước khi Founder duyệt.

## Amendment 2026-10-20 — invariant máy chủ

1. `Metric.value=null` bắt buộc có `missing_reason`; giá trị không null phải nằm trong scale đã khai báo. `percent` dùng 0–100, `ratio` dùng 0–1. So sánh `value` với `scale_min/max` và kiểm soát số chữ số thập phân là invariant runtime vì JSON Schema không biểu diễn được đầy đủ quan hệ này.
2. Tiền tệ không dùng binary floating point. Backend lưu decimal hoặc minor unit cùng ISO-4217 currency, scale, rounding mode, period và `as_of`; không cộng chéo currency khi thiếu FX source/date.
3. `confidence` nếu có phải có kind, value, meaning và evidence IDs; symbolic map bắt buộc null. `probability` chỉ khác null cho `approved_model`, kèm model release, target, horizon, population, evaluation receipt và applicability check.
4. `state=complete` bắt buộc `missing_inputs=[]` và `unresolved_rules=[]`. `blocked` phải có lý do máy đọc được. Claim không có source/lineage không được xuất bản.
5. JSON Schema chỉ kiểm hình dạng. Các quan hệ chéo — cùng subject/tenant, claim thuộc result, section claim là tập con của report, arithmetic identity, release có trong registry và rights còn hiệu lực — phải được backend kiểm lại trong cùng transaction/snapshot.
6. Contract hiện hành được đối chiếu bằng `RESULT_CONTRACT_MATRIX.json`; dependency input/result bằng `METHOD_DEPENDENCY_MATRIX.json`; công thức chỉ lấy từ `FORMULA_CATALOG.json`.


---

# Bộ số: quy tắc độc lập, trường hợp biên và Mã đuôi 80

Mã tài liệu: **D12** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Method Engineering. Nguồn đối chiếu: G02, S15. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Bộ máy được tách thành các hàm
normalize_name bảo toàn chuỗi nguyên gốc và tạo derivative có phiên bản; latin_name_sum theo bảng A–Z công bố; digit_sum nhận chuỗi không âm; personal_year cần quy ước rút gọn và thời điểm bắt đầu năm; pair_classifier dùng cặp chồng lấn; tail80 chỉ dùng đúng bốn chữ số. Không trộn kết quả thành điểm hợp mệnh nếu chưa duyệt một scoring preference rõ.
## 2. Mã đuôi 80
Với chuỗi N có đúng bốn chữ số ASCII, r = int(N) % 80, miền 0–79. Bảng do Founder gửi có nhãn 1–80. Chính sách mặc định cho r=0 là unresolved; cấu hình as80 chỉ bật sau phê duyệt. `0000` không phải tài năng đặc biệt; đó là giá trị số dư. Dùng số nguyên, không dùng phần thập phân rồi floor/truncate.
Mỗi lớp dư có 125 đuôi trong 0000–9999. Một số điện thoại và số định danh có cùng đuôi nhận cùng mã. Ngày sinh không tham gia hàm nên không thể cá nhân hóa Tâm/Thi bằng riêng mô-đun này. 6231→71; 1986→66; 3468→28 là ví dụ kiểm thử từ nội dung cuộc trao đổi, không kết luận cát/hung thực tế.
## 3. Bảng tượng nghĩa
Lưu đủ source_text, source_label, edited_theme, reflection_question, editorial_note và version. Các mục 34/55 có vấn đề chữ trong bản nguồn: không âm thầm coi cách sửa là bản gốc. Nhãn Hung chỉ thuộc bảng; tuyệt đối không dịch thành dự báo bệnh/tai nạn/mất tiền. Không bán đổi SIM hoặc gói hóa giải bằng nỗi sợ.
## 4. Cặp số Bát Cực
Cặp liền kề có chồng lấn, n chữ số tạo n−1 cặp. Bảng cơ sở 64 cặp dùng tập 1,2,3,4,6,7,8,9. Cặp chứa 0 hoặc 5 trả unsupported theo cấu hình đầu; không tự gán 55=Phục vị. Các quy tắc nối qua 5 cần method release khác và source cụ thể; được kiểm tra độ nhạy nhưng không mặc nhiên là chân lý.
## 5. Họ tên và lịch số
Chuỗi quốc tế +84 và nội địa có thể khác tổng chữ số nếu chưa chuẩn hóa. Giữ raw_input, numbering_context và normalized_input; không cộng mã quốc gia tùy ý. Tên có dấu không bị sửa gốc; các hệ chữ khác Latin cần adapter riêng, không tự phiên âm rồi gọi hợp mệnh theo toàn thế giới.
## 6. Nghiệm thu
Exhaustive tail80 10.000 trường hợp; 64 cặp độc nhất; tests r=0, input invalid, NFC, quốc tế/nội địa, unsupported chars, output không có probability. Mã tham chiếu được giao kèm chỉ là minh chứng hợp đồng; không thay review phương pháp và production security.

## Amendment 2026-10-20 — công thức được phép và test biên

1. Chỉ `tail4_mod80`, `digit_sum`, `digital_root`, `latin_name_cycle_1_9`, `adjacent_pair_classification`, `task_completion`, `observation_coverage`, `cashflow_difference` và `age_interval` có entry trong `FORMULA_CATALOG.json`; entry `specified` không có nghĩa là đã được phép phát hành.
2. Không bổ sung master-number retention, personal-year boundary, Bát Cực qua 0/5, bảng tượng nghĩa hoặc quy tắc chuyển tự nếu chưa có source/config được duyệt. Trường hợp thiếu phải trả `unsupported`/`unresolved`, không tự chọn biến thể.
3. Tail80 runtime phải kiểm `N = 80 × quotient + remainder`, `0 ≤ remainder < 80`, và quan hệ `zero_policy`/`lookup_code`. JSON Schema không thay kiểm tra số học chéo trường.
4. Fixture tối thiểu gồm `0000`, `0001`, `0079`, `0080`, `0081`, `0160`, `6231`, `1986`, `3468`, `9999`; input sai gồm sai độ dài, khoảng trắng, số âm, decimal, non-ASCII digit và ký tự. Cả `unmapped` lẫn `as80` phải có negative/positive case.
5. Output số học là deterministic calculation; nhãn/tượng nghĩa là symbolic claim riêng, bị chặn khi rights/source/content review còn pending. Không nối kết quả với sức khỏe, tính cách, tai nạn, tài lộc hoặc xác suất.


---

# Dòng thời gian 0–99: lịch sử, chu kỳ, kế hoạch và kịch bản

Mã tài liệu: **D13** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Data + Method Council. Nguồn đối chiếu: G06, S16. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Bốn đường thời gian
History lưu sự kiện do người dùng cung cấp với độ chính xác ngày/tháng/năm và nguồn. Symbolic cycle lưu kết quả phương pháp có nhãn; không giả làm sự kiện. Plan lưu mục tiêu và lịch hành động tự chọn. Forecast chỉ mở khi có mô hình được phép cho kết quả cụ thể. Giao diện phân biệt bằng chữ, hình thức và chú giải, không chỉ bằng màu.
## 2. Tuổi không phải năm vận hạn
Với ngày sinh B, tuổi a là khoảng từ anniversary(B,a) đến anniversary(B,a+1), nửa mở [start,end). 0–99 gồm 100 khoảng. Ngày 29/02 phải chọn chính sách anniversary không nhuận là 28/02 hoặc 01/03, lưu cấu hình và không âm thầm áp. Bản thử dùng ngày 28/02 nếu đã được product policy chọn, không dùng `add 365 days`.
Chỉ biết năm sinh thì trả khoảng thời gian phù hợp; không tạo sinh nhật 01/01 như dữ kiện. Có nhiều hypothesis tạo nhiều đường tính riêng hoặc band, không hòa thành ngày trung bình. Không mặc định 27, 42, 54 là khủng hoảng; mốc người dùng lập có thể khác.
## 3. Phân tích quá khứ
Không kể một sự kiện chỉ vì một chu kỳ tương ứng. Nếu người dùng chưa kể hôn nhân, nghề hoặc biến cố, report giữ không biết. Nếu nhận sự kiện sau khi đọc báo cáo, đánh dấu observed_after_report để tránh dùng nó làm bằng chứng dự báo trước. Các lịch sử cũ do AI suy diễn không được nhập làm dữ kiện.
## 4. Kịch bản tương lai
Kịch bản ghi assumptions, choices, dependencies, earliest/latest dates và trigger_to_review. Ví dụ chuyển vai trò công việc có ba phương án với thời gian, kỹ năng và nguồn lực; không gán năm thành công chắc chắn. Những mốc xa có độ chi tiết thấp hơn. Kế hoạch 10 năm là hướng và điểm xem lại, không phải lịch biến cố.
## 5. Kiểm thử và UI
Zoom năm/tháng/ngày, chế độ bảng có thể đọc bằng screen reader. Khi nhiều nguồn mâu thuẫn, hiện conflict chip và cho chọn view. Tooltips chứa loại nội dung và provenance. Test đủ tuổi, thứ tự không chồng lấn, năm nhuận, không có ngày sinh, date-only không bị timezone đổi ngày, timezone biên và danh sách rỗng. Mọi timeline sample phải không có hàm sin/seed tạo risk.

## Amendment 2026-10-20 — precision, timezone và version

1. Date-only, local date-time và instant là ba kiểu khác nhau. Backend không được parse date-only qua UTC rồi hiển thị lại theo timezone. Mọi local date-time cần IANA timezone, tzdb version và xử lý explicit cho DST gap/fold.
2. `date_precision` là `full_date`, `month`, `year` hoặc `unknown`. Dữ liệu chỉ có năm/tháng không được materialize thành 01/01 hay ngày 01; timeline trả interval/band và giữ candidate hypothesis.
3. Leap-day policy, calendar conversion, timezone resolution và age-interval formula đều là configuration có version. Thay đổi bất kỳ mục nào tạo method result mới; không ghi đè snapshot.
4. Test bắt buộc có 29/02 với cả hai policy, ranh giới nửa đêm, DST gap, hai instant trong DST fold, timezone lịch sử thay đổi, date-only ở UTC−12/UTC+14, nhiều birth hypotheses và missing birth date.
5. Scenario chỉ chứa assumption/choice/dependency/date range/trigger. Không có seed, pseudo-random, probability, risk score hay sự kiện tiểu sử tự sinh khi thiếu approved model release và evaluation receipt.


---

# Backend: modular monolith, ranh giới tin cậy và lựa chọn công nghệ

Mã tài liệu: **D14** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Tech Lead + Platform. Nguồn đối chiếu: G09, G10, S09, S10, S12, S13. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Lựa chọn đích đề xuất
P0 giữ trang tĩnh hiện có để giảm thay đổi. Sau đó dùng Astro static cho marketing, React/Vite cho app cần tương tác; cùng artifact public qua Pages, API qua Worker/BFF cùng origin. Node/TypeScript là lõi nghiệp vụ và method core để phù hợp source hiện tại. Python chỉ dành tác vụ thư viện đặc thù hoặc worker render; không viết hai implementation công thức.
PostgreSQL là hệ nghiệp vụ đích; D1 được giữ trong vùng legacy chỉ đọc trong migration. R2 chứa tài nguyên riêng tư; Queues điều phối job; outbox trong PostgreSQL là nguồn công việc phải gửi. Không chọn một nhà cung cấp PostgreSQL/IdP/thanh toán trước khi có vùng dữ liệu, pháp nhân, DPA và dự toán. Đây là bốn decision blockers, không phải placeholder triển khai.
## 2. Ranh giới mô-đun
Identity, Access, Profile, Knowledge, Methods, Observations, Analysis, Reports, Plans, Commerce, Practice, Academy, Organizations, Partners và Ops dùng package/service boundary. Mọi gọi nội bộ mang principal và purpose đã được server xác nhận. Một mô-đun không đọc trực tiếp bảng private của mô-đun khác nếu bỏ được policy boundary.
## 3. API gateway
Gateway xử lý request ID, limit kích thước, validation, session, CSRF, quyền đối tượng, quota và route. Authenticated POST không chấp nhận user_id như quyền; subject_id là resource cần kiểm tra. Không lưu payload đầu vào ở edge logs. Không dùng Origin/CORS thay auth. BFF cho web giữ session HttpOnly; mobile/partner dùng token có scope qua IdP được chọn.
## 4. Kết nối database
Hyperdrive query cache phải tắt cho kết nối nghiệp vụ cá nhân hóa; dùng kết nối riêng nếu cần cache dữ liệu công khai. Truy vấn parametrized. Dùng transaction-bound SET LOCAL cho context nếu triển khai RLS; tuyệt đối không giữ user context session-wide trên pool. Service role không BYPASSRLS; report worker không dùng vai trò chủ bảng.
## 5. Assets và deployment
Thay rsync denylist bằng allowlist build có kiểm tra. Docs, API source, engine tests, .env và dữ liệu không thuộc public bundle. App shell fallback chỉ dưới /app; route API và marketing không được trả app index nhầm. CI build từ exact SHA sạch, deps khóa phiên bản, SBOM và digest. Pages/Worker receipt độc lập; release manifest chỉ hợp lệ khi chúng tương thích schema/method versions.
## 6. Rollback
Giữ artifact an toàn gần nhất; không quay lại build có lỗi auth hoặc điểm giả. Dùng expand–contract migrations: deploy code đọc cả schema cũ/mới trong cửa sổ xác định, migrate, rồi mới bỏ cột. Thử rollback trên dữ liệu tổng hợp trước production. Không xóa dữ liệu hoặc khóa người dùng bằng một script “cleanup” không có review.

## Bổ sung 2026-10-20 — artifact triển khai chi tiết

Giữ nguyên lựa chọn modular monolith ở trên. Hợp đồng thực thi sâu hơn nằm tại `05_METHOD_EXECUTION_AND_RESULT_CONTRACT.md`; object authorization tại `06_AUTHORIZATION_POLICY_AND_NEGATIVE_MATRIX.md`; migration tại `07_MIGRATION_AND_RECONCILIATION_RUNBOOK.md`. `SCHEMA_DELTA_REFERENCE_2026_10_20.sql` là thiết kế có thể kiểm tra tĩnh, không phải migration đã triển khai. `openapi.upgrade.overlay.yaml` là input chuyển đổi; `openapi.resolved.yaml` là canonical current planning contract đã materialize, còn `openapi.resolved.json` là semantic mirror. Cả hai vẫn là thiết kế `DESIGN_APPROVAL_PENDING_NOT_IMPLEMENTED`, không phải API runtime. Approval thiết kế vẫn `PENDING` và không thay release gate.


---

# Danh tính, phiên, chia sẻ và kiểm soát đối tượng

Mã tài liệu: **D15** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Security + Backend. Nguồn đối chiếu: G04, G08, G11, S07, S08, S09. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Phiên mới không dựa vào danh tính client tự khai
IdP giải quyết đăng nhập, MFA, recovery và account verification theo cấu hình đã duyệt. BFF tạo session nội bộ từ danh tính đã xác thực. Cookie ưu tiên __Host-lc_session, Secure, HttpOnly, Path=/, không Domain; SameSite và callback flow được kiểm thử. Luồng web mutation có CSRF token/Origin check thích hợp; CORS là kiểm soát khác.
Nếu tự quản session, token đủ entropy, DB chỉ lưu digest/HMAC kiểm tra kèm expiry, revocation, created_at và auth_strength. Không log bearer, không đặt token trong URL/localStorage. Session rotation sau đăng nhập, nâng quyền và recovery; revoke all khi nghi ngờ. Idle/absolute TTL cấu hình theo loại vai trò, không làm hardcoded session sống mãi.
## 2. Công thức quyền
Allow = authenticated ∧ active account ∧ resource state allowed ∧ matching grant ∧ allowed purpose ∧ valid processing basis. Operation trả phí thêm entitlement. Grant có subject/resource/category/action, expiry, grantee và revoker. Organization membership không thay personal grant. Người có report ID nhưng không có quyền nhận 404/403 nhất quán theo policy, không lộ metadata khác chủ thể.
## 3. Điều chỉnh đồng thời và TOCTOU
Kiểm tra quyền tại intake, khi job bắt đầu và trước phát hành. Permission revision tăng khi thu hồi, worker phải kiểm tra revision mới nhất. Update nhạy cảm kiểm tra row/version trong transaction; optimistic concurrency bằng If-Match. Grant bị thu hồi trong khi export thì artifact chưa phát hành bị hủy/ẩn. Background role chỉ được quyền cho task scope, không quyền query toàn cơ sở dữ liệu.
## 4. Chuyên gia và break-glass
Practitioner chỉ thấy phần subject chia sẻ cho case. Ghi chú nội bộ phân loại rõ; khách hàng được biết quyền tiếp cận theo luật và policy. Support không xem nội dung đời tư để xử lý lỗi thanh toán. Break-glass cần hai người hoặc approval có thời hạn, reason code và audit; dùng để xử lý sự cố xác định, không phục vụ tò mò hoặc nghiên cứu.
## 5. Nghiệm thu
Ma trận A chủ thể 1, B chủ thể 2, practitioner có grant giới hạn, org admin, suspended account và anonymous. Test mọi read/update/list/export/search/job status/attachment. Kiểm thử token sai, stale, revoked; object thuộc tenant khác; grant đúng người sai purpose; kết quả từ profile version khác; report được đoán ID. Không kiểm thử trên người dùng thật khi chưa có scope riêng.

## Bổ sung 2026-10-20 — policy registry và failure matrix

`AUTHORIZATION_POLICY_MATRIX.json` định nghĩa policy cho toàn bộ permission label của 64 operation ID hiện có; `06_AUTHORIZATION_POLICY_AND_NEGATIVE_MATRIX.md` khóa trình tự server-side resource resolution, 401/403/404, CSRF, job recheck, permission revision, RLS và các ca âm. Đây là contract mục tiêu; không suy ra code baseline đã được sửa. CORS tiếp tục là kiểm soát trình duyệt, không phải quyền đối tượng.


---

# Tác vụ nền, thanh toán và tính nhất quán nghiệp vụ

Mã tài liệu: **D16** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Backend + Platform + Commerce. Nguồn đối chiếu: S10, S20. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Transactional outbox
Trong một transaction, tạo analysis_run và outbox_event. Dispatcher đọc outbox, gửi queue rồi đánh dấu; nếu bị crash, gửi lại không tạo tác dụng trùng. Consumer có receipt unique theo task_id + handler_version. At-least-once không có nghĩa phải trả phí AI nhiều lần hoặc phát report nhiều lần.
## 2. Idempotency contract
Khóa idempotency có account_id, operation, client_key và request_hash. Cùng key/cùng nội dung trả cùng kết quả; cùng key/nội dung khác trả 409. Khóa không bị chia sẻ giữa accounts. Operation có side effect lưu trạng thái và output ID bền vững; không chỉ dùng cache TTL ngắn. Dùng lease cho worker, timeout và tối đa số retry được cấu hình. DLQ có owner, cảnh báo và thao tác replay được kiểm tra quyền.
## 3. Báo cáo nền
Queue chỉ chứa ID và version, không gửi toàn bộ hồ sơ. Worker resolve quyền và purpose trước truy xuất. Render có ngân sách CPU, bộ nhớ, byte size và timeout. Thành công tính toán không bằng đã xuất PDF thành công; file tạm private được xóa khi job fail. Sau review, tạo report snapshot và artifact hash; publication là transition có audit.
## 4. Thanh toán
Order khóa SKU release, số tiền, currency, thuế/phí đã tính, merchant entity và country pack. Webhook dùng raw body cho signature verification, giới hạn timestamp/replay theo provider. Payment event unique theo provider + merchant_account + event_id. Không tin return URL từ trình duyệt; webhook trùng/out-of-order xử lý bằng state transition và reconciliation.
Grant entitlement là effect một lần sau payment state hợp lệ, không phát lại khi webhook gửi trùng. Refund/dispute tác động entitlement theo terms rõ; không xóa quyền data export của người dùng. Trước cấp report phải kiểm tra report_ready riêng với payment_succeeded. Nếu không đủ dữ liệu, không âm thầm lấy tiền rồi bịa phần thiếu.
## 5. Chuỗi trạng thái
Run: queued → validating → calculating → drafting → reviewing → completed hoặc failed/cancelled. Export: queued → rendering → checking → ready → revoked/deleted. Order: draft → pending_payment → paid → fulfilling → fulfilled; nhánh cancelled, refund_pending, refunded, disputed. Không dùng một trường paid=true cho tất cả nghiệp vụ.
## 6. Diễn tập
Simulate webhook trùng, queue duplicate, worker chết sau gọi AI nhưng trước ghi output, hết quota giữa job, quyền bị thu hồi khi queue đang chờ, mất R2/DB, provider chậm và replay DLQ. Kiểm tra chỉ một quyền được cấp và không phát artifact của người khác. Tài liệu nhà cung cấp là tham chiếu; adapter cụ thể chỉ được release sau sandbox E2E.

## Bổ sung 2026-10-20 — schema delta có thể đối chiếu

`SCHEMA_DELTA_REFERENCE_2026_10_20.sql` bổ sung thiết kế `job_execution`, idempotency receipt bền vững, lease/retry/DLQ fields cho outbox, `merchant_account` và khóa webhook `provider + merchant_account + event`. Nó cũng ghi rõ blocker của unique key cũ. File vẫn `NOT EXECUTED`; provider adapter, signature window, replay behavior và rollback phải được chứng minh trong sandbox trước khi tạo migration thật.


---

# API v2, tương thích và migration D1 sang PostgreSQL

Mã tài liệu: **D17** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Backend + Data + QA. Nguồn đối chiếu: G02, S14. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Contract-first
OpenAPI 3.1.1 là hợp đồng thiết kế được xuất kèm. `/api/v2` là namespace đích; không khẳng định route đã tồn tại. API response dùng request_id, data, warnings và problem details khi lỗi. Trường bắt buộc được schema khóa; phần tự khai có provenance. POST tạo run/report/export trả 202 khi xử lý nền, không trả thành công nội dung giả.
## 2. Nhóm endpoint
Catalog/methods công khai chỉ expose published releases. Accounts/subjects/profiles phục vụ dữ liệu và version. Grants/consents cho chia sẻ. Observations/plans/check-ins cho vòng đời sống. Analysis-runs/results/claims cho tính toán. Reports/exports/downloads cho nội dung. Commerce cho orders/events/entitlements. Practice, Academy, Organizations và Partners chỉ bật bằng product/market flag.
Mọi list có pagination cursor, max page size và filter allowlist. User-controlled sorting không nối vào SQL trực tiếp. PATCH dùng If-Match; stale version trả 412. Export link không đưa PII vào filename URL; tên thân thiện có thể nằm trong Content-Disposition sau kiểm tra ký tự.
## 3. Tương thích legacy
`/api/v1/lci`, `/timeline`, `/life-code-data`, `/report`, session start và profile theo ID có matrix giữ/sửa/khóa. Không proxy xuyên vào mã cũ chỉ vì UI cần hoạt động. Trong containment trả response bảo trì/retired với thông điệp; phần educational sandbox dùng synthetic-only và access gate. Sau v2 có adapter chỉ cho operations an toàn, kèm ngày ngừng và telemetry không PII.
## 4. Migration
Inventory tables và counts, phân nhóm dữ liệu gốc/derived/unknown owner, copy read-only, mapping ID, dry run chuyển, đối soát count + hash + quan hệ, manual xử lý ngoại lệ, cutover có write freeze hoặc capture change được thiết kế. Không merge chủ thể chỉ vì tên/ngày sinh giống nhau. Legacy AI narrative không trở thành fact. Giữ migration ledger từng record với source ID, target ID, reason và status.
## 5. Dữ liệu đầy đủ giả
Không dùng summary cũ để suy rằng khách hàng đã hoàn tất câu hỏi. Những score hardcode chuyển experimental_legacy, không cùng bảng metric mới. Hồ sơ chưa rõ quyền ở quarantine, không tự nhập vào account gần giống. Từ chối migration trái purpose là kết quả hợp lệ, không ép 100% rows.
## 6. Nghiệm thu
Schema validation, contract tests, migration rehearsal rollback, number counts có giải thích ngoại lệ, privacy sign-off, điểm cắt không mất cập nhật và report snapshot trước/sau không đổi dữ liệu gốc. Bộ SQL tham chiếu không được chạy thẳng trên DB sống; developer phải tạo migration incremental có forward/rollback path phù hợp schema hiện tại.

## Bổ sung 2026-10-20 — OpenAPI overlay và mapping legacy cụ thể

Hai file OpenAPI 2026-10-11 được giữ để đối chiếu. **Hợp đồng thiết kế hiện hành duy nhất cho DEV là `openapi.resolved.yaml`**; `openapi.resolved.json` là semantic mirror. Resolver local apply `openapi.upgrade.overlay.yaml`, nhúng nguyên chín JSON Schema canonical, giữ đủ 64 operation ID, kiểm tra toàn bộ local ref và gắn authorization registry. `OPENAPI_UPGRADE_NOTES.md` ghi lệnh tái tạo/`--check`; generic `Resource.attributes` và 46 success contract liên quan được đánh dấu `TRANSITIONAL_GENERIC_BLOCKER`, `x-lc-codegen-ready: false` thay vì xem như contract production.

`MIGRATION_RECONCILIATION_MATRIX.csv` map sáu bảng D1 nhìn thấy tại baseline `99b402764437f81859fa0cd3a3af860125f7bd52`; `07_MIGRATION_AND_RECONCILIATION_RUNBOOK.md` khóa inventory, immutable extraction, quarantine, transform, reconcile, cutover và rollback. Không có số row hoặc receipt runtime trong gói này; tất cả execution status vẫn `NOT_RUN`.


---

# Frontend: điều hướng, trang công khai và không gian ứng dụng

Mã tài liệu: **D18** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Frontend Lead + UX. Nguồn đối chiếu: S01, S02, S03, S04, S06, S18, S19. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Giữ URL công khai, thay trải nghiệm có kiểm soát
Không đổi tên miền hay phá SEO. Home, giới thiệu, hệ thống, chín tầng, LCI, timeline, báo cáo, FAQ, bản quyền, terms, privacy và liên hệ được giữ hoặc 301 một bước tới đường chuẩn. `.html` không tạo nội dung trùng; canonical/hreflang cho từng locale. Engine Lab chuyển khu staging/internal có auth, không chỉ bỏ nav.
Sau P0, marketing dùng static build; app dưới /app dùng route shell riêng. Các route tương tác không được lập chỉ mục. robots/noindex không phải bảo mật; server vẫn kiểm tra quyền. Sitemaps chỉ liệt kê nội dung public được phép, không URL hồ sơ/report hoặc receipt riêng.
## 2. App navigation
Điều hướng chính: Hôm nay, Hồ sơ, Khám phá, Hành động, Báo cáo. Nút hồ sơ luôn hiện chủ thể và không gian cá nhân/tổ chức để tránh thao tác nhầm. Mục Cài đặt gồm quyền chia sẻ, dữ liệu/xóa, bảo mật phiên, thông báo, gói dịch vụ, hỗ trợ và ngôn ngữ. Quota và trạng thái job nhìn được nhưng không chiếm chỗ hành động chính.
## 3. Home mới
Mở đầu bằng giá trị cụ thể: “Hiểu dữ liệu của mình, khám phá góc nhìn có nguồn và xây bước đi phù hợp.” Ba CTA: thử công cụ miễn phí, lập kế hoạch, tìm hiểu chín cấp. Không dùng video autoplay hoặc testimonial giả. Phần phương pháp giải thích loại dữ liệu; trang sản phẩm hiển thị input needed, expected output, limitations, price status và review mode.
## 4. Dashboard mới
Hàng đầu là mục tiêu, hành động kế tiếp và báo cáo đang xử lý. Tiếp theo là thay đổi từ lần trước và điều người dùng muốn cập nhật. Không có đồng hồ “nguy cơ số phận”. Coverage được giải thích bằng các trường còn thiếu cho nhu cầu đang chọn, không áp một con số 38% cho toàn con người. Empty state có mẫu synthetic và CTA phù hợp, không tự điền điểm.
## 5. Screen registry
Bộ kèm `SCREEN_REGISTRY.csv` mô tả route, mục đích, dữ liệu, quyền, loading/empty/error/blocked/ready states và nghiệm thu cho public, user, pro, org, academy, partner và admin. Mọi screen có bản mobile, keyboard và screen-reader. Không vẽ chỉ happy-path rồi để dev tự nghĩ phần lỗi.
## 6. Công nghệ và chuyển đổi
Chưa chuyển framework trong P0. Sau đó chọn Astro marketing, React/Vite app vì ranh giới static/interactive rõ; API shared contract. Không buộc Next.js thêm lớp server không cần thiết. Component library nội bộ có tokens, form primitives, evidence badge và report block renderer. Mỗi PR nhỏ có visual regression và routes smoke.

## Bổ sung thực thi 2026-10-20
`04_PWA_RESPONSIVE_EXECUTION_PLAN_2026-10-20.md` và `SCREEN_EXECUTION_EXTENSION.*` chuẩn hóa đủ 45 route, phone/tablet/desktop transformations, state/offline/cache/a11y/test/evidence. Đây là responsive web/PWA; native app không thuộc deliverable hiện tại.


---

# Thiết kế giao diện, ngôn ngữ Việt và khả năng tiếp cận

Mã tài liệu: **D19** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Design + Frontend + Editorial. Nguồn đối chiếu: S17, S15. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Nguyên tắc trải nghiệm
Bình tĩnh, ấm, rõ ràng; tránh thị giác định mệnh hoặc gây khẩn cấp. Không phân hạng người dùng bằng màu đỏ/xanh. Dữ kiện, tự khai, biểu tượng và kế hoạch có nhãn chữ; màu chỉ hỗ trợ. Typographic scale và khoảng trắng đủ cho tiếng Việt; không viết hoa toàn bộ đoạn dài.
## 2. Design tokens đề xuất
Light theme nền ngà nhạt, ink xanh đen, accent xanh trầm, màu vàng chỉ dùng nhấn nhá. Bộ tokens JSON xuất kèm có spacing 4/8/12/16/24/32, radius và typography. Không nhúng/chia sẻ file font trong gói. Hệ dùng system sans đã hỗ trợ tiếng Việt; khi triển khai web font phải kiểm tra license và subset dấu đầy đủ.
Breakpoints và component đáp ứng theo nội dung. Mobile có một CTA chính, thanh hành động không che bàn phím/nội dung. Thông báo quota không dùng modal lặp. Form có label thực, mô tả và thông báo lỗi được liên kết bằng aria-describedby. Không dùng placeholder thay label.
## 3. WCAG target
WCAG 2.2 AA là mục tiêu nghiệm thu, không tuyên bố đã đạt chỉ bằng chạy axe. Kiểm tra keyboard, focus visible và không bị overlay che; reflow ở 320 CSS px; zoom; contrast tối thiểu theo loại chữ; target size, error suggestion, accessible authentication và hỗ trợ reduced motion. Screen reader đọc bảng và tabs đúng thứ tự.
## 4. Content states
Dữ liệu thiếu: “Chưa có giờ sinh. Những phương pháp cần giờ chưa được chạy.” Chưa rõ quy tắc: “Bảng hiện tại chưa xử lý cặp chứa 5.” Không đủ quyền: thông điệp không lộ chủ thể. Quá hạn mức: nêu limit và lựa chọn tiếp tục xem dữ liệu miễn phí. Quá trình review: nêu vì sao cần kiểm tra và thời gian mục tiêu, không hứa có chuyên gia đang đọc khi chưa phân công.
## 5. Localization
Ngôn ngữ hiển thị bằng tên đầy đủ; cờ chỉ hỗ trợ nơi thích hợp, không dùng cờ như ngôn ngữ vì một ngôn ngữ có nhiều quốc gia. VI trước, EN sau; NL/FR/ZH/JA/KO/TH/HI/AR là country pack chờ duyệt. Date input có ISO storage, locale display; không hiểu 02/11 theo thói quen trình duyệt. RTL thử riêng, tên riêng không tự phiên âm thành dữ liệu chuẩn.
## 6. Nghiệm thu
30 người dùng không phải ngưỡng khoa học; pilot số lượng cụ thể do đội nghiên cứu chọn. Đánh giá thực hành: người mới tìm được cách tính, biết phần chưa biết, sửa hồ sơ và thu hồi chia sẻ mà không cần admin. Chụp baseline visual cho các trạng thái thật, không chỉ màn hình đẹp có dữ liệu giả.

## Bổ sung thực thi 2026-10-20
Target kiểm thử, reflow, orientation, focus, status, authentication, drag alternative và PWA lifecycle được neo vào WCAG 2.2/WAI/manifest/service-worker sources tại `04_PWA_RESPONSIVE_EXECUTION_PLAN_2026-10-20.md`. `DESIGN_TOKENS.json` bổ sung test viewports và interaction/focus/PWA contract, đều `NOT_CHECKED` cho tới khi có receipt.


---

# Nâng cấp nội dung live và SEO không phá đường dẫn

Mã tài liệu: **D20** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Editorial + Frontend. Nguồn đối chiếu: S01, S03, S04, S05, S06, G09. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Copy cần thay cùng chức năng
Home đang dùng thông điệp đọc tới 99 tuổi, luôn có xác suất và các cửa thời gian. Chuyển sang định nghĩa phạm vi, dữ liệu, phương pháp và hành động. LCI không còn nói đã khóa chuẩn nếu điểm người dùng còn tự gán. Bắt đầu không hứa điểm mạnh bẩm sinh đã biết. Timeline không quảng bá năm rủi ro khi engine legacy đã bị tắt. Privacy không hẹn xóa dữ liệu “làm sau” trong một sản phẩm đang thu dữ liệu sâu.
## 2. Ma trận đối chiếu
`SOURCE_TO_TARGET_MATRIX.csv` gắn mỗi trang/route/file hiện có với observed_state, keep/change/quarantine, target module, evidence, owner, task IDs và acceptance. Phần bản quyền giữ quyền sáng tạo được xác lập nhưng không nhận quyền trên standards, bảng có nguồn khác hoặc dữ liệu người dùng. FAQ giải thích rõ full book là phạm vi được bàn giao, không toàn tri.
## 3. SEO thực tế
Mỗi public page có title, description, một H1, cấu trúc heading, canonical và social preview mô tả đúng dịch vụ. Không hứa rich result hoặc thứ hạng. Chỉ dùng structured data phản ánh nội dung đang công bố: Organization, WebSite, Course nếu thực sự có khóa; không tạo rating, giá hoặc review giả. Trang app/private đặt noindex và auth; noindex không thay bảo mật.
## 4. Redirect và sitemap
Đối chiếu toàn bộ href trong source và bản live có thể đọc; clean URL là canonical. Redirect file .html tới clean path một bước; ngôn ngữ có route riêng khi đã có bản dịch đầy đủ. Không redirect mọi 404 về home. Sitemap không chứa preview/staging/account/private reports. Kiểm tra URL cũ với 301/200/404 expectations, không chỉ bấm vài link thủ công.
## 5. Bundle hygiene
Phải tạo manifest public assets từ allowlist: trang, CSS, JS đã build, static images được phép, robots/sitemap. Không copy mọi file trong repo rồi loại trừ vài thư mục. Kiểm thử artifact không có .env, SQL, private fixture, source snapshots hoặc security evidence. Source của dự án có thể public nhưng không đồng nghĩa mọi file thuộc public website.
## 6. Nghiệm thu
Đọc lại toàn bộ bản VI và EN có thay đổi; kiểm tra consistency tên level/layer/field; link checker trên bundle; sample accessibility; diff copy cũ/mới và legal review. Không công bố tính năng là hoạt động trước receipt E2E. Mỗi release có content digest và approval, không để AI tự sửa trang chính sách.

## Bổ sung thực thi 2026-10-20
Public routes UI-01–UI-06 có state, phone/desktop, offline/cache và no-private-payload test IDs trong `SCREEN_EXECUTION_EXTENSION.*`; DEMO-01 và DEMO-12 giữ install/PWA là progressive enhancement. Content digest và approval vẫn là evidence riêng, không được suy từ registry.


---

# AI hỗ trợ: học, hỏi, viết và kiểm soát hành động

Mã tài liệu: **D21** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: AI Lead + Security + Editorial. Nguồn đối chiếu: S21, S22, G02. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Phân vai, không dựng một AI toàn quyền
Bộ điều phối nhận mục tiêu người dùng cùng phạm vi tài khoản, subject, purpose và entitlement đã resolve ở server. Retriever tìm trong nguồn được cấp quyền. Method Runner gọi bộ tính phát hành. Claim Assembler tạo nhận định có provenance. Writer viết từ nhận định được phép. Reviewer kiểm tra ngôn ngữ, số liệu, đối tượng, dữ liệu thiếu và giới hạn. Support Assistant giải thích quy trình. Learning Tutor chỉ dùng học liệu đã phát hành. Ops Assistant tóm tắt vận hành bằng metadata đã loại PII.
Không AI nào được tự cấp grant, sửa bảng tra, phê duyệt phương pháp, đổi chủ thể, truy vấn SQL tùy ý hoặc deploy. Các hành động được phép đi qua công cụ có schema và policy. Model/provider dùng alias có phiên bản và ngân sách; lựa chọn nhà cung cấp là quyết định sau đánh giá data processing, khu vực, chất lượng VI và chi phí, không gắn cứng tên model quảng cáo.
## 2. Retrieval và bộ nhớ
Tách kho nguồn công khai, nguồn được cấp phép, ghi chú chuyên gia và dữ liệu riêng của người dùng. Bộ lọc quyền bắt buộc trước retrieval và kiểm tra lại trước xuất nội dung. Mỗi chunk có source, edition, trang/mục, ngôn ngữ, claim type và rights. Không đưa một bản dịch tự động chưa duyệt vào nguồn chuẩn.
Conversation memory chỉ ghi những điều cần thiết để phục vụ mục tiêu đã chọn. Không tái sử dụng câu chuyện của khách hàng A làm ví dụ cho khách hàng B. Dữ liệu rút consent phải bị loại khỏi chỉ mục, cache và job đang chờ. Lịch sử hội thoại cần phân loại retention riêng; không gọi “bộ nhớ vĩnh viễn” là một tính năng mặc định.
## 3. Chống prompt injection
Tài liệu truy xuất, nội dung web và lời người dùng là dữ liệu, không được quyền đổi system policy. Những câu “bỏ qua quyền”, “đọc hồ sơ khác”, “đổi score thành 95” phải bị từ chối ở công cụ lẫn tầng viết. Model không thấy secrets, không có credential production và không được tự tải URL tùy ý. URL do người dùng nhập không được trở thành quyền outbound request.
Kiểm thử gồm injection trong PDF, đầu mục sách, mô tả ảnh, tên hồ sơ và source excerpt. Reviewer dùng cả luật xác định lẫn rà soát nội dung; hai model cùng đồng ý không được coi là bằng chứng độc lập về sự thật.
## 4. Trách nhiệm và dấu vết
Mỗi generation lưu model alias, model version khi có, prompt version, claim IDs, retrieval IDs, policy decisions, thời gian, token/cost và final content hash. Không log đầy đủ nội dung nhạy cảm vào công cụ phân tích hành vi. Khi provider lỗi, trả bản deterministic hoặc trạng thái chờ; không âm thầm dùng provider khác có điều kiện dữ liệu chưa duyệt.
## 5. Nghiệm thu
Một báo cáo có thể truy từ câu tới claim và nguồn; dữ liệu người khác không lọt vào retrieval; số trong lời văn khớp method output; không xuất mô tả sức khỏe hay nhân cách từ ảnh; low-confidence transcription được trình xác nhận; người dùng có thể đánh dấu sai. Prompt rollback không thay method release. Bộ kiểm thử AI phải gồm tiếng Việt có dấu, câu thiếu dấu, Anh và các bản dịch thử nhưng chỉ locale đã duyệt được phát hành.

## Bổ sung thực thi 2026-10-20
`07_AI_EVALUATION_AND_DEMO_PLAN_2026-10-20.md` tách 12 suite, hard stop, version trigger, cost accounting và offline trace explorer. `NINE_LEVEL_REPORT_CONTRACTS.*` ràng buộc AI role/reviewer/rejection theo từng cấp; chưa có kết quả test nào được suy từ tài liệu này.


---

# Tự động hóa có giới hạn: giảm thao tác, không bỏ trách nhiệm

Mã tài liệu: **D22** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Product Operations + AI Lead. Nguồn đối chiếu: S10, S20, S21. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Bốn mức tự chủ
A0 là đề xuất/soạn nháp, không có tác động bên ngoài. A1 là tính toán hoặc tác vụ đảo ngược, có policy và phạm vi nhỏ. A2 là tác vụ nghiệp vụ đã được người dùng cho phép trước, giới hạn bởi ngân sách, đối tượng, thời hạn và kiểm soát xác định. A3 là thay đổi nhạy cảm phải duyệt: method release, quyền truy cập vượt scope, thông báo sự cố, dữ liệu trẻ em, refund ngoài policy, hợp đồng lãnh thổ, deploy production.
Đây là cơ chế ủy quyền phần mềm, không phải mức thông minh của model. Entitlement có thể tự cấp từ payment event được xác thực bởi server; không phải AI “quyết định khách hàng đã trả tiền”. Quyền xóa dữ liệu có thể tự xử lý theo luồng hợp lệ, nhưng legal hold cần quy trình phê duyệt và giải thích.
## 2. Những việc nên tự động hóa sớm
Kiểm tra đủ trường, tính công thức, báo thiếu dữ liệu, tạo draft, kiểm tra chính tả theo glossary, dựng preview, nhắc hành động đã đăng ký, đối soát job trùng, báo lỗi xuất file, cấp quyền đúng SKU từ webhook hợp lệ và cảnh báo vận hành đã loại thông tin riêng. Các việc này giảm thao tác không cần thiết của Admin mà không tạo lời tiên đoán.
Support bot trả lời từ chính sách đã duyệt, tra trạng thái đơn của đúng tài khoản và mở ticket có mã. Không bịa trạng thái “đã hoàn tiền”; trạng thái phải từ commerce service. Khi cần chuyển người thật, bot gửi tóm tắt vấn đề và dữ liệu tối thiểu, không chia toàn bộ hồ sơ đời sống cho nhân viên hỗ trợ.
## 3. Human review theo rủi ro và độ trưởng thành
Paid beta: mọi báo cáo cá nhân hóa có reviewer trước publish. Sau khi có dữ liệu đánh giá đủ, deterministic result và giáo dục chung có thể auto-publish nếu tất cả kiểm tra máy đạt. Báo cáo sâu, đa chủ thể và dữ liệu nhạy cảm giữ review thích hợp. Tỷ lệ sampling không đặt bằng số tùy ý để gọi là an toàn; cần quyết định release riêng, theo tỷ lệ lỗi và mức tác động đã đo.
Ai duyệt không đồng nghĩa người ấy nhìn được mọi PII. Reviewer chỉ nhận gói dữ liệu tối thiểu. Founder duyệt phương pháp và thương hiệu; không phải nút cổ chai sửa từng dòng của mọi report.
## 4. Automation Center
Mỗi automation card hiển thị: mục đích, trigger, dữ liệu dùng, hành động tối đa, thời hạn ủy quyền, quota, chi phí, lịch sử, nút dừng và người xử lý ngoại lệ. Không gửi nhắc theo “năm xấu”. Quiet hours, timezone, unsubscribe và tránh gửi trùng là điều kiện nghiệm thu.
## 5. Quyền dừng
Kill switch độc lập cho generation, publish, notifications, payments fulfillment, partner exports và từng method release. Dừng generation không làm mất quyền download dữ liệu của người dùng. Dừng intake không xóa báo cáo đã có; việc cần hiệu chỉnh có trạng thái riêng. Mọi nút khẩn cấp phải có diễn tập và người chịu trách nhiệm.

## Bổ sung thực thi 2026-10-20
Eval provider failure, budget exhaustion, revoked grant và prompt injection được yêu cầu trong `07_AI_EVALUATION_AND_DEMO_PLAN_2026-10-20.md`. Mức A0–A3 vẫn là policy proposal; không workflow nào được tự nâng quyền vì xuất hiện trong demo hoặc backlog.


---

# Nhà máy báo cáo: một nội dung chuẩn cho Web, PDF và Word

Mã tài liệu: **D23** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Report Lead + Editorial + QA. Nguồn đối chiếu: G02, G03. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Snapshot và content model
Một report snapshot chốt profile version, method releases, claims, purpose, grants tại thời điểm chạy và content revision. Quyền được kiểm tra lại lúc publish/download; snapshot quyền cũ không duy trì quyền đã thu hồi. Snapshot bất biến về nội dung không có nghĩa PII phải giữ vĩnh viễn: deletion policy được ưu tiên, dùng tombstone không chứa nội dung riêng khi cần audit.
Section có stable ID, layer, purpose, supported claim IDs, narrative blocks, tables, limitations, questions và actions. Các renderer dùng chung content tree. Không tính lại ngày sinh hoặc score trong HTML/Word. Nội dung cá nhân hóa, giáo dục chung, bảng tra và worksheet có nhãn khác nhau.
## 2. Cấu trúc chín template
Mỗi level có mở đầu/phạm vi/source of truth; Identity; Analysis; Timeline nếu có; Action; phụ lục và quyền dữ liệu. Level 1 giải thích phép tính và một thử nghiệm ngắn. Level 2 thêm mâu thuẫn giá trị được người dùng xác nhận. Level 3 sử dụng nhật ký. Level 4 dùng work/resources. Level 5 dùng grant từng bên. Level 6 giữ bốn dòng thời gian riêng. Level 7 chỉ quan sát phù hợp. Level 8 kết tinh lựa chọn sứ mệnh, không phán linh hồn. Level 9 loại lặp và giữ lineage từ mọi phần.
Ngân sách trang là giới hạn biên tập, không là KPI bắt buộc. Dữ liệu ít không được làm thành một “tiểu sử 600 trang”. Có thể xuất sách ngắn hơn với phần thiếu được nói rõ hoặc báo cáo có phụ lục hướng dẫn nhưng phân biệt nội dung chung.
## 3. Quy trình xuất
Validate claims → build tree → editorial rules → preview → review → publish snapshot → queue export → sandboxed renderer → kiểm tra file → private storage → entitlement/grant download. Renderer không tải URL bất kỳ, không đọc local file ngoài thư mục cho phép, không có internet/secret nếu không cần. HTML/Markdown được sanitize. Không nhúng script người dùng vào report.
PDF phải selectable text, font tiếng Việt, bookmark, TOC, số trang, bảng không tràn và link nguồn. DOCX dùng heading/table thật và alt text khi có hình. Web Book lazy-load nội dung nhưng có bản in rõ. EPUB mở sau khi kiểm tra accessibility và font licensing.
## 4. Hiệu chỉnh và thu hồi
Báo cáo sai tạo revision mới; ghi phần thay đổi và lý do. Trạng thái withdrawn chặn phát hành tiếp và cho người dùng biết phần không còn đáng dựa vào. File đã tải không thể thu hồi vật lý khỏi máy người dùng. Không hứa ngược lại. Nếu lỗi hệ thống ảnh hưởng nhiều người, dùng impact query trên method version/claim lineage để tìm report liên quan.
## 5. Nghiệm thu và ngân sách
Máy kiểm tra số liệu, tên subject, thiếu citation, chữ rác và trang trắng; người biên tập kiểm tra tiếng Việt và cách hiểu. Thời gian sinh Level 1 mục tiêu dưới 5 phút chỉ là giả định benchmark; 600 trang chưa cam kết. Retry phải tái dùng snapshot, không phát sinh một bản luận khác mà không có revision ID.

## Bổ sung thực thi 2026-10-20
Factory phải thực hiện typed snapshot → deterministic checks → scoped retrieval → claim plan/draft → reviewer → immutable publish → correction/withdrawal như `06_NINE_LEVEL_AI_REPORT_CONTRACTS_2026-10-20.md`. Page budget không phải acceptance; lineage, rejection, accessible render và revision evidence mới là acceptance.


---

# Chuẩn tiếng Việt, cấu trúc bài đọc và chất lượng học liệu

Mã tài liệu: **D24** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Editorial Authority + Method Council. Nguồn đối chiếu: S15, S38, S39. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Viết cho người thực sự sử dụng
Mỗi phần phải trả lời: kết quả nào đã có, nó được tạo ra thế nào, người đọc nên hiểu phạm vi ra sao và việc gì có thể làm tiếp. Không mở đầu mọi đoạn bằng cùng một mệnh đề; không gọi một chủ đề trừu tượng là “đọc tận tâm can”. Những câu đẹp nhưng không có tác dụng phải được rút gọn.
Từ “năng lượng” cần xác định là trải nghiệm người dùng, biểu tượng hay đại lượng vật lý. “Tu tập” là thực hành tự quan sát có quyền lựa chọn, không phải điều kiện được đối xử tốt. “Sứ mệnh” là hướng giá trị người dùng chọn và thử, không phải món nợ của linh hồn. Không gán nghĩa một họ tên chỉ bằng từ đồng âm.
## 2. Glossary và dịch thuật
Tiếng Việt là bản biên tập chính; giữ dấu, chuẩn NFC, thống nhất Huyền Nhân Học, Mã đuôi 80, Đồng nhịp sống. Thuật ngữ kỹ thuật Anh được giữ trong schema nhưng giải thích bằng tiếng Việt. Bản dịch dùng termbase, translator và reviewer độc lập cho các đoạn có tác động lớn. Dịch ngược là một kỹ thuật kiểm tra nội dung, không chứng minh validity tâm lý của thang hỏi.
Ngôn ngữ nguồn và ngôn ngữ giao diện là hai registry khác. Có đọc một tài liệu Trung văn không đồng nghĩa sản phẩm tiếng Trung đã đủ legal/culture gate. RTL, dấu tên, lịch, số thập phân, ngày tháng và đồng tiền đều cần locale tests.
## 3. Bốn loại đoạn văn
Đoạn dữ kiện nêu nguồn. Đoạn biểu tượng ghi quy ước. Đoạn tự thuật gắn lời người dùng. Đoạn hành động nói rõ điều kiện và lựa chọn. Không dùng một disclaimer cuối sách để hợp thức hóa hàng chục trang khẳng định tuyệt đối bên trong.
Ví dụ sửa: “Thiếu số 4 nên sức khỏe yếu” thành “Trong biểu đồ này không xuất hiện chữ số 4; phương pháp không cho phép kết luận sức khỏe.” “Cặp đôi khắc số” thành “Hai bảng quy ước tạo chủ đề khác nhau; cách hai người giao tiếp cần dựa trên dữ liệu hai bên đồng ý chia sẻ.”
## 4. Học liệu và bài đánh giá
Câu hỏi tự quan sát do HNH viết không tự được gọi là trắc nghiệm chuẩn hóa. Muốn dùng IPIP/O*NET hoặc công cụ khác phải xác định phiên bản, quyền, ngôn ngữ, cách chấm và đối tượng; không chỉnh wording một thang rồi giữ claim độ tin cậy cũ. Các worksheet của HNH có thể hữu ích mà không cần giả nhận là đo được tính cách bẩm sinh.
## 5. Nghiệm thu
Không lỗi chủ thể/ngày sinh, không lỗi phép tính, không chữ mất dấu do encoding, không nhầm CCDD/CCCD, không bảng 80/81 tráo nhau, không câu khẳng định y khoa. Đánh giá gồm checklist máy và đọc trực quan tài liệu đã render. Mẫu đạt mới được đưa vào report factory.

## Bổ sung thực thi 2026-10-20
Mỗi Level 1–9 có golden/null/conflict/unauthorized/injection/correction fixture và reviewer khác biệt trong `NINE_LEVEL_REPORT_CONTRACTS.*`. Hard-stop case không được che bởi điểm trung bình; mức/ngưỡng mềm phải được quyết trước khi xem kết quả.


---

# Chuẩn bài đọc người dùng: từ dữ liệu đến lựa chọn

Mã: **D38** | Phiên bản: **2026-10-11.r1** | **ĐỀ XUẤT / CHỜ PHÊ DUYỆT**

Chủ trì: Editorial + Product. Nguồn đã tiếp cận: G02. Các nhóm văn bản khác bên dưới là danh mục cần nghiên cứu, không được hiểu là đã đọc toàn văn.


## Ca minh họa tổng hợp, không phải hồ sơ thật
Một người dùng mô phỏng nói: đang làm sáu dự án, có kỹ năng đào tạo, thường chưa hoàn tất tài liệu, mất hai giờ đi lại và sợ làm cộng sự thất vọng khi từ chối. Đây là dữ liệu giả để thử giao diện/nội dung; không gán cho Founder hoặc bất kỳ người thật.
## Identity
Bản đọc mở bằng dữ liệu đã cung cấp và phần thiếu: chưa có lịch chi tiết, tình hình tài chính hoặc sức khỏe; không kết luận kiệt sức hay rối loạn. Người dùng muốn hoàn tất một tài liệu trong30 ngày. Những phương pháp biểu tượng nếu được chọn nằm trong phần riêng, không dùng để chứng minh năng lực.
## Analysis
“Điều đã biết là nhiều cam kết đang dùng chung thời gian của anh/chị. Trước khi mở thêm việc, cần biết mỗi dự án đang đòi bao nhiêu giờ, ai là người quyết và phần nào có thể bàn giao. Chúng tôi chưa thể kết luận vì sao anh/chị khó hoàn thành; đó có thể liên quan đến phạm vi, gián đoạn hoặc tiêu chí hoàn tất chưa rõ. Hãy chọn một tài liệu và mô tả ‘xong’ bằng đầu ra cụ thể.”
Cách viết này đi sâu vào vấn đề thật mà không nói người đó bẩm sinh phân tán, thiếu số4 hoặc đang đi sai sứ mệnh. Nếu người dùng bác bỏ, hệ cập nhật dữ liệu và cách hỏi; không ép phản hồi về trạng thái “đúng nhưng chưa nhận ra”.
## Timeline
“Trong bảy ngày đầu, ghi công việc và thời gian; trong tuần thứ hai, chọn phạm vi tài liệu và người nhận; tuần thứ ba viết bản dùng thử; tuần thứ tư nhận phản hồi và sửa. Lịch này là đề xuất theo mục tiêu của anh/chị, không phải năm cơ hội được tiên đoán.” Các ngày được tính theo timezone người dùng; action không tự đánh done.
## Action
Một hành động có tiêu đề, lý do, owner, due date, giới hạn nguồn lực, điều kiện dừng và cách tự đánh giá. Ví dụ: bỏ một cuộc họp không cần thiết trong hai tuần; theo dõi số giờ viết thực tế. Không bảo người dùng nghỉ việc hoặc thay quan hệ từ dữ liệu ít. Bài tập được bỏ qua mà không bị trừ phẩm chất.
## Giao diện cho người chưa quen thuật ngữ
Mỗi thẻ có “Dữ liệu đã dùng”, “Kết quả nói gì”, “Không nói gì”, “Việc có thể thử”. Người đọc có thể mở công thức và source nhưng không bị buộc đọc hết sách kỹ thuật. Báo cáo đầy đủ nằm phía sau khi họ muốn xem; giá trị đầu tiên là một vấn đề được làm rõ và một bước có thể bắt đầu.
## Chỉ số chất lượng trải nghiệm
Đo người đọc có phân biệt được dữ kiện/biểu tượng không, tìm được hành động không, sửa sai được không và biết ai có quyền xem hồ sơ không. Không tối ưu conversion bằng lo sợ hoặc giữ người dùng lệ thuộc vào câu trả lời của AI. Life Code phải giúp họ tự chủ hơn sau khi dùng.

## Bổ sung thực thi 2026-10-20
PM-01/02/03/04/07 tại `../01_Chien_luoc_San_pham/07_PRODUCT_EXECUTION_CHARTER_2026-10-20.md` chuyển giá trị này thành giả thuyết đo được cùng kill trigger. Cohort, target và observation window vẫn cần Q20; tài liệu không tuyên bố metric đã đạt.


---

# Dữ liệu cá nhân: mục đích, lưu giữ, xóa và khôi phục

Mã tài liệu: **D25** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Privacy Lead + Data Lead. Nguồn đối chiếu: S23, S24, S30, S40, S05. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Thiết kế theo mục đích
Mỗi lần intake giải thích dùng để làm gì, bắt buộc hay tùy chọn, ai xem và retention. Căn cứ xử lý được pháp lý xác định theo hoạt động và quốc gia; không gọi mọi xử lý đều là consent. Consent cho dịch vụ không bao gồm training, marketing, nghiên cứu, chia sẻ chuyên gia hay tổ chức. Rút đồng ý ảnh hưởng processing nào phải được giải thích.
Hồ sơ cá nhân không thuộc về employer hoặc regional licensee chỉ vì họ trả tiền. Hệ cấp quyền chia sẻ theo field/section, thời hạn và hành động. Reviewer support không thấy nội dung sức khỏe/tình cảm mặc định. Subject access và account access không đồng nhất.
## 2. Lịch lưu giữ đề xuất để pháp lý duyệt
Các giá trị trong RETENTION_SCHEDULE là thiết kế, chưa phải pháp luật: tệp upload tạm 24 giờ nếu chưa hoàn tất; job payload tối thiểu xóa sau khi giao/đối soát; log bảo mật giữ có thời hạn dựa vào mục đích; bản báo cáo còn hiệu lực theo hợp đồng và yêu cầu người dùng; backup theo chu kỳ được xác định. Hóa đơn, tranh chấp và legal hold có quy tắc riêng. Không ghi “immutable forever” cho dữ liệu nhạy cảm.
## 3. Luồng xóa
Nhận yêu cầu → xác minh quyền → mô tả phạm vi và ngoại lệ hợp pháp → freeze processing liên quan → lập deletion plan → DB → R2 → search/vector index → cache → queue/DLQ → provider theo hợp đồng → receipt. Job đang chạy phải recheck trước publish và bỏ kết quả nếu scope đã bị thu hồi. Hệ phải có tombstone/revocation register đủ để backup restore không phục hồi dữ liệu đã xóa.
Receipt ghi hệ đã xử lý, hệ chờ hết backup retention và ngoại lệ còn giữ. Không tuyên bố xóa tức thời tất cả bản sao khi provider hoặc backup chưa hoàn tất. Hợp đồng provider phải cho phép thực hiện quyền đã hứa với người dùng.
## 4. Trẻ em và hình thái
First beta không thu dữ liệu trẻ, ảnh sinh trắc hoặc dữ liệu bệnh. Những dòng này có legal gate, thiết kế guardian/assent phù hợp tuổi, scope chuyên gia và quy trình thu hồi riêng. Một tuổi ngưỡng toàn cầu không đủ. Country pack kiểm soát tuổi và dịch vụ được cung cấp; không tự suy giới tính từ tên/ảnh.
## 5. Sự cố và hỗ trợ
Phân biệt lỗ hổng source, dấu hiệu khai thác và sự cố đã xác minh. Ghi thời điểm phát hiện, dữ liệu liên quan, phạm vi truy cập, bằng chứng và đánh giá pháp lý. Thời hạn thông báo là nghĩa vụ theo tình huống/quốc gia, không đặt một con số chung. Người dùng có kênh sửa dữ liệu và khiếu nại miễn phí; quyền xuất/xóa dữ liệu không nằm sau paywall.


## Bổ sung ngày 20 tháng 10 năm 2026

Áp dụng activity-level legal matrix và data-system inventory; test deletion gồm jobs đang chạy, DLQ, provider, cache và restore. Mọi retention chưa được ký vẫn là proposal. Xem SECURITY_AND_PRIVACY_ACCEPTANCE.md.


---

# Mô hình đe dọa và ranh giới bảo vệ

Mã tài liệu: **D26** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Security Lead + Architect. Nguồn đối chiếu: S07, S08, S09, S11, S12. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Tài sản và đối tượng đe dọa
Tài sản gồm hồ sơ, dữ liệu quan hệ, quyền chuyên gia, báo cáo, nguồn có bản quyền, thông tin thanh toán, method release và secret hạ tầng. Kịch bản gồm người dùng đổi ID để đọc người khác, insider xem dữ liệu vượt vai, partner tùy biến bỏ policy, prompt injection trong nguồn, upload độc hại, webhook giả, job trùng và artifact build vô tình công khai.
## 2. Trust boundary
Trình duyệt không đáng tin để quyết user_id, score, weight hay quyền. Gateway xác thực; service xác định subject/grant/purpose; DB giới hạn tenant và subject; renderer bị cách ly; AI chỉ thấy gói dữ liệu tối thiểu. Public docs khác kho nguồn có license. Preview/staging không nối production database hoặc bucket người thật.
## 3. Kiểm soát cụ thể
BOLA: mọi route nhận ID có authorization cùng truy vấn, bao gồm list/search/download/aggregate. RLS là phòng vệ sâu, role không owner/superuser/BYPASSRLS. SET LOCAL context phải nằm trong transaction với identity do server resolve; test pool reuse giữa hai tenant. Hyperdrive cache OFF cho workload riêng tư cho tới khi có chứng minh không lẫn context.
Session: cookie an toàn, CSRF/Origin cho mutating calls, revoke và expiry, reauth cho thao tác cao; recovery không dựa tên/ngày sinh. Upload: MIME/magic sniff, size/pixel/decompression limits, filename random, quarantine scan, stripping EXIF khi phù hợp, không publish trực tiếp. Renderer: block outbound/SSRF và file URL; HTML sanitize và CSP phù hợp.
Supply chain: public allowlist, secrets scan, dependency review, locked artifact, pinned action release theo chính sách, protected environment approvals và deployment receipt. Không coi mã nguồn public là incident nếu chủ định công khai; chỉ coi đóng gói ngoài allowlist là lỗi artifact.
## 4. Kiểm thử ưu tiên
Hai account ở cùng tenant và khác tenant; revoked grant lúc job chạy; presigned URL đã cấp; cache khóa sai; identifier enumeration; denial-of-service qua report600pages; ký webhook sai; replay payment; forged model tool call; partner certificate thu hồi. Rate limit không được là cơ chế phân quyền. CORS không ngăn request ngoài trình duyệt.
## 5. Tải báo cáo và break-glass
Authorized proxy download là mặc định khi cần thu hồi nhanh. URL ký ngắn vẫn là bearer cho tới hết hạn, cần ghi rõ. Break-glass chỉ qua người được duyệt, phạm vi/thời hạn nhỏ, cảnh báo độc lập và review sau sự kiện; Founder/admin tổng không có quyền xem nội dung mặc định.


## Bổ sung ngày 20 tháng 10 năm 2026

Bổ sung pool reuse/failed transaction, field redaction, service worker cache, renderer isolation và metadata enumeration vào test scope. Source/model/document content không cấp quyền tool. Xem SECURITY_AND_PRIVACY_ACCEPTANCE.md.


---

# Vận hành, quan sát, khôi phục và kiểm soát chi phí

Mã tài liệu: **D27** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: SRE + Finance Operations. Nguồn đối chiếu: S10, S11, S13, S20. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Service objectives đề xuất
Trước launch phải đo trên staging và tải mục tiêu. API thường p95 dưới 800 ms; report Level 1 xử lý nền mục tiêu dưới 5 phút; availability mục tiêu 99,5% cho beta có cửa bảo trì; RPO nghiệp vụ tối đa 1 giờ; RTO tối đa 4 giờ. Đây là mục tiêu thiết kế chưa phải SLA. Thay mục tiêu phải có capacity/cost reasoning và người duyệt.
## 2. Quan sát không lộ nội dung
Log request ID, account/subject pseudonymous ID theo chính sách, endpoint, latency, quyết định quyền, lỗi loại và job ID. Không log raw birth/photo, bearer, presigned URL, prompt hoặc report nội dung mặc định. Metrics gồm success/denied, queue age, retry, DLQ, generation cost, provider errors, export fail và entitlement mismatch.
Alerts có owner, mức nghiêm trọng, quiet channel cho noncritical và runbook. AI có thể tổng hợp alert nhưng không tự nâng quyền hoặc sửa database. Health public chỉ xác nhận tiến trình; readiness/dependency sâu được kiểm soát để tránh lộ cấu hình.
## 3. Khôi phục
Thử backup restore trong isolated environment; đối soát rowcounts, FKs, sample synthetic checksum, grants và deletion tombstones. Không dùng backup người thật ở dev cá nhân. Sau restore phải replay revocation/deletion phù hợp rồi mới mở truy cập. Canary rollout chỉ dùng cohort được phép; rollback method/prompt phải không mở lại phương pháp revoked.
## 4. Incident runbook
Phân công Incident Commander, technical owner, privacy/legal và comms. Mốc 0–4h: phân loại, chặn, lưu chứng cứ tối thiểu. Theo dõi tác động thay vì tuyên bố đã an toàn vì health200. Đánh giá thông báo theo luật và hợp đồng. Sau sự cố: root cause, timeline, quyết định, sửa tests và prevention owner. Không sửa log để làm lịch sử đẹp.
## 5. Chi phí và chống lạm dụng
Free tool ưu tiên deterministic local; anonymous AI không mở vô hạn. Quota theo account/device/risk phù hợp, không thu ID nhạy cảm chỉ để chống abuse. Giới hạn tokens, retries, reportpages, đồng thời jobs và export frequency theo SKU. Cache chỉ nguồn công khai/versioned; kết quả cá nhân cache scoped hoặc không cache. Ngưỡng ngân sách bật degrade-to-deterministic, dừng job không cấp thiết và thông báo minh bạch.
## 6. Vận hành tối thiểu con người
Automation xử lý đối soát và cảnh báo thông thường. Ca nhạy cảm giữ người trực được đào tạo. Support cần macro ngôn ngữ thân thiện và source đúng policy. Không để bot tiếp tục gây sợ khi khách hàng nói báo cáo Hung làm họ hoảng. KPI gồm time-to-resolution, lỗi tái phát, user correction và tỷ lệ tác vụ hoàn thành; không chỉ số phút con người tiết kiệm.


## Bổ sung ngày 20 tháng 10 năm 2026

SLI denominator, alert thresholds, service ownership, DR drill, capacity profiles và budget actions được đặc tả trong OPERATIONS_ACCEPTANCE_RUNBOOK.md và OPERATIONS_ACCEPTANCE.json; chưa là số đo hiện tại.


---

# Pháp lý Việt Nam và phạm vi dịch vụ phải rà soát

Mã tài liệu: **D28** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Legal Counsel + Privacy Lead. Nguồn đối chiếu: S23, S24, S25, S26, S27, S28, S29. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Phạm vi của tài liệu
Đã đối chiếu thông tin chính thức về văn bản; đây không phải legal opinion, chứng nhận tuân thủ hay xác nhận đã đọc đầy đủ mọi điều khoản áp dụng. Counsel cần kiểm tra văn bản hiện hành, điều khoản chuyển tiếp, hoạt động cụ thể và nhà cung cấp thực tế trước launch. Không sao chép nguyên đoạn “Nghị định 85/2021 là đủ” từ plan cũ sang dịch vụ sau 01/07/2026.
## 2. Bộ văn bản nền đã nhận diện
Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 và Nghị định 356/2025 có hiệu lực từ01/01/2026. Luật AI 134/2025/QH15 có hiệu lực từ01/03/2026; Nghị định 142/2026 từ01/05/2026. Luật Thương mại điện tử122/2025/QH15 và Nghị định 248/2026 có mốc hiệu lực01/07/2026 theo thông tin chính thức được đối chiếu. Mỗi function AI, loại dữ liệu và vai trò kinh doanh phải được phân loại; không suy ra nghĩa vụ của toàn nền tảng chỉ từ tên “ứng dụng giáo dục”.
## 3. Những quyết định phải có chủ thể chịu trách nhiệm
Pháp nhân cung cấp dịch vụ, bên thu tiền, bên kiểm soát/xử lý dữ liệu, chủ thể sử dụng thương hiệu và nhà cung cấp AI phải được chỉ định. Không tự chọn pháp nhân phi lợi nhuận hoặc doanh nghiệp của Founder mà chưa có quyết định. Counsel lập data flow, vendor terms, địa điểm xử lý, subprocessors, căn cứ xử lý, hồ sơ/thủ tục cần thực hiện và lịch rà soát.
## 4. Chính sách người tiêu dùng
Trước trả tiền hiển thị phạm vi, định dạng, thời hạn dự kiến, dữ liệu cần có, giới hạn chỉnh sửa, điều kiện không thể cung cấp, hủy/hoàn tiền và kênh khiếu nại. Không bán mức “độ chính xác95%” khi không có cơ sở. Không dùng feedback cá nhân làm testimonial y khoa hoặc cam kết lợi nhuận. Nội dung đào tạo HNH không tự là chứng chỉ hành nghề được pháp luật công nhận.
## 5. Ranh giới sức khỏe, tài chính và trẻ em
Không mở diagnosis, kê đơn, hướng dẫn bỏ điều trị, quyết định đầu tư tự động hoặc xếp hạng trẻ em bằng hình thái/số. Muốn mở dịch vụ chuyên môn cần workstream riêng về giấy phép, nghề nghiệp, trách nhiệm, dữ liệu và chuyên gia. Disclaimer không thay cơ chế kiểm soát. Đối với partner, hợp đồng cấm quảng bá sai phạm vi và có quy trình kiểm tra/thu hồi.
## 6. Gate
Legal readiness chỉ pass khi có ý kiến áp dụng cho scope phát hành, chủ thể dịch vụ, policy version, data processing, commerce flow và support. Các văn bản tham khảo trong SOURCE_REGISTRY là điểm bắt đầu tra cứu, không được ghi “đã tuân thủ” chỉ vì có đường dẫn.


## Bổ sung ngày 20 tháng 10 năm 2026

Metadata chính thức về Luật AI134/2025, NĐ142/2026, Luật TMĐT122/2025, NĐ248/2026 và Luật91/2025 đã được đọc lại20/10. Không đồng nhất metadata với full-text applicability. LEGAL_ACTIVITY_MATRIX.json khóa từng hoạt động và owner; RESEARCH_UPDATE_2026-10-20.json ghi phạm vi đã đọc.


---

# Cấp phép quốc tế và nhượng quyền Huyền Nhân Học

Mã tài liệu: **D29** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Founder + Partnerships + Legal. Nguồn đối chiếu: S30, S31, S32, S33, S34, S35, S36, S37, S40, S41. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Bốn mô hình hợp tác, không gọi chung là nhượng quyền
Referral giới thiệu khách không truy cập dữ liệu. Certified Practitioner hành nghề trong phạm vi đào tạo/nội quy và quyền khách hàng cho phép. Institutional License dùng phần mềm/học liệu theo số ghế, công dụng và quốc gia. Regional License/Franchise có thể kèm thương hiệu, đào tạo, tiêu chuẩn vận hành, phí và hỗ trợ. Việc gọi hợp đồng là license không tự loại trừ luật franchise; counsel phải phân loại theo nội dung thực chất tại từng nơi.
## 2. Country pack trước khi bán ở quốc gia mới
Mỗi pack chốt pháp nhân/merchant, dịch vụ được phép, dữ liệu cần hạn chế, age policies, ngôn ngữ đã review, thuế/hóa đơn, thanh toán, complaint/refund, dữ liệu xuyên biên giới, nhà cung cấp, support timezone, trademark scope và phân loại license/franchise. Không mặc định dịch giao diện sang Anh là quyền kinh doanh toàn cầu.
Việt Nam là giai đoạn chính. EU/EEA, Hoa Kỳ, Australia và Singapore là các jurisdiction candidates cần thẩm định, không phải thị trường đã phê duyệt. GDPR và lịch áp dụng EU AI Act phải được kiểm tra bằng văn bản hợp nhất trước launch, kể cả thay đổi Omnibus công bố2026. Tài liệu PDPC Singapore hiện mới truy xuất mức hạn chế; không coi đã hoàn tất review PDPA.
## 3. Hợp đồng đối tác cần có gì
Lãnh thổ, nhóm khách hàng, SKU, quyền thương hiệu, quyền dịch thuật, tiêu chuẩn phương pháp, version sử dụng, phạm vi tư vấn, bảo mật, processing roles, đơn vị thu tiền, fees/royalties, báo cáo doanh số, audit quyền hạn, cấm sub-license khi chưa duyệt, tiêu chuẩn đào tạo và support. Không cam kết thu nhập, không bán “độc quyền lãnh thổ” vô điều kiện trước khi đủ pháp lý và năng lực vận hành.
Điều khoản chấm dứt phải bảo vệ người dùng: cách chuyển support, quyền truy cập/xuất/xóa dữ liệu, report còn hiệu lực, giới hạn sử dụng thương hiệu và xử lý phí chưa thực hiện. Không giữ dữ liệu khách làm đòn bẩy tranh chấp với partner.
## 4. Lưu ý pháp lý cụ thể để kiểm tra
FTC có hướng dẫn FDD23 hạng mục và mốc cung cấp ít nhất14 ngày theo luật liên bang áp dụng; state requirements có thể khác và cần counsel. Australia có Franchising Code mới từ01/04/2025 cùng một số mốc01/11/2025; phải kiểm tra disclosure và nghĩa vụ áp dụng từng giao dịch. Nguồn Bộ Công Thương đã đọc là danh mục nhượng quyền, không đủ kết luận thủ tục outbound. Madrid là cơ chế nộp yêu cầu bảo hộ tại thành viên được chỉ định; không có nghĩa thương hiệu đã được cấp độc quyền khắp thế giới.
## 5. Kiểm soát chất lượng xuyên quốc gia
Partner có thể thay theme, logo phụ, locale và gói dịch vụ được cấp. Không được thay method table, bỏ limitations, bật trẻ em/sức khỏe hoặc tăng autonomy. Country policy giao với method/product/tenant policy theo nguyên tắc deny wins. Mỗi report giữ method release và locale content release; một bản dịch đã thu hồi có thể chặn publish mới mà không hủy hồ sơ gốc.
## 6. Lộ trình thương mại
Bắt đầu đối tác thử nghiệm không độc quyền, số khách giới hạn, cùng hỗ trợ từ trung tâm. Chỉ bàn franchise rộng sau khi có sản phẩm ổn định, economics đo được, vận hành hỗ trợ, pháp lý lãnh thổ và brand governance. Phí/royalty là cấu hình chờ đàm phán, không tự đặt giá như báo giá hiện hành.

## Bổ sung thực thi 2026-10-20
LC-REGIONAL được giữ ở train T8/F_LEGAL trong `PRODUCT_EXECUTION_EXTENSION.*`; DEMO-10/11 và FPOS/custom gates chỉ tạo evidence slot. Mọi `COUNTRY_PACKS.json` hiện `NOT_APPROVED`; không quốc gia, giá hay mô hình franchise nào được tài liệu này tự mở.


---

# Academy, đào tạo giảng viên và không gian chuyên gia

Mã tài liệu: **D30** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Academic Lead + Method Council. Nguồn đối chiếu: G02, S38, S39. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Ba tuyến đào tạo
Tuyến tự ứng dụng dành cho người dùng muốn hiểu công cụ và lập kế hoạch. Tuyến practitioner có thực hành quan sát, quyền dữ liệu, giới hạn, viết báo cáo và xử lý phản hồi. Tuyến trainer/researcher bổ sung phương pháp, source rights, biên tập đa ngôn ngữ, giám sát và governance. Không coi hoàn tất video là đủ năng lực tư vấn độc lập.
## 2. Khóa nền chín buổi, 120 phút/buổi
Buổi 1: triết lý HNH, quyền lựa chọn và phân loại nhận định; đầu ra là một hồ sơ phạm vi. Buổi 2: dữ liệu sinh, tên, nguồn và bất định; thực hành sửa giả định sai. Buổi 3: bộ số và quy tắc; tính tay đối chiếu code. Buổi 4: hành vi, giá trị và ngữ pháp sáu quan hệ; viết câu hỏi không dẫn dắt. Buổi 5: Đồng nhịp sống; lập nhật ký và thử nghiệm nhỏ. Buổi 6: nghề, nguồn lực và quan hệ; giới hạn chuyên môn và consent. Buổi 7: báo cáo bốn lớp; thuyết minh có nguồn, không lặp hoặc gây sợ. Buổi 8: đạo đức, dữ liệu, khiếu nại và referral; mô phỏng ca. Buổi 9: bài tổng hợp, phản biện, sửa và kế hoạch hành động.
Lịch mở lớp, phí và quà tặng phải thuộc cohort cụ thể. Không dùng lại ngày khai giảng2026 cũ như lịch còn hiệu lực. Giá chưa được chốt trong bộ này.
## 3. Đánh giá năng lực
Rubric gồm tính đúng dữ liệu và công thức, chất lượng câu hỏi, khả năng chấp nhận sai, tiếng Việt, privacy, scope và hành động phù hợp. Các lỗi nghiêm trọng như bịa bệnh, ép mua hóa giải, lấy dữ liệu người khác hoặc lộ ảnh làm bài không đạt dù các mục khác tốt. Chứng nhận nội bộ thể hiện program version, phạm vi và thời hạn hiệu lực đề xuất; không giả danh bằng cấp tâm lý/y khoa.
## 4. Practitioner Studio
Khách hàng cấp quyền theo hồ sơ/section và thời hạn. Case có mục tiêu, consent, notes scope, draft, review và closure. Ghi chú practitioner không tự trở thành fact; khách hàng có cơ chế phản hồi và sửa. Lịch hẹn và hóa đơn không cần toàn bộ nội dung report. Chuyên gia rời tổ chức bị thu hồi quyền nhưng lịch sử nghiệp vụ hợp lệ vẫn được quản lý theo retention.
## 5. Giám sát và phát triển
Practitioner mới có ca tổng hợp và ca thực hành dưới giám sát trước khi cấp phạm vi rộng. Audit lấy mẫu theo rủi ro; khi bị phản ánh, tạm khóa quyền publish liên quan, không tự kết luận vi phạm. Training updates theo method version; method retired thì học liệu và bài kiểm tra liên quan được cập nhật. Peer supervision giúp giữ chất lượng mà không đẩy mọi quyết định lên Founder.

## Bổ sung thực thi 2026-10-20
LC-EXPERT, LC-PRACTICE và ba tuyến Academy được giữ trong train T3/T5/T6 tại `PRODUCT_EXECUTION_EXTENSION.*`; demo case/review/credential là DEMO-08/09. Mọi scope practitioner, nội dung, chứng nhận và complaint path vẫn phụ thuộc Q17 cùng evidence quyền/nguồn.


---

# Tổ chức, gia đình và quyền cá nhân không thể bị hòa tan

Mã tài liệu: **D31** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Product + Privacy + Enterprise Lead. Nguồn đối chiếu: S07, S09, S23, S30. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Không gian tổ chức
Workspace quản lý dự án, vai trò, mục tiêu, học tập và năng lực có minh chứng. Thành viên có hồ sơ công việc khác hồ sơ cá nhân; employer không tự đọc journal, tình cảm, sức khỏe hoặc nội dung HNH riêng. Người trả phí có quyền quản lý seat và invoice, không mua quyền đọc tâm trí người khác.
Không sử dụng biểu tượng, ảnh, niềm tin, ngày sinh để xếp hạng tuyển dụng, sa thải, tín dụng hay mức lương. Assessment nghề nghiệp có mục đích, instrument và consent phù hợp; không đổi thành workplace scoring vì khách hàng yêu cầu. Mọi chức năng có tác động lớn cần thẩm định pháp lý riêng.
## 2. Dashboard đội nhóm
Chỉ tổng hợp dữ liệu được phép và có ngưỡng chống nhận dạng lại. Team nhỏ không xuất biểu đồ có thể suy ra từng thành viên; các bộ lọc liên tiếp phải chống differencing. Chưa có ngưỡng đã đánh giá thì trả insufficient_cohort thay vì hiện trung bình. Metrics vận hành dự án không trộn với “năng lượng nhân viên”.
## 3. Family mode
Người trưởng thành tự quản quyền riêng; gia đình không có admin toàn quyền mặc định. Mục tiêu chung và lịch dùng shared objects với quyền riêng. Relationship report hai người chỉ nhận phần mỗi bên đồng ý; một bên rút quyền thì các kết quả kết hợp bị xem lại. Không gửi nhận định về người vắng mặt chỉ từ lời kể một phía như fact.
## 4. Hồ sơ trẻ và người cần đại diện
Family foundation có thể triển khai người trưởng thành trước. Guardian/minor flow mở sau khi country pack, age policy, phạm vi dịch vụ và safeguard được duyệt. Quyền đại diện có evidence, thời hạn, review và quy trình tranh chấp. Trẻ đến tuổi có quyền tự quản cần transition, không tiếp tục để phụ huynh xem dữ liệu vô thời hạn. Dữ liệu phát triển không được dùng để gán nghề hoặc năng lực cố định.
## 5. Tích hợp doanh nghiệp
SSO và SCIM là khả năng về sau tùy khách hàng, không bảo đảm đã có trong beta. Provision seat không đồng nghĩa grant hồ sơ cá nhân. Tenant export có scope; termination bảo toàn quyền riêng và lối ra của thành viên. API key được giới hạn capability/tenant/purpose, rotation và revocation; không dùng một master token xuyên quốc gia.
## 6. Acceptance
Test account đổi tenant, offboard chuyên gia, withdraw share, export tổ chức, audit access và aggregate nhỏ. Một user thuộc hai tổ chức không làm dữ liệu tổ chức A xuất hiện khi dùng context B. Template country partner không được ghi đè các nguyên tắc này.

## Bổ sung thực thi 2026-10-20
Family, organization, API và regional product vẫn thuộc tầm nhìn, được xếp train T6–T8 với stop rule riêng tại `07_PRODUCT_EXECUTION_CHARTER_2026-10-20.md`. DEMO-10 bắt buộc tenant/context negative tests; không có route/UI hoặc thiết kế hoàn tất nào tự cấp quyền tổ chức.


---

# Mô hình thương mại, chi phí và tính bền vững của miễn phí

Mã tài liệu: **D32** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Product + Finance + Commerce. Nguồn đối chiếu: S20, S28, S29, S33. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Không định giá theo độ chính xác tưởng tượng
Giá phản ánh phạm vi dịch vụ, thời gian review, lượng dữ liệu, tệp xuất và hỗ trợ. Không bán “độ đúng95%” hoặc khẳng định gói đắt hơn biết thêm định mệnh. Free education và privacy rights không bị khóa sau thanh toán. Deep content được bán bằng chất lượng đọc, phương pháp minh bạch và hành động có ích.
## 2. Các cấu phần chi phí
Chi phí trực tiếp = deterministic compute + AI + render/storage + editorial + support + payment fees. Contribution = doanh thu thuần – chi phí trực tiếp. Kế hoạch ngân sách bao gồm đội ngũ, legal, security review, translation, licensing sources và dự phòng. Workbook kèm theo dùng INPUT ASSUMPTIONS, không phải báo giá tuyển dụng hoặc cloud hiện hành.
Chi phí free tier được kiểm soát bằng tính local, nguồn nội dung cache công khai, quota AI, chính sách fair use và batch hợp lý. Không tài trợ miễn phí bằng bán nhật ký người dùng. Giới hạn quota ghi rõ trước sử dụng; khi hết có chế độ deterministic và nội dung chung vẫn hữu ích.
## 3. Gói trả phí
One-time Report: scope, một snapshot, định dạng, revision và support cụ thể. Companion: thời hạn, quota, renew/cancel và đường xuất dữ liệu. Expert: chuyên gia, thời lượng, booking/cancel, review và responsibility. Academy: cohort, curriculum, assessment và certificate scope. Workspace/API: seats, capabilities, purpose, rate/cost cap và billing. Regional license có term sheet và legal review riêng.
## 4. Kênh bán
Nội dung giáo dục công khai → công cụ minh bạch → hồ sơ mục tiêu → trải nghiệm có kết quả → gói nâng cao phù hợp. Không dùng nhãn Hung để tạo funnel sợ hãi. Referral disclosure và xung đột lợi ích phải rõ nếu giới thiệu SIM, khóa học hoặc dịch vụ đối tác. Không cho practitioner tự đổi bảng nghĩa để tăng conversion.
## 5. Thước đo thử nghiệm thị trường
Theo dõi mức người dùng hiểu phạm vi, completion mục tiêu, satisfaction với hành động, correction rate, refund reason, support cost và retention tự nguyện. “Thấy luận đúng” không phải chỉ số duy nhất. Không chốt TAM, ROI nhượng quyền hoặc thu nhập giảng viên bằng giả định không nguồn.
## 6. Quyết định mở rộng
Mỗi SKU cần evidence unit economics dưới quota thực, công suất reviewer và tỷ lệ lỗi. Mở miễn phí rộng trước paid không nhất thiết giảm rủi ro; dữ liệu riêng vẫn cần trust gates. Quốc gia mới cần support và legal budget, không chỉ thêm bản dịch. Price list chính thức chờ Founder/Finance/Legal chọn pháp nhân và scope.

## Bổ sung thực thi 2026-10-20
`06_PROGRAM_EXECUTION_PLAN_2026-10-20.md` giữ chi phí dưới dạng công thức labor/vendor/review/licensing/contingency cho tới Q14/Q15/Q20. 452–1.039 person-days là inventory planning sau amendment, không phải báo giá; mọi currency/rate/vendor còn `null`/`BLOCKED`.


---

# Lộ trình, phân công và quản trị phụ thuộc

Mã tài liệu: **D33** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Program Lead + Tech Lead. Nguồn đối chiếu: G02. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Thời gian có điều kiện
T0 là ngày đủ người chủ trì, quyền môi trường và scope được duyệt. P0 ngày 0–3; governance tuần 1–3; Trust Core tuần 2–7; first product tuần 5–14; private paid beta tuần 13–24; Level 2–5/Resonance/Practice tháng 6–10; hợp nhất/mobile/Academy/API tháng 9–18+. Đây là estimate với đội lõi6–8 người và chuyên gia hỗ trợ, không hứa mọi module sức khỏe hoặc trẻ em sẽ mở theo lịch.
Giai đoạn có thể chồng về thiết kế, không mở intake thật trước gates. Research K01–K20 tiếp tục song song nhưng method release không tự theo ngày. Quốc tế/franchise chỉ qua country/legal/brand gate và năng lực vận hành thực.
## 2. Vai trò chịu trách nhiệm
Founder quyết triết lý, phạm vi và Q decisions. Program Lead quản backlog, phụ thuộc và đổi scope. Tech Lead chịu architecture và integration. Backend/Data giữ dữ liệu, quyền, migrations. Frontend giữ UX/a11y/i18n. AI/Knowledge giữ retrieval/policy. Editorial giữ nội dung. QA/Security xác nhận độc lập. SRE giữ release/restore. Legal/Privacy giữ áp dụng luật và quyền. Partnerships/Academic giữ license, đào tạo và chất lượng đại diện thương hiệu.
Một người có thể kiêm nhiệm nhưng người viết không là người duy nhất phê duyệt mọi phần. Mỗi task có accountable owner, reviewer, đầu ra và evidence path. Không dùng “AI team sẽ tự làm tất cả” làm người chịu trách nhiệm.
## 3. Chu kỳ điều hành đề xuất
Stand-up ngắn theo workstream; daily report là snapshot: việc đã hoàn thành có evidence, đang làm, blocked, tác động scope và quyết định cần chốt. Báo cáo hàng giờ cho lane đang dev chỉ nên phản ánh CI/job/commit và blocker, không yêu cầu con người viết lại báo cáo mỗi giờ. Automation có thể chuẩn bị báo cáo, chưa được tạo hoặc lên lịch trong gói bàn giao này.
## 4. Definition of done
Một task code xong phải có contract phù hợp, test, quyền dữ liệu, log đúng, tài liệu dùng và rollback khi liên quan. Task tài liệu phải có nguồn, owner, phiên bản và review; không đánh dấu completed chỉ vì tạo file. Backlog đi kèm mặc định NOT_STARTED cho triển khai production; kiểm thử reference package nằm ở receipt riêng.
## 5. Thay đổi phạm vi
Request mới được phân loại P0 khẩn cấp, sửa hiểu sai, extension phase hoặc backlog. Không âm thầm thêm chức năng vào sprint hiện tại rồi giữ deadline cũ. Khi đổi method contract, chạy impact analysis cho templates, API, translations và báo cáo cũ. Khi đổi luật, country pack phải quyết pending/restrict/release; không sửa trang disclaimer rồi bỏ qua xử lý dữ liệu.

## Bổ sung thực thi 2026-10-20
Phase canonical là P0/A/B/C/D/E/F; `F_REVIEW`, `E_F_REVIEW`, `F_LEGAL` là suffix điều kiện. Critical path, lane song song, capacity, RACI, stop rule và cost formula nằm tại `06_PROGRAM_EXECUTION_PLAN_2026-10-20.md`. 140 task gốc được giữ và chỉ nối thêm task có prefix `UPG-*`.


---

# Mười hai cổng phát hành và yêu cầu bằng chứng

Mã tài liệu: **D34** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Release Authority + QA + Security. Nguồn đối chiếu: S07, S13, S21. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Nguyên tắc
Không kế thừa tỷ lệ3/12 hoặc25% từ audit cũ sang bộ cổng mới. Tất cả gates trong register kèm theo là NOT_CHECKED ở production trong gói này; source evidence có bảng riêng. Không bù lỗi quyền bằng điểm giao diện đẹp. Gate scope được chốt trước, không đánh N/A cho điều cốt lõi chỉ để tăng tỷ lệ.
## 2. Danh sách cổng
G01 Source/Release: source–artifact–runtime–schema liên kết, rollback an toàn. G02 Authentication: xác thực chuẩn, legacy revoked, recovery hợp lệ. G03 Authorization: object/tenant/field/grant kiểm tra và negative tests. G04 Legal/Purpose: phạm vi dịch vụ, mục đích, pháp nhân, notices và country. G05 Retention/Deletion: xóa xuyên hệ và restore không tái sinh dữ liệu. G06 Methods/Claims: passport, rights, rules, null và giới hạn. G07 Legacy/Migration: phân loại quyền và output, đối soát chuyển. G08 Reports/AI: lineage, ngôn ngữ, file và injection tests. G09 Commerce: chữ ký/replay/refund/entitlement. G10 Reliability: tải, retries, backup/restore. G11 Security Review: đánh giá độc lập và retest. G12 Operations/Pilot: support, công suất, incident và phê duyệt scope.
## 3. Bằng chứng mỗi gate
Có người chủ trì, câu hỏi nghiệm thu, môi trường, exact SHA, test run, thời gian, kết quả, người review, ngoại lệ và quyết định. Bằng chứng có PII nằm private, repo chỉ giữ pointer/hash. Link ảnh chụp màn hình không thay toàn bộ test; CI green không thay method review.
## 4. Mở các mức dịch vụ
Containment exit: bề mặt rủi ro đã khóa, không còn output cá nhân giả, tokens cũ vô hiệu, biết deploy và owner incident. Public guest deterministic: thêm bundle privacy, rules tests và copy review. Private alpha: G01–G08 và phần cần thiết G10–G12 theo scope; commerce N/A chỉ nếu thực sự không thu tiền. Paid beta: cả12 gates áp dụng phải pass. Sensitive/children/international: bổ sung cổng riêng, không tự thừa hưởng paid-beta approval.
## 5. Rollback và exception
Exception chỉ dùng cho rủi ro có thể chấp nhận với thời hạn và compensating control; không cho phép bypass quyền chủ thể, giả dữ kiện hoặc tuyên bố sai. Khi không có bản rollback an toàn, chuyển chế độ maintenance/static. Chỉ người được giao quyền mới mở lại. Báo cáo có withdrawn status nếu ảnh hưởng nội dung sau phát hành; người dùng nhận giải thích và quyền xử lý phù hợp.


## Bổ sung ngày 20 tháng 10 năm 2026

G01–G12 là nhóm gate sản phẩm. FPOS_GATE_MAPPING.json ánh xạ đầy đủ RG0–RG13 và là bảng dùng khi review RC. Verdict hiện HOLD; BLOCKED là evidence/gate state. Các nhãn pass cũ không chuyển thành VERIFIED_CURRENT.


---

# Quyết định Q1–Q20: nền cũ và phạm vi mở rộng

Mã tài liệu: **D35** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Founder + Functional Approvers. Nguồn đối chiếu: G02. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Tình trạng phê duyệt
Người dùng đã yêu cầu xuất kế hoạch. Điều đó xác nhận quyền tạo bộ tài liệu này, không tự phê duyệt mọi Q hoặc cho phép deploy. Tất cả Q trong DECISION_REGISTER bắt đầu PENDING_FOUNDER. Quyết định liên quan security/privacy còn cần người phụ trách chức năng ký theo phạm vi.
## 2. Q1–Q12 giữ tương thích kế hoạch audit
Q1 định vị tự hiểu/life design. Q2 giữ9levels/12layers/4reportblocks/12fields/K01–20. Q3 method riêng theo source/version. Q4 entitlement khác eligibility/data. Q5 dừng score giả, cho null. Q6 Numbers là reference không đo số phận. Q7 content model chung, không filler. Q8 mở dòng sản phẩm theo gates. Q9 privacy/auth/delete từ đầu. Q10 xuất tám bộ nền từ baseline đã khóa. Q11 quarantine experimental_legacy. Q12 không release method thiếu passport/rights/tests/limits/approver.
## 3. Q13–Q20 cho phạm vi mới
Q13 Free Essentials: một hồ sơ tự quản, mục tiêu, nhật ký và privacy rights; quota AI/chi phí proposal. Q14 pháp nhân/merchant/controller và mô hình trách nhiệm. Q15 chọn IdP, PostgreSQL host, payment và AI providers qua ADR/vendor assessment. Q16 mức tự chủ A0–A3 và quyền dừng. Q17 Academy/practitioner certification scope và review. Q18 organization privacy boundaries, không high-impact profiling. Q19 country-pack order và mô hình license/franchise. Q20 ngân sách, đội lõi, nghiệm thu và lịch có điều kiện.
## 4. Cách duyệt
Mỗi Q trả APPROVE, APPROVE_WITH_CONDITIONS, REVISE hoặc REJECT; ghi điều kiện, phạm vi, ngày và approver. Câu “đồng ý tiếp tục” chỉ áp dụng cho hành động được nói rõ. Nếu chưa chọn provider, dùng adapter contract và decision TBD thay vì giả vờ đã ký hợp đồng. Không đặt placeholder bí mật trong file để user có thể lỡ chia sẻ credentials.
## 5. Quyết định không thể thay bằng marketing
Không chữ ký nào biến hình thái thành phép đo đạo đức hoặc số học thành bằng chứng bệnh tật. Founder có thể chọn ngôn ngữ biểu tượng và triết lý HNH nhưng sản phẩm vẫn phải gắn đúng loại nhận định. Nội dung thương hiệu công khai cần biên tập trước khi phát hành và kiểm tra trên các locale đã mở.

## Bổ sung thực thi 2026-10-20
Các artifact 2026-10-20 chỉ liên kết dependency Q1–Q20 và không đổi trạng thái `PENDING_FOUNDER`. `DECISION_EXECUTION_PACKETS.json` và `.csv` cung cấp ba phương án loại trừ nhau, phương án khuyến nghị cùng trade-off, dependency, task ảnh hưởng, trạng thái chi phí, vai trò duyệt, sự kiện phải quyết định và hợp đồng receipt cho từng Q. Đây là packet để review, không phải lựa chọn đã được duyệt. Mỗi quyết định vẫn cần baseline, phạm vi, điều kiện, approver thật và thời gian; không suy approval từ việc Founder yêu cầu hoàn thiện kế hoạch.


---

# Giao việc cho AI và DEV: bối cảnh, lệnh thực hiện và báo cáo

Mã tài liệu: **D36** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Tech Lead + AI Engineering. Nguồn đối chiếu: G02, G09, G10. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Start here cho đội thực thi
Đọc README và baseline, quyết định Q, P0 runbook, source-target matrix, contracts và task tương ứng. Không bắt đầu bằng build UI mới. Kiểm tra repo/branch/HEAD, môi trường, clean working copy ngoài iCloud và quyền được giao. Chưa có receipt thì báo BLOCKED_RECEIPT, không tự đoán deployed SHA.
## 2. Hợp đồng một work item
Mỗi task phải có mục tiêu, scope files, inputs, dependencies, forbidden actions, acceptance, tests, rollback và output evidence. AI chỉ làm trong branch được giao; không sửa shared schema hoặc policy ngoài scope. Không dùng dữ liệu khách làm fixture. Một commit nhỏ với test và giải thích tốt hơn nhiều sửa đổi lan rộng thiếu integration owner.
## 3. Báo cáo cuối phiên
Ghi file thay đổi, logic thay đổi, test đã chạy, test chưa chạy, lỗi/blocked, diff summary, risk, review yêu cầu và next task. Không báo90% done khi chưa biết denominator. Không ghi tests pass nếu mới đọc package.json. AI không được tự quảng bá production-ready chỉ vì sample chạy.
## 4. Commands và secret
Trong bộ này, reference scripts chỉ chạy trong container/local với dữ liệu tổng hợp. Không có script tự deploy, migrate production, revoke session thật hoặc reset repo. Hướng dẫn production cần scope riêng và người duyệt. Secret truyền qua manager/CI, không paste vào chat hay doc. `.env.example` nếu tạo về sau chỉ chứa tên biến không giá trị; giá trị thiếu ghi rõ required decision.
## 5. Handover prompts
Prompt cho backend yêu cầu triển khai owner-scoped queries theo OpenAPI và auth matrix, không tin client IDs. Prompt frontend yêu cầu không tính score riêng, đủ states/a11y, không log payload. Prompt method yêu cầu passport và tests. Prompt AI yêu cầu claim-driven writer, retrieval ACL. Prompt QA yêu cầu negative tests. Prompt release yêu cầu build allowlist/receipt/rollback và không deploy khi chưa có quyền.
## 6. Tái sử dụng và đổi phiên bản
Lõi hiện tại JS/TS được tái cấu trúc theo package; không chuyển hết sang Python chỉ để có kiến trúc đẹp. Legacy templates bị deprecated, không âm thầm dùng khi thiếu content mới. Khi phát hiện mâu thuẫn tài liệu, báo decision cần chốt thay vì chọn lời thuận lợi. Artifact package này là baseline thiết kế chờ phê duyệt, không phải patch repository.

## Bổ sung thực thi 2026-10-20
`TASK_EXECUTION_CONTRACTS.*` cung cấp allowed paths/dependencies/tests/negative tests/evidence/roles/estimate cho đủ task; `REQUIREMENT_TRACE_MATRIX.*` nối requirement→screen→operation_id→task→test→evidence. Production permission của mọi task vẫn `SEPARATE_APPROVAL_REQUIRED`.


---


# Tài liệu kỹ thuật chi tiết bổ sung

Các hợp đồng công thức, ma trận phương pháp, demo fixtures, OpenAPI, migration, UI đa thiết bị, AI/report và task acceptance được tra theo INDEX.html và các README thư mục. File JSON/schema là artifact máy đọc của cùng phiên bản. Toàn bộ 149 tệp gốc và ZIP được giữ trong sources cùng checksum.


---


# Nguồn đối chiếu


---


### G01 Remote branches

https://api.github.com/repos/tranhatam-collab/Life-Code-OS/branches?per_page=100

Phạm vi: GitHub connector GET; đọc danh sách nhánh. Giới hạn: Không phải deployed SHA.


---


### G02 Kế hoạch audit 1.096 dòng

https://github.com/tranhatam-collab/Life-Code-OS/blob/336ef35a8386a744c6de18a7f7c6e268e89e6dac/docs/audit/LIFE_CODE_OS_COMPREHENSIVE_UPGRADE_PLAN_2026-10-11.md

Phạm vi: Đọc các dải nội dung toàn tài liệu qua GitHub; trạng thái PROPOSED_FOR_TEAM_AUDIT. Giới hạn: Các kết quả live của tác giả audit là nguồn khai báo, không mặc nhiên là đo lại trong phiên này.


---


### G03 Kiến trúc 9 level cũ

https://github.com/tranhatam-collab/Life-Code-OS/blob/99b402764437f81859fa0cd3a3af860125f7bd52/docs/LEVELS_ARCHITECTURE_V1.md

Phạm vi: Đã đọc nội dung. Giới hạn: Nguồn lịch sử chưa ghi; cần tái kiểm tra trước áp dụng.


---


### G04 API routes: profile và session

https://github.com/tranhatam-collab/Life-Code-OS/blob/99b402764437f81859fa0cd3a3af860125f7bd52/workers/life-code-api/src/index.js#L653-L760

Phạm vi: Đọc nhánh xử lý mã remote. Giới hạn: Không thử lấy hồ sơ người thật; không xác nhận exploit runtime.


---


### G05 LCI legacy

https://github.com/tranhatam-collab/Life-Code-OS/blob/99b402764437f81859fa0cd3a3af860125f7bd52/engine/core/lci.js

Phạm vi: Đã đọc trong audit đối chiếu của chuỗi trao đổi, cùng SHA. Giới hạn: Nguồn lịch sử chưa ghi; cần tái kiểm tra trước áp dụng.


---


### G06 Timeline legacy

https://github.com/tranhatam-collab/Life-Code-OS/blob/99b402764437f81859fa0cd3a3af860125f7bd52/engine/core/timeline.js

Phạm vi: Đã đọc trong audit đối chiếu của chuỗi trao đổi, cùng SHA. Giới hạn: Nguồn lịch sử chưa ghi; cần tái kiểm tra trước áp dụng.


---


### G07 Biểu mẫu Bắt đầu

https://github.com/tranhatam-collab/Life-Code-OS/blob/99b402764437f81859fa0cd3a3af860125f7bd52/bat-dau.html#L250-L320

Phạm vi: Đã đọc đoạn gửi payload trong chuỗi audit, cùng SHA. Giới hạn: Nguồn lịch sử chưa ghi; cần tái kiểm tra trước áp dụng.


---


### G08 Migration session

https://github.com/tranhatam-collab/Life-Code-OS/blob/99b402764437f81859fa0cd3a3af860125f7bd52/workers/life-code-api/migrations/002_create_sessions.sql

Phạm vi: Đã đọc trong chuỗi audit, cùng SHA. Giới hạn: Nguồn lịch sử chưa ghi; cần tái kiểm tra trước áp dụng.


---


### G09 Pages build script

https://github.com/tranhatam-collab/Life-Code-OS/blob/99b402764437f81859fa0cd3a3af860125f7bd52/scripts/prepare-pages.sh

Phạm vi: Đã đọc trực tiếp. Giới hạn: Denylist còn có thể để lọt file mới; chưa đo bundle live.


---


### G10 Workflow Pages

https://github.com/tranhatam-collab/Life-Code-OS/blob/99b402764437f81859fa0cd3a3af860125f7bd52/.github/workflows/deploy-pages.yml

Phạm vi: Đã đọc trực tiếp. Giới hạn: Có --commit-dirty=true; không có bước smoke/security trong workflow đã đọc.


---


### G11 Report API legacy

https://github.com/tranhatam-collab/Life-Code-OS/blob/99b402764437f81859fa0cd3a3af860125f7bd52/workers/life-code-api/src/index.js#L1014-L1065

Phạm vi: Đã đọc trong chuỗi audit, cùng SHA. Giới hạn: Nguồn lịch sử chưa ghi; cần tái kiểm tra trước áp dụng.


---


### G12 Audit commit metadata

https://github.com/tranhatam-collab/Life-Code-OS/commit/336ef35a8386a744c6de18a7f7c6e268e89e6dac

Phạm vi: Đã đọc metadata và diff tài liệu. Giới hạn: Không phải commit sửa P0.


---


### S01 Life Code trang chủ

https://lifecode.iai.one/

Phạm vi: Nội dung HTML qua công cụ web; nguồn báo crawled yesterday. Giới hạn: Không xác nhận byte hash, HTTP headers hoặc deployed SHA.


---


### S02 Life Code chín tầng

https://lifecode.iai.one/9-levels-life-code

Phạm vi: Đọc nội dung công khai qua liên kết clean URL. Giới hạn: Nguồn lịch sử chưa ghi; cần tái kiểm tra trước áp dụng.


---


### S03 Life Code Bắt đầu

https://lifecode.iai.one/bat-dau

Phạm vi: Đọc giao diện biểu mẫu; không gửi dữ liệu. Giới hạn: Nguồn lịch sử chưa ghi; cần tái kiểm tra trước áp dụng.


---


### S04 Life Code Dashboard

https://lifecode.iai.one/dashboard

Phạm vi: Đọc nội dung giao diện public; không đăng nhập. Giới hạn: Nguồn lịch sử chưa ghi; cần tái kiểm tra trước áp dụng.


---


### S05 Life Code chính sách bảo mật

https://lifecode.iai.one/chinh-sach-bao-mat

Phạm vi: Đã đọc nội dung công khai. Giới hạn: Nguồn lịch sử chưa ghi; cần tái kiểm tra trước áp dụng.


---


### S06 Life Code Engine Lab

https://lifecode.iai.one/engine-lab

Phạm vi: Đọc giao diện; không gửi POST. Giới hạn: Nguồn lịch sử chưa ghi; cần tái kiểm tra trước áp dụng.


---


### S07 OWASP API BOLA

https://api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/

Phạm vi: Đã đọc trang chính thức. Giới hạn: Nguồn lịch sử chưa ghi; cần tái kiểm tra trước áp dụng.


---


### S08 OWASP Session Management

https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html

Phạm vi: Đã đọc trang chính thức. Giới hạn: Nguồn lịch sử chưa ghi; cần tái kiểm tra trước áp dụng.


---


### S09 PostgreSQL Row Security

https://www.postgresql.org/docs/current/ddl-rowsecurity.html

Phạm vi: Đã đọc trang chính thức. Giới hạn: Trang current được trả là tài liệu PostgreSQL 18; không coi database dự án đã nâng cấp.


---


### S10 Cloudflare Queues delivery guarantees

https://developers.cloudflare.com/queues/reference/delivery-guarantees/

Phạm vi: Đã đọc trang chính thức. Giới hạn: Nguồn lịch sử chưa ghi; cần tái kiểm tra trước áp dụng.


---


### S11 Cloudflare R2 presigned URL

https://developers.cloudflare.com/r2/api/s3/presigned-urls/

Phạm vi: Đã đọc trang chính thức. Giới hạn: Nguồn lịch sử chưa ghi; cần tái kiểm tra trước áp dụng.


---


### S12 Hyperdrive query caching

https://developers.cloudflare.com/hyperdrive/concepts/query-caching/

Phạm vi: Đã đọc trang chính thức. Giới hạn: Nguồn lịch sử chưa ghi; cần tái kiểm tra trước áp dụng.


---


### S13 Cloudflare Workers versions/deployments

https://developers.cloudflare.com/workers/versions-and-deployments/

Phạm vi: Đã đọc trang chính thức. Giới hạn: Nguồn lịch sử chưa ghi; cần tái kiểm tra trước áp dụng.


---


### S14 OpenAPI 3.1.1

https://spec.openapis.org/oas/v3.1.1.html

Phạm vi: Đã đọc trang chính thức. Giới hạn: Nguồn lịch sử chưa ghi; cần tái kiểm tra trước áp dụng.


---


### S15 Unicode Normalization

https://unicode.org/reports/tr15/

Phạm vi: Đã đọc trang chính thức. Giới hạn: Nguồn lịch sử chưa ghi; cần tái kiểm tra trước áp dụng.


---


### S16 IANA Time Zone Database

https://www.iana.org/time-zones

Phạm vi: Đã đọc trang chính thức. Giới hạn: Nguồn lịch sử chưa ghi; cần tái kiểm tra trước áp dụng.


---


### S17 WCAG 2.2

https://www.w3.org/TR/WCAG22/

Phạm vi: Đã đọc trang chính thức. Giới hạn: Nguồn lịch sử chưa ghi; cần tái kiểm tra trước áp dụng.


---


### S18 Astro deployment Cloudflare

https://docs.astro.build/en/guides/deploy/cloudflare/

Phạm vi: Đã đọc trang chính thức. Giới hạn: Nguồn lịch sử chưa ghi; cần tái kiểm tra trước áp dụng.


---


### S19 React Quick Start

https://react.dev/learn

Phạm vi: Đã đọc trang chính thức. Giới hạn: Nguồn lịch sử chưa ghi; cần tái kiểm tra trước áp dụng.


---


### S20 Stripe webhook guidance

https://docs.stripe.com/webhooks

Phạm vi: Đã đọc trang chính thức. Giới hạn: Tham chiếu giao thức; chưa chọn Stripe làm nhà cung cấp khả dụng cho pháp nhân dự án.


---


### S21 NIST AI Risk Management Framework

https://www.nist.gov/itl/ai-risk-management-framework

Phạm vi: Đã đọc trang chính thức. Giới hạn: Nguồn lịch sử chưa ghi; cần tái kiểm tra trước áp dụng.


---


### S22 ISO/IEC 42001 overview

https://www.iso.org/standard/42001

Phạm vi: Đọc trang giới thiệu tiêu chuẩn. Giới hạn: Chưa đọc toàn văn tiêu chuẩn trả phí; không chứng nhận tuân thủ.


---


### S23 Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15

https://vanban.chinhphu.vn/?docid=214590&pageid=27160

Phạm vi: Đọc metadata chính thức. Giới hạn: Hiệu lực 01/01/2026; chưa thay ý kiến pháp lý áp dụng.


---


### S24 Nghị định 356/2025/NĐ-CP

https://chinhphu.vn/?classid=1&docid=216387&orggroupid=2&pageid=27160

Phạm vi: Đọc metadata chính thức. Giới hạn: Nguồn lịch sử chưa ghi; cần tái kiểm tra trước áp dụng.


---


### S25 Luật Trí tuệ nhân tạo 134/2025/QH15

https://congbao.chinhphu.vn/van-ban/luat-so-134-2025-qh15-468694/61695.htm

Phạm vi: Đọc metadata chính thức. Giới hạn: Hiệu lực 01/03/2026.


---


### S26 Nghị định 142/2026/NĐ-CP

https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-142-2026-nd-cp-469480/64703.htm

Phạm vi: Đọc metadata chính thức. Giới hạn: Hiệu lực 01/05/2026.


---


### S27 Khung pháp lý AI - Cục Công nghệ số và AI

https://dda.gov.vn/khung-phap-ly-ai

Phạm vi: Đã đọc trang chính thức. Giới hạn: Nguồn lịch sử chưa ghi; cần tái kiểm tra trước áp dụng.


---


### S28 Nghị định 248/2026/NĐ-CP

https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-248-2026-nd-cp-469983.htm

Phạm vi: Đọc metadata chính thức. Giới hạn: Hiệu lực 01/07/2026.


---


### S29 Bộ Công Thương phổ biến Luật TMĐT và Nghị định 248

https://moit.gov.vn/tin-tuc/bo-cong-thuong-pho-bien-luat-thuong-mai-dien-tu-va-nghi-dinh-so-248-2026-nd-cp.html

Phạm vi: Đã đọc trang chính thức. Giới hạn: Nguồn xác nhận hiệu lực từ 01/07/2026; cần pháp lý đọc văn bản ký.


---


### S30 EU GDPR

https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng

Phạm vi: Truy cập văn bản pháp quy; rà soát định nghĩa và quyền. Giới hạn: Không thay đánh giá tác động hoặc tư vấn thị trường cụ thể.


---


### S31 EU AI Act application timeline

https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai

Phạm vi: Đã đọc trang chính thức. Giới hạn: Trang Ủy ban được kiểm tra 11/10/2026; thể hiện AI Omnibus có hiệu lực 27/07/2026 và lịch high-risk điều chỉnh. Đối chiếu văn bản hợp nhất trước launch.


---


### S32 EU AI Act - bản tiếng Hà Lan

https://digital-strategy.ec.europa.eu/nl/policies/regulatory-framework-ai

Phạm vi: Đối chiếu phần lịch áp dụng đa ngôn ngữ. Giới hạn: Nguồn lịch sử chưa ghi; cần tái kiểm tra trước áp dụng.


---


### S33 FTC Consumer Guide to Buying a Franchise

https://www.ftc.gov/business-guidance/resources/consumers-guide-buying-franchise

Phạm vi: Đã đọc trang chính thức. Giới hạn: Thông tin FDD/14 ngày, không phải ý kiến phân loại hợp đồng Life Code.


---


### S34 ACCC Franchising Code

https://www.accc.gov.au/business/industry-codes/franchising-code-of-conduct

Phạm vi: Đã đọc trang chính thức. Giới hạn: Bộ quy tắc mới 01/04/2025; một số quy định 01/11/2025.


---


### S35 ACCC franchise disclosure document

https://www.accc.gov.au/business/industry-codes/franchising-code-of-conduct/franchise-disclosure-document

Phạm vi: Đã đọc trang chính thức. Giới hạn: Nguồn lịch sử chưa ghi; cần tái kiểm tra trước áp dụng.


---


### S36 Bộ Công Thương danh mục nhượng quyền

https://moit.gov.vn/nhuong-quyen-thuong-mai

Phạm vi: Đọc danh mục công khai. Giới hạn: Không đủ kết luận thủ tục outbound cho Life Code; pháp lý phải xác minh.


---


### S37 WIPO Madrid filing

https://www.wipo.int/en/web/madrid-system/how_to/file/index

Phạm vi: Đã đọc trang chính thức. Giới hạn: Đăng ký quốc tế không bảo đảm được bảo hộ ở mọi thị trường; không xác minh nhãn Life Code đã đăng ký.


---


### S38 IPIP ngân hàng mục hỏi

https://ipip.ori.org/

Phạm vi: Đã đọc trang chính thức. Giới hạn: Phải kiểm tra quyền của từng bản dịch và thang; chưa xác nhận giá trị đo trên mẫu Life Code.


---


### S39 O*NET Interest Profiler

https://www.onetcenter.org/IP.html

Phạm vi: Đã đọc trang chính thức. Giới hạn: Dùng phạm vi hứng thú nghề; không quyết định nghề bắt buộc.


---


### S40 OAIC privacy rights

https://www.oaic.gov.au/privacy/your-privacy-rights

Phạm vi: Đã đọc trang chính thức. Giới hạn: Điểm xuất phát rà soát Australia; chưa audit nghĩa vụ cụ thể.


---


### S41 Singapore PDPC PDPA

https://www.pdpc.gov.sg/overview-of-pdpa/the-legislation/personal-data-protection-act

Phạm vi: Trang phản hồi rất ít nội dung. Giới hạn: Chưa đủ nội dung để khẳng định điều khoản; rà soát trước launch.


---


### R20-01 Vietnam AI Law134/2025

https://vanban.chinhphu.vn/?docid=216334&orggroupid=1&pageid=27160

Đọc 20/10: Metadata; effective2026-03-01. Giới hạn: Metadata verified; full applicability not reviewed.


---


### R20-02 Vietnam Decree142/2026

https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-142-2026-nd-cp-469480/64703.htm

Đọc 20/10: Metadata; effective2026-05-01. Giới hạn: 97-page document linked; full text not read in this research pass.


---


### R20-03 Vietnam Ecommerce Law122/2025

https://congbao.chinhphu.vn/van-ban-dang-cong-bao/luat-l13/trang-6.htm

Đọc 20/10: Gazette metadata; effective2026-07-01. Giới hạn: Counsel must retrieve signed text and transition rules.


---


### R20-04 Vietnam Decree248/2026

https://congbao.chinhphu.vn/van-ban/nghi-dinh-so-248-2026-nd-cp-469983.htm

Đọc 20/10: Metadata; effective2026-07-01. Giới hạn: 93-page document linked; full applicability not reviewed.


---


### R20-05 Vietnam Personal Data Law91/2025

https://vanban.chinhphu.vn/?docid=214590&pageid=27160

Đọc 20/10: Metadata; effective2026-01-01. Giới hạn: No compliance conclusion from metadata.


---


### R20-06 EU AI Act Commission guidance

https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai

Đọc 20/10: Risk-based application overview. Giới hạn: Recheck consolidated law, amendments and timetable per country launch.


---


### R20-07 PostgreSQL18 Row Security

https://www.postgresql.org/docs/18/ddl-rowsecurity.html

Đọc 20/10: Technical RLS behavior and bypass roles. Giới hạn: Does not verify project DB, provider or SQL execution.


---


### R20-08 Cloudflare Queues delivery

https://developers.cloudflare.com/queues/reference/delivery-guarantees/

Đọc 20/10: At-least-once delivery design basis. Giới hạn: No account provisioning or runtime receipt.

