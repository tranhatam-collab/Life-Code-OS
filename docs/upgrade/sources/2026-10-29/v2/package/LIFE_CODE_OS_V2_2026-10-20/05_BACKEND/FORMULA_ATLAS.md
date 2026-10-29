# Danh mục công thức, ma trận và điều kiện triển khai



**Ngày:** 20/10/2026. Bản tham chiếu có thể chạy khác với phương pháp đã được phê duyệt production.



## LCF-01 — Mã đuôi 80

**Công thức hoặc phép biến đổi:** r = N mod 80; q = floor(N / 80)

**Đầu vào:** Chuỗi đúng bốn chữ số ASCII và chính sách zero_policy.

**Đầu ra được hiểu thế nào:** Thương, số dư và mã tra trong bảng; không phải xác suất.

**Trường hợp biên:** Giữ nguyên số 0 đầu; số dư 0 mặc định chưa ánh xạ. Chỉ dùng as80 khi được chọn rõ; không tính qua số thực.

**Mã tham chiếu:** `06_DEMO_LAB/src/numbers.mjs`.

**Phạm vi liên hệ kế hoạch gốc:** M06. Không tự phê duyệt toàn bộ phương pháp gốc.

**Ví dụ DEMO-001:** Đuôi 6789 · quy tắc unmapped

```json

{"suffix":"6789","zero_policy":"unmapped"}

```

**Kỳ vọng cần kiểm tra:** `{"calculation":{"lookup_code":69}}`.

**Các ca liên quan:** DEMO-001, DEMO-002, DEMO-003, DEMO-004, DEMO-005, DEMO-006, DEMO-007, DEMO-008, DEMO-009.

**Trước khi áp dụng thật:** rà soát quy tắc, nguồn, quyền sử dụng, tích hợp quyền dữ liệu và kiểm thử staging. Không dùng test số học để tuyên bố đúng số phận.



## LCF-02 — Cặp số chồng lấn

**Công thức hoặc phép biến đổi:** p_i = (d_i, d_(i+1)), với i từ 0 đến n−2

**Đầu vào:** Chuỗi 2–32 chữ số; chọn strict hoặc bridge5_diagnostic.

**Đầu ra được hiểu thế nào:** Nhóm của từng cặp, phần chưa xử lý và độ bao phủ phép phân loại.

**Trường hợp biên:** Trong strict, cặp có 0 hoặc 5 chưa được gán nhóm. Cặp 55 không mặc nhiên là Phục vị.

**Mã tham chiếu:** `06_DEMO_LAB/src/numbers.mjs`.

**Phạm vi liên hệ kế hoạch gốc:** M07. Không tự phê duyệt toàn bộ phương pháp gốc.

**Ví dụ DEMO-010:** Chuỗi 1234 · giữ phần chưa biết

```json

{"digits":"1234","policy":"strict"}

```

**Kỳ vọng cần kiểm tra:** `{"calculation":{"known":3,"total":3,"counts":{"TM":1,"HH":1,"DN":1}}}`.

**Các ca liên quan:** DEMO-010, DEMO-011, DEMO-012, DEMO-013, DEMO-014, DEMO-015, DEMO-016.

**Trước khi áp dụng thật:** rà soát quy tắc, nguồn, quyền sử dụng, tích hợp quyền dữ liệu và kiểm thử staging. Không dùng test số học để tuyên bố đúng số phận.



## LCF-03 — Ma trận chữ số thô

**Công thức hoặc phép biến đổi:** count(k) = Σ I(d_i = k); tổng đường = Σ count(k)

**Đầu vào:** Chuỗi chữ số gốc theo phạm vi của công cụ.

**Đầu ra được hiểu thế nào:** Số lần xuất hiện của các chữ số và tổng tám đường; không đo năng lực con người.

**Trường hợp biên:** Không thêm các số làm việc khi chưa có quy tắc nguồn. Số 0 được ghi riêng.

**Mã tham chiếu:** `06_DEMO_LAB/src/numbers.mjs`.

**Phạm vi liên hệ kế hoạch gốc:** M08. Không tự phê duyệt toàn bộ phương pháp gốc.

**Ví dụ DEMO-017:** Đếm tần suất chữ số thô

```json

{"digits":"20000229"}

```

**Kỳ vọng cần kiểm tra:** `{"calculation":{"zero_count":4}}`.

**Các ca liên quan:** DEMO-017.

