# 02. Hợp đồng chuẩn hóa và nguyên tắc số học

Điện thoại Việt Nam trong demo nhận chuỗi nội địa 10 chữ số bắt đầu bằng 0 hoặc dạng +84/0084 tương ứng. Dấu cách, ngoặc, chấm và gạch nối là ký tự trình bày; số máy lẻ và chữ bị từ chối. Đây là chính sách demo, không phải xác minh thuê bao. Quốc gia khác phải có adapter riêng và cùng một thuê bao cần được quy về cùng một chuỗi trước khi so.

Phép rút gọn đơn với n>0 có công thức root(n)=1+((n−1) mod 9). Số 0 giữ 0. Chế độ preserve_11_22_33 dừng tại 11, 22 hoặc 33 theo các bước công bố; vẫn lưu căn đơn để so một số tiêu chí. Không dùng “master number” như nhãn đẳng cấp con người.

Hai biến thể LifePath được giữ: cộng trực tiếp mọi chữ số; hoặc rút gọn ngày, tháng và năm rồi cộng. Số trung gian có thể khác. Tài liệu WorldNumerology là nguồn cho một cách dùng, không đại diện mọi trường phái. [R06]

Bảng Latin tuần hoàn 1–9 được ghi tường minh: A1 B2 C3 D4 E5 F6 G7 H8 I9 J1 K2 L3 M4 N5 O6 P7 Q8 R9 S1 T2 U3 V4 W5 X6 Y7 Z8. Dấu tiếng Việt được chuyển ở một bản dẫn xuất, không thay tên gốc. NFC giải quyết các biểu diễn ký tự tương đương; nó không tự làm công việc phiên âm hoặc chọn nghĩa tên. [R16]

Kết quả được phân loại derived_metric khi chỉ là con số tính được; đoạn tự suy ngẫm là symbolic_interpretation hoặc guidance riêng. Chữ “Energy”, “Personality” hoặc “Memory” trong tên một chỉ số không biến phép quy đổi thành phép đo năng lượng, nhân cách hay trí nhớ.

# 03. Hai mươi ba thành phần: công thức và cách đọc

Danh mục sau đáp ứng từng chỉ số đã được yêu cầu trong các hồ sơ trước. Các giá trị chỉ xuất hiện khi đầu vào và cấu hình tương ứng có đủ. Điểm mới quan trọng là các tổng trung gian, chính sách và phần null được trả cùng kết quả; không còn chỉ đưa một số cuối cùng.

## NUM-01. Đường đời

**Công thức:** R(sum(ddmmyyyy)) hoặc R(R(month)+R(day)+R(sum(year))).

**Đầu vào:** Ngày sinh, life_path_variant, reduction_policy.

Hãy xem đây là cách tóm tắt chữ số ngày sinh trong một hệ biểu tượng. Không từ nó suy ra năng lực nghề nghiệp hoặc bắt người dùng sống theo một vai trò duy nhất.

**Trường hợp biên:** Tổng trung gian có thể khác dù căn giống nhau; lưu trace. Nguồn phương pháp: [R06].

## NUM-02. Ngày sinh

**Công thức:** day và R(day).

**Đầu vào:** Ngày sinh.

Giữ ngày gốc 1–31 cùng kết quả rút gọn. Ngày 11 vẫn là 11 trong hồ sơ; việc quy về 2 là thao tác của cấu hình chứ không sửa ngày sinh.

**Trường hợp biên:** Giữ ngày 1–31 cùng kết quả rút gọn. Nguồn phương pháp: [R06].

## NUM-03. Dấu số truyền thống 13/14/16/19

**Công thức:** Các số 13,14,16,19 thực sự xuất hiện trong trace được chọn.

**Đầu vào:** Trace của các chỉ số.

Chỉ ghi các số 13/14/16/19 thực sự có trong trace được chọn. Không thêm “nợ nghiệp” vì một diễn giải nghe phù hợp, không gán lỗi đạo đức hoặc nguyên nhân bệnh.

