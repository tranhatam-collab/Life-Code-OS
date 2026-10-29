# Từ điển sử dụng trong bộ nâng cấp

Ngôn ngữ giao diện ưu tiên tiếng Việt. Thuật ngữ kỹ thuật giữ nguyên trong mã và có giải thích tại đây. Đây không phải từ điển toàn bộ các truyền thống HNH.

| Thuật ngữ | Tiếng Việt | Cách dùng |
|---|---|---|
| Account | Tài khoản | Danh tính đăng nhập và quyền dịch vụ; không đồng nhất với người trong hồ sơ. |
| Subject | Chủ thể hồ sơ | Người mà thông tin mô tả; có quyền riêng về dữ liệu. |
| Tenant | Không gian dữ liệu | Ranh giới tổ chức hoặc cá nhân dùng để cách ly dữ liệu. |
| Access grant | Quyền được cấp | Quyền theo chủ thể, loại dữ liệu, thao tác, mục đích và thời hạn. |
| Consent | Sự đồng ý | Một hình thức cho phép xử lý; không đồng nghĩa mọi căn cứ xử lý pháp lý. |
| Processing purpose | Mục đích xử lý | Lý do cụ thể sử dụng dữ liệu; quyền dịch vụ không tự cho phép nghiên cứu hoặc huấn luyện. |
| Entitlement | Quyền sử dụng sản phẩm | Quyền theo gói hoặc giao dịch; không cho phép đọc hồ sơ người khác. |
| Eligibility | Điều kiện thực hiện | Quyền, dữ liệu, phương pháp và thị trường đều thỏa điều kiện. |
| Profile version | Phiên bản hồ sơ | Bản chốt đầu vào có lịch sử; không ghi đè âm thầm. |
| Data hypothesis | Phương án dữ liệu | Một giả thuyết về đầu vào như hai năm sinh; không tự chọn hoặc lấy trung bình. |
| Source of truth | Dữ liệu căn cứ | Nguồn đã được chọn cho phạm vi cụ thể; phải giữ tình trạng xác nhận. |
| Provenance | Nguồn gốc và quá trình tạo | Đường đi từ nguồn/dữ liệu đến phép tính và nhận định. |
| Lineage | Quan hệ phụ thuộc dữ liệu | Biết thay đổi một dữ liệu ảnh hưởng những kết quả nào. |
| Method | Phương pháp | Một hệ quy tắc có nguồn, cấu hình, phiên bản và giới hạn. |
| Method passport | Hộ chiếu phương pháp | Hồ sơ nguồn, quyền sử dụng, đầu vào, quy tắc, kiểm thử và người duyệt. |
| Method release | Bản phát hành phương pháp | Phiên bản bất biến đã được cho phép cho phạm vi cụ thể. |
| Deterministic | Tính xác định | Cùng đầu vào và cấu hình cho cùng kết quả; không có nghĩa tiên đoán đúng con người. |
| Symbolic interpretation | Diễn giải biểu tượng | Ý nghĩa trong quy ước/truyền thống; không tự là dữ kiện. |
| Self-report | Thông tin tự khai | Lời người dùng cung cấp; giữ nguồn và thời điểm. |
| Observation | Quan sát | Ghi nhận có điều kiện và phương tiện; không suy tâm lý từ ngoại hình. |
| Derived metric | Chỉ số tính từ dữ liệu | Đại lượng có công thức, đơn vị, chiều và cửa sổ quan sát. |
| Model probability | Xác suất từ mô hình | Cần sự kiện mục tiêu, mô hình, phạm vi, đánh giá và điều kiện áp dụng. |
| Confidence | Mức chắc chắn theo loại | Phải nêu chắc về phép đọc, dữ liệu hay mô hình; không dùng chung tùy ý. |
| Coverage | Độ bao phủ | Phần dữ liệu/quy tắc đã có trên mẫu số do hệ định nghĩa. |
| Claim | Nhận định | Mệnh đề có nguồn, loại nội dung, quyền và trạng thái rà soát. |
| Layer | Lớp phân tích | Một phạm vi của con người; không phải một nghề hoặc cấp bán hàng. |
| Field | Trường môi trường | Một phần điều kiện sống như thực phẩm, âm thanh hoặc công việc. |
| Level | Cấp sản phẩm | Phạm vi dịch vụ; trả phí nhiều hơn không làm dữ kiện đúng hơn. |
| Resonance | Đồng nhịp sống | Khung quan sát sự phù hợp người–môi trường; không mặc định đại lượng vật lý. |
| Mission | Hướng sứ mệnh được lựa chọn | Giá trị và hướng phụng sự người dùng có thể chọn, thử và thay đổi. |
| Snapshot | Bản chốt | Nội dung có phiên bản tại một thời điểm; quyền truy cập vẫn có thể thu hồi. |
| Report artifact | Tệp báo cáo | PDF/Word/HTML được dựng từ cùng nội dung chuẩn. |
| Idempotency | Chống lặp hiệu ứng | Thực hiện lại cùng yêu cầu hợp lệ không tạo thêm hiệu ứng nghiệp vụ. |
| Outbox | Hộp sự kiện giao dịch | Lưu việc cần gửi cùng transaction của dữ liệu nghiệp vụ. |
| Dead-letter queue | Hàng đợi lỗi | Job vượt số lần thử được cách ly để xử lý có quyền. |
| RLS | Bảo mật theo hàng | Cơ chế cơ sở dữ liệu; không thay toàn bộ phân quyền ứng dụng. |
| BOLA | Lỗi quyền cấp đối tượng | Có ID hoặc đăng nhập chưa đủ quyền truy cập đối tượng. |
| BFF | Backend phục vụ giao diện | Lớp máy chủ xử lý phiên và hợp đồng cho frontend. |
| IdP | Nhà cung cấp danh tính | Dịch vụ xác thực cần được chọn và thẩm định theo phạm vi. |
| CSRF | Giả mạo yêu cầu liên trang | Rủi ro cần kiểm soát khi browser dùng cookie xác thực. |
| CORS | Chính sách chia sẻ nguồn trình duyệt | Không phải authentication và không chặn mọi client ngoài trình duyệt. |
| TOCTOU | Quyền thay đổi giữa kiểm tra và sử dụng | Cần kiểm tra lại khi job bắt đầu, thay đổi và phát hành. |
| SSRF | Giả mạo yêu cầu từ máy chủ | Chặn URL tùy ý trong upload, retrieval và render. |
| SLO | Mục tiêu mức dịch vụ | Mục tiêu đo theo phạm vi và cửa sổ; chưa phải cam kết đã đạt. |
| SLA | Cam kết dịch vụ | Thỏa thuận với khách hàng; chỉ công bố sau khi có nền vận hành. |
| RPO | Mức mất dữ liệu tối đa mục tiêu | Khoảng dữ liệu chấp nhận mất trong sự cố theo thiết kế. |
| RTO | Thời gian khôi phục mục tiêu | Thời gian mục tiêu đưa dịch vụ an toàn hoạt động trở lại. |
| Receipt | Biên nhận bằng chứng | Mã phiên bản, thời gian, môi trường, kết quả và người xác nhận. |
| Gate | Cổng nghiệm thu | Điều kiện phải có bằng chứng trước khi mở phạm vi dịch vụ. |
| Country pack | Bộ điều kiện thị trường | Luật, ngôn ngữ, dữ liệu, giá, support và quyền theo thị trường. |
| License | Cấp phép | Quyền dùng IP/phần mềm theo phạm vi; bản chất hợp đồng có thể vẫn thuộc luật nhượng quyền. |
| Franchise | Nhượng quyền | Mô hình kinh doanh có điều kiện pháp lý từng nước; không chỉ là bản dịch website. |
| FDD | Hồ sơ công bố nhượng quyền | Tài liệu theo yêu cầu pháp lý liên quan; không tự coi mẫu nội bộ là đã đáp ứng. |
| DPA | Thỏa thuận xử lý dữ liệu | Điều khoản vai trò, mục đích, dữ liệu, bảo mật và trách nhiệm các bên. |
| DPIA | Đánh giá tác động bảo vệ dữ liệu | Thực hiện theo điều kiện pháp lý và hoạt động cụ thể; không chỉ điền tên biểu mẫu. |
| PII | Thông tin nhận dạng cá nhân | Không log toàn bộ vào telemetry hoặc kho chứng cứ công khai. |
| Break-glass | Truy cập khẩn cấp có kiểm soát | Phạm vi và thời hạn hẹp; có lý do, phê duyệt và rà soát. |
| Kill switch | Cơ chế dừng khẩn cấp | Dừng từng hoạt động có rủi ro; không làm mất quyền dữ liệu. |
| SKU | Mã sản phẩm thương mại | Đơn vị cung cấp có quyền, quota, chi phí và đầu ra rõ. |
| SME | Chuyên gia lĩnh vực | Người rà soát phạm vi phương pháp; không có quyền truy cập mọi dữ liệu mặc định. |
