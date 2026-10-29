# P0: chặn rủi ro trong 48–72 giờ và bảo toàn chứng cứ

Mã tài liệu: **D03** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Incident Commander + Backend + Security. Nguồn đối chiếu: G04, G05, G06, G07, G08, G11, S07, S08. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Thẩm quyền và giới hạn
Đây là runbook đề xuất, không phải lệnh đã thực hiện. Chủ trì P0 phải được chỉ định; duyệt danh sách môi trường và kênh liên lạc. Không thực hiện dò ID người thật, trích hồ sơ production hoặc truy cập dữ liệu bằng token không thuộc mình. Mốc 48–72 giờ là mục tiêu chặn rủi ro, không phải thời gian xây xong toàn bộ hệ danh tính.
## 2. Trình tự
### Trình tự phụ thuộc hiện hành ngày 20/10/2026

Trình tự dưới đây thay thứ tự tuần tự ngầm của backlog 11/10 nhưng không thay quyền thực hiện. P0-01 phải chốt scope, môi trường, người chỉ huy và authority trước. P0-08 xác minh clean clone, remote, branch, full SHA và tính toàn vẹn nguồn ngay sau P0-01. Chỉ sau baseline này, P0-02 mới lập inventory bề mặt/runtime; P0-03 bắt đầu containment server-side. Từ control point đó, P0-04 thu hồi luồng danh tính cũ; P0-05 khóa Engine Lab; P0-06 cách ly output legacy; P0-07 bảo toàn/phân loại dữ liệu có thể chạy theo dependency ghi trong `P0_PACKET/03_PATCH_PLAN.csv`; P0-09 dựng và quét artifact allowlist từ clean baseline. P0-10 là bước cuối, phụ thuộc P0-03/04/05/06/07/09 và vẫn cần approval production gắn exact SHA/artifact/environment/rollback.

Mốc 48–72 giờ chỉ là mục tiêu phản ứng cho **containment subset đã được cấp quyền** khi đã có Incident Commander, clean baseline, quyền provider và đủ người thực hiện. Đây không phải lời hứa hoàn tất cả mười task, phân loại dữ liệu, independent review, deploy provider và rollback evidence trong 72 giờ. Khi chưa có authority/capacity thật, effort vẫn là planning range và có thể phải giữ static maintenance thay vì deploy.

### Các dải giờ phản ứng lịch sử

Các dải giờ sau mô tả nhịp phản ứng mong muốn, không ghi đè dependency hiện hành hoặc tự cấp quyền production.

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


## Bổ sung ngày 20 tháng 10 năm 2026

P0 được tách thành containment code, negative tests, rollout receipt và incident/data review. Auth source đã xác nhận thiếu owner checks tại baseline; chưa có runtime exploit hoặc breach receipt. Xem SECURITY_AND_PRIVACY_ACCEPTANCE.md.
