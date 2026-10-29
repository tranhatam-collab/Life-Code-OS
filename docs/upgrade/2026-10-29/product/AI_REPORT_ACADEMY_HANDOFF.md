# Bàn giao AI, chín cấp báo cáo và Academy ngày 29/10/2026

Mục tiêu là chuyển dữ liệu có quyền và phương pháp đã phát hành thành tài liệu dễ hiểu, có thể sửa, kiểm chứng và hành động. Chín tệp report contract V3 chủ yếu lặp một cấu trúc chung nên chưa đủ để thay thế chín hợp đồng nội bộ ngày 20/10. Bản hợp nhất giữ nguyên trường cũ của RPT-L1–L9, thêm nguồn V3 và đề xuất thực thi riêng trong `NINE_LEVEL_REPORT_CONTRACTS.json`.

## Mô hình nội dung dùng chung

Pipeline cần bàn giao là snapshot dữ liệu có kiểu → phép tính xác định → retrieval đã lọc quyền → claim plan → bản nháp → kiểm tra tự động → review con người → snapshot bất biến → render web/PDF/Word → sửa, thu hồi và thông báo tác động theo quyền. AI giải thích và soạn thảo trên bằng chứng đã cho phép; nó không tự tính lại công thức trong văn xuôi, tự cấp consent, tự mở release hoặc tạo dữ kiện cuộc đời chưa có.

Một claim cần `claim_id`, loại claim, nội dung, subject/version, purpose, input references, method/source versions, mức độ chính xác dữ kiện, quyền truy cập và trạng thái review. Phân biệt fact người dùng cung cấp, phép tính, quan sát, tham chiếu tượng trưng, kịch bản, khuyến nghị và giới hạn. Không dùng confidence tùy ý làm chứng cứ. Phần LCI bắt buộc có trạng thái nếu cấu trúc yêu cầu, nhưng giá trị để `null` khi chưa có hợp đồng đo lường đã duyệt; mã LCI cũ không tự trở thành thước đo được xác thực.

Bốn khối V3 là Identity, Analysis, Timeline và Action. Mười bốn phần gồm cover, source_of_truth, input_completeness, data_coverage, lci_status, identity, name_code_if_applicable, chrono_if_applicable, matrix_if_applicable, current_context, risk_boundaries, mission_options, action_plan, limitations_and_sources. “Có phần” nghĩa là có mục với dữ liệu hợp lệ hoặc lý do thiếu/không áp dụng/không được chia sẻ, không phải ép mọi báo cáo chứa tên, lịch, ma trận hay trang filler.

Một snapshot xuất cần ID, subject version, purpose, grant snapshot, method versions, source versions, template version, locale, claim IDs, reviewer receipt, timestamp và content digest. Web/PDF/Word cùng đọc một content tree. Render không được tải URL tùy ý hoặc đường dẫn hệ thống từ nội dung người dùng. Artifact private dùng truy cập được xác thực, thời hạn phù hợp và kiểm tra quyền lại; revoke/withdraw làm mất quyền tải theo chính sách đã duyệt. Sửa dữ kiện tạo revision mới và hiển thị thay đổi, không đổi âm thầm báo cáo đã xuất.

## Phạm vi riêng của từng cấp

