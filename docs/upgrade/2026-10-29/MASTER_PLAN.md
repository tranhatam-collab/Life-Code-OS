# Life Code OS — Tổng kế hoạch hợp nhất chuẩn bị phát triển

Phiên bản 2026-10-29.r1. Chủ dự án: Trần Hà Tâm. Trạng thái: **kế hoạch đã hợp nhất trong local worktree; release HOLD**.

## 1. Kết quả hợp nhất và cách áp dụng

Bản này đưa V1, V2, V3 và phần bổ sung 20/10.r2 đang có trong dự án vào cùng một chương trình thực thi. Bảo toàn nội dung nguồn bằng SHA-256; giữ hợp đồng đã chi tiết hơn; ghi rõ phần thay thế, phần bổ sung và quyết định còn chờ. Bộ nguồn vẫn là tài liệu tham chiếu. Một hướng dẫn nhập gói, câu lệnh triển khai hoặc tuyên bố “đã kiểm thử” nằm trong đính kèm không tự trở thành quyền chạy trên dự án.

Đọc tổng kế hoạch này cùng ba sổ bàn giao: [backend](backend/BACKEND_DEV_HANDOFF.md), [sản phẩm và giao diện](product/PRODUCT_UX_REPORT_HANDOFF.md), [chương trình DEV](execution/PROGRAM_EXECUTION_PLAN.md). Hợp đồng máy đọc và ma trận nghiệm thu là phần của cùng phiên bản. Khi văn xuôi và schema khác nhau, lập conflict record và chặn phần phát hành bị ảnh hưởng cho tới khi có quyết định; không âm thầm chọn bản dễ triển khai hơn.

| Hạng mục | Phạm vi hợp nhất | Ý nghĩa hiện tại |
| --- | --- | --- |
| Nguồn đầu vào mới | V2: 307 tệp; V3: 520 tệp | 827 mục nguồn được lưu riêng, có phần lặp được bảo toàn |
| Kế hoạch cũ trong dự án | 216 tệp ngày 20/10.r2 | Giữ nguyên byte, gồm 16 đầu việc UPG mà V3 chưa có |
| Backlog | 296 đầu việc nguồn + 20 phần phân rã tích hợp | 316 bản ghi kế hoạch; chưa chứng minh hoàn thành DEV |
| Quyết định | Q1–Q45 | Giữ 20 packet chi tiết cũ; bổ sung 25 packet; chưa tự duyệt |
| Tri thức | 20 họ, 62 adapter, 12 lớp, 12 trường đồng nhịp | Có vị trí, đầu vào, nguồn và cổng riêng; 0 adapter được chứng minh đã phát hành production |
| Sản phẩm | 28 sản phẩm; chín cấp báo cáo | Quyền sản phẩm độc lập; phạm vi triển khai chia đợt |
| Giao diện | 69 màn hình | 45 hợp đồng cũ + 12 V2 + 12 V3; route đích chưa là route đã triển khai |
| API | 99 thao tác đích | Giữ 64 thao tác local và chín schema chuẩn mạnh; bổ sung 35 thao tác |
| Trace | 407 dòng | 87 yêu cầu local + 62 yêu cầu V3 + 28 sản phẩm + 69 màn hình + 62 adapter + 99 API |

Không dùng số lượng tệp, task, API hoặc trang để suy ra tỷ lệ sẵn sàng. Mỗi yêu cầu phải đi qua nguồn → đặc tả → candidate code → kiểm thử → artifact → môi trường → vận hành → phê duyệt theo đúng phạm vi.

## 2. Bản sắc, giá trị và giới hạn sản phẩm

Huyền Nhân Học là triết lý và ngữ pháp tổng hợp do Founder định hướng. Life Code OS là nền tảng dữ liệu, phần mềm, báo cáo và hành động. Life Resonance quan sát quan hệ người–môi trường. Life Design giúp chọn một bước làm, theo dõi và xem lại. AI hỗ trợ truy xuất, giải thích và biên tập theo quyền được cấp.

Một Code cá nhân gồm dữ liệu được phép, giả thuyết, kết quả từng phương pháp, nguồn, quan sát, hoàn cảnh, mục tiêu và hành động. Không rút một con người thành một căn số hoặc một điểm định mệnh. Phép tính theo quy ước, lời diễn giải biểu tượng, quan sát thực tế, tự thuật và dự báo có mô hình là các loại nhận định riêng. Không đếm các chỉ số chung ngày sinh như nhiều nguồn chứng minh độc lập.

Giá trị cần thử trong pilot: người dùng hiểu dữ liệu nào đã dùng, sửa được dữ liệu sai, nhận ra phần chưa biết, chọn được hành động vừa sức và thực hiện quyền dữ liệu. Phản hồi “cảm thấy đúng” được ghi như trải nghiệm tự thuật. Nó không xác nhận độ chính xác dự báo, công dụng y tế hoặc hiệu quả tài chính.

