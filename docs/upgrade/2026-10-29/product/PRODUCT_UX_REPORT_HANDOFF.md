# Bàn giao sản phẩm và giao diện Life Code OS ngày 29/10/2026

Bộ hợp đồng này cập nhật tổng kế hoạch bằng cách giữ nguyên từng trường của 23 sản phẩm, 45 màn hình và 9 hợp đồng báo cáo đã được chi tiết hóa trong bản nội bộ ngày 20/10. Dữ liệu V2 và V3 được đặt trong trường nguồn riêng; đề xuất thực thi mới nằm trong `v3_execution`. Kết quả là 28 sản phẩm và 69 ID yêu cầu màn hình. Các con số này mô tả phạm vi thiết kế; chúng không chứng minh có 69 trang hoạt động hoặc 28 sản phẩm đã phát hành.

Ba tệp máy đọc đi kèm là `PRODUCT_EXECUTION_CONTRACTS.json`, `SCREEN_EXECUTION_CONTRACTS.json` và `NINE_LEVEL_REPORT_CONTRACTS.json`. Mỗi bản ghi có nguồn, trạng thái và tiêu chí bằng chứng. Script `build_product_contracts.py` kiểm tra giữ nguyên các trường cũ, danh mục CSV/JSON 28 dòng và phép hợp 45 + 12 + 12 màn hình. Script chỉ đọc dữ liệu nguồn và dựng tài liệu; không chạy mã trong gói đính kèm, không triển khai ứng dụng.

## Phạm vi đã hợp nhất và những điểm cần quyết định

| Đối tượng | Giữ lại | Bổ sung | Cách xử lý |
|---|---:|---:|---|
| Sản phẩm | 23 ID cũ | 5 ID V3 | Giữ train T0–T8, giới hạn, giá chưa duyệt và bằng chứng của sản phẩm cũ; thêm hợp đồng đầu vào, đầu ra, quyền, lỗi, billing và exit gate cho 5 sản phẩm mới. |
| Màn hình | UI-01 đến UI-45 | V2-S01 đến V2-S12; V3-UI-058 đến V3-UI-069 | Giữ tất cả ID. 24 bổ sung có route, vai trò, operationId, trạng thái và bằng chứng đề xuất; chưa được ghi là đã triển khai. |
| Báo cáo | RPT-L1 đến RPT-L9 | 18 lĩnh vực, 4 khối nội dung, 14 phần chung V3 | Giữ hợp đồng riêng từng cấp, fixture cũ và giới hạn; phần không có dữ liệu được giải thích thay vì bịa nội dung. |
| Bề mặt sử dụng | Web responsive, desktop web | PWA theo khả năng trình duyệt | Native mobile/desktop chưa có bằng chứng triển khai. Không mở một engine công thức thứ hai cho từng thiết bị. |
| Thương mại | Quyền dữ liệu không bị khóa bởi thanh toán | 5 sản phẩm mở rộng | Giá, tiền tệ, provider và giấy phép cần hồ sơ riêng; `null` không phải giá miễn phí hoặc đồng ý chi tiền. |

V2-S02 trùng route mục tiêu với UI-12. Đề xuất dùng một màn hình với các biến thể so sánh giả thuyết, giữ cả hai ID để không mất yêu cầu. V2-S09 bổ sung quản lý quyền tại `/app/privacy/sharing`, trong khi UI-14 dùng `/app/sharing`; đây là đề xuất alias cần duyệt, chưa tự đổi route ứng dụng. UI-30 cũ mang nhóm trạng thái thanh toán dù là hỗ trợ; trường cũ được giữ và nhóm trạng thái hỗ trợ sửa lại được ghi riêng để reviewer xác nhận.

OpenAPI nguồn có 99 operationId; một nhóm đường dẫn mới đã chứa tiền tố `/api/v2` trong khi server cũng có base path. Frontend phải sinh adapter từ hợp đồng backend đã chuẩn hóa và kiểm tra URL thực tế, tránh ghép tiền tố hai lần. Các bản ghi màn hình tham chiếu operationId, không dùng đường dẫn nguồn làm bằng chứng endpoint hoạt động.

Một số khoảng trống API cần giải quyết trước khi dựng giao diện có dữ liệu thật: `syncOfflineBatch` chưa đủ cho toàn bộ hàng chờ và giải quyết xung đột; `methodReleaseDraft` chưa mô tả đầy đủ đọc hàng chờ, review và duyệt; TAIL80 chưa có endpoint production riêng; tạo chuyển giao di sản chưa đủ cho xác minh người nhận, đọc, sửa và thu hồi. `cases` là hợp đồng practice, không tự trở thành thư viện lab công khai. Những điểm này được ghi trong `contract_gaps` thay vì che bằng nút giao diện.

