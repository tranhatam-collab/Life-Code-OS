# Nâng cấp nội dung live và SEO không phá đường dẫn

Mã tài liệu: **D20** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Editorial + Frontend. Nguồn đối chiếu: S01, S03, S04, S05, S06, G09. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Copy cần thay cùng chức năng
Home đang dùng thông điệp đọc tới 99 tuổi, luôn có xác suất và các cửa thời gian. Chuyển sang định nghĩa phạm vi, dữ liệu, phương pháp và hành động. LCI không còn nói đã khóa chuẩn nếu điểm người dùng còn tự gán. Bắt đầu không hứa điểm mạnh bẩm sinh đã biết. Timeline không quảng bá năm rủi ro khi engine legacy đã bị tắt. Privacy không hẹn xóa dữ liệu “làm sau” trong một sản phẩm đang thu dữ liệu sâu.
## 2. Ma trận đối chiếu
`SOURCE_TO_TARGET_MATRIX.csv` gắn mỗi trang/route/file hiện có với observed_state, keep/change/quarantine, target module, evidence, owner, task IDs và acceptance. Phần bản quyền giữ quyền sáng tạo được xác lập nhưng không nhận quyền trên standards, bảng có nguồn khác hoặc dữ liệu người dùng. FAQ giải thích rõ full book là phạm vi được bàn giao, không toàn tri.
## 3. SEO thực tế
Mỗi public page có title, description, một H1, cấu trúc heading, canonical và social preview mô tả đúng dịch vụ. Không hứa rich result hoặc thứ hạng. Chỉ dùng structured data phản ánh nội dung đang công bố: Organization, WebSite, Course nếu thực sự có khóa; không tạo rating, giá hoặc review giả. Trang app/private đặt noindex và auth; noindex không thay bảo mật.
## 4. Redirect và sitemap
Đối chiếu toàn bộ href trong source và bản live có thể đọc; clean URL là canonical. Redirect file .html tới clean path một bước; ngôn ngữ có route riêng khi đã có bản dịch đầy đủ. Không redirect mọi 404 về home. Sitemap không chứa preview/staging/account/private reports. Kiểm tra URL cũ với 301/200/404 expectations, không chỉ bấm vài link thủ công.
## 5. Bundle hygiene
Phải tạo manifest public assets từ allowlist: trang, CSS, JS đã build, static images được phép, robots/sitemap. Không copy mọi file trong repo rồi loại trừ vài thư mục. Kiểm thử artifact không có .env, SQL, private fixture, source snapshots hoặc security evidence. Source của dự án có thể public nhưng không đồng nghĩa mọi file thuộc public website.
## 6. Nghiệm thu
Đọc lại toàn bộ bản VI và EN có thay đổi; kiểm tra consistency tên level/layer/field; link checker trên bundle; sample accessibility; diff copy cũ/mới và legal review. Không công bố tính năng là hoạt động trước receipt E2E. Mỗi release có content digest và approval, không để AI tự sửa trang chính sách.

## Bổ sung thực thi 2026-10-20
Public routes UI-01–UI-06 có state, phone/desktop, offline/cache và no-private-payload test IDs trong `SCREEN_EXECUTION_EXTENSION.*`; DEMO-01 và DEMO-12 giữ install/PWA là progressive enhancement. Content digest và approval vẫn là evidence riêng, không được suy từ registry.