Phạm vi sản phẩm đầu tiên là người trưởng thành tự tạo hồ sơ, tự chọn mục đích, nhận Level 1, công cụ Numbers có phương pháp đã duyệt và kế hoạch 30 ngày. Trẻ em, ảnh, người thứ ba, sức khỏe, tổ chức và lãnh thổ mới được giữ trong tổng kế hoạch với cổng riêng. Chưa mở tất cả cùng lúc.

## 3. Nguồn, phiên bản và quyền sử dụng

Nguồn nguyên bản đặt tại `docs/upgrade/sources/2026-10-29/`; hai ZIP, hai lời bàn giao, 827 mục đã giải nén và các bản trích xuất được tách rõ. V3 bảo toàn đủ 307 mục V2, gồm ba tệp rời ngoài thư mục lõi. V2 bảo toàn 149 tệp V1. Manifest V2 có 303 mục cho 304 tệp lõi; V3 có 519 mục cho 520 tệp. Manifest tự loại chính nó nên các số này phù hợp phạm vi.

Mỗi nguồn tri thức cần ID, tác giả/chủ quyền, edition, ngôn ngữ, trang/đoạn, ngày truy cập, hash, phạm vi toàn văn đã đọc, quy tắc trích được, quyền triển khai/biên dịch/diễn giải, hạn chế và người rà soát. Một URL, đoạn tìm kiếm hoặc ghi chú tên sách chưa đủ cho một method release. Nội dung từ cộng đồng/thực hành trường phái không tự là bằng chứng thực nghiệm.

Giữ riêng bảng Founder cung cấp, nội dung HNH tự biên soạn và biểu đạt/bản dịch có quyền. Kho nghiên cứu chưa có quyền phát hành không được đưa vào RAG thương mại hoặc gói tải của khách. Nadi, sách nâng cao chưa có toàn văn, rank cường độ và các trường phái chưa khóa quy tắc tiếp tục là research backlog. Chỉ mở khi có nguồn, quyền, golden cases và người duyệt đúng chuyên môn.

## 4. Danh mục sản phẩm và chín cấp

28 bản ghi gồm 23 sản phẩm cũ và năm dòng mới: `LC-NUM-ATLAS`, `LC-LIFE-MAP`, `LC-LEGACY`, `LC-REGION-KIT`, `LC-RESEARCH-STUDIO`. Dùng một hệ tài khoản, kết quả, thanh toán và entitlement; không xây 28 ứng dụng độc lập. Mỗi hợp đồng sản phẩm ghi đối tượng, nhu cầu, đầu vào tối thiểu/tùy chọn, đầu ra, quyền, phương pháp được phát hành, giới hạn, luồng lỗi, hỗ trợ, giá chờ duyệt và bằng chứng nghiệm thu.

| Cấp | Sản phẩm | Dữ liệu và tiêu chí riêng |
| --- | --- | --- |
| 1 | Self Signal | Tên/ngày sinh theo phương pháp, mục tiêu; 14 mục nguồn–độ đầy đủ–kết quả–hành động; LCI chưa định nghĩa để null |
| 2 | Inner Architecture | Giá trị, vai trò, nhu cầu và tình huống tự thuật; không suy toàn bộ nội tâm từ ngày sinh |
| 3 | Behavior Code | Nhật ký và instrument có nguồn; phân biệt quan sát với suy ngẫm |
| 4 | Work & Wealth Code | Kỹ năng, vai trò, nguồn lực, tiền có đơn vị; không biến biểu tượng thành lời hứa thu nhập |
| 5 | Relationship Field | Mỗi chủ thể có quyền riêng, purpose và thu hồi; không cho người mua đọc toàn bộ người còn lại |
| 6 | Life Timeline | Lịch sử, chu kỳ biểu tượng, dự định và dự báo có mô hình được tách |
| 7 | Body Intelligence | Quan sát và tự chăm sóc có quyền; không suy trí tuệ, đạo đức, bệnh hoặc thu nhập từ hình thái |
| 8 | Mission Path | Giá trị, năng lực có minh chứng và hướng lựa chọn; không áp đặt sứ mệnh |
| 9 | Full Life Code | Hợp nhất phần được phép, chống lặp và xung đột; không nối tám tệp thành một cuốn sách dày |

Không bắt mua tuần tự. Body Intelligence không là điều kiện phải mua trước Mission Path. Mở báo cáo theo entitlement + chủ thể + mục đích + quyền + method release + dữ liệu cần thiết. Độ dài 30–600 trang trong nguồn là ngân sách tham khảo theo cấp, không phải hạn ngạch phải tạo đủ bằng nội dung lặp.

Free Essentials, báo cáo một lần, Companion, Practice, Academy, Family, Workspace, Publishing và API giữ phạm vi cũ. Quyền sửa, xuất hoặc yêu cầu xóa dữ liệu không đặt sau paywall. Người trả tiền cho tổ chức không tự đọc nhật ký hoặc dữ liệu sức khỏe của thành viên.

## 5. Mô hình đời sống và dữ liệu đầu vào