## Một tài khoản và các không gian được phép

Điểm vào V3-UI-058 bắt đầu bằng mục đích và chọn chủ thể được phép. Server xác minh tài khoản, tenant, chủ thể, mục đích, grant đang hiệu lực, phương pháp được phát hành và entitlement nếu sản phẩm yêu cầu. Người trả tiền không mặc nhiên là chủ dữ liệu. Chuyển hồ sơ hoặc tenant phải xóa nội dung nhạy cảm của ngữ cảnh trước, hủy request còn chạy và ngăn response trễ ghi vào ngữ cảnh mới.

Đợt đầu phục vụ người trưởng thành dùng dữ liệu của chính mình. Cặp đôi, gia đình, trẻ em, tổ chức, người hành nghề và đối tác có cổng quyền riêng. Không hiển thị tìm kiếm PII toàn cục. Không dùng điểm số tượng trưng để tuyển dụng, tín dụng, chẩn đoán, xếp đạo đức, dự đoán trung thành hoặc xác định vận mệnh. Nội dung do người dùng nhập, phép tính, quan sát, tham chiếu tượng trưng, kịch bản và khuyến nghị phải có nhãn phân biệt xuyên suốt màn hình và bản xuất.

## Năm sản phẩm bổ sung và quan hệ với sản phẩm cũ

| ID mới | Quan hệ giữ lại | Đầu ra dùng được cần bàn giao | Chặn phát hành khi |
|---|---|---|---|
| LC-NUM-ATLAS | Mở rộng LC-NUMBERS và các thành phần báo cáo | 23 chỉ số có bước trung gian; tên và policy Y/Unicode; vị trí cặp Bát Cực, chuyển nhóm, strict/diagnostic; tail80 có dòng nguồn; ma trận raw/working 17 vị trí | Chưa chốt nguồn, policy 0/5/zero, tên, phép giảm hoặc phiên bản công thức; chưa có fixture đối chiếu độc lập. |
| LC-LIFE-MAP | Mở rộng LC-L6 | 18 lĩnh vực tự chọn; lưới 100 khoảng tuổi có thể để trống; lịch sử, kế hoạch, chu kỳ và giả thuyết/kịch bản phân biệt; xem nguồn, độ chính xác và thay đổi | Bịa lịch sử để lấp lưới, nhập chu kỳ thành sự kiện, mất precision/timezone hoặc suy ra tuổi thọ. |
| LC-LEGACY | Dùng nền quyền chia sẻ và phiên bản LC-PUBLISH | Bộ viết/âm thanh có quyền; manifest người nhận/phạm vi/điều kiện; preview theo người nhận; receipt chuyển giao và thu hồi | Chưa xác minh người nhận/quyền tác giả; lộ nội dung từ preview; biến thành thực thi thừa kế pháp lý tự động. |
| LC-REGION-KIT | Bộ vận hành của LC-REGIONAL | Checklist theo lãnh thổ và sản phẩm, bản địa hóa, nguồn/giấy phép, pháp nhân, vai trò dữ liệu, hỗ trợ và loại đối tác | Chỉ có bản dịch, thiếu ý kiến pháp lý hoặc hợp đồng, giấy phép hết hạn, partner bị thu hồi. |
| LC-RESEARCH-STUDIO | Mở rộng phương pháp và quyền quản trị | Phiên bản nguồn, so sánh trường phái, rule tests, giới hạn, tác động thu hồi; nghiên cứu và release tách rõ | Tác giả tự duyệt, thiếu quyền nguồn, không truy được downstream hoặc thay quy tắc âm thầm trong báo cáo đã xuất. |

Hợp đồng JSON ghi cụ thể từng trường đầu vào, đầu ra, trường hợp âm tính và exit gate của cả năm. Không tạo quyền sử dụng mới chỉ vì ID xuất hiện trong catalog. `M01..M15` trong danh mục sản phẩm cũ và method_id của register62 là hai namespace nguồn; chỉ thay bằng mapping có bằng chứng. Các method_candidates trong chín cấp có ID thật trong register62 nhưng cả 62 phương pháp đều chưa phát hành production theo register nguồn. Reference implementation không thay thế quyết định phát hành.

