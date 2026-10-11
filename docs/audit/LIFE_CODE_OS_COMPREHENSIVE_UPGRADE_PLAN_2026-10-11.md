# LIFE CODE OS

## Kế hoạch nâng cấp toàn diện để Team Audit thẩm định

| Thuộc tính | Giá trị |
|---|---|
| Tên sản phẩm | Life Code OS |
| Trục phương pháp | Huyền Nhân Học - Mật Mã Đời Người - Đồng nhịp sống - Hành động chuyển hóa |
| Ngày lập | 2026-10-11 |
| Mốc đối chiếu thông tin công khai | 2026-10-10 |
| Trạng thái tài liệu | `PROPOSED_FOR_TEAM_AUDIT` |
| Trạng thái phát hành sản phẩm | `NO_GO_FOR_PRODUCTION_EXPANSION` |
| Người phê duyệt cuối | Founder Trần Hà Tâm |
| Phạm vi | Product, method governance, data, API, AI, security, privacy, reports, commerce, operations và release gates |
**Không phải:** Chứng nhận tuân thủ pháp luật, phê duyệt phương pháp, biên bản nghiệm thu production hoặc lệnh deploy

---

## 0. Cách đọc và nguyên tắc bằng chứng

Tài liệu này tách bốn loại sự thật:

| Nhãn | Nghĩa |
|---|---|
| `VERIFIED_CURRENT` | Đã kiểm tra trực tiếp ở source hoặc live tại ngày audit |
| `VERIFIED_CONTENT_MATCH` | Nội dung live khớp byte hoặc hành vi với source, nhưng chưa chứng minh deployed SHA |
| `CONTRADICTED` | Báo cáo cũ bị source hoặc runtime hiện tại bác bỏ |
| `NOT_CHECKED` | Chưa có bằng chứng đủ tin cậy |
| `BLOCKED` | Không thể xác minh vì thiếu quyền, receipt hoặc hạ tầng |

Không dùng số trang, số file, báo cáo tự khai, test smoke hoặc HTTP 200 để suy ra sản phẩm đã đúng phương pháp, an toàn dữ liệu hay production-ready.

### 0.1 Repo và baseline audit

| Hạng mục | Bằng chứng | Trạng thái |
|---|---|---|
| Canonical remote candidate | `git@github.com:tranhatam-collab/Life-Code-OS.git` | `VERIFIED_CURRENT` |
| Remote `main` tại thời điểm lập plan | `99b402764437f81859fa0cd3a3af860125f7bd52` | `VERIFIED_CURRENT` |
| Local phase branch đã quan sát | `phase-1.5/handover-bilingual-foundation` | `VERIFIED_CURRENT` |
| Local phase HEAD đã quan sát | `4df9b6efa6601bc113bc51956ed83e076da75657` | `VERIFIED_CURRENT` |
| Quan hệ remote/local | Local phase có thêm một commit so với remote main | `VERIFIED_CURRENT` |
| Nội dung public live | Home, Engine Lab và Bắt đầu khớp local phase source | `VERIFIED_CONTENT_MATCH` |
| Deployed commit SHA | Chưa có deployment receipt ánh xạ live về commit | `BLOCKED` |
| Local worktree sạch/bẩn | Git status trên checkout iCloud chưa hoàn tất ổn định | `NOT_CHECKED` |

Nhánh chứa tài liệu này được tạo từ remote `main` sạch để Team Audit chỉ review kế hoạch, không trộn source local chưa được khóa.

### 0.2 Runtime đã xác minh

| Surface | Kết quả |
|---|---|
| `https://lifecode.iai.one/` | HTTP 200 |
| Các trang public chính | HTTP 200 hoặc redirect chuẩn sang clean URL rồi HTTP 200 |
| Worker `/health` | Trả `ok: true`, service `life-code-api`, version `1` |
| `/api/v1/me` không token | HTTP 401 |
| Timeline engine | Đang trả chuỗi tín hiệu 0-99 và các nhóm risk/opportunity/transformation/mission |
| Security headers | Có một phần; chưa chứng minh CSP và HSTS đầy đủ |
| CORS | Có trường hợp trả `Access-Control-Allow-Origin: *`; cần khóa theo origin và loại endpoint |

### 0.3 Test hiện có

`npm run engine:test` và `npm run report:test` pass trên clean clone. Các test hiện tại mới chứng minh tính deterministic, hình dạng response và report smoke. Chúng chưa chứng minh:

- Tính đúng của phương pháp.
- Giá trị khoa học hoặc khả năng dự báo.
- Object-level authorization.
- Consent, retention và deletion.
- Payment/entitlement.
- Production E2E.
- Backup/restore và disaster recovery.

---

## 1. Phán quyết hiện tại

### 1.1 Kết luận

Life Code hiện có website, API, D1 schema, một số engine deterministic và giao diện báo cáo. Tuy nhiên, hệ thống chưa đáp ứng kiến trúc Life Code OS được mô tả trong kế hoạch này.

**Quyết định đề xuất:**

| Hoạt động | Quyết định |
|---|---|
| Tiếp tục nghiên cứu, đặc tả và remediation | `GO` |
| Tiếp tục website public với copy đã giảm claim | `CONDITIONAL_GO` |
| Mở rộng thu dữ liệu sâu, ảnh hình thái, trẻ em hoặc sức khỏe | `NO_GO` |
| Bán báo cáo sâu dựa trên LCI/timeline hiện tại | `NO_GO` |
| Mở Level 2-9 như sản phẩm hoàn chỉnh | `NO_GO` |
| Chạy private pilot sau khi P0-P4 đạt gate | `CONDITIONAL_GO` |

### 1.2 Mức hoàn thành theo cổng phát hành

Không dùng một điểm chủ quan duy nhất. Nếu quy đổi theo 12 cổng bắt buộc, hiện mới có khoảng 3 cổng có bằng chứng một phần: public surfaces, Worker liveness và engine/report smoke.