Giữ 120 trường tùy chọn, 12 lớp và 12 trường đồng nhịp. Chỉ thu dữ liệu cần cho nhu cầu người dùng đã chọn. Mỗi trường có mục đích, độ chính xác, nguồn tự khai/quan sát, đơn vị, quyền xem, thời hạn và trạng thái thiếu. Tên gốc, NFC, tên chuyển tự được xác nhận, tên thường dùng và given_name là các phiên bản liên kết; không bỏ dấu hoặc chọn token đầu tên Việt một cách ngầm định.

18 lĩnh vực gồm bản sắc; học tập; công việc; nguồn lực/tài chính; quan hệ; gia đình; nhà ở; cộng đồng; cơ thể/tự chăm sóc; nhịp sống; ý nghĩa; sáng tạo; di chuyển; chăm sóc/người phụ thuộc; lớn tuổi; di sản/chuyển giao; biến chuyển/mất mát; đời sống số. 54 kịch bản là lời gợi ý nhập liệu hoặc hành động. Một sự kiện liên quan nhiều lĩnh vực vẫn có một nguồn gốc, liên kết nhiều nơi mà không nhân bản bằng chứng.

Chín giai đoạn chỉ điều hướng biên tập. Không ép mọi người kết hôn, sinh con, nghỉ hưu hoặc đi theo một tuyến thành công. Khoảng tuổi dùng `[sinh nhật a, sinh nhật a+1)`. Mốc 0–99 là 100 khoảng điều hướng, không là giới hạn tuổi thọ; tuổi 100+ và sự kiện sau 99 cần giữ nguyên. Ngày 29/02 phải chọn `feb28` hoặc `mar01` và lưu vào kết quả.

Ngày sinh giấy tờ khác thực tế tạo các hypothesis ID độc lập. Giờ sinh thiếu không tự điền 12:00. Chỉ biết năm hoặc tháng phải giữ precision và khoảng ứng viên; không điền 01/01 hoặc ngày đầu tháng. Lab V3 nhận ngày đầy đủ chỉ là một phạm vi nhỏ, không được làm mất hợp đồng ngày chưa chính xác của V1. DST gap/fold trả danh sách ứng viên hoặc lý do không có. Lưu tzdb/ICU, lịch, tọa độ, timescale, sai số và boundary policy. Đổi giả thuyết chỉ tính lại các nút phụ thuộc, không sửa lịch sử tự thuật.

Giữ 144 câu hỏi đồng nhịp tùy chọn; Resonance không tạo thêm “lớp thứ13”. Quan sát và thử một thay đổi trong bảy ngày là lựa chọn có sự đồng ý, không chứng minh quan hệ nhân quả. Life Design giữ tối đa ba hành động ưu tiên trong một chu kỳ, kèm tiêu chí xem lại. Sự kiện được nhập sau khi đọc báo cáo phải ghi `observed_after_report`, không dùng hồi tưởng đó làm xác nhận dự báo trước.

## 6. Hợp đồng công thức, ma trận và phương pháp

62 adapter thuộc K01–K20 được phân rã trong `backend/FORMULA_METHOD_EXECUTION_MATRIX.json`. Giữ crosswalk tới passport M01–M15 và formula LCF theo phạm vi, không giả rằng các namespace là ánh xạ một-một. Cờ source `reference_implementation=true` của 11 adapter chưa chứng minh toàn bộ phạm vi adapter có mã hoàn chỉnh; receipt phải ghi entrypoint và phần thực sự đã chạy.

Mỗi method release chốt input schema, normalization, source edition/digest, ruleset, variant, hằng số, đơn vị, precision, output schema, missing-data policy, claim types, forbidden claims, phụ thuộc, tính tất định, kiểm thử và quyền sử dụng. Không chạy JavaScript do biên tập viên đưa vào bảng quy tắc. Không lấy nội dung tài liệu hoặc prompt làm lệnh thay quyền.

Các nhóm cần nguồn chuyên biệt: lịch/24 tiết khí/âm dương; Bát tự; Tử vi; Dịch; Kỳ Môn/Lục Nhâm/Thái Ất; không gian/Vastu; Jyotish/Nadi; thiên thể/hệ nhà; lịch vùng; số–tên; Bát Cực/đuôi 80; danh học; hình thái; Tarot/Rune/Ifá; Human Design/Gene Keys; HNH/nội tâm; tâm lý đo lường; hành vi/nguồn lực/quan hệ; sinh hoạt; nguồn/AI/kỹ thuật. Mỗi họ có điều kiện mở, không tạo lá số giả khi chưa có ephemeris hoặc quy ước.

## 7. Bộ số–tên 23 thành phần

Giữ NUM-01…NUM-23: Life Path; Birthday; dấu số 13/14/16/19 trong trace; Expression đầy đủ/thường dùng; Heart đầy đủ/thường dùng; số ghép và reduction path; Personality đầy đủ/thường dùng; Maturity; Rational Thought theo given_name xác nhận; nhóm số vắng; tổng chữ đầu; nhóm lặp nhiều nhất; số nhóm có mặt; bốn Challenges; phạm vi Challenges; bốn Pinnacles; phạm vi tuổi Pinnacles; ba Period Cycles; cầu LP–Expression; cầu Heart–Personality.