**Trước khi áp dụng thật:** rà soát quy tắc, nguồn, quyền sử dụng, tích hợp quyền dữ liệu và kiểm thử staging. Không dùng test số học để tuyên bố đúng số phận.



## LCF-04 — Đặc trưng dãy số

**Công thức hoặc phép biến đổi:** Tổng chữ số; căn rút gọn; nhóm lặp; tính đối xứng

**Đầu vào:** Chuỗi chữ số với giới hạn độ dài được kiểm tra.

**Đầu ra được hiểu thế nào:** Các thuộc tính của chuỗi, không phải điểm trí nhớ hoặc độ hợp mệnh.

**Trường hợp biên:** Chuỗi đối xứng không tự chứng minh dễ nhớ đối với người sử dụng.

**Mã tham chiếu:** `06_DEMO_LAB/src/numbers.mjs`.

**Phạm vi liên hệ kế hoạch gốc:** Mô-đun bổ sung. Không tự phê duyệt toàn bộ phương pháp gốc.

**Ví dụ DEMO-018:** Chuỗi đối xứng không phải số phận

```json

{"digits":"12344321"}

```

**Kỳ vọng cần kiểm tra:** `{"calculation":{"palindrome":true}}`.

**Các ca liên quan:** DEMO-018.

**Trước khi áp dụng thật:** rà soát quy tắc, nguồn, quyền sử dụng, tích hợp quyền dữ liệu và kiểm thử staging. Không dùng test số học để tuyên bố đúng số phận.



## LCF-05 — Quy đổi tên Latin có truy vết

**Công thức hoặc phép biến đổi:** value(c) = ((ord(c) − 65) mod 9) + 1, với c thuộc A–Z

**Đầu vào:** Tên Việt hoặc Latin; cấu hình chữ Y và cách giữ số đặc biệt.

**Đầu ra được hiểu thế nào:** Tổng từng từ, tổng tên, nguyên âm, phụ âm và chuỗi bước tính.

**Trường hợp biên:** Giữ tên gốc; chuẩn hóa NFC; quy đổi Đ thành D ở chuỗi dẫn xuất. Từ chối văn tự chưa được hỗ trợ.

**Mã tham chiếu:** `06_DEMO_LAB/src/names.mjs`.

**Phạm vi liên hệ kế hoạch gốc:** M02, M03. Không tự phê duyệt toàn bộ phương pháp gốc.

**Ví dụ DEMO-021:** Quy đổi có giữ nguyên tên: Đỗ An

```json

{"name":"Đỗ An"}

```

**Kỳ vọng cần kiểm tra:** `{"calculation":{"latin":"DO AN","sum":16,"vowel_sum":7,"consonant_sum":9}}`.

**Các ca liên quan:** DEMO-021, DEMO-022, DEMO-023, DEMO-024, DEMO-025, DEMO-026, DEMO-027, DEMO-028, DEMO-029.

**Trước khi áp dụng thật:** rà soát quy tắc, nguồn, quyền sử dụng, tích hợp quyền dữ liệu và kiểm thử staging. Không dùng test số học để tuyên bố đúng số phận.



## LCF-06 — Khoảng tuổi 0–99

**Công thức hoặc phép biến đổi:** [anniv(B, a), anniv(B, a+1))

**Đầu vào:** Ngày sinh ISO, ngày đối chiếu as_of và chính sách ngày nhuận.

**Đầu ra được hiểu thế nào:** 100 khoảng tuổi; danh sách sự kiện mặc định rỗng.

**Trường hợp biên:** Ngày 29/02 dùng chính sách feb28 hoặc mar01 đã chọn rõ. Không suy đoán tuổi thọ.

**Mã tham chiếu:** `06_DEMO_LAB/src/time.mjs`.

**Phạm vi liên hệ kế hoạch gốc:** M09. Không tự phê duyệt toàn bộ phương pháp gốc.

**Ví dụ DEMO-037:** Timeline 100 khoảng tuổi, không biến cố

```json

{"birth_date":"2000-02-29","as_of":"2026-10-20","leap_policy":"feb28"}

```

**Kỳ vọng cần kiểm tra:** `{"calculation":{"age_at_as_of":26}}`.

**Các ca liên quan:** DEMO-037, DEMO-038.

**Trước khi áp dụng thật:** rà soát quy tắc, nguồn, quyền sử dụng, tích hợp quyền dữ liệu và kiểm thử staging. Không dùng test số học để tuyên bố đúng số phận.



