# Nhà máy tri thức: từ nhiều ngôn ngữ đến phương pháp có thể chạy

**Life Code OS · Bản nâng cấp bảo toàn V2 · 20/10/2026**  
**Trạng thái:** Đặc tả để triển khai và rà soát; không phải chứng nhận production.

## 1. Hai mươi họ vẫn được giữ, nhưng đơn vị phát hành là phương pháp nhỏ
K01–K20 là registry nghiên cứu, không phải hai mươi phép tính đã hoàn thành. Trong một họ có nhiều bản dịch, trường phái và phiên bản. Một adapter chỉ được phát hành khi khóa được đầu vào, quy tắc, ngoại lệ, tài liệu nguồn, quyền sử dụng và bộ ví dụ. Bản giới thiệu sách hoặc mục lục không thay toàn văn.

## 2. Quy trình tiếp nhận
Nhận diện tác phẩm → lưu metadata và quyền → phân đoạn theo trang/mục → giữ nguyên văn và bản dịch riêng → trích quy tắc → soát ngược với nguồn → tạo golden cases độc lập → lập adapter → kiểm tra độ phù hợp phạm vi → duyệt release. AI có thể hỗ trợ dịch và trích xuất nhưng không tự xác nhận quyền hoặc nguồn chưa đọc.

Mỗi nguồn có trạng thái `DISCOVERED`, `METADATA_READ`, `EXCERPT_READ`, `FULL_TEXT_AVAILABLE`, `RULES_REVIEWED`. Không dùng “đã nghiên cứu đầy đủ” cho tất cả tài liệu chỉ vì chúng nằm trong thư mục. Những văn bản tiếng Hán, Phạn, Pāli, Tamil, Nga, Ả Rập hoặc Hebrew cần người đọc ngôn ngữ phù hợp rà thuật ngữ và quy tắc khi ảnh hưởng phép tính.

## 3. Ngữ pháp HNH tổng hợp
Sáu quan hệ được giữ: nuôi dưỡng, cản trở, bù đắp, xung đột, chuyển tiếp, lựa chọn. Mỗi liên hệ phải nói rõ là biểu tượng từ nguồn hay quan sát từ người dùng. Hai hệ cùng dùng ngày sinh không tạo hai bằng chứng thực nghiệm độc lập. Có thể trình bày đồng thuận và khác biệt về chủ đề, nhưng không tự tăng confidence bằng số lượng bộ môn.

## 4. Dòng phương pháp nâng cao
Bát tự cần timezone, tiết khí, quy tắc ranh ngày và trường phái dụng thần. Tử Vi cần lịch âm, tháng nhuận, quy tắc an sao và tuổi hạn. Chiêm tinh cần ephemeris, hệ nhà và hệ hoàng đạo; giấy phép thư viện phải được kiểm tra. Nadi cần định nghĩa nhánh và nguồn; không tuyên bố đã có mọi lá của mọi người. Kinh Dịch cần cách lấy quẻ, thứ tự hào và văn bản; demo sáu bit không phải engine Lục Hào đầy đủ. Các phương pháp hình thái cần dữ liệu quan sát và phạm vi hợp lệ, không dùng để suy phẩm chất hoặc bệnh.

Những phần này không bị xóa; chúng có backlog riêng và trạng thái `RESEARCH_ONLY` hoặc `SPECIFICATION_PENDING`. Một người dùng chưa đủ dữ liệu nhận lời giải thích phần thiếu, không nhận một kết quả giả theo template.

## 5. Quản trị nguồn và bản quyền
Một bảng có 80 mục vẫn phải biết nguồn từng mục và cách biên tập. Tệp V1 giữ 80 nhãn/chủ đề nhưng thiếu trường nguyên văn; V2 không tự điền từ trí nhớ. Trạng thái source_text_missing chặn chức năng “trích nguyên văn nguồn”, không chặn phép tính số dư. Khi quyền không cho đưa toàn văn vào RAG, chỉ lưu metadata hoặc phần được phép. Tài liệu khách hàng không tự trở thành học liệu hoặc dữ liệu huấn luyện.

## 6. Bằng chứng cần có trước release
Một method receipt cần exact code hash, source version, rule digest, runtime dependency, vector đầu vào/đầu ra, reviewer và phạm vi người dùng. Kết quả tính đúng mới cho phép gọi “calculation verified”. Tính hợp lệ nội dung, tác dụng người dùng và dự báo thực tế là các workstream khác; không dùng một nhãn pass thay tất cả.