| Cấp | Nội dung và dữ liệu cần | Method candidates V3 | Điều phải ngăn |
|---|---|---|---|
| L1 Self Signal | Mục tiêu, tên/ngày có quyền, policy và precision; tóm tắt ngắn, bước tính, unknowns và một hành động 30 ngày | NUM23, TAIL80, BCLC64, NAME-UNICODE | Trộn giả thuyết ngày/tên; biến tham chiếu thành tính cách cố định hoặc vận mệnh. |
| L2 Inner Architecture | Nhu cầu, giá trị, vai trò và 3–5 tình huống do chủ thể kể; phương án lựa chọn và câu hỏi xác nhận/bác bỏ | VALUES-INTEREST, HNH-REFLECTION | Đọc ý nghĩ, dựng động cơ/sự kiện hoặc ép mua L1 trước. Dữ kiện L1 liên quan có thể được nhập trực tiếp theo quyền và method release. |
| L3 Behavior Code | Nhật ký, check-in, bảng hỏi đã duyệt và cửa sổ quan sát; hành vi theo bối cảnh, mẫu số và thời gian | IPIP, LIFE-DESIGN, RESONANCE | Nhãn lâm sàng, kết luận mẫu khi ít quan sát, quan hệ nhân quả từ tương quan. |
| L4 Work & Wealth | Kỹ năng/lịch sử có bằng chứng, nguồn lực, mục tiêu và kịch bản người dùng nhập; sensitivity và trade-off | CAREER, CASHFLOW | Quyết định đầu tư/tín dụng/tuyển dụng hoặc dùng chu kỳ tượng trưng làm bằng chứng tài chính. |
| L5 Relationship Field | Consent riêng của từng người trưởng thành; sự kiện cùng được chia sẻ, thỏa thuận/xung đột tự kể | RELATIONSHIPS, HNH-REFLECTION | Tiết lộ nội dung riêng, kết luận chung bị ép, dự đoán trung thành hoặc định mệnh tương hợp. |
| L6 Life Timeline | Sự kiện có nguồn/ngày/precision, kế hoạch, chu kỳ riêng và giả thuyết/kịch bản; lĩnh vực life_changes/later_life/legacy/mobility | NUM-LIFE-CYCLES, LIFE-DESIGN | Bịa sự kiện hoặc tuổi thọ; nhập chu kỳ thành lịch sử; lấp 100 khoảng tuổi bằng suy đoán. |
| L7 Body Intelligence | Adult-self qua gate chuyên biệt; nhật ký môi trường và tự quan sát có mục đích rõ | HAND, FACE, FOOT-VOICE, RESONANCE | Suy bệnh/hormone/tính cách/đạo đức/đặc điểm riêng tư từ hình thái, giọng nói hay ảnh. Baseline không mở image inference. |
| L8 Mission Path | Giá trị tự chọn, năng lực có chứng cứ, trách nhiệm/nguồn lực; nhiều giả thuyết phụng sự và thử nghiệm 90 ngày | HNH-REFLECTION, CONTEMPLATION, LIFE-DESIGN | Một sứ mệnh định sẵn, ép hy sinh nguy hiểm, gán năng lực chưa có bằng chứng. |
| L9 Full Life Code | Tổng hợp các thành phần có quyền và khả dụng trong 18 lĩnh vực; deduplicate, giữ bất đồng, ưu tiên và hành động | LINEAGE, REPORT, LIFE-DESIGN | Ép đủ L1–L8 hoặc mua tất cả; giấu L7 chưa release; lấp số trang hoặc gọi là sự thật trọn đời. |

Các ID trên có thật trong register62. Theo dữ liệu nguồn, 62/62 phương pháp chưa production release; 11 có reference implementation. Con số này không phải 11 phương pháp sản phẩm đã được duyệt. `LINEAGE` có reference DAG/digest không chứng minh đã có production claim graph; `REPORT` chưa được đánh dấu reference dù có mã template. Backend bàn giao matrix method/formula/source/fixture riêng để reviewer xác định phạm vi thực tế.

Ngân sách trang L1 30–50, L2 40–60, L3 50–70, L4/L5 50–80, L6 60–100, L7 60–120, L8 80–150 và L9 150–600 là định hướng biên tập không bắt buộc. Tài liệu ngắn hơn vì thiếu dữ liệu hoặc không áp dụng là kết quả hợp lệ. Không dùng số trang, số token hoặc lời luận có vẻ đúng làm thước đo chất lượng.

## Hợp đồng AI và quyền

A0 chỉ soạn nháp; A1 đọc dữ liệu được cấp quyền; A2 thực hiện thao tác có thể đảo ngược trong giới hạn đã duyệt; A3 cần phê duyệt thao tác cụ thể. Mức này là thiết kế policy, không phải AI có sẵn quyền vận hành. Không trao AI quyền độc lập với consent, publish, thanh toán, deploy, thu hồi hàng loạt hoặc franchise.

