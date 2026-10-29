# Lộ trình, phân công và quản trị phụ thuộc

Mã tài liệu: **D33** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Program Lead + Tech Lead. Nguồn đối chiếu: G02. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Thời gian có điều kiện
T0 là ngày đủ người chủ trì, quyền môi trường và scope được duyệt. P0 ngày 0–3; governance tuần 1–3; Trust Core tuần 2–7; first product tuần 5–14; private paid beta tuần 13–24; Level 2–5/Resonance/Practice tháng 6–10; hợp nhất/mobile/Academy/API tháng 9–18+. Đây là estimate với đội lõi6–8 người và chuyên gia hỗ trợ, không hứa mọi module sức khỏe hoặc trẻ em sẽ mở theo lịch.
Giai đoạn có thể chồng về thiết kế, không mở intake thật trước gates. Research K01–K20 tiếp tục song song nhưng method release không tự theo ngày. Quốc tế/franchise chỉ qua country/legal/brand gate và năng lực vận hành thực.
## 2. Vai trò chịu trách nhiệm
Founder quyết triết lý, phạm vi và Q decisions. Program Lead quản backlog, phụ thuộc và đổi scope. Tech Lead chịu architecture và integration. Backend/Data giữ dữ liệu, quyền, migrations. Frontend giữ UX/a11y/i18n. AI/Knowledge giữ retrieval/policy. Editorial giữ nội dung. QA/Security xác nhận độc lập. SRE giữ release/restore. Legal/Privacy giữ áp dụng luật và quyền. Partnerships/Academic giữ license, đào tạo và chất lượng đại diện thương hiệu.
Một người có thể kiêm nhiệm nhưng người viết không là người duy nhất phê duyệt mọi phần. Mỗi task có accountable owner, reviewer, đầu ra và evidence path. Không dùng “AI team sẽ tự làm tất cả” làm người chịu trách nhiệm.
## 3. Chu kỳ điều hành đề xuất
Stand-up ngắn theo workstream; daily report là snapshot: việc đã hoàn thành có evidence, đang làm, blocked, tác động scope và quyết định cần chốt. Báo cáo hàng giờ cho lane đang dev chỉ nên phản ánh CI/job/commit và blocker, không yêu cầu con người viết lại báo cáo mỗi giờ. Automation có thể chuẩn bị báo cáo, chưa được tạo hoặc lên lịch trong gói bàn giao này.
## 4. Definition of done
Một task code xong phải có contract phù hợp, test, quyền dữ liệu, log đúng, tài liệu dùng và rollback khi liên quan. Task tài liệu phải có nguồn, owner, phiên bản và review; không đánh dấu completed chỉ vì tạo file. Backlog đi kèm mặc định NOT_STARTED cho triển khai production; kiểm thử reference package nằm ở receipt riêng.
## 5. Thay đổi phạm vi
Request mới được phân loại P0 khẩn cấp, sửa hiểu sai, extension phase hoặc backlog. Không âm thầm thêm chức năng vào sprint hiện tại rồi giữ deadline cũ. Khi đổi method contract, chạy impact analysis cho templates, API, translations và báo cáo cũ. Khi đổi luật, country pack phải quyết pending/restrict/release; không sửa trang disclaimer rồi bỏ qua xử lý dữ liệu.

## Bổ sung thực thi 2026-10-20
Phase canonical là P0/A/B/C/D/E/F; `F_REVIEW`, `E_F_REVIEW`, `F_LEGAL` là suffix điều kiện. Critical path, lane song song, capacity, RACI, stop rule và cost formula nằm tại `06_PROGRAM_EXECUTION_PLAN_2026-10-20.md`. 140 task gốc được giữ và chỉ nối thêm task có prefix `UPG-*`.
