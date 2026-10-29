# 13. Backend và các ranh giới nghiệp vụ

Giữ kiến trúc khối ứng dụng mô-đun như kế hoạch cũ. Website công khai, ứng dụng và cổng chuyên gia gọi cùng API gateway/BFF. Lõi phương pháp là package độc lập. PostgreSQL quản lý nghiệp vụ; R2 lưu tệp riêng tư; hàng đợi và transactional outbox xử lý công việc dài. Tiến trình xuất sách chạy trong môi trường hạn chế mạng và hệ thống tệp. [R03, R18, R19]

Các miền nghiệp vụ gồm danh tính, quyền chủ thể, mục đích và sự đồng ý, hồ sơ có phiên bản, kho tri thức, thực thi phương pháp, quan sát, đồng nhịp, nhận định, báo cáo, kế hoạch, thương mại, chuyên gia, học viện và lãnh thổ. Không chia một dịch vụ nhỏ cho mỗi môn. Chỉ tách tiến trình khi tải, quyền hoặc vòng đời vận hành cần khác nhau.

Gateway lấy principal từ phiên xác thực. Dữ liệu user_id do trình duyệt gửi không được tạo quyền. Mỗi analysis run chốt phiên bản hồ sơ, giả thuyết ngày sinh, phương pháp, bảng nguồn, cấu hình, mục đích, phiên bản quyền và ngôn ngữ. Kiểm tra quyền diễn ra khi tạo tác vụ, khi worker nhận việc, trước khi phát hành và khi tải kết quả. Tác vụ đang chờ không được tiếp tục công bố sau khi chủ thể rút quyền.

V3 giữ 83 thao tác API V2, bổ sung 16 thao tác đích, tổng cộng 99. Đây là hợp đồng thiết kế. Demo cục bộ chỉ có ba route nghiệp vụ: health, catalog và run; các tệp giao diện là tài nguyên tĩnh. Không lấy số lượng endpoint trong đặc tả làm số lượng chức năng production đã triển khai.

RLS là lớp phòng vệ bổ sung. Tài khoản ứng dụng không là chủ bảng hoặc có quyền BYPASSRLS. Khóa ngoại cho dữ liệu riêng tư cần gắn tenant và subject để ngăn bản ghi con tham chiếu sang chủ thể khác. Mọi chính sách phải được thử bằng tài khoản thực trong staging, không chỉ đọc SQL hoặc nhìn sơ đồ. [R19, R24]

Đường đọc dữ liệu cần giới hạn theo quyền ngay trong truy vấn. Đường ghi dùng schema đóng, chống mass assignment, kiểm tra phiên bản hồ sơ và nhật ký thay đổi. Những tác vụ sửa quyền, xuất dữ liệu, xóa hoặc cấp entitlement phải có audit event không chứa bí mật truy cập.