Atlas 590 dòng bổ sung những điều kiện cần giữ ngay trên giao diện: số nhập dạng chuỗi giữ số 0 đầu; tên Unicode gốc giữ riêng bản dẫn xuất; không nhận PIN, OTP, mật khẩu, mã khôi phục hoặc toàn bộ giấy tờ để tính suffix. Có Y chưa xác định thì chỉ phần nguyên âm/phụ âm và cầu nối liên quan để null, không chặn tổng tên. Số đồng hạng được giữ; hai kết quả cùng căn nhưng khác tổng trung gian không được ghi là đã tái lập nguồn. Các span Challenge và Period không tự lấy tuổi Pinnacle nếu thiếu policy có nguồn.

Bát Cực cần lưu đủ vị trí n−1 cặp, n−2 cửa sổ ba số và chuyển nhóm liền nhau. Strict giữ nguyên cặp chứa 0/5 ở trạng thái chưa xử lý; diagnostic chỉ bổ sung cầu đơn A0B/A5B đủ điều kiện, không xóa trace cặp gốc. `8553`, `1001`, `3501` phải giữ `unresolved_modifier_run`. Không dựng hệ số độ mạnh/chế hóa khi nguồn chưa có. Psychomatrix tách raw/working, có W1–W4 và 17 vị trí; W3 âm là trường hợp chưa hỗ trợ, không tự đổi thuật toán. TAIL80 giữ `source_text` riêng bản biên tập; zero_policy chưa chọn không tự đổi 0 thành 80. So phương án không có tiêu chí utility được duyệt thì `recommended=null`; giá hoặc tình trạng thuê bao trong ảnh chưa được xác minh phải có nhãn thích hợp.

Lưới Life Map 100 khoảng 0–99 chỉ là cách điều hướng ban đầu. Sự kiện ở tuổi 100 hoặc 120 vẫn phải có trong lịch sử toàn cục và được truy cập qua phạm vi mở rộng hoặc phân trang; không bị cắt vì không thuộc ô điều hướng. Stage S09 không có điểm kết thúc cố định không tạo dự đoán tuổi thọ. Plan cần canonical ID và version trước CRUD/offline sync; cấu trúc demo chưa chứng minh đã đủ các trường này.

## Hợp đồng trải nghiệm trên điện thoại, tablet và desktop

Mọi màn hình cần chứng minh cùng dữ liệu, quyền, provenance, trạng thái và hành động tiếp theo ở các kích thước 320, 360, 390, 768, 1280 và 1440 px. Điện thoại ưu tiên một luồng thao tác, tóm tắt trước, mở rộng phép tính khi cần. Desktop có thể dùng cột so sánh và bảng chi tiết nhưng không được tự mở thêm dữ liệu hoặc quyền. Ma trận, timeline và đồ thị luôn có cách đọc dạng danh sách/bảng cho bàn phím và screen reader.

Trạng thái chung gồm loading, empty, error, blocked, ready, partial, needs_input, offline, stale và forbidden. Hành động ghi có validating/submitting/conflict; công việc dài có queued/running/cancel_requested/cancelled/retryable/terminal; báo cáo có draft/review/corrected/withdrawn; xóa dữ liệu thể hiện legal_hold/partial_failure/backup_expiry_pending. Nút “thử lại” không gửi lại khoản thanh toán hoặc job thiếu idempotency. Không báo lưu, xuất, thanh toán, thu hồi hoặc xóa thành công trước receipt server.

Mỗi lỗi có thông điệp người dùng hiểu được và bước tiếp theo: 401 đăng nhập lại; 403 không lộ sự tồn tại của dữ liệu; 409 giữ bản nháp và cho chọn cách xử lý; 422 chỉ rõ trường hoặc policy thiếu; 429 giữ ý định và thời gian thử lại; 503 nói chưa có kết quả. Khi quyền bị thu hồi, màn hình đang mở và link xuất phải mất khả năng đọc đúng phạm vi bị thu hồi.

Accessibility nhắm WCAG 2.2 AA cho luồng chính, kiểm tra bàn phím, thứ tự focus, focus không bị che, label/error được đọc, reflow 320 px và zoom 400%, giảm chuyển động và thông tin không chỉ dựa màu. Mục tiêu chạm ưu tiên 44 px; đây là lựa chọn usability của sản phẩm, không được mô tả sai thành ngưỡng tối thiểu AA cho mọi trường hợp. Kiểm thử tự động hỗ trợ, còn keyboard/screen reader và bố cục ở viewport thật cần receipt thủ công có cấu hình thiết bị.