| Gate | Hiện trạng |
|---|---|
| Canonical source và deployed SHA | Chưa đạt |
| Website public hoạt động | Đạt một phần |
| API liveness | Đạt |
| Authorization/tenant isolation | Chưa đạt |
| Consent/privacy/deletion | Chưa đạt |
| Method/source/version governance | Chưa đạt |
| Valid computation contracts | Chưa đạt |
| Structured report pipeline | Chưa đạt |
| Commerce/entitlement/refund | Chưa đạt |
| Operations/backup/recovery | Chưa đạt |
| Independent security/method review | Chưa đạt |
| Pilot outcome/Founder release approval | Chưa đạt |

Nếu buộc quy đổi: **20-25% so với kiến trúc đích**, không phải 90-95%. Claim 90-95% trong `PROJECT_STATUS_MASTER.md` là `CONTRADICTED` bởi source, runtime và thiếu các gate nêu trên.

---

## 2. P0 cần containment trước khi mở rộng

### 2.1 Engine và claim không hợp lệ

1. `engine/core/timeline.js` dùng hàm lượng giác trên seed/năm để tạo tín hiệu rồi gán nhãn risk, opportunity, transformation và mission.
2. `bat-dau.html` gửi nhiều layer score và health/wealth/mission input hardcode, không phát sinh từ câu trả lời thực.
3. LCI đang trộn data completeness, method coverage, adaptation, convergence và readiness vào một nhãn khó kiểm chứng.
4. Contract hiện ép score/confidence cho cả phép tính biểu tượng, trong khi kết quả đúng có thể cần `null`.
5. Timeline spec mô tả xác suất/rủi ro nhưng implementation chưa có mô hình được đánh giá.

**Containment bắt buộc:**

- Gắn `experimental_legacy` cho LCI, timeline và risk/wealth/mission hiện tại.
- Không dùng các output này để bán, cảnh báo, tư vấn sức khỏe, tài chính hoặc quyết định quan trọng.
- Gỡ hoặc ẩn Engine Lab khỏi public production; chỉ cho phép môi trường test có access control.
- Thay copy “xác suất” bằng “tín hiệu biểu tượng” cho đến khi có mô hình phù hợp và được đánh giá.
- Không tạo dữ liệu còn thiếu để làm giao diện có vẻ đầy đủ.

### 2.2 Authorization và session

Source cho thấy các điểm cần remediation riêng tư:

- Đọc profile theo ID chưa chứng minh ownership check.
- Session start nhận `user_id` từ client và có đường ghi đè profile.
- Life-code-data có thể ưu tiên `payload.user_id` hơn authenticated subject.
- Report nhận `result_id` nhưng chưa chứng minh report thuộc subject hiện tại.
- Bearer session token đang được lưu plaintext.
- Frontend lưu định danh và token trong `localStorage`.

**Containment bắt buộc:**

- Tắt endpoint profile/report không owner-scoped cho tới khi có middleware bắt buộc.
- Không tin bất kỳ `user_id`, `profile_id`, `result_id` do client gửi nếu chưa resolve qua session và grant.
- Thu hồi toàn bộ session token cũ sau khi đổi auth model.
- Lưu hash token, rotation metadata và expiry; ưu tiên secure, HttpOnly, SameSite cookie cho web.
- Tạo negative authorization tests cho mọi object ID.
- Rà soát audit/access logs mà không khai thác dữ liệu người dùng thật.

### 2.3 Privacy và dữ liệu nhạy cảm

Tạm dừng intake mới cho ảnh mặt, tay, chân, dữ liệu trẻ em, sức khỏe và lịch sử xã hội cho tới khi có:

- Account-subject relationship.
- Consent theo mục đích và phiên bản notice.
- Guardian flow cho trẻ em.
- Retention schedule.
- Export, correction và deletion workflow.
- Private object storage và short-lived access.
- Data protection impact assessment phù hợp.

### 2.4 Source và deploy provenance

- Chốt canonical repo, canonical release branch và protected branch rules.
- Build từ clean checkout theo exact SHA.
- Ghi commit SHA, deployment ID, Worker version và asset digest vào release receipt.
- Không deploy Worker nếu test/security/migration gate chưa pass.
- Không dùng `--commit-dirty=true` cho production release.

---

## 3. Định nghĩa sản phẩm được đề xuất

### 3.1 Public definition

> Life Code OS là nền tảng tự hiểu và thiết kế đời sống, kết hợp hồ sơ cá nhân, các hệ tri thức và biểu tượng, quan sát thực tế, bối cảnh sống và kế hoạch hành động trong một hệ thống có thể cập nhật.

Life Code là hồ sơ sống, không phải lời phán cố định. Báo cáo là một snapshot có phiên bản, không phải kết thúc hành trình.

### 3.2 Bốn câu hỏi sản phẩm

| Câu hỏi | Dữ liệu ưu tiên |
|---|---|
| Tôi đang có gì? | Hồ sơ, năng lực có minh chứng, nguồn lực, giá trị, trách nhiệm, phần chưa biết |
| Tôi vận hành thế nào? | Hành vi, lịch, công việc, tiền bạc, học tập, giao tiếp |
| Điều gì phù hợp với hiện tại? | Vai trò, môi trường, quan hệ, nhịp sống, thực phẩm, tải việc |
| Tôi nên làm gì tiếp? | Hành động, người thực hiện, thời hạn, nguồn lực, cách đánh giá |

### 3.3 Vòng đời trải nghiệm

```text
Hiểu -> Chọn -> Thực hành -> Ghi nhận -> Xem lại -> Điều chỉnh
```

### 3.4 Định vị thị trường

Không cạnh tranh bằng lời hứa “AI biết số phận”. Định vị khác biệt là:

> Provenance-first living profile: tri thức có nguồn, dữ liệu đúng chủ thể, nội dung biểu tượng được gắn nhãn, quan sát thực tế, kế hoạch hành động, theo dõi kết quả và quyền rà soát của con người.

Đối chiếu sản phẩm:

| Nhóm | Điểm mạnh thị trường | Khoảng khác biệt Life Code |
|---|---|---|
| The Pattern/Co-Star | Personality, astrology, relationship, timing | Nguồn/phương pháp có version, hành động và outcome tracking |
| Daylio/habit apps | Nhật ký, goal và mood tracking | Tổng hợp tri thức, bối cảnh và báo cáo có cấu trúc |
| BetterUp/coaching | AI + human coaching | HNH, symbolic methods rõ nhãn, hồ sơ sống sở hữu bởi người dùng |