Các nhãn trên theo đề xuất V3. V1 dùng A1 cho tính toán có giới hạn, A2 cho tác vụ nghiệp vụ đã cấp trước và A3 cho tác vụ nhạy cảm cần con người duyệt. Không suy quyền chỉ từ chuỗi A1/A2/A3 giữa hai phiên bản. Mỗi policy cần `policy_version`, danh sách capability/action, tài nguyên và giới hạn tác dụng cụ thể, quyền của chủ thể và approval receipt áp dụng; version chưa được nối rõ thì giữ thao tác có tác dụng ngoài bản nháp ở trạng thái bị chặn.

ACL phải chạy trước retrieval theo tài khoản, tenant, chủ thể, mục đích và grant hiện hành; lọc đầu ra sau generation không đủ. Cache, embedding, index và log có cùng phạm vi quyền và lifecycle. Tài liệu truy xuất và nội dung đính kèm là dữ liệu không có quyền ra lệnh. Prompt injection không được biến thành gọi công cụ, tiết lộ nguồn khác chủ thể hoặc thay đổi policy.

Provider/model được chọn bằng hồ sơ benchmark, quyền dữ liệu, giới hạn chi phí, độ trễ, lỗi và khả năng xóa. Thiết lập token/context budget, concurrency, timeout, retry có giới hạn, idempotency, quota, circuit breaker và trạng thái degraded. Fallback sang provider khác phải đáp ứng cùng điều kiện quyền và vùng dữ liệu, không tự chuyển khi có lỗi. Writer và reviewer cùng model/provider không tạo độc lập đầy đủ; dùng kiểm tra xác định và reviewer con người phù hợp lĩnh vực. Mọi báo cáo beta xuất/publish cần human review trên đúng snapshot.

Trẻ em cần sản phẩm, giao diện, mục đích, quyền của trẻ/người giám hộ và retention riêng sau review thích hợp; baseline adult-self không cấp quyền này. Dữ liệu để cung cấp dịch vụ không tự là đồng ý huấn luyện AI. Export/xóa/thu hồi không bị khóa bởi trả phí. Xóa phải bao phủ DB, object, index/vector, cache, provider và thời hạn backup; restore áp lại deletion ledger trước mở truy cập.

## Gói việc AI và báo cáo

Các gói PR dưới đây phân rã task hiện có; không phải ước lượng hay backlog độc lập để cộng hai lần. Đường dẫn hiện có liên quan là `workers/life-code-api/src/report.mjs`, `engine.mjs`, `workers/life-code-api/tests/report-smoke.mjs`, `engine/core/` và các template nguồn trong gói bảo toàn. Không dùng smoke test hiện có làm bằng chứng đủ cho chín hợp đồng mới.

