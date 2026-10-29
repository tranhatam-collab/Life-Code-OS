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