---

## 4. Khóa thuật ngữ hệ thống

| Thuật ngữ | Định nghĩa bắt buộc |
|---|---|
| Method | Một phương pháp cụ thể với nguồn, input, rule, version và giới hạn |
| Layer | Phạm vi phân tích như thời gian, tên, hành vi, quan hệ |
| Field | Thành phần môi trường như công việc, nơi sống, âm thanh |
| Signal | Kết quả hoặc quan sát có nguồn và loại nội dung |
| Pattern | Chuỗi lặp nhận diện từ dữ liệu hoặc chủ đề biểu tượng có nhãn |
| Level | Gói sản phẩm có mục tiêu, input, output và entitlement |
| Report | Snapshot có version của kết quả tại một thời điểm |
| Plan | Hành động, owner, deadline, nguồn lực và cách đánh giá |

Quy tắc chống double counting:

- Một method có thể đóng góp nhiều layer nhưng không trở thành nhiều bằng chứng độc lập.
- Mission là synthesis, không được cộng ngược như một nguồn độc lập.
- Cùng ngày sinh không được tạo bốn “phép đo độc lập” về hành vi, sức khỏe, tài chính và sứ mệnh.

---

## 5. Kiến trúc sản phẩm hợp nhất

```text
PUBLIC WEB / MOBILE WEB
        |
ACCOUNT - SUBJECT - CONSENT - ENTITLEMENT
        |
PROFILE VERSION + DATA HYPOTHESES + OBSERVATIONS
        |
ANALYSIS ORCHESTRATOR
  | validate | select methods | record run | enforce purpose
        |
VERSIONED METHOD CORE
  | chrono | name | numbers | questionnaires | resources
        |
12 LIFE CODE LAYERS <-> 12 RESONANCE FIELDS
        |
HNH SYNTHESIS
  | agreement | conflict | missing data | questions | options
        |
AI RETRIEVAL / WRITER / REVIEWER
        |
TIMELINE + ACTION SYSTEM
        |
9 PRODUCT LEVELS + REPORTS + PRACTITIONER
        |
OUTCOME OBSERVATION + PROFILE UPDATE

Cross-cutting: authorization, privacy, audit, cost, quality,
method governance, observability, backup and recovery.
```

### 5.1 Kiến trúc kỹ thuật đích

Khởi đầu bằng modular monolith, không chia hàng chục microservice.

| Thành phần | Hướng đề xuất |
|---|---|
| Public website | Giữ clean URLs; copy an toàn; method education và product discovery |
| User application | Dashboard, profiles, consent, journals, reports, actions, sharing |
| API gateway | TypeScript Cloudflare Worker với OpenAPI và policy middleware |
| Business database | PostgreSQL, migration có version, row/object authorization |
| File/image/report | Private R2; presigned URL thời hạn ngắn; malware/content checks |
| Background work | Cloudflare Queues; job idempotency; retries và dead-letter policy |
| Method core | Một implementation canonical có version; Python chỉ khi library/precision cần |
| AI gateway | Tách khỏi deterministic core; policy, model routing, cost và evidence log |
| Admin | Method/source release, content approval, access review, quality và cost |
| Observability | Structured logs, traces, SLO, privacy-safe alerts |

Không tính lại nghiệp vụ trong UI, mobile hoặc PDF. Tất cả surface dùng cùng immutable method result snapshot.

---

## 6. Kho tri thức và method governance

### 6.1 Hai mươi họ phương pháp

Giữ registry K01-K20 trong phạm vi nghiên cứu. Registry không đồng nghĩa đã triển khai hoặc được phép phát hành.

| Mã | Họ tri thức | Release mặc định |
|---|---|---|
| K01 | Lịch pháp, thiên văn, múi giờ lịch sử | Candidate cho Level 1 |
| K02 | Bát tự, Tứ trụ, Tử Bình | Research only |
| K03 | Tử Vi Đẩu Số và mệnh bàn liên quan | Research only |
| K04 | Kinh Dịch, Mai Hoa, Lục Hào | Research only |
| K05 | Kỳ Môn, Lục Nhâm, Thái Ất, trạch nhật | Research only |
| K06 | Phong thủy, Vastu và bố trí không gian | Research only |
| K07 | Jyotish, Nadi và truyền thống Ấn Độ | Research only |
| K08 | Chiêm tinh phương Tây và trung đại | Research only |
| K09 | Lịch và chiêm nghiệm khu vực | Research only |
| K10 | Thần số học, Psychomatrix, chữ-số | Candidate có điều kiện |
| K11 | Bát Cực Linh Số, Mã đuôi 80, dãy định danh | Candidate có điều kiện |
| K12 | Danh học, ngôn ngữ, ký hiệu | Candidate có điều kiện |
| K13 | Bàn tay, khuôn mặt, bàn chân và hình thái | Research only |
| K14 | Tarot, Rune, Ifá, giấc mơ và chiêm nghiệm | Research only |
| K15 | Human Design, Gene Keys và hệ tổng hợp mới | Research only |
| K16 | Triết học, tôn giáo, thực hành nội tâm | Content + reflection |
| K17 | Tâm lý học và đo lường cá nhân | Chỉ instrument đủ điều kiện |
| K18 | Hành vi, nghề nghiệp, kinh tế, xã hội | Candidate cho action planning |
| K19 | Sinh hoạt, sức khỏe nền, môi trường | Observation only |
| K20 | Toán, dữ liệu, AI, kỹ thuật tri thức | Platform governance |

### 6.2 Method passport

Mỗi method release phải có:

| Nhóm | Trường bắt buộc |
|---|---|
| Identity | `method_id`, tên, family, owner, status |
| Provenance | Nguồn, edition, page/section, ngôn ngữ, license/rights |
| Contract | Input, output, rule, precision, missing-data behavior |
| Boundaries | Không hỗ trợ gì, chống chỉ định claim, nhóm người dùng không áp dụng |
| Validation | Golden examples, edge cases, peer review, regression suite |
| Release | Version, approver, release date, rollback target |

### 6.3 Trạng thái phát hành

```text
researching -> specified -> calculation_verified -> content_reviewed
-> permitted_for_product -> deprecated -> retired
```

Không method nào đi thẳng từ tài liệu nghiên cứu sang production.

