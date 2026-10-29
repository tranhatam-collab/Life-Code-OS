# Thư viện 90 tình huống minh họa

Mỗi ca dùng dữ liệu tổng hợp. Lỗi được kỳ vọng là một kết quả đúng của kiểm soát, không phải lỗi phải né để tạo lời luận. Input đầy đủ nằm trong `06_DEMO_LAB/data/demo-cases.json`; output thật của lần chạy nằm trong `receipts/demo-results.json`.

| Mã | Nhóm / công cụ | Tình huống | Kỳ vọng |
|---|---|---|---|
| DEMO-001 | Bộ số / `tail80` | Đuôi 6789 · quy tắc unmapped | {"calculation":{"lookup_code":69}} |
| DEMO-002 | Bộ số / `tail80` | Đuôi 0000 · quy tắc unmapped | {"calculation":{"lookup_code":null}} |
| DEMO-003 | Bộ số / `tail80` | Đuôi 0080 · quy tắc as80 | {"calculation":{"lookup_code":80}} |
| DEMO-004 | Bộ số / `tail80` | Đuôi 0001 · quy tắc unmapped | {"calculation":{"lookup_code":1}} |
| DEMO-005 | Bộ số / `tail80` | Đuôi 9999 · quy tắc unmapped | {"calculation":{"lookup_code":79}} |
| DEMO-006 | Bộ số / `tail80` | Đuôi 6231 · quy tắc unmapped | {"calculation":{"lookup_code":71}} |
| DEMO-007 | Bộ số / `tail80` | Đuôi 1986 · quy tắc unmapped | {"calculation":{"lookup_code":66}} |
| DEMO-008 | Bộ số / `tail80` | Đuôi 3468 · quy tắc unmapped | {"calculation":{"lookup_code":28}} |
| DEMO-009 | Bộ số / `tail80` | Đầu vào ba chữ số phải bị từ chối | INVALID_SUFFIX |
| DEMO-010 | Bộ số / `pairs` | Chuỗi 1234 · giữ phần chưa biết | {"calculation":{"known":3,"total":3,"counts":{"TM":1,"HH":1,"DN":1}}} |
| DEMO-011 | Bộ số / `pairs` | Chuỗi 1819 · giữ phần chưa biết | {"calculation":{"known":3,"total":3,"counts":{"NQ":2,"DN":1}}} |
| DEMO-012 | Bộ số / `pairs` | Chuỗi 1413 · giữ phần chưa biết | {"calculation":{"known":3,"total":3,"counts":{"SK":2,"TY":1}}} |
| DEMO-013 | Bộ số / `pairs` | Chuỗi 5555 · giữ phần chưa biết | {"calculation":{"known":0,"total":3}} |
| DEMO-014 | Bộ số / `pairs` | Chuỗi 8553 · giữ phần chưa biết | {"calculation":{"known":0,"total":3}} |
| DEMO-015 | Bộ số / `pairs` | Chuỗi 0000 · giữ phần chưa biết | {"calculation":{"known":0,"total":3}} |
| DEMO-016 | Bộ số / `pairs` | Nối qua 5 chỉ để đối chiếu độ nhạy | {"calculation":{"evaluated_digits":"83","known":1}} |
| DEMO-017 | Bộ số / `digit_matrix` | Đếm tần suất chữ số thô | {"calculation":{"zero_count":4}} |
| DEMO-018 | Bộ số / `sequence` | Chuỗi đối xứng không phải số phận | {"calculation":{"palindrome":true}} |
| DEMO-019 | Bộ số / `phone` | Ký hiệu nội địa | {"canonical":"0900000001"} |
| DEMO-020 | Bộ số / `phone` | Ký hiệu quốc tế cùng chuỗi nội địa | {"canonical":"0900000001"} |
| DEMO-021 | Tên / `name` | Quy đổi có giữ nguyên tên: Đỗ An | {"calculation":{"latin":"DO AN","sum":16,"vowel_sum":7,"consonant_sum":9}} |
| DEMO-022 | Tên / `name` | Quy đổi có giữ nguyên tên: ĐỖ AN | {"calculation":{"latin":"DO AN","sum":16,"vowel_sum":7,"consonant_sum":9}} |
| DEMO-023 | Tên / `name` | Quy đổi có giữ nguyên tên: Lê Bình | {"calculation":{"latin":"LE BINH","sum":32,"vowel_sum":14,"consonant_sum":18}} |
| DEMO-024 | Tên / `name` | Quy đổi có giữ nguyên tên: Nguyễn An | {"calculation":{"latin":"NGUYEN AN","sum":38,"vowel_sum":9,"consonant_sum":29}} |
| DEMO-025 | Tên / `name` | Quy đổi có giữ nguyên tên: Demo An | {"calculation":{"latin":"DEMO AN","sum":25,"vowel_sum":12,"consonant_sum":13}} |
| DEMO-026 | Tên / `name` | Y được tính như nguyên âm theo lựa chọn | {"calculation":{"vowel_sum":8}} |
| DEMO-027 | Tên / `name` | Y không tính như nguyên âm | {"calculation":{"vowel_sum":1}} |
| DEMO-028 | Tên / `name` | Không ép chữ Hán vào bảng Latin | UNSUPPORTED_SCRIPT |
| DEMO-029 | Tên / `name` | Ký tự điều khiển bị từ chối | INVALID_NAME |
| DEMO-030 | Ngày và lịch / `birth` | Ngày nhuận hợp lệ | {"calculation":{"raw_digit_sum":15}} |
| DEMO-031 | Ngày và lịch / `birth` | Ngày không tồn tại | INVALID_INTEGER |
| DEMO-032 | Ngày và lịch / `birth` | Không đoán định dạng ngày | INVALID_DATE |
| DEMO-033 | Ngày và lịch / `birth` | Giữ số 11/22/33 khi được chọn | {"calculation":{"raw_digit_sum":24,"calculation_sum":24,"reduction":{"value":6,"root":6}}} |
| DEMO-034 | Ngày và lịch / `birth` | Đối chiếu cộng theo thành phần | {"calculation":{"raw_digit_sum":24,"calculation_sum":33,"reduction":{"value":33,"root":6}}} |
| DEMO-035 | Ngày và lịch / `cycle` | Chu kỳ biểu tượng theo năm dương lịch | {"calculation":{"personal_year":9,"personal_month":1}} |
| DEMO-036 | Ngày và lịch / `cycle` | Chu kỳ theo sinh nhật trước ngày chuyển | {"calculation":{"effective_year":2025}} |
| DEMO-037 | Ngày và lịch / `timeline` | Timeline 100 khoảng tuổi, không biến cố | {"calculation":{"age_at_as_of":26}} |
| DEMO-038 | Ngày và lịch / `timeline` | Ngày nhuận chọn mốc 01/03 | {"calculation":{"age_at_as_of":24}} |
| DEMO-039 | Ngày và lịch / `hypotheses` | Hai phương án năm sinh giữ riêng | {"calculation":{"selected":null}} |
| DEMO-040 | Múi giờ / `time` | Việt Nam · thời điểm duy nhất | {"calculation":{"state":"exact"}} |
| DEMO-041 | Múi giờ / `time` | Berlin · giờ lặp lại cần lựa chọn | {"calculation":{"state":"ambiguous"}} |
| DEMO-042 | Múi giờ / `time` | Berlin · giờ không tồn tại | {"calculation":{"state":"nonexistent"}} |
| DEMO-043 | Múi giờ / `time` | New York · giờ lặp lại | {"calculation":{"state":"ambiguous"}} |
| DEMO-044 | Múi giờ / `time` | Múi giờ chưa được cung cấp | TIMEZONE_REQUIRED |
| DEMO-045 | Quan sát / `coverage` | Coverage lấy mẫu số từ registry | {"calculation":{"numerator":1,"denominator":3}} |
| DEMO-046 | Quan sát / `coverage` | Client không được đặt lại trọng số | CLIENT_SCORES_FORBIDDEN |
| DEMO-047 | Quan sát / `actions` | Tiến độ có thời hạn và quy tắc hủy | {"calculation":{"completed":1,"due":2,"ratio":0.5}} |
| DEMO-048 | Quan sát / `actions` | Không có việc đến hạn trả null | {"calculation":{"ratio":null}} |
| DEMO-049 | Quan sát / `cashflow` | Dòng tiền số nguyên · không dự báo | {"calculation":{"net_minor":"4500000"}} |
| DEMO-050 | Quan sát / `cashflow` | Không cộng lẫn VND và USD | MIXED_CURRENCY |
| DEMO-051 | Quan sát / `resonance` | Đồng nhịp · mô tả cảm nhận không suy nhân quả | {"calculation":{"summaries":[{"field":"work","count":2,"sum":14,"mean":7,"median":7},{"field":"sound","count":1,"sum":4,"mean":4,"median":4}]}} |
| DEMO-052 | Quan sát / `preference` | Ma trận ưu tiên do người dùng lựa chọn | {"calculation":{"ranking_allowed":true}} |
| DEMO-053 | Quan sát / `preference` | Tiêu chí thiếu không tự chuẩn hóa thành 100 | {"calculation":{"ranking_allowed":false}} |
| DEMO-054 | Cấu trúc biểu tượng / `hexagram` | Biến đổi sáu hào từ dưới lên | {"calculation":{"changed_lines":[1,0,0,0,1,1]}} |
| DEMO-055 | Phạm vi nghiên cứu / `blocked` | Adapter giữ chỗ có điều kiện: bazi.full | {"status":"METHOD_NOT_RELEASED"} |
| DEMO-056 | Phạm vi nghiên cứu / `blocked` | Adapter giữ chỗ có điều kiện: ziwei.full | {"status":"METHOD_NOT_RELEASED"} |
| DEMO-057 | Phạm vi nghiên cứu / `blocked` | Adapter giữ chỗ có điều kiện: nadi.record_lookup | {"status":"METHOD_NOT_RELEASED"} |
| DEMO-058 | Phạm vi nghiên cứu / `blocked` | Chặn loại suy luận vượt phạm vi: face.personality | {"status":"POLICY_BLOCKED"} |
| DEMO-059 | Phạm vi nghiên cứu / `blocked` | Chặn loại suy luận vượt phạm vi: medical_risk_from_palm | {"status":"POLICY_BLOCKED"} |
| DEMO-060 | Quyền và vận hành / `authorization` | Quyền đúng phạm vi | {"allowed":true} |
| DEMO-061 | Quyền và vận hành / `authorization` | Khác chủ thể bị chặn | {"allowed":false} |
| DEMO-062 | Quyền và vận hành / `authorization` | Quyền đã thu hồi bị chặn | {"allowed":false} |
| DEMO-063 | Quyền và vận hành / `authorization` | Khác mục đích bị chặn | {"allowed":false} |
| DEMO-064 | Quyền và vận hành / `authorization` | Revision cũ bị chặn | {"allowed":false} |
| DEMO-065 | Quyền và vận hành / `authorization` | Người chưa đăng nhập bị chặn | {"allowed":false} |
| DEMO-066 | Quyền và vận hành / `claim` | Biểu tượng không được có xác suất | PROBABILITY_NOT_ALLOWED |
| DEMO-067 | Quyền và vận hành / `claim` | Model ID giả không mở quyền dự báo | MODEL_NOT_APPROVED |
| DEMO-068 | Quyền và vận hành / `optimistic` | Cập nhật đúng phiên bản | {"version":5} |
| DEMO-069 | Quyền và vận hành / `optimistic` | Cập nhật từ phiên bản cũ bị chặn | VERSION_CONFLICT |
| DEMO-070 | Quyền và vận hành / `transition` | Thanh toán có trạng thái riêng | {"next":"paid"} |
| DEMO-071 | Quyền và vận hành / `transition` | Không đi từ nháp thẳng tới hoàn tất | INVALID_STATE_TRANSITION |
| DEMO-072 | Quyền và vận hành / `transition` | Yêu cầu xóa chuyển sang hạn chế truy cập | {"next":"restricted"} |
| DEMO-073 | Báo cáo / `report` | Level 1 · bốn lớp và phần còn thiếu | {"level":1,"production_ready":false} |
| DEMO-074 | Báo cáo / `report` | Level 2 · bốn lớp và phần còn thiếu | {"level":2,"production_ready":false} |
| DEMO-075 | Báo cáo / `report` | Level 3 · bốn lớp và phần còn thiếu | {"level":3,"production_ready":false} |
| DEMO-076 | Báo cáo / `report` | Level 4 · bốn lớp và phần còn thiếu | {"level":4,"production_ready":false} |
| DEMO-077 | Báo cáo / `report` | Level 5 · bốn lớp và phần còn thiếu | {"level":5,"production_ready":false} |
| DEMO-078 | Báo cáo / `report` | Level 6 · bốn lớp và phần còn thiếu | {"level":6,"production_ready":false} |
| DEMO-079 | Báo cáo / `report` | Level 7 · bốn lớp và phần còn thiếu | {"level":7,"production_ready":false} |
| DEMO-080 | Báo cáo / `report` | Level 8 · bốn lớp và phần còn thiếu | {"level":8,"production_ready":false} |
| DEMO-081 | Báo cáo / `report` | Level 9 · bốn lớp và phần còn thiếu | {"level":9,"production_ready":false} |
| DEMO-082 | Luồng hồ sơ hoàn chỉnh / `profile_pipeline` | Hồ sơ xuyên suốt: đủ dữ liệu nền | {"state":"DRAFT_REFERENCE_ONLY","level":1} |
| DEMO-083 | Luồng hồ sơ hoàn chỉnh / `profile_pipeline` | Hồ sơ thiếu dữ liệu: không điền giờ sinh giả | {"state":"PARTIAL_REFERENCE","score":null} |
| DEMO-084 | Luồng hồ sơ hoàn chỉnh / `profile_pipeline` | Hồ sơ có hai ngày sinh: cần lựa chọn | {"state":"NEEDS_INPUT_CHOICE","probability":null} |
| DEMO-085 | Điều phối và tính gia tăng / `dag` | DAG: chia các đợt tính độc lập | {"status":"REFERENCE_PLAN_ONLY"} |
| DEMO-086 | Điều phối và tính gia tăng / `dag` | DAG: chặn chu trình | DAG_CYCLE |
| DEMO-087 | Điều phối và tính gia tăng / `dag` | DAG: thiếu phụ thuộc không tự bỏ qua | MISSING_DEPENDENCY |
| DEMO-088 | Điều phối và tính gia tăng / `impact` | Impact: đổi ngày chỉ chạy các nút phụ thuộc | {"impacted":["birth","cycle","report"],"unchanged":["profile","name"]} |
| DEMO-089 | Điều phối và tính gia tăng / `cache_key` | Cache: khóa theo tenant/chủ thể/mục đích | {"scope":"tenant_subject_purpose_version"} |
| DEMO-090 | Điều phối và tính gia tăng / `cache_key` | Cache: thiếu chủ thể phải từ chối | INVALID_CACHE_CONTEXT |
