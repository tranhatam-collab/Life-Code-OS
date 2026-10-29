# LIFE CODE OS — ALL-IN-ONE V3

## Kế hoạch hợp nhất để chuẩn bị triển khai

Ngày khóa bản bàn giao: **29/10/2026**. Founder: **Trần Hà Tâm**.

**Giữ nguyên V1 và V2. Bản này bổ sung và làm rõ; không tự phê duyệt phương pháp, quyền dữ liệu hoặc production.**

# 01. Phán quyết và phạm vi bàn giao

Life Code OS V3 là bản kế hoạch tích hợp, đặc tả và phòng thử tham chiếu. Bản này hợp nhất triết lý Huyền Nhân Học, các hệ số–tên, dòng đời, đồng nhịp sống, sản phẩm và kiến trúc vận hành. Không coi việc tăng số trang hoặc số mô-đun là bằng chứng hệ thống đã giải mã mọi con người.

Điểm thay đổi so với V2 là một hồ sơ đầu vào có thể đi qua nhiều mô-đun, nhưng kết quả vẫn giữ nguồn, quy tắc và mục đích riêng. Người dùng thấy một trải nghiệm thống nhất; hệ thống không hòa tan các phép tính khác nhau thành một lời phán không thể truy ngược. Bát Cực không còn chỉ là một bảng 64 cặp: có vị trí, chuỗi ba chữ số, ma trận chuyển nhóm, phần chưa giải, chẩn đoán quy tắc 0–5 và so sánh nhiều dãy. Bộ tên–ngày sinh mở đủ 23 thành phần đã được yêu cầu. Psychomatrix được tách khỏi ma trận chữ số thô.

Cấu trúc sản phẩm vẫn gồm chín cấp, 12 lớp và bốn khối Identity–Analysis–Timeline–Action. V3 bổ sung 18 lĩnh vực đời sống, chín giai đoạn điều hướng biên tập và 54 kịch bản nhập dữ liệu hoặc hành động. Đây là bản đồ nhu cầu, không phải yêu cầu mọi người phải trải qua cùng một kiểu hôn nhân, nghề nghiệp hay tuổi nghỉ hưu.

Mục tiêu phát hành ban đầu không đổi: xử lý P0, xây Trust Core, rồi mới mở Level 1, Numbers và kế hoạch 30 ngày cho người trưởng thành tự tạo hồ sơ. Báo cáo chuyên sâu, hồ sơ bên thứ ba, ảnh, trẻ em và sức khỏe vẫn cần cổng riêng. Không có cam kết gần như tuyệt đối về dự báo số phận; phần tính toán đúng theo quy ước và phần hữu ích cho người dùng phải được đánh giá riêng.

Trạng thái toàn hệ: **DESIGN + LOCAL REFERENCE; NOT PRODUCTION-READY**. Không sửa main, không migrate dữ liệu thật, không cấp quyền hoặc triển khai production trong lần bàn giao này.


# 02. Bảo toàn V1, V2 và đối chiếu GitHub

Bộ V1 ngày 11/10/2026 có 149 tệp. ZIP V2 ngày 20/10/2026 có 307 mục tệp, trong đó đã chứa bản bảo toàn V1. V3 giữ nguyên toàn bộ nội dung ZIP V2 dưới 01_BASELINES/V2_EXPORT, đồng thời giữ cả hai ZIP gốc. Mỗi tệp có SHA-256 trong manifest bảo toàn. Tài liệu cũ không bị sửa để làm cho các quyết định mới có vẻ luôn tồn tại.

Nguồn GitHub được đọc lại ngày 29/10/2026: main ở 99b402764437f81859fa0cd3a3af860125f7bd52; nhánh audit ở 336ef35a8386a744c6de18a7f7c6e268e89e6dac. Nhánh wip/rescue-20261027-codex-complete-upgrade-plan-2026-10-20 cùng trỏ về commit audit. Điều này chưa chứng minh toàn bộ gói V2 đã được nhập lên remote. Bản local trên máy của Founder và deployed SHA vẫn chưa được tiếp cận trong lần này. [R02, R03, R27]

Các trang công khai được truy xuất chỉ là bằng chứng nội dung ở bề mặt đã đọc; công cụ có thể trả bản crawl. Không dùng nội dung giống nhau để suy ra deployed SHA. Không gọi API hồ sơ người thật hoặc tạo giao dịch trên production để kiểm tra.

Thứ tự ưu tiên khi đọc: dữ kiện nguồn được giữ nguyên; quyết định V3 đang trình duyệt không giả là đã phê duyệt; thay đổi chỉ có hiệu lực sau khi được ghi trong decision register. Nếu tài liệu cũ nói bắt buộc mua level trước hoặc dùng coverage để mở mọi cấp, V3 ghi rõ phương án thay thế, không xóa dòng lịch sử.

Hướng nhập dự án là bổ sung dưới docs/upgrades/2026-10-29-v3/. Không ghi vào engine hiện chạy hoặc thư mục public. Công cụ nhập chỉ kiểm tra và sao chép; không tự commit, push, merge hoặc deploy. Việc nhập và triển khai là hai quyết định riêng.


# 03. Bản sắc Huyền Nhân Học trong sản phẩm all-in-one

Huyền Nhân Học giữ vai trò triết lý và phương pháp tổng hợp do Trần Hà Tâm định hướng. Life Code OS là hệ dữ liệu và phần mềm. Life Resonance là cách quan sát quan hệ giữa người với môi trường. Life Design là vòng hành động và xem lại. AI phục vụ truy xuất, giải thích, biên tập và tương tác; không được tự tạo ngày sinh, sự kiện, chẩn đoán, điểm số hoặc lời xác nhận quyền.

Phần sáng tạo HNH được tổ chức thành sáu quan hệ: nuôi dưỡng, cản trở, bù đắp, xung đột, chuyển tiếp và lựa chọn. Ví dụ, nhật ký cho thấy một người mất nhiều thời gian đi lại và khó hoàn thành việc học. Hệ thống có thể giúp xem lại lịch, vai trò, môi trường và một bước điều chỉnh. Không cần gọi thời gian đi lại là một tần số xấu để làm cho phân tích sâu hơn.

Một Code cá nhân không phải một căn số duy nhất. Nó là gói dữ liệu gồm danh tính được phép, các giả thuyết sinh, tên và phiên bản tên, kết quả phương pháp, quan sát theo thời gian, hoàn cảnh, lựa chọn, hành động và nguồn gốc. Các thành phần có thể thay đổi khác nhau: ngày sinh khai báo được sửa, mục tiêu đổi, tên công khai đổi, quyền chia sẻ bị thu hồi. Bản báo cáo phải phản ánh thời điểm chốt của riêng nó.

Sự hợp nhất không đồng nghĩa mọi môn đồng ý. Khi hai quy ước khác nhau, hệ thống trình bày nguyên nhân khác biệt. Khi ba chỉ số cùng xuất phát từ ngày sinh, không được đếm chúng như ba nguồn chứng minh độc lập. Khi người dùng không thấy một chủ đề phù hợp, lời phản hồi ấy phải được giữ, không được diễn giải thành “đúng ở tầng sâu mà anh chưa thấy”.

Triết lý “một đời người” vì thế bao gồm quyền không kể, quyền thay đổi, quyền không đồng ý và quyền giữ đời sống riêng. Một sản phẩm giúp con người không thể yêu cầu họ trao tất cả thông tin để nhận một lời giải thích đơn giản.


# 04. Toàn bộ nhu cầu một đời sống: 18 lĩnh vực

Dòng đời là danh mục nhu cầu có thể thay đổi, không phải một tuyến thành công duy nhất. Mỗi lĩnh vực có dữ liệu, mục tiêu, quyền và phương pháp phù hợp. Người học có thể ưu tiên học tập; người chăm sóc người thân ưu tiên lịch và hỗ trợ; người lớn tuổi ưu tiên tiếp nối và khả năng tiếp cận. Không ai bắt buộc chọn tất cả.

