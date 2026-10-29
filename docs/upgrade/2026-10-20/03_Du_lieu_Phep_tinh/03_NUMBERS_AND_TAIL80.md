# Bộ số: quy tắc độc lập, trường hợp biên và Mã đuôi 80

Mã tài liệu: **D12** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Method Engineering. Nguồn đối chiếu: G02, S15. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Bộ máy được tách thành các hàm
normalize_name bảo toàn chuỗi nguyên gốc và tạo derivative có phiên bản; latin_name_sum theo bảng A–Z công bố; digit_sum nhận chuỗi không âm; personal_year cần quy ước rút gọn và thời điểm bắt đầu năm; pair_classifier dùng cặp chồng lấn; tail80 chỉ dùng đúng bốn chữ số. Không trộn kết quả thành điểm hợp mệnh nếu chưa duyệt một scoring preference rõ.
## 2. Mã đuôi 80
Với chuỗi N có đúng bốn chữ số ASCII, r = int(N) % 80, miền 0–79. Bảng do Founder gửi có nhãn 1–80. Chính sách mặc định cho r=0 là unresolved; cấu hình as80 chỉ bật sau phê duyệt. `0000` không phải tài năng đặc biệt; đó là giá trị số dư. Dùng số nguyên, không dùng phần thập phân rồi floor/truncate.
Mỗi lớp dư có 125 đuôi trong 0000–9999. Một số điện thoại và số định danh có cùng đuôi nhận cùng mã. Ngày sinh không tham gia hàm nên không thể cá nhân hóa Tâm/Thi bằng riêng mô-đun này. 6231→71; 1986→66; 3468→28 là ví dụ kiểm thử từ nội dung cuộc trao đổi, không kết luận cát/hung thực tế.
## 3. Bảng tượng nghĩa
Lưu đủ source_text, source_label, edited_theme, reflection_question, editorial_note và version. Các mục 34/55 có vấn đề chữ trong bản nguồn: không âm thầm coi cách sửa là bản gốc. Nhãn Hung chỉ thuộc bảng; tuyệt đối không dịch thành dự báo bệnh/tai nạn/mất tiền. Không bán đổi SIM hoặc gói hóa giải bằng nỗi sợ.
## 4. Cặp số Bát Cực
Cặp liền kề có chồng lấn, n chữ số tạo n−1 cặp. Bảng cơ sở 64 cặp dùng tập 1,2,3,4,6,7,8,9. Cặp chứa 0 hoặc 5 trả unsupported theo cấu hình đầu; không tự gán 55=Phục vị. Các quy tắc nối qua 5 cần method release khác và source cụ thể; được kiểm tra độ nhạy nhưng không mặc nhiên là chân lý.
## 5. Họ tên và lịch số
Chuỗi quốc tế +84 và nội địa có thể khác tổng chữ số nếu chưa chuẩn hóa. Giữ raw_input, numbering_context và normalized_input; không cộng mã quốc gia tùy ý. Tên có dấu không bị sửa gốc; các hệ chữ khác Latin cần adapter riêng, không tự phiên âm rồi gọi hợp mệnh theo toàn thế giới.
## 6. Nghiệm thu
Exhaustive tail80 10.000 trường hợp; 64 cặp độc nhất; tests r=0, input invalid, NFC, quốc tế/nội địa, unsupported chars, output không có probability. Mã tham chiếu được giao kèm chỉ là minh chứng hợp đồng; không thay review phương pháp và production security.

## Amendment 2026-10-20 — công thức được phép và test biên

1. Chỉ `tail4_mod80`, `digit_sum`, `digital_root`, `latin_name_cycle_1_9`, `adjacent_pair_classification`, `task_completion`, `observation_coverage`, `cashflow_difference` và `age_interval` có entry trong `FORMULA_CATALOG.json`; entry `specified` không có nghĩa là đã được phép phát hành.
2. Không bổ sung master-number retention, personal-year boundary, Bát Cực qua 0/5, bảng tượng nghĩa hoặc quy tắc chuyển tự nếu chưa có source/config được duyệt. Trường hợp thiếu phải trả `unsupported`/`unresolved`, không tự chọn biến thể.
3. Tail80 runtime phải kiểm `N = 80 × quotient + remainder`, `0 ≤ remainder < 80`, và quan hệ `zero_policy`/`lookup_code`. JSON Schema không thay kiểm tra số học chéo trường.
4. Fixture tối thiểu gồm `0000`, `0001`, `0079`, `0080`, `0081`, `0160`, `6231`, `1986`, `3468`, `9999`; input sai gồm sai độ dài, khoảng trắng, số âm, decimal, non-ASCII digit và ký tự. Cả `unmapped` lẫn `as80` phải có negative/positive case.
5. Output số học là deterministic calculation; nhãn/tượng nghĩa là symbolic claim riêng, bị chặn khi rights/source/content review còn pending. Không nối kết quả với sức khỏe, tính cách, tai nạn, tài lộc hoặc xác suất.
