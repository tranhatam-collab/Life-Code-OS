# Backend: modular monolith, ranh giới tin cậy và lựa chọn công nghệ

Mã tài liệu: **D14** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Tech Lead + Platform. Nguồn đối chiếu: G09, G10, S09, S10, S12, S13. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Lựa chọn đích đề xuất
P0 giữ trang tĩnh hiện có để giảm thay đổi. Sau đó dùng Astro static cho marketing, React/Vite cho app cần tương tác; cùng artifact public qua Pages, API qua Worker/BFF cùng origin. Node/TypeScript là lõi nghiệp vụ và method core để phù hợp source hiện tại. Python chỉ dành tác vụ thư viện đặc thù hoặc worker render; không viết hai implementation công thức.
PostgreSQL là hệ nghiệp vụ đích; D1 được giữ trong vùng legacy chỉ đọc trong migration. R2 chứa tài nguyên riêng tư; Queues điều phối job; outbox trong PostgreSQL là nguồn công việc phải gửi. Không chọn một nhà cung cấp PostgreSQL/IdP/thanh toán trước khi có vùng dữ liệu, pháp nhân, DPA và dự toán. Đây là bốn decision blockers, không phải placeholder triển khai.
## 2. Ranh giới mô-đun
Identity, Access, Profile, Knowledge, Methods, Observations, Analysis, Reports, Plans, Commerce, Practice, Academy, Organizations, Partners và Ops dùng package/service boundary. Mọi gọi nội bộ mang principal và purpose đã được server xác nhận. Một mô-đun không đọc trực tiếp bảng private của mô-đun khác nếu bỏ được policy boundary.
## 3. API gateway
Gateway xử lý request ID, limit kích thước, validation, session, CSRF, quyền đối tượng, quota và route. Authenticated POST không chấp nhận user_id như quyền; subject_id là resource cần kiểm tra. Không lưu payload đầu vào ở edge logs. Không dùng Origin/CORS thay auth. BFF cho web giữ session HttpOnly; mobile/partner dùng token có scope qua IdP được chọn.
## 4. Kết nối database
Hyperdrive query cache phải tắt cho kết nối nghiệp vụ cá nhân hóa; dùng kết nối riêng nếu cần cache dữ liệu công khai. Truy vấn parametrized. Dùng transaction-bound SET LOCAL cho context nếu triển khai RLS; tuyệt đối không giữ user context session-wide trên pool. Service role không BYPASSRLS; report worker không dùng vai trò chủ bảng.
## 5. Assets và deployment
Thay rsync denylist bằng allowlist build có kiểm tra. Docs, API source, engine tests, .env và dữ liệu không thuộc public bundle. App shell fallback chỉ dưới /app; route API và marketing không được trả app index nhầm. CI build từ exact SHA sạch, deps khóa phiên bản, SBOM và digest. Pages/Worker receipt độc lập; release manifest chỉ hợp lệ khi chúng tương thích schema/method versions.
## 6. Rollback
Giữ artifact an toàn gần nhất; không quay lại build có lỗi auth hoặc điểm giả. Dùng expand–contract migrations: deploy code đọc cả schema cũ/mới trong cửa sổ xác định, migrate, rồi mới bỏ cột. Thử rollback trên dữ liệu tổng hợp trước production. Không xóa dữ liệu hoặc khóa người dùng bằng một script “cleanup” không có review.