Life Path có thể cộng trực tiếp hoặc rút gọn tháng/ngày/năm theo policy. Giữ tổng trung gian và từng bước, kể cả hai tổng khác nhau cùng root. Master-number policy và quy tắc reduction phải có release ID. Y chưa xác nhận làm các đầu ra phụ thuộc nguyên/phụ âm để null, kèm lý do; tổng tên có thể còn hợp lệ. Không lấy quy ước phát âm tiếng Anh làm mặc định cho tên Việt.

Hidden Passion giữ mọi đồng hạng. Challenge dùng các hiệu tuyệt đối; Pinnacles dùng bốn tổng đã khai báo. Các chu kỳ có công thức và boundary policy riêng; không sao chép bảng tuổi giữa các nhánh. Tên truyền thống như Rational Thought hay Subconscious Confidence là tên phép quy đổi, không là đo trí tuệ hoặc xác suất tự tin. Test gồm tên có dấu, NFC/NFD, Đ/đ, tên nhiều token, Y, thiếu given_name, ngày nhuận, master numbers, ties, biên giai đoạn và hai biến thể cho kết quả khác nhau.

## 8. Bát Cực, đuôi 80 và Psychomatrix

Bát Cực giữ tám nhóm, 64 cặp, vị trí, cặp chồng lấn, cửa sổ ba chữ số, số lặp và phần chưa phân loại. Với chuỗi dài n phải có n−1 cặp và n−2 cửa sổ khi n đủ lớn. 64 ô chuyển nhóm 8×8 là câu hỏi HNH mới biên soạn; không gọi là toàn bộ 512 chuỗi ba chữ số từ tập tám chữ số.

Ba chế độ tách version: `strict` giữ nguyên 0/5 và báo unresolved; `diagnostic` chỉ thêm single bridge A0B/A5B đủ điều kiện, giữ cặp gốc; `full_traditional_context` chờ nguồn. V2 có biến thể bỏ toàn bộ 0/5; giữ nó trong lịch sử và golden conflict case, không cho ghi đè diagnostic V3. `8553` không tự rút thành `83`. Rank chưa có căn cứ không chuyển thành trọng số. So sánh nhiều SIM giữ cấu trúc, giá và tình trạng tự nhập riêng; không mặc định tạo điểm hợp người hoặc khuyến nghị mua.

Đuôi 80 nhận đúng bốn chữ số. Dùng integer `divmod(N,80)`, dư 0–79; bảng gốc 1–80 yêu cầu `unmapped` hoặc `as80`. Không dùng `r+1`. Giữ đủ 80 lời nguồn, nhãn nội dung biên tập riêng, đánh dấu câu gốc chưa rõ ở 34/55. Test toàn miền 0000–9999, leading zero, tính chất N+80, input không hợp lệ và policy dư 0. Kết quả không có dữ liệu ngày sinh nên không tạo độ hợp cá nhân.

Psychomatrix tách đếm chữ số gốc và quy tắc bốn số phụ. W1=tổng chữ số ngày sinh; W2=tổng chữ số W1; W3=W1−2×chữ số đầu ngày không đệm 0; W4=tổng chữ số W3. W3 âm trả unsupported cho variant này. Giữ chín ô, tám đường, nguồn và policy. Thiếu 9 không suy trí nhớ; thiếu 4 không suy sức khỏe; trục 3–5–7 không tạo nhận định đời sống thân mật.

## 9. Kiến trúc đích và đối chiếu repository thực

Khởi đầu bằng modular monolith: gateway/BFF; identity/subject/grant/purpose; profile/hypothesis; knowledge/method; observation/resonance; claim/report/action; commerce; practitioner/Academy/territory; audit/deletion. PostgreSQL nghiệp vụ, private object storage, queue + transactional outbox và renderer cô lập là thiết kế đích. Nhà cung cấp và chi phí chờ quyết định; không coi bản thiết kế là hạ tầng đã mua.

Repository hiện có static HTML/JS và Worker tại `workers/life-code-api/src/`, engine tại `engine/core/`, migrations SQL và các script kiểm thử. Đây là điểm xuất phát phải audit trên candidate cụ thể. Astro/React/Vite hoặc các thư mục mới `apps/web`, `packages/method-core`, `services/report-renderer` là phương án tổ chức đích; chưa tồn tại không được trình bày như code đã có. Không đổi framework hàng loạt trước khi lập parity matrix và kế hoạch di chuyển URL.

Mô hình SQL V1 gồm41 bảng và entity registry toàn miền vẫn là nguồn thiết kế phải đối chiếu. Chín bảng transaction core của V2 và chín bảng extension của V3 là phần bổ sung theo phạm vi; không thay thế toàn bộ41 bảng. DEV lập entity crosswalk, composite FK, quyền, migration order và reconciliation cho cả mô hình, không chỉ cho lab.

