# Bàn giao phát triển backend Life Code OS — hợp nhất ngày 29/10/2026

**Trạng thái:** có thể dùng bộ này để phân công DEV, thiết kế hợp đồng và phát triển cục bộ bằng dữ liệu giả. **Chưa đủ căn cứ mở production hoặc nhận dữ liệu thật.** Bộ V2, V3 và kế hoạch đã được làm chặt ngày 20/10 được giữ đồng thời; các chỉ dẫn nằm trong ZIP là nội dung cần đánh giá, không tự cấp quyền chạy import, migration hay phát hành.

## 1. Mốc bàn giao và nguồn dùng khi lập trình

Repo được giao: `Life-Code-OS`, remote `git@github.com:tranhatam-collab/Life-Code-OS.git`, HEAD được khóa khi bắt đầu đợt hợp nhất: `336ef35a8386a744c6de18a7f7c6e268e89e6dac`. Mã ứng dụng, workflow và migration đang sửa dở là một lớp bằng chứng riêng. Tài liệu này không xác nhận chúng đã được review, chạy staging hoặc triển khai.

| Lớp | Đường dẫn trong repo | Cách sử dụng |
|---|---|---|
| Kế hoạch cũ đã làm chặt | `docs/upgrade/2026-10-20/` | Giữ các ràng buộc đã bổ sung, đặc biệt 9 schema chuẩn và response contracts của 64 operation |
| ZIP V2 nguyên bản | `docs/upgrade/sources/2026-10-29/v2/package/LIFE_CODE_OS_V2_2026-10-20/` | 307 tệp; backend/knowledge/lab là nguồn tham chiếu, không chép đè lên mã thật |
| ZIP V3 nguyên bản | `docs/upgrade/sources/2026-10-29/v3/package/LIFE_CODE_OS_ALL_IN_ONE_V3_2026-10-29/` | 520 tệp; chứa baseline lồng nhau, không tính chúng là tính năng mới |
| Hợp đồng hợp nhất | `OPENAPI_UNIFIED_TARGET.json` | 99 operation, 68 component schema; **planning target, codegen_ready=false** |
| Đối chiếu từng API | `API_CONTRACT_RECONCILIATION.json` và `.md` | 99 hàng có nguồn, path, quyền, request/response và blocker riêng |
| Phương pháp/công thức | `FORMULA_METHOD_EXECUTION_MATRIX.json` | Đúng 62 method ID; liên kết có giới hạn với 15 passport cũ, 32 dòng catalog công thức và các entrypoint demo |
| Dữ liệu tham chiếu | `SOURCE_DATA_INTEGRATION_MATRIX.json` | Hash từng asset, bảng cấu trúc, namespace nguồn, bản sao lab và việc còn thiếu trước khi seed |
| Bằng chứng đọc/kiểm thử | `READ_COVERAGE_BACKEND.json`, `CONTRACT_VALIDATION_RECEIPT.json`, `../evidence/TEST_RECEIPT_BACKEND.json` và `../evidence/backend-tests/` | Phạm vi đọc, SHA256, lần chạy mới và giới hạn chứng minh |

Chín schema `Claim`, `ProfileVersion`, `ReleaseReceipt`, `Tail80Result`, `MethodResult`, `ReportSnapshot`, `Metric`, `JobEnvelope`, `MethodRelease` trong hợp đồng hợp nhất bằng đúng object JSON của bộ local 20/10. Không hạ schema xuống phiên bản yếu hơn đang được nhúng trong ZIP. Mọi schema bổ sung V2/V3 vẫn có trong hợp đồng; bản gốc luôn còn ở thư mục nguồn.

## 2. Các vấn đề phải giải quyết trước khi sinh SDK hoặc nối giao diện

