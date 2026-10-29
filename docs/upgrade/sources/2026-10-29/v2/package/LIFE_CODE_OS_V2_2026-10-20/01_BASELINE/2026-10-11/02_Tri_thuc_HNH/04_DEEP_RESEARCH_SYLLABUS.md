# Chương trình nghiên cứu chuyên sâu K01–K20 và cách tạo Code HNH

Mã: **D37** | Phiên bản: **2026-10-11.r1** | **ĐỀ XUẤT / CHỜ PHÊ DUYỆT**

Chủ trì: Method Council + Ngôn ngữ + Data Science. Nguồn đã tiếp cận: G02, S15, S16, S38, S39. Các nhóm văn bản khác bên dưới là danh mục cần nghiên cứu, không được hiểu là đã đọc toàn văn.


## Mục tiêu và trạng thái
Đây là bản thiết kế nghiên cứu theo từng họ, không tuyên bố đã sở hữu tri thức tất cả các nền văn minh. Mỗi nhóm có hai đường: tái lập phương pháp đúng nguồn và tìm giá trị ứng dụng phù hợp. Không suy rằng tái lập đúng phép tính đồng nghĩa giải mã chính xác kiếp người. Học thuyết HNH có thể giữ ngôn ngữ triết lý, nhưng engine phải phân biệt biểu tượng với dữ kiện.
## K01. Thời gian và lịch
Khóa loại lịch gốc, vùng địa lý, timezone lịch sử, độ chính xác giờ và quy tắc quy đổi. Thiếu địa điểm không tự dùng timezone Việt Nam cho mọi hồ sơ. Tách ngày dân dụng, ngày theo phương pháp và giờ Mặt Trời khi trường phái yêu cầu. Mỗi lần quy đổi lưu tzdb/library version và các giả định. Golden corpus phải có ngày nhuận, ranh giới nửa đêm, giờ trùng/không tồn tại khi chuyển giờ mùa hè và dữ liệu chỉ có năm. Đây là phần nền có thể tính chính xác hơn qua đặc tả, không tạo ra prediction về con người.
## K02. Bát tự/Tứ trụ
Nghiên cứu nguồn và chú giải trước khi khóa cách an bốn trụ, ranh giới năm/tháng/ngày, giờ sinh và khởi vận. Các cách dùng nguyệt lệnh, tàng can, vượng–suy, dụng thần, hợp–xung–hình–hại phải có adapter riêng. Một cấu hình không được dùng ưu điểm của trường phái A rồi lặng lẽ đổi sang B khi lời luận không khớp. Corpus gồm cùng dữ liệu nhưng khác cấu hình để người dùng thấy khác biệt. Không chuyển “Mộc vượng” thành hormone, bệnh hoặc năng lực lãnh đạo.
## K03. Tử vi và mệnh bàn
Đặc tả thứ tự an cung/sao, các quy tắc tháng nhuận, cách tính tuổi và hệ hạn theo edition. Giữ tên thuật ngữ nguồn, chữ gốc và bản dịch. Dùng bản đồ lĩnh vực như chất liệu tự soi chiếu, không tự đếm anh chị em, con cái hoặc viết quá khứ. Những nhánh Hà Lạc/Thiết Bản, nếu tiếp nhận, có method ID và input riêng. Nhiệm vụ nghiên cứu là làm rõ khác biệt của sơ đồ, không ép mọi mệnh bàn thành cùng một Life Code Index.
## K04. Kinh Dịch và các cách lấy quẻ
Tách nghiên cứu văn bản với gieo quẻ. Lưu câu hỏi, thời điểm, cách tạo quẻ, hào động và quy tắc quẻ biến. Randomness nếu dùng để tạo quẻ phải công khai và không mô tả là dữ liệu vận mệnh. Mai Hoa, Lục Hào và chú giải Chu Dịch là các phương pháp liên quan nhưng không dùng chung rules mặc định. HNH có thể tạo sáu câu hỏi tình huống: đang hình thành gì, đang vướng gì, hỗ trợ nào có thật, lựa chọn nào có thể thử, giới hạn nào cần giữ và khi nào xem lại.
## K05. Tam thức và trạch nhật
Kỳ Môn, Lục Nhâm, Thái Ất cùng hệ chọn thời điểm cần schema khác nhau. Khóa điều kiện lịch, phương pháp lập cục và bảng nguồn; thử các thời điểm biên và sai số đầu vào. Luận thời điểm nằm trong symbolic track, bên cạnh lịch thực, nguồn lực, thời hạn và an toàn. Không khuyên trì hoãn khám bệnh, bỏ nghĩa vụ pháp lý hoặc giao dịch quan trọng chỉ vì thời điểm biểu tượng. Sản phẩm phát hành sau nguồn đầy đủ và nội dung phù hợp.
## K06. Phong thủy/Vastu và nơi sống
Tách hình thế, hướng đo, bảng phương vị, thời điểm xây/sửa theo từng trường phái. Ghi phương pháp đo hướng, thiết bị, sai số và phiên bản mặt bằng. Song song là quan sát thực: ánh sáng, tiếng ồn, thông khí, an toàn, riêng tư, access và đi lại. Bản HNH có thể giúp người dùng lựa chọn cách bố trí trong ngân sách, nhưng không gọi căn nhà là nguyên nhân chắc chắn của bệnh/tai nạn hoặc buộc mua vật phẩm.
## K07. Jyotish và Nadi
Tạo adapters cho hệ hoàng đạo, ayanāṃśa, nhà, phân đồ và chu kỳ được nguồn quy định. Bảng thuật ngữ giữ Sanskrit và bản dịch, có review ngôn ngữ. Phương pháp tính gọi là Nadi khác việc xác thực một bản thảo lá cọ dành cho người cụ thể. Không dựng văn bản lá Nadi từ tên/ngày sinh rồi trình bày như cổ bản tìm được. Quyền số hóa/dịch bản thảo và nguồn lưu trữ cần xác nhận.
## K08. Chiêm tinh phương Tây
Tính vị trí thiên thể là một loại tính toán; suy luận tâm lý từ vị trí là loại nhận định khác. Khóa hệ nhà, hệ hoàng đạo, orb, vị trí địa lý và time standard trong release. Golden fixtures cần có đối chiếu với nguồn ephemeris được cấp phép và các trường hợp vùng cực/giờ sinh thiếu. Trình diễn lá số không phải chứng nhận một người có tính cách cố định. Lời giải thích phải có mode biểu tượng được người dùng lựa chọn.
## K09. Lịch và truyền thống khu vực
Tây Tạng, Nhật, Hàn, Thái, Myanmar, Weton/Pawukon và lịch Maya cần researcher/người bản ngữ phù hợp. Không gộp các truyền thống vào một bảng “Đông–Tây chung”. Kiểm tra lịch dùng, bối cảnh văn hóa và cách cộng đồng mong muốn tri thức được sử dụng. Có lịch ngày không có nghĩa có quyền luận mọi người bằng nó. Product locale được duyệt độc lập với nguồn nghiên cứu locale.
## K10. Thần số và Psychomatrix
Bảng chữ–số, thứ tự cộng, giữ master numbers, cách tạo working numbers và cách lập chu kỳ phải được ghi đủ. Giữ cả số trung gian và căn rút gọn để so sánh. Hai phương pháp cùng trả3 không có nghĩa lời luận cùng được chứng minh. Không dùng thiếu3/4/9 để gán kém logic, sức khỏe yếu hoặc trí nhớ kém; không suy nghề/lãnh đạo/tình dục từ chart. Một Psychomatrix chưa khóa variant phải trả method_not_supported, không viết bảng theo trí nhớ.
## K11. Bộ số định danh
Mã đuôi80 có hàm dư rõ nhưng bảng nghĩa và quy tắc0 cần phiên bản. Bát Cực phân loại cặp chồng lấn, số0/5 và chuỗi, không thể thay bằng digital root. Phone số quốc tế/nội địa phải có normalization policy và giữ raw form; kết quả khác do ký hiệu không được gọi là “tần số vật lý”. Kiểm thử đồng hạng, cùng đuôi, duplicatepairs và chữ viết không rõ. Cấm thu mật khẩu/PIN/OTP; chỉ bốn số cuối khi method cần như vậy.
## K12. Tên và ngôn ngữ
Tên gốc, chữ gốc nếu có, cách phát âm, nguồn gia đình và ý nghĩa tự nhận là những trường riêng. Không tự biến họ Trần thành “bụi trần” hoặc tên Hà thành “sông” như định nghĩa chắc chắn. Name semantics phải cho nhiều khả năng và câu hỏi xác nhận. Transliteration phụ thuộc ngôn ngữ; không dùng bảng Latin làm phép phổ quát cho Trung/Nhật/Ả Rập. Kiểm thử ký tự ghép, dấu, thứ tự họ/tên và đổi tên có lịch sử.
## K13. Hình thái
Ảnh trước hết là dữ liệu cần consent và chất lượng. Lưu camera condition, bên trái/phải, xoay, che khuất, blur và phép đo. Các dấu hiệu như nếp gấp, hướng ngón hoặc cấu trúc hình học được mô tả; không gán tính cách, bệnh, đạo đức, tài lộc, giới hay phẩm chất. Thư viện tướng học truyền thống nếu dùng chỉ ở khu giáo dục có nhãn, không tạo lời phán riêng về người trong ảnh. Level 7 phải qua thẩm định riêng.
## K14. Chiêm nghiệm biểu tượng
Tarot, Rune, Ifá, giải mộng và các công cụ kể chuyện có phương pháp và bối cảnh văn hóa riêng. Lưu người tạo biểu tượng, phương pháp chọn, câu hỏi và cách người dùng diễn giải. Không kết luận người thứ ba đã ngoại tình, có ác ý hoặc sắp chết từ một lá bài. Người dùng được quyền nói biểu tượng không phù hợp. HNH dùng nó để mở câu hỏi, không bắt mọi trải nghiệm khớp lời luận.
## K15. Các hệ tổng hợp hiện đại
Human Design, Gene Keys và các hệ mới có tên thương hiệu, nội dung, bản quyền và thuật toán riêng. Nghiên cứu kiến trúc tích hợp, cách trải nghiệm và các tuyên bố tự công bố; không tái đặt tên thành HNH rồi coi nguồn bị xóa. Những thuật ngữ gene/energy/quantum nếu chỉ dùng biểu tượng phải giữ nhãn đó. Quyền sử dụng tài liệu và tạo sản phẩm thương mại cần rà soát.
## K16. Nội tâm và triết học
Kho thực hành cần phân biệt văn bản gốc, dịch, chú giải và trải nghiệm người dạy. Tập trung tự quan sát, trách nhiệm, không dính mắc, giới hạn và lòng trắc ẩn. Tu tập không yêu cầu người dùng chấp nhận một tín ngưỡng; không dùng khổ đau để đổ lỗi “thiếu phúc”. Bài tập ngắn có quyền dừng, không áp các thực hành cường độ cao cho mọi người. Tình trạng cần chuyên môn được chuyển hướng phù hợp.
## K17. Đo lường tâm lý
Chỉ dùng instrument có phiên bản, scoring, license, ngôn ngữ và đối tượng phù hợp. Kho IPIP công khai không biến mọi bản dịch hoặc bộ câu hỏi tự ghép thành validscale. Cần nghiên cứu reliability, cấu trúc, bias và sự phù hợp tại Việt Nam. Bản hỏi120 câu HNH có thể được gọi là tự quan sát, nhưng chưa mang nhãn chẩn đoán. Không dùng birthchart để thay response thật.
## K18. Hành vi, nghề và nguồn lực
Bắt đầu từ việc đã làm, kỹ năng có minh chứng, thời gian, chi phí, trách nhiệm và lựa chọn. Hướng nghiệp cần cả hứng thú lẫn môi trường, kỹ năng và điều kiện. Dữ liệu O*NET là nguồn tham khảo cấu trúc nghề, không bản đồ định mệnh. Finance scenarios dùng giả định rõ, số tiền có currency/as_of và mức thiếu dữ liệu. Lịch sử thành công/khó khăn do người dùng xác nhận, không được AI viết để khớp tuổi.
## K19. Môi trường và sinh hoạt
Ghi nhận thực phẩm, giờ ăn, nơi ở, di chuyển, âm thanh, nhịp làm và phản ứng chủ quan. Những phép đo thiết bị phải có đơn vị, thiết bị và độ tin cậy riêng. Thử nghiệm nhỏ, có quyền dừng, tránh can thiệp y khoa. “Phù hợp với tôi” không tự là tương quan nhân quả; nhiều thay đổi cùng lúc được ghi để tránh quy hết kết quả cho một việc. Không dùng số để chọn thuốc hoặc chế độ ăn điều trị.
## K20. Toán, dữ liệu và AI
Lập knowledge graph với source/edition/rule/claim/purpose; đơn vị lưu trữ là nhận định có loại, không phải những đoạn văn vô hạn. Tái lập method và đánh giá outcome là hai chương trình khác nhau. Corpus người nổi tiếng chỉ hợp nghiên cứu lịch sử có giới hạn và quyền; không dùng hindsight để tuyên bố tiên đoán. Mọi probability cần target/horizon/model/evaluation. Hệ không có mô hình phù hợp sẽ trả scenario, không tự tạo phần trăm.
## Đầu ra của một chu kỳ nghiên cứu
Bản corpus manifest; glossary; method passport; rule spec; input/output schema; golden fixtures; log tranh luận; hạn chế; biên tập VI; rights decision; release recommendation. Mỗi nguồn có trạng thái chưa tiếp cận/đã đọc một phần/đã đọc toàn văn/đã đối chiếu. Không đưa một phạm vi nghiên cứu dài thành quảng cáo “Life Code đã hiểu toàn bộ nhân loại”.
