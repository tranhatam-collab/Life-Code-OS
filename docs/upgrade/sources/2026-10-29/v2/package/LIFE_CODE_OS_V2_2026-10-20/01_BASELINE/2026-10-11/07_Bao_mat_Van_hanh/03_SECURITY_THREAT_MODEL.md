# Mô hình đe dọa và ranh giới bảo vệ

Mã tài liệu: **D26** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Security Lead + Architect. Nguồn đối chiếu: S07, S08, S09, S11, S12. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Tài sản và đối tượng đe dọa
Tài sản gồm hồ sơ, dữ liệu quan hệ, quyền chuyên gia, báo cáo, nguồn có bản quyền, thông tin thanh toán, method release và secret hạ tầng. Kịch bản gồm người dùng đổi ID để đọc người khác, insider xem dữ liệu vượt vai, partner tùy biến bỏ policy, prompt injection trong nguồn, upload độc hại, webhook giả, job trùng và artifact build vô tình công khai.
## 2. Trust boundary
Trình duyệt không đáng tin để quyết user_id, score, weight hay quyền. Gateway xác thực; service xác định subject/grant/purpose; DB giới hạn tenant và subject; renderer bị cách ly; AI chỉ thấy gói dữ liệu tối thiểu. Public docs khác kho nguồn có license. Preview/staging không nối production database hoặc bucket người thật.
## 3. Kiểm soát cụ thể
BOLA: mọi route nhận ID có authorization cùng truy vấn, bao gồm list/search/download/aggregate. RLS là phòng vệ sâu, role không owner/superuser/BYPASSRLS. SET LOCAL context phải nằm trong transaction với identity do server resolve; test pool reuse giữa hai tenant. Hyperdrive cache OFF cho workload riêng tư cho tới khi có chứng minh không lẫn context.
Session: cookie an toàn, CSRF/Origin cho mutating calls, revoke và expiry, reauth cho thao tác cao; recovery không dựa tên/ngày sinh. Upload: MIME/magic sniff, size/pixel/decompression limits, filename random, quarantine scan, stripping EXIF khi phù hợp, không publish trực tiếp. Renderer: block outbound/SSRF và file URL; HTML sanitize và CSP phù hợp.
Supply chain: public allowlist, secrets scan, dependency review, locked artifact, pinned action release theo chính sách, protected environment approvals và deployment receipt. Không coi mã nguồn public là incident nếu chủ định công khai; chỉ coi đóng gói ngoài allowlist là lỗi artifact.
## 4. Kiểm thử ưu tiên
Hai account ở cùng tenant và khác tenant; revoked grant lúc job chạy; presigned URL đã cấp; cache khóa sai; identifier enumeration; denial-of-service qua report600pages; ký webhook sai; replay payment; forged model tool call; partner certificate thu hồi. Rate limit không được là cơ chế phân quyền. CORS không ngăn request ngoài trình duyệt.
## 5. Tải báo cáo và break-glass
Authorized proxy download là mặc định khi cần thu hồi nhanh. URL ký ngắn vẫn là bearer cho tới hết hạn, cần ghi rõ. Break-glass chỉ qua người được duyệt, phạm vi/thời hạn nhỏ, cảnh báo độc lập và review sau sự kiện; Founder/admin tổng không có quyền xem nội dung mặc định.