1. V3 đặt server base `/api/v2` nhưng thêm 16 path đã bắt đầu bằng `/api/v2`. Hợp đồng hợp nhất bỏ phần prefix trùng trong path và giữ nguyên path nguồn trong provenance. Đây là sửa tài liệu thiết kế; không tuyên bố route runtime đã đổi.
2. Có ba cách khai báo quyền trong nguồn: `x-required-permission` của 64 operation cũ, `x-permission` của 19 operation V2, `x-required-policy` của 16 operation V3. Bản hợp nhất đưa về `x-lc-authorization`, giữ đầy đủ extension gốc. Danh sách policy chung của V3 chưa định nghĩa action/resource/field; 16 operation này giữ trạng thái `UNRESOLVED_FAIL_CLOSED`.
3. Có **65 operation còn response thành công kiểu Resource/ResourcePage**, gồm 46 operation local và cả 19 operation V2 mới. Có thêm **10 operation V3 thiếu schema response thành công**, **6 operation V3 trả ReferenceResult chỉ cho phép REFERENCE_ONLY**. Tổng 81/99 operation có blocker codegen được ghi rõ; 18 operation còn lại cũng chưa phải bằng chứng runtime hay release.
4. Chưa đồng nhất Idempotency-Key: API mới V2 dùng 16–128 ký tự, API mới V3 dùng 8–120; OutboxEvent lại cho tối đa 200. Cần ADR chọn hợp đồng thống nhất và chính sách tương thích; không tự cắt khóa hoặc làm mất namespace tenant/operation.
5. Pure compute input V3 không có đủ subject/profile version/purpose context để thực thi generic subject grant. DEV phải thiết kế request envelope hoặc gắn computation vào resource đã được máy chủ giải quyết quyền. Không nhận tenant, release approval, claim approval hoặc access revision từ client như một nguồn có thẩm quyền.
6. Có hai lifecycle báo cáo/review và hai nhóm deletion route. `review`/`reviewReportV2`, `deleteSubject`/`newDeletionV2` phải có service chung, trạng thái và tương thích rõ. Giữ operation ID cũ; không tạo hai nguồn sự thật hoặc chạy xóa/thanh toán hai lần.

