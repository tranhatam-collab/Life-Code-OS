# Backend: điều kiện tích hợp trước khi chạy thật

| Tình huống | Kết quả bắt buộc | Bằng chứng cần thu |
|---|---|---|
| Account A gửi subject B | Từ chối trước truy vấn nội dung | Negative auth test bằng runtime role |
| Cùng idempotency key, payload khác | 409; không ghi thêm run | Transaction receipt |
| Queue giao trùng | Một hiệu ứng xuất bản/quyền sử dụng | Outbox và job receipt |
| Thu hồi quyền khi job đang chờ | Không phát hành; trạng thái blocked/cancelled | Worker test và audit |
| Tên có Y chưa xác nhận | Tổng tên có; các tổng phụ thuộc Y là null | Golden case |
| Cụm 8553 ở strict/diagnostic | Cặp gốc nguyên vẹn, không tự xóa 55 | Golden trace |
| Mục 80 chưa được duyệt | Số dư 0 không tự thành Đại cát | Policy test |
| Hai ngày sinh khác nhau | Hai giả thuyết, không chọn theo lời luận | Bundle fixture |
| Dữ liệu bị xóa rồi restore | Tombstone áp lại trước mở truy cập | Restore drill |
| Partner API gọi ngoài territory | Từ chối theo release/purpose | Tenant and market tests |
| Renderer gặp URL bên ngoài | Không tự tải tài nguyên tùy ý | Sandbox test |
| AI được tài liệu yêu cầu bỏ quyền | Bỏ qua instruction trong dữ liệu | Injection test |

Demo chỉ chứng minh một phần các quy tắc thuần. Các phép thử IdP, PostgreSQL, R2, payment, queue và restore vẫn phải thực hiện trong staging; không được đánh dấu đạt từ văn bản này.