**Trường hợp biên:** Không gán lỗi đạo đức, nghiệp xấu hay nợ kiếp trước. Nguồn phương pháp: [R06].

## NUM-04. Biểu đạt theo tên đầy đủ

**Công thức:** R(Σ giá trị chữ Latin đã xác nhận).

**Đầu vào:** Tên khai sinh + bảng quy đổi.

Trả bảng từng chữ, giá trị từng thành phần tên, tổng và chuỗi rút gọn. Người dùng có thể nhìn thấy nguyên nhân khác biệt giữa tổng 52 và 25, dù cả hai cùng căn 7.

**Trường hợp biên:** Giữ nguyên tên Unicode; không suy năng lực từ số. Nguồn phương pháp: [R26].

## NUM-05. Biểu đạt theo tên thường dùng

**Công thức:** R(Σ giá trị chữ tên thường dùng).

**Đầu vào:** Tên thường dùng xác nhận.

Chạy lại trên chuỗi tên thường dùng được người dùng xác nhận. Không tự bỏ họ hoặc chọn biệt danh chỉ vì cho ra số thuận lợi.

**Trường hợp biên:** Không có tên thường dùng thì null; không tự lấy tên cuối. Nguồn phương pháp: [R26].

## NUM-06. Tổng nguyên âm tên đầy đủ

**Công thức:** R(Σ nguyên âm theo vowel_policy).

**Đầu vào:** Tên + chính sách Y.

Nguyên âm được xác định theo policy. CóY chưa rõ thì để null; không suy ham muốn, niềm tin hoặc động cơ sâu từ tổng chữ.

**Trường hợp biên:** Có Y chưa phân loại thì null cho phần này, không chặn tổng tên. Nguồn phương pháp: [R07].

## NUM-07. Tổng nguyên âm tên thường dùng

**Công thức:** R(Σ nguyên âm tên thường dùng).

**Đầu vào:** Tên thường dùng + Y policy.

Tên thường dùng có policy nguyên âm độc lập được ghi trong lần chạy. Không có tên thường dùng thì không dựng “phiên bản xã hội” giả.

**Trường hợp biên:** Dùng đúng chính sách của lần chạy. Nguồn phương pháp: [R07].

## NUM-08. Số ghép và các bước rút gọn

**Công thức:** Lưu tổng, path, root theo từng component.

**Đầu vào:** Tất cả trace.

Lưu path của tất cả thành phần có phép rút gọn: tên, ngày, maturity, rational, balance, các tổng pinnacle. Đây là dữ liệu toán học, không tự thêm 80 hoặc 81 lời nghĩa vào mọi số ghép.

**Trường hợp biên:** Không áp một nghĩa cố định cho 11/22/33 trên mọi vị trí. Nguồn phương pháp: [R06].

## NUM-09. Tổng phụ âm tên đầy đủ

**Công thức:** R(Σ phụ âm theo vowel_policy).

**Đầu vào:** Tên + Y policy.

Tên truyền thống Personality được giải thích là tổng phụ âm. Nó không thay bảng hỏi nhân cách hoặc quan sát người thật.

**Trường hợp biên:** Là chỉ số quy ước, không phải đo nhân cách. Nguồn phương pháp: [R07].

## NUM-10. Tổng phụ âm tên thường dùng

**Công thức:** R(Σ phụ âm tên thường dùng).

**Đầu vào:** Tên thường dùng.

Giữ cùng nguyên tắc với tên đầy đủ. Không coi khác biệt giữa hai tổng là bằng chứng người đó có hai nhân cách.

**Trường hợp biên:** Không có dữ liệu thì null. Nguồn phương pháp: [R07].

## NUM-11. Chỉ số trưởng thành quy ước

**Công thức:** R(LifePath.value + Expression.value).

**Đầu vào:** Hai chỉ số nền + maturity_policy.

Cộng hai kết quả theo policy đã chọn; giữ cả tổng mới và căn. Không tự suy ra thời điểm trưởng thành tâm lý hay sứ mệnh.

