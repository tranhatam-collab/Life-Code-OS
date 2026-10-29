# Hợp đồng kết quả, chỉ số và cách xử lý điều chưa biết

Mã tài liệu: **D11** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Method Engineering + Data. Nguồn đối chiếu: G05, S14. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Sáu loại nội dung
fact: dữ kiện có nguồn và phạm vi xác nhận; self_report: người dùng kể; observation: quan sát của công cụ/người kèm điều kiện; symbolic_interpretation: tượng nghĩa theo phương pháp; derived_metric: đại lượng tính có định nghĩa; model_probability: xác suất từ mô hình được phép. Kết quả phép chia có thể là derived_metric; lời “mã 71 gợi giữ thành quả” là symbolic_interpretation. Hai loại không được gộp.
## 2. Optional không có nghĩa tùy tiện
score có thể không xuất hiện hoặc null. Khi có phải kèm metric_id, scale_min/max, direction, unit, formula_version và observation_window. Confidence phải có confidence_kind: extraction, data_quality hoặc model_calibration; không dùng một 0,9 chung cho mọi thứ. Probability chỉ được khác null khi result_type=model_probability và có approved_model_release, target_event, horizon, population, evaluation_receipt và applicability check.
Schema là lớp đầu; server còn phải tra model registry để xác nhận version thực sự đã được phê duyệt. Một client tự điền model_release_id không đủ mở cổng. Unknown và zero là khác nhau: không có dữ liệu tài chính không bằng tài chính 0 điểm.
## 3. Coverage không do client định nghĩa
Mẫu số do product release khai báo yêu cầu. Chỉ tính trường phù hợp mục đích và được phép sử dụng. Server bỏ qua mảng weight hoặc score do client tự gửi. Hiển thị riêng input_coverage và method_coverage. Một method có ba cặp không xử lý phải trả unresolved_pairs; không loại chúng khỏi giao diện để làm điểm đẹp.
## 4. Cách ly LCI cũ
raw_lci/normalized_lci/adjusted_lci cũ chỉ tồn tại trong compatibility object experimental_legacy. Không dùng nó để unlock, quyết định giá, xếp người hoặc tạo risk. Báo cáo mới không yêu cầu một điểm toàn đời. Nếu nghiên cứu LCI mới, cần định nghĩa cấu trúc cần đo, data requirements, tính trùng, xử lý missingness và đối tượng sử dụng trước.
## 5. Chỉ số thực hành có thể mở sớm
Task completion = completed_due_tasks / due_tasks với cửa sổ và quy tắc hủy rõ; mẫu số 0 trả null. Observation coverage = observed_days / planned_days. Cashflow = inflows minus outflows theo đơn vị tiền và kỳ tự khai, không so sánh hai tiền tệ nếu không có tỷ giá và ngày. Không gọi những chỉ số này là vận mệnh.
## 6. Sửa sai
Result bất biến theo method release; chỉnh công thức tạo result mới. Diff giải thích field nào đổi và vì sao. Chấm “không phù hợp” giữ trong feedback, không tự tăng/giảm trọng số chung. Không làm đẹp score trước khi Founder duyệt.

## Amendment 2026-10-20 — invariant máy chủ

1. `Metric.value=null` bắt buộc có `missing_reason`; giá trị không null phải nằm trong scale đã khai báo. `percent` dùng 0–100, `ratio` dùng 0–1. So sánh `value` với `scale_min/max` và kiểm soát số chữ số thập phân là invariant runtime vì JSON Schema không biểu diễn được đầy đủ quan hệ này.
2. Tiền tệ không dùng binary floating point. Backend lưu decimal hoặc minor unit cùng ISO-4217 currency, scale, rounding mode, period và `as_of`; không cộng chéo currency khi thiếu FX source/date.
3. `confidence` nếu có phải có kind, value, meaning và evidence IDs; symbolic map bắt buộc null. `probability` chỉ khác null cho `approved_model`, kèm model release, target, horizon, population, evaluation receipt và applicability check.
4. `state=complete` bắt buộc `missing_inputs=[]` và `unresolved_rules=[]`. `blocked` phải có lý do máy đọc được. Claim không có source/lineage không được xuất bản.
5. JSON Schema chỉ kiểm hình dạng. Các quan hệ chéo — cùng subject/tenant, claim thuộc result, section claim là tập con của report, arithmetic identity, release có trong registry và rights còn hiệu lực — phải được backend kiểm lại trong cùng transaction/snapshot.
6. Contract hiện hành được đối chiếu bằng `RESULT_CONTRACT_MATRIX.json`; dependency input/result bằng `METHOD_DEPENDENCY_MATRIX.json`; công thức chỉ lấy từ `FORMULA_CATALOG.json`.
