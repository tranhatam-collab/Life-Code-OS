# Hành trình người dùng, trạng thái trống và tiêu chí giá trị

Mã tài liệu: **D06** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: UX Lead + QA. Nguồn đối chiếu: Yêu cầu của Nhà sáng lập và thiết kế đề xuất trong bộ này. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Người mới miễn phí
Trang đầu đưa ba lối: tìm hiểu phương pháp, thử công cụ không lưu hồ sơ, hoặc xây kế hoạch. Chọn công cụ số thì chỉ hỏi dữ liệu phép tính cần. Kết quả có “cách tính”, “nguồn bảng” và “điều kết quả không nói”. CTA tiếp theo là ghi một câu hỏi hoặc mục tiêu, không phải mua để tránh vận xấu.
## 2. Người tạo hồ sơ cá nhân
Trước nhập, chọn ai là chủ thể và mục đích. Trong beta chỉ cho “chính tôi, từ 18 tuổi”; ủy quyền và trẻ em chưa mở. Bản nháp có thể lưu; ngày sinh cho phép không biết giờ. Người dùng thấy từng dữ kiện gắn tự khai/đã xác nhận/giả thuyết. Trước chạy, màn hình xác nhận phạm vi và những phần không thể thực hiện.
## 3. Người nhận báo cáo
Report bắt đầu bằng mục tiêu, điều đã biết và một hành động. Các claim có thể bung để xem dữ liệu/cách tính. Bên cạnh nhận định có phản hồi “đúng với tình huống”, “không phù hợp”, “cần sửa dữ kiện”; phản hồi không tự huấn luyện engine. Bản report đã phát hành giữ nguyên snapshot, chỉnh sửa tạo phiên bản khác.
## 4. Người làm với chuyên gia
Chọn practitioner theo năng lực, ngôn ngữ và phạm vi; xem lịch, phí và quy tắc. Chia sẻ chỉ những phần cần cho ca. Trước buổi hẹn, chuyên gia chỉ thấy phần đã cấp. Sau buổi, ghi chú phân biệt khách hàng nói và chuyên gia đề xuất. Hết ca hoặc thu hồi grant chặn truy cập mới; file đã tải không thể được hứa thu hồi vật lý.
## 5. Người thuộc tổ chức
SSO có thể cho đăng nhập workspace, không tự cấp quyền vào nhật ký cá nhân. Màn hình luôn chỉ rõ đang ở vùng cá nhân hay công việc. Quản lý nhìn mục tiêu đã chia sẻ và kết quả cộng tác; không thấy thần số, quan hệ riêng hoặc nội dung tự thuật không thuộc công việc. Không có bảng xếp hạng nhân viên theo LCI.
## 6. Trường hợp lỗi và khả năng tiếp cận
Input invalid chỉ lỗi ngay field, không xóa form. Job lâu có progress và lựa chọn xem lại, không spinner vô hạn. Thiếu quyền trả thông báo không lộ sự tồn tại của hồ sơ khác. Thanh toán đang chờ không hiện đã cấp dịch vụ. Báo cáo thiếu dữ liệu phải rõ hơn chứ không trắng hoàn toàn. Mạng gián đoạn giữ draft được phép, có TTL và nút xóa; không cache nội dung riêng trong service worker mặc định.
## 7. Đánh giá giá trị
Pilot theo dõi tỷ lệ hiểu được khác biệt dữ kiện/biểu tượng, số người chọn được hành động, tỷ lệ hoàn thành tự khai và lỗi cần sửa. Không lấy đánh giá “thấy đúng” làm bằng chứng tiên đoán. Chỉ thu analytics dạng sự kiện có whitelist; không gửi trường form, report text, mã số hay câu hỏi riêng vào sự kiện sản phẩm.
