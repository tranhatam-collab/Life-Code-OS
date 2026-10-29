# Tự động hóa có giới hạn: giảm thao tác, không bỏ trách nhiệm

Mã tài liệu: **D22** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Product Operations + AI Lead. Nguồn đối chiếu: S10, S20, S21. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Bốn mức tự chủ
A0 là đề xuất/soạn nháp, không có tác động bên ngoài. A1 là tính toán hoặc tác vụ đảo ngược, có policy và phạm vi nhỏ. A2 là tác vụ nghiệp vụ đã được người dùng cho phép trước, giới hạn bởi ngân sách, đối tượng, thời hạn và kiểm soát xác định. A3 là thay đổi nhạy cảm phải duyệt: method release, quyền truy cập vượt scope, thông báo sự cố, dữ liệu trẻ em, refund ngoài policy, hợp đồng lãnh thổ, deploy production.
Đây là cơ chế ủy quyền phần mềm, không phải mức thông minh của model. Entitlement có thể tự cấp từ payment event được xác thực bởi server; không phải AI “quyết định khách hàng đã trả tiền”. Quyền xóa dữ liệu có thể tự xử lý theo luồng hợp lệ, nhưng legal hold cần quy trình phê duyệt và giải thích.
## 2. Những việc nên tự động hóa sớm
Kiểm tra đủ trường, tính công thức, báo thiếu dữ liệu, tạo draft, kiểm tra chính tả theo glossary, dựng preview, nhắc hành động đã đăng ký, đối soát job trùng, báo lỗi xuất file, cấp quyền đúng SKU từ webhook hợp lệ và cảnh báo vận hành đã loại thông tin riêng. Các việc này giảm thao tác không cần thiết của Admin mà không tạo lời tiên đoán.
Support bot trả lời từ chính sách đã duyệt, tra trạng thái đơn của đúng tài khoản và mở ticket có mã. Không bịa trạng thái “đã hoàn tiền”; trạng thái phải từ commerce service. Khi cần chuyển người thật, bot gửi tóm tắt vấn đề và dữ liệu tối thiểu, không chia toàn bộ hồ sơ đời sống cho nhân viên hỗ trợ.
## 3. Human review theo rủi ro và độ trưởng thành
Paid beta: mọi báo cáo cá nhân hóa có reviewer trước publish. Sau khi có dữ liệu đánh giá đủ, deterministic result và giáo dục chung có thể auto-publish nếu tất cả kiểm tra máy đạt. Báo cáo sâu, đa chủ thể và dữ liệu nhạy cảm giữ review thích hợp. Tỷ lệ sampling không đặt bằng số tùy ý để gọi là an toàn; cần quyết định release riêng, theo tỷ lệ lỗi và mức tác động đã đo.
Ai duyệt không đồng nghĩa người ấy nhìn được mọi PII. Reviewer chỉ nhận gói dữ liệu tối thiểu. Founder duyệt phương pháp và thương hiệu; không phải nút cổ chai sửa từng dòng của mọi report.
## 4. Automation Center
Mỗi automation card hiển thị: mục đích, trigger, dữ liệu dùng, hành động tối đa, thời hạn ủy quyền, quota, chi phí, lịch sử, nút dừng và người xử lý ngoại lệ. Không gửi nhắc theo “năm xấu”. Quiet hours, timezone, unsubscribe và tránh gửi trùng là điều kiện nghiệm thu.
## 5. Quyền dừng
Kill switch độc lập cho generation, publish, notifications, payments fulfillment, partner exports và từng method release. Dừng generation không làm mất quyền download dữ liệu của người dùng. Dừng intake không xóa báo cáo đã có; việc cần hiệu chỉnh có trạng thái riêng. Mọi nút khẩn cấp phải có diễn tập và người chịu trách nhiệm.

## Bổ sung thực thi 2026-10-20
Eval provider failure, budget exhaustion, revoked grant và prompt injection được yêu cầu trong `07_AI_EVALUATION_AND_DEMO_PLAN_2026-10-20.md`. Mức A0–A3 vẫn là policy proposal; không workflow nào được tự nâng quyền vì xuất hiện trong demo hoặc backlog.