---

## 7. Hợp đồng 12 lớp Life Code

| Layer | Input chính | Output hợp lệ | Claim bị cấm nếu không có căn cứ riêng |
|---|---|---|---|
| Chrono Code | Ngày/giờ/nơi sinh, sai số | Quy đổi thời gian, chu kỳ ghi nhãn | Sự kiện chắc chắn sẽ xảy ra |
| Name Code | Tên gốc, tên dùng, cách đọc | Quy đổi và nghĩa khả dĩ | Tính cách đã xác minh chỉ từ tên |
| Birth Matrix | Method result riêng | Bản đồ song song | Trộn quy tắc thành một “chân lý” |
| Face Code | Ảnh có consent và điều kiện chụp | Mô tả hình thức | Đạo đức, trí tuệ, bệnh, thu nhập |
| Hand Code | Ảnh + tay trái/phải + phép đo | Mô tả hình thái | Số phận hoặc bệnh lý |
| Foot Code | Ảnh/quan sát phù hợp | Mô tả hình thái | Căn cơ, sứ mệnh, hormone |
| Behavior Code | Bảng hỏi, nhật ký, ví dụ | Pattern theo bối cảnh | Chẩn đoán lâm sàng |
| Social Fate Code | Gia đình, môi trường, nguồn lực | Điều kiện sống/cơ hội | Quy trách nhiệm số phận |
| Relationship Code | Nhu cầu, lịch sử tự thuật | Giao tiếp, ranh giới, plan | Phản bội/ly hôn từ tên/ảnh/ngày sinh |
| Wealth Code | Việc, thu-chi, nợ, tài sản | Kịch bản và giả định | Tư vấn đầu tư cá nhân tự động |
| Health Risk Code | Dữ liệu phù hợp, phạm vi chuyên môn | Lối sống và câu hỏi referral | Chẩn đoán hoặc dự báo bệnh từ hình thái |
| Mission Code | Giá trị, năng lực, việc đã làm | Hướng sống để thử nghiệm | Sứ mệnh duy nhất hoặc bắt buộc |

Face/Hand/Foot/Health không thuộc first paid beta.

---

## 8. Mười hai trường Đồng nhịp sống

Các trường: thực phẩm, nước, thời gian, nơi sống, thiên nhiên, âm thanh, con người, công việc, vận động, ngủ/phục hồi, môi trường số và ý nghĩa sống.

### 8.1 Data model của resonance

Mỗi observation cần:

```text
subject_id
field_id
occurred_at
context
user_reported_input
user_reported_response
optional_measurement
source
confidence_type
consent_scope
```

12 lớp x 12 trường là ma trận tổ chức câu hỏi, không phải 144 năng lượng đã được đo.

### 8.2 Output

- Nhật ký phù hợp/không phù hợp.
- Trend theo dữ liệu người dùng nhập.
- Thử nghiệm nhỏ có thời hạn.
- Review outcome.
- Referral khi vượt phạm vi sản phẩm.

Không tạo thực phẩm “hợp mệnh”, “địa khí chữa lành” hoặc health score từ ngày sinh.

---

## 9. Hợp đồng chín cấp sản phẩm

| Level | Mục tiêu | Input tăng thêm | Output MVP | Release condition |
|---|---|---|---|---|
| 1 Self Signal | Khởi đầu hiểu mình | Hồ sơ tối thiểu + mục tiêu | Dữ liệu gốc, phép tính truy ngược, câu hỏi, plan 30 ngày | P0-P4 đạt |
| 2 Inner Architecture | Động lực/xung đột | Vai trò, áp lực, tình huống | Giá trị-nhu cầu-vai trò, plan 90 ngày | Outcome + content review |
| 3 Behavior Code | Cách đang hành động | Hành vi và nhật ký | Pattern theo bối cảnh, experiment | Instrument governance |
| 4 Work & Wealth | Công việc/nguồn lực | Kỹ năng, thu-chi, ràng buộc | Role comparison, cashflow scenarios | Financial claim policy |
| 5 Relationship Field | Giao tiếp/ranh giới | Dữ liệu từng bên có consent | Needs, responsibilities, conversation plan | Sharing consent |
| 6 Life Timeline | Lịch sử và lựa chọn | Event có thời gian/nguồn | History, symbolic cycles, plan, scenario | Legacy timeline removed |
| 7 Body Intelligence | Cơ thể/môi trường | Ảnh/observation hợp lệ | Description, limits, lifestyle journal | DPIA + specialist review |
| 8 Mission Path | Hướng sống/phụng sự | Giá trị, năng lực có minh chứng | Options, experiment, 90-day plan | No destiny claims |
| 9 Full Life Code | Hồ sơ hợp nhất | Results được phép | Deduplicated living book | All included modules released |

Các level không bắt buộc mua tuần tự. Eligibility được tính bằng:

```text
product_entitlement
AND subject_access
AND valid_processing_purpose
AND released_methods
AND required_inputs_valid
```

Độ dài báo cáo là editorial budget, không phải bằng chứng về độ chính xác.

### 9.1 Các dòng sản phẩm bao quanh chín cấp

| Dòng sản phẩm | Phạm vi | Guardrail bắt buộc |
|---|---|---|
| Life Code Numbers | Tên, ngày sinh, chu kỳ số, Psychomatrix, Bát Cực, Mã đuôi 80 | Mỗi method có result riêng; không tự tạo “điểm SIM tổng hợp” |
| Life Code Companion | Nhật ký, mục tiêu, check-in, nhắc việc, giải thích báo cáo | Không cảnh báo mất tiền/sức khỏe từ symbolic signal |
| Life Code Family | Hồ sơ riêng, lịch và mục tiêu chung, chia sẻ theo phần | Guardian flow; không dán nhãn trẻ em |
| Life Code Practice | Case, lịch hẹn, ghi chú, draft và approval | Chuyên gia chỉ xem phần subject chia sẻ; mọi sửa đổi có history |
| Life Code Academy | Self-application, supervised practice, research/teaching | Chứng nhận nội bộ không thay bằng cấp chuyên môn |
| Life Code Workspace | Mục tiêu, vai trò, phối hợp và năng lực có minh chứng | Không dùng symbolic/health/private-life data để tuyển dụng hoặc sa thải |
| Life Code Publishing & API | Xuất bản và API có license | Dùng cùng method core; scope, quota, data right và branding rõ ràng |