| Lĩnh vực | Dữ liệu cần thiết | Câu hỏi mở |
| --- | --- | --- |
| Bản sắc và quyền tự chủ | Tên gọi, vai trò, điều người dùng muốn được hiểu | Tôi muốn được gọi thế nào và ai có quyền xem hồ sơ? |
| Học tập và năng lực | Kỹ năng, sản phẩm học tập, mục tiêu, phản hồi | Điều gì đã học được và có minh chứng nào? |
| Công việc và vai trò | Kinh nghiệm, quyền hạn, tải việc, trách nhiệm | Vai trò nào phù hợp nguồn lực và mục tiêu hiện tại? |
| Nguồn lực và tài chính | Thu–chi, tài sản, nợ do người dùng nhập, đơn vị tiền | Điều gì cần được giữ, giảm hoặc tổ chức lại? |
| Quan hệ và ranh giới | Nhu cầu, cách đối thoại, thỏa thuận, quyền của mỗi bên | Tôi đang mong điều gì và đã nói rõ chưa? |
| Gia đình và trách nhiệm chung | Vai trò tự khai, lịch chung, quyền chia sẻ từng phần | Trách nhiệm nào là của tôi, của người khác hoặc cần thỏa thuận? |
| Nhà ở và môi trường | Không gian, thời gian đi lại, chi phí, an toàn | Nơi sống hỗ trợ hay làm khó hoạt động nào? |
| Cộng đồng và sự tham gia | Nhóm tham gia, nhu cầu hỗ trợ, đóng góp tự nguyện | Có thể đóng góp điều gì mà vẫn giữ giới hạn? |
| Cơ thể và tự chăm sóc | Quan sát tự khai, dữ liệu phù hợp có quyền, referral khi cần | Điều gì đang cần được trao đổi với chuyên gia phù hợp? |
| Nhịp sống và phục hồi | Lịch ngủ, nghỉ, vận động, thời gian, cảm nhận | Một điều chỉnh nhỏ nào thực hiện được trong tuần? |
| Ý nghĩa và niềm tin | Giá trị tự chọn, thực hành nội tâm, điều không muốn đánh đổi | Điều quan trọng với tôi có mặt trong việc tôi đang làm không? |
| Sáng tạo và biểu đạt | Bản thảo, sản phẩm, sở thích và thời gian thực hành | Tôi muốn tạo ra điều gì thay vì chỉ tiêu thụ? |
| Di chuyển và chuyển môi trường | Địa điểm, lịch đi lại, ngôn ngữ, nhu cầu hỗ trợ | Chuyển nơi sống cần chuẩn bị những điều kiện nào? |
| Chăm sóc và người phụ thuộc | Vai trò chăm sóc, sự ủy quyền, lịch và nguồn hỗ trợ | Cần phân chia trách nhiệm thế nào để không một người phải gánh tất cả? |
| Nghỉ hưu và đời sống lớn tuổi | Mục tiêu, nguồn lực, nhịp sống, khả năng tiếp cận | Bước tiếp theo nào vừa sức và có ý nghĩa? |
| Di sản và chuyển giao | Tri thức, tài liệu, người nhận, quyền truy cập và nguyện vọng | Điều gì cần được ghi lại, bàn giao hoặc giữ riêng? |
| Biến chuyển và mất mát | Sự kiện người dùng muốn kể, nguồn hỗ trợ, nhu cầu riêng tư | Người dùng muốn kể đến đâu và cần điều gì lúc này? |
| Đời sống số và danh tính | Tài khoản, thói quen màn hình, dữ liệu, quyền truy cập | Thông tin nào cần bảo vệ, giảm chia sẻ hoặc dọn lại? |

Một sự kiện có thể thuộc nhiều lĩnh vực, nhưng chỉ được lưu một nguồn gốc. Chuyển nơi sống có thể ảnh hưởng công việc, gia đình và lịch sinh hoạt; hệ thống tạo liên kết đến cùng sự kiện, không nhân bản thành ba bằng chứng độc lập.

Các nội dung nhạy cảm như mất mát, bệnh, khó khăn tài chính hoặc xung đột gia đình chỉ được xử lý trong phạm vi người dùng tự chọn. Bản đồ này không đưa ra ngày chết, tuổi thọ hoặc tiểu sử kiếp trước. Di sản là việc ghi lại và chuyển giao kiến thức, nguyện vọng, quyền truy cập theo quy trình phù hợp; các văn bản có hiệu lực pháp lý phải được chuyên gia pháp lý xử lý riêng.


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


# 06. Hai mươi họ tri thức và 62 adapter

Kho nguồn được giữ theo 20 họ K01–K20 của kế hoạch cũ. V3 cụ thể hóa thành 62 adapter, mỗi adapter có đầu vào, nguồn cần có, trường hợp biên và tiêu chí nghiệm thu. “Có trong registry” nghĩa là có vị trí trong chương trình nghiên cứu, không có nghĩa sách đã đọc hết hoặc công thức đã chạy production.

| Họ | Phạm vi |
| --- | --- |
| K01 | Lịch pháp, thiên văn và múi giờ |
| K02 | Bát tự, Tứ trụ, Tử Bình |
| K03 | Tử Vi Đẩu Số và mệnh bàn |
| K04 | Kinh Dịch, Mai Hoa, Lục Hào |
| K05 | Kỳ Môn, Lục Nhâm, Thái Ất |
| K06 | Phong thủy, Vastu, không gian |
| K07 | Jyotish, Nadi, truyền thống Ấn Độ |
| K08 | Chiêm tinh phương Tây và trung đại |
| K09 | Lịch và chiêm nghiệm khu vực |
| K10 | Thần số học, Psychomatrix, chữ–số |
| K11 | Bát Cực Linh Số, Mã đuôi 80, dãy số |
| K12 | Danh học, ngôn ngữ và ký hiệu |
| K13 | Bàn tay, khuôn mặt, bàn chân, hình thái |
| K14 | Tarot, Rune, Ifá, giấc mơ |
| K15 | Human Design, Gene Keys và hệ tổng hợp |
| K16 | Triết học, tôn giáo và nội tâm |
| K17 | Tâm lý học và đo lường |
| K18 | Hành vi, nghề nghiệp, kinh tế, xã hội |
| K19 | Sinh hoạt, môi trường, sức khỏe nền |
| K20 | Toán học, dữ liệu, AI và kỹ thuật |

Các adapter thời gian phải khóa lịch, múi giờ, timescale, tọa độ và sai số. Bát tự phải phân biệt nhật trụ, ranh giới ngày, giao tiết, chiều khởi vận và trường phái dụng thần. Tử vi phải khóa âm lịch, tháng nhuận, cách an sao và tuổi hạn. Jyotish phải chỉ định ayanamsa, hệ nhà, varga và daśā. Chiêm tinh phương Tây phải có ephemeris hợp pháp, hệ nhà và kiểm tra vùng vĩ độ cao. Không có bộ dữ liệu ấy thì không sinh một lá số giả bằng tên gọi quen thuộc. [R16, R17]

Nguồn Nadi, sách nâng cao Nguyễn Thu Nga và các tài liệu chưa được cung cấp toàn văn vẫn được ghi là cần bổ sung. Không tạo một “lá Nadi riêng” rồi coi đó là bản dịch tìm thấy trong bản thảo. Chuyển thể nội dung, bảng nghĩa, phần mềm tính và bản dịch cần được đánh giá quyền riêng. [R25]

Các phương pháp hình thái được giữ trong nghiên cứu, nhưng đầu ra sản phẩm không suy đạo đức, trí tuệ, tính cách, sức khỏe hoặc thu nhập từ ngoại hình. Bộ câu hỏi tâm lý cần có instrument, nguồn, đối tượng và quy trình dịch phù hợp; 120 câu tự quan sát không tự trở thành trắc nghiệm chuẩn hóa.


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


# 08. Bát Cực Linh Số: tích hợp ở mức chuỗi và quy tắc

V3 có bảng tám nhóm và 64 cặp; dãy gốc; cặp chồng lấn; chuỗi ba chữ số; vị trí đầu–giữa–đuôi; thống kê chuyển nhóm; số lặp; phần chưa phân loại; và lớp câu hỏi HNH. Chuỗi 4134 tạo 41–13–34; 4314 tạo 43–31–14. Cùng tổng chữ số nhưng thứ tự nhóm khác nhau.

Nguồn công khai dùng tên “từ trường” và những luận giải cát–hung. V3 giữ đây là thuật ngữ trường phái, không xác nhận dãy số có từ trường vật lý chữa bệnh hoặc tăng thu nhập. Các nguồn thực hành được đối chiếu để hiểu quy tắc, không được gắn nhãn nghiên cứu thực nghiệm. [R04, R05]

