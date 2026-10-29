# Giao việc cho AI và DEV: bối cảnh, lệnh thực hiện và báo cáo

Mã tài liệu: **D36** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Tech Lead + AI Engineering. Nguồn đối chiếu: G02, G09, G10. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Start here cho đội thực thi
Đọc README và baseline, quyết định Q, P0 runbook, source-target matrix, contracts và task tương ứng. Không bắt đầu bằng build UI mới. Kiểm tra repo/branch/HEAD, môi trường, clean working copy ngoài iCloud và quyền được giao. Chưa có receipt thì báo BLOCKED_RECEIPT, không tự đoán deployed SHA.
## 2. Hợp đồng một work item
Mỗi task phải có mục tiêu, scope files, inputs, dependencies, forbidden actions, acceptance, tests, rollback và output evidence. AI chỉ làm trong branch được giao; không sửa shared schema hoặc policy ngoài scope. Không dùng dữ liệu khách làm fixture. Một commit nhỏ với test và giải thích tốt hơn nhiều sửa đổi lan rộng thiếu integration owner.
## 3. Báo cáo cuối phiên
Ghi file thay đổi, logic thay đổi, test đã chạy, test chưa chạy, lỗi/blocked, diff summary, risk, review yêu cầu và next task. Không báo90% done khi chưa biết denominator. Không ghi tests pass nếu mới đọc package.json. AI không được tự quảng bá production-ready chỉ vì sample chạy.
## 4. Commands và secret
Trong bộ này, reference scripts chỉ chạy trong container/local với dữ liệu tổng hợp. Không có script tự deploy, migrate production, revoke session thật hoặc reset repo. Hướng dẫn production cần scope riêng và người duyệt. Secret truyền qua manager/CI, không paste vào chat hay doc. `.env.example` nếu tạo về sau chỉ chứa tên biến không giá trị; giá trị thiếu ghi rõ required decision.
## 5. Handover prompts
Prompt cho backend yêu cầu triển khai owner-scoped queries theo OpenAPI và auth matrix, không tin client IDs. Prompt frontend yêu cầu không tính score riêng, đủ states/a11y, không log payload. Prompt method yêu cầu passport và tests. Prompt AI yêu cầu claim-driven writer, retrieval ACL. Prompt QA yêu cầu negative tests. Prompt release yêu cầu build allowlist/receipt/rollback và không deploy khi chưa có quyền.
## 6. Tái sử dụng và đổi phiên bản
Lõi hiện tại JS/TS được tái cấu trúc theo package; không chuyển hết sang Python chỉ để có kiến trúc đẹp. Legacy templates bị deprecated, không âm thầm dùng khi thiếu content mới. Khi phát hiện mâu thuẫn tài liệu, báo decision cần chốt thay vì chọn lời thuận lợi. Artifact package này là baseline thiết kế chờ phê duyệt, không phải patch repository.
