# Công thức, ma trận và chính sách sai số

**Life Code OS · Bản nâng cấp bảo toàn V2 · 20/10/2026**  
**Trạng thái:** Đặc tả để triển khai và rà soát; không phải chứng nhận production.

## 1. Mỗi công thức có một hợp đồng
Catalog `FORMULA_CATALOG.json` tách trường input, miền hỗ trợ, đơn vị, cấu hình, công thức, output, dữ liệu thiếu, lỗi, độ phức tạp, code path, demo IDs và trạng thái. Mã LCF-01 đến LCF-16 là họ phép tính tham chiếu có implementation, không phải 16 bộ môn đã được chứng minh khoa học. Những công thức nâng cao được ghi `SPEC_ONLY` hoặc `RESEARCH_ONLY`.

## 2. Mã đuôi 80
N là chuỗi đúng bốn chữ số; r=N mod 80. Số dư 0 mặc định unresolved; ánh xạ 0→80 chỉ khi cấu hình as80 được duyệt. Giữ số 0 đầu. Không dùng số thực rồi cắt phần lẻ. Bảng nhãn là một artifact có version; thiếu nguyên văn không được tự tạo nguyên văn. 10.000 đuôi chia đều 125/mã khi bật as80. Không cá nhân hóa từ phép tính không nhận hồ sơ.

## 3. Chuỗi cặp và ma trận chữ số
Với dãy n chữ số, tạo n−1 cặp chồng lấn. Bảng 64 dùng tập {1, 2, 3, 4, 6, 7, 8, 9}; cặp chứa 0 hoặc 5 ở policy strict trả unresolved. Policy bridge5_diagnostic là phân tích độ nhạy công khai, không được âm thầm áp hoặc coi là nguồn truyền thống đã phê duyệt. Ma trận thô đếm chữ số gốc; việc không có số 9 không nói trí nhớ kém. Các đường tổng chỉ là tổng số lần xuất hiện trong các ô được quy định.

## 4. Tên và rút gọn
Tên gốc → NFC → chuỗi VI-Latin theo quy tắc minh bạch. Đ được đổi thành D ở derivative. A–Z quy đổi tuần hoàn 1–9. Tổng nguyên âm/phụ âm có chính sách Y include/exclude; không có mặc định phổ quát cho mọi ngôn ngữ. Văn tự chưa hỗ trợ được từ chối, không tự Latin hóa rồi luận như cùng phương pháp. [N07]

Rút gọn giữ trace: 38→11→2 hoặc dừng ở 11 tùy policy. Cách cộng toàn bộ chữ số và cách rút gọn thành phần được lưu riêng. Căn đơn bằng 0 nếu n=0, bằng 1+((n−1) mod 9) nếu n>0. Mọi số phải là safe integer trong demo; tiền không đi qua floating-point.

## 5. Hào và quẻ
Demo nhận sáu bit từ dưới lên, 0 âm,1 dương. Hào động là tập chỉ số 1–6 không trùng. Quẻ biến lật đúng bit; chỉ số nhị phân không phải số thứ tự Văn Vương. Kiểm thử toàn bộ 64 quẻ × 64 mặt nạ. Không gán tên/lời quẻ trước khi khóa bảng ánh xạ, nguồn và quyền. Đây là ví dụ dùng toán học để làm rõ cấu trúc, không biến biểu tượng thành chứng minh đời người.

## 6. Điểm ưu tiên có trọng số
MCDA chỉ dùng tiêu chí và trọng số người dùng hiểu, tổng trọng số 100. Khi thiếu một tiêu chí, giữ nguyên mẫu số, hiển thị coverage và chặn xếp hạng toàn bộ; không renormalize âm thầm làm phương án thiếu dữ liệu có vẻ tốt hơn. Điểm là ưu tiên theo tiêu chí, không phải “độ hợp mệnh”.

## 7. Công thức từ dữ liệu thực
Action completion = số việc done đến hạn trong cửa sổ / số việc không hủy đến hạn trong cửa sổ. Mẫu số 0 trả null. Dòng tiền = tổng inflow−outflow theo từng currency, dùng minor units dạng chuỗi nguyên; không cộng VND với USD. Resonance chỉ tổng hợp điểm tự khai theo field/date; mean không chứng minh quan hệ nhân quả hoặc hiệu quả điều trị.

**Tra nguồn:** xem `11_SOURCES/SOURCE_ADDENDUM.csv`; các mã Nxx là nguồn đối chiếu chính thức, không phải mọi nhận định của HNH đã được khoa học xác nhận.
