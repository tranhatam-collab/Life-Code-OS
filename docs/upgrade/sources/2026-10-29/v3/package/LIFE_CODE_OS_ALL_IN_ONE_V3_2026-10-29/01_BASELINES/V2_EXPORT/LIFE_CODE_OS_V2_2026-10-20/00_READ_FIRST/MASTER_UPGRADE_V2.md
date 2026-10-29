# Kế hoạch hợp nhất V2: giữ nền cũ, làm sâu backend, đưa trải nghiệm vào vận hành

**Life Code OS · Bản nâng cấp bảo toàn V2 · 20/10/2026**  
**Trạng thái:** Đặc tả để triển khai và rà soát; không phải chứng nhận production.

## 1. Mục tiêu và quyết định kiến trúc
Bản V2 không thay bằng một kế hoạch khác. Toàn bộ 149 tệp của gói ngày 11/10/2026 được giữ nguyên trong `01_BASELINE/2026-10-11`. Tệp ZIP gốc cũng được giữ nguyên; bốn đính kèm trực tiếp được xác nhận trùng hash với tệp trong ZIP. Danh mục 23 sản phẩm, 20 họ phương pháp, 12 lớp, 12 trường đồng nhịp, chín cấp, 120 trường dữ liệu tùy chọn, 140 công việc và Q1–Q20 vẫn tồn tại. V2 bổ sung hợp đồng thực thi, ví dụ có thể chạy, tiêu chí nghiệm thu và lịch sử quyết định.

Hệ đích là một nền tảng tự hiểu và thiết kế đời sống: tri thức có nguồn; phép tính được tách khỏi diễn giải; dữ liệu thực được tách khỏi giả thuyết; hành động được theo dõi. Huyền Nhân Học giữ vai trò triết lý và ngữ pháp tổng hợp. Công nghệ không tự tuyên bố biết những bí mật chưa được người dùng cung cấp.

## 2. Điểm phát triển mới
Backend cần trả lời được không chỉ “mã nào được tính”, mà cả “tính từ dữ liệu phiên bản nào, theo quy tắc nào, kết quả thiếu gì, ai được xem, kết quả nào phải cập nhật khi nguồn thay đổi”. V2 đưa thêm 16 họ công thức tham chiếu, luồng hồ sơ Level 1, 90 tình huống demo, API demo chạy tại máy, ma trận kiểm thử và thiết kế kiểm soát concurrency. Bộ công thức nâng cao chưa đủ nguồn vẫn được giữ trong danh mục, có điều kiện mở, thay vì được thay bằng một lời luận ngẫu nhiên.

Frontend được thiết kế theo nhu cầu: hiểu mình, bộ số, công việc, quan hệ, nhịp sống, hồ sơ tổng hợp. Giao diện mobile và desktop dùng cùng kết quả máy chủ. Bản demo đã thể hiện tìm kiếm tình huống, chọn nhóm, tự nhập dữ liệu, xem lời giải từng bước và tải JSON; nó không giả làm ứng dụng đã có xác thực hoặc thanh toán.

## 3. Sản phẩm hoàn thiện cần làm được gì?
Người mới có thể dùng công cụ minh bạch và nội dung giáo dục mà không phải giao toàn bộ đời tư. Người có tài khoản giữ mục tiêu, nhật ký và các bản báo cáo. Người dùng trả phí nhận thêm phạm vi phân tích, xuất bản và rà soát, không mua “độ đúng của số phận”. Chuyên gia làm việc trên phần hồ sơ được chia sẻ. Tổ chức quản mục tiêu và phối hợp, không dùng phương pháp biểu tượng để tuyển dụng hoặc sa thải. Đối tác quốc tế chỉ mở nội dung, phương pháp và phạm vi đã được cấp phép.

Chín cấp là chín hợp đồng sản phẩm, không bắt buộc mua tuần tự. Body Intelligence không là điều kiện phải mua trước Mission Path. Hồ sơ trẻ em, nội dung sức khỏe và dịch vụ có tác động lớn có cổng riêng; không tự được mở chỉ vì phần mềm đã có ô nhập.

## 4. Căn cứ đối chiếu
Repo đúng là `tranhatam-collab/Life-Code-OS`. Remote `main` được đọc tại SHA `99b402764437f81859fa0cd3a3af860125f7bd52`; nhánh audit ngày 11/10/2026 tại `336ef35a8386a744c6de18a7f7c6e268e89e6dac`. Nội dung trang công khai được truy xuất lại, nhưng đây không phải biên nhận SHA đang chạy. Truy cập trực tiếp Engine Lab và health chưa xác minh được trong môi trường này. Không kết luận website ngừng hoạt động chỉ từ việc công cụ không truy cập được.

Các lỗi P0 trong audit cũ tiếp tục là căn cứ cần xử lý: cấp phiên tin ID client, truy cập đối tượng thiếu khóa chủ sở hữu, token thô, điểm hardcode và timeline lượng giác. Việc làm bản kế hoạch V2 và demo không sửa các lỗi production ấy. Toàn bộ cổng phát hành production giữ trạng thái chưa chứng minh.

## 5. Cấu trúc vận hành
Public web → Account/Subject/Grant/Purpose → Profile versions/Hypotheses → Method orchestrator → Deterministic core → Claim registry/HNH synthesis → Writer/Reviewer → Report snapshot/Action plan. PostgreSQL quản nghiệp vụ; private R2 quản tệp; queue/outbox quản tác vụ; policy và audit xuyên suốt. Modular monolith là điểm khởi đầu để kiểm soát phụ thuộc, không chia hàng chục microservice theo tên bộ môn.

Một codebase lõi JS/TypeScript tiếp tục phục vụ web, mobile, báo cáo và API. Python chỉ bổ sung cho nghiên cứu hoặc tính toán cần thư viện chuyên biệt. Việc chọn nhà cung cấp xác thực, PostgreSQL, AI và thanh toán vẫn là quyết định phải duyệt; không được viết tài liệu như thể đã ký hợp đồng.

## 6. Cách dùng bộ V2
Founder đọc bản tổng hợp, danh mục quyết định và bảng khác biệt. Tech Lead đọc backend book, schema, OpenAPI, kế hoạch migration và P0. DEV chạy demo, kiểm thử và xem công thức trước khi triển khai adapter thật. QA dùng corpus và ma trận negative tests để tái kiểm. Biên tập dùng ví dụ người dùng đọc được, không chỉ cấu trúc JSON. Đội quốc tế dùng country pack và hợp đồng cấp phép, không tự dịch một trang web rồi mở bán toàn cầu.

Đọc kế hoạch không đồng nghĩa được quyền deploy. Mọi nhiệm vụ production vẫn cần phạm vi, người chịu trách nhiệm, branch, môi trường, evidence và điều kiện quay lui. Người triển khai phải nhận rõ khác biệt giữa `REFERENCE_TESTED`, `DESIGN_ONLY`, `RESEARCH_ONLY` và `PRODUCTION_VERIFIED`.
