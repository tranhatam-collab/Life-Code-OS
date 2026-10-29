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
