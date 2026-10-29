# 23. Cổng phát hành, bằng chứng và 280 công việc

Backlog giữ 140 công việc V1 và 68 phần làm rõ V2, bổ sung 72 công việc V3, tổng 280 bản ghi. Đây là danh mục kiểm soát phạm vi, không phải 280 việc đã hoàn thành. Những phần đã có mã tham chiếu vẫn giữ trạng thái production chưa bắt đầu cho tới khi có tích hợp và receipt riêng.

Mười hai cổng gồm nguồn và phát hành; xác thực; phân quyền; pháp lý và mục đích; lưu giữ và xóa; phương pháp và nhận định; legacy và migration; báo cáo và AI; thương mại; độ tin cậy; rà soát bảo mật độc lập; vận hành. Không lấy trung bình để bù lỗi phân quyền bằng chất lượng giao diện. Người sửa không là người duy nhất xác nhận phần sửa đã an toàn.

Thứ tự triển khai theo bằng chứng: containment, governance, Trust Core, sản phẩm đầu tiên, paid private beta, mở rộng dữ liệu đời sống và hệ hợp nhất. Chín cấp không cần mở cùng lúc. Ước lượng cũ 4–6 tháng cho paid beta và 12–18+ tháng cho tầm nhìn rộng chỉ có ý nghĩa với nguồn lực tương ứng; V3 không đổi nó thành cam kết giao hàng.

Kiểm thử gồm unit, property, hợp đồng API, quyền âm tính, migration, báo cáo, khả năng truy cập, staging E2E, khôi phục và review. Tính đúng Mã đuôi 80 với 10.000 đầu vào không chứng minh 10.000 cuộc đời. Đếm đúng 17 vị trí Psychomatrix không xác nhận các nhãn truyền thống về trí nhớ hoặc sức khỏe.

Mỗi yêu cầu nối tới tài liệu, công việc, code/config, kiểm thử và bằng chứng. VERIFY_PACKAGE.py kiểm hash và cấu trúc tệp trong gói; không thay đánh giá bảo mật production. Cổng chỉ đạt khi receipt được tạo trong đúng môi trường, ghi rõ SHA, artifact digest, thời điểm và người chịu trách nhiệm.

Khi một cổng chưa đạt, báo cáo nêu thiếu bằng chứng nào và ai xử lý. Không đổi nhãn thành “đạt một phần” rồi cộng vào tỷ lệ sẵn sàng chung. Có thể mở một phạm vi nhỏ khi tất cả cổng áp dụng cho phạm vi ấy đạt; không mở một mô-đun nhạy cảm chỉ vì mô-đun tính số đã chạy đúng.
