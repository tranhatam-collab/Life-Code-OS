# P0 — Triển khai và khôi phục có chứng cứ
**Kế hoạch; chưa thực hiện.** Nguồn G09/G10/S13.

## Trước triển khai
Build từ checkout sạch ngoài vùng đồng bộ gây lỗi; ghi SHA đầy đủ, lockfile digest, kiểm thử, migration version, public asset allowlist và người duyệt. Pages và Worker có receipt riêng. Một workflow thành công trong quá khứ không xác nhận deployment hôm nay.

## Bản containment
Ưu tiên khóa route nguy hiểm hoặc sửa nhỏ đúng phạm vi; tránh refactor lớn. Bỏ hardcoded score khỏi UI không đủ nếu endpoint vẫn trả kết quả cũ. Chặn từ server; kiểm tra preview/worker origin và job chờ.

## Sau triển khai
Ghi deployment IDs/versions, thời điểm, cấu hình không có secret và kết quả kiểm tra. Xác nhận token cũ bị từ chối, profile/report không đọc chéo, demo ghi nhãn và intake sâu bị khóa. Lưu hash báo cáo kiểm thử và người xác nhận.

## Rollback
Chỉ quay về artifact an toàn đã biết. Nếu không có bản an toàn, dùng chế độ bảo trì/marketing tĩnh. Không phục hồi bảng session hoặc quyền lỗi từ backup. Mọi thay đổi database phải có kế hoạch tương thích và đối soát; không chạy SQL reference của gói này lên DB sống.

## Biểu mẫu receipt
Dùng schema và example ReleaseReceipt trong thư mục 03_Du_lieu_Phep_tinh. Example là dữ liệu mẫu, không phải receipt của dự án. Chưa có SHA/runtime thực thì để trạng thái BLOCKED_RECEIPT trong evidence, không điền giá trị giả để pass gate.


## Bổ sung ngày 20 tháng 10 năm 2026

Evidence label chuẩn là BLOCKED khi thiếu receipt, kèm reason_code DEPLOYMENT_RECEIPT_MISSING. Không dùng BLOCKED_RECEIPT như claim status. Trình tự drill và SLI nằm trong OPERATIONS_ACCEPTANCE_RUNBOOK.md.
