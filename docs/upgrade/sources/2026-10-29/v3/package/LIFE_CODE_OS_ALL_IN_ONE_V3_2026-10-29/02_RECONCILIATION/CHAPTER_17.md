# 17. AI đồng hành và mức tự chủ

AI là trợ lý trong một hệ quyền hạn, không đứng trên cổng API. Các vai trò gồm trợ lý nhập dữ liệu, truy xuất nguồn, giải thích công thức, viết nháp, rà nội dung, hỗ trợ mục tiêu và tổng hợp vận hành. Một mô hình không được là người duy nhất vừa tính, vừa xác nhận nguồn và vừa duyệt phát hành.

A0 chỉ đề xuất. A1 thực hiện tác vụ đọc đã được cho phép, như giải thích kết quả đã chốt. A2 thực hiện việc có thể đảo trong hạn mức đã duyệt, như tạo bản nháp hoặc nhắc việc người dùng đăng ký. A3 là tự động hóa vận hành theo playbook có điều kiện, kèm công tắc dừng và người chịu trách nhiệm. Mở quyền dữ liệu, phát hành phương pháp, giao dịch ngoài chính sách, triển khai production hoặc ký nhượng quyền không được tùy ý giao cho A3.

Truy xuất tăng cường — RAG — phải kiểm quyền trước khi lấy nội dung. Tài liệu nguồn và lời người dùng không được xem là lệnh thay quyền. Bộ viết chỉ nhận các claim và trích đoạn được phép. Không đưa toàn bộ hồ sơ khác vào ngữ cảnh để trả lời một câu hỏi. Yêu cầu về một người thứ ba không tạo quyền đọc hồ sơ của người ấy.

Ngân sách AI được giới hạn theo tài khoản và tác vụ: token, chi phí, retry, model dự phòng, thời gian và ngưỡng dừng. Khi nhà cung cấp lỗi, hệ thống có thể trả phần phép tính đã hoàn thành hoặc đưa tác vụ vào hàng chờ xem lại. Không chuyển dữ liệu sang nhà cung cấp khác có chính sách xử lý rộng hơn mà không đánh giá quyền và mục đích.

Giảm thao tác quản trị bằng hàng chờ ngoại lệ và bằng chứng rõ, không bằng việc bỏ trách nhiệm. Người duyệt xem phần thay đổi, nguồn và rủi ro; các phần máy kiểm được có receipt riêng. Người dùng được biết đang tương tác với AI và luôn có đường sửa dữ liệu, báo sai hoặc kết thúc phiên.

Phản hồi “rất đúng với tôi” có thể được lưu như trải nghiệm tự thuật, không tự tăng độ chính xác của phương pháp. Việc học từ dữ liệu người dùng là chương trình nghiên cứu riêng, có mục đích, quyền, phạm vi và cách đánh giá; không diễn ra ngầm trong sản phẩm trả phí.