## LCF-07 — Quy đổi ngày sinh

**Công thức hoặc phép biến đổi:** all_digits hoặc reduced_components theo cấu hình

**Đầu vào:** Ngày sinh ISO, biến thể cộng và quy tắc rút gọn.

**Đầu ra được hiểu thế nào:** Tổng trung gian và từng bước rút gọn theo đúng cấu hình.

**Trường hợp biên:** Không trộn cách giữ 11, 22, 33 giữa các phương pháp.

**Mã tham chiếu:** `06_DEMO_LAB/src/time.mjs`.

**Phạm vi liên hệ kế hoạch gốc:** M04. Không tự phê duyệt toàn bộ phương pháp gốc.

**Ví dụ DEMO-030:** Ngày nhuận hợp lệ

```json

{"birth_date":"2000-02-29"}

```

**Kỳ vọng cần kiểm tra:** `{"calculation":{"raw_digit_sum":15}}`.

**Các ca liên quan:** DEMO-030, DEMO-031, DEMO-032, DEMO-033, DEMO-034.

**Trước khi áp dụng thật:** rà soát quy tắc, nguồn, quyền sử dụng, tích hợp quyền dữ liệu và kiểm thử staging. Không dùng test số học để tuyên bố đúng số phận.



## LCF-08 — Chu kỳ năm và tháng biểu tượng

**Công thức hoặc phép biến đổi:** r(r(ngày) + r(tháng) + r(tổng chữ số năm))

**Đầu vào:** Ngày sinh; năm xét; quy ước năm dương lịch hoặc từ sinh nhật; as_of khi cần.

**Đầu ra được hiểu thế nào:** Mã năm hoặc tháng theo quy ước, không phải sự kiện được dự báo.

**Trường hợp biên:** Giữ rõ chính sách chuyển năm và không gọi mã số là năm cưới, năm giàu hoặc năm tai họa.

**Mã tham chiếu:** `06_DEMO_LAB/src/time.mjs`.

**Phạm vi liên hệ kế hoạch gốc:** M05. Không tự phê duyệt toàn bộ phương pháp gốc.

**Ví dụ DEMO-035:** Chu kỳ biểu tượng theo năm dương lịch

```json

{"birth_date":"1990-03-14","year":2026,"month":10}

```

**Kỳ vọng cần kiểm tra:** `{"calculation":{"personal_year":9,"personal_month":1}}`.

**Các ca liên quan:** DEMO-035, DEMO-036.

**Trước khi áp dụng thật:** rà soát quy tắc, nguồn, quyền sử dụng, tích hợp quyền dữ liệu và kiểm thử staging. Không dùng test số học để tuyên bố đúng số phận.



## LCF-09 — Thời điểm UTC ứng viên từ giờ địa phương

**Công thức hoặc phép biến đổi:** Liệt kê độ lệch múi giờ; đối chiếu ngược về giờ địa phương

**Đầu vào:** Ngày, giờ địa phương và định danh múi giờ IANA.

**Đầu ra được hiểu thế nào:** Không có, một hoặc hai thời điểm UTC ứng viên trong các trường hợp minh họa.

**Trường hợp biên:** Phạm vi demo 1900–2100; ghi phiên bản Intl/ICU. Không thay thư viện lịch pháp hoặc thiên văn đầy đủ.

**Mã tham chiếu:** `06_DEMO_LAB/src/time.mjs`.

**Phạm vi liên hệ kế hoạch gốc:** M01. Không tự phê duyệt toàn bộ phương pháp gốc.

**Ví dụ DEMO-040:** Việt Nam · thời điểm duy nhất

```json

{"date":"2000-02-29","time":"04:25","time_zone":"Asia/Ho_Chi_Minh"}

```

**Kỳ vọng cần kiểm tra:** `{"calculation":{"state":"exact"}}`.

**Các ca liên quan:** DEMO-040, DEMO-041, DEMO-042, DEMO-043, DEMO-044.

**Trước khi áp dụng thật:** rà soát quy tắc, nguồn, quyền sử dụng, tích hợp quyền dữ liệu và kiểm thử staging. Không dùng test số học để tuyên bố đúng số phận.



## LCF-10 — So sánh giả thuyết ngày sinh

**Công thức hoặc phép biến đổi:** Tính độc lập cho từng giả thuyết, không trộn đầu vào

**Đầu vào:** Từ hai đến năm phương án có ID và ngày ISO hợp lệ.

