# AI hỗ trợ: học, hỏi, viết và kiểm soát hành động

Mã tài liệu: **D21** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: AI Lead + Security + Editorial. Nguồn đối chiếu: S21, S22, G02. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Phân vai, không dựng một AI toàn quyền
Bộ điều phối nhận mục tiêu người dùng cùng phạm vi tài khoản, subject, purpose và entitlement đã resolve ở server. Retriever tìm trong nguồn được cấp quyền. Method Runner gọi bộ tính phát hành. Claim Assembler tạo nhận định có provenance. Writer viết từ nhận định được phép. Reviewer kiểm tra ngôn ngữ, số liệu, đối tượng, dữ liệu thiếu và giới hạn. Support Assistant giải thích quy trình. Learning Tutor chỉ dùng học liệu đã phát hành. Ops Assistant tóm tắt vận hành bằng metadata đã loại PII.
Không AI nào được tự cấp grant, sửa bảng tra, phê duyệt phương pháp, đổi chủ thể, truy vấn SQL tùy ý hoặc deploy. Các hành động được phép đi qua công cụ có schema và policy. Model/provider dùng alias có phiên bản và ngân sách; lựa chọn nhà cung cấp là quyết định sau đánh giá data processing, khu vực, chất lượng VI và chi phí, không gắn cứng tên model quảng cáo.
## 2. Retrieval và bộ nhớ
Tách kho nguồn công khai, nguồn được cấp phép, ghi chú chuyên gia và dữ liệu riêng của người dùng. Bộ lọc quyền bắt buộc trước retrieval và kiểm tra lại trước xuất nội dung. Mỗi chunk có source, edition, trang/mục, ngôn ngữ, claim type và rights. Không đưa một bản dịch tự động chưa duyệt vào nguồn chuẩn.
Conversation memory chỉ ghi những điều cần thiết để phục vụ mục tiêu đã chọn. Không tái sử dụng câu chuyện của khách hàng A làm ví dụ cho khách hàng B. Dữ liệu rút consent phải bị loại khỏi chỉ mục, cache và job đang chờ. Lịch sử hội thoại cần phân loại retention riêng; không gọi “bộ nhớ vĩnh viễn” là một tính năng mặc định.
## 3. Chống prompt injection
Tài liệu truy xuất, nội dung web và lời người dùng là dữ liệu, không được quyền đổi system policy. Những câu “bỏ qua quyền”, “đọc hồ sơ khác”, “đổi score thành 95” phải bị từ chối ở công cụ lẫn tầng viết. Model không thấy secrets, không có credential production và không được tự tải URL tùy ý. URL do người dùng nhập không được trở thành quyền outbound request.
Kiểm thử gồm injection trong PDF, đầu mục sách, mô tả ảnh, tên hồ sơ và source excerpt. Reviewer dùng cả luật xác định lẫn rà soát nội dung; hai model cùng đồng ý không được coi là bằng chứng độc lập về sự thật.
## 4. Trách nhiệm và dấu vết
Mỗi generation lưu model alias, model version khi có, prompt version, claim IDs, retrieval IDs, policy decisions, thời gian, token/cost và final content hash. Không log đầy đủ nội dung nhạy cảm vào công cụ phân tích hành vi. Khi provider lỗi, trả bản deterministic hoặc trạng thái chờ; không âm thầm dùng provider khác có điều kiện dữ liệu chưa duyệt.
## 5. Nghiệm thu
Một báo cáo có thể truy từ câu tới claim và nguồn; dữ liệu người khác không lọt vào retrieval; số trong lời văn khớp method output; không xuất mô tả sức khỏe hay nhân cách từ ảnh; low-confidence transcription được trình xác nhận; người dùng có thể đánh dấu sai. Prompt rollback không thay method release. Bộ kiểm thử AI phải gồm tiếng Việt có dấu, câu thiếu dấu, Anh và các bản dịch thử nhưng chỉ locale đã duyệt được phát hành.
