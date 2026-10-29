# 06. Bát Cực Linh Số: tám nhóm và 64 cặp

Bảng dưới là bảng tham chiếu đối chiếu từ nguồn thực hành công khai. Tên nhóm giữ Hán–Việt và chữ Trung văn để truy nguồn. Chúng không phải tên bệnh hoặc kết luận về một chủ thể. Chỉ bảng này chưa tạo đủ toàn bộ nội dung cuốn “Thiên Mệnh Giàu Sang” nâng cao; toàn văn sách và quyền sử dụng vẫn chưa được cung cấp. [R04, R05]

| Nhóm | Trung văn | Tám cặp | Chủ đề câu hỏi HNH |
| --- | --- | --- | --- |
| Sinh khí | 生氣 | 14 · 41 · 67 · 76 · 39 · 93 · 28 · 82 | kết nối và nguồn hỗ trợ |
| Thiên y | 天醫 | 13 · 31 · 68 · 86 · 49 · 94 · 27 · 72 | nguồn lực và điều cần gìn giữ |
| Diên niên | 延年 | 19 · 91 · 78 · 87 · 34 · 43 · 26 · 62 | tổ chức và trách nhiệm |
| Phục vị | 伏位 | 11 · 22 · 33 · 44 · 66 · 77 · 88 · 99 | duy trì và khả năng điều chỉnh |
| Tuyệt mệnh | 絕命 | 12 · 21 · 69 · 96 · 48 · 84 · 37 · 73 | lựa chọn và giới hạn đánh đổi |
| Ngũ quỷ | 五鬼 | 18 · 81 · 79 · 97 · 36 · 63 · 24 · 42 | ý tưởng mới và tính nhất quán |
| Lục sát | 六煞 | 16 · 61 · 47 · 74 · 38 · 83 · 29 · 92 | quan hệ và ranh giới |
| Họa hại | 禍害 | 17 · 71 · 89 · 98 · 46 · 64 · 23 · 32 | lời nói và trách nhiệm giao tiếp |

Về toán học, tập chữ sốD={1,2,3,4,6,7,8,9}tạo 64 cặp có thứ tự. Mỗi cặp xuất hiện đúng một lần trong bảng. Việc kiểm toàn bộ bảng xác nhận nó đầy đủ theo tập D, không xác nhận những cặp ấy gây ra sự kiện trong đời.

Tám nhóm đều có chủ đề có thể dùng để đặt câu hỏi. Nhóm có tên mạnh như Tuyệt mệnh không được chuyển thành dự báo mất mạng; Họa hại không chứng minh người đó nói dối; Thiên y không là chẩn đoán hoặc điều trị. Giải thích này phải nằm cạnh kết quả, không giấu trong một trang điều khoản riêng.

# 07. Vị trí, chuỗi ba chữ số và ma trận chuyển nhóm

Một dãy n chữ số tạo n−1 cặp và n−2 cửa sổ ba chữ số. Mỗi cặp lưu start_index, end_exclusive và group_id. Mỗi cửa sổ ba số nối hai cặp có chung chữ số giữa. Không tạo một tổ hợp từ hai cặp không liền nhau rồi nói đó là thứ tự thực của dãy.

Ví dụ 4134 → 41(SK),13(TY),34(DN). Ví dụ 4314 → 43(DN),31(TY),14(SK). Tổng chữ số giống nhau nhưng luồng nhóm khác nhau. Bộ máy lưu cả histogram và order; histogram giống nhau không đủ để khẳng định hai chuỗi giống toàn bộ.

Ma trận 8×8 ghi đếm mỗi chuyển nhóm trong dãy và dẫn tới một câu hỏi biên tập HNH. Chẳng hạn, DN → SK gợi câu hỏi về trách nhiệm và nguồn hỗ trợ; HH → TY gợi việc giao tiếp và điều cần gìn giữ. Đây là chất liệu tự soi chiếu nguyên bản chờ duyệt, không được quảng bá là 64 công thức bí truyền đã tìm trong sách.

Trong 512 chuỗi ba chữ số của tập D, mọi cặp đều được phân loại. Các chuỗi có 0 hoặc 5 có thể thiếu một hoặc hai nhóm; trạng thái chuyển phải unresolved. Hệ không lấp nhóm thiếu bằng sao của chữ số gần nhất.

