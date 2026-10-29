# Dữ liệu cá nhân: mục đích, lưu giữ, xóa và khôi phục

Mã tài liệu: **D25** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Privacy Lead + Data Lead. Nguồn đối chiếu: S23, S24, S30, S40, S05. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Thiết kế theo mục đích
Mỗi lần intake giải thích dùng để làm gì, bắt buộc hay tùy chọn, ai xem và retention. Căn cứ xử lý được pháp lý xác định theo hoạt động và quốc gia; không gọi mọi xử lý đều là consent. Consent cho dịch vụ không bao gồm training, marketing, nghiên cứu, chia sẻ chuyên gia hay tổ chức. Rút đồng ý ảnh hưởng processing nào phải được giải thích.
Hồ sơ cá nhân không thuộc về employer hoặc regional licensee chỉ vì họ trả tiền. Hệ cấp quyền chia sẻ theo field/section, thời hạn và hành động. Reviewer support không thấy nội dung sức khỏe/tình cảm mặc định. Subject access và account access không đồng nhất.
## 2. Lịch lưu giữ đề xuất để pháp lý duyệt
Các giá trị trong RETENTION_SCHEDULE là thiết kế, chưa phải pháp luật: tệp upload tạm 24 giờ nếu chưa hoàn tất; job payload tối thiểu xóa sau khi giao/đối soát; log bảo mật giữ có thời hạn dựa vào mục đích; bản báo cáo còn hiệu lực theo hợp đồng và yêu cầu người dùng; backup theo chu kỳ được xác định. Hóa đơn, tranh chấp và legal hold có quy tắc riêng. Không ghi “immutable forever” cho dữ liệu nhạy cảm.
## 3. Luồng xóa
Nhận yêu cầu → xác minh quyền → mô tả phạm vi và ngoại lệ hợp pháp → freeze processing liên quan → lập deletion plan → DB → R2 → search/vector index → cache → queue/DLQ → provider theo hợp đồng → receipt. Job đang chạy phải recheck trước publish và bỏ kết quả nếu scope đã bị thu hồi. Hệ phải có tombstone/revocation register đủ để backup restore không phục hồi dữ liệu đã xóa.
Receipt ghi hệ đã xử lý, hệ chờ hết backup retention và ngoại lệ còn giữ. Không tuyên bố xóa tức thời tất cả bản sao khi provider hoặc backup chưa hoàn tất. Hợp đồng provider phải cho phép thực hiện quyền đã hứa với người dùng.
## 4. Trẻ em và hình thái
First beta không thu dữ liệu trẻ, ảnh sinh trắc hoặc dữ liệu bệnh. Những dòng này có legal gate, thiết kế guardian/assent phù hợp tuổi, scope chuyên gia và quy trình thu hồi riêng. Một tuổi ngưỡng toàn cầu không đủ. Country pack kiểm soát tuổi và dịch vụ được cung cấp; không tự suy giới tính từ tên/ảnh.
## 5. Sự cố và hỗ trợ
Phân biệt lỗ hổng source, dấu hiệu khai thác và sự cố đã xác minh. Ghi thời điểm phát hiện, dữ liệu liên quan, phạm vi truy cập, bằng chứng và đánh giá pháp lý. Thời hạn thông báo là nghĩa vụ theo tình huống/quốc gia, không đặt một con số chung. Người dùng có kênh sửa dữ liệu và khiếu nại miễn phí; quyền xuất/xóa dữ liệu không nằm sau paywall.


## Bổ sung ngày 20 tháng 10 năm 2026

Áp dụng activity-level legal matrix và data-system inventory; test deletion gồm jobs đang chạy, DLQ, provider, cache và restore. Mọi retention chưa được ký vẫn là proposal. Xem SECURITY_AND_PRIVACY_ACCEPTANCE.md.
