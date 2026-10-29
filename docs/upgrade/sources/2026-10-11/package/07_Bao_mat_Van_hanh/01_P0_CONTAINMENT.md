# P0: chặn rủi ro trong 48–72 giờ và bảo toàn chứng cứ

Mã tài liệu: **D03** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Incident Commander + Backend + Security. Nguồn đối chiếu: G04, G05, G06, G07, G08, G11, S07, S08. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Thẩm quyền và giới hạn
Đây là runbook đề xuất, không phải lệnh đã thực hiện. Chủ trì P0 phải được chỉ định; duyệt danh sách môi trường và kênh liên lạc. Không thực hiện dò ID người thật, trích hồ sơ production hoặc truy cập dữ liệu bằng token không thuộc mình. Mốc 48–72 giờ là mục tiêu chặn rủi ro, không phải thời gian xây xong toàn bộ hệ danh tính.
## 2. Trình tự
Trong 0–4 giờ: ghi domain, Workers route, Pages preview, bindings, queue, storage và phiên bản deploy có thể truy cập. Bảo toàn bản source và bằng chứng tối thiểu ở kho riêng tư. Không commit PII vào GitHub public.
Trong 4–12 giờ: chặn server-side các route profile/report/session legacy chưa an toàn; khóa mọi đường vòng workers.dev, preview, custom domain và tác vụ nền. Có thể trả trạng thái dịch vụ tạm ngưng với mã lỗi an toàn. `noindex`, CORS và việc ẩn Engine Lab không thay authentication.
Cùng thời gian: dừng cấp session theo client user_id; vô hiệu token legacy; dừng intake ảnh, trẻ em, sức khỏe và thanh toán báo cáo sâu. Hạ nội dung chỉ số và cảnh báo giả về trạng thái nghiên cứu. Không xóa chứng cứ trước khi đánh giá sự cố.
Trong 12–36 giờ: tái hiện bằng hai tài khoản tổng hợp ở staging; viết negative tests; kiểm tra old token, ID chéo, result ID chéo, grant vừa bị thu hồi và job còn trong queue. Bản vá tối thiểu phải giới hạn phạm vi để dễ kiểm tra.
Trong 36–72 giờ: deploy bản đã duyệt, giữ receipt, kiểm tra bên ngoài ở các bề mặt allowlisted. Nếu chưa sửa chắc, duy trì chế độ giới thiệu/bảo trì thay vì mở lại vì áp lực lịch.
## 3. Điều kiện kết thúc
Tất cả route intake nguy hiểm đã bị chặn hoặc sửa có kiểm thử; phiên cũ bị từ chối; không còn đầu ra số phận giả lập trong phạm vi public; source/artifact/runtime được liên kết; dữ liệu legacy có chủ trì xử lý; đã định nghĩa rollback an toàn. Bản rollback không được chứa lại lỗi gốc. Chưa có bản an toàn thì rollback về trang tĩnh không nhập dữ liệu.
## 4. Lưu ý về tài khoản legacy
Tên, ngày sinh hoặc ID cũ không đủ khôi phục quyền sở hữu. Session cấp bởi luồng cũ không tự là bằng chứng quyền hợp pháp. Phân loại hồ sơ chưa rõ quyền; chỉ chuyển khi có quy trình xác minh phù hợp. Không tự gán email mới cho hồ sơ dựa vào việc người dùng biết thông tin phổ biến.
## 5. Biên bản bắt buộc
Mỗi hành động ghi thời điểm UTC, người thao tác, môi trường, request/change ID, tác động, bằng chứng và người duyệt. Nhật ký kỹ thuật chỉ giữ thông tin cần thiết; báo cáo công khai không chứa payload người dùng. Cửa đóng P0 do kỹ thuật, bảo mật và người có thẩm quyền sản phẩm cùng quyết định, không dựa vào một lần `/health` trả 200.
