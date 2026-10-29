# OpenAPI v2.1 — contract hiện hành và cách tái tạo

`openapi.json` và `openapi.yaml` là bản gốc 2026-10-11 và được giữ để đối chiếu. `openapi.upgrade.overlay.yaml` là **OpenAPI Overlay 1.2.0** đề xuất ngày 2026-10-20, không phải API đã triển khai.

**Canonical current planning contract:** `openapi.resolved.yaml`. `openapi.resolved.json` là semantic mirror dành cho máy. DEV, contract test và codegen thử nghiệm phải bắt đầu từ file resolved, không bắt đầu từ hai base cũ hoặc overlay đứng riêng. Trạng thái vẫn `DESIGN_APPROVAL_PENDING_NOT_IMPLEMENTED`; “current” ở đây chỉ có nghĩa là hợp đồng thiết kế mới nhất trong gói.

Overlay thực hiện bốn việc:

1. Giữ nguyên toàn bộ 64 `operationId`.
2. Liên kết mọi operation với `API_OPERATIONS.json` và `AUTHORIZATION_POLICY_MATRIX.json`.
3. Thay chín schema nhúng bị trùng bằng schema canonical trong `03_Du_lieu_Phep_tinh/schemas/`.
4. Đánh dấu `Resource` generic là blocker; operation production phải có response schema cụ thể.

## Artifact resolved và lệnh tái tạo

Resolver local là `../10_Ma_tham_chieu_Kiem_thu/tools/resolve_openapi.py`; dependency được pin tại `../10_Ma_tham_chieu_Kiem_thu/requirements-openapi-resolver.txt`. Script không dùng network, clock, environment hay random input.

```bash
python3 10_Ma_tham_chieu_Kiem_thu/tools/resolve_openapi.py
python3 10_Ma_tham_chieu_Kiem_thu/tools/resolve_openapi.py --check
```

Chạy hai lệnh từ thư mục `docs/upgrade/2026-10-20`. `--check` không ghi file và thất bại nếu JSON/YAML resolved không còn khớp base, overlay hoặc chín schema canonical. Trình tự máy thực hiện:

1. Xác nhận `openapi.json` và `openapi.yaml` base bằng nhau về semantic.
2. Chỉ nhận Overlay 1.2.0 trỏ đúng base local; target ngoài tập đã kiểm soát làm resolver fail.
3. Apply đủ 17 action và đối chiếu đủ 64 record registry theo `operationId`, method, path, permission, request schema, response schema và success status.
4. Nhúng nguyên object của chín JSON Schema canonical; artifact resolved không còn external `$ref`.
5. Resolve toàn bộ 655 local JSON Pointer; ref đứt hoặc ref ra ngoài repo làm build fail.
6. Tạo mapping success contract cho đủ 64 operation; 46 operation còn dùng `Resource`/`ResourcePage` được ghi riêng là `TRANSITIONAL_GENERIC_BLOCKER` và `x-lc-codegen-ready: false`.
7. Ghi input SHA-256 vào `info.x-lc-input-sha256`; không ghi timestamp để output lặp lại byte-for-byte.

Trong working copy 2026-10-20, record `health` của `API_OPERATIONS.json` đã được sửa từ generic `Resource` sang `HealthStatus` để khớp response 200 trong cả hai base OpenAPI. Bản gốc 2026-10-11 trong `docs/upgrade/sources/2026-10-11/package` không bị sửa. Resolver fail ngay nếu registry và spec lại lệch ở bất kỳ trường nào nêu trên.

## Blocker còn lại

46 operation resolved vẫn trả `Resource` hoặc `ResourcePage` với `attributes` mở. Artifact ghi method, path, success status, route namespace và generic ref của từng operation trong `x-lc-generic-response-blockers`; đây là mapping có thể kiểm tra, không phải schema nghiệp vụ được bịa. `Resource.attributes` và cả hai generic envelope đều ghi `x-lc-codegen-ready: false`.

`API_RESPONSE_DESIGN_PACKETS.json` và bản đọc người `API_RESPONSE_DESIGN_PACKETS.md` phân rã đủ 46 operation thành named-response proposal, field whitelist public/private/server-only, null/missing rule, read scope, failure cases, dependency task, approval receipt còn thiếu và câu hỏi mở. Chín packet thiếu entity/contract nguồn được đánh dấu `BLOCKED_SOURCE_MODEL_GAP`; không packet nào được tự động nhập vào resolved spec và `codegen_ready_count` vẫn bằng 0.

UPG-BE-006 phải thay từng operation bằng named response schema dựa trên module implementation và field-level authorization review. Không được gọi candidate là production-ready, không được sinh SDK domain production và không được đóng gate khi blocker count chưa bằng 0.

Nguồn định dạng overlay: <https://spec.openapis.org/overlay/latest.html>.