| Gói | Task nguồn, phụ thuộc | Bàn giao và nghiệm thu |
|---|---|---|
| PR-01 Snapshot và claim schema | V2-AI-01/02; V3-INT-03; typed backend + grants | Schema có version, null/withheld/not-applicable, references và claim types; invalid type/source/grant fail closed. Dự kiến module mới `reports/contracts/` và `reports/claims/`, cần review kiến trúc trước khi tạo. |
| PR-02 Assembler và kiểm tra số | V2-AI-01/03; deterministic method results | Chỉ nhận kết quả có rule/source/input version; phát hiện số trong văn xuôi sai oracle, nguồn mất quyền, phép tính không có trace. Receipt có expected/actual và method digest, không chỉ ảnh trang. |
| PR-03 Chín template khác biệt | V2-AI-04; REPORT-02/03/04; V3-INT-05 | Mỗi template giữ output_emphasis và prohibited_inferences riêng; 14 phần có null policy; cùng content tree. Mục tiêu mới `reports/templates/LEVEL_1..9`, không coi template V3 boilerplate là đã hoàn thành. |
| PR-04 Bộ mẫu và đối chứng | V2-AI-05; PR-01–03 | 9 cấp × 10 fixture = 90 case yêu cầu: giữ 54 case của sáu loại cũ, thêm locale/withdrawn method/revoked grant/export parity. Đây là bộ cần thực hiện, chưa có claim đã chạy. L1 cần ba preview full/missing/hypothesis rõ ràng. |
| PR-05 Quota và lỗi provider | V2-AI-06; V3-INT-03; Q44 | Budget/token/timeout/retry/circuit-breaker; không retry vô hạn hoặc đổi provider trái quyền; cancel nhận receipt, không tạo hai job/bill. Chi phí/rate để null tới khi có quyết định. |
| PR-06 Biên tập và bản địa hóa | V2-AI-07; V2-FE-12 | Glossary claim types/methods, bản VI chuẩn và editor bản ngữ; test không tăng mức khẳng định, không mất limitation/null/source khi dịch; lưu locale/template/source versions. |
| PR-07 Review và publish | REPORT-05–08; PR-01–06 | Role author/reviewer/publisher, conflict-of-interest, approval hết hiệu lực khi snapshot đổi; negative test self-review/stale approval/revoked source. Beta human-review 100% snapshot xuất/publish. |
| PR-08 Export và correction | REPORT-09/10; V2-AI-08; PX-08 | Web/PDF/Word semantic parity, signed/authenticated download, correction diff, withdraw/impact và purge. Test arbitrary URL/path injection, expired/revoked link và sửa dữ kiện làm invalid review. |
| PR-09 Academy thực hành | V3-INT-08; V2-OPS-07; PR-03/04 | Chín lesson 120 phút, synthetic case, rubric thao tác/quyền/giới hạn, reviewer training, mẫu lesson và đánh giá học viên. Không lấy bài thực hành là review đồng ý phát hành phương pháp. |
| PR-10 Lãnh thổ và license | V3-INT-07; V2-OPS-08; Q42/43 | Hồ sơ theo product/country/partner class, nguồn/license, locale editor, pháp nhân/data roles, support/complaints và biên bản legal. Chỉ mở scope có hồ sơ hợp lệ; không suy ra luật hiện hành từ tài liệu đính kèm. |

`reports/`, `tests/fixtures/reports/` và `tests/integration/report-lifecycle/` là các thư mục mục tiêu mới được đề xuất, chưa phải cấu trúc ứng dụng hiện hữu. Việc hiện thực hóa cần chọn path phù hợp repo, danh sách allowed paths và review patch; không sửa mã đang dở trong đợt hợp nhất kế hoạch.

## Fixture, tiêu chí chất lượng và receipt

Sáu nhóm cũ mỗi cấp là GOLDEN, NULL, CONFLICT, UNAUTHORIZED, INJECTION, CORRECTION. Bốn nhóm thêm là LOCALE, WITHDRAWN_METHOD, REVOKED_GRANT, EXPORT_PARITY. Case golden đối chiếu output có cấu trúc với oracle và nguồn đã duyệt; case null phải không có đoạn bịa; conflict giữ ít nhất hai nguồn/hypothesis phân biệt; unauthorized/injection không đọc hay lộ dữ liệu ngoài quyền; correction tạo revision và vô hiệu review cũ. Case locale giữ claim boundary; withdrawn method dừng tái sinh nội dung cũ; revoke ngăn retrieval/download; parity so heading, bảng, số, claim/source IDs và giới hạn trên ba định dạng.

Mỗi receipt cần fixture ID/version, source snapshot/method/template/locale, SHA candidate, môi trường, input đã loại PII hoặc fixture synthetic, expected/actual, log lỗi đã che dữ liệu, người chạy/reviewer và thời gian. Văn bản trôi chảy chưa đủ pass. Sai số học, lộ dữ liệu, claim y khoa/tính cách không có căn cứ, lẫn track lịch sử/chu kỳ và review sai snapshot là lỗi chặn. Chất lượng biên tập xem khả năng hiểu nguồn, nhận biết phần chưa biết, sửa dữ kiện và chọn hành động có thể đánh giá; không tự dựng chỉ số điểm hài lòng hoặc tỷ lệ thành công khi chưa đo.

## Academy chín buổi 120 phút

