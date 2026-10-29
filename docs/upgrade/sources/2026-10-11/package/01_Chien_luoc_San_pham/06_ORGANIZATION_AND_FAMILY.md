# Tổ chức, gia đình và quyền cá nhân không thể bị hòa tan

Mã tài liệu: **D31** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Product + Privacy + Enterprise Lead. Nguồn đối chiếu: S07, S09, S23, S30. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Không gian tổ chức
Workspace quản lý dự án, vai trò, mục tiêu, học tập và năng lực có minh chứng. Thành viên có hồ sơ công việc khác hồ sơ cá nhân; employer không tự đọc journal, tình cảm, sức khỏe hoặc nội dung HNH riêng. Người trả phí có quyền quản lý seat và invoice, không mua quyền đọc tâm trí người khác.
Không sử dụng biểu tượng, ảnh, niềm tin, ngày sinh để xếp hạng tuyển dụng, sa thải, tín dụng hay mức lương. Assessment nghề nghiệp có mục đích, instrument và consent phù hợp; không đổi thành workplace scoring vì khách hàng yêu cầu. Mọi chức năng có tác động lớn cần thẩm định pháp lý riêng.
## 2. Dashboard đội nhóm
Chỉ tổng hợp dữ liệu được phép và có ngưỡng chống nhận dạng lại. Team nhỏ không xuất biểu đồ có thể suy ra từng thành viên; các bộ lọc liên tiếp phải chống differencing. Chưa có ngưỡng đã đánh giá thì trả insufficient_cohort thay vì hiện trung bình. Metrics vận hành dự án không trộn với “năng lượng nhân viên”.
## 3. Family mode
Người trưởng thành tự quản quyền riêng; gia đình không có admin toàn quyền mặc định. Mục tiêu chung và lịch dùng shared objects với quyền riêng. Relationship report hai người chỉ nhận phần mỗi bên đồng ý; một bên rút quyền thì các kết quả kết hợp bị xem lại. Không gửi nhận định về người vắng mặt chỉ từ lời kể một phía như fact.
## 4. Hồ sơ trẻ và người cần đại diện
Family foundation có thể triển khai người trưởng thành trước. Guardian/minor flow mở sau khi country pack, age policy, phạm vi dịch vụ và safeguard được duyệt. Quyền đại diện có evidence, thời hạn, review và quy trình tranh chấp. Trẻ đến tuổi có quyền tự quản cần transition, không tiếp tục để phụ huynh xem dữ liệu vô thời hạn. Dữ liệu phát triển không được dùng để gán nghề hoặc năng lực cố định.
## 5. Tích hợp doanh nghiệp
SSO và SCIM là khả năng về sau tùy khách hàng, không bảo đảm đã có trong beta. Provision seat không đồng nghĩa grant hồ sơ cá nhân. Tenant export có scope; termination bảo toàn quyền riêng và lối ra của thành viên. API key được giới hạn capability/tenant/purpose, rotation và revocation; không dùng một master token xuyên quốc gia.
## 6. Acceptance
Test account đổi tenant, offboard chuyên gia, withdraw share, export tổ chức, audit access và aggregate nhỏ. Một user thuộc hai tổ chức không làm dữ liệu tổ chức A xuất hiện khi dùng context B. Template country partner không được ghi đè các nguyên tắc này.
