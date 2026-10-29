# Phạm vi đã làm và giới hạn còn lại ngày 20 tháng 10 năm 2026

## Đã thực hiện trong bản hợp nhất

149 tệp nguồn ngày 11/10 được đọc hoặc trích xuất toàn bộ nội dung phù hợp định dạng, đối chiếu ZIP với thư mục giải nén và giữ nguyên byte trong `sources/2026-10-11`. Bản mới giữ 38 chuyên đề cũ, 23 sản phẩm, 9 cấp, 20 họ phương pháp, 120 trường và 45 màn hình; bổ sung hợp đồng phát triển, 156 công việc, 87 dòng trace yêu cầu, 20 decision packet và 64 ca demo tổng hợp. Kiểm tra nguồn ngoài có phạm vi đọc và giới hạn riêng trong registry; không phải đã đọc mọi sách được nhắc tới.

Tạo checkout độc lập từ nguồn Git đã khóa tại `336ef35a8386a744c6de18a7f7c6e268e89e6dac`; không sửa checkout handover đang dirty. Thay đổi hiện tại là local worktree trên `codex/complete-upgrade-plan-2026-10-20`, chưa commit, push hoặc deploy. Hồ sơ cũ được giữ và chỉ bổ sung chỉ dẫn phiên bản mới.

## Chưa được xác nhận và vẫn là gate bắt buộc

- Production/deployed SHA, provider version, tài khoản dịch vụ, DNS và cấu hình hiện phục vụ.
- Authentication thật, session revocation, tenant/subject/purpose/action scoping, RLS dưới đúng DB role, payment/webhook thật, queue bền vững và durable idempotency ledger.
- Migration D1 sang PostgreSQL, reconciliation, backup restore, rollback, load/SLO và pentest trên môi trường được cho phép.
- Nguồn quy tắc, quyền khai thác, bản dịch và sự phù hợp của từng phương pháp trong 20 họ; demo không mở method release.
- Năng lực dự đoán, chẩn đoán hoặc tuyên bố khoa học về số phận. Bộ hồ sơ không xác nhận các tuyên bố này.
- Pháp lý áp dụng đầy đủ tại từng thị trường, privacy impact, quyền thương hiệu, franchise, giấy phép chuyên môn và thủ tục thương mại. Một số văn bản chỉ mới kiểm tra metadata chính thức, không được gọi là kết luận tuân thủ.
- Named owners, ngân sách có báo giá, lịch cam kết và phê duyệt Q1–Q20. Khoảng ngày công là proposal, không phải cam kết thời gian hay chi phí.

## Tính chất hợp đồng và mã tham chiếu

OpenAPI/schema/SQL là hợp đồng thiết kế và scaffold, không phải backend đang chạy. SQL tham chiếu chưa được thực thi hoặc phân tích bằng PostgreSQL trong phiên này. RLS bật/force không thay policy và role tests; owner, superuser và BYPASSRLS phải kiểm tra riêng. Dùng `OPENAPI_UPGRADE_NOTES.md` để phân biệt base, overlay và artifact hợp nhất; các payload generic còn lại phải được đặc tả trước khi codegen endpoint liên quan.

Reference functions và 64 fixture dùng dữ liệu tổng hợp, không gọi IdP, DB, AI trả phí hoặc payment. Authorization demo không thay middleware hoặc query scoping. Ledger trong bộ thử là mô hình bộ nhớ, không thay transaction và kho bền vững. Các ca date/decimal/normalization chứng minh quy ước phần mềm trong phạm vi test, không chứng minh giá trị diễn giải cá nhân.

## Phạm vi kiểm tra đầu ra

Xem `PACKAGE_QA.json`, `WORKBOOK_QA.json`, `EXPORT_QA.json`, `BROWSER_QA.json` và `10_Ma_tham_chieu_Kiem_thu/test-results.tap` cho command, số lượng và giới hạn thực tế. Không suy từ test xanh sang E2E sản phẩm, production readiness, WCAG toàn ứng dụng, PDF-UA hoặc native app acceptance. Portal và Demo Lab là giao diện đọc/minh họa của bộ kế hoạch; chưa phải 45 màn hình sản phẩm.

## Quyền và trạng thái

Yêu cầu của Founder cho phép nâng cấp bộ kế hoạch và tích hợp attachment cục bộ. Nội dung “lệnh thi công” trong attachment chỉ là nguồn cần đối chiếu. Không có phê duyệt giá, method, nhà cung cấp, thị trường, dữ liệu thật hoặc production được tự tạo. Release giữ **HOLD** cho tới receipt đúng baseline và approval đúng thẩm quyền.
