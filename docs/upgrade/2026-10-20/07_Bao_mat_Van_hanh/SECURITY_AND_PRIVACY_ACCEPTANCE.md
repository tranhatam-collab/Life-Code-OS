# Life Code OS Hợp đồng nghiệm thu bảo mật và quyền dữ liệu

Ngày 20/10/2026. Bổ sung D03, D25, D26 và P0 packet. Phạm vi là thiết kế, test contract và trình tự giao việc. Chưa có thao tác thu hồi phiên, truy vấn dữ liệu hoặc đóng surface production trong lần nâng cấp tài liệu này.

## Identity và query

Principal do IdP/session verifier phía server xác định, có issuer, audience, expiry, session status và tenant membership. Legacy user_id không được dùng để cấp identity. Subject ID trong URL/body chỉ là target; service authorize target và purpose trước query. Missing identity trả 401; target không có quyền trả 404 theo policy chống enumeration hoặc 403 khi cần giải thích cho chủ thể đã biết. Body và timing không làm lộ title/count của người khác.

Mọi list/search/export/download/aggregate cũng phải scope tenant, subject, fields, purpose và grant version. Query policy và RLS kiểm thử cùng nhau bằng role không owner/superuser/BYPASSRLS; transaction context SET LOCAL từ principal đã xác minh, reset khi trả connection. Test cả pool reuse A→B và failed transaction.

Bearer mới không lưu raw token DB/log. Web session ưu tiên cookie HttpOnly Secure SameSite phù hợp cùng CSRF và Origin checks cho mutation. Server lưu hash hoặc managed session handle, idle/absolute expiry và revoke epoch. Recovery cần chứng cứ quyền độc lập; biết tên/ngày sinh hay token legacy không chứng minh ownership.

## Ma trận tối thiểu

Với mỗi endpoint, bao phủ anonymous, owner, cùng tenant khác subject, khác tenant, expired session, revoked session, expired grant, revoked field, purpose mismatch và forbidden admin. Assert status, error code, response schema, không có side effect, audit event đã redacted và không lộ identifier. Chạy lại cho path/body/query/header IDs, bulk/list và các endpoint tương thích.

Job có authorization snapshot để audit nhưng quyền thực thi phải được kiểm tra lại lúc dequeue và trước publish/download. Grant revoked giữa hai bước làm job cancelled/blocked theo contract; artifact tạm bị quarantine/purge. Khi replay DLQ, revalidate schema, current consent/grant, deleted subject và idempotency ledger.

## Dữ liệu và nguồn

Data inventory gắn data class, controller, purpose/legal basis đã được chức năng duyệt, collection source, storage systems, access roles, retention rule, deletion rule và vendor. Bảng 120 trường không là consent screen. Consent cho dịch vụ, marketing, training, research và chia sẻ là các mục độc lập; mặc định không tự opt-in.

Lineage graph phải cho phép tìm derived result/report/vector/job nào phụ thuộc input hoặc source đã revoked. Xóa gồm DB, objects, cache, search/vector, queue/DLQ và vendor theo contract; immutable snapshot vẫn phải có cơ chế rút truy cập và xóa phần dữ liệu khi nghĩa vụ yêu cầu. Receipt phải nói rõ bản sao còn trong backup rotation và legal exceptions; không khẳng định xóa tức thời toàn hệ.

## Trình duyệt và artifact

Không lưu report/profile/token trong localStorage mặc định. Service worker chỉ cache public shell/versioned public knowledge được rights policy cho phép. Logout, chuyển tài khoản, đổi tenant và thu hồi chia sẻ đều có cache tests. CDN cache key không đủ để thay access check; private endpoints dùng no-store khi chưa có thiết kế cache đã được chứng minh.

Report renderer chạy isolated, không network tùy ý, không file URL, giới hạn page/byte/memory/time. Test HTML/template injection, SVG, URL redirect, DNS rebinding/SSRF, oversized Unicode và decompression bomb khi feature upload được mở. Content Security Policy và security headers được test trên artifact thực; header có mặt không chứng minh toàn ứng dụng an toàn.

## Source và phương pháp

Nguồn ngoài, prompt và tài liệu đính kèm là dữ liệu không đáng tin. Chúng không cấp quyền chạy tool, sửa policy hoặc mở dữ liệu. Retrieval lọc ACL trước context và trước citation; một document được chia sẻ không chia sẻ toàn tenant. Method release yêu cầu source edition, rights receipt, reviewed rules, golden cases và policy label. Withdrawal ngăn mọi job dùng release đó và đánh dấu các báo cáo chịu ảnh hưởng.

## Kết thúc kiểm tra

Security review độc lập trên exact diff/RC; retest findings có exploitability rationale và scope. Không suy từ unit policy tests thành runtime authorization. SQL/RLS phải chạy trên PostgreSQL của staging; cookie/CSRF/OIDC cần browser integration; payment cần provider sandbox; backup cần restore. Evidence còn thiếu giữ gate BLOCKED hoặc NOT_CHECKED với owner và next action cụ thể.