Ba chế độ được tách. Strict giữ nguyên dãy và đánh dấu cặp có 0/5 chưa xử lý. Diagnostic chỉ thêm một cầu A0B hoặc A5B khi đúng một ký tự đặc biệt nằm giữa hai chữ số được hỗ trợ; không xóa cặp gốc. Full traditional context vẫn chờ nguồn chi tiết về cường độ, chuỗi dài, chế hóa và tiên thiên–hậu thiên. Chuỗi 8553 không bị rút thành 83 trong diagnostic mới.

64 ô chuyển nhóm 8×8 được dùng để tổ chức câu hỏi mới của HNH. Chúng không được gọi là 64 điều cổ truyền hoặc một danh mục toàn bộ chuỗi ba chữ số. Với tập tám chữ số hỗ trợ có 512 chuỗi ba chữ số; cấu trúc nối chung chữ số giữa phải được giữ, không chỉ chọn hai cặp rời.

Các ví dụ nguồn công khai 876 và 678 có xung đột giữa bảng cặp và lời minh họa. V3 ghi nhận xung đột, giữ cách tính theo bảng được khai báo và không dùng câu văn thuận lợi để ghi đè kết quả. Bảng rank cường độ chưa đủ nguồn không được tự chuyển thành trọng số 4–3–2–1. [R04]

So sánh SIM giữ các kết quả riêng: cấu trúc dãy, tổng chữ số, Mã đuôi 80, giá và tình trạng sử dụng do người dùng nhập. Không tạo điểm hợp người mặc định. Hai dãy đồng thống kê phải được phép đồng hạng; chỉ phân biệt khi có tiêu chí bổ sung được công bố.


# 09. Mã đuôi 80 và Psychomatrix trong cùng hồ sơ

Mã đuôi 80 nhận đúng bốn chữ số, tính divmod(N,80) bằng số nguyên. Số dư thuộc 0–79; bảng nguồn lại đánh 1–80. Vì vậy zero_policy phải được chọn: unmapped hoặc as80. Không dùng r+1 làm lệch tất cả mã. Không dùng số thực rồi cắt phần thập phân; phép tính trực tiếp có thể sai do biểu diễn máy.

80 mục giữ nguyên nhãn và lời nguồn người dùng cung cấp, đồng thời có theme, câu hỏi và hành động biên tập riêng. Mục 34 và 55 được gắn lưu ý câu chữ gốc chưa rõ. Chưa khẳng định bảng 80 có một nguyên bản lịch sử duy nhất hoặc giống bảng 81. [R28]

Một mã đại diện 125 đuôi trong miền 0000–9999. Cộng 80 không đổi mã. Với phép số dư 80, tính toàn bộ số thập phân và tính bốn số cuối cho cùng số dư vì 10.000 chia hết 80. Tính chất này không áp dụng cho tổng chữ số hay cặp liền nhau. Phương pháp không nhận ngày sinh nên không tạo độ hợp riêng cho từng người.

Psychomatrix có hai chế độ rõ: đếm chữ số gốc và đếm sau khi thêm bốn số phụ. Trong cấu hình trừ được mô tả, W1 là tổng chữ số ngày sinh; W2 là tổng chữ số W1; W3=W1−2 × chữ số đầu ngày không có 0 đệm; W4 là tổng chữ số W3. Nếu W3 âm, cấu hình này từ chối, không lấy trị tuyệt đối hay tự áp một biến thể sau năm 2000. Nguồn Nga được nhận diện qua trích đoạn; toàn văn và quyền sử dụng vẫn cần đối chiếu. [R15]

Chín ô và tám đường là kết quả đếm. Thiếu 9 không có nghĩa trí nhớ kém, thiếu 4 không có nghĩa sức khỏe yếu. Trục 3–5–7 được trình bày bằng tên hình học trung tính; không suy đời sống thân mật từ ngày sinh. Đặc biệt không tạo nội dung tình dục cho hồ sơ trẻ em.


# 10. Một hồ sơ, nhiều không gian sản phẩm

All-in-one là sự thống nhất về tài khoản, dữ liệu có quyền, thư viện kết quả, thanh toán và trải nghiệm; không phải tất cả thông tin đều được mọi mô-đun đọc. Người dùng chọn nhu cầu, hệ thống giải thích dữ liệu cần thiết và chỉ chạy phương pháp đã được phát hành.

Profile version là bản chốt dữ liệu. Analysis bundle lưu danh sách phương pháp, phiên bản nguồn, giả thuyết, cấu hình và quyền ở thời điểm tạo. Mỗi method result độc lập. Bộ tổng hợp sử dụng những kết quả được phép, ghi nhận phần khác nhau và không tự tạo một số “chung cuộc” nếu thiếu phép đo phù hợp.

Một người có thể làm bộ tên hôm nay, nhật ký hành vi tháng sau và hồ sơ nguồn lực năm sau. Dữ liệu có thể liên kết khi mục đích và quyền cho phép, nhưng không ép người đó trả tiền lại cho cùng một phép tính không đổi. Phí mới cần gắn với phạm vi phân tích, cập nhật, rà soát hoặc dịch vụ thực tế.

Hệ thống phân biệt account, profile_subject và tenant. Người trả tiền không tự có quyền đọc hồ sơ người khác. Một người tải ảnh lên không được mặc nhiên xác nhận là người trong ảnh. Đối với nhiều người cùng một báo cáo quan hệ, mỗi người có quyền riêng theo mục và có cơ chế thu hồi; một người không được tải bản đầy đủ của người kia chỉ vì quan hệ gia đình.

Demo V3 thực hiện một intake tham chiếu với lựa chọn mô-đun, bốn khối xem trước và thông báo phần thiếu. Nó không có đăng nhập, lưu trữ, thanh toán, AI provider hoặc việc phát hành đủ chín sản phẩm. Điều này được ghi ngay trong giao diện và receipt, không giấu ở cuối tài liệu.


# 11. Chín cấp sản phẩm và bộ báo cáo đầy đủ

Tên chín cấp của GitHub được giữ. Cơ chế mở khóa cũ theo coverage không được dùng để tự coi một người đủ điều kiện nhận mọi báo cáo. Phương án V3 là quyền sản phẩm, quyền dữ liệu, mục đích xử lý, phương pháp phát hành và đầu vào cần thiết. [R27]

| Cấp | Mục tiêu | Đầu vào tăng thêm | Độ dài tham chiếu |
| --- | --- | --- | --- |
| 1 Self Signal | Tín hiệu nền | Tên, ngày sinh khi phương pháp cần, mục tiêu; giờ/nơi có thể thiếu | 30–50 trang, không bắt buộc |
| 2 Inner Architecture | Cấu trúc nội tâm | Giá trị, vai trò, nhu cầu, tình huống do chủ thể kể | 40–60 trang, không bắt buộc |
| 3 Behavior Code | Hành vi và mô thức | Nhật ký và bảng hỏi phù hợp | 50–70 trang, không bắt buộc |
| 4 Work & Wealth Code | Công việc và nguồn lực | Kỹ năng, việc làm, nguồn lực và thu–chi có đơn vị | 50–80 trang, không bắt buộc |
| 5 Relationship Field | Quan hệ và ranh giới | Nhu cầu, lịch sử tự thuật; quyền dữ liệu từng bên | 50–80 trang, không bắt buộc |
| 6 Life Timeline | Dòng đời và phương án | Sự kiện có ngày, giả thuyết thời điểm và kế hoạch | 60–100 trang, không bắt buộc |
| 7 Body Intelligence | Cơ thể và môi trường | Quan sát có quyền, nhật ký sinh hoạt; ảnh tùy chọn | 60–120 trang, không bắt buộc |
| 8 Mission Path | Hướng sống và phụng sự | Giá trị, năng lực có minh chứng, lựa chọn tự nguyện | 80–150 trang, không bắt buộc |
| 9 Full Life Code | Hồ sơ đời sống hợp nhất | Các kết quả được phép và dữ liệu chủ thể đồng ý | 150–600 trang, không bắt buộc |

Mọi báo cáo đều có dữ liệu gốc, phạm vi, những điều chưa biết, kết quả tính, loại nhận định, nguồn, câu hỏi và hành động. Level 1 giữ đủ 14 mục đã yêu cầu: bìa; Source of Truth; Input Completeness; Data Coverage; LCI status; Identity; Name; Chrono; Birth Matrix; Current Cycle; Risk Signals đúng giới hạn; Mission Options; 30-Day Action; Disclaimer. Nếu LCI chưa được xác lập, mục đó vẫn hiện với giải thích và giá trị null, không điền điểm giả để đủ khung.