Source lock lần hợp nhất: root Life-Code-OS, origin `git@github.com:tranhatam-collab/Life-Code-OS.git`, branch `codex/complete-upgrade-plan-2026-10-20`, HEAD `336ef35a8386a744c6de18a7f7c6e268e89e6dac`. Worktree có thay đổi app/workflow/migration từ lane khác; kế hoạch không sửa các tệp đó. HEAD, worktree, CI, deployment và runtime là các lớp bằng chứng riêng.

## 10. API và schema cần đóng trước code generation

`backend/OPENAPI_UNIFIED_TARGET.json` hợp nhất 99 operation: giữ nguyên business contracts của 64 operation local; bổ sung 19 V2 và 16 V3. Chín schema chuẩn local được giữ nguyên object để tránh mất các ràng buộc metric/claim. 16 đường V3 đã bỏ phần prefix bị lặp khi ghép với server `/api/v2`; nguyên bản vẫn có provenance. Ba khóa policy `x-required-permission`, `x-permission`, `x-required-policy` được nối vào authorization registry, không suy “không có auth” chỉ vì tên khóa khác.

Còn **81/99 operation có blocker cho typed code generation**: 65 generic success (46 local +19 V2), 10 V3 thiếu success schema cụ thể và sáu V3 dùng ReferenceResult chỉ dành tham chiếu. 16 operation V3 chưa chốt action/resource permission nên phải đóng mặc định. Đây là công việc INT29-010, không được đánh dấu đã hoàn tất vì file OpenAPI parse thành công.

Mỗi operation cần schema request/response/error đóng, principal/tenant/subject/purpose, permission action/resource, field filtering, pagination, concurrency/ETag, idempotency, rate limit, audit, timeout, cancellation và negative cases. Giải quyết khác biệt độ dài idempotency key giữa các nguồn bằng quyết định version; không nới validation ngầm. JSON Schema và SQL enum phải cùng version. Demo envelope cần adapter sang canonical Claim/Metric trước khi dùng trong app.

## 11. Identity, quyền và dữ liệu riêng tư

Account, profile_subject và tenant tách rõ. Principal lấy từ session đã xác thực; client `user_id` chỉ là dữ liệu, không tạo quyền. Object lookup phải khóa quyền tại query, kiểm grant/purpose và chống quan hệ con trỏ sang tenant/subject khác. Kiểm quyền khi tạo run, worker nhận việc, phát hành và tải. Thu hồi grant phải chặn tác vụ đang chờ và link tải mới.

RLS là lớp bổ sung, runtime role không là chủ bảng hoặc BYPASSRLS. Thiết kế SQL mới chỉ là bản thiết kế có ROLLBACK, chưa là migration đã áp dụng. Cần rehearsal bằng role thực, cross-tenant tests, composite foreign keys, deny-by-default và scope GRANT cụ thể. Không chạy file SQL nguồn trong lần hợp nhất kế hoạch.

Với connection pool, đặt tenant/subject/purpose context trong từng transaction và xóa đúng vòng đời; không giữ user context cấp session hoặc dùng personalized query cache chung. SQL V1 kết thúc bằng COMMIT, khác với bản thiết kế V2/V3; tất cả vẫn chỉ là nguồn để review, không có file SQL nào được thực thi trong lần này.

Dữ liệu có mục đích, retention và cơ chế sửa/xuất/rút/xóa xuyên DB, object store, cache, index, provider và backup. Deletion barrier chặn run/publication mới; restore áp lại tombstone trước mở truy cập. Không hứa thu hồi vật lý bản người nhận đã tải. Dữ liệu nghiên cứu/huấn luyện tách mục đích dịch vụ. Audit tránh token, prompt đầy đủ, tên/ngày sinh hoặc URL tải riêng tư.

## 12. Jobs, tính lại, hiệu năng và phục hồi

