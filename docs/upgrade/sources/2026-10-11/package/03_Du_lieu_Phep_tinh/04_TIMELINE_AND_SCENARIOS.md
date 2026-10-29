# Dòng thời gian 0–99: lịch sử, chu kỳ, kế hoạch và kịch bản

Mã tài liệu: **D13** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Data + Method Council. Nguồn đối chiếu: G06, S16. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Bốn đường thời gian
History lưu sự kiện do người dùng cung cấp với độ chính xác ngày/tháng/năm và nguồn. Symbolic cycle lưu kết quả phương pháp có nhãn; không giả làm sự kiện. Plan lưu mục tiêu và lịch hành động tự chọn. Forecast chỉ mở khi có mô hình được phép cho kết quả cụ thể. Giao diện phân biệt bằng chữ, hình thức và chú giải, không chỉ bằng màu.
## 2. Tuổi không phải năm vận hạn
Với ngày sinh B, tuổi a là khoảng từ anniversary(B,a) đến anniversary(B,a+1), nửa mở [start,end). 0–99 gồm 100 khoảng. Ngày 29/02 phải chọn chính sách anniversary không nhuận là 28/02 hoặc 01/03, lưu cấu hình và không âm thầm áp. Bản thử dùng ngày 28/02 nếu đã được product policy chọn, không dùng `add 365 days`.
Chỉ biết năm sinh thì trả khoảng thời gian phù hợp; không tạo sinh nhật 01/01 như dữ kiện. Có nhiều hypothesis tạo nhiều đường tính riêng hoặc band, không hòa thành ngày trung bình. Không mặc định 27, 42, 54 là khủng hoảng; mốc người dùng lập có thể khác.
## 3. Phân tích quá khứ
Không kể một sự kiện chỉ vì một chu kỳ tương ứng. Nếu người dùng chưa kể hôn nhân, nghề hoặc biến cố, report giữ không biết. Nếu nhận sự kiện sau khi đọc báo cáo, đánh dấu observed_after_report để tránh dùng nó làm bằng chứng dự báo trước. Các lịch sử cũ do AI suy diễn không được nhập làm dữ kiện.
## 4. Kịch bản tương lai
Kịch bản ghi assumptions, choices, dependencies, earliest/latest dates và trigger_to_review. Ví dụ chuyển vai trò công việc có ba phương án với thời gian, kỹ năng và nguồn lực; không gán năm thành công chắc chắn. Những mốc xa có độ chi tiết thấp hơn. Kế hoạch 10 năm là hướng và điểm xem lại, không phải lịch biến cố.
## 5. Kiểm thử và UI
Zoom năm/tháng/ngày, chế độ bảng có thể đọc bằng screen reader. Khi nhiều nguồn mâu thuẫn, hiện conflict chip và cho chọn view. Tooltips chứa loại nội dung và provenance. Test đủ tuổi, thứ tự không chồng lấn, năm nhuận, không có ngày sinh, date-only không bị timezone đổi ngày, timezone biên và danh sách rỗng. Mọi timeline sample phải không có hàm sin/seed tạo risk.