Level 2 cần tình huống và giá trị tự thuật. Level 3 cần nhật ký hoặc instrument phù hợp. Level 4 cần nguồn lực thực và đơn vị tiền. Level 5 cần quyền chia sẻ nhiều chủ thể. Level 6 tách lịch sử, chu kỳ và dự định. Level 7 chỉ quan sát hình thái, không “đọc tâm can” qua ảnh. Level 8 trả những hướng sống để lựa chọn. Level 9 hợp nhất và loại lặp, không nối tám tệp rồi gọi là cuốn sách mới.

Chín mẫu cấu trúc được giao trong 06_PRODUCTS. Ngân sách trang không là cam kết mọi hồ sơ sinh đủ trang. Phần giáo trình chung, phép tính, cá nhân hóa và bài tập cần được gắn loại nội dung; không để người dùng nhầm 20 trang hướng dẫn chung là 20 trang dữ kiện riêng của họ.


# 12. Chuỗi miễn phí, cá nhân, chuyên gia và tổ chức

Toàn bộ 23 sản phẩm V2 được giữ. V3 mở thêm năm dòng chuyên biệt: Numbers & Names Atlas, Living Life Map, Knowledge Legacy, Territory Kit và Research Studio. Tổng 28 bản ghi là danh mục dự kiến, không phải 28 dịch vụ đã mở bán. Những sản phẩm có phạm vi gần nhau phải được quản lý bằng gói quyền sử dụng, tránh xây nhiều phần mềm trùng chức năng.

Miễn phí có hai trải nghiệm. Khách có thể dùng một công cụ cục bộ phù hợp mà không tạo tài khoản. Tài khoản Free Essentials có mục tiêu, nhật ký và kết quả trong hạn mức công khai. Quyền sửa, tải hoặc yêu cầu xóa dữ liệu không nằm sau việc mua gói cao hơn. Hạn mức AI được tính theo ngân sách dịch vụ, không đổi lấy quyền khai thác dữ liệu riêng tư để quảng cáo.

Báo cáo cá nhân một lần có phạm vi, bản chốt dữ liệu, định dạng giao, số lần chỉnh sửa và người rà soát. Companion cung cấp theo dõi mục tiêu, giải thích và nhắc việc do người dùng chọn. Trước khi thanh toán, giao diện phải nói rõ dữ liệu bắt buộc, phần chưa hỗ trợ và cách xử lý khi không thể hoàn thành dịch vụ. Không tăng giá bằng việc gán người dùng là người có “sứ mệnh đặc biệt”.

Practice quản lý ca được chia sẻ, lịch hẹn, ghi chú và bản nháp. Academy tổ chức chương trình học và tiêu chuẩn chứng nhận. Family có quyền riêng theo từng thành viên và luồng trẻ em được đánh giá riêng. Workspace chỉ sử dụng dữ liệu phù hợp mục đích công việc; người trả tiền cho tổ chức không được tự đọc nhật ký hoặc hồ sơ sức khỏe của thành viên.

Publishing và API dùng chung lõi phương pháp. Đối tác được cấp phạm vi nội dung, mức sử dụng, vùng xử lý dữ liệu và điều kiện thương hiệu. Đối tác không được sửa bảng nghĩa để tối ưu doanh số rồi giữ tên “Life Code chính thức”. Việc ngừng giấy phép phải được thiết kế để người dùng vẫn thực hiện được quyền dữ liệu hợp lệ.

Trải nghiệm thương mại không bắt mua tuần tự từ Level 1 đến Level 9. Điều kiện mở một sản phẩm là quyền sản phẩm, quyền truy cập chủ thể, mục đích xử lý, phương pháp được phép phát hành và đầu vào cần thiết. Người muốn lập kế hoạch nghề nghiệp không phải cung cấp ảnh chân hoặc mua phân tích quan hệ trước.


# 13. Backend và các ranh giới nghiệp vụ

Giữ kiến trúc khối ứng dụng mô-đun như kế hoạch cũ. Website công khai, ứng dụng và cổng chuyên gia gọi cùng API gateway/BFF. Lõi phương pháp là package độc lập. PostgreSQL quản lý nghiệp vụ; R2 lưu tệp riêng tư; hàng đợi và transactional outbox xử lý công việc dài. Tiến trình xuất sách chạy trong môi trường hạn chế mạng và hệ thống tệp. [R03, R18, R19]

Các miền nghiệp vụ gồm danh tính, quyền chủ thể, mục đích và sự đồng ý, hồ sơ có phiên bản, kho tri thức, thực thi phương pháp, quan sát, đồng nhịp, nhận định, báo cáo, kế hoạch, thương mại, chuyên gia, học viện và lãnh thổ. Không chia một dịch vụ nhỏ cho mỗi môn. Chỉ tách tiến trình khi tải, quyền hoặc vòng đời vận hành cần khác nhau.

Gateway lấy principal từ phiên xác thực. Dữ liệu user_id do trình duyệt gửi không được tạo quyền. Mỗi analysis run chốt phiên bản hồ sơ, giả thuyết ngày sinh, phương pháp, bảng nguồn, cấu hình, mục đích, phiên bản quyền và ngôn ngữ. Kiểm tra quyền diễn ra khi tạo tác vụ, khi worker nhận việc, trước khi phát hành và khi tải kết quả. Tác vụ đang chờ không được tiếp tục công bố sau khi chủ thể rút quyền.

V3 giữ 83 thao tác API V2, bổ sung 16 thao tác đích, tổng cộng 99. Đây là hợp đồng thiết kế. Demo cục bộ chỉ có ba route nghiệp vụ: health, catalog và run; các tệp giao diện là tài nguyên tĩnh. Không lấy số lượng endpoint trong đặc tả làm số lượng chức năng production đã triển khai.

RLS là lớp phòng vệ bổ sung. Tài khoản ứng dụng không là chủ bảng hoặc có quyền BYPASSRLS. Khóa ngoại cho dữ liệu riêng tư cần gắn tenant và subject để ngăn bản ghi con tham chiếu sang chủ thể khác. Mọi chính sách phải được thử bằng tài khoản thực trong staging, không chỉ đọc SQL hoặc nhìn sơ đồ. [R19, R24]

Đường đọc dữ liệu cần giới hạn theo quyền ngay trong truy vấn. Đường ghi dùng schema đóng, chống mass assignment, kiểm tra phiên bản hồ sơ và nhật ký thay đổi. Những tác vụ sửa quyền, xuất dữ liệu, xóa hoặc cấp entitlement phải có audit event không chứa bí mật truy cập.


# 14. Dữ liệu, công thức và ma trận phụ thuộc

Trục dữ liệu giữ các thực thể account, profile_subject, access_grant, consent, processing_purpose, profile_version, data_hypothesis, method_release, source_edition, observation, analysis_run, method_result, claim, report_snapshot, action_plan, order, entitlement, practitioner_case, audit_event và deletion_job. V3 bổ sung số–tên có phiên bản, comparison run, phân đoạn chuỗi số, xung đột nguồn, lĩnh vực đời sống và chuyển giao tri thức.

Mỗi công thức khai báo đầu vào, cách chuẩn hóa, bảng hằng số, phiên bản, độ chính xác, cách xử lý dữ liệu thiếu, đầu ra và kiểm thử. Không cho người biên tập nhập JavaScript tùy ý vào bảng quy tắc production. Điều văn, tài liệu truy xuất và prompt là dữ liệu; công cụ không thực thi chúng như mã hoặc như lệnh đổi quyền.

Đồ thị phụ thuộc — DAG — phải phát hiện nút trùng, thiếu phụ thuộc và vòng lặp trước khi chạy. Các nút độc lập có thể chạy song song với giới hạn tài nguyên. Khi thay bảng tên, các chỉ số tên và nội dung phụ thuộc được đánh dấu cần tính lại; lịch sử do người dùng cung cấp không bị sửa. Khi đổi giả thuyết ngày sinh, chỉ những nút phụ thuộc ngày sinh được tính lại. Báo cáo đã xuất không âm thầm đổi nội dung mà không có phiên bản mới.

