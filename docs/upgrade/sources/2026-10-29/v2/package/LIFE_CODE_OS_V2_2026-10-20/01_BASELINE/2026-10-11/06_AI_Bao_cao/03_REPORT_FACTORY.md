# Nhà máy báo cáo: một nội dung chuẩn cho Web, PDF và Word

Mã tài liệu: **D23** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Report Lead + Editorial + QA. Nguồn đối chiếu: G02, G03. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Snapshot và content model
Một report snapshot chốt profile version, method releases, claims, purpose, grants tại thời điểm chạy và content revision. Quyền được kiểm tra lại lúc publish/download; snapshot quyền cũ không duy trì quyền đã thu hồi. Snapshot bất biến về nội dung không có nghĩa PII phải giữ vĩnh viễn: deletion policy được ưu tiên, dùng tombstone không chứa nội dung riêng khi cần audit.
Section có stable ID, layer, purpose, supported claim IDs, narrative blocks, tables, limitations, questions và actions. Các renderer dùng chung content tree. Không tính lại ngày sinh hoặc score trong HTML/Word. Nội dung cá nhân hóa, giáo dục chung, bảng tra và worksheet có nhãn khác nhau.
## 2. Cấu trúc chín template
Mỗi level có mở đầu/phạm vi/source of truth; Identity; Analysis; Timeline nếu có; Action; phụ lục và quyền dữ liệu. Level 1 giải thích phép tính và một thử nghiệm ngắn. Level 2 thêm mâu thuẫn giá trị được người dùng xác nhận. Level 3 sử dụng nhật ký. Level 4 dùng work/resources. Level 5 dùng grant từng bên. Level 6 giữ bốn dòng thời gian riêng. Level 7 chỉ quan sát phù hợp. Level 8 kết tinh lựa chọn sứ mệnh, không phán linh hồn. Level 9 loại lặp và giữ lineage từ mọi phần.
Ngân sách trang là giới hạn biên tập, không là KPI bắt buộc. Dữ liệu ít không được làm thành một “tiểu sử 600 trang”. Có thể xuất sách ngắn hơn với phần thiếu được nói rõ hoặc báo cáo có phụ lục hướng dẫn nhưng phân biệt nội dung chung.
## 3. Quy trình xuất
Validate claims → build tree → editorial rules → preview → review → publish snapshot → queue export → sandboxed renderer → kiểm tra file → private storage → entitlement/grant download. Renderer không tải URL bất kỳ, không đọc local file ngoài thư mục cho phép, không có internet/secret nếu không cần. HTML/Markdown được sanitize. Không nhúng script người dùng vào report.
PDF phải selectable text, font tiếng Việt, bookmark, TOC, số trang, bảng không tràn và link nguồn. DOCX dùng heading/table thật và alt text khi có hình. Web Book lazy-load nội dung nhưng có bản in rõ. EPUB mở sau khi kiểm tra accessibility và font licensing.
## 4. Hiệu chỉnh và thu hồi
Báo cáo sai tạo revision mới; ghi phần thay đổi và lý do. Trạng thái withdrawn chặn phát hành tiếp và cho người dùng biết phần không còn đáng dựa vào. File đã tải không thể thu hồi vật lý khỏi máy người dùng. Không hứa ngược lại. Nếu lỗi hệ thống ảnh hưởng nhiều người, dùng impact query trên method version/claim lineage để tìm report liên quan.
## 5. Nghiệm thu và ngân sách
Máy kiểm tra số liệu, tên subject, thiếu citation, chữ rác và trang trắng; người biên tập kiểm tra tiếng Việt và cách hiểu. Thời gian sinh Level 1 mục tiêu dưới 5 phút chỉ là giả định benchmark; 600 trang chưa cam kết. Retry phải tái dùng snapshot, không phát sinh một bản luận khác mà không có revision ID.