**Trường hợp biên:** Không kết luận sứ mệnh hay tuổi trưởng thành thật. Nguồn phương pháp: [R08].

## NUM-12. Chỉ số tên riêng và ngày sinh

**Công thức:** R(Σ chữ của given_name + day).

**Đầu vào:** given_name được xác nhận.

Tên riêng Việt Nam có thể nhiều âm tiết. Người dùng phải nhập given_name. Không áp chữ đầu của tên đầy đủ như một nguồn Anh ngữ mà bỏ qua cấu trúc tên Việt. [R09]

**Trường hợp biên:** Tên Việt có thể nhiều âm tiết; không tự dùng first token. Nguồn phương pháp: [R09].

## NUM-13. Nhóm số không xuất hiện trong tên

**Công thức:** {1..9} trừ các giá trị chữ có mặt.

**Đầu vào:** Tên khai sinh.

Danh sách các giá trị 1–9 không xuất hiện trong tên là phép đếm. Thiếu 3 không có nghĩa thiếu sáng tạo; thiếu 9 không có nghĩa thiếu trí nhớ.

**Trường hợp biên:** Thiếu chữ số không có nghĩa thiếu năng lực. Nguồn phương pháp: [R10].

## NUM-14. Tổng chữ đầu các thành phần tên

**Công thức:** root(Σ initial_value).

**Đầu vào:** Tên có thành phần rõ.

Tổng chữ đầu mỗi thành phần tên được rút gọn đơn. Không đo cân bằng cảm xúc; giữ chú giải tên gọi truyền thống. [R11]

**Trường hợp biên:** Không đo cân bằng tâm lý. Nguồn phương pháp: [R11].

## NUM-15. Nhóm số lặp nhiều nhất trong tên

**Công thức:** argmax frequency; giữ mọi đồng hạng.

**Đầu vào:** Tên.

Đếm tần suất từng giá trị chữ. Khi có hai giá trị cùng lớn nhất, phải trả cả hai; không chọn một số theo cảm tính.

**Trường hợp biên:** Không chọn tùy ý một số khi hòa. Nguồn phương pháp: [R10].

## NUM-16. Số nhóm chữ có mặt

**Công thức:** count(distinct values 1..9).

**Đầu vào:** Tên.

Đếm số nhóm giá trị khác nhau có mặt. Kết quả 0–9 theo cấu trúc không được đổi thành 0–100% tự tin hoặc xác suất thành công.

**Trường hợp biên:** Không quy đổi thành confidence xác suất. Nguồn phương pháp: [R10].

## NUM-17. Bốn hiệu số thử thách

**Công thức:** |M-D|, |D-Y|, |C1-C2|, |M-Y|.

**Đầu vào:** M,D,Y rút gọn đơn.

Dùng M, D, Y rút gọn đơn để tạo bốn hiệu tuyệt đối. Challenge 0 là kết quả hiệu số, không có nghĩa không có khó khăn.

**Trường hợp biên:** Số 0 được giữ; không có nghĩa không khó khăn. Nguồn phương pháp: [R13].

## NUM-18. Phạm vi thời gian thử thách

**Công thức:** Chính sách dùng cùng band hoặc nhập band có nguồn.

**Đầu vào:** Span policy.

Bản thử mặc định không gán thời gian. Chỉ dùng band Pinnacle khi policy follow_pinnacles được chọn; đây là cấu hình, không đồng thuận lịch sử tuyệt đối.

**Trường hợp biên:** Mặc định chưa suy ra tuổi nếu chưa chọn chính sách. Nguồn phương pháp: [R13].

## NUM-19. Bốn tổng đỉnh cao

**Công thức:** R(M+D),R(D+Y),R(P1+P2),R(M+Y).

**Đầu vào:** Components + reduction policy.

Bốn tổng có trace. Tổng thứ 3 dùng chính P1 và P2 đã tạo bởi cấu hình đang chạy. Không thay giữa root và master một cách âm thầm. [R12]

**Trường hợp biên:** P3 dùng đúng P1,P2 của phiên bản đã chọn. Nguồn phương pháp: [R12].

