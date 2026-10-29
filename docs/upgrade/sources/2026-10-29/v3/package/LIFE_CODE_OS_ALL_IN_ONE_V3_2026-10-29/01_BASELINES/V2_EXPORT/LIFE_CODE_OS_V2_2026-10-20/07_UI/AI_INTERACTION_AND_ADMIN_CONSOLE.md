# AI tương tác và bảng điều hành giảm thao tác lặp

**Life Code OS · Bản nâng cấp bảo toàn V2 · 20/10/2026**  
**Trạng thái:** Đặc tả để triển khai và rà soát; không phải chứng nhận production.

## 1. AI trợ giúp ngay trong ngữ cảnh
Người dùng có thể hỏi “con số này được tính thế nào?”, “tại sao giờ sinh này có hai phương án?”, “phần nào trong báo cáo là dữ liệu tôi cung cấp?” hoặc “việc nào tôi nên làm trong tuần?”. AI nhận đúng report snapshot và nguồn được phép, không tự mở toàn hồ sơ nếu câu hỏi chỉ cần một phép tính.

## 2. Bốn vai AI
Retriever tìm đoạn nguồn có quyền và phiên bản. Explainer diễn giải calculation trace bằng tiếng Việt. Writer dựng văn bản từ claims đã được phép. Reviewer tìm số liệu sai, câu không có nguồn, nhãn gây sợ, dữ liệu lẫn chủ thể và lặp nội dung. Deterministic checks phải chạy trước và sau AI. Reviewer cùng họ model với writer không được coi là đánh giá độc lập tuyệt đối.

## 3. Mức tự chủ
A0 chỉ soạn nháp. A1 chạy phép tính hoặc truy xuất ít rủi ro trong quyền đã cấp. A2 thực hiện workflow lặp có điều kiện và quyền người dùng đã chấp thuận, ví dụ nhắc kế hoạch. A3 là nhóm tác vụ vận hành được phê duyệt chặt, có hạn mức và cách dừng. Không cấp AI quyền tự deploy, đọc PII toàn bộ, mở health/children, ký franchise hoặc tự thu tiền. Mức tự chủ không tăng chỉ vì có model mới.

## 4. Admin làm theo hàng ngoại lệ
Console có hàng chờ method release, source rights, report review, input conflicts, deletion provider_pending, payment exception, cost limit, incident và partner quality. Sự kiện bình thường được tự ghi receipt; người thật tập trung quyết định có rủi ro. Dashboard hiển thị owner và deadline; không cần nhân sự viết báo cáo tiến độ lặp mỗi giờ khi hệ có thể tổng hợp commit/test/job.

## 5. Bảo mật nội dung
Prompt injection từ sách, tệp hoặc câu hỏi không được ra lệnh bỏ quyền. Tool allowlist theo role/purpose; dữ liệu truy xuất đã ACL-filter trước model. Không chỉ lọc đầu ra rồi cho model đọc dữ liệu không được phép. Không ghi chain-of-thought; lưu prompt template version, claim/source IDs, quyết định policy và kết quả cần kiểm toán.

## 6. Chất lượng hội thoại
AI cần hỏi một câu có ích thay vì dồn 30 câu một lần. Có nút sửa dữ kiện, báo không đúng, xem nguồn và chuyển người phụ trách. Không tạo quan hệ lệ thuộc hoặc nói chỉ mình hiểu người dùng. Với câu hỏi sức khỏe/tài chính/pháp lý vượt phạm vi, chuyển hướng đúng mà vẫn hỗ trợ tổ chức thông tin để làm việc với chuyên gia.

## 7. Chưa có AI provider trong demo
Gói demo dùng nội dung template xác định để kiểm tra trace và hiển thị. Chưa gọi mô hình, chưa đo chi phí token hoặc quality của mô hình. Kế hoạch AI kèm evaluation set, data policy và ngân sách; mọi provider cần review trước khi xử lý dữ liệu thật.
