# Mô hình miền: tài khoản, chủ thể, quyền và dữ liệu nhiều giả thuyết

Mã tài liệu: **D10** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Data Architect + Privacy. Nguồn đối chiếu: S09, S15, S16. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Tách tài khoản khỏi con người
Account xác định người đăng nhập; Subject là người được phân tích; Organization là đơn vị hợp tác; Membership chỉ cho quyền công việc trong organization. Không suy từ membership rằng được đọc hồ sơ riêng. Account có thể là chủ thể, người được ủy quyền hoặc người thực hành; mỗi vai cần grant có resource, action, purpose, expiry và trạng thái.
Chủ thể không nhất thiết có account ngay, nhưng việc tạo hồ sơ người thứ ba cần luồng ủy quyền được phát hành. Beta adult-self không mở thao tác ấy. Quan hệ người giám hộ, nhiều bên và quan hệ doanh nghiệp chỉ mở sau review riêng. Founder không có quyền thường trực đọc tất cả dữ liệu; break-glass có lý do, thời hạn và phê duyệt.
## 2. Dữ liệu gốc và dữ liệu dẫn xuất
Profile version là snapshot không sửa âm thầm. Dữ liệu tự khai được lưu với nguồn khai, thời điểm, mức chính xác và ngôn ngữ. Ngày sinh giấy tờ, ngày được gia đình nhớ lại và giờ ước tính là data hypotheses; không ghi đè lẫn nhau và không tự lấp tháng/ngày. Hypothesis có field_path, candidate_value, provenance và trạng thái selected/alternative/unresolved.
Chuỗi tên nguyên bản giữ Unicode NFC; chuỗi bỏ dấu là derivative kèm normalization_version. Không tự chọn ý nghĩa Hán Việt hoặc giới tính từ tên. Thời gian có date_precision, time_precision, time_range, place_text, tọa độ đã xác nhận hay chưa và tzdb_version. Không lấy timezone hiện tại thay timezone lịch sử.
## 3. Quan hệ dữ liệu
Analysis run tham chiếu một profile version, selected hypotheses, product release, purpose và bộ method release. Mỗi method result chỉ về run. Claim chỉ về result hoặc observation liên quan; dependencies tạo đồ thị không chu trình. Report snapshot gom claim đã được phép, không trỏ tùy ý sang dữ liệu live. Export artifact có hash, format, storage key, retention và trạng thái revoked/deleted.
Action plan là dữ liệu sống tách report: người dùng sửa kế hoạch tạo history, không sửa PDF đã xuất. Outcome tự khai vẫn mang self_report. Một nhận định cũ do AI viết không được nhập ngược thành “sự kiện đời thật”.
## 4. Toàn vẹn và phạm vi tenant
Mỗi đối tượng nghiệp vụ có subject_id hoặc owner_account_id phù hợp và tenant_id nếu là dữ liệu tổ chức. Composite foreign keys bảo đảm child không chỉ tới parent ở tenant/subject khác. Tất cả bảng private deny-by-default; API dùng session-derived identity. Idempotency key có namespace account + operation; không dùng khóa global chỉ theo chuỗi client gửi.
## 5. Dữ liệu dẫn xuất và quyền thu hồi
Lineage phải chỉ được report nào dùng observation nào để xóa/sửa chính xác. Khi dữ liệu bị thu hồi, chặn job mới, hủy job chưa phát hành và cập nhật trạng thái artifact. Đã tải về thiết bị ngoài hệ không thể được hứa thu hồi vật lý. Sau khôi phục backup phải áp lại deletion ledger trước phục vụ lưu lượng.
## 6. Nghiệm thu
Schema phải chặn liên kết chéo chủ thể, mục đích không hỗ trợ và version không tồn tại. E2E phải kiểm thử concurrent update với If-Match, profile version đã xóa, grant hết hạn và report đang render. DDL trong bộ này là tham chiếu thiết kế; chỉ được gọi migration sản xuất sau khi chạy PostgreSQL isolated và diễn tập dữ liệu tổng hợp.