**Đầu ra được hiểu thế nào:** Kết quả riêng cho mỗi phương án; selected mặc định là null.

**Trường hợp biên:** Không lấy trung bình ngày sinh và không tự chọn phương án vì lời diễn giải hấp dẫn hơn.

**Mã tham chiếu:** `06_DEMO_LAB/src/time.mjs`.

**Phạm vi liên hệ kế hoạch gốc:** M01. Không tự phê duyệt toàn bộ phương pháp gốc.

**Ví dụ DEMO-039:** Hai phương án năm sinh giữ riêng

```json

{"hypotheses":[{"id":"paper","birth_date":"1970-05-10"},{"id":"family","birth_date":"1972-05-10"}]}

```

**Kỳ vọng cần kiểm tra:** `{"calculation":{"selected":null}}`.

**Các ca liên quan:** DEMO-039.

**Trước khi áp dụng thật:** rà soát quy tắc, nguồn, quyền sử dụng, tích hợp quyền dữ liệu và kiểm thử staging. Không dùng test số học để tuyên bố đúng số phận.



## LCF-11 — Độ đầy đủ đầu vào

**Công thức hoặc phép biến đổi:** Σ(trọng số máy chủ × có dữ liệu) / Σ(trọng số máy chủ)

**Đầu vào:** Mã phiên bản sản phẩm và danh sách trường đầu vào hợp lệ.

**Đầu ra được hiểu thế nào:** Tỷ lệ dữ liệu đã có trong phạm vi sản phẩm; không phải độ chính xác về cuộc đời.

**Trường hợp biên:** Mẫu số do máy chủ khóa; điểm và trọng số tự gửi từ client bị từ chối.

**Mã tham chiếu:** `06_DEMO_LAB/src/metrics.mjs`.

**Phạm vi liên hệ kế hoạch gốc:** Mô-đun bổ sung. Không tự phê duyệt toàn bộ phương pháp gốc.

**Ví dụ DEMO-045:** Coverage lấy mẫu số từ registry

```json

{"product_release":"self-signal.demo.2","valid_field_ids":["name"]}

```

**Kỳ vọng cần kiểm tra:** `{"calculation":{"numerator":1,"denominator":3}}`.

**Các ca liên quan:** DEMO-045, DEMO-046.

**Trước khi áp dụng thật:** rà soát quy tắc, nguồn, quyền sử dụng, tích hợp quyền dữ liệu và kiểm thử staging. Không dùng test số học để tuyên bố đúng số phận.



## LCF-12 — Tiến độ công việc đến hạn

**Công thức hoặc phép biến đổi:** Số việc hoàn thành đến hạn / số việc không hủy đến hạn trong cửa sổ

**Đầu vào:** Danh sách công việc và khoảng ngày đối chiếu.

**Đầu ra được hiểu thế nào:** Số việc đủ điều kiện, số hoàn thành và tỷ lệ nếu mẫu số khác 0.

**Trường hợp biên:** Loại việc hủy và việc ngoài cửa sổ; mẫu số 0 trả null, không giả thành 100%.

**Mã tham chiếu:** `06_DEMO_LAB/src/metrics.mjs`.

**Phạm vi liên hệ kế hoạch gốc:** M10. Không tự phê duyệt toàn bộ phương pháp gốc.

**Ví dụ DEMO-047:** Tiến độ có thời hạn và quy tắc hủy

```json

{"actions":[{"id":"A1","due_on":"2026-10-21","state":"done"},{"id":"A2","due_on":"2026-10-22","state":"scheduled"},{"id":"A3","due_on":"2026-10-23","state":"cancelled"},{"id":"A4","due_on":"2026-11-01","state":"done"}],"window_start":"2026-10-20","window_end":"2026-10-30"}

```

**Kỳ vọng cần kiểm tra:** `{"calculation":{"completed":1,"due":2,"ratio":0.5}}`.

**Các ca liên quan:** DEMO-047, DEMO-048.

**Trước khi áp dụng thật:** rà soát quy tắc, nguồn, quyền sử dụng, tích hợp quyền dữ liệu và kiểm thử staging. Không dùng test số học để tuyên bố đúng số phận.



## LCF-13 — Dòng tiền theo đơn vị nhỏ nhất

**Công thức hoặc phép biến đổi:** Tổng tiền vào − tổng tiền ra, tách theo từng loại tiền