Bộ hợp nhất tránh tính trùng. Life Path, năm cá nhân và ma trận ngày sinh đều dùng cùng DOB nên không được xem là ba nguồn chứng minh riêng. Ba bài viết sao chép một sách cũng không phải ba nguồn độc lập. Mỗi nhận định có đồ thị phụ thuộc và danh sách nguồn, ghi rõ quan hệ kế thừa.

Giá trị cần độ chính xác được biểu diễn bằng số nguyên, phân số hoặc chuỗi thập phân theo hợp đồng. Số dư 80 dùng số nguyên. Tiền dùng đơn vị nhỏ nhất kèm mã tiền tệ, không cộng chéo khi thiếu tỷ giá có nguồn. Thiếu mẫu số thì tỷ lệ là null, không gán 0 để bảng trông đầy đủ.

Chỉ số truyền thống có tên như Rational Thought hay Subconscious Confidence không được tự biến thành điểm đo tư duy hoặc độ tự tin thống kê. Bộ máy trả kết quả quy ước, cách tính và giới hạn; lớp biên tập giải thích ý nghĩa của tên gọi và cho phép người dùng không đồng ý với phần tự suy ngẫm.


# 15. Queue, idempotency, cache và tính lại

Cloudflare Queues có cơ chế giao ít nhất một lần. Cùng một thông điệp có thể được xử lý lại; ứng dụng phải quản lý hiệu ứng nghiệp vụ, không hứa hàng đợi chỉ chạy một lần. [R18]

Tạo run, idempotency receipt và outbox event trong cùng giao dịch cơ sở dữ liệu. Khóa idempotency có phạm vi tài khoản, thao tác và mục đích. Cùng khóa, cùng payload trả lại receipt trước; cùng khóa nhưng khác payload trả lỗi xung đột. Worker cần lease, heartbeat, retry có giới hạn, thời gian chờ tăng dần, hàng đợi lỗi và công cụ rà soát lại. Không giữ một HTTP request để dựng 600 trang trong vòng lặp không có giới hạn.

Cache phải gắn tenant, subject, purpose, access revision, input digest, method release, source digest và locale release. Không tạo cache chung theo ngày sinh rồi trả dữ liệu riêng của người khác. Hash phục vụ tái lập không đồng nghĩa ẩn danh; dữ liệu đầu vào dễ đoán vẫn có thể bị đối chiếu. Nhật ký không ghi tên, ngày sinh, prompt riêng hoặc URL tải nếu không thật sự cần.

Hủy tác vụ là trạng thái có lịch sử. Worker kiểm cờ hủy tại các điểm an toàn. Khi có yêu cầu xóa, deletion barrier chặn tác vụ mới và phát hành mới; khôi phục backup phải áp lại các chỉ thị xóa trước khi mở truy cập. Báo cáo đã tải về không thể thu hồi vật lý từ thiết bị người nhận, vì vậy giao diện không được hứa làm được điều đó.

Giới hạn công việc gồm số phương pháp trong một run, kích thước dữ liệu, số dãy so sánh, thời gian chạy, số lần gọi AI, kích thước tệp xuất và số lần thử lại. Các giới hạn phải trả lỗi đọc hiểu được, không chỉ mã lỗi kỹ thuật.

Hiệu năng được đo theo lớp: phép tính ngắn, tổng hợp hồ sơ, xuất tệp, AI và truy xuất. Benchmark máy cục bộ chỉ mô tả môi trường đó; không được chuyển thành SLA công khai hoặc chứng nhận độ chính xác về cuộc đời.


# 16. Frontend, mobile web, desktop và native app

Giữ URL công khai và nội dung có giá trị của website hiện có. Những lời hứa vượt căn cứ cần được biên tập lại mà không xóa lịch sử quyết định. Ứng dụng mới dùng chung API và cấu trúc nội dung; giao diện không tính lại công thức theo một cách khác. Astro cho nội dung công khai và React/Vite cho ứng dụng là phương án đích đã đề xuất; quyết định chuyển đổi cần đối chiếu repository thực.

Màn hình đầu hỏi nhu cầu thay vì ép nhập hồ sơ dài. Mỗi bước nói rõ vì sao cần thông tin, bắt buộc hay tùy chọn, ai được xem và cách sửa. Các trạng thái sẵn sàng, có một phần, cần bổ sung, chính sách chưa hỗ trợ, phương pháp chưa phát hành, thiếu quyền, kết quả cũ và tác vụ lỗi phải có lời giải thích riêng.

Dashboard ưu tiên mục tiêu và những việc có thể làm hôm nay. Các chỉ số số học nằm trong khu vực tham khảo có nhãn; dấu vết phép tính có thể mở rộng. Trên mobile, 23 chỉ số và bảng cặp số được trình bày bằng thẻ hoặc bảng cuộn có tiêu đề rõ. Desktop hỗ trợ thanh điều hướng và so sánh nhiều dãy. Không bắt người dùng đọc JSON để hiểu kết quả.

Demo có giao diện responsive. Native iOS/Android chưa được triển khai; chỉ mở khi nhật ký ngoại tuyến, camera hoặc thông báo tạo giá trị rõ. Native dùng chung lõi, không có bộ công thức riêng. Dữ liệu riêng tư không được lưu ngoại tuyến mặc định. Đăng xuất, đổi chủ thể, thu hồi quyền và xóa dữ liệu đều cần xử lý cache tương ứng. Thông báo không đưa nội dung nhạy cảm lên màn hình khóa.

Mục tiêu WCAG 2.2 AA cho các luồng chính gồm điều hướng bàn phím, focus, nhãn trường, độ tương phản, phóng to, thông báo lỗi và giảm chuyển động. Kiểm tra ảnh chụp ở bốn kích thước chỉ là một phần QA, không phải chứng nhận khả năng truy cập đầy đủ. [R20]

Nội dung tiếng Việt được duyệt trước, bản dịch giữ nguyên mức khẳng định. Không dịch “chủ đề tham khảo” thành “sự thật chắc chắn”. Tên người không được dịch hoặc bỏ dấu âm thầm. Ngôn ngữ giao diện, thị trường, nơi cư trú và vùng lưu trữ là các trường khác nhau, không suy tất cả từ địa chỉ IP.


# 17. AI đồng hành và mức tự chủ

AI là trợ lý trong một hệ quyền hạn, không đứng trên cổng API. Các vai trò gồm trợ lý nhập dữ liệu, truy xuất nguồn, giải thích công thức, viết nháp, rà nội dung, hỗ trợ mục tiêu và tổng hợp vận hành. Một mô hình không được là người duy nhất vừa tính, vừa xác nhận nguồn và vừa duyệt phát hành.

A0 chỉ đề xuất. A1 thực hiện tác vụ đọc đã được cho phép, như giải thích kết quả đã chốt. A2 thực hiện việc có thể đảo trong hạn mức đã duyệt, như tạo bản nháp hoặc nhắc việc người dùng đăng ký. A3 là tự động hóa vận hành theo playbook có điều kiện, kèm công tắc dừng và người chịu trách nhiệm. Mở quyền dữ liệu, phát hành phương pháp, giao dịch ngoài chính sách, triển khai production hoặc ký nhượng quyền không được tùy ý giao cho A3.

Truy xuất tăng cường — RAG — phải kiểm quyền trước khi lấy nội dung. Tài liệu nguồn và lời người dùng không được xem là lệnh thay quyền. Bộ viết chỉ nhận các claim và trích đoạn được phép. Không đưa toàn bộ hồ sơ khác vào ngữ cảnh để trả lời một câu hỏi. Yêu cầu về một người thứ ba không tạo quyền đọc hồ sơ của người ấy.

Ngân sách AI được giới hạn theo tài khoản và tác vụ: token, chi phí, retry, model dự phòng, thời gian và ngưỡng dừng. Khi nhà cung cấp lỗi, hệ thống có thể trả phần phép tính đã hoàn thành hoặc đưa tác vụ vào hàng chờ xem lại. Không chuyển dữ liệu sang nhà cung cấp khác có chính sách xử lý rộng hơn mà không đánh giá quyền và mục đích.

Giảm thao tác quản trị bằng hàng chờ ngoại lệ và bằng chứng rõ, không bằng việc bỏ trách nhiệm. Người duyệt xem phần thay đổi, nguồn và rủi ro; các phần máy kiểm được có receipt riêng. Người dùng được biết đang tương tác với AI và luôn có đường sửa dữ liệu, báo sai hoặc kết thúc phiên.

