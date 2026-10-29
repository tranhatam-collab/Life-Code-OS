# Hợp đồng thực thi phương pháp và kết quả v2.1

Ngày bổ sung: **2026-10-20**  
Trạng thái: **PROPOSED / DESIGN_APPROVAL_PENDING / NOT_IMPLEMENTED**  
Phạm vi: đặc tả backend, không phải migration hoặc bằng chứng production.

## 1. Vì sao cần bản bổ sung

Bản 2026-10-11 đã đặt đúng nguyên tắc nhưng chưa đủ để một đội độc lập triển khai mà không tự điền phần còn thiếu:

- `MethodRelease` cho phép `permitted_for_product` khi mảng edition, product hoặc country vẫn rỗng; trạng thái kỹ thuật và trạng thái giá trị của phương pháp chưa tách nhau.
- `MethodResult.calculation` và `confidence` là object mở; `Metric.value` chưa có precision, scale hoặc rounding; một kết quả `complete` vẫn có thể mang `missing_inputs`.
- `ReportSnapshot` hỗ trợ nhiều subject trong OpenAPI, nhưng SQL 2026-10-11 chỉ giữ một `subject_id` và một `profile_version_id`.
- `ReleaseReceipt` có thể đạt `deployed_verified` mà không chốt method release nào; một trong hai receipt Worker/Pages là đủ dù release có thể cần cả hai artifact tương thích.
- SQL có `tenant.country_pack_id text` trong khi `country_pack.id` là UUID; payment-event uniqueness thiếu `merchant_account`; chưa có job/lease/DLQ, dependency giữa method/result, hoặc junction của report nhiều chủ thể.

Các điểm trên được giữ nguyên trong bản nguồn ở `docs/upgrade/sources/2026-10-11/package/04_Backend_API/`; bản này chỉ đưa ra hợp đồng thay thế có thể kiểm thử.

## 2. Ba trục độc lập của một method release

Không dùng một trường `status` để nói đồng thời “đã viết code”, “đúng theo một truyền thống”, “được kiểm chứng thực nghiệm” và “được phép bán”. Mỗi release phải có ba trục:

1. `computation_kind`
   - `deterministic`: cùng input đã chuẩn hóa + cùng config cho cùng output.
   - `symbolic`: phép biến đổi có thể tái lập, nhưng nội dung đầu ra chỉ là tượng nghĩa.
   - `observational`: tóm tắt dữ liệu người dùng/thiết bị, không suy quan hệ nhân quả.
   - `validated_model`: mô hình xác suất có target, horizon, population và evaluation receipt.
2. `evidence_class`
   - `unsourced_candidate`, `source_transcribed`, `rule_reproduced`, `instrument_evaluated`, `model_evaluated`.
   - Đây là provenance của rule/evaluation, không phải lời khẳng định chân lý về con người.
3. `release_state`
   - `research_only`, `specified`, `calculation_verified`, `content_reviewed`, `permitted_for_product`, `suspended`, `retired`.

Một phép tính biểu tượng có thể đạt `calculation_verified` vì tái lập đúng rule đã chốt, nhưng vẫn không được đổi thành `validated_model`. Một family K01–K20 không phải một method release. Sự tồn tại của family chỉ mở workstream nghiên cứu.

## 3. Registry và điều kiện phát hành

Registry canonical của bản nâng cấp là:

- `../02_Tri_thuc_HNH/METHOD_FAMILY_READINESS.json`: đủ K01–K20 và blocker thực tế.
- `../02_Tri_thuc_HNH/METHOD_RELEASE_REGISTRY_V2.json`: release cụ thể, không dùng family để lấp chỗ trống.
- `../02_Tri_thuc_HNH/SOURCE_RIGHTS_REGISTER.json`: nguồn, edition, locator, quyền và receipt.
- `../03_Du_lieu_Phep_tinh/FORMULA_CATALOG.json`: công thức/rule đã được ghi đủ hoặc trạng thái blocked.
- `../03_Du_lieu_Phep_tinh/METHOD_DEPENDENCY_MATRIX.json`: dependency input/source/release.
- `../03_Du_lieu_Phep_tinh/RESULT_CONTRACT_MATRIX.json`: loại result, null, metric và claim cho phép.