**Đầu vào:** Mã tiền tệ và các số tiền ở dạng chuỗi số nguyên của đơn vị nhỏ nhất.

**Đầu ra được hiểu thế nào:** Tổng thu, tổng chi và chênh lệch, được trả dưới dạng chuỗi.

**Trường hợp biên:** Dùng BigInt; không cộng lẫn các loại tiền hoặc tự quy đổi tỷ giá. Không dự báo lợi nhuận.

**Mã tham chiếu:** `06_DEMO_LAB/src/metrics.mjs`.

**Phạm vi liên hệ kế hoạch gốc:** M13. Không tự phê duyệt toàn bộ phương pháp gốc.

**Ví dụ DEMO-049:** Dòng tiền số nguyên · không dự báo

```json

{"currency":"VND","entries":[{"currency":"VND","kind":"inflow","minor_units":"12000000"},{"currency":"VND","kind":"outflow","minor_units":"7500000"}]}

```

**Kỳ vọng cần kiểm tra:** `{"calculation":{"net_minor":"4500000"}}`.

**Các ca liên quan:** DEMO-049, DEMO-050.

**Trước khi áp dụng thật:** rà soát quy tắc, nguồn, quyền sử dụng, tích hợp quyền dữ liệu và kiểm thử staging. Không dùng test số học để tuyên bố đúng số phận.



## LCF-14 — Tổng hợp nhật ký tự khai

**Công thức hoặc phép biến đổi:** Số quan sát, trung bình và trung vị theo từng trường

**Đầu vào:** Ngày, mã trường môi trường và điểm tự khai từ 0 đến 10.

**Đầu ra được hiểu thế nào:** Thống kê mô tả những quan sát người dùng đã nhập.

**Trường hợp biên:** Không suy ra quan hệ nhân quả, hiệu quả điều trị hoặc thang đo sinh học.

**Mã tham chiếu:** `06_DEMO_LAB/src/metrics.mjs`.

**Phạm vi liên hệ kế hoạch gốc:** Mô-đun bổ sung. Không tự phê duyệt toàn bộ phương pháp gốc.

**Ví dụ DEMO-051:** Đồng nhịp · mô tả cảm nhận không suy nhân quả

```json

{"observations":[{"date":"2026-10-17","field":"work","rating":6},{"date":"2026-10-18","field":"work","rating":8},{"date":"2026-10-19","field":"sound","rating":4}]}

```

**Kỳ vọng cần kiểm tra:** `{"calculation":{"summaries":[{"field":"work","count":2,"sum":14,"mean":7,"median":7},{"field":"sound","count":1,"sum":4,"mean":4,"median":4}]}}`.

**Các ca liên quan:** DEMO-051.

**Trước khi áp dụng thật:** rà soát quy tắc, nguồn, quyền sử dụng, tích hợp quyền dữ liệu và kiểm thử staging. Không dùng test số học để tuyên bố đúng số phận.



## LCF-15 — So sánh tiêu chí do người dùng chọn

**Công thức hoặc phép biến đổi:** Σ(trọng số × điểm tiêu chí) / 100

**Đầu vào:** Bộ tiêu chí có tổng trọng số 100 và điểm của từng phương án.

**Đầu ra được hiểu thế nào:** Điểm ưu tiên có trọng số và phần dữ liệu còn thiếu.

**Trường hợp biên:** Thiếu dữ liệu chặn xếp hạng toàn bộ; không tự chuẩn hóa lại mẫu số để làm đẹp kết quả.

**Mã tham chiếu:** `06_DEMO_LAB/src/metrics.mjs`.

**Phạm vi liên hệ kế hoạch gốc:** Mô-đun bổ sung. Không tự phê duyệt toàn bộ phương pháp gốc.

**Ví dụ DEMO-052:** Ma trận ưu tiên do người dùng lựa chọn

```json

{"criteria":[{"id":"cost","weight":40},{"id":"time","weight":60}],"options":[{"id":"A","values":{"cost":70,"time":80}},{"id":"B","values":{"cost":90,"time":60}}]}

```

**Kỳ vọng cần kiểm tra:** `{"calculation":{"ranking_allowed":true}}`.

**Các ca liên quan:** DEMO-052, DEMO-053.

**Trước khi áp dụng thật:** rà soát quy tắc, nguồn, quyền sử dụng, tích hợp quyền dữ liệu và kiểm thử staging. Không dùng test số học để tuyên bố đúng số phận.



