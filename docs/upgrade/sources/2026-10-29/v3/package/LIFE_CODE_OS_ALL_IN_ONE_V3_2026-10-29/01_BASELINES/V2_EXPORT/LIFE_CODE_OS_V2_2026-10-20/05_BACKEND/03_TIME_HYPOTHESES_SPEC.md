# Lịch, giờ sinh, múi giờ và nhiều giả thuyết

**Life Code OS · Bản nâng cấp bảo toàn V2 · 20/10/2026**  
**Trạng thái:** Đặc tả để triển khai và rà soát; không phải chứng nhận production.

## 1. Dữ liệu thời gian phải có nguồn
BirthRecord giữ calendar, date_original, date_iso khi quy đổi được, precision, local_time, time_range, place_original, timezone_id, coordinates và source. Không suy múi giờ từ vị trí hiện tại. Geocoding là bước gợi ý có người xác nhận, không lấy tên tỉnh cùng tên ở nơi khác làm kết quả chắc chắn. IANA tzdb được lưu version. [N08]

## 2. Các trường hợp khó phải là ca chuẩn
Chỉ biết năm → không điền 01/01. Không rõ giờ → không điền 00:00. Giờ được nhớ “khoảng 6–7 giờ” → khoảng, không một timestamp. Ngày dương/âm chưa rõ → yêu cầu xác nhận calendar. Nơi sinh chưa biết → không chạy phương pháp cần tọa độ chính xác. Ngày 29/02 → chọn chính sách anniversary theo sản phẩm và ghi rõ.

## 3. DST fold và gap
Một local time có thể ứng với 0, 1 hoặc 2 thời điểm UTC. Demo dùng Intl/ICU, liệt kê offset ứng viên trong vùng thời gian và đối chiếu lại phần local, không âm thầm chọn một. Gap yêu cầu sửa nguồn; fold yêu cầu lựa chọn hoặc chạy hai phương án. Phạm vi demo 1900–2100, sampling offset không thay một thư viện thiên văn/lịch pháp được thẩm định cho mọi thời kỳ.

## 4. Giờ Mặt Trời và hệ truyền thống
Civil time, mean solar time và apparent solar time là các biểu diễn khác nhau. Adapter nâng cao phải công bố dùng biểu diễn nào, kinh độ, equation of time, precision và ranh ngày. Không tự “sửa giờ sinh cho hợp lá số”. Bát tự có chính sách đổi ngày lúc 23 giờ hoặc 00 giờ và khởi vận khác nhau; không dùng một rule cho mọi trường phái. Các chính sách này đang ở phần đặc tả nghiên cứu, chưa được code đầy đủ trong demo.

## 5. Timeline tuổi
Tuổi a là [sinh nhật năm B+a, sinh nhật năm B+a+1). Không cộng 365 ngày. Khung 0–99 có 100 khoảng, không dự báo tuổi thọ. Demo trả events rỗng; sự kiện chỉ được thêm từ dữ liệu lịch sử, kế hoạch hoặc symbolic cycle có nhãn. Không được gọi năm 6 là năm cưới, năm 8 là năm giàu như một dữ kiện dự báo.

## 6. Hypothesis engine
Mỗi phương án có ID, nguồn, field_path, giá trị, thời điểm và trạng thái. Run dùng selected_hypotheses cụ thể; một phép so sánh tạo từng kết quả song song và không tự chọn phương án có lời luận hấp dẫn. Khi sửa một phương án, dependency graph xác định run/report nào cần cập nhật. Mốc tuổi do giấy tờ và mốc tuổi thực tế có thể khác; giao diện phải nêu chứ không lấy trung bình hai ngày.

## 7. Nghiệm thu
Các ca gồm Berlin 2026-10-25 02:30 có 2 ứng viên, New York DST gap, UTC thường, Việt Nam, ngày nhuận, lịch chưa biết, timezone thiếu và năm vượt phạm vi. Runtime receipt lưu Node/ICU/tzdb. Không coi việc một ca đúng là lịch toàn cầu đã được triển khai đầy đủ.

**Tra nguồn:** xem `11_SOURCES/SOURCE_ADDENDUM.csv`; các mã Nxx là nguồn đối chiếu chính thức, không phải mọi nhận định của HNH đã được khoa học xác nhận.
