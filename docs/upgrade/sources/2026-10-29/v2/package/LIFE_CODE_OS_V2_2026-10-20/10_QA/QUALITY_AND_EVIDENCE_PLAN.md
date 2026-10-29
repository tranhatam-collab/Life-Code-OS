# Chất lượng, kiểm thử và cách đọc bằng chứng

**Life Code OS · V2 · 20/10/2026**  
**Trạng thái:** Kiểm thử tham chiếu cục bộ; chưa xác nhận production.

## 1. Năm phạm vi kiểm tra riêng
Kiểm thử phép tính đánh giá công thức. Kiểm thử hợp đồng đánh giá cấu trúc dữ liệu. Kiểm thử chính sách đánh giá trường hợp được phép và bị chặn. Kiểm thử trình duyệt đánh giá tương tác hiển thị. Kiểm thử production đánh giá quyền và hạ tầng thật. Một phạm vi đạt không thay thế tất cả các phạm vi còn lại.

Bằng chứng phải ghi môi trường, phiên bản mã, dữ liệu đầu vào, thời điểm, kết quả và giới hạn. Không dùng số lượng phép thử để quảng bá độ chính xác về số phận con người.

## 2. Bằng chứng cục bộ trong V2
Demo gồm 90 tình huống. Bộ Node có 125 kiểm thử, bao gồm các vòng kiểm tra toàn miền 10.000 đuôi số, 64 cặp và 4.096 phép biến đổi hào. Các vòng kiểm tra toàn miền không được tính thành 14.000 cuộc đời đã xác minh. Bộ kiểm thử gốc có 83 kiểm thử được chạy lại riêng trên bản sao.

HTTP cục bộ được kiểm tra giới hạn đầu vào, nguồn yêu cầu, danh sách tệp được phục vụ và định dạng lỗi. Kiểm thử trình duyệt sử dụng markup cục bộ và cầu nối loopback rõ ràng do điều hướng trực tiếp bị hạn chế trong môi trường chạy. Không thay đổi chính sách trình duyệt và không gọi hệ thống đang hoạt động.

## 3. Bằng chứng chưa có
Chưa thực thi migration PostgreSQL, chính sách RLS bằng tài khoản runtime, callback nhà cung cấp danh tính, triển khai Cloudflare, thanh toán sandbox, R2, hàng đợi cloud, kiểm thử xâm nhập, tải nhiều người dùng, diễn tập khôi phục hoặc phê duyệt pháp lý. Các tài liệu thiết kế không được xem là biên bản hoàn thành những việc này.

## 4. Tính đầy đủ của gói
Verifier xác nhận 149 tệp gốc giữ nguyên hash; các JSON/schema đọc được; ID sản phẩm và công việc gốc được giữ; phụ thuộc có thật; mã demo không trùng; phản hồi phù hợp kết quả kỳ vọng; tham chiếu OpenAPI nội bộ tồn tại. Những kiểm tra thực tế được lưu riêng với các cổng production chưa hoàn tất.

## 5. Tài liệu và giao diện
Word/PDF mới phải được render và kiểm tra hình trang, bảng, khả năng chọn chữ, tiếng Việt và điều hướng. Không chia sẻ tệp phông chữ. Workbook giữ nguyên 11 trang tính gốc về dữ liệu nhập và công thức, bổ sung chín trang tính V2. Việc tính lại có thể đổi giá trị cache trống từ null thành chuỗi rỗng nhưng không thay công thức hoặc đơn giá.

Giao diện demo được xem ở độ rộng 360, 390, 768 và 1440 px. Đây không phải chứng nhận WCAG hoặc kiểm thử ứng dụng native iOS/Android. Các quyền camera, lưu offline, thông báo và danh tính thật vẫn thuộc kế hoạch triển khai riêng.

## 6. Quản lý sai sót
Khi một kết quả kỳ vọng bị sai, phải sửa kèm lý do và phiên bản fixture. Không đổi quy tắc production chỉ để làm test đạt. Lỗi nguồn cần hội đồng phương pháp rà soát; lỗi hiển thị cần bằng chứng giao diện; nhận định vượt dữ liệu cần được rút và kiểm tra những báo cáo phụ thuộc.

Người dùng có quyền không đồng ý với một diễn giải. Đội sản phẩm không được coi mọi phản hồi khác biệt là dấu hiệu “chưa đủ hiểu” để bảo vệ kết quả của hệ thống.