Mobile giai đoạn đầu là responsive web dùng chung API và result snapshot. Native app chỉ mở khi notification, offline journal hoặc camera workflow tạo giá trị đủ lớn; không tạo một bộ công thức khác cho iOS/Android.

---

## 10. Data architecture

### 10.1 Account khác subject

```text
account -> subject -> access_grant -> purpose -> consent
```

Một account có thể quản lý chính mình, con được giám hộ hoặc subject ủy quyền. Người tải ảnh không mặc định là người trong ảnh và không mặc định có quyền chia sẻ.

### 10.2 Domain entities bắt buộc

| Domain | Entities |
|---|---|
| Identity | accounts, subjects, organizations, memberships, guardianships |
| Access | access_grants, roles, object_permissions, consent_records |
| Profile | profile_versions, data_hypotheses, source_assertions, birth_time_precision |
| Knowledge | methods, method_versions, sources, rights_register, term_registry |
| Observation | journals, events, resonance_observations, goals, resources |
| Analysis | analysis_runs, method_results, claims, missing_inputs, review_status |
| Product | products, product_requirements, orders, payments, entitlements |
| Reporting | report_snapshots, report_sections, approvals, export_artifacts |
| Action | plans, actions, check_ins, outcomes, reviews |
| Practice | practitioner_cases, shared_views, notes, appointments |
| Operations | jobs, idempotency_keys, audit_events, access_logs, deletion_jobs |

### 10.3 Dữ liệu mâu thuẫn

- Ngày sinh giấy tờ và ngày sinh thực tế là hai hypothesis, không ghi đè lẫn nhau.
- Thiếu ngày/tháng không được tự điền.
- Tên gốc được giữ; NFC normalization và chuỗi bỏ dấu là derivative riêng.
- Giờ sinh có precision và source.
- Timezone conversion lưu IANA tzdb version.

### 10.4 Result contract

```json
{
  "run_id": "...",
  "profile_version_id": "...",
  "method_id": "...",
  "method_version": "...",
  "result_type": "fact|self_report|observation|symbolic|metric|model_probability",
  "calculation": {},
  "score": null,
  "confidence": null,
  "probability": null,
  "missing_inputs": [],
  "limitations": [],
  "claims": [],
  "questions": [],
  "actions": [],
  "review_status": "draft"
}
```

---

## 11. LCI, metrics và timeline mới

### 11.1 Tách bốn loại chỉ số

| Loại | Ví dụ |
|---|---|
| Data completeness | Tỷ lệ trường bắt buộc đã có |
| Method coverage | Method xử lý được bao nhiêu input |
| Observed metric | Nhiệm vụ hoàn thành, overdue commitments, nhật ký, cashflow delta |
| Model probability | Xác suất của event được định nghĩa từ model đã đánh giá |

### 11.2 Legacy compatibility

- Giữ `raw_lci`, `normalized_lci`, `adjusted_lci` chỉ để migration/audit.
- Dữ liệu không có generation rule được gắn `legacy_experimental`.
- Component thiếu trả `null`, không dùng AI lấp điểm.
- Không cộng lại derived synthesis thành evidence độc lập.

### 11.3 Timeline bốn đường

| Track | Nội dung |
|---|---|
| History | Event đã xảy ra, nguồn và verification level |
| Symbolic cycle | Method output, convention và limitation |
| Plan | Việc người dùng dự định làm |
| Model forecast | Chỉ khi có target event, dataset, evaluation và applicability |

Legacy pseudo-random timeline phải bị loại khỏi production decision flow.

---

## 12. AI architecture và governance

### 12.1 AI được phép

- Truy xuất nguồn được cấp quyền.
- Giải thích calculation đã khóa.
- Phát hiện dữ liệu mâu thuẫn.
- Đề xuất câu hỏi bổ sung.
- Biên tập nội dung từ claim đã được phê duyệt.
- Tóm tắt nhật ký và hỗ trợ review plan.

### 12.2 AI bị cấm

- Tạo ngày sinh, sự kiện, tiểu sử hoặc consent còn thiếu.
- Tự đổi method table/rule/version.
- Tự tạo health/wealth/mission score.
- Biến model confidence thành calibrated probability.
- Nhận diện con người hoặc suy tính cách/đạo đức/bệnh từ ảnh.
- Tự phát hành báo cáo, cấp entitlement, trừ tiền hoặc hoàn tiền.

### 12.3 Pipeline

```text
Orchestrator
  -> deterministic tools
  -> authorized retrieval
  -> claim assembler
  -> writer
  -> policy reviewer
  -> human approval where required
```

### 12.4 Evidence log

Mỗi AI generation lưu:

- Model/provider alias, không lộ secret.
- Prompt template version.
- Input claim IDs.
- Retrieved source IDs.
- Policy decisions.
- Cost/latency/token usage.
- Reviewer outcome.
- Final content hash.

Không dùng dữ liệu dịch vụ để training nếu chưa có consent riêng và legal basis phù hợp.

---

## 13. Report and publishing system

### 13.1 Single content source

```text
profile/result snapshot
  -> approved claims
  -> structured report sections
  -> editorial review
  -> web/PDF/Word/EPUB renderers
```

### 13.2 Report section contract

Mỗi section có:

- Stable section ID.
- Purpose.
- Supporting data/result/claim IDs.
- Narrative blocks.
- Tables/figures.
- Limitations.
- Questions.
- Actions.
- Review state.

### 13.3 Bốn khối nội dung

| Khối | Nội dung |
|---|---|
| Identity | Dữ liệu gốc, tự mô tả, phạm vi, điều chưa biết |
| Analysis | Method result và pattern, phân biệt content type |
| Timeline | History, symbolic cycle, plan, forecast nếu đủ điều kiện |
| Action | Stop/start/protect/build, owner, deadline, outcome measure |

### 13.4 Export acceptance

- PDF có selectable text, bookmark, TOC, page number, internal link, Vietnamese font.
- Word dùng heading/table/TOC thật, không dựng cả trang bằng ảnh.
- Artifact lưu private, có retention và access audit.
- Không cam kết 600 trang hoặc thời gian render trước benchmark.