`permitted_for_product` chỉ hợp lệ khi **tất cả** điều kiện sau đúng:

```text
source_gate
∧ rights_gate
∧ immutable_rule_gate
∧ input_schema_gate
∧ output_schema_gate
∧ fixture_gate
∧ independent_review_gate
∧ product_scope_gate
∧ country_scope_gate
∧ claim_type_gate
∧ approval_gate
```

Trong đó:

- `source_gate`: có ít nhất một source record, edition và locator đủ tìm lại đoạn rule; “theo kiến thức phổ biến” không đạt.
- `rights_gate`: `permitted` với purpose, territory, channels, expiry và receipt; public URL không tự là quyền thương mại.
- `immutable_rule_gate`: rule spec, normalization policy và configuration đều có digest SHA-256.
- `fixture_gate`: có positive, boundary, invalid và metamorphic cases; test receipt trỏ đúng digest.
- `product_scope_gate`/`country_scope_gate`: danh sách không rỗng và khớp product/country release đang chạy.
- `approval_gate`: design approval và method/content/rights approval là các receipt tách biệt. Trạng thái hiện tại của gói vẫn là `PENDING`, không được nâng bằng tài liệu này.

Nếu một gate chưa có bằng chứng, API trả `method_not_released` hoặc `method_input_not_ready`; không chạy một implementation gần giống.

## 4. Formula specification bắt buộc

Mỗi formula/rule có:

| Trường | Yêu cầu |
|---|---|
| `formula_id`, `formula_version` | ID ổn định và SemVer hoặc phiên bản bất biến |
| `method_release_id` | release duy nhất sở hữu rule |
| `source_refs` | source + edition + locator + rights receipt |
| `input_contract` | type, normalization, unit, range, null/missing policy |
| `algorithm` | pseudocode không mơ hồ hoặc AST/rule table được hash |
| `configuration` | mọi variant; không dùng default ẩn |
| `numeric_policy` | integer/decimal, precision, scale, rounding, overflow |
| `time_policy` | calendar, civil time, timezone, tzdb, leap-day/DST policy |
| `output_contract` | type, unit, range, null reason, claim types |
| `fixtures` | exact expected output và expected error |
| `limitations` | điều không được suy ra |

Không chấp nhận code block trong tài liệu làm source của công thức. Code chỉ chứng minh implementation khớp đặc tả; source/rights/evidence phải đi qua registry riêng.

## 5. Null, unknown, unavailable và zero

Mọi trường optional phải theo một trong ba hình thức:

- Giá trị có mặt và hợp lệ.
- `null` kèm `missing_reason` từ enum có phiên bản.
- Trường không xuất hiện vì schema của result type không chứa trường đó.

`missing_reason` tối thiểu: `not_collected`, `not_permitted`, `not_applicable`, `insufficient_input`, `conflicting_input`, `unsupported_variant`, `source_not_verified`, `rights_not_permitted`, `method_not_released`, `division_by_zero`, `withdrawn`.

Không dùng `0`, chuỗi rỗng, ngày `1970-01-01`, `01/01` hoặc timezone hiện tại để thay unknown. `state=complete` yêu cầu `missing_inputs=[]` và `unresolved_rules=[]`; nếu còn phần thiếu thì dùng `partial` hoặc `blocked`.

## 6. Số, thập phân và tiền

- Count/index dùng integer có range cụ thể; input string dài phải có byte/character limit trước parse.
- Tiền lưu `amount_minor bigint` + ISO currency của release; không dùng float.
- Tỷ lệ và metric cần tái lập lưu decimal canonical string ở API và `numeric(p,s)` trong PostgreSQL. Contract phải chốt `scale` và `rounding` (`half_even`, `half_up`, `floor`, `ceiling`, `truncate`).
- JSON number chỉ dùng khi sai số nhị phân được chấp nhận và đã ghi rõ; không dùng nó cho tiền hoặc equality receipt.
- Mẫu số bằng 0 trả null + `division_by_zero`; không trả 0%.
- Range được kiểm tra ở schema và domain service. Score không có thang/ý nghĩa/chiều không được phát hành.

