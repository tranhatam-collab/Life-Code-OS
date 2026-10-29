# 10. Mã đuôi 80: toán học, nguồn và toàn bộ bảng

Công thức là r=N mod 80. Với 6789, thương 84 và dư 69; phép nhân phần lẻ đúng là 0,8625×80=69, không phải 0,6825×80. Phép chia 80 trả 0–79, vì vậy bảng 1–80 cần zero_policy riêng. V3 mặc định chưa ánh xạ, chỉ dùng 0 → 80 khi được chọn rõ.

Miền 0000–9999 có 10.000 đầu vào, chia đều 125 đuôi cho mỗi mã. Do 10.000 chia hết 80, thêm tiền tố không thay số dư khi tính theo hệ thập phân. Tính chất ấy chỉ nói về modulo, không xác nhận bốn số đuôi quyết định toàn đời.

Bảng nguồn có 15 Đại cát, 23 Cát, 16 Bình, 23 Hung và 3 Đại hung. Nhãn được giữ để đối chiếu lịch sử; chúng không thành điểm phẩm chất. Tính toàn bộ 10.000 đầu vào là kiểm thuật toán, không kiểm 10.000 người.

Bảng sau giữ nguyên lời nguồn có thể còn lỗi chép, đồng thời thêm câu hỏi riêng. Các lỗi nguồn không được âm thầm sửa trong source_text; bản biên tập và nguyên văn là hai trường. [R28]

## Các mã 01–20

| Mã | Nhãn nguồn | Lời nguồn giữ để đối chiếu | Câu hỏi ứng dụng |
| --- | --- | --- | --- |
| 01 | Cát | Đại triển hồng đô, khả được thành công | Kết quả cụ thể nào sẽ thể hiện chí hướng của bạn trong 30 ngày? |
| 02 | Bình | Thăng trầm không số, về già vô công | Điều gì thường bị gián đoạn, và bạn có cách giữ lại phần đã hoàn thành không? |
| 03 | Đại cát | Ngày ngày tiến tới, vạn sự thuận toàn | Một dấu hiệu tiến bộ nhỏ nào có thể được ghi nhận mỗi tuần? |
| 04 | Hung | Tiền đồ gai góc, dâu khổ theo đuổi | Trở ngại hiện tại là kỹ năng, nguồn lực, thông tin hay cách tổ chức? |
| 05 | Đại cát | Làm ăn phát đạt, lợi danh đều có | Hình ảnh bên ngoài có đang đi nhanh hơn giá trị bạn thực sự giao không? |
| 06 | Cát | Trời cho số phận có thể thành công | Nguồn hỗ trợ nào đã có nhưng bạn chưa sử dụng hoặc chưa biết cách đề nghị? |
| 07 | Cát | Ôn hòa êm dịu nhất phải thành công | Cách trao đổi nào giúp giữ hòa khí mà vẫn nói rõ giới hạn? |
| 08 | Cát | Qua giai đoạn gian nan, có ngày thành công | Bạn đang kiên trì với mục tiêu hay chỉ lặp một phương pháp chưa hiệu quả? |
| 09 | Hung | Tự làm có sức thất bại khó lường | Việc nào không nên tiếp tục phụ thuộc vào sức của một người? |
| 10 | Hung | Tâm sức làm không, không được đến bờ | Đầu ra nào cần hoàn tất thay vì tiếp tục tăng số việc đang làm? |
| 11 | Cát | Vững đi từng bước, được người trọng vọng | Lời hứa nhỏ nào bạn có thể thực hiện đều để xây sự tin cậy? |
| 12 | Hung | Gầy gò yếu đuối, mọi việc khó thành | Kế hoạch đang thiếu điểm tựa nào, không phải cơ thể bạn thiếu điều gì? |
| 13 | Cát | Trời cho cát vận, được người kính trọng | Bạn có thể cho người khác xem minh chứng cụ thể nào về năng lực? |
| 14 | Bình | Nửa được nửa bại, dựa vào nghị lực | Có thể thử lựa chọn này ở phạm vi nhỏ và điều chỉnh ở mốc nào? |
| 15 | Cát | Đại sự thành tựu, nhất định hưng vương | Việc lớn cần được chia thành những mốc bàn giao nào? |
| 16 | Đại cát | Thành tựu to lớn, tên tuổi lừng danh | Trách nhiệm nào sẽ tăng nếu công việc phát triển đúng mong muốn? |
| 17 | Cát | Quý nhân trợ giúp, sẽ được thành công | Bạn cần loại hỗ trợ nào và có thể đóng góp gì trong quan hệ hợp tác? |
| 18 | Đại cát | Thuận lợi xương thịnh, trăm việc trôi chảy | Quy trình nào nên được giữ ngay cả khi mọi việc đang thuận lợi? |
| 19 | Hung | Nội ngoại bất hòa, khó khăn muôn phát | Những bên liên quan đang khác nhau ở mục tiêu hoặc kỳ vọng nào? |
| 20 | Đại hung | Vượt mọi gian nan, lo xa nghĩ hoài | Bạn có thể giảm phạm vi vấn đề nào để không phải xử lý mọi thứ cùng lúc? |