Private API, báo cáo, nhật ký, token và grant không vào service-worker cache mặc định. Nếu cho bản nháp offline, cần đồng ý rõ, TTL, phân tách tài khoản, mã hóa phù hợp, version conflict và receipt purge khi logout, đổi tài khoản, thu hồi hoặc xóa. Đồng ý, chia sẻ, xóa, thanh toán, review, publish và admin dùng mạng. Chưa bật background sync trước khi duyệt schema xung đột và idempotency. Cài PWA là cải tiến theo khả năng trình duyệt; native chỉ được đề xuất sau khi chứng minh nhu cầu camera/offline/notification và chi phí vận hành.

## Gói việc frontend có thể bàn giao

Các mã PX dưới đây chia nhỏ công việc trong backlog hợp nhất, không cộng thêm ngày công vào 296 task nguồn. Ước lượng mới để `null` đến khi schema, prototype và người chịu trách nhiệm được chốt. Các phụ thuộc nguồn dạng chuỗi của V2 được giữ nguyên; parallel hóa thực tế chỉ sau khi Tech Lead xác nhận hợp đồng độc lập.

| Gói | Task nguồn và phụ thuộc | Phần phải xây | Nghiệm thu và bằng chứng |
|---|---|---|---|
| PX-01 Khung ngữ cảnh | WEB-01; V2-FE-01/02; V3-INT-01; Q39 | Navigation, chọn subject/purpose/tenant, dữ liệu tối thiểu, V3-UI-058, adapter identity/grants/eligibility. | Hai tenant, hai subject, response trễ và browser back không lộ ngữ cảnh trước; receipt request/response đã che PII và ảnh phone/desktop. |
| PX-02 Lab synthetic | V2-FE-03; V2-AI-05; backend demo contracts | V2-S01/S12: tìm case, biết input thiếu, expected result, reset và phiên bản fixture; adapter lab riêng. | Không nhận dữ liệu khách hàng, không gọi practice API như guest; case full/missing/conflict chạy lặp lại xác định, hiển thị rõ giới hạn reference. |
| PX-03 Số và tên | V2-FE-04; V3 method tasks; Q32/33/35/36 | V3-UI-059–065, V2-S03/04; component trace, pair table, matrix, name diff. | Từng giá trị trỏ input/rule/source; leading zero và Unicode không mất; strict/diagnostic có nhãn; ma trận có bảng thay thế; số học so oracle backend. |
| PX-04 Life Map | V2-FE-05; V3-INT-02; Q37/38 | V3-UI-066/067 cùng UI-19; 18 lĩnh vực, 100 khoảng tuổi, lọc track và precision; canonical plan ID/version. | Không có dữ liệu vẫn điều hướng được; sự kiện sai thời gian/tz/conflict được cảnh báo; các tuổi 80/99/100/120 không bị mất lịch sử; không sinh lịch sử; phone và bàn phím đọc được cùng nguồn. |
| PX-05 Hợp đồng trạng thái | V2-FE-06/07/08; WEB-02–10 khi được phân công | State components, lỗi, focus, responsive; sửa đề xuất UI-30 sau review; bao phủ 69 ID bằng checklist. | Mỗi màn hình có PHONE/DESKTOP/A11Y/OFFLINE/NEGATIVE receipt hoặc trạng thái blocked có lý do; không dùng snapshot một trang đại diện toàn bộ. |
| PX-06 Offline có kiểm soát | V2-FE-09; V3-INT-06; Q28 | V2-S05, storage adapter, conflict UI, purge lifecycle, network-only actions. | Duplicate retry không nhân mutation; stale draft không ghi đè server; revoke/logout/switch/delete purge qua receipt; nếu chưa đạt thì giữ offline write disabled. |
| PX-07 Quyền và di sản | V2-FE-10; V3-INT-02; privacy backend | V2-S09/10, V3-UI-068; grant scope/expiry, người nhận, status xóa và preview. | Không lộ dữ liệu người chưa đồng ý; revoke khi tab/export đang mở; deleted/expired/partial state rõ; quyền dữ liệu không phụ thuộc mua hàng. |
| PX-08 Đọc và xuất báo cáo | V2-FE-11; V3-INT-05; REPORT-05–10 | Outline theo content tree, nguồn/unknowns, phiên bản/correction, trạng thái export và download có quyền. | Cùng snapshot trên web/PDF/Word; revoke/withdraw chặn đúng link; bài dài đọc phone không mất heading/table/next action. |
| PX-09 Reviewer và Research Studio | V2-OPS-07; V3-INT-03; method release contracts | V2-S06/07/08, V3-UI-069; nguồn xung đột, test vectors, hàng chờ và impact preview. | Author/reviewer/publisher tách; stale approval bị chặn; không mở deploy hay freeze chỉ do UI; receipt tác động chỉ gồm phạm vi có quyền. |
| PX-10 Bản địa hóa và territory | V2-FE-12; V2-OPS-08; V3-INT-07/08; Q42/43 | V2-S11, glossary, locale source references, country gate UI và academy access. | Dịch không làm mạnh claim hoặc mất null/limitation; partner/country pending không thành enabled; có editor bản ngữ và support rehearsal. |

