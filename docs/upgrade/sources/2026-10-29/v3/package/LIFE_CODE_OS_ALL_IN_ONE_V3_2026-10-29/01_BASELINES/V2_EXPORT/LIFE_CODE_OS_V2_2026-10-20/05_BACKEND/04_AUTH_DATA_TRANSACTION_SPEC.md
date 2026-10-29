# Quyền dữ liệu, transaction và chống truy cập chéo

**Life Code OS · Bản nâng cấp bảo toàn V2 · 20/10/2026**  
**Trạng thái:** Đặc tả để triển khai và rà soát; không phải chứng nhận production.

## 1. Identity boundary
Session-derived account_id là nguồn danh tính; payload user_id không cấp quyền. Tài khoản khác subject. Grant chứa tenant, subject, grantee, purpose, actions, expiry, revision và state. Giao dịch đọc/ghi kiểm tra processing basis đang hợp lệ và resource state. Consent không thay authentication; entitlement không thay grant. [N09]

## 2. Mô hình tenant
Self workspace có tenant riêng hoặc namespace tương đương theo quyết định schema. Organization membership chỉ cho quyền công việc, không làm tất cả subject trong tổ chức trở thành dữ liệu quản trị có thể đọc. Composite foreign keys dùng (tenant_id,subject_id,id) để child không tham chiếu sang parent khác chủ thể. Role ứng dụng không là owner/superuser và không BYPASSRLS. [N02]

## 3. RLS và pool
Mỗi transaction đặt SET LOCAL context từ server sau xác thực. Không nhận tenant/account headers trực tiếp từ client. Không dựa vào SET dài hạn vì connection pool tái sử dụng kết nối. Policy deny-by-default, FORCE RLS cho bảng phù hợp; quyền của background worker cũng phải qua context tương ứng. Pool/query cache không dùng lại kết quả cá nhân hóa giữa tenant; cache key và grant revision được thiết kế rõ.

## 4. Kiểm tra quyền hai lần cho job
Trước khi enqueue kiểm tra quyền. Khi worker claim job kiểm tra lại. Trước publish/download kiểm tra lại lần nữa. Nếu grant bị thu hồi, job chuyển BLOCKED_REVOKED và không tiếp tục xuất. Snapshot quyền không cho phép job vượt một lần thu hồi về sau. File đã tải xuống không thể hứa thu hồi vật lý.

## 5. Chống cập nhật mất dữ liệu
Update dùng expected_version hoặc If-Match. Server cập nhật với điều kiện version=expected; không có dòng cập nhật trả 412/409 theo contract thống nhất. Không dùng last-write-wins cho ngày sinh, consent hoặc report approval. Người dùng được xem khác biệt và tạo phiên bản kế tiếp có chủ ý.

## 6. Transaction boundaries
Tạo run, outbox event và idempotency receipt trong cùng transaction. Provider call không giữ transaction DB mở lâu. Sau call, ghi kết quả bằng compare-and-set/unique constraint. Nếu worker chết giữa side effect và receipt, phải có reconciliation theo khóa provider; không tuyên bố exactly-once từ queue at-least-once. [N03]

## 7. Negative tests
A không đọc/write/report/download subjectB. Tenant khác cùng idempotency key không chia kết quả. Grant expired/revoked/wrong-purpose bị chặn. Role developer không đọc PII production. Malformed grant fail closed. PostgreSQL policy cần được chạy bằng role runtime thật trên staging, không kiểm thử bằng superuser rồi đánh dấu đạt.

**Tra nguồn:** xem `11_SOURCES/SOURCE_ADDENDUM.csv`; các mã Nxx là nguồn đối chiếu chính thức, không phải mọi nhận định của HNH đã được khoa học xác nhận.