---

## 14. API groups và backward compatibility

OpenAPI là contract canonical. API v1 cũ chỉ tồn tại qua compatibility adapter có deprecation plan.

| API group | Chức năng |
|---|---|
| `/accounts`, `/subjects` | Account, subject, guardianship |
| `/profiles` | Profile version, hypothesis, source |
| `/consents`, `/access-grants` | Purpose, consent, sharing, revoke |
| `/methods` | Registry và released versions |
| `/journals`, `/observations` | Self-report và resonance data |
| `/analysis-runs` | Create, status, result, cancel |
| `/reports` | Draft, approve, export, download |
| `/plans`, `/actions`, `/check-ins` | Action system và outcome |
| `/catalog`, `/orders`, `/entitlements` | Commerce và access |
| `/practice` | Practitioner cases và shared views |
| `/admin` | Method/source/release/quality/cost/audit |

Mọi route nhận object ID phải enforce authorization trên object, không chỉ kiểm tra đăng nhập.

---

## 15. Commerce và entitlement

### 15.1 Revenue models

| Model | Contract |
|---|---|
| One-time report | Scope, snapshot, formats, revisions |
| Subscription companion | Usage limits, journals, check-ins, AI quota |
| Practitioner session | Provider, duration, responsibility, cancellation |
| Organization/API license | Seats, purpose, data rights, rate/cost limits |

### 15.2 Pricing inputs

```text
direct_cost = computation + AI + editorial + storage + support
price = direct_cost + risk_reserve + margin + taxes/fees
```

Không định giá chỉ bằng số trang. Không thu tiền để “giải số xấu”. Không thay rule để bán SIM/sản phẩm khác.

### 15.3 Entitlement requirements

- Payment success không tự đồng nghĩa report ready.
- Fulfillment có idempotency key.
- Missing input được giải thích trước thanh toán.
- Refund/cancel/dispute policy có state machine và audit.

---

## 16. Privacy, legal và rights workstream

### 16.1 Việt Nam

Legal/DPO phải rà soát theo hoạt động thực tế, tối thiểu:

- Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15, hiệu lực 2026-01-01.
- Nghị định 356/2025/NĐ-CP, hiệu lực 2026-01-01.
- Luật Bảo vệ quyền lợi người tiêu dùng 19/2023/QH15.
- Nghị định 85/2021/NĐ-CP về thương mại điện tử.
- Luật Khám bệnh, chữa bệnh 15/2023/QH15 cho ranh giới nội dung sức khỏe.

### 16.2 Children, biometric and health

- Guardian relationship và age-aware consent.
- Không dùng dữ liệu trẻ em để dán nhãn nghề nghiệp, thiên tài hoặc khó dạy.
- Ảnh mặc định private; không dùng facial recognition.
- Health content có scope, disclaimer và referral policy.
- Access to sensitive data được monitor và định kỳ review.

### 16.3 International

Nếu phục vụ EU hoặc subject tại EU:

- Rà soát GDPR role, lawful basis, international transfer và data subject rights.
- Rà soát AI Act classification và transparency obligation.
- Thông báo rõ khi người dùng tương tác với AI.

### 16.4 Rights register

Nguồn bên thứ ba phải phân biệt idea/method với expression, tables, translations và adaptations. Không ingest hoặc phát hành nội dung khi rights status chưa rõ.

### 16.5 Primary references

- Vietnam Personal Data Protection Law: <https://vanban.chinhphu.vn/?classid=1&docid=214590&pageid=27160&typegroupid=3>
- Decree 356/2025: <https://chinhphu.vn/?classid=1&docid=216387&orggroupid=2&pageid=27160>
- Consumer Protection Law: <https://vanban.chinhphu.vn/?docid=208363&pageid=27160>
- NIST AI RMF: <https://www.nist.gov/itl/ai-risk-management-framework>
- ISO/IEC 42001: <https://www.iso.org/standard/42001>
- OWASP API BOLA: <https://api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/>
- IANA timezone database: <https://www.iana.org/time-zones/tz-link>
- OpenAPI: <https://spec.openapis.org/oas/>
- WIPO copyright overview: <https://www.wipo.int/en/web/copyright/protection>
- Cloudflare Queues delivery guarantees: <https://developers.cloudflare.com/queues/reference/delivery-guarantees/>
- Cloudflare R2 presigned URLs: <https://developers.cloudflare.com/r2/api/s3/presigned-urls/>
- Unicode normalization: <https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/>
- O*NET content model: <https://www.onetcenter.org/content.html/content.html>
- IPIP items and scales: <https://www.ipip.ori.org/>
- EU AI Act enforcement/transparency milestone: <https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august>

Tài liệu này không thay opinion của luật sư hoặc DPO.

---

## 17. Security and operations baseline

### 17.1 Required controls

- Object-level authorization middleware and negative tests.
- Secret manager; no secret in repository or public client.
- Session rotation, expiry, revocation and token hashing.
- CSP, HSTS, restrictive CORS and secure cookies.
- Input validation, body/file limits and anti-automation controls.
- Private R2 and short-lived presigned URL.
- Immutable audit events for sensitive access and admin changes.
- Dependency/SAST/secret scan in CI.
- Backup, restore drill, RPO/RTO and rollback.
- Incident response and breach notification workflow.

### 17.2 Service objectives

Đặt SLO sau khi có baseline. Không công bố SLA trước khi đo. Mỗi service cần:

- Liveness và readiness khác nhau.
- Dependency health có timeout.
- Error budget.
- Alert owner.
- Runbook và rollback target.

### 17.3 Queue and job rules

Queues là at-least-once. Report generation, payment fulfillment, entitlement và deletion phải idempotent và có replay-safe state transition.

---

## 18. UX và accessibility

### 18.1 Entry flow

Màn hình đầu hỏi nhu cầu, không ép người dùng điền hồ sơ dài:

- Hiểu mình.
- Bộ số và tên.
- Công việc và nguồn lực.
- Quan hệ.
- Nhịp sống.
- Hồ sơ tổng hợp.

Trước mỗi field, hiển thị vì sao cần, bắt buộc/tùy chọn, retention và ai có thể xem.

### 18.2 Dashboard