## LCF-16 — Biến đổi sáu hào

**Công thức hoặc phép biến đổi:** Quẻ biến = quẻ gốc XOR mặt nạ hào động

**Đầu vào:** Sáu bit từ dưới lên; 0 là âm, 1 là dương; các hào động 1–6 không trùng.

**Đầu ra được hiểu thế nào:** Cấu trúc quẻ gốc, quẻ biến và chỉ số nhị phân.

**Trường hợp biên:** Chỉ số nhị phân không phải thứ tự Văn Vương. Demo không kèm tên quẻ hoặc lời quẻ chưa được khóa nguồn.

**Mã tham chiếu:** `06_DEMO_LAB/src/symbolic.mjs`.

**Phạm vi liên hệ kế hoạch gốc:** Mô-đun bổ sung. Không tự phê duyệt toàn bộ phương pháp gốc.

**Ví dụ DEMO-054:** Biến đổi sáu hào từ dưới lên

```json

{"lines_bottom_up":[1,0,0,0,1,0],"changing_lines":[6]}

```

**Kỳ vọng cần kiểm tra:** `{"calculation":{"changed_lines":[1,0,0,0,1,1]}}`.

**Các ca liên quan:** DEMO-054.

**Trước khi áp dụng thật:** rà soát quy tắc, nguồn, quyền sử dụng, tích hợp quyền dữ liệu và kiểm thử staging. Không dùng test số học để tuyên bố đúng số phận.



## Các adapter chưa được triển khai đầy đủ



| Mã | Phạm vi | Điều còn thiếu |
|---|---|---|
| SPEC-BAZI_PILLARS | Bát tự bốn trụ | Tiết khí, múi giờ lịch sử, ranh giới ngày và chính sách trường phái. |
| SPEC-BAZI_STRENGTH | Vượng–suy/dụng thần | Quy tắc nguồn, ví dụ độc lập và cách xử lý khác biệt trường phái. |
| SPEC-ZIWEI_PLACEMENT | Tử Vi an sao | Lịch âm, tháng nhuận, quy tắc an Mệnh, cục và hệ sao. |
| SPEC-ZIWEI_CYCLES | Đại hạn/tiểu hạn | Cách tính tuổi và chính sách chu kỳ theo trường phái. |
| SPEC-WESTERN_ASTRO | Thiên thể và hệ nhà | Giấy phép và phiên bản ephemeris; múi giờ; cấu hình hệ nhà. |
| SPEC-JYOTISH_DASHA | Jyotish và daśā | Ayanāṃśa, nakshatra và phiên bản các quy tắc daśā. |
| SPEC-QIMEN_BOARD | Kỳ Môn lập bàn | Quy tắc lập cục, tiết khí và nguồn tham chiếu. |
| SPEC-LIUYAO_RELATIONS | Lục Hào | Nguồn lấy quẻ, quy tắc lục thân, Thế–Ứng và ngày tháng. |
| SPEC-NAME_NON_LATIN | Tên ngoài Latin | Văn tự gốc, cách đọc, bảng quy đổi và người rà soát bản ngữ. |
| SPEC-NADI_LIBRARY | Kho Nadi | Bản thảo có quyền sử dụng; không giả định đã có mọi cuộc đời. |
| SPEC-IMAGE_MEASURE | Quan sát hình thái | Quyền xử lý ảnh, điều kiện chụp và hiệu chỉnh; không suy nhân cách từ hình thái. |
| SPEC-VOICE_MEASURE | Quan sát giọng nói | Quyền xử lý âm thanh, microphone và hiệu chỉnh tín hiệu; không suy đạo đức. |
| SPEC-BEHAVIOR_INSTRUMENT | Thang hành vi phù hợp | Quyền sử dụng, bản dịch, cách chấm và đánh giá phạm vi áp dụng. |
| SPEC-OUTCOME_PROBABILITY | Xác suất mục tiêu cụ thể | Mục tiêu dự báo, thời hạn, nhóm áp dụng, hiệu chỉnh và đánh giá độc lập. |
| SPEC-RLS_POSTGRES | Phân quyền cơ sở dữ liệu thực tế | Tài khoản runtime, chính sách và kiểm thử từ chối truy cập trên staging. |
| SPEC-OUTBOX_DURABLE | Idempotency bền vững | Giao dịch cơ sở dữ liệu, ràng buộc duy nhất, lease và đối soát tác vụ. |