## Các mã 21–40

| Mã | Nhãn nguồn | Lời nguồn giữ để đối chiếu | Câu hỏi ứng dụng |
| --- | --- | --- | --- |
| 21 | Cát | Chuyên tâm kinh doanh hay dung trí | Một vấn đề nào đáng để tập trung đến khi tạo được kết quả? |
| 22 | Hung | Có tài không vận, việc không gặp may | Năng lực nào chưa được đặt trong vai trò hoặc môi trường thích hợp? |
| 23 | Đại cát | Tên tuổi 4 phương, sẽ thành đại nghiệp | Bạn muốn được biết đến vì giá trị cụ thể nào, không chỉ vì xuất hiện nhiều? |
| 24 | Cát | Phải dựa tự lập sẽ thành đại nghiệp | Phần nào bạn tự quyết được và phần nào cần hợp tác rõ ràng? |
| 25 | Cát | Thiên thời địa lợi vì được nhân cách | Cơ hội, nguồn lực và cách đối nhân đang hỗ trợ nhau hay xung đột? |
| 26 | Hung | Bảo táp phong ba qua được hiểm nguy | Nếu một điều kiện quan trọng thay đổi, kế hoạch có phương án dự phòng không? |
| 27 | Cát | Lúc thắng lúc thua giữ được thành công | Kết quả nào cần được gìn giữ sau mỗi lần thử? |
| 28 | Đại cát | Tiến mãi không lùi trí tuệ được dung | Bạn có thể đưa năng lực đang có vào một nhiệm vụ rõ ràng nào? |
| 29 | Hung | Cát hung chia đổ, được thua mỗi nữa | Lợi ích và điều phải đánh đổi của lựa chọn hiện tại là gì? |
| 30 | Đại cát | Danh lợi được mùa đại sự thành công | Bạn phân biệt kết quả thật, sự ghi nhận và kỳ vọng bằng cách nào? |
| 31 | Đại cát | Con rồng trong nước thành công sẽ đến | Điều kiện nào còn thiếu để khả năng đang có được dùng trong thực tế? |
| 32 | Cát | Dùng trí lâu dài, sẽ được thịnh vượng | Việc nào vẫn có giá trị sau một năm, thay vì chỉ làm bạn bận tuần này? |
| 33 | Hung | Rủi ro không ngừng khó có thành công | Nguyên nhân chung nào xuất hiện trong những lần không đạt mục tiêu? |
| 34 | Bình | Số phận trung cất tiến lùi bảo thủ | Có thể chia quyết định thành bước nhỏ để giữ khả năng điều chỉnh không? |
| 35 | Hung | Trôi nổi bập bùng thường hay gặp nạn | Điểm ổn định nào có thể duy trì giữa những việc đang thay đổi? |
| 36 | Cát | Tránh được điểm ác, thuận buồm xuôi gió | Nút thắt nào có thể sửa trực tiếp thay vì chờ hoàn cảnh tự chuyển? |
| 37 | Bình | Danh thì được tiếng lợi thì bằng không | Công sức, sự ghi nhận và quyền lợi có được thỏa thuận rõ chưa? |
| 38 | Đại cát | Đường rộng thênh thang nhìn thấy tương lai | Bạn chọn hướng nào trước khi mở thêm nhiều cơ hội? |
| 39 | Bình | Lúc thịnh lúc suy chìm nổi vô định | Tiêu chí quyết định có thay đổi quá mạnh theo tâm trạng khi được hoặc mất không? |
| 40 | Đại cát | Thiên ý cất vận tiền đồ sang sủa | Cơ hội mới có phù hợp nguồn lực và mục tiêu của chính bạn không? |