Ưu tiên:

- Mục tiêu hiện tại.
- Ba hành động ưu tiên.
- Thay đổi từ lần trước.
- Dữ liệu cần bổ sung.
- Report/history.

Không đặt “đồng hồ nguy cơ cuộc đời” hoặc pseudo-probability ở trung tâm.

### 18.3 Proposed routes

```text
/app/profiles
/app/reports
/app/timeline
/app/actions
/app/resonance
/numbers
/academy
/practitioner
/research
```

Routes là target, không phải claim đã tồn tại.

### 18.4 Accessibility and localization

- WCAG 2.2 AA target cho core flows.
- Vietnamese-first terminology registry.
- English translation không đổi claim level.
- Date/time/name normalization không phá dữ liệu gốc.

---

## 19. Quality system

### 19.1 Năm bảng chất lượng

| Board | Gate |
|---|---|
| Method quality | Source, version, calculation, edge cases, limitations |
| Data quality | Correct subject, provenance, consent, no silent fill |
| Content quality | Claim IDs, no fabricated history, no filler |
| Software quality | Auth, payment, idempotency, recovery, export |
| Outcome quality | User understands, acts and can review change |

### 19.2 Golden test corpus

Tối thiểu gồm:

- Ngày sinh giấy tờ khác ngày sinh thực tế.
- Chỉ biết năm sinh.
- Giờ sinh không rõ và nhiều precision levels.
- Tên Unicode có dấu, không dấu và normalized variants.
- Ảnh xoay, thiếu metadata, không đúng subject.
- Mã đuôi 80 có số dư 0.
- Rule table version cũ/mới khác nhau.
- Profile/report access của subject khác.
- Retry queue và duplicate payment webhook.
- Delete request qua DB, R2, cache, search và backup policy.

### 19.3 Required test layers

- Unit tests cho rules.
- Property/edge tests cho calculation.
- Contract tests từ OpenAPI.
- Authorization matrix tests.
- Migration tests.
- Report snapshot tests.
- Accessibility tests.
- Staging E2E.
- Restore/rollback drill.
- Independent security and method review.

---

## 20. Roadmap theo exit evidence

### Phase P0 - Containment and provenance

**Thời lượng:** 48-72 giờ cho containment, 1-2 tuần để đóng gate.

**Owner:** Tech Lead + Security + Founder.

**Deliverables:**

- Legacy engine quarantine.
- Authorization hotfix design và negative tests.
- Session invalidation plan.
- Canonical repo/branch/deployed SHA receipt.
- Public claim inventory.
- Privacy intake freeze.

**Exit evidence:**

- Exact commit SHA và deployment ID.
- Unauthorized cross-object tests fail closed.
- Legacy endpoints không còn public decision output.
- Founder signs containment receipt.

### Phase A - Architecture and governance lock

**Thời lượng:** 2-3 tuần.

**Owner:** Founder/Product + Method Council + Legal/DPO + Architect.

**Deliverables:**

- Q1-Q12 decisions.
- Doctrine, terminology and claim policy.
- Product catalog and eligibility graph.
- Method/source/rights registry skeleton.
- Data classification and retention policy.

**Exit evidence:** Approved documents with owner, version, dependencies and change control.

### Phase B - Trust core

**Thời lượng:** 4-6 tuần.

**Owner:** Backend/Security/Data.

**Deliverables:**

- Account-subject-access-consent schema.
- Auth/session replacement.
- PostgreSQL migrations.
- Private R2 flow.
- Audit, export, correction and deletion workflows.
- OpenAPI baseline.

**Exit evidence:** Auth matrix green, migration rehearsal, deletion test, backup/restore and threat-model review.

### Phase C - First safe product

**Thời lượng:** 6-10 tuần.

**Owner:** Method Engineering + App + Content + QA.

**Scope:** Level 1, Numbers, selected K01/K10/K11/K12/K16-K20 components, reflection journal and 30-day plan.

**Exit evidence:**

- Method passports approved.
- Golden corpus green.
- Input-to-report staging E2E.
- No hardcoded user scores.
- Report every claim traceable to result/source.

### Phase D - Paid private beta

**Thời lượng:** 6-8 tuần.

**Owner:** Commerce + Reports + SRE + Support.

**Deliverables:** Structured report pipeline, PDF/Word, payment, entitlement, refund, support, monitoring and incident runbook.

**Exit evidence:** Payment-to-entitlement E2E, duplicate webhook test, restore drill, private pilot consent and rollback.

### Phase E - Life data expansion

**Thời lượng:** 3-5 tháng.

**Scope:** Levels 2-5, Resonance, Practitioner and Family foundations.

**Exit evidence:** Outcome measures, sharing consent, practitioner access review, method/content review for each level.

### Phase F - Unified Life Code OS

**Thời lượng:** 6-12 tháng sau paid beta.

**Scope:** Levels 6-9, Academy, Workspace, native mobile only if justified, partner API.

**Exit evidence:** Portfolio-level security, legal, cost and operations review; Founder release decision for each product line.

### Overall estimate

| Milestone | Estimate with staffed core team |
|---|---|
| Safe internal alpha | 3-4 months |
| Paid private beta | 4-6 months |
| Levels 1-5 with resonance/practice | 8-12 months |
| Full target vision | 12-18+ months |

Estimate assumes 6-8 core contributors plus Founder, method experts, Legal/DPO and editorial reviewers. It is not a fixed delivery commitment before staffing and source-rights audit.

---

## 21. Team topology and accountability

| Role | Accountability |
|---|---|
| Founder/Product Authority | Doctrine, product boundaries, Q decisions, final release authority |
| Method Council | Sources, rules, limitations, examples and method approval |
| Legal/DPO | Privacy, children, health, consumer, rights and international scope |
| Technical Lead | Canonical architecture, repo, release and integration |
| Security Engineer | AuthZ, threat model, secrets, incident and review |
| Data/Backend | PostgreSQL, migrations, API, queues, audit and deletion |
| Frontend/Product | Consent-aware UX, dashboard, accessibility and report views |
| AI/Knowledge | Retrieval, prompt/version, policy, reviewer and evidence log |
| Editorial/Report | Claim-safe narrative, templates, PDF/Word quality |
| QA/SRE | Test matrix, staging, observability, recovery and release receipt |

