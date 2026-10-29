# Lịch sử thay đổi và bảo toàn kế hoạch

## Bản hợp nhất ngày 20 tháng 10 năm 2026

Phạm vi là bộ chuẩn bị phát triển, không phải thay đổi production. Bản này supersede hướng dẫn nhận việc, master và receipt xuất bản ngày 11/10 trong working package; không xóa hoặc sửa nguồn lịch sử.

- Bảo toàn toàn bộ 149 tệp, ZIP, handoff message và checksum nguồn trong `sources/2026-10-11`; snapshot handover phase-1.5 riêng. Giữ mọi ID cũ và 38 chuyên đề.
- Bổ sung 16 task, nâng backlog từ 140 lên 156; tạo hợp đồng thực thi từng task, 87 dòng trace và 20 decision packet có phương án, đánh đổi, điều kiện, receipt. Sửa DAG P0 để khóa nguồn trước sửa code; giữ `original_dependencies`.
- Làm rõ 23 product contracts, 45 screen contracts, 9 level/report contracts, PWA/responsive, offline/privacy/failure states và acceptance đa thiết bị.
- Bổ sung method execution/result contract, source-rights-research matrix 20 họ, decimal/date/normalization, auth negative matrix, migration/reconciliation runbook, schema delta và API overlay/hợp nhất.
- Thêm 64 ca demo tổng hợp, Demo Lab không gửi dữ liệu, và test contract/negative. Số kiểm thử hiện tại xem TAP và QA receipt, không dùng số 83 của source cũ.
- Ánh xạ đủ FPOS RG0–RG13, dịch vụ/operations, RPO/RTO/SLO đề xuất, legal activity gates và nghiên cứu nguồn chính thức cập nhật có giới hạn.
- Hợp nhất lại master Markdown/Word/PDF và workbook 14 tab; sửa blank/zero budget guards, thêm decision options, task negative/rollback và trace. Thêm portal tìm kiếm tài liệu ngoại tuyến, catalog và integrity verifier.
- Chỉ bổ sung dated entry point vào README, PROJECT_STATUS_MASTER và PRE_CODE_LOCK_CHECKLIST hiện có. Không tự commit, push, deploy, sửa dữ liệu hay nâng maturity.

## Nội dung changelog ngày 11 tháng 10 được giữ nguyên bên dưới

Các số 140 công việc và 83 kiểm thử dưới đây thuộc bản lịch sử, không phải receipt của lần nâng cấp 20/10. Câu “không sửa repository, branch” mô tả phiên cũ; bản 20/10 có thay đổi local worktree được Founder yêu cầu.

### Thay đổi so với kế hoạch audit 336ef35a…
## Phần giữ
9 cấp; 12 lớp; 4 phần báo cáo; HNH; 12 trường Đồng nhịp sống; 20 họ nghiên cứu; modular monolith; trust core; cách ly legacy; bằng chứng nguồn và cổng phát hành.

## Phần nâng cấp trong bộ này
1. 23 sản phẩm/gói: thêm Free Guest, Free Essentials, hạn mức và đường tiếp tục hữu ích khi hết AI.
2. 45 màn hình mục tiêu có trạng thái, quyền, khả năng tiếp cận và liên kết việc triển khai.
3. 64 thao tác OpenAPI v2, 9 schema và ví dụ, 41 entity SQL tham chiếu với composite subject/tenant boundaries.
4. 140 công việc có người chủ trì, phụ thuộc, ước lượng ngày công, đầu ra, tiêu chí nghiệm thu và cổng liên quan.
5. P0 packet riêng, ma trận nguồn→đích, nguyên tắc không tin client user_id, quyền kiểm tra lại khi job chạy/publish.
6. Bốn mức tự động hóa A0–A3, 10 luồng tự động hóa và quyền dừng; không trao một AI toàn quyền.
7. Bộ chương trình nghiên cứu K01–K20, glossary Việt–Anh, 15 passport và 120 trường tùy chọn; không ép intake.
8. 9 mẫu báo cáo khác nhau, nội dung có lineage, không bắt đủ trang khi thiếu dữ kiện.
9. Bốn loại đối tác; 5 bộ điều kiện thị trường Việt Nam, EU/EEA, Hoa Kỳ, Australia và Singapore đều chưa được phê duyệt mở bán.
10. Cập nhật danh mục pháp lý Việt Nam năm 2026 và điều kiện rà soát quốc tế; không dùng pháp luật cũ làm kết luận tuân thủ.
11. 83 kiểm thử mã tham chiếu; bao gồm toàn miền Mã đuôi 80, kiểu nhận định, quyền và xử lý thiếu dữ liệu.
12. Workbook có công thức quản lý tiến độ/ngân sách; không ngụy tạo trạng thái DONE hoặc đơn giá thị trường.

## Không thay đổi
Không sửa live, repository, branch, session, dữ liệu, payment hoặc deployment. Trạng thái P0 chưa được đóng bởi bộ bàn giao.