## Các mã 41–60

| Mã | Nhãn nguồn | Lời nguồn giữ để đối chiếu | Câu hỏi ứng dụng |
| --- | --- | --- | --- |
| 41 | Hung | Sự nghiệp không chuyên hầu như không thành | Việc đang mở nào phải hoàn thành, bàn giao hoặc dừng? |
| 42 | Cát | Nhẫn nhịn chịu đựng, xấu sẽ thành tốt | Dấu hiệu nào cho thấy sự kiên nhẫn hiện tại đang có ích? |
| 43 | Cát | Cây xanh trổ lá đột nhiên thành công | Kết quả mới đến từ những chuẩn bị nào cần được tiếp tục? |
| 44 | Hung | Ngược với ý mình tham công lỡ việc | Kỳ vọng có đang vượt thời gian hoặc nguồn lực thực tế không? |
| 45 | Hung | Quanh co khúc khuỷu khó khăn kéo dài | Bước nào trên lộ trình không còn cần thiết hoặc cần cách làm khác? |
| 46 | Đại cát | Quý nhân giúp đỡ thành công đại sự | Bạn đã nói rõ điều cần giúp và trách nhiệm của mỗi bên chưa? |
| 47 | Đại cát | Danh lợi đều có thành công tốt đẹp | Kết quả có được duy trì cùng chất lượng và cam kết sau khi đạt mục tiêu không? |
| 48 | Bình | Gặp cát được cát gặp hung thì hung | Những điều kiện nào làm cùng một lựa chọn có kết quả khác nhau? |
| 49 | Bình | Hung cát cùng có, một thành một bại | Phần đã hoạt động tốt nào cần giữ, phần nào cần sửa? |
| 50 | Bình | Một thịnh một suy bập bùn sóng gió | Kết quả dao động vì hoàn cảnh hay vì cách làm liên tục thay đổi? |
| 51 | Cát | Trời quanh mây tạnh nay được thành công | Bài học cũ nào cần mang theo khi bắt đầu lại? |
| 52 | Hung | Sướng thịnh nửa số cát trước hung sau | Khởi đầu thuận lợi có cơ chế duy trì hay chỉ dựa vào một lần may mắn? |
| 53 | Bình | Nổ lực hết mình thành công ít ỏi | Hoạt động nào chiếm nhiều thời gian mà chưa tạo giá trị tương xứng? |
| 54 | Hung | Bề ngoài tươi sang ẩn họa sẽ tới | Thông tin nào chưa được kiểm tra phía sau vẻ hấp dẫn ban đầu? |
| 55 | Đại hung | Ngược lại ý mình, có có thành công | Có thể giữ mục tiêu nhưng thay phương pháp, quy mô hoặc thời điểm không? |
| 56 | Cát | Nổ lực phấn đấu phận tốt quay về | Một việc vừa sức nào có thể làm ngay để mở lại tiến trình? |
| 57 | Bình | Bấp bênh nhiều chuyến hung trước tốt sau | Bạn đang ở bước nào và điều gì đã được học từ giai đoạn khó? |
| 58 | Hung | Gặp việc do dự khó có thành công | Thông tin tối thiểu nào cần có để ra quyết định đúng hạn? |
| 59 | Bình | Mơ mơ hồ hồ khó có định phương hướng | Ba lựa chọn có thật nào cần được so sánh bằng tiêu chí rõ? |
| 60 | Hung | Mây che nửa trăng dấu hiệu phong ba | Giả định nào đang được dùng thay cho thông tin chưa biết? |