## NUM-20. Phạm vi tuổi đỉnh cao

**Công thức:** B=36-root(LP); B+9; B+18.

**Đầu vào:** boundary_policy.

B=36−root(LP). Demo quy ước B là tuổi nguyên cuối giai đoạn đầu, vì vậy giai đoạn sau bắt đầu ở tuổi B+1. Các phương pháp dùng ngày sinh nhật B để chuyển phải là cấu hình khác.

**Trường hợp biên:** Demo chọn last-integer-age-inclusive; lưu rõ điểm chuyển. Nguồn phương pháp: [R12].

## NUM-21. Ba chu kỳ tháng–ngày–năm

**Công thức:** root(month),root(day),root(sum(year)).

**Đầu vào:** Ngày sinh + period span policy.

Giá trị là tháng–ngày–năm rút gọn. Mốc tuổi chưa có quy tắc đầy đủ thì null; có thể nhận ba khoảng liên tiếp do người dùng xác nhận kèm source_note. Không lấy ba mốc của một bảng có sẵn nếu không rõ nó được tính thế nào. [R14]

**Trường hợp biên:** Giá trị tính được; tuổi chu kỳ không mặc nhiên bằng pinnacle. Nguồn phương pháp: [R14].

## NUM-22. Cầu nối đường đời–tên

**Công thức:** |root(LP)-root(Expression)|.

**Đầu vào:** Hai chỉ số.

Hiệu tuyệt đối giữa hai căn chỉ mô tả khoảng cách chữ số trong quy ước. Không chuyển nó thành điểm hợp nghề hoặc mức xung đột nội tâm.

**Trường hợp biên:** Hiệu số mô tả, không phải mức hợp khoa học. Nguồn phương pháp: [R26].

## NUM-23. Cầu nối nguyên âm–phụ âm

**Công thức:** |root(Heart)-root(Personality)|.

**Đầu vào:** Hai chỉ số đủ policy.

Nếu một tổng thiếu policy Y thì cầu nối cũng thiếu. Số 0 trả về không có nghĩa đời sống bên trong và ngoài hoàn toàn đồng nhất.

**Trường hợp biên:** Y chưa rõ thì bridge=null. Nguồn phương pháp: [R26].

# 04. Ví dụ số–tên đọc được từng bước

Dùng hồ sơ giả AN BINH, sinh 02/01/1990, tên riêng AN. Không gắn hồ sơ này với một người thật.

AN=1+5=6. BINH=2+9+5+8=24. Tổng tên 30→3. Nguyên âmA+I=1+9=10→1. Phụ âm 20→2. Tổng chữ đầuA+B=3. Tên riêngAN cộng ngày 2 được 8.

Tổng chữ số ngày sinh 2 + 1 + 1 + 9 + 9 + 0=22. Cấu hình rút gọn đơn trả 4; cấu hình giữ 22 trả value 22 và root 4. Cả hai phải lưu đúng tên policy. Số trưởng thành cũng thay đổi trace theo việc cộng value hay root; không lấy một số trung gian từ phương pháp này rồi gán nhãn của phương pháp khác.

Cách đọc đúng là: “Hệ quy đổi đang dùng tạo ra các tổng sau.” Phần suy ngẫm có thể hỏi người dùng muốn dùng tên trong hoàn cảnh nào, tên có ý nghĩa gì đối với gia đình hoặc cách phát âm nào cần giữ. Không kết luận AN BINH sinh ra thích giao tiếp hoặc có trực giác mạnh chỉ vì phép cộng.

Đối chiếu bảng cũ cần ba trạng thái: khớp cả tổng và căn; chỉ khớp căn; khác cả hai. Kết quả chỉ khớp căn không được coi là đã tái lập toàn bộ nguồn. Một ví dụ gặp trước đây có Expression 25/7 trong dữ liệu nhập nhưng phép cộng từng chữ theo bảng Latin cho 52/7. Hệ mới giữ hai record và yêu cầu chọn nguồn, không đảo số 52 thành 25 để khớp.
