# Danh tính, phiên, chia sẻ và kiểm soát đối tượng

Mã tài liệu: **D15** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Security + Backend. Nguồn đối chiếu: G04, G08, G11, S07, S08, S09. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Phiên mới không dựa vào danh tính client tự khai
IdP giải quyết đăng nhập, MFA, recovery và account verification theo cấu hình đã duyệt. BFF tạo session nội bộ từ danh tính đã xác thực. Cookie ưu tiên __Host-lc_session, Secure, HttpOnly, Path=/, không Domain; SameSite và callback flow được kiểm thử. Luồng web mutation có CSRF token/Origin check thích hợp; CORS là kiểm soát khác.
Nếu tự quản session, token đủ entropy, DB chỉ lưu digest/HMAC kiểm tra kèm expiry, revocation, created_at và auth_strength. Không log bearer, không đặt token trong URL/localStorage. Session rotation sau đăng nhập, nâng quyền và recovery; revoke all khi nghi ngờ. Idle/absolute TTL cấu hình theo loại vai trò, không làm hardcoded session sống mãi.
## 2. Công thức quyền
Allow = authenticated ∧ active account ∧ resource state allowed ∧ matching grant ∧ allowed purpose ∧ valid processing basis. Operation trả phí thêm entitlement. Grant có subject/resource/category/action, expiry, grantee và revoker. Organization membership không thay personal grant. Người có report ID nhưng không có quyền nhận 404/403 nhất quán theo policy, không lộ metadata khác chủ thể.
## 3. Điều chỉnh đồng thời và TOCTOU
Kiểm tra quyền tại intake, khi job bắt đầu và trước phát hành. Permission revision tăng khi thu hồi, worker phải kiểm tra revision mới nhất. Update nhạy cảm kiểm tra row/version trong transaction; optimistic concurrency bằng If-Match. Grant bị thu hồi trong khi export thì artifact chưa phát hành bị hủy/ẩn. Background role chỉ được quyền cho task scope, không quyền query toàn cơ sở dữ liệu.
## 4. Chuyên gia và break-glass
Practitioner chỉ thấy phần subject chia sẻ cho case. Ghi chú nội bộ phân loại rõ; khách hàng được biết quyền tiếp cận theo luật và policy. Support không xem nội dung đời tư để xử lý lỗi thanh toán. Break-glass cần hai người hoặc approval có thời hạn, reason code và audit; dùng để xử lý sự cố xác định, không phục vụ tò mò hoặc nghiên cứu.
## 5. Nghiệm thu
Ma trận A chủ thể 1, B chủ thể 2, practitioner có grant giới hạn, org admin, suspended account và anonymous. Test mọi read/update/list/export/search/job status/attachment. Kiểm thử token sai, stale, revoked; object thuộc tenant khác; grant đúng người sai purpose; kết quả từ profile version khác; report được đoán ID. Không kiểm thử trên người dùng thật khi chưa có scope riêng.

## Bổ sung 2026-10-20 — policy registry và failure matrix

`AUTHORIZATION_POLICY_MATRIX.json` định nghĩa policy cho toàn bộ permission label của 64 operation ID hiện có; `06_AUTHORIZATION_POLICY_AND_NEGATIVE_MATRIX.md` khóa trình tự server-side resource resolution, 401/403/404, CSRF, job recheck, permission revision, RLS và các ca âm. Đây là contract mục tiêu; không suy ra code baseline đã được sửa. CORS tiếp tục là kiểm soát trình duyệt, không phải quyền đối tượng.
