# 07. Bộ số–tên hợp nhất: 23 thành phần

Các yêu cầu trước đây đã được gom vào một hợp đồng thống nhất, nhưng từng kết quả vẫn có trace riêng. Tên nguyên văn, tên quy đổi và tên thường dùng không ghi đè nhau. Tên riêng để tính Rational Thought phải do người dùng xác nhận; với tên Việt không được tự lấy token đầu.

| Mã | Thành phần | Công thức và điều kiện |
| --- | --- | --- |
| NUM-01 | Đường đời | R(sum(ddmmyyyy)) hoặc R(R(month)+R(day)+R(sum(year))) |
| NUM-02 | Ngày sinh | day và R(day) |
| NUM-03 | Dấu số truyền thống 13/14/16/19 | Các số 13,14,16,19 thực sự xuất hiện trong trace được chọn |
| NUM-04 | Biểu đạt theo tên đầy đủ | R(Σ giá trị chữ Latin đã xác nhận) |
| NUM-05 | Biểu đạt theo tên thường dùng | R(Σ giá trị chữ tên thường dùng) |
| NUM-06 | Tổng nguyên âm tên đầy đủ | R(Σ nguyên âm theo vowel_policy) |
| NUM-07 | Tổng nguyên âm tên thường dùng | R(Σ nguyên âm tên thường dùng) |
| NUM-08 | Số ghép và các bước rút gọn | Lưu tổng, path, root theo từng component |
| NUM-09 | Tổng phụ âm tên đầy đủ | R(Σ phụ âm theo vowel_policy) |
| NUM-10 | Tổng phụ âm tên thường dùng | R(Σ phụ âm tên thường dùng) |
| NUM-11 | Chỉ số trưởng thành quy ước | R(LifePath.value + Expression.value) |
| NUM-12 | Chỉ số tên riêng và ngày sinh | R(Σ chữ của given_name + day) |
| NUM-13 | Nhóm số không xuất hiện trong tên | {1..9} trừ các giá trị chữ có mặt |
| NUM-14 | Tổng chữ đầu các thành phần tên | root(Σ initial_value) |
| NUM-15 | Nhóm số lặp nhiều nhất trong tên | argmax frequency; giữ mọi đồng hạng |
| NUM-16 | Số nhóm chữ có mặt | count(distinct values 1..9) |
| NUM-17 | Bốn hiệu số thử thách | /M-D/, /D-Y/, /C1-C2/, /M-Y/ |
| NUM-18 | Phạm vi thời gian thử thách | Chính sách dùng cùng band hoặc nhập band có nguồn |
| NUM-19 | Bốn tổng đỉnh cao | R(M+D),R(D+Y),R(P1+P2),R(M+Y) |
| NUM-20 | Phạm vi tuổi đỉnh cao | B=36-root(LP); B+9; B+18 |
| NUM-21 | Ba chu kỳ tháng–ngày–năm | root(month),root(day),root(sum(year)) |
| NUM-22 | Cầu nối đường đời–tên | /root(LP)-root(Expression)/ |
| NUM-23 | Cầu nối nguyên âm–phụ âm | /root(Heart)-root(Personality)/ |

Mặc định gặp Y chưa xác nhận thì tổng tên vẫn được tính, còn tổng nguyên âm, phụ âm và cầu nối liên quan để null. Người dùng có thể chọn policy “Y là nguyên âm” hoặc “Y là phụ âm”, nhưng hệ thống ghi đó là cấu hình, không là chân lý cho mọi ngôn ngữ. Quy tắc theo phát âm tiếng Anh không được mặc nhiên áp cho tên Việt. [R07]

Tổng trung gian là dữ liệu quan trọng. Hai cách có cùng căn 7 nhưng tổng 25 và 52 không được coi là cùng một trace. Khi đối chiếu bảng cũ, hệ thống tạo conflict record thay vì tự sửa để khớp. Chỉ số có tên truyền thống như Karmic Lessons, Rational Thought hay Subconscious Confidence được giải thích là tên của phép quy đổi, không phải kết luận nghiệp, khả năng tư duy hoặc xác suất tự tin.

Số lặp được mô tả theo chữ số, độ dài và vị trí. 22, 222 và 2222 khác nhau về hình thức, nhưng không tự suy ra độ mạnh gấp hai hay gấp bốn. Nhóm 2–5–8 là một trục đếm của một biểu đồ, không phải một mạch năng lượng cơ thể.
