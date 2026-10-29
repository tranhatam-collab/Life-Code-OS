# Tác vụ nền, thanh toán, xóa dữ liệu và tình huống gián đoạn

**Life Code OS · Bản nâng cấp bảo toàn V2 · 20/10/2026**  
**Trạng thái:** Đặc tả để triển khai và rà soát; không phải chứng nhận production.

## 1. Outbox và worker lease
Outbox nằm cùng database transaction với nghiệp vụ. Publisher có lease, retry và trạng thái dispatched; giao lại không tạo side effect mới. Worker nhận operation_id và payload_digest, kiểm tra idempotency theo tenant+operation+key. Payload khác trên cùng khóa trả conflict. Có max_attempts, next_attempt_at, dead-letter và công cụ review có quyền. Không retry vô hạn.

## 2. State machine
Analysis: queued→running→review_required→approved→published, với nhánh blocked/cancelled/failed. Report: draft→reviewed→released→withdrawn/deleted. Payment order: created→pending→paid→fulfilled với nhánh failed/cancelled/refund_requested/refunded. Deletion: requested→verified→blocked_new_work→purging→provider_pending→completed, có legal_hold riêng. Trạng thái là nghiệp vụ, không một chuỗi tùy ý client gửi.

## 3. Thanh toán
Webhook xác minh chữ ký bằng raw body; kiểm tra event ID, merchant/order, currency và amount. Event trùng nhận lại không cấp entitlement thêm. Redirect trình duyệt không là chứng từ thanh toán. Refund có giới hạn tự động theo chính sách được phê duyệt; ngoại lệ cần người có quyền. Đơn vị thu tiền và chính sách thuế chưa chọn không được giả làm hoàn tất.

## 4. Thu hồi và xóa xuyên hệ
Deletion chặn job mới trước khi xóa vật lý. Lineage chỉ ra profile, observation, result, report, vector, cache, export và object liên quan. Provider AI có chính sách lưu giữ phải được đánh giá riêng; chưa xác minh được thì không nói đã xóa mọi nơi. Backup giữ theo lịch và không phục vụ trực tiếp; khi restore phải áp tombstone trước mở traffic. Audit tránh lưu raw sensitive payload để không tạo bản sao không thể xóa.

## 5. Queue failure scenarios
Kiểm thử worker chết trước/giữa/sau render; provider timeout nhưng trả thành công muộn; notification gửi hai lần; grant revoked khi render; file upload hoàn tất nhưng job không ghi receipt; database rollback; không đủ disk; PDF quá lớn; webhook đến ngược thứ tự. Mỗi trường hợp có trạng thái, cách reconcile và người xử lý, không chỉ ghi log error.

## 6. Receipt
Receipt chứa job ID, attempt, input digest, method/report release, access revision, code artifact, latency, chi phí, result digest và trạng thái. Nó không chứa token, URL ký trước còn sống, raw prompts nhạy cảm hoặc secret. Receipt của demo Map là bằng chứng local, không bằng chứng database transaction thật.