Tạo run, idempotency receipt và outbox trong cùng transaction. Queue có thể giao lặp; business effect phải deduplicate. Cùng key/cùng payload trả receipt cũ; khác payload trả conflict. Worker có lease/heartbeat, bounded retry/backoff, DLQ, cancel checkpoints và công cụ reconciliation. Không dựng sách dài trong một HTTP request vô hạn. Thiết kế này phù hợp [delivery guarantee của Cloudflare Queues](https://developers.cloudflare.com/queues/reference/delivery-guarantees/); vẫn cần thử trong môi trường chọn thật.

Cache key gồm tenant, subject, purpose, access revision, input digest, method/source release và locale. Hash không tự ẩn danh dữ liệu dễ đoán. Tính lại theo DAG phụ thuộc; thay bảng tên chỉ invalidates nhánh tên. Snapshot đã xuất bất biến; tạo bản mới với diff. Không lấy cache chung theo DOB để trả kết quả riêng của người khác.

Benchmark phân lớp: tính nhanh; tổng hợp nhiều method; truy xuất; AI; export. Chốt dataset, concurrency, p50/p95/p99, CPU/memory, giới hạn và ngân sách sau spike; chưa điền SLA công khai bằng thời gian máy local. Định nghĩa RPO/RTO và restore drill trước paid beta. Tính tiền bằng minor units + currency, không cộng chéo tiền tệ khi thiếu tỷ giá đã duyệt.

## 13. Mobile web, desktop web và native

69 màn hình có route đích, operation ID hoặc lý do không có API, trạng thái, quyền, viewport, a11y và evidence. Dùng cùng kết quả máy chủ. Mobile ưu tiên mục tiêu, thẻ từng nhóm số, bảng có tiêu đề và phần “xem cách tính”. Desktop hỗ trợ thanh điều hướng, so sánh nhiều chuỗi và workspace. Người dùng đọc giải thích, không buộc đọc JSON.

Mọi luồng xử lý loading, empty, partial, unsupported policy, method chưa phát hành, forbidden, stale, offline, lỗi, retry và thành công có receipt. Không hiện “đã lưu/đã trả tiền/đã xóa” khi chỉ có trạng thái client. 320/360/390/768/1280/1440px, bàn phím, screen reader, zoom 400%, focus/error/contrast/reduced motion được đưa vào QA. Mục tiêu WCAG2.2AA theo [W3C](https://www.w3.org/TR/WCAG22/); screenshot responsive không thay chứng nhận khả năng truy cập.

PWA chỉ cache public assets đã duyệt theo mặc định. Dữ liệu riêng tư, background sync và offline draft cần chính sách conflict/revocation. Logout, đổi account/subject/tenant, thu hồi grant và xóa phải dọn dữ liệu view/cache. Native iOS/Android hoặc app desktop là đợt riêng khi offline/camera/notification tạo giá trị rõ; chưa được trình bày là sản phẩm đã làm.

## 14. AI và nhà máy báo cáo

Quy trình: intake → snapshot → deterministic methods → claim registry → ACL-filtered retrieval → writer → reviewer → structured content tree → web/PDF/DOCX → publication receipt. LLM không tạo số tính toán hoặc sự kiện người dùng chưa cung cấp. Reviewer đối chiếu claim IDs, source chunks và mức khẳng định. RAG tài liệu không được thay quyền hay gọi tool ngoài phạm vi.

Giữ chín report contract local giàu chi tiết, bổ sung method routes và 18 life domains từ V3. Level 1 có đủ 14 section; section chưa có dữ liệu hiển thị lý do và null. Level 9 chống trùng nguồn, trùng chủ đề, mâu thuẫn và thông tin không có quyền. Content tree có section IDs, claim refs, loại nội dung chung/cá nhân hóa/bài tập, câu hỏi, hành động và giới hạn. Web/PDF/Word dựng cùng nội dung.

Render sandbox không tự đọc filesystem hoặc tải URL từ nội dung khách. Tệp private, link ngắn hạn hoặc kiểm quyền lại. QA kiểm TOC/bookmark/page count/font/table/citation/dedup/cross-reference/PII. Sách dài chỉ phát hành sau review toàn cuốn. Living Book có phiên bản bất biến và diff, không âm thầm đổi cuốn đã ký.

Tự chủ A0 đề xuất; A1 đọc đúng quyền; A2 việc đảo được trong hạn mức; A3 playbook vận hành đã duyệt có kill switch. Không tự cấp quyền dữ liệu, phát hành method, đổi provider xử lý rộng hơn, thu tiền ngoài chính sách, ký nhượng quyền hoặc deploy. Token/cost/retry/model/time limits chốt theo task; hết ngân sách trả phần tính đã có hoặc ngoại lệ chờ xem lại.

Các nhãn A0–A3 đã đổi nghĩa giữa policy V1 và V3: V1 dùng A1 cho phép tính đảo được, A2 cho nghiệp vụ đã cho phép, A3 cho việc nhạy cảm cần người duyệt; V3 dùng phạm vi nêu ở đoạn trên. Giữ cả hai bản với `policy_version` và danh sách capability cụ thể. Adapter chuyển đổi phải kiểm từng hành động, mức tác động và receipt; không tăng quyền chỉ vì cùng mang nhãn A1/A2/A3. Phần giao nhau chưa rõ phải đóng mặc định cho tới khi quyết định Q44 được chốt.

## 15. Thương mại và mô hình chi phí

Order, payment, entitlement, job và report là các thực thể riêng. Redirect thành công không cấp quyền. Webhook kiểm chữ ký, order, amount, currency và state machine; replay/retry không thu lặp/cấp lặp/gửi lặp. Refund/chargeback và reconciliation phải thu hồi đúng quyền theo chính sách, giữ audit. Nhà cung cấp, pháp nhân, chính sách giá/thuế/hoàn tiền chưa được suy ra từ bản demo.

Giá gắn phạm vi, cập nhật, định dạng, số lần sửa, reviewer và dịch vụ thực tế. Không bán độ chắc chắn số phận hoặc nhãn “sứ mệnh đặc biệt”. Free có hạn mức công khai; không lấy dữ liệu riêng tư bù chi phí quảng cáo ngầm. Support phân loại lỗi dữ liệu, công thức, nội dung, quyền và thanh toán; lỗi method release cần tìm mọi report bị ảnh hưởng.

Chi phí gồm nhân sự, AI, compute, storage, editor, support, payment, thuế và contingency. V1 task cha, 68 phần V2, 72 phần V3, 16 UPG và 20 INT có chồng phạm vi. Chưa cộng thành tổng ngân sách. V3 còn thiếu estimate; người và capacity thật chưa được phân công. Workbook để trống đơn giá/tiền tệ/khối lượng chưa chốt; số 0 chỉ hợp lệ khi có căn cứ. Lịch 10 ngày đầu là trình tự có điều kiện, không ngày giao hàng đã cam kết.

## 16. Academy, chuyên gia và lãnh thổ

Giữ chín buổi × 120 phút: dữ liệu/giới hạn; số–tên; Bát Cực/đuôi 80; lịch/chu kỳ; ma trận; đồng nhịp; đối thoại/ranh giới; hành động; ca thực hành/QA. Mỗi buổi cần learning outcomes, nguồn, bài tập, rubric, case thiếu dữ liệu và giới hạn. Chứng nhận nội bộ ghi scope, thời hạn, gia hạn, khiếu nại; không tự là giấy phép chữa bệnh hoặc bằng cấp ngoài thẩm quyền.

Bốn mô hình đối tác: giới thiệu; chuyên gia có scope; tổ chức được cấp phép; lãnh thổ/nhượng quyền. Mỗi mô hình có thương hiệu, quyền sửa nội dung, dữ liệu, phí, audit, hỗ trợ, chấm dứt và đường quyền dữ liệu cho khách. VN, EU/EEA, US, AU, SG được giữ; CA, UK là checklist nghiên cứu bổ sung. Ngôn ngữ không đồng nghĩa nơi cư trú, thị trường hay vùng lưu trữ. Có AI đa ngôn ngữ không thay biên tập viên và người rà soát địa phương.

Metadata văn bản Việt Nam đã được kiểm lại ngày 29/10: [91/2025/QH15](https://chinhphu.vn/?classid=1&docid=214590&orggroupid=1&pageid=27160) hiệu lực 01/01/2026; [134/2025/QH15](https://chinhphu.vn/?classid=1&docid=216334&orggroupid=1&pageid=27160) hiệu lực 01/03/2026; [122/2025/QH15](https://chinhphu.vn/?classid=1&docid=216503&pageid=27160&typegroupid=3) hiệu lực 01/07/2026. Đây là đối chiếu metadata, chưa là legal opinion cho hoạt động cụ thể. Packet pháp lý cần map từng feature/dataflow/territory tới nghĩa vụ và reviewer.

## 17. Chuyển đổi hệ hiện có và P0

Các vấn đề P0 trong audit cũ là lịch sử cần tái kiểm trên exact candidate: quyền tin ID client, object ownership, session/token, điểm hardcode, timeline lượng giác, coverage denominator. Worktree hiện có sửa đổi từ lane khác nên không kết luận lỗi cũ còn nguyên hoặc đã sửa chỉ từ tài liệu. INT29-002 nhận baseline, diff và receipt để triage lại; không gọi hồ sơ người thật để chứng minh.

Giữ thứ tự containment/Gate0 đã chuẩn hóa của P0 local ở sáu dependency khác incoming. Lưu cạnh nguồn cũ để đối chiếu. Chặn bề mặt thiếu quyền, kế hoạch vô hiệu phiên cũ, kiểm owner mapping, quarantine unknown legacy, rehearsal migration, đối soát counts/digest và restore. Output AI legacy không chuyển thành self_report chỉ vì nằm trong hồ sơ. Rollback chỉ về target an toàn; chưa có thì giữ scope giới thiệu/bảo trì.

Giữ raw/normalized/adjusted LCI cũ ở `experimental_legacy`; không dùng để mở quyền, định giá, xếp hạng hoặc phân loại rủi ro. Migration có ledger từng bản ghi; trùng tên/ngày sinh không đủ để merge. Chủ sở hữu hoặc mục đích chưa xác định phải quarantine, không ép tỷ lệ di chuyển100%. Các hàm policy/in-memory ledger tham chiếu V1 chưa thay thế registry, RLS và outbox đã harden ở hợp đồng mới.

Tài liệu/ZIP/SQL/demo/receipt nội bộ không thuộc bundle public. Build cần allowlist và kiểm artifact thực; việc lưu nguồn trong repo không cho phép website publish toàn bộ. Kiểm đường prepare-pages/deploy riêng trước bất kỳ phát hành nào.

## 18. Chương trình DEV, phụ thuộc và nhận việc

`execution/BACKLOG_UNIFIED.json` giữ raw record + source path/hash cho từng task. `TASK_DEPENDENCY_GRAPH.json` tách task, decision và gate; đồ thị task không có vòng/đầu mối thiếu. Q và G không được xem là task đã xong. Parent-child và work-order refinement không cộng lặp effort. `TASK_DEV_CONTRACTS.json` có 316 contract, kế thừa 156 contract local và gắn chi tiết method/work-order cho phần mới.

20 INT bao phủ: nhập nguồn; authority; graph/effort; 45 quyết định; 62 method/rights; input/time/name; 23 số–tên; Bát Cực/đuôi 80/Psychomatrix; life map; 99 API/schema; identity/privacy; jobs/cache; 167 demo; chín report; 69 screen contract; AI; commerce; staging/restore; Academy/territory; trace/pilot. Đây là phần phân rã tích hợp của task nguồn. Chi tiết scope, vai trò, acceptance, negative tests, rollback và estimate nằm trong từng work order.

Trình tự thực thi: (A) khóa source/candidate và scope an toàn; (B) chốt các quyết định nền, identity/schema/method input; (C) dựng một vertical slice người trưởng thành tự hồ sơ với dữ liệu giả; (D) tích hợp Trust Core và method đã duyệt; (E) Level 1/Numbers/action 30 ngày trên staging; (F) paid private beta sau đóng cổng liên quan; (G) mở rộng theo module và lãnh thổ. Nguồn và thiết kế độc lập có thể làm song song; không buộc xong toàn bộ 62 adapter trước slice đầu.

Mỗi người nhận việc xác nhận task ID, role/named assignee, clean candidate SHA/diff, file allowlist, decision/gate áp dụng, fixtures, lệnh kiểm thử, reviewer, receipt path và rollback. Một task chỉ DONE khi scope receipt đủ và reviewer độc lập chấp nhận. Thay đổi kế hoạch có version; artifact tổng hợp không ghi người thật hoặc phê duyệt giả vào ô trống.

## 19. QA, demo và cổng phát hành

167 case V3 gồm 90 case V2; không cộng thành 257 case độc lập. 64 fixture local r2 được giữ để regression/crosswalk, không ghép IDs không namespace. Phân loại unit/property, input/output schema, HTTP local, deterministic demo, mocked browser fixture, real browser, staging integration, security, migration/restore và load. Không lấy một loại pass để suy loại khác.

Lần này chạy lại V2 125/125, V3 192/192; bản legacy V2 nằm trong V3 cũng 125/125 nhưng là lớp lặp. Replay 90 và 167 case được ghi riêng. 27 schema nguồn đã kiểm cấu trúc; 26 example có sẵn pass; ReferenceResult chưa có supplied example. Các test này ở temp copy, không sửa source. Cần xem `evidence/TEST_RECEIPT_BACKEND.json` để biết chính xác lệnh, môi trường, skip và giới hạn.

Browser receipt đính kèm V3 dùng mock/fixture ngoại tuyến, chưa là E2E tích hợp với auth/DB/payment/provider. Chưa có bằng chứng deploy SHA, staging toàn luồng, restore thực, legal/commercial approval hoặc vận hành hiện tại trong lần hợp nhất này. Giữ HOLD cho các phạm vi đó.

12 cổng sản phẩm giữ nguồn và phát hành; auth; authorization; legal/purpose; retention/delete; method/claims; legacy/migration; report/AI; commerce; reliability; independent security; operations. Mapping governance cũ được giữ trong 216 tệp. Mỗi gate chỉ đóng bằng receipt đúng candidate/artifact/môi trường/scope; không lấy trung bình các gate. Không có tỷ lệ sẵn sàng chung khi thiếu denominator được duyệt.

## 20. Bàn giao và cập nhật tiếp theo

Founder nhận tổng kế hoạch, báo cáo đối chiếu và 45 decision packet. Tech Lead nhận 316 task contract, 20 INT, graph/trace, API và method matrix. Backend nhận schema blockers, SQL/migration requirements, jobs/auth/privacy và demo matrix. Frontend nhận 69 screen contract và 28 product contract. QA nhận fixtures, positive/negative cases, scope evidence và release gates. Editorial/Method Council/Legal nhận nguồn, quyền, claim limits, report/Academy/territory packets.

Lần nhận việc đầu tiên đóng phạm vi nguồn/candidate, phân công role và reviewer, chọn vertical slice, giải quyết quyết định nền và rà 81 API blockers theo scope. Chưa cần mở tất cả sản phẩm để DEV bắt đầu thiết kế hoặc local synthetic work. Paid beta phải có đúng hệ quyền, nguồn/phương pháp đã duyệt, thanh toán đối soát, output review, support, recovery và release packet.

Tất cả thay đổi lần này ở lane tài liệu/công cụ kế hoạch. Các tệp ứng dụng đang có thay đổi được đối chiếu hash để bảo toàn. Không commit/push/merge/deploy, không chạy migration hoặc cấp quyền production. Những bước đó sẽ dùng một candidate và phạm vi thực thi được giao riêng.
