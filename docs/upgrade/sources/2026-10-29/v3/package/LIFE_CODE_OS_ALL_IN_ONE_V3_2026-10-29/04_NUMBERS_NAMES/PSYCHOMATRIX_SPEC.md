# 05. Psychomatrix: đủ 17 vị trí và hai lớp dữ liệu

Biểu đồ raw chỉ đếm chữ số ngày sinh. Biểu đồ bốn số phụ thêm W1, W2, W3, W4 trước khi đếm. Không dùng hai tên cho cùng một kết quả hoặc giữ một biểu đồ rồi gắn lời nghĩa của biểu đồ kia.

Với ngày minh họa 02/11/2008: W1=14; W2=5; chữ số đầu của ngày 2 là 2; W3=14−2×2=10; W4=1. Sau khi thêm chuỗi các số 14, 5, 10, 1 vào chữ số ngày sinh, số lượng ô 1 đến 9 lần lượt là 5, 2, 0, 1, 1, 0, 0, 1, 0. Tổng tám trục theo thứ tự 147, 258, 369, 123, 456, 789, 159, 357 là 6, 4, 0, 7, 2, 1, 6, 1. Đây chỉ là ví dụ tính đếm, không phân tích đời sống một trẻ cụ thể.

| Vị trí | Nhãn công khai | Cách tính |
| --- | --- | --- |
| CELL-1 | Ô số 1 | Tổng số lần xuất hiện của 1 |
| CELL-2 | Ô số 2 | Tổng số lần xuất hiện của 2 |
| CELL-3 | Ô số 3 | Tổng số lần xuất hiện của 3 |
| CELL-4 | Ô số 4 | Tổng số lần xuất hiện của 4 |
| CELL-5 | Ô số 5 | Tổng số lần xuất hiện của 5 |
| CELL-6 | Ô số 6 | Tổng số lần xuất hiện của 6 |
| CELL-7 | Ô số 7 | Tổng số lần xuất hiện của 7 |
| CELL-8 | Ô số 8 | Tổng số lần xuất hiện của 8 |
| CELL-9 | Ô số 9 | Tổng số lần xuất hiện của 9 |
| AXIS-147 | Đường 1-4-7 | Tổng số lần xuất hiện của 1, 4, 7 |
| AXIS-258 | Đường 2-5-8 | Tổng số lần xuất hiện của 2, 5, 8 |
| AXIS-369 | Đường 3-6-9 | Tổng số lần xuất hiện của 3, 6, 9 |
| AXIS-123 | Đường 1-2-3 | Tổng số lần xuất hiện của 1, 2, 3 |
| AXIS-456 | Đường 4-5-6 | Tổng số lần xuất hiện của 4, 5, 6 |
| AXIS-789 | Đường 7-8-9 | Tổng số lần xuất hiện của 7, 8, 9 |
| AXIS-159 | Đường 1-5-9 | Tổng số lần xuất hiện của 1, 5, 9 |
| AXIS-357 | Đường 3-5-7 | Tổng số lần xuất hiện của 3, 5, 7 |

Các nhãn nguồn được giữ trong registry nghiên cứu để biết xuất xứ, nhưng giao diện không dự báo sức khỏe, trí tuệ, đạo đức hoặc thân mật từ chúng. Khi W3 âm, demo trả lỗi phương pháp chưa hỗ trợ. Các biến thể thêm hằng số cho năm 2000 hoặc đổi thuật toán phải có adapter riêng, nguồn và kiểm thử; không được tự bổ sung để luôn có một lời luận.
