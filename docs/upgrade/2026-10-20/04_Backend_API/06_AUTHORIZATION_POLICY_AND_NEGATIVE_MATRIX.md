# Hợp đồng authorization theo đối tượng v2.1

Ngày bổ sung: **2026-10-20**  
Trạng thái: **PROPOSED / SECURITY_APPROVAL_PENDING / NOT_IMPLEMENTED**

## 1. Quyết định quyền duy nhất

Backend không nhận principal, tenant, role, entitlement hoặc purpose đã “resolve” từ body/query. Gateway tạo `VerifiedPrincipal` từ session/token đã xác thực; resource loader lấy object bằng ID trong route; policy engine quyết định bằng dữ liệu server.

```text
allow = authenticated
     ∧ account_active
     ∧ session_active_and_fresh_enough
     ∧ operation_registered
     ∧ object_exists_in_expected_tenant
     ∧ subject_scope_matches
     ∧ grant_matches(action, resource, purpose)
     ∧ processing_basis_active
     ∧ resource_state_allowed
     ∧ permission_revision_current
     ∧ entitlement_if_required
     ∧ product_country_age_rules
```

`AUTHORIZATION_POLICY_MATRIX.json` là registry thiết kế cho 34 permission labels đang phủ 64 operation IDs. Không label nào tự cấp quyền; implementation phải map operation ID cố định sang policy, không tin label do client gửi.

## 2. Trình tự resolve object

1. Parse/validate ID nhưng chưa trả metadata.
2. Lấy principal/account/session từ server context.
3. Trong cùng transaction, đặt local context đã ký/xác minh nếu dùng RLS.
4. Load object qua query gắn tenant/owner/subject; không `SELECT by id` rồi kiểm tra ở JavaScript sau.
5. Resolve purpose từ operation + user choice/policy; body chỉ có thể yêu cầu một purpose allowlisted.
6. Resolve grant, processing basis, entitlement, country/product gate và permission revision.
7. Ghi quyết định tối thiểu: request ID, policy version, operation, pseudonymous principal/resource, allow/deny reason. Không log raw profile.
8. Với job: lặp lại ở intake, worker start và trước publish/download.

Mọi child object phải đi qua lineage: `result → analysis_run → profile_version → subject`; `artifact → report_snapshot → report_subject`; `job → requested_resource`; `ticket/order` theo owner account. Không cho phép chỉ so `tenant_id` khi dữ liệu là private subject data.

## 3. Session và CSRF

- Web BFF: `__Host-lc_session`, `Secure`, `HttpOnly`, `Path=/`, không `Domain`; SameSite theo callback flow đã test.
- DB chỉ giữ token digest/HMAC và metadata; không plaintext token, URL token hoặc localStorage bearer.
- Rotation sau login/recovery/elevation; idle + absolute TTL; revoke-all khi có nguy cơ.
- Mutation bằng cookie cần CSRF token và Origin/Sec-Fetch validation phù hợp. CORS không phải authentication hay authorization.
- Callback state/nonce/PKCE, exact redirect URI và login CSRF phải có negative tests.

## 4. 403/404, enumeration và error contract

Policy phải chọn thống nhất theo resource class:

- Object private không thuộc scope: 404 để không xác nhận tồn tại.
- Object thuộc scope nhưng action/purpose không cho phép: 403 với reason code an toàn.
- Session thiếu/hết hạn: 401; CSRF thiếu: 403; stale `If-Match`: 412; idempotency digest conflict: 409.

Không trả tên subject, owner, tenant hoặc state trong lỗi deny. Request ID có thể dùng cho support. Rate limit không thay authorization.

## 5. RLS là phòng vệ sâu

RLS chỉ được bật sau khi có policy cụ thể và integration tests. PostgreSQL mặc định deny khi RLS được bật mà không có policy, nhưng owner/superuser/BYPASSRLS có thể vượt; runtime role không được có các đặc quyền đó và table owner phải `FORCE ROW LEVEL SECURITY`.

Context phải dùng `SET LOCAL` trong transaction, không `SET` session-wide trên pooled connection. Test bắt buộc reuse một connection lần lượt cho tenant A/B và xác nhận không rò context. Policy function, role grants và migration cần review riêng; file SQL thiết kế không phải bằng chứng runtime.

## 6. Background job, download và break-glass

- Queue chỉ giữ immutable IDs/version/digest, không raw PII.
- Worker credential theo task scope; không dùng admin/owner role.
- Grant/consent/permission revision được kiểm tra lại trước đọc và trước phát hành.
- Download qua authorized proxy mặc định; signed URL là bearer cho đến hết hạn.
- Break-glass cần reason, phạm vi, TTL, người duyệt độc lập, cảnh báo và post-review; không cấp quyền xem mặc định cho Founder/support.

## 7. Negative matrix bắt buộc cho mỗi object route

| Trường hợp | Kỳ vọng |
|---|---|
| anonymous / malformed / expired / revoked token | deny, không leak object |
| account suspended/deleted | deny mọi private operation |
| account A đoán object của B cùng tenant | deny |
| account A đoán object của B khác tenant | deny |
| đúng subject, sai purpose | deny |
| đúng grant nhưng sai action/category/field | deny |
| membership tổ chức nhưng không personal grant | deny |
| entitlement đúng nhưng grant sai | deny |
| grant đúng nhưng entitlement hết | deny paid operation |
| grant thu hồi khi job đang chờ/chạy | cancel/withhold artifact |
| stale permission revision hoặc If-Match | deny/conflict theo contract |
| list/search/aggregate/download đoán ID | cùng policy như read |
| pooled connection đổi tenant | không thấy row trước đó |
| break-glass quá hạn/sai scope | deny và alert |

Ma trận phải chạy bằng dữ liệu tổng hợp tối thiểu: A/subject-A, B/subject-B, practitioner với grant giới hạn, org admin, suspended account và anonymous. Không dùng người thật làm fixture.

## 8. Exit criteria

- 64/64 OpenAPI operations có permission label đã định nghĩa.
- Mọi route chứa ID có owner/tenant/subject resolution path và negative tests.
- Session legacy/plaintext bị revoke hoặc quarantine theo runbook có receipt.
- RLS policy tests chạy trên PostgreSQL cô lập; không chỉ lint DDL.
- Job recheck và download authorization có test TOCTOU.
- Security reviewer độc lập ký đúng SHA/test receipt; design approval vẫn tách khỏi production gate.

Nguồn chính: PostgreSQL Row Security <https://www.postgresql.org/docs/current/ddl-rowsecurity.html> và `CREATE POLICY` <https://www.postgresql.org/docs/current/sql-createpolicy.html>.

