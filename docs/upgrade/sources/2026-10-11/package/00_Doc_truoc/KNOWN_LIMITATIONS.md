# Những điều đã làm và giới hạn của bộ bàn giao
## Đã làm
Đối chiếu nhánh main và nhánh audit theo SHA; đọc các tài liệu nguồn và một số tuyến mã chính; truy xuất nội dung trang công khai có thể tiếp cận; tham khảo nguồn chính thức về kỹ thuật, AI, dữ liệu và điều kiện quốc tế. Tạo master, 38 chuyên đề, catalog, backlog, hợp đồng API/dữ liệu, mẫu báo cáo, workbook và mã kiểm thử.

## Chưa xác nhận
- Deployed SHA, Worker version, Pages deployment receipt hiện đang phục vụ.
- Hiện trạng phân quyền production sau mọi thay đổi có thể xảy ra ngoài phiên làm việc.
- Worktree local/iCloud và dữ liệu, log, bản sao lưu người dùng thật.
- Luồng đăng nhập với IdP, thanh toán với merchant thực, migration D1→PostgreSQL, RLS E2E, restore và pentest.
- Toàn văn mọi sách và mọi ngôn ngữ trong 20 họ phương pháp; quyền khai thác từng nguồn.
- Ý kiến pháp lý áp dụng hoàn chỉnh tại từng thị trường, quyền thương hiệu, franchise disclosure và giấy phép chuyên môn.
- Hiệu quả tiên đoán hoặc tuyên bố khoa học về số phận; gói này không xác nhận các tuyên bố đó.

## Tính chất mã và schema
OpenAPI là hợp đồng thiết kế, không phải server đã chạy. Các entity tương lai còn cần schema chuyên biệt theo tính năng và migrations được kiểm thử. SQL có RLS bật/force và không có policy cho phép để tránh bị hiểu là có thể dùng ngay; đội backend phải xây policy theo quyền thật và kiểm thử. Hàm authorization tham chiếu nhận dữ liệu đã giả lập; không thay authentication, query scoping hoặc security middleware. Ledger idempotency trong bộ thử là mô hình bộ nhớ, không thay giao dịch/durable ledger production.

## Phạm vi kiểm tra tệp
Đã kiểm tra parse JSON/YAML, JSON Schema với ví dụ, các liên kết nội bộ schema, mã công việc và điều kiện tương ứng, định dạng workbook và test reference. Chưa dùng trình phân tích SQL hoặc máy chủ PostgreSQL. Kiểm tra accessibility DOCX không đồng nghĩa toàn bộ sản phẩm đạt WCAG/PDF-UA.

## Trạng thái phê duyệt
Yêu cầu “xuất bộ kế hoạch” được thực hiện. Nó không phê duyệt giá, nhà cung cấp, thị trường, Q1–Q20 hoặc deploy. Các trạng thái chờ duyệt trong tệp là chủ ý, không phải trường dữ liệu bị quên điền.
