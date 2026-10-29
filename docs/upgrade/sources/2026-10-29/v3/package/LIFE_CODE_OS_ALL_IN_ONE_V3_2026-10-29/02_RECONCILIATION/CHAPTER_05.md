# 05. Chín giai đoạn điều hướng và dòng thời gian 0–99

Chín giai đoạn trong V3 chỉ hỗ trợ chọn cách hỏi và mức thông tin phù hợp. Chúng không áp đặt tất cả trẻ em, người trưởng thành hoặc người lớn tuổi giống nhau. Ngưỡng tuổi cần được điều chỉnh theo lãnh thổ và nhu cầu sử dụng; các nghĩa vụ về quyền của trẻ em không chỉ được quyết định bằng bảng biên tập.

| Giai đoạn | Khoảng tuổi | Điều kiện sử dụng |
| --- | --- | --- |
| Đầu đời | 0–3 | Người chăm sóc đồng hành; không gắn nhãn tính cách hoặc sứ mệnh. |
| Khám phá | 3–6 | Chơi, ngôn ngữ, an toàn và nhịp sống; không xếp hạng trẻ. |
| Học nền | 6–12 | Sở thích, cơ hội học và kỹ năng; không suy trí nhớ từ ma trận. |
| Tuổi thiếu niên | 12–18 | Quyền riêng tư theo tuổi, phát triển bản sắc; không dự báo thân mật hoặc ép nghề. |
| Tự lập | 18–30 | Học, việc, quan hệ và trách nhiệm do chủ thể chọn. |
| Xây dựng | 30–45 | Nhiều vai trò có thể cùng tồn tại; không buộc kết hôn, sinh con hoặc sở hữu tài sản. |
| Tái định hướng | 45–60 | Điều chỉnh vai trò, chăm sóc, học lại, nguồn lực; không gọi tuổi này là khủng hoảng tất yếu. |
| Tiếp nối | 60–75 | Chủ động, khả năng tiếp cận, cộng đồng và chuyển giao. |
| Tiếp tục sống và trao truyền | 75–tiếp tục | Không dự báo tuổi thọ; có thể vượt 99 tuổi. Nội dung tùy nhu cầu, không rập khuôn. |

Một khoảng tuổi được biểu diễn [sinh nhật thứ a, sinh nhật thứ a+1). Với ngày 29/02, chọn chính sách 28/02 hoặc 01/03 và ghi vào kết quả. Khoảng 0–99 là 100 khoảng điều hướng, không giới hạn quyền sống hoặc hồ sơ sau 99 tuổi. Sự kiện sau 99 vẫn được giữ trong history, không ép vào tuổi 99.

Có bốn đường độc lập: lịch sử người dùng kể; chu kỳ biểu tượng; kế hoạch người dùng chọn; dự báo chỉ khi có mô hình được cho phép. Demo V3 có ba đường đầu và không có dự báo xác suất. Các năm chưa có sự kiện được để trống. Dữ liệu năm sinh giấy tờ khác thực tế tạo hai hồ sơ giả thuyết; không lấy trung bình hoặc chọn bản nào có lời luận dễ nghe hơn.

Ba chu kỳ tháng–ngày–năm, bốn Pinnacles và bốn Challenges không tự chia sẻ một bảng tuổi. Mỗi nhánh lưu boundary_policy. Quy ước last-integer-age-inclusive có nghĩa tuổi kết thúc là số tuổi tròn cuối cùng trong giai đoạn; ngày chuyển là sinh nhật tiếp theo. Phương pháp khác phải có mã phiên bản khác.
