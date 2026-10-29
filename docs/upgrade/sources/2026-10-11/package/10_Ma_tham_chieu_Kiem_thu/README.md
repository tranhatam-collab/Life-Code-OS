# Mã tham chiếu và kiểm thử cục bộ

Chạy: `npm test` trong thư mục này bằng Node 22 trở lên. Không cần cài dependency bên ngoài.

Đây là **reference package**, không phải ứng dụng production. Không có IdP, PostgreSQL, payment provider, migration production hoặc quy trình deploy. `ReceiptLedger` là mô phỏng trong bộ nhớ để minh họa idempotency; production cần transactional ledger/outbox. Hàm `allowed` là policy minh họa, không thay xác thực, RLS hoặc E2E. Method/source rights và Founder approval vẫn chưa được cấp qua các test này.

Bảng 80 mục giữ nhãn do người dùng cung cấp; chủ đề được biên tập, chưa có quyền tuyên bố bảng cổ truyền duy nhất. 0 mặc định unresolved. Số 0/5 trong phân tích cặp vẫn unresolved; không suy bệnh, tài lộc hoặc nội tâm từ số.

Kết quả chạy nằm ở `test-results.tap` và receipt QA. Test exhaustive kiểm tra 10.000 chuỗi, không phải 10.000 cuộc đời.
