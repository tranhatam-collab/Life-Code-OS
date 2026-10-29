# Mã tham chiếu và kiểm thử cục bộ

Chạy: `npm test` trong thư mục này bằng Node 22 trở lên. Không cần cài dependency bên ngoài.

Đây là **reference package**, không phải ứng dụng production. Không có IdP, PostgreSQL, payment provider, migration production hoặc quy trình deploy. `ReceiptLedger` là mô phỏng trong bộ nhớ để minh họa idempotency; production cần transactional ledger/outbox. Hàm `allowed` là policy minh họa, không thay xác thực, RLS hoặc E2E. Method/source rights và Founder approval vẫn chưa được cấp qua các test này.

Bảng 80 mục giữ nhãn do người dùng cung cấp; chủ đề được biên tập, chưa có quyền tuyên bố bảng cổ truyền duy nhất. 0 mặc định unresolved. Số 0/5 trong phân tích cặp vẫn unresolved; không suy bệnh, tài lộc hoặc nội tâm từ số.

Kết quả chạy hiện hành nằm ở `test-results.tap` và receipt QA. File TAP của working copy 2026-10-20 được tạo bằng `node --test --test-reporter=tap tests/*.test.mjs`, hiện ghi đúng 173/173 test; `npm run test:tap` gọi cùng lệnh. Bản 83/83 ngày 2026-10-11 vẫn được bảo toàn trong source package. Test exhaustive kiểm tra 10.000 chuỗi, không phải 10.000 cuộc đời.

## Bổ sung 2026-10-20

- `data/demo_cases.json`: đúng 64 ca tổng hợp có exact expected output/error; không ca nào là hồ sơ người thật hoặc chứng nhận phương pháp.
- `src/decimal.mjs`: tỷ lệ rational → decimal string bằng BigInt, scale/rounding rõ và mẫu số 0 trả null reason.
- `src/timeline.mjs`: khoảng tuổi theo civil date, chính sách 29/02 rõ, không đổi date-only qua timezone và không tạo forecast.
- `tests/demo-suite.test.mjs`: chạy toàn bộ demo manifest.
- `tests/backend-contract.test.mjs`: kiểm 64 operation ID, permission registry, registry K01–K20, schema/ref và demo offline.
- `tools/resolve_openapi.py` + `requirements-openapi-resolver.txt`: materialize/check deterministic `openapi.resolved.yaml` và semantic JSON mirror, không network.
- `../04_Backend_API/API_RESPONSE_DESIGN_PACKETS.json` và `.md`: packet fail-closed cho đủ 46 generic success response; mọi proposal vẫn chưa overlay và chưa codegen.
- `demo.html`: explorer responsive chạy `file://`, không network/storage/cookie; Ctrl/⌘+Enter để chạy trace.

Các family K01–K20 chưa có source/right/rule/release gate đầy đủ chỉ hiển thị trạng thái registry, không tạo kết quả hư cấu. `npm test` vẫn chỉ là receipt reference local; không chứng minh API, PostgreSQL, IdP, RLS, migration hoặc production.