Phản hồi “rất đúng với tôi” có thể được lưu như trải nghiệm tự thuật, không tự tăng độ chính xác của phương pháp. Việc học từ dữ liệu người dùng là chương trình nghiên cứu riêng, có mục đích, quyền, phạm vi và cách đánh giá; không diễn ra ngầm trong sản phẩm trả phí.


# 18. Báo cáo, PDF, Word và Living Book

Một report snapshot chốt phiên bản hồ sơ, giả thuyết, phương pháp, claim IDs, dữ liệu và quyền sử dụng. Cây nội dung có section ID, tiêu đề, mục đích, tham chiếu claim, đoạn văn, bảng, hình, câu hỏi, hành động và giới hạn. Web, PDF và Word dựng từ cùng một cấu trúc, không viết ba bài khác nhau.

PDF cần chữ chọn được, mục lục, dấu trang, số trang và nguồn. Word dùng kiểu tiêu đề và bảng thật. Trình render chỉ đọc tài nguyên được phép, không tự tải URL từ nội dung người dùng hoặc đọc đường dẫn hệ thống tùy ý. Tệp ở kho riêng tư; việc tải được kiểm quyền hoặc dùng liên kết ngắn hạn theo chính sách. Không đóng gói bí mật, log nội bộ hoặc phông chữ máy chủ vào sách.

Living Book không có nghĩa một báo cáo đã ký tự đổi mỗi ngày. Mỗi phiên bản bất biến; người dùng xem được phần thay đổi. Bản sai được rút hoặc thay thế bằng bản mới có lý do. Khi người dùng rút quyền với một nguồn, không sinh báo cáo mới từ nguồn đó. Hệ thống giải thích giới hạn với những bản đã tải về trước đây.

Khả năng 150–600 trang chỉ áp dụng khi nội dung và dữ liệu tương xứng. Không lặp một đặc điểm qua chín cấp để sách dày hơn. Phần triết lý chung và bài tập có nhãn riêng; phần cá nhân hóa phải truy về dữ liệu hợp lệ. Ngữ nghĩa tên chưa rõ thì trình bày các khả năng và nguồn, không chọn một nghĩa rồi coi là bằng chứng nội tâm.

Quy trình biên tập gồm kiểm dữ kiện, phép tính, đúng chủ thể, chính tả, trùng lặp, phạm vi khẳng định, nguồn và bố cục. Một sách dài có thể chia thành phần để xử lý, nhưng chỉ phát hành sau khi kiểm mục lục, liên kết, số trang, tham chiếu và tính nhất quán toàn cuốn.

Chân trang ghi Life Code OS, địa chỉ hệ thống, phiên bản và mức riêng tư thích hợp. Địa chỉ website là nguồn hệ thống, không phải nguồn khoa học cho mọi câu trong sách. Mỗi nội dung ngoài dữ liệu tự khai cần có nguồn riêng hoặc nhãn diễn giải rõ.


# 19. Dữ liệu nhạy cảm, trẻ em và giới hạn sử dụng

Dịch vụ đầu tiên dành cho người trưởng thành tự lập hồ sơ. Mở hồ sơ gia đình, trẻ em, người được ủy quyền hoặc tổ chức phải có mục đích, vai trò, sự đồng ý và chính sách phù hợp. Người thanh toán không tự trở thành chủ sở hữu mọi dữ liệu. Không suy giới tính, quan hệ hoặc danh tính chỉ từ ảnh hoặc tên.

Ảnh mặt, tay và chân được xử lý trong phạm vi rõ; loại bỏ metadata vị trí khi không cần. Không nhận diện danh tính người thật trong ảnh hoặc suy nhân cách, đạo đức, trí thông minh, bệnh hay khả năng kiếm tiền từ hình thái. Thuật ngữ truyền thống được lưu trong kho nghiên cứu không đồng nghĩa được phép áp làm kết luận về người dùng.

Trẻ em không bị gắn nhãn nghề, thiên tài, trí nhớ kém hoặc sứ mệnh bắt buộc. Không có đánh giá đời sống thân mật từ ma trận. Nội dung sức khỏe giới hạn ở quan sát, lối sống phù hợp và câu hỏi để trao đổi với chuyên gia. Không hướng dẫn chọn cá cược, thuốc hoặc quyết định điều trị bằng số.

Dữ liệu dịch vụ và dữ liệu nghiên cứu có mục đích riêng. Đồng ý nhận báo cáo không tự là đồng ý huấn luyện AI. Xuất, sửa, rút quyền và xóa cần đi qua cơ sở dữ liệu, R2, chỉ mục tìm kiếm, cache, dữ liệu tại nhà cung cấp và lịch lưu giữ backup. Audit không lưu nội dung nhạy cảm vô thời hạn. Bản phục hồi cần áp lại các quyết định xóa trước khi mở cho người dùng.

Pháp lý Việt Nam cần rà soát theo hoạt động thực tế: Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 có hiệu lực 01/01/2026; Luật Trí tuệ nhân tạo 134/2025/QH15 từ 01/03/2026; Luật Thương mại điện tử 122/2025/QH15 từ 01/07/2026. Trong lần nghiên cứu này đã đối chiếu thông tin văn bản chính thức, chưa có ý kiến pháp lý riêng xác nhận đủ điều kiện mở bán. [R21, R22, R23]

Một câu disclaimer không khắc phục một API sai quyền hoặc lời quảng bá gây hiểu nhầm. Pháp nhân cung cấp dịch vụ, đơn vị thu tiền, bên kiểm soát dữ liệu và nhà cung cấp xử lý phải được xác định trước khi triển khai.


# 20. Thương mại, chi phí và chất lượng dịch vụ

Đơn hàng, thanh toán, entitlement, trạng thái tác vụ và báo cáo là năm đối tượng riêng. Trình duyệt quay về trang thành công không đủ để mở quyền. Máy chủ phải đối chiếu sự kiện nhà cung cấp, chữ ký, số tiền, mã tiền tệ, mã đơn và trạng thái hoàn tiền. Retry không được tạo khoản thu, quyền sử dụng hoặc email giao hàng lặp.

Free Essentials có hạn mức rõ, không yêu cầu ảnh hoặc số định danh đầy đủ để chạy một công cụ bốn chữ số. Phí báo cáo một lần gắn với phạm vi, định dạng, số lần chỉnh và rà soát. Phí Companion gắn với năng lực sử dụng theo kỳ. Phí chuyên gia gắn với dịch vụ và trách nhiệm. API và cấp phép có giới hạn nghiệp vụ, dữ liệu và thương hiệu.

Chi phí trực tiếp gồm tính toán, AI, biên tập, lưu trữ, hỗ trợ và phí thanh toán. Giá cần thêm dự phòng, thuế và biên lợi nhuận đã duyệt. Workbook để trống đơn giá chưa có báo giá; không điền 0 rồi gọi dịch vụ miễn phí vận hành. Các ước lượng V2 là phần làm rõ công việc cha; không tự cộng cả hai thành tổng mới.

Trước pilot cần chọn ngưỡng chi phí cho một lần đọc, tỷ lệ cần người hỗ trợ, thời gian xử lý ngoại lệ và giới hạn số lần sinh lại báo cáo. Khi đạt hạn mức, hệ thống trả thông báo và lựa chọn phù hợp, không âm thầm cắt phần quan trọng hoặc lấy tiền từ tài khoản khác.

Chất lượng pilot đo bằng việc người dùng hiểu loại nội dung, sửa được dữ liệu, chọn hành động, theo dõi tiến độ và được hỗ trợ khi có lỗi. Mức “cảm thấy lời luận đúng” được ghi riêng, không thay độ chính xác dự báo hoặc hiệu quả điều trị. Không dùng nỗi sợ về nhãn Hung để bán SIM, dịch vụ hóa giải hoặc gói cao hơn.

Luồng khiếu nại phải cho phép phân loại lỗi dữ liệu, lỗi tính toán, nội dung không phù hợp, quyền riêng tư và vấn đề thanh toán. Việc sửa một báo cáo phải liên kết với phiên bản bị ảnh hưởng; phát hiện lỗi phương pháp có thể yêu cầu rà các báo cáo khác cùng release.


# 21. Academy, chuyên gia và cấp phép quốc tế

