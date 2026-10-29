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
