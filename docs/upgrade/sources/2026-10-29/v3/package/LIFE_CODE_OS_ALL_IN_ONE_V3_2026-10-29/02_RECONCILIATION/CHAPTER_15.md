# 15. Queue, idempotency, cache và tính lại

Cloudflare Queues có cơ chế giao ít nhất một lần. Cùng một thông điệp có thể được xử lý lại; ứng dụng phải quản lý hiệu ứng nghiệp vụ, không hứa hàng đợi chỉ chạy một lần. [R18]

Tạo run, idempotency receipt và outbox event trong cùng giao dịch cơ sở dữ liệu. Khóa idempotency có phạm vi tài khoản, thao tác và mục đích. Cùng khóa, cùng payload trả lại receipt trước; cùng khóa nhưng khác payload trả lỗi xung đột. Worker cần lease, heartbeat, retry có giới hạn, thời gian chờ tăng dần, hàng đợi lỗi và công cụ rà soát lại. Không giữ một HTTP request để dựng 600 trang trong vòng lặp không có giới hạn.

Cache phải gắn tenant, subject, purpose, access revision, input digest, method release, source digest và locale release. Không tạo cache chung theo ngày sinh rồi trả dữ liệu riêng của người khác. Hash phục vụ tái lập không đồng nghĩa ẩn danh; dữ liệu đầu vào dễ đoán vẫn có thể bị đối chiếu. Nhật ký không ghi tên, ngày sinh, prompt riêng hoặc URL tải nếu không thật sự cần.

Hủy tác vụ là trạng thái có lịch sử. Worker kiểm cờ hủy tại các điểm an toàn. Khi có yêu cầu xóa, deletion barrier chặn tác vụ mới và phát hành mới; khôi phục backup phải áp lại các chỉ thị xóa trước khi mở truy cập. Báo cáo đã tải về không thể thu hồi vật lý từ thiết bị người nhận, vì vậy giao diện không được hứa làm được điều đó.

Giới hạn công việc gồm số phương pháp trong một run, kích thước dữ liệu, số dãy so sánh, thời gian chạy, số lần gọi AI, kích thước tệp xuất và số lần thử lại. Các giới hạn phải trả lỗi đọc hiểu được, không chỉ mã lỗi kỹ thuật.

Hiệu năng được đo theo lớp: phép tính ngắn, tổng hợp hồ sơ, xuất tệp, AI và truy xuất. Benchmark máy cục bộ chỉ mô tả môi trường đó; không được chuyển thành SLA công khai hoặc chứng nhận độ chính xác về cuộc đời.
