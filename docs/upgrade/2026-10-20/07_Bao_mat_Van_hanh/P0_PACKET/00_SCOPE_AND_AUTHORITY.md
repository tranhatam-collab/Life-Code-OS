# P0 — Phạm vi và quyền thực hiện
**Trạng thái: kế hoạch chuẩn bị; chưa có phê duyệt thay đổi production.**

Nguồn chính: G02, G04–G11 trong SOURCE_REGISTRY. Đây là gói thực thi dự kiến, không phải thông báo P0 đã được xử lý.

## Mục tiêu
Chặn đường truy cập/ghi hồ sơ chưa có quyền hợp lệ, ngừng xuất điểm và timeline giả lập như kết quả cá nhân, giữ chứng cứ tối thiểu, biết chính xác bản nào được triển khai và giữ lối liên hệ cho người dùng.

## Phạm vi được đề xuất
Website marketing có nội dung đã rà soát có thể tiếp tục. Profile/session/report legacy chưa bảo đảm quyền phải đóng ở server hoặc lớp truy cập tương ứng. Tạm dừng intake trẻ em, ảnh và dữ liệu sâu. Demo chỉ dùng dữ liệu tổng hợp và được ghi nhãn.

## Thẩm quyền
Founder duyệt phạm vi sản phẩm và người chịu trách nhiệm. Incident Commander điều phối. Backend/Platform thực hiện thay đổi trong phạm vi. QA/Security rà soát độc lập. Privacy/Legal đánh giá nghĩa vụ thông báo và dữ liệu cần bảo toàn. Việc xuất gói tài liệu này không cấp quyền cho bất kỳ agent nào tự deploy, thu hồi session thật, xóa dữ liệu hoặc truy vấn hồ sơ người khác.

## Trước khi thay đổi
Xác định người thực hiện và người duyệt; môi trường; cửa thay đổi; exact SHA; bản rollback an toàn; bề mặt đường đi; cách đo thành công; kênh hỗ trợ. Không reset worktree, chạy cleanup phá dữ liệu hoặc giữ chứng cứ PII trong repository công khai.

## Việc nằm ngoài P0
Không thay framework frontend, không viết lại mọi engine, không mở thanh toán, không ra mắt nhượng quyền và không huấn luyện mô hình từ dữ liệu legacy. P0 phải có phạm vi đủ nhỏ để đánh giá và khôi phục.


## Bổ sung ngày 20 tháng 10 năm 2026

Yêu cầu mới20/10 cho phép nâng cấp, copy và kiểm thử bộ kế hoạch cục bộ. Runbook bên trong gói vẫn không tự cấp authority cho thao tác production.