## 7. Ngày, giờ và timezone

Tách bốn khái niệm:

- `date`: ngày dân sự, không chuyển UTC.
- `local_time`: giờ được khai tại địa phương, chưa là instant.
- `timezone_id`: IANA zone như `Asia/Ho_Chi_Minh`; offset không thay zone.
- `instant`: RFC 3339 có offset, canonical lưu UTC.

Khi kết hợp ngày + giờ + zone phải giữ `tzdb_version` và policy cho local time không tồn tại/lặp do DST. Không tự chọn lần sớm/lần muộn. Ngày sinh thiếu giờ không được bù `00:00`. Tuổi là khoảng anniversary nửa mở; 29/02 phải ghi `feb28` hoặc `mar01` trong product/method configuration.

PostgreSQL dùng `date` cho civil date, `time` cho local time khi cần giữ nguyên, `timestamptz` cho instant, và `numeric` cho exact decimal. Đây là lựa chọn thiết kế, chưa xác nhận provider/version production.

## 8. Dependency và lineage

Hai đồ thị tách biệt:

1. Method dependency: release A cần release B, source, field hoặc policy nào. Chu trình bị từ chối trước publish.
2. Result dependency: result/claim/report dùng result, observation, profile version và grant snapshot nào. Xóa/withdraw phải truy ra artifact bị ảnh hưởng.

Mọi edge có `dependency_kind`, `required`, `purpose`, `introduced_in`, `retired_in`. Dependency optional không được biến mất khỏi trace; nó ghi `not_used` hoặc reason.

Result tối thiểu chốt: tenant, subject, profile version, run, method release, formula/config digest, input digest (không chứa raw PII), dependency IDs, calculation trace, metric/null semantics, claims, state và timestamp. Trace chỉ chứa dữ liệu tối thiểu; không ghi ảnh, tên đầy đủ hay nội dung đời tư vào log công khai.

## 9. Ma trận result theo loại

| `computation_kind` | Output | Probability | Confidence |
|---|---|---|---|
| deterministic | calculation/derived metric | luôn null | chỉ data quality/extraction nếu có schema |
| symbolic | symbolic map + reflection prompt | luôn null | mặc định null |
| observational | summary + sample/window | luôn null | data quality, không gọi causal confidence |
| validated_model | target probability | bắt buộc 0..1 | model calibration/evaluation receipt bắt buộc |

Claim `model_probability` cần đồng thời `model_release_id`, `target_event`, `horizon`, `population`, `evaluation_receipt_id` và `applicability_check=passed`. Không đủ một trường probability hợp range.

## 10. Nghiệm thu

- Registry bao phủ K01–K20 nhưng không làm tăng giả trạng thái release.
- Mỗi release được phép có source/edition/locator/rights/test/product/country/approver không rỗng.
- JSON Schema chặn mọi invalid state đã ghi trong audit 2026-10-20.
- Test metamorphic chứng minh input không liên quan không đổi output; test boundary/null/timezone/decimal có expected chính xác.
- OpenAPI giữ đủ 64 operation ID; mọi operation resolve tới policy trong `AUTHORIZATION_POLICY_MATRIX.json`.
- Không có method nào phát probability nếu không thuộc `validated_model`.
- Không có migration nào biến result legacy thành fact hoặc validated metric.

## Nguồn kỹ thuật chính

- OpenAPI 3.1.1: <https://spec.openapis.org/oas/v3.1.1.html>
- OpenAPI Overlay 1.2.0: <https://spec.openapis.org/overlay/latest.html>
- JSON Schema 2020-12 validation: <https://json-schema.org/draft/2020-12/json-schema-validation>
- PostgreSQL data types: <https://www.postgresql.org/docs/current/datatype.html>
- PostgreSQL date/time types: <https://www.postgresql.org/docs/current/datatype-datetime.html>
- IANA Time Zone Database: <https://www.iana.org/time-zones>

