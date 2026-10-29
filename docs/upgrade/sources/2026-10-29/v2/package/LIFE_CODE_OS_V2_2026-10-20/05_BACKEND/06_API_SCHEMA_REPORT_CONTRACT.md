# API, schema và báo cáo có thể truy vết

**Life Code OS · Bản nâng cấp bảo toàn V2 · 20/10/2026**  
**Trạng thái:** Đặc tả để triển khai và rà soát; không phải chứng nhận production.

## 1. Hai hợp đồng khác nhau
OpenAPI đích dùng /api/v2 và giữ 64 mã thao tác cũ. Các thao tác mới bổ sung về phương án dữ liệu, preview, method dependencies, impact review và request deletion. Mỗi operation ghi request/response, quyền, idempotency, concurrency, lỗi và trạng thái implementation. File OpenAPI không chứng minh endpoint đã live. [N04]

OpenAPI demo chỉ có health/catalog/run tại loopback. Không cấu hình cookie giả hoặc quảng bá auth của demo là production. JSON Schema 2020-12 kiểm cấu trúc; các ràng buộc liên trường như subject grants, date consistency hoặc probability calibration vẫn cần logic nghiệp vụ và test. [N10]

## 2. Claim là đơn vị kiểm soát nội dung
Sáu loại giữ nguyên: fact, self_report, observation, symbolic_interpretation, derived_metric, model_probability. Mỗi claim có evidence_ref, scope, temporal context và phiên bản. Model probability bắt buộc model release, target, horizon, population và evidence; symbol không được mang probability. confidence nếu dùng phải có kind và definition. “Dữ liệu đầy đủ” không là confidence về đời người.

## 3. Report assembly
Một report snapshot chỉ dùng claims được cấp quyền từ các result cụ thể. Mỗi section giữ supporting_claim_ids, title, narrative_blocks, tables, limitations, questions, actions và review_state. AI viết từ danh sách claims, không đọc cả kho khách. Renderer HTML/PDF/Word dùng chung content model, không tính công thức riêng.

## 4. Chín template, không chín đoạn văn chung
Level 1 cần calculation traces và input uncertainty; Level 2 cần các ví dụ người dùng xác nhận; Level 3 cần dữ liệu hành vi theo khoảng thời gian; Level 4 cần kịch bản nguồn lực; Level 5 cần giới hạn dữ liệu hai bên; Level 6 tách bốn đường thời gian; Level 7 ghi điều kiện ảnh; Level 8 ghi lựa chọn sứ mệnh; Level 9 liên kết và loại lặp. Thiếu input tạo section unavailable rõ ràng, không tăng trang bằng văn bản sáo rỗng.

## 5. Định dạng lỗi và thay phiên bản
400 cho JSON không hợp lệ;401 chưa xác thực;403/404 theo anti-enumeration policy;409 conflict nghiệp vụ;412 version precondition;422 dữ liệu hợp lệ JSON nhưng không đạt schema;429 quota;503 phụ thuộc tạm không sẵn. Problem Details không lộ query hay dữ liệu subject khác. Deprecated endpoint có sunset plan và adapter giới hạn; không giữ endpoint cũ không auth chỉ để “tương thích”. [N05]

## 6. Report security
Render chạy sandbox, mặc định không network egress. Chỉ cho tài nguyên đã allowlist, không nhận URL tùy ý để tránh SSRF. Tệp private, kiểm quyền mỗi lần cấp link. Link ký trước có thời hạn và vẫn có thể được dùng đến hết hạn; khi cần revoke tức thì dùng proxy download kiểm quyền. Word và PDF phải có text thật, mục lục, font tiếng Việt và không chứa metadata cá nhân thừa.

**Tra nguồn:** xem `11_SOURCES/SOURCE_ADDENDUM.csv`; các mã Nxx là nguồn đối chiếu chính thức, không phải mọi nhận định của HNH đã được khoa học xác nhận.
