# Life Code OS Hướng dẫn nhận việc phát triển

Phiên bản 2026-10-20.r2. Mục tiêu là giúp từng DEV nhận một phần nhỏ, hiểu dữ liệu và công thức liên quan, chạy demo rồi tạo thay đổi có thể review. Bản này hợp nhất bộ 11/10 và kết quả audit 20/10; bảo toàn đầy đủ kế hoạch dài hạn.

## Đọc và chạy trong ngày đầu

1. Đọc `DOCUMENT_AUTHORITY.md`, `AMENDMENT_2026-10-20.md` và `09_Doi_chieu_Bang_chung/BASELINE_LOCK.json`. Xác nhận repo, nhánh và SHA thực tế bằng lệnh đọc Git trước khi nhận việc.
2. Đọc charter, sản phẩm và journeys trong `01_Chien_luoc_San_pham`; chọn đúng cohort và lát cắt sản phẩm. Không suy ra một người mua Level 9 đã có đủ dữ liệu cho mọi phương pháp.
3. Backend đọc `02_Tri_thuc_HNH`, `03_Du_lieu_Phep_tinh`, `04_Backend_API`, các schema và OpenAPI. Đọc passport, nguồn, phạm vi quyền và golden cases trước code từng thuật toán.
4. Chạy test và demo trong `10_Ma_tham_chieu_Kiem_thu` bằng dữ liệu tổng hợp. Xem đầu vào, bước tính, đầu ra, trường thiếu và lý do chặn. Các demo là oracle cho hợp đồng cục bộ, chưa chứng minh server đích đã triển khai.
5. Frontend đối chiếu screen registry, ma trận requirement và API. Thực hiện các trạng thái loading, empty, partial, denied, conflict, offline, quota và error trước khi gắn dữ liệu thật.
6. QA đọc P0 packet và negative matrix; chuẩn bị hai account tổng hợp cùng tenant và khác tenant. Mỗi case phải nêu endpoint, actor, policy version, expected status/body và chứng cứ không có side effect.
7. Nhận task triển khai khi blocking dependency và quyết định bắt buộc của lát cắt đã có receipt. Khi Q còn pending, chỉ chuẩn bị thiết kế có thể đảo ngược, schema, evidence và demo synthetic trong phạm vi được giao; không khóa lựa chọn hoặc dùng dữ liệu thật. Ghi đường dẫn được phép, test, rollback và người review trong task. Chỉ chạy command đã đọc scripts và xác định đúng môi trường.

## Ba lát cắt phát triển đầu

Lát cắt 0 là containment: identity không do client quyết định, query có owner scope, kết quả legacy bị cách ly, public build dùng allowlist, source gắn artifact. Việc đã viết runbook không đóng task containment.

Lát cắt 1 là công cụ miễn phí dùng input tối thiểu, phép tính xác định và lời giải thích từng bước. Lưu được mục tiêu và nhật ký trong account khi trust core đã đạt. Các phương pháp chưa có quyền hoặc chưa được duyệt vẫn hiển thị điều kiện nghiên cứu và ví dụ tổng hợp, không trả kết luận cá nhân.

Lát cắt 2 là báo cáo Level 1 từ profile version bất biến và method releases được phép, có quyền đọc/xuất/xóa, job retry/idempotency và template Web/PDF/Word nhất quán. Pilot chỉ bắt đầu sau gate staging; paid beta bổ sung commerce và support.

## Phân công theo hợp đồng

Product owner chốt problem, cohort, output và acceptance. Method lead chịu trách nhiệm source/rules/rights; Backend lead chịu trách nhiệm tính đúng, schema, auth và durability; Frontend lead chịu trách nhiệm trạng thái và khả năng sử dụng; QA độc lập giữ negative/golden/e2e; SRE giữ release/recovery; Privacy/Legal giữ áp dụng pháp luật. Tên người, năng lực và lịch làm việc phải được điền bằng quyết định phân công, không suy đoán từ vai trò.

Một task chỉ được coi hoàn tất khi có diff, exact SHA, command/exit code, test counts thực, evidence pointer, review và cập nhật requirement trace. Task triển khai không hoàn tất chỉ vì tài liệu đã được nâng cấp.

## Phạm vi công nghệ và thiết bị

Web công khai, ứng dụng web trên điện thoại và desktop, cùng PWA dùng chung API và method core. Không tính công thức nghiệp vụ lần hai ở frontend để tạo một số khác với backend. Desktop web có sidebar/keyboard và không gian so sánh; mobile dùng bố cục một cột, thao tác chạm và luồng nhập ngắn. Native app và desktop wrapper là các quyết định tương lai; kế hoạch có adapter boundary để mở rộng, không tự phát sinh lời hứa app-store.

## Cổng nhận việc tiếp theo

Thiếu quyền nguồn thì tiếp tục xây adapter, schema và demo tổng hợp với kết quả bị chặn rõ lý do. Thiếu provider thì dùng contract test local, không giả API live. Thiếu ngân sách thì giữ unavailable và nêu input cần điền. Thiếu người phê duyệt thì hoàn tất packet có thể review; task/decision liên quan chưa được mở, gate giữ NOT_CHECKED hoặc BLOCKED theo evidence thực tế. Những việc độc lập như tài liệu, test thuần và demo local vẫn có thể tiếp tục.