Chương trình HNH giữ định hướng chín buổi, mỗi buổi 120 phút. Các buổi đi từ dữ liệu và giới hạn; số–tên; Bát Cực và Mã đuôi 80; lịch và chu kỳ; ma trận và mô thức; đồng nhịp sống; đối thoại và ranh giới; thiết kế hành động; đến thực hành ca và kiểm tra chất lượng. Học phí hoặc ngày khai giảng cũ là dữ liệu lịch sử, không tự xuất hiện như khóa đang tuyển sinh.

Người thực hành cần chứng minh biết tính, biết nguồn, biết nói phần chưa rõ và biết chuyển biểu tượng thành câu hỏi. Chứng nhận nội bộ ghi rõ phạm vi, thời hạn, tiêu chuẩn gia hạn và cơ chế khiếu nại. Không cấp chứng nhận như giấy phép chữa bệnh hoặc bằng cấp chuyên môn ngoài thẩm quyền.

Bốn mô hình đối tác gồm giới thiệu khách hàng, chuyên gia được cấp phạm vi, cấp phép tổ chức và lãnh thổ/nhượng quyền. Mỗi mô hình cần quy định quyền thương hiệu, quyền sửa nội dung, hỗ trợ, phí, audit, dữ liệu, điều kiện chấm dứt và chất lượng. Không dùng một bản hợp đồng cho mọi quốc gia mà không rà soát luật áp dụng.

Mỗi lãnh thổ có bộ ngôn ngữ, biên tập viên bản địa, pháp nhân hoặc đơn vị thanh toán, bản đồ dòng dữ liệu, cơ chế chuyển vùng và danh sách phương pháp được phép. Các bộ VN, EU/EEA, US, AU và SG trước đây được giữ. CA và UK có checklist bổ sung chờ nghiên cứu pháp lý cụ thể. Không tuyên bố đã đủ điều kiện mở bán ở những nơi này.

Tài khoản đối tác không thấy toàn bộ dữ liệu toàn cầu. Khi giấy phép bị thu hồi, ngừng quyền thương hiệu và quản trị theo hợp đồng; người dùng vẫn cần đường thực hiện quyền dữ liệu. Quyền sở hữu phương pháp, phần mềm, nội dung đào tạo và dữ liệu cá nhân không được gộp làm một.

Quy trình chuyển giao gồm kiểm năng lực đối tác, huấn luyện, thực hành có giám sát, kiểm tra chất lượng nội dung bản địa, pilot giới hạn, rà soát rồi mới mở rộng. Mỗi địa phương cần người có trách nhiệm thực tế; việc có AI đa ngôn ngữ không thay thế người biên tập và chuyên gia pháp lý bản địa.


# 22. Nâng cấp hiện trạng: P0 và đồng bộ không mất dữ liệu

Các vấn đề P0 được ghi nhận ở baseline trước vẫn phải đối chiếu với source và runtime hiện hành: điểm hardcode; timeline tạo bằng Math.sin; quyền dựa vào ID do client gửi; session chưa an toàn; coverage lấy mẫu số từ các lớp client đưa lên. Demo mới không tự sửa những đường production ấy.

Bước đầu là khóa các đường dữ liệu chưa an toàn, vô hiệu session cũ theo kế hoạch, giữ bằng chứng riêng tư và chốt source, artifact, runtime. Không tạo yêu cầu đọc hồ sơ người thật để chứng minh lỗi. Một endpoint health trả 200 chỉ thể hiện liveness, không phải kiểm thử phân quyền end-to-end.

Output legacy được gắn experimental_legacy. Không chuyển lời luận AI cũ thành self_report vì nó nằm trong hồ sơ một người. Hồ sơ chưa xác nhận chủ sở hữu phải cách ly; tên và ngày sinh không đủ để phục hồi quyền. Migration có đối soát và chạy thử; backup restore áp lại các chỉ thị xóa để dữ liệu đã xóa không quay lại.

V3 bổ sung dưới docs/upgrades/2026-10-29-v3/. Nhánh review sạch, remote đúng và manifest khớp là điều kiện nhập. Công cụ từ chối ghi đè nội dung khác, đường dẫn vượt thư mục, symlink và worktree có thay đổi chưa xử lý. Nó không tự chạy SQL hoặc script deploy. Rollback chỉ về bản an toàn; nếu chưa có, duy trì chế độ giới thiệu hoặc bảo trì.

Receipt phát hành cần commit SHA, artifact digest, CI run, deployment ID, schema version, method configuration, tests, người duyệt, thời điểm và rollback target. Không dùng việc trang web trông giống một nhánh mã để khẳng định nhánh đó là bản đang chạy.

Các tệp cũ được giữ để truy vết, nhưng không được đưa nhầm vào bundle website. Build production phải có allowlist tài nguyên công khai; loại tài liệu nội bộ, SQL, ZIP, demo, dữ liệu mẫu và receipt nhạy cảm. Đưa kế hoạch vào repository không đồng nghĩa xuất bản tất cả nội dung lên website.


# 23. Cổng phát hành, bằng chứng và 280 công việc

Backlog giữ 140 công việc V1 và 68 phần làm rõ V2, bổ sung 72 công việc V3, tổng 280 bản ghi. Đây là danh mục kiểm soát phạm vi, không phải 280 việc đã hoàn thành. Những phần đã có mã tham chiếu vẫn giữ trạng thái production chưa bắt đầu cho tới khi có tích hợp và receipt riêng.

Mười hai cổng gồm nguồn và phát hành; xác thực; phân quyền; pháp lý và mục đích; lưu giữ và xóa; phương pháp và nhận định; legacy và migration; báo cáo và AI; thương mại; độ tin cậy; rà soát bảo mật độc lập; vận hành. Không lấy trung bình để bù lỗi phân quyền bằng chất lượng giao diện. Người sửa không là người duy nhất xác nhận phần sửa đã an toàn.

Thứ tự triển khai theo bằng chứng: containment, governance, Trust Core, sản phẩm đầu tiên, paid private beta, mở rộng dữ liệu đời sống và hệ hợp nhất. Chín cấp không cần mở cùng lúc. Ước lượng cũ 4–6 tháng cho paid beta và 12–18+ tháng cho tầm nhìn rộng chỉ có ý nghĩa với nguồn lực tương ứng; V3 không đổi nó thành cam kết giao hàng.

Kiểm thử gồm unit, property, hợp đồng API, quyền âm tính, migration, báo cáo, khả năng truy cập, staging E2E, khôi phục và review. Tính đúng Mã đuôi 80 với 10.000 đầu vào không chứng minh 10.000 cuộc đời. Đếm đúng 17 vị trí Psychomatrix không xác nhận các nhãn truyền thống về trí nhớ hoặc sức khỏe.

Mỗi yêu cầu nối tới tài liệu, công việc, code/config, kiểm thử và bằng chứng. VERIFY_PACKAGE.py kiểm hash và cấu trúc tệp trong gói; không thay đánh giá bảo mật production. Cổng chỉ đạt khi receipt được tạo trong đúng môi trường, ghi rõ SHA, artifact digest, thời điểm và người chịu trách nhiệm.

Khi một cổng chưa đạt, báo cáo nêu thiếu bằng chứng nào và ai xử lý. Không đổi nhãn thành “đạt một phần” rồi cộng vào tỷ lệ sẵn sàng chung. Có thể mở một phạm vi nhỏ khi tất cả cổng áp dụng cho phạm vi ấy đạt; không mở một mô-đun nhạy cảm chỉ vì mô-đun tính số đã chạy đúng.


# 24. Quyết định phê duyệt và lệnh giao đội triển khai

Q1–Q30 được giữ nguyên trong kho baseline và được đưa vào ledger hợp nhất. Q31–Q45 chốt phần bổ sung: bảo toàn tệp; 23 chỉ số; Bát Cực strict và diagnostic; không tạo điểm định mệnh; bảng 80; Psychomatrix 17; 18 lĩnh vực; mốc chu kỳ độc lập; nhiều workspace; 28 sản phẩm; sách không bịa sự kiện; Academy; quốc tế; mức tự chủ AI; nhập additive.

Founder duyệt triết lý và phạm vi. Người rà soát phương pháp duyệt nguồn, quy tắc và ví dụ. Tech Lead duyệt hợp đồng kỹ thuật. Security và QA kiểm tra đường dữ liệu. Pháp lý rà soát phạm vi lãnh thổ. Một phê duyệt nội dung không thay thế quyền triển khai.