## Đường dẫn triển khai và giới hạn sửa đổi

Repository hiện có frontend HTML/CSS/JS ở root: `index.html`, `9-levels-life-code.html`, `account.html`, `dashboard.html`, `timeline-cuoc-doi.html`, `bao-cao-life-code.html`, `engine-lab.html`, `app.js`, `site.js`, `style.css`. Backend hiện có `workers/life-code-api/src/index.js`, `engine.mjs`, `report.mjs`, `api/server.cjs` và `engine/core/`. Các file hiện tại có thay đổi đang làm; bản bàn giao này không sửa hay coi chúng là đã hoàn tất.

Đề xuất đợt triển khai tạo module ở `frontend/contracts/`, `frontend/features/context/`, `frontend/features/numbers/`, `frontend/features/life-map/`, `frontend/features/privacy/`, `frontend/features/reports/` và `frontend/features/research/`; đây là thư mục mục tiêu mới, chưa tồn tại, cần quyết định kiến trúc trước khi tạo. Tiếp tục frontend tĩnh hay chuyển framework là quyết định riêng, không được tự nhận một scaffold mới là ứng dụng đã nâng cấp. Adapter API chỉ lấy operationId từ spec chuẩn hóa của backend. Bộ test mục tiêu `tests/ui/` và `tests/fixtures/product/` cũng là đề xuất mới; mọi patch ứng dụng cần danh sách allowed paths và review riêng.

## Bộ demo và thứ tự nghiệm thu

Ngoài case backend có sẵn, yêu cầu tối thiểu 24 kịch bản sản phẩm dưới đây. Đây là acceptance mới đề xuất, không cộng thành số demo đã chạy. Mỗi case ghi fixture version, expected output, locale, viewport, role/scope, method/source version, receipt và trạng thái pass/fail/blocked.

Atlas nguồn ghi 90 tình huống V2 và 77 tình huống mới, tổng 167; tính toàn miền 10.000 đuôi, 64 cặp và 512 chuỗi ba số là phép kiểm thuật toán riêng. Chỉ báo cáo là đã chạy sau receipt thực tế từ lane backend/demo; không cộng chúng thành 10.000 người được kiểm chứng hoặc coi 167 case là toàn bộ acceptance của 69 màn hình.

| Nhóm | ID đề xuất | Tình huống |
|---|---|---|
| Intake và ngữ cảnh | PX-DEMO-01–04 | Người dùng adult-self đầy đủ; thiếu ngày sinh vẫn vào được phần hợp lệ; hai giả thuyết không tự chọn; đổi tenant khi response cũ về trễ. |
| Atlas | PX-DEMO-05–10 | Unicode/Y; leading zero; Bát Cực strict 0/5; diagnostic có nhãn; tail80 thiếu bảng nguồn; raw/working psychomatrix khác nhau. |
| Life Map | PX-DEMO-11–14 | Lĩnh vực tự chọn và khoảng tuổi trống; sự kiện thiếu precision/timezone; lịch sử xung đột; chu kỳ chưa release không biến thành lịch sử. |
| Quyền | PX-DEMO-15–18 | Người trả tiền không có grant; revoke khi tab mở; người nhận di sản chưa xác minh; xóa một phần và backup expiry. |
| Báo cáo và vận hành | PX-DEMO-19–24 | Báo cáo thiếu dữ liệu; export bị thu hồi; bản dịch giữ limitation; offline conflict không overwrite; người viết tự review bị chặn; territory chưa đủ hồ sơ vẫn đóng. |

Đóng mỗi gói theo thứ tự: hợp đồng dữ liệu/quyền và decision cần thiết; prototype fixture; adapter và component; test âm tính; QA phone/desktop/accessibility; review snapshot; staging theo SHA và môi trường cụ thể. Hoàn thành tài liệu chỉ cho phép bắt đầu chuẩn bị DEV. Release cần bằng chứng backend, nguồn/phương pháp, vận hành và người có thẩm quyền riêng; bảng này không cấp quyền triển khai hoặc mở thanh toán.
