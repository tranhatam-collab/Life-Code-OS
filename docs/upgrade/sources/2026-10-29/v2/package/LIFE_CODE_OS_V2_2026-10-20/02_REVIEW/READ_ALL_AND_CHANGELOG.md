# Rà soát toàn bộ gói cũ và nguyên tắc không mất nội dung

**Life Code OS · Bản nâng cấp bảo toàn V2 · 20/10/2026**  
**Trạng thái:** Đặc tả để triển khai và rà soát; không phải chứng nhận production.

## 1. Phạm vi đã đọc
Tất cả tệp trong ZIP được kiểm kê, trích xuất hoặc phân tích theo định dạng. Markdown, JSON, YAML, CSV, SQL, JS và Python được đọc bằng công cụ; PDF được trích văn bản; Word được đọc các đoạn và bảng; workbook được đọc cả giá trị và công thức của 11 trang tính bằng artifact_tool. Một số hình trang của bản cũ được xem để hiểu thiết kế; không gọi đó là nghiệm thu trực quan lại toàn bộ 47 trang cũ. Phần mới có quy trình render và kiểm tra riêng.

`FILE_REVIEW_LEDGER.csv` liên kết từng tệp gốc với hash và trạng thái. Toàn bộ tệp gốc còn nguyên trong thư mục baseline; sửa đổi chỉ diễn ra ở các thư mục V2. Các ảnh và hồ sơ cá nhân từ những yêu cầu khác không thuộc bộ đính kèm kế hoạch hiện tại, nên không được tự đưa vào gói hoặc repository.

## 2. Các khoảng trống đã xác định
Bộ cũ có kiến trúc rộng nhưng chỉ một nhóm mã tham chiếu nhỏ. Bảng API có nhiều phản hồi dùng một kiểu Resource tổng quát; thiếu một số hợp đồng thao tác sâu. SQL thiết kế bật RLS nhưng không tự tạo được một hệ phân quyền hoàn chỉnh. Các trường date/time đã nêu ý tưởng, nhưng cần thuật toán DST fold/gap, chính sách ngày nhuận và nhiều giả thuyết chạy được.

Tài liệu bộ số nói cần lưu nguyên văn, trong khi tệp tail80 hiện chứa nhãn và chủ đề biên tập, không có nguyên văn toàn bộ 80 dòng. V2 giữ đúng dữ liệu có sẵn, ghi nguồn nguyên văn chưa nằm trong tệp; không tái tạo âm thầm rồi gọi là nguyên bản. Hai mục 34 và 55 tiếp tục có ghi chú biên tập cần duyệt.

Hàm goalProgress cũ chưa thể hiện đầy đủ cửa sổ ngày đến hạn. Demo V2 tính theo khoảng ngày, loại nhiệm vụ hủy và trả null khi mẫu số bằng không. Ledger xử lý trùng cũ là ví dụ đơn giản; V2 có mô phỏng đồng thời trong một tiến trình, đồng thời bổ sung đặc tả transaction/outbox thật. Không coi Map bộ nhớ là kho idempotency production.

## 3. Những quyết định không được lùi lại
Không quay về chấm LCI tùy ý. Không dùng Math.sin/seed để tạo năm rủi ro. Không suy năng lực, bệnh hay đạo đức từ ngoại hình. Không thu dữ liệu nhạy cảm để làm biểu đồ trông đầy. Không thay một input thiếu bằng giá trị mặc định mà không ghi trạng thái.

## 4. Giữ lịch sử nhưng không giữ hiệu lực sai
“Không loại bỏ kế hoạch cũ” được thực hiện bằng bảo toàn nguyên bản và liên kết thay thế. Một công thức legacy được lưu cho audit nhưng không được tiếp tục chạy trong sản phẩm. Tệp cũ vẫn đọc được; V2 có bảng đối chiếu và quyết định ưu tiên khi hai phiên bản khác nhau. Đây là quản lý thay đổi, không phải xóa lịch sử.

## 5. Trạng thái nghiệm thu
Các kiểm thử của gói tham chiếu chỉ chứng minh hành vi cụ thể trong môi trường local. Chưa có auth thật, PostgreSQL thật, payment gateway, R2 private, queue cloud, penetration test hoặc production E2E trong demo. Thông tin này phải xuất hiện ở README, receipt và phần giao việc, không chỉ ở disclaimer cuối sách.
