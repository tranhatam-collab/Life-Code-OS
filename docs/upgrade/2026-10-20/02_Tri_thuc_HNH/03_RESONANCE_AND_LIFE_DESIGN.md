# Đồng nhịp sống và thiết kế đời sống: đặc tả dữ liệu và thực hành

Mã tài liệu: **D09** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: HNH Council + Product + Privacy. Nguồn đối chiếu: Yêu cầu của Nhà sáng lập và thiết kế đề xuất trong bộ này. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Không tạo Layer 13
Resonance là quan hệ xuyên 12 lớp, gồm thực phẩm, nước, thời gian, nơi sống, thiên nhiên, giọng nói/âm thanh, con người, công việc, vận động, ngủ/phục hồi, môi trường số và ý nghĩa. Ma trận 144 ô chỉ tổ chức câu hỏi. Không bắt một người điền đủ 144 ô hoặc suy ra giá trị bằng ngày sinh.
## 2. Observation tối thiểu
Ghi subject, field, occurred_at, local timezone nếu có, context, input tự khai, response tự khai, optional measurement, source, data_class, purpose và phiên bản câu hỏi. Mức “thấy nhẹ hơn” là self_report ordinal có nhãn; không gọi là tần số đo bằng hertz. Các đo lường từ thiết bị phải lưu đơn vị, thiết bị và điều kiện, không giả định tương đương với cảm nhận.
## 3. Thử nghiệm nhỏ
Người dùng chọn mục tiêu như giảm gián đoạn lúc viết. Giai đoạn quan sát bảy ngày ghi lịch tự khai. Giai đoạn thử bảy ngày tắt một nhóm thông báo hoặc đổi giờ làm nếu họ chọn. Hệ hiển thị dữ liệu trước–sau và những thay đổi đồng thời. Không kết luận nhân quả từ nhật ký không đối chứng, không nói “cây đã chữa stress” hoặc “SIM tạo tập trung”.
Thay đổi có dấu hiệu gây hại, xung đột trách nhiệm hoặc vấn đề sức khỏe thì dừng và khuyến nghị nguồn hỗ trợ phù hợp; AI không thiết kế nhịn ăn, bỏ thuốc, ngủ ít hoặc trị liệu không chuyên môn.
## 4. Thiết kế đời sống
Life Design nối goal → constraints → options → selected_action → due_date → self_reported_outcome. Mỗi phương án có điều kiện, chi phí thời gian và người chịu ảnh hưởng. Không biến kế hoạch 90 ngày thành 28 nhiệm vụ bắt buộc. Chọn tối đa ba hành động ưu tiên; việc bổ sung mới phải hiển thị phần đánh đổi.
## 5. Bảo mật
Trường “con người” không yêu cầu họ tên đầy đủ của người thứ ba. Dùng bí danh quan hệ; không lập hồ sơ tâm lý bí mật cho họ. Trường thực phẩm/sleep có thể trở thành dữ liệu sức khỏe tùy mục đích và bối cảnh; beta giới hạn nhật ký không lâm sàng và kiểm tra phân loại pháp lý trước mở.
## 6. Nghiệm thu
Tất cả observation sửa được bằng phiên bản, export/xóa được; không có hành vi âm thầm bật tracking. Dashboard tách measurement và tự khai. Khi mẫu ít hoặc dữ liệu ngắt quãng, trả “chưa đủ để nhận xu hướng” cùng số ngày đã ghi, không ép đường trend đẹp.