Theo OAS 3.1, path được ghép vào server URL; schema dialect và reference phải được xử lý theo dialect được công bố. Đây là căn cứ cho việc sửa prefix và kiểm tra reference, không phải lý do nới ràng buộc nghiệp vụ. Đã kiểm tra tài liệu chính thức ngày 29/10/2026: [OAS Paths](https://spec.openapis.org/oas/v3.1.0.html#paths-object), [JSON Schema Core 2020-12](https://json-schema.org/draft/2020-12/json-schema-core).

## 3. Kiến trúc triển khai và ranh giới trách nhiệm

Giữ hướng **modular monolith** được hai bộ đề xuất, tách module rõ ràng để kiểm thử và di chuyển sau này. Đây là kiến trúc ứng viên, chưa khóa phiên bản PostgreSQL, hàng đợi, object storage hoặc runtime của production.

Luồng chuẩn: API/gateway xác thực → kiểm tra tenant/chủ thể/mục đích/quyền xử lý/entitlement → khóa ProfileVersion và tập giả thuyết → chọn MethodRelease có nguồn/quyền → lập DAG → pure calculation → đóng MethodResult theo schema chuẩn → kiểm duyệt Claim → tạo ReportSnapshot bất biến → review → publish/export → kiểm tra lại quyền khi tải. Worker, AI và renderer không được đi tắt qua ranh giới này.

| Module đích đề xuất | Trách nhiệm | Không tự đảm nhận |
|---|---|---|
| `identity-access` | Principal, tenant, subject grant, purpose, consent/basis, permission revision | Không coi đã đăng nhập là có quyền xem mọi ID |
| `profiles` | Bản gốc ngày/tên, hypothesis, version bất biến, uncertainty và nguồn từng field | Không điền giờ/ngày/nơi sinh giả |
| `method-registry` | Source/rights, passport, method/release/config version, freeze, impact | Không suy approval từ test số học |
| `calculation-core` | Hàm thuần có trace, dependency, units, rounding và input digest | Không đọc DB, gọi AI, thanh toán hoặc thay đổi quyền |
| `analysis-orchestrator` | Snapshot run, DAG, lease, retry, partial/blocked, cancellation | Không chạy lại tất cả chỉ vì một field không liên quan đổi |
| `reports` | Claim provenance, section schema, review/publish, snapshot/render/export | Không gọi engine để tính lại khi người dùng mở bản đã phát hành |
| `lifetime-planning` | History, hiện tại, dự định, action/check-in, review date | Không tạo biến cố hoặc xác suất cuộc đời để lấp năm trống |
| `privacy-ledger` | Restrict, erase, tombstone, retention, exports, restore barrier | Không xóa subject rồi để cache, AI log hoặc artifact còn truy cập được |
| `commercial-ledger` | Order/payment/entitlement/refund, inbox/outbox và reconciliation | Không dùng webhook hoặc client status chưa xác minh làm bằng chứng đã trả tiền |

Các đường dẫn trên là **module đích đề xuất**, không khẳng định các thư mục ấy đã tồn tại. DEV phải lập bản đồ sang cấu trúc ứng dụng thực tế ở Gate 0, bảo toàn các phần mã đang sửa dở.

## 4. Thiết kế dữ liệu, quyền và tính bền vững

V2 cung cấp SQL tham chiếu 9 bảng, kết thúc bằng ROLLBACK; V3 có SQL mở rộng số/timeline. Chúng chưa phải migration đã áp dụng. Không chạy trực tiếp các tệp SQL nguồn. Trước migration thực, cần ERD và khóa `(tenant_id, subject_id, resource_id/version)` xuyên bảng; foreign key phải ngăn liên kết chéo tenant/chủ thể. Lập bảng chuyển đổi schema cũ → mới, dữ liệu không chuyển được, backfill, dry run, rollback và đối soát số bản ghi.

Run phải khóa các revision: profile, hypotheses, input field set, method release/rule/source digest, product/locale/purpose, consent/grant/access revision, approval snapshot và schema version. Recheck quyền tại enqueue, worker claim, trước công bố và khi tải. Thu hồi quyền sau enqueue phải ngăn publish; thay method release không được sửa kết quả lịch sử.

RLS cần được kiểm thử bằng **runtime role thật**, thiếu context thì từ chối, không dùng owner/superuser/BYPASSRLS để chứng minh cách ly. FORCE RLS không thay thế GRANT, kiểm tra quyền API hoặc kiểm thử trường dữ liệu. PostgreSQL mô tả riêng ngoại lệ owner/BYPASSRLS và default deny; do đó SQL có câu CREATE POLICY không đủ đóng gate. [PostgreSQL 18 — Row Security Policies](https://www.postgresql.org/docs/18/ddl-rowsecurity.html), kiểm tra 29/10/2026; phiên bản DB sản phẩm vẫn phải được chốt bằng ADR.

Idempotency bền vững: một giao dịch ghi state + unique request/inbox/outbox; khóa theo tenant/operation/key; cùng key khác digest trả conflict; lease có hạn và fencing/revision; retry không tạo artifact/payment/notification trùng. Ghi nhận thất bại, retryable/terminal, attempt/deadline, DLQ, cancellation_requested và cleanup receipt. Demo Map chỉ chứng minh một process, không chứng minh điều này.

120 field hiện đều `required_by_default=false`; 90 PRIVATE, 30 RESTRICTED; 90 gắn cờ first_beta trong catalog. Cờ đó không cấp quyền thu thập. Cả 12 nhóm còn `retention_policy=...pending_review`: phải chốt thời hạn và đồ thị xóa/cache/object/log/backup trước dữ liệu thật. Các domain quan hệ/cơ thể/tài chính, trẻ em, ảnh và giọng cần scope riêng; không mặc định mở trong beta người lớn tự dùng.

State machine phải là một nguồn chung cho API/schema/DB/worker/UI. V2 narrative và RunStatus có `approved`, SQL run chưa có; demo run chuyển reviewing → completed, V3 bundle thêm partial/stale. Không tự gộp chúng bằng một enum tùy ý. Viết transition table gồm event, actor, precondition, side effect, terminal/retryable, timestamp, audit và cancel/revoke race; chỉ sau đó mới sinh enum và migration.

## 5. Quy tắc công thức và demo phải bàn giao

| Bộ tính | Quy tắc phải hiện trong trace | Demo/biên bắt buộc và giới hạn |
|---|---|---|
| Đuôi 80 | `N=80*q+r`; giữ đúng bốn chữ số; r=0 mặc định chưa ánh xạ, `as80` chỉ khi chọn rõ | `0000`, `0080`, `6789→69`; kiểm toàn miền 10.000 giá trị và 125 đuôi/mã khi as80. Bảng 80 không phải điểm người hay dự báo |
| 64 cặp Bát Cực | Cặp chồng lấn theo vị trí, 8 nhóm × 8 cặp; cặp có 0/5 giữ unresolved | Kiểm 64 cặp, 512 chuỗi ba chữ số, thứ tự và matrix 8×8; `876` phải DN→SK, `678` SK→DN và gắn cờ mâu thuẫn văn xuôi nguồn |
| Biến thể 0/5 | V2 `bridge5_diagnostic` xóa mọi 5 ở dãy đánh giá; V3 `bridge_single_0_5_diagnostic_v3` chỉ thêm cầu một số giữa hai số đã biết | `8553` ở V2 có thể thành 83; V3 giữ 55 unresolved. Không thay thế ngầm, không chung cache/release/config digest. Cường độ/rank/ratio chưa cấu hình giữ null |
| Tên Unicode/Latin | Giữ tên gốc; NFC và chuỗi Latin dẫn xuất tách riêng; Đ→D chỉ ở dẫn xuất; bảng A–Z chu kỳ 1–9 | NFC/NFD cùng phép tính nhưng raw trace khác; tên ngoài script hỗ trợ trả unavailable. Y unknown không chặn Expression nhưng để nguyên âm/phụ âm/bridge null |
| Numerology 23 | Lưu từng tổng trung gian, path/root, policy giữ 11/22/33 và `all_digits`/`reduced_components` | Cho ví dụ hai biến thể cùng root nhưng khác số ghép; given_name phải xác nhận riêng. Karmic markers không thành lỗi đạo đức, confidence không thành xác suất |
| Pinnacle/challenge/period | `B=36-root(LP)`; demo band đầu kết thúc sau tuổi nguyên B; challenge và period có policy độc lập | Kiểm B/B+1, B+9/B+10, B+18/B+19; band không hở/chồng. Period mặc định không có spans; không dùng pinnacle spans cho mọi chu kỳ |
| Psychomatrix | Raw counts khác four-working; `W1=sum(DOB digits)`, `W2=sum(W1)`, `W3=W1−2*first_nonzero_day_digit`, `W4=sum(W3)` | Giữ zero trong trace, 9 ô + 8 đường; `2008-11-02` có hai kết quả khác nhau; W3 âm không tự abs hay thêm hằng số sau năm 2000. Không đo trí nhớ/sức khỏe/thân mật |
| Lịch và giả thuyết | Ngày ISO, leap policy feb28/mar01; UTC candidates theo timezone/runtime version; không tự chọn giờ lặp | 29/02, năm nhuận thế kỷ, DST gap/fold Berlin/New York; giữ 2–5 hypothesis riêng, không lấy trung bình ngày sinh |
| Lifetime | 100 khoảng `[birthday,next_birthday)` cho điều hướng; history/self_report, plans/user_intention, cycles/symbolic là các danh sách riêng | Sự kiện đúng một khoảng; ngày lịch sử không sau as_of; dự định không biến thành lịch sử. Có dữ liệu sau tuổi 99 phải giữ history, thiết kế mở rộng/pagination thay vì làm mất dữ liệu |
| Quan sát và ma trận | Coverage mẫu số từ product registry; progress theo cửa sổ/việc hủy; tiền minor units bằng số nguyên; nhật ký là thống kê mô tả | Mẫu số 0 trả null; không cộng VND/USD; BigInt/string chống sai tiền; thiếu tiêu chí chặn xếp hạng. 144 câu hỏi không phải 144 phép đo năng lượng |
| Dịch sáu hào | Sáu bit từ dưới lên, hào động 1–6, XOR mask | 64×64 biến đổi và biến đổi ngược; binary index không phải thứ tự Văn Vương; văn bản quẻ có quyền và release riêng |

Các method ID NUM23/BCLC64/TAIL80… là ID thật trong register 62 dòng; cả 19 ID được dùng bởi 9 cấp đều phân giải được. Nhưng **62/62 chưa production_released**, chỉ 11 dòng tự gắn reference_implementation=true. Nhiều code phụ trợ chỉ đáp ứng một phần adapter. Ví dụ LINEAGE có DAG/digest demo, chưa có claim graph bền vững; REPORT có mẫu preview nhưng register vẫn chưa phát hành. Không đổi trạng thái nghiên cứu sang production chỉ vì có một hàm cùng chủ đề.

Giữ toàn bộ 32 dòng catalog V2: 16 phép tính tham chiếu và 16 specification chưa triển khai. Bát tự, Tử Vi, tiết khí/âm lịch, ephemeris, Jyotish/daśā, Nadi, Kỳ Môn, Lục Hào đầy đủ, tên ngoài Latin, ảnh/giọng, công cụ tâm lý và xác suất mục tiêu phải qua nguồn/edition/trường phái/quyền/golden cases riêng. Adapter không có đủ nguồn phải trả METHOD_NOT_RELEASED, scoped partial hoặc POLICY_BLOCKED theo loại; không có lời luận thay thế bằng phỏng đoán.

## 6. Nguồn, quyền sử dụng và nội dung

Mỗi lần phát hành phương pháp cần source edition/page/language, rule extraction có trace, license/rights receipt theo mục đích thương mại và bản dịch, đối chiếu ví dụ độc lập, người review và chữ ký release trên exact digest. `Sxx`, `Rxx`, `USER_TABLE80_CONVERSATION`, method ID và formula ID là các namespace khác nhau. Alias USER_TABLE80_CONVERSATION → R28 là một đề xuất đối chiếu nguồn, không phải chứng cứ bản quyền.

80 nhãn/nguyên văn được giữ nguyên trong source asset V3; lỗi chép nếu có cũng không sửa âm thầm. Tách trường nguyên văn, nhãn truyền thống, câu hỏi biên tập mới và cảnh báo. Hai mâu thuẫn nguồn Bát Cực `876`/`678` có sổ riêng. 64 câu hỏi chuyển nhóm là ORIGINAL_HNH_EDITORIAL_PROPOSAL, không ghi thành “công thức cổ truyền đã xác minh”. Bảng Psychomatrix 17 vị trí giữ nhãn nguồn để audit nhưng giao diện dùng ô/đường số, không biến “health/memory” thành chẩn đoán.

## 7. Gói công việc DEV, phụ thuộc và nghiệm thu

Ước lượng dưới đây là **người-ngày thực hiện sơ bộ**, dành cho team có quyền truy cập môi trường và nguồn đã chốt; không phải cam kết lịch giao hàng. BE lead phải ước lượng lại sau WP01 và spike DB/provider. Mỗi WP giao cả contract, code, fixtures, test receipt và hướng dẫn vận hành, cùng SHA ứng viên.

| WP / Owner / Ước lượng | Phụ thuộc | Đầu việc và artifact phải giao | Điều kiện nghiệm thu |
|---|---|---|---|
| **BE-WP01 Contract & state** — BE lead + FE lead + QA, 4–7 | Gate 0, hợp đồng hợp nhất | 99operation registry; typed request/response/error cho 81 blocker; schema examples/negative; action/resource/field matrix; Idempotency ADR; unified transition table; phân biệt auth redirects/no-body/binary | Không mất ID; không prefix trùng; 0 ref lỗi; 9 schema chuẩn bằng đúng bản đã duyệt hoặc có amendment rõ; không generic payload trên route phát hành; 16 V3 có permission/context cụ thể; SDK smoke tests |
| **BE-WP02 Source & registry** — Method Council + data steward + BE, 5–10 + review ngoài | WP01 | 62method crosswalk, 15passport, 32formula, 23component, 17position; SourceVersion/RightsReceipt/MethodRelease/ConfigRelease; source conflict và freeze/impact | Hash asset; source/rights không có thì method unavailable; đổi release tạo version mới; không suy approval; nội dung có claim_type/limitations và source-linked independent golden |
| **BE-WP03 Data & access** — DBA + security/BE, 6–10 | WP01, WP02 | ERD/tenant-subject composite FK; runtime roles/RLS; subject-purpose authorization; immutable ProfileVersion; migration/backfill/rollback; 120field collection/retention mapping | Negative cross-tenant/cross-subject/cross-purpose/field denial trên runtime role; missing context fail; stale revision conflict; rollback dry run; không owner-bypass test; revoke concurrent test |
| **BE-WP04 Queue & durable ledger** — BE platform, 5–9 | WP03 | Durable inbox/outbox/idempotency; lease/fencing/retry/deadline/DLQ; 1 nguồn state; webhook state verification; cancellation cleanup | Crash ở mọi ranh giới transaction; duplicate/reordered messages; same key different payload conflict; parallel consumer chỉ một side effect; revoked/deleted subject không publish/tải; recovery receipts |
| **BE-WP05 Pure engine foundation** — BE math/core + QA, 4–7 | WP01, WP02 | Canonical input/rule digest; units/rounding/null reason; named dependency IDs; DAG/toposort/impact; HMAC private cache scope; fixtures độc lập engine | Same input/config cùng output; reorder object keys ổn định, arrays giữ thứ tự; reject NaN/unsafe ints/surrogate; partial missing not guessed; cache đổi tenant/subject/purpose/revision không hit |
| **BE-WP06 Tên, ngày & ma trận** — BE method + bilingual reviewer, 5–9 | WP05 | Production adapters cho Unicode/birth/cycle/23component/Psychomatrix với explicit variants, input/result schema và trace UI; tzdb/runtime receipt | Các biên ở mục 5; no automatic Y/given name/script guess; correct time candidates; independent examples; MethodResult chuẩn; no probability hoặc trait từ số |
| **BE-WP07 Chuỗi, đuôi80 & Bát Cực** — BE method + source reviewer, 4–7 | WP02, WP05 | 80row/tableversion, pair64, transition64, repeat70; contexts; V2/V3 diagnostic policies giữ riêng; compare không mặc định recommend | 10.000tail,64pairs,512triples; source conflict flag đúng; strict pairs không bị diagnostic thay thế; 0/5run unresolved; suffix privacy; rights/release gate trước nội dung thật |
| **BE-WP08 Lifetime & quan sát** — BE product + QA, 4–7 | WP03, WP05, WP06 | 18domain/54scenario/9stage/144question IDs; history/intentions/cycles; events/plans canonical ID/version; coverage/progress/cashflow/resonance | No event duplication; >=100 tuổi không mất history; plan/history date guards; currency split; denominator0=null; deterministic rounding; grant từng người trong quan hệ; 54scenario vẫn không forecast |
| **BE-WP09 Bundle & incremental** — BE orchestration + QA, 4–7 | WP04, WP06–08 | Bundle snapshot, node eligibility, partial/blocked/stale; progress receipt; selective recompute; method freeze; worker auth recheck | Một node lỗi không giả cả bundle thành completed; cancel/revoke races; impact closure đúng; snapshot đúng source/config; 9level chỉ mở khi gates riêng đạt; không “đủ data” là đủ quyền |
| **BE-WP10 Claim, report, book** — BE reports + editorial + QA, 5–9 | WP09, WP02 | Fact/self_report/observation/symbolic/metric/model labels; local canonical Claim/ReportSnapshot adapters; review/publish/withdraw/version/diff/export; artifact signed access | Renderer chỉ đọc snapshot; không tính lại/AI bù nội dung khi đọc; claim provenance trace tới sourcefield/method; model_probability phải có đủ model evidence; thu hồi quyền làm tải thất bại; export có nội dung tương đương và không lộ subject khác |
| **BE-WP11 Research adapters** — Council + chuyên gia bản ngữ + BE | WP02, WP05, nguồn/quyền từng method | Từng passport riêng cho các phương pháp nghiên cứu còn lại; edition, school, language reviewer, formula spec, independent goldens và output boundaries | Mỗi method được phê duyệt độc lập; không chuyển đồng loạt family; chưa đủ đầu vào/nguồn thì unavailable; không tạo dữ liệu Nadi/ephemeris hoặc lời đoán giả |
| **BE-WP12 Integration, privacy & ops** — QA lead + SRE + security + product | WP03–10 | SDK cho mobile web/PWA/desktop web; E2E current SHA; rate/body/concurrency limits; observability redaction; deletion/restore drills; performance and release receipts | 99contract coverage theo scope phát hành; all required negative tests; no private payload logs; deletion graph+restore tombstones trước traffic; crash/retry/cancel; measured p50/p95 under stated hardware/data/concurrency; approval/legal/provider/staging/live mapping riêng |

Chuỗi ưu tiên: WP01 → WP02/WP03 → WP04/WP05 → WP06/WP07/WP08 → WP09 → WP10 → WP12. WP11 chạy thành lane nghiên cứu riêng, không ngăn beta có phạm vi hẹp đã được phê duyệt; không được dùng việc loại khỏi beta để xóa các yêu cầu nghiên cứu cũ.

WP là phân rã kỹ thuật bên trong backlog 316 đầu việc, không cộng thêm 12 lần vào ngân sách. Liên kết: WP01→INT29-010; WP02/WP11→INT29-005; WP03→INT29-011; WP04→INT29-012/017; WP05→INT29-006/012/013; WP06→INT29-006/007/008; WP07→INT29-008; WP08→INT29-009; WP09→INT29-010/012; WP10→INT29-014/016; WP12→INT29-015/018/020. `WORK_PACKAGE_BACKLOG_CROSSWALK.json` ghi cùng liên kết và quy tắc không cộng trùng.

## 8. Hợp đồng bàn giao cho mobile web, web app và desktop web

Một backend contract chung với SDK/type cùng schema/version. Giao diện chọn subject/profile/purpose đã được máy chủ kiểm tra, module được phép, policy và input còn thiếu; hiển thị tiến độ theo node, variant/source/limitations, kết quả tính và câu hỏi riêng. “Xem trace” phải đọc được từng bước trên màn hình nhỏ, bảng/matrix có bản danh sách tương đương, lỗi field map về đúng ô nhập. Không bắt người dùng đọc mã engine để hiểu kết quả.

Offline sync cần client-generated command ID, resource version, schema version, transaction group, replay receipt và conflict policy. Khi quyền đã thu hồi hoặc schema quá cũ, không silently overwrite; trả lỗi có thể xử lý. Deletion và logout phải xóa payload/cache cục bộ theo policy. Không lưu ảnh/giọng hoặc định danh thật vào synthetic lab.

Các response thống nhất cần request/correlation ID, status, resource/result version, pending/blocked/missing reasons, field errors và retry guidance; payload chỉ có trường được cấp quyền. Error message không tiết lộ sự tồn tại của người khác. Đây là yêu cầu thiết kế để WP01 chốt schema, chưa phải các field đã đồng loạt có ở 99route.

## 9. Kiểm thử đã có và bộ chứng cứ phải bổ sung

Lần chạy mới 29/10 dùng Node bundled, các **bản sao trong /private/tmp**, nguồn lab được kiểm tra không thay đổi. V2 **125/125**, V3 **192/192**, legacy V2 nằm trong V3 **125/125**. Dòng legacy là lặp lại suite cũ, không cộng thành 442 tính năng hay ca nghiệp vụ độc lập. Replay tạo 90 kết quả V2 và 167 kết quả hợp nhất; trường hợp expected_error là kiểm soát đúng, không phải API thành công giả.

Draft202012Validator với FormatChecker kiểm tra 27 standalone schema mới và 26 example được cung cấp: **26/26 example pass**, ReferenceResult không có supplied example. Điều này chỉ chứng minh các example mẫu thỏa schema; chưa chứng minh schema đã mô tả hết luật nghiệp vụ. Fresh contract/example/replay mismatch nếu có phải nằm trong receipt riêng, không sửa ngầm source để làm xanh.

Kiểm tra hợp đồng bổ sung: 68 component schema hợp lệ về cú pháp; 9 schema local và 27 standalone schema mới giữ nguyên object, kể cả `$schema`/`$id`/title vốn bị lược khỏi target nguồn. JSON/YAML OpenAPI V2 tương đương. Đối chiếu 72 ca của bảy dispatcher V3 với input schema và output ReferenceResult: 57 kết quả dương thỏa hợp đồng, 15 từ chối theo kỳ vọng; không có kết quả dương sai schema. Đây vẫn là bộ fixture tổng hợp của gói, không phải golden được một chuyên gia độc lập phê duyệt.

Không có bằng chứng mới cho DB/RLS runtime, queue durable, IdP/payment/AI/R2/provider, source license, scientific predictive validity, production load/SLA, mobile/device/browser visual hay triển khai live từ các suite trên. Các receipt cũ trong ZIP vẫn được giữ nhưng không thay lần chạy hiện tại.

WP12 phải bổ sung: unauthenticated/wrong tenant/subject/purpose/field; permission và entitlement revoked; hypothesis uncertain; stale version; duplicate/cross-tenant idempotency; outbox crash/retry/reorder; cancel/delete/freeze giữa run; report publish/download races; backup restore tombstone; large/deep/malformed input; DST/leap/variant boundaries; non-Latin/Y/source disagreement; zero denominator/currency/rounding; accessibility và responsive client E2E cùng exact backend candidate.

## 10. Biên bản nhận bàn giao DEV

BE lead và QA nhận các artifact trong mục 1, kiểm SHA nguồn và contract, gán người và dependency cho WP01–12, ghi scope từng release. Một WP chỉ hoàn tất khi có code ứng viên, schema/fixtures, kết quả kiểm tra, giới hạn còn mở và người review. Hoàn tất tài liệu hoặc chạy demo không đóng gate triển khai. Quyết định mở dữ liệu thật, seed/migration staging, provider, production và phát hành phải có scope/đích/candidate/approval tương ứng, nằm ngoài đợt hợp nhất kế hoạch này.