Lệnh giao đội: đọc START_HERE và REQUIREMENTS_TRACE; kiểm tra PRESERVATION_MANIFEST; chạy demo bằng dữ liệu giả; đối chiếu remote baseline với receipt triển khai mới nhất; tạo nhánh review đúng repository; nhập theo cách chỉ bổ sung; đối soát hash; nhận công việc theo phụ thuộc. Không sửa dữ liệu thật, merge hoặc deploy khi chưa có release packet được duyệt.

Bộ V3 là kế hoạch hợp nhất, hợp đồng dữ liệu và mã tham chiếu mở rộng. Giá trị của nó là kết nối tri thức với dữ liệu, quyền lựa chọn và hành động có thể xem lại, không phải tuyên bố đã biết toàn bộ bí mật của mọi người. Những phần chưa triển khai vẫn được ghi đúng trạng thái để đội phát triển biết công việc còn lại.


# Nguồn và phạm vi tiếp cận

### [R01] Life Code: nội dung website công khai

PUBLIC_PAGE_RETRIEVED. Đối chiếu định vị, 12 lớp, 9 cấp; không xác minh deployed SHA.

https://lifecode.iai.one/

### [R02] GitHub: danh sách nhánh

CONNECTOR_READ. main và audit giữ SHA; nhánh rescue cùng SHA audit.

https://api.github.com/repos/tranhatam-collab/Life-Code-OS/branches?per_page=100

### [R03] GitHub: kế hoạch audit 11/10/2026

CONNECTOR_READ. Kế hoạch có đề xuất, chưa phải release approval.

https://github.com/tranhatam-collab/Life-Code-OS/blob/336ef35a8386a744c6de18a7f7c6e268e89e6dac/docs/audit/LIFE_CODE_OS_COMPREHENSIVE_UPGRADE_PLAN_2026-10-11.md

### [R04] Kim Tâm Cát: Bát Cực Linh Số

PRACTITIONER_SOURCE. Bảng cặp và quy ước; các tuyên bố số phận không được coi là bằng chứng thực nghiệm.

https://kimtamcat.com.vn/bat-cuc-linh-so-la-gi-va-cach-ung-dung-cai-van/

### [R05] 八星數字能量在人生各方面的應用

PRACTITIONER_SOURCE. Đối chiếu thuật ngữ và chuỗi; không gộp ngầm trường phái.

https://20401319.org/number02/

### [R06] World Numerology: Life Path

PRACTITIONER_SOURCE. Phân biệt cộng trực tiếp và rút gọn từng thành phần; lưu phương pháp.

https://www.worldnumerology.com/numerology-life-path/

### [R07] World Numerology: chữ Y

PRACTITIONER_SOURCE. Y phụ thuộc quy ước/phát âm; không áp máy móc một quy tắc cho mọi tên Việt.

https://www.worldnumerology.com/numerology-articles/numerology-Y-vowel-consonant.html

### [R08] World Numerology: Maturity

PRACTITIONER_SOURCE. Cộng Life Path và Expression theo quy tắc được chọn.

https://www.worldnumerology.com/numerology-articles/numerology-maturity-number.html

### [R09] World Numerology: Rational Thought

PRACTITIONER_SOURCE. Tên riêng cần được xác nhận, không tự dùng token đầu của tên Việt.

https://www.worldnumerology.com/numerology-articles/rational-thought-number.html

### [R10] World Numerology: Subconscious Self

PRACTITIONER_SOURCE. Đếm nhóm số có mặt trong tên; Hidden Passion có thể đồng hạng.

https://www.worldnumerology.com/numerology-articles/numerology-subconscious-self.html

### [R11] World Numerology: Balance

PRACTITIONER_SOURCE. Quy đổi chữ đầu tên; không phải đo cân bằng tâm lý.

https://www.worldnumerology.com/numerology-balance-number/

### [R12] World Numerology: Pinnacles

PRACTITIONER_SOURCE. Bốn công thức, ranh giới tuổi cần khóa cách tính inclusive/exclusive.

https://www.worldnumerology.com/numerology-pinnacles/

### [R13] World Numerology: Challenges

PRACTITIONER_SOURCE. Bốn hiệu tuyệt đối; mốc thời gian phải có chính sách riêng.

https://www.worldnumerology.com/numerology-challenges/

### [R14] World Numerology: Period Cycles

PRACTITIONER_SOURCE. Chu kỳ không đồng nhất với Pinnacles; không tự giữ bảng tuổi cũ nếu thiếu nguồn.

https://www.worldnumerology.com/numerology-period-cycles/

### [R15] Yandex Books: Цифровой психоанализ для начинающих

SEARCH_EXCERPT_ONLY_FULL_TEXT_NOT_ACCESSED. Nhận diện công thức bốn số phụ; quyền và toàn văn còn phải đối chiếu.

https://books.yandex.ru/books/WHuirlQq/read-online

### [R16] Unicode Normalization

PRIMARY_STANDARD. NFC không đồng nghĩa xóa dấu hoặc phiên âm.

https://www.unicode.org/reports/tr15/

### [R17] IANA Time Zone Database

PRIMARY_DOCUMENTATION. Lưu phiên bản tzdb và độ chính xác thời điểm sinh.

https://www.iana.org/time-zones

### [R18] Cloudflare Queues: delivery guarantees

PRIMARY_DOCUMENTATION. At-least-once; tác vụ phải chống tác dụng phụ trùng.

https://developers.cloudflare.com/queues/reference/delivery-guarantees/

### [R19] PostgreSQL Row Security Policies

PRIMARY_DOCUMENTATION. Runtime role không được tự bỏ qua RLS.

https://www.postgresql.org/docs/current/ddl-rowsecurity.html

### [R20] W3C WCAG 2.2

PRIMARY_STANDARD. Mục tiêu AA; kiểm thử demo không tự là chứng nhận toàn hệ.

https://www.w3.org/TR/WCAG22/

### [R21] Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15

OFFICIAL_METADATA_VERIFIED. Hiệu lực 01/01/2026; cần pháp lý rà phạm vi áp dụng thực tế.

https://chinhphu.vn/?classid=1&docid=214590&orggroupid=1&pageid=27160

### [R22] Luật Trí tuệ nhân tạo 134/2025/QH15

OFFICIAL_METADATA_VERIFIED. Hiệu lực 01/03/2026; phân loại theo chức năng, không theo nhãn giáo dục.

https://chinhphu.vn/?classid=1&docid=216334&orggroupid=1&pageid=27160

### [R23] Luật Thương mại điện tử 122/2025/QH15

OFFICIAL_METADATA_VERIFIED. Hiệu lực 01/07/2026; chưa có legal opinion cho launch.

https://chinhphu.vn/?classid=1&docid=216503&pageid=27160&typegroupid=3

### [R24] OWASP API1:2023 BOLA

PRIMARY_SECURITY_GUIDANCE. Mọi ID đối tượng cần kiểm tra quyền ở phía server.

https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/

### [R25] WIPO Copyright

PRIMARY_RIGHTS_GUIDANCE. Tách ý tưởng/phương pháp khỏi biểu đạt, bản dịch và phần mềm có quyền.

https://www.wipo.int/en/web/copyright

### [R26] World Numerology: tự tính biểu đồ

PRACTITIONER_SOURCE. Các công thức tham khảo; không sao chép luận giải thương mại.

https://www.worldnumerology.com/do-your-own-reading/

### [R27] GitHub: kiến trúc chín cấp v1

CONNECTOR_READ. Giữ tên/ID; thay cơ chế mở khóa theo dữ liệu và quyền, không chỉ coverage.

https://github.com/tranhatam-collab/Life-Code-OS/blob/99b402764437f81859fa0cd3a3af860125f7bd52/docs/LEVELS_ARCHITECTURE_V1.md

### [R28] Bảng Mã đuôi 80 do Founder cung cấp

USER_SUPPLIED. Lưu bảng 80 riêng; chưa xác minh một bảng gốc lịch sử duy nhất.

user-supplied:conversation:tail80

### [R29] Bộ V1 đính kèm 11/10/2026

BYTES_PRESERVED. 149 tệp, hash ở PRESERVATION_MANIFEST.

attachment:Life_Code_OS_Complete_Upgrade_Package_2026-10-11.zip

### [R30] Bộ V2 đính kèm 20/10/2026

BYTES_PRESERVED. 307 mục tệp của ZIP được giữ nguyên; các receipt cũ giữ ngày cũ.

attachment:Life_Code_OS_V2_Complete_Upgrade_2026-10-20.zip