V2 và V3 có thứ tự chủ đề khác nhau; cả hai nguồn được giữ. Chương trình dưới đây theo đề xuất V3, chưa tự trở thành giáo trình được người có thẩm quyền duyệt. Mỗi buổi gồm 20 phút ôn, 35 phút nội dung, 45 phút thực hành, 20 phút phản hồi: tổng 120 phút.

| Buổi | Nội dung | Thực hành và điều kiện đánh giá |
|---|---|---|
| 1 | Dữ liệu, quyền và giới hạn | Chọn mục đích/subject, phát hiện grant sai và phân biệt fact/symbolic/scenario; sai quyền phải sửa trước đi tiếp. |
| 2 | Tên và 23 chỉ số | Đối chiếu tên gốc/tên dùng, Unicode/Y và bước giảm; chỉ ra chỉ số chưa tính được. |
| 3 | Bát Cực và tail80 | Dẫn dòng nguồn và vị trí cặp; so strict/diagnostic 0/5; không kết luận tốt/xấu cả cuộc đời. |
| 4 | Lịch và độ chính xác thời gian | Hai giả thuyết ngày/giờ/timezone, các giới hạn nguồn và phần không thể phân giải. |
| 5 | Ma trận | Phân biệt raw/working và 17 vị trí; giải thích phép đếm, không suy sức khỏe/tính cách. |
| 6 | Resonance | Tự quan sát có thời gian/mẫu số và nhận biết thiếu bằng chứng; không gọi là đo năng lượng thực nghiệm. |
| 7 | Đối thoại và ranh giới | Diễn tập đồng thuận riêng, lời từ chối, quyền rút lại và giới hạn referral phù hợp. |
| 8 | Hành động | Viết thử nghiệm nhỏ, có thời hạn, tiêu chí đánh giá, điều kiện dừng và cách phản hồi. |
| 9 | Case tổng hợp synthetic | Báo cáo từ input tới nguồn/quyền/trace/unknown/action, reviewer độc lập chấm và yêu cầu sửa. |

Rubric cần tiêu chí đạt/chưa đạt theo thao tác và bằng chứng, không tự điền ngưỡng số hoặc học phí. Chứng nhận nội bộ phải nói rõ phạm vi, đơn vị cấp, version rubric, ngày đánh giá, tình trạng còn hiệu lực/thu hồi và cách xác minh công khai tối thiểu. Không mô tả là giấy phép lâm sàng hoặc nghề nghiệp. Trainer cần năng lực quan sát, review, giám sát, tái đánh giá và xử lý khiếu nại; người học không dùng dữ liệu người thật trước gate quyền và giám sát thích hợp.

## License, thị trường và điều kiện mở rộng

Bốn loại đối tác giữ riêng: referral, practitioner, institutional license và regional franchise. Mỗi loại có phạm vi thương hiệu, dữ liệu, nguồn/nội dung, hỗ trợ, review chất lượng, doanh thu và chấm dứt phù hợp; không dùng một mẫu hợp đồng chung để tự cấp mọi quyền. Thông tin giấy phép/nhượng quyền từ tài liệu là đề xuất, không phải hợp đồng đã ký.

Các phạm vi VN, EU/EEA, US, AU và SG được giữ cùng CA/UK ở mức nghiên cứu có điều kiện. Cần matrix theo country × product × audience × processing purpose với trạng thái legal entity, data roles/transfer, AI, child policy, source rights, locale editor, expert scope, support và franchise. `PENDING`, `NOT_RELEASED` hoặc thiếu receipt không được đổi thành market-ready. Trước mở thị trường, Legal phải nghiên cứu nguồn chính thức hiện hành tại thời điểm phát hành và lưu ý kiến theo phạm vi cụ thể; tài liệu này không tuyên bố đã xác nhận luật của từng nước.

Đóng bàn giao theo bằng chứng cùng candidate: typed schema và mapping phương pháp; fixture xác định; ACL/RAG/provider policy; template/renderer; human review; lifecycle export/correction/withdrawal/deletion; academy và territory hồ sơ riêng. Hoàn tất một bộ demo local không đóng các gate production, quyền nguồn, thương mại, pháp lý hoặc vận hành.