## Các mã 61–80

| Mã | Nhãn nguồn | Lời nguồn giữ để đối chiếu | Câu hỏi ứng dụng |
| --- | --- | --- | --- |
| 61 | Hung | Lo nghỉ nhiều điều mọi việc không thành | Điều gì có thể hành động và điều gì đang chỉ được lo nghĩ lặp lại? |
| 62 | Cát | Biết hướng nổ lực con đường phồn vinh | Hướng đi có được kiểm tra trước khi bạn tăng nỗ lực không? |
| 63 | Hung | Mười việc chín không mất công mất sức | Bao nhiêu việc đã được bàn giao so với số việc đang mở? |
| 64 | Cát | Cát vận tự đến, có được thành công | Bạn đã chuẩn bị năng lực và thời gian để tiếp nhận cơ hội chưa? |
| 65 | Bình | Nội ngoại bất hòa thiếu thốn tín nhiệm | Thỏa thuận nào cần được làm rõ để tăng sự tin cậy? |
| 66 | Đại cát | Mọi việc như ý phú quý tự đến | Nguồn lực thuận lợi đang có được sử dụng và gìn giữ thế nào? |
| 67 | Cát | Nắm được thời cơ, thành công sẽ đến | Dấu hiệu thực tế nào cho biết đây là lúc bắt đầu một bước đã chuẩn bị? |
| 68 | Hung | Lo trước nghĩ sau thường hay gặp nạn | Việc cân nhắc đang giúp quyết định hay chỉ kéo dài trì hoãn? |
| 69 | Hung | Bập bên khó tránh vất vả | Phần chưa ổn định nằm ở lịch, mục tiêu, trách nhiệm hay thông tin? |
| 70 | Bình | Cát hung đều có chỉ dự chí khí | Bạn có thể giữ chủ động bằng cách nào trong cả hai phía thuận và nghịch? |
| 71 | Hung | Được rồi lại mất khó có bình yên | Quy trình nào giúp giữ thành quả thay vì phụ thuộc trí nhớ một người? |
| 72 | Cát | An lạc tự đến tự nhiên cát tường | Điều gì làm đời sống vừa sức hơn mà không bỏ những trách nhiệm quan trọng? |
| 73 | Bình | Như là vô mưu khó được thành đạt | Kế hoạch đã có mục tiêu, nguồn lực, trình tự và tiêu chí hoàn tất chưa? |
| 74 | Bình | Trong lành có hung tiến không bằng lùi | Tiến, thu hẹp hay chờ thêm: phương án nào phù hợp điều kiện hiện tại? |
| 75 | Đại hung | Nhiều điều đại hung, hiện tượng phân tán | Những việc không có người chịu trách nhiệm nào cần được đóng hoặc phân công lại? |
| 76 | Cát | Khổ trước sướng sau, không bị thất bại | Điều gì đã cải thiện và điều gì vẫn cần thay cách làm? |
| 77 | Bình | Nửa được nửa mất sang mà không thực | Bạn đang đánh giá bằng hình ảnh bên ngoài hay sản phẩm có thật? |
| 78 | Đại cát | Tiền đồ tươi sang trăm đầy hy vọng | Hy vọng nào có thể chuyển thành một lựa chọn có thứ tự? |
| 79 | Hung | Được rồi lại mất lo cũng bằng không | Điểm phụ thuộc nào khiến kết quả khó được bảo toàn? |
| 80 | Đại cát | Số phận cao nhất, sẽ được thành công | Điều gì cần được hoàn tất, tổng kết và bàn giao trước khi mở chu kỳ mới? |
