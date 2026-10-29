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
