# Life Code OS Nghiệm thu vận hành và khôi phục

Cập nhật 20/10/2026. Bổ sung D27 và CI_RELEASE_POLICY trong phạm vi tiêu chí chuẩn bị dev. Mọi target là đề xuất đo trên staging và pilot, chưa là số đo hoặc SLA hiện tại. Dữ liệu máy đọc nằm trong `OPERATIONS_ACCEPTANCE.json`.

## Service ownership và môi trường

Service catalog phải có public site, user web/BFF, auth/session, method core, database, job worker/outbox, private object store/report renderer, AI gateway và observability/support. Mỗi service có named accountable owner và backup owner trước pilot; hiện chỉ phân vai dự kiến. Registry provider/account/region/binding/version lưu ở kho có quyền, trong repo giữ pointer và hash không có secret.

Local dùng fake provider, ephemeral storage và synthetic accounts. CI không có production credentials. Staging dùng account/bucket/DB/queues tách riêng, mail/payment sandbox và chặn recipient thật. Production có environment authorization riêng và chỉ nhận immutable artifact. Mỗi resource được đặt environment/project labels và kiểm tra binding parity trước rollout.

## SLI và target beta

Availability tính `successful_eligible_requests / eligible_requests` trên cửa sổ lăn 30 ngày, target 0,995. Eligible là request hợp lệ trong quota đã cam kết; expected 4xx vì input/policy bị loại với reason code đã định nghĩa. Timeout, 5xx, overload 429 và lỗi provider của request eligible tính thất bại. Không loại maintenance hoặc lỗi nội bộ khỏi denominator để làm số đẹp. Khi không có eligible requests, SLI unavailable; không ghi 100%.

Latency API thông thường dùng p95 end-to-end dưới 800 ms, đo từ BFF ingress đến response byte cuối trong cùng region/cohort; không đưa report generation vào API latency. Ghi sample size, request mix, payload sizes, cache hit, cold starts và success/failure separately. Mục tiêu report Level 1 là ít nhất 95% job eligible hoàn tất trong 300 giây từ accepted đến artifact sẵn sàng; failed/timed-out job không được biến mất khỏi denominator.

RPO đề xuất tối đa 1 giờ cho dữ liệu nghiệp vụ và RTO tối đa 4 giờ đến trạng thái phục vụ an toàn. Bằng chứng phải chứng minh khoảng thiếu dữ liệu thực tế sau restore, không chỉ lịch backup. Khôi phục deletion tombstones, revocations, method revocations và idempotency/payment ledger trước khi mở lại.

## Cảnh báo có hành động

Auth cross-owner/cross-tenant hoặc private-data cache leak dù một lần là P0: ngừng surface liên quan, giữ bằng chứng tối thiểu và gọi Incident Commander + Security + Privacy. Chưa có người trực thì surface không đủ điều kiện pilot.

Error-budget burn dùng error_ratio/0,005, hai cửa sổ để hạn chế nhiễu. Đề xuất page khi burn trên 14,4 ở cả 5 phút và 1 giờ, ít nhất 20 eligible requests mỗi cửa; cảnh báo ticket khi burn trên 6 ở cả 30 phút và 6 giờ. Với low traffic, dùng synthetic allowlisted và cảnh báo lỗi kéo dài; không dùng denominator quá nhỏ để chốt reliability.

Queue oldest age trên 60 giây 5 phút liên tiếp, DLQ có message trên 10 phút, report p95 vượt 300 giây, DB pool saturation trên 80% 10 phút hoặc restore receipt quá hạn phải có runbook và owner. Đây là cấu hình khởi điểm để thử tải và điều chỉnh có evidence.

## Chạy diễn tập khôi phục

1. Chốt backup artifact, thời điểm, version DB/schema/method, encryption-key access theo quyền và recovery owner.
2. Tạo environment isolated, outbound allowlist và sandbox integrations. Không restore PII vào laptop DEV hoặc staging dùng chung.
3. Restore theo runbook provider; ghi commands đã redacted, exit codes, start/end, restore point và recovery point thực tế.
4. Đối soát counts theo tenant/table, foreign keys, orphan rows, immutable version IDs và sample checksum được phép. Không chỉ so tổng row count.
5. Replay deletion/revocation và kiểm tra account A/B, grant revoked, method revoked, legal hold và pending jobs. Các job cũ không được phát hành báo cáo hoặc cấp entitlement lần hai.
6. Đo RPO/RTO; QA độc lập kiểm tra synthetic journeys. Nếu có mismatch, giữ environment đóng và ghi reconciliation ledger.
7. Người có authority mới quyết định mở lại. Lưu recovery receipt và thời hạn review; sau thay schema/key/provider phải chạy lại phần bị ảnh hưởng.

Diễn tập trước pilot, trước thay đổi migration lớn, sau đổi cơ chế backup/key và tối thiểu mỗi quý là proposal vận hành. Kiểm tra backup integrity hàng ngày không thay restore drill.

## Rollout và rollback

Release packet phải có full SHA, clean-tree receipt, lockfile/artifact digest, schema/method/prompt/template versions, test evidence, gate dispositions, provider IDs và approver. Canary theo cohort đã đồng ý; không trộn traffic test với người không trong scope.

Rollback application chỉ dùng artifact đã xác nhận không có lỗi security bị chặn. Database thay đổi theo expand/contract, có compatibility window và checkpoint trước destructive step. Không chạy SQL reference trong gói như migration production. Nếu không có artifact an toàn, chuyển static/maintenance và giữ quyền xuất/xóa/liên hệ theo policy được duyệt.

## Capacity và chi phí

Trước pilot chạy workloads 1, 10 và 50 concurrent synthetic users; đây là mức thử ban đầu, không là capacity cam kết. Mỗi mức có ramp 5 phút, steady 15 phút, recovery 5 phút; profile login/read/save/report riêng và mixed load. Kiểm tra connection pool, queue backlog, render memory, AI budget, timeout và retry amplification. Staging load được scope riêng để không phát sinh phí ngoài quota.

Budget đề xuất dùng cảnh báo ở 50%, 75%, 90% và hard stop cho tác vụ AI không thiết yếu ở 100% cap đã duyệt; đọc/sửa/xóa dữ liệu không bị khóa vì AI hết ngân sách. Cap chưa được phê duyệt thì không bật AI production. Không đặt đơn giá giả; workbook giữ quote date/currency/tax/region/limits và missing inputs.

## Incident và hỗ trợ

Incident receipt ghi detection time, affected environment/version, observed impact, known/unknown, containment, evidence pointer, decision log và notification assessment. Source bug, suspected exploitation và confirmed data incident là ba trạng thái khác nhau. Legal xác định nghĩa vụ thông báo từng quốc gia từ thời điểm liên quan; không áp một deadline toàn cầu trong code.

Support beta cần giờ hỗ trợ công khai do owner chốt, escalation cho privacy/security và đường liên hệ ngoài app. Dùng macro giải thích score thiếu dữ liệu, thu hồi báo cáo, chỉnh input, hoàn tiền và quyền dữ liệu. Mỗi tháng review SLO, incident, restore age, cost/user, provider terms và rights expiry; mỗi quý review threat model và capacity.