Vị trí đầu–giữa–đuôi được lưu theo số thực trong dãy. Nếu một phương pháp chỉ đọc đuôi, cần lưu start_index riêng và tên cấu hình. Không tự chuyển số điện thoại quốc tế thành số khác ở lớp tính toán chỉ vì thay cách viết mã quốc gia.

# 08. Số 0, số 5, độ mạnh và những điều còn phải khóa

Nguồn thực hành mô tả 0 và 5 như yếu tố điều chỉnh, không phải hai sao mới. Bản V3 cố ý không tự lượng hóa bằng các hệ số không được cung cấp. [R04, R05]

Strict_adjacent_v3 là chế độ mặc định. Tất cả chữ số được giữ; cặp chứa 0 hoặc 5 được ghi chưa xử lý. Diagnostic_single_bridge chỉ tạo quan hệ bổ sung cho A0B hoặc A5B với A, B trong tập D. Ví dụ 103 thêm quan hệ 13 thuộc TY, 153 cũng thêm 13 thuộc TY nhưng lưu modifier khác nhau. Các cặp 10/03 hoặc 15/53 vẫn còn nguyên trong trace.

Chuỗi 8553, 1001 hoặc 3501 không có một cầu đơn đủ điều kiện để xóa toàn bộ ký tự đặc biệt. Chúng được giữ là unresolved_modifier_run. Không giả lập “số 5 khuếch đại” bằng cách nhân trọng số hoặc “số 0 ẩn” bằng cách bỏ nội dung bất lợi.

Độ mạnh, chế hóa, tỷ lệ các nhóm, quan hệ tiên thiên–hậu thiên và số lượng sao tối ưu phải có hồ sơ phương pháp riêng. Thứ tự một danh sách không đủ để suy tỷ lệ 4:3:2:1. Một nguồn nói Thiên y chế Tuyệt mệnh vẫn cần định nghĩa cách chọn, vị trí, điều kiện và ví dụ trước khi có hàm tính. Chưa có những điều ấy thì không được trả một “điểm chế hóa thành công”.

Cách đọc và hình thức sử dụng của số thuộc một lớp khác: nhịp đọc, dễ nhầm, sở thích, giá, quyền chuyển nhượng. Giá cao không tự cộng điểm tượng nghĩa. Hai số cùng đuôi có thể cùng Mã 80 nhưng khác luồng Bát Cực; không có quy tắc nào tự là quy tắc cao nhất cho mọi mục tiêu.

# 09. So sánh số cho cá nhân, doanh nghiệp và định danh

Một bài so sánh cần tách mục tiêu: số liên lạc cá nhân, số công việc, tên thương hiệu, dãy định danh hoặc mẫu thiết kế. Chỉ dùng dữ liệu đúng mục tiêu. Không tiếp nhận toàn bộ số căn cước để chạy phép bốn chữ số; không luận mật khẩu hoặc khuyên đổiOTPcho hợp số.

Mỗi phương án hiển thị tổng chữ số, căn, histogram, chuỗi, phần chưa xử lý, số lặp, Mã đuôi 80 và các tiêu chí thực tế được người dùng nhập. Không có tiêu chí utility được duyệt thì recommended=null. Khi có trọng số do người dùng chọn, phải gọi đó là điểm ưu tiên theo sở thích, không phải phần trăm đổi vận.

Ngày sinh hoặc tên có thể được đặt bên cạnh kết quả số để người dùng đối chiếu biểu tượng; không sinh tương tác sinh học chưa được đo. Nếu giá là dữ liệu từ ảnh, phải ghi “chưa xác nhận”. Nếu số không còn bán hoặc quyền chuyển giao chưa rõ, bài so khớp biểu tượng không giải quyết được vấn đề sử dụng.

Với doanh nghiệp, số liên lạc không quyết định năng lực đội ngũ, an toàn dữ liệu hoặc khả năng tạo doanh thu. Giá trị thực là liên hệ đúng, giữ quyền quản lý, dễ đọc và quy trình bàn giao khi người giữ SIM rời tổ chức. Bộ phận thương mại cần đánh giá những yếu tố ấy độc lập với bảng số.

Các mục kết luận đồng hạng được giữ. Trong hai dãy 0943876231 và 0916876231, số lượng nhóm và căn có thể giống nhau; chỉ quy tắc thứ tự mới có thể phân biệt. Nếu hệ chưa có quy tắc thứ tự được duyệt, không ép một dãy thắng để bài viết có vẻ quyết đoán.