Mỗi workstream có một accountable owner. Không dùng nhiều lane song song mà không có integration owner.

---

## 22. Q1-Q12 đề xuất Founder duyệt

| Mã | Đề xuất | Mức bắt buộc |
|---|---|---|
| Q1 | Life Code là living profile và life design; probability chỉ ở model đủ điều kiện | Required |
| Q2 | Giữ 9 levels, 12 layers, 4 report blocks; thêm 12 resonance fields và K01-K20 registry | Required |
| Q3 | Method chạy riêng theo source/version; HNH synthesis không xóa provenance | Required |
| Q4 | Không bắt mua tuần tự; eligibility theo entitlement, access, purpose, method và input | Required |
| Q5 | Legacy LCI không tiếp tục tự gán điểm; component không hợp lệ trả null | P0 mandatory |
| Q6 | Numbers/80/Bát Cực là reference modules, không tự đo số phận/kết quả | Required |
| Q7 | Structured reports; không kéo dài giả tạo theo số trang | Required |
| Q8 | Companion/Family/Practice/Academy/Workspace/API mở theo gates | Required |
| Q9 | Privacy, delete, object authorization và child protection từ first product | P0 mandatory |
| Q10 | Xuất tám bộ execution docs sau architecture approval và source lock | Required |
| Q11 | Quarantine toàn bộ legacy risk/timeline/LCI output là experimental | P0 mandatory |
| Q12 | Không release method thiếu passport, rights, validation, limitations và approver | P0 mandatory |

---

## 23. Tám bộ tài liệu cần xuất sau Team Audit

| Bộ | Artifacts |
|---|---|
| 01 Philosophy/Scope | `LIFE_CODE_MASTER.md`, `HNH_DOCTRINE.md`, `TERMINOLOGY.md`, `CLAIM_POLICY.md` |
| 02 Product | `NINE_LEVELS.yaml`, `PRODUCT_CATALOG.yaml`, `ENTITLEMENTS.yaml`, `USER_JOURNEYS.md` |
| 03 Knowledge | `METHOD_REGISTRY.yaml`, `SOURCE_REGISTRY.csv`, `RIGHTS_REGISTER.csv`, glossary |
| 04 Data/Calculation | Profile/result schemas, scoring/timeline/resonance specs |
| 05 Technical | Architecture, OpenAPI, database, jobs/events, AI orchestration |
| 06 Reports | Content model, templates, editorial and export standards |
| 07 Security/Ops | Access, consent/retention, threat model, runbook, cost control |
| 08 Execution | Roadmap, backlog, test plan, acceptance and release checklist |

Mỗi artifact có ID, version, owner, status, dependencies, approver và definition of done.

---

## 24. Team Audit checklist

Team Audit không duyệt bằng cảm nhận. Yêu cầu trả verdict theo từng mục:

| Audit lane | Câu hỏi bắt buộc | Evidence cần có |
|---|---|---|
| Source | Repo/branch/HEAD/deployed SHA có khóa không? | Git + deployment receipt |
| Runtime | Live có đúng source và contract không? | Read-only probes + version endpoint |
| Method | Rule có source/version/test/limitation không? | Passport + golden corpus |
| Data | Account/subject/consent/purpose có tách không? | Schema + authorization matrix |
| Security | Object ID có owner/tenant check không? | Negative tests + review |
| Privacy | Intake/export/delete/retention có chạy E2E không? | DPIA + test receipts |
| AI | AI có bị chặn tạo facts/scores và auto-publish không? | Policy tests + evidence log |
| Report | Mỗi claim truy về source/result không? | Snapshot + claim graph |
| Commerce | Payment, entitlement, duplicate, refund có đúng không? | Sandbox/staging E2E |
| Operations | Backup/restore/rollback/incident có thử thật không? | Drill receipts |
| UX | Người dùng hiểu loại nội dung, limitation và action không? | Usability/accessibility test |
| Release | Independent review và Founder approval có đủ không? | Signed release packet |

### 24.1 Expected Team Audit output

Team Audit phải trả:

1. Ledger `VERIFIED_CURRENT / CONTRADICTED / NOT_CHECKED / BLOCKED`.
2. Findings theo P0-P3, có file/line hoặc runtime receipt.
3. Decision cho Q1-Q12.
4. Đề xuất thay đổi plan nếu có.
5. NO_GO/CONDITIONAL_GO/GO cho từng phase.
6. Danh sách evidence còn thiếu và owner.

Không sửa production, deploy, migrate hoặc truy cập PII thật trong vòng audit nếu chưa có scope riêng.

---

## 25. Release gates cuối cùng

Không được công bố production-ready cho tới khi có đủ:

1. Exact source SHA và deployment ID.
2. Canonical method/source/version registry.
3. Authorization and tenant/subject isolation tests.
4. Consent, export, correction, deletion and retention E2E.
5. Structured report with claim provenance.
6. Payment/entitlement/refund E2E.
7. Backup restore, rollback and incident drill.
8. Independent security review.
9. Independent method/content review.
10. Legal/DPO review for the actual launch scope.
11. Private pilot outcome and support readiness.
12. Explicit Founder release approval.

Local pass, document count, PDF quality, test smoke hoặc HTTP 200 không thay thế các gate này.

---

## 26. Kết luận

Life Code OS không nên được triển khai theo chuỗi:

```text
Nhiều môn -> AI luận dài -> xuất sách
```

Kiến trúc đích là:

```text
Tri thức có nguồn
-> dữ liệu đúng chủ thể và đúng quyền
-> method có version
-> kết quả phân loại đúng bản chất
-> HNH synthesis có giới hạn
-> lựa chọn theo bối cảnh
-> hành động
-> outcome được ghi nhận
-> hồ sơ tiếp tục trưởng thành
```

Điểm khác biệt không nằm ở số lượng môn hay độ dài báo cáo. Điểm khác biệt nằm ở provenance, khả năng sửa sai, quyền của người dùng, sự minh bạch giữa biểu tượng và dữ kiện, cùng vòng lặp biến hiểu biết thành hành động có thể xem lại.

Tài liệu này chỉ trở thành execution baseline sau khi Team Audit hoàn tất và Founder duyệt Q1-Q12.
