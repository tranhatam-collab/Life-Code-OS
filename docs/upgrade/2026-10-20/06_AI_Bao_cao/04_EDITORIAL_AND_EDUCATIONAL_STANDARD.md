# Chuẩn tiếng Việt, cấu trúc bài đọc và chất lượng học liệu

Mã tài liệu: **D24** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Editorial Authority + Method Council. Nguồn đối chiếu: S15, S38, S39. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Viết cho người thực sự sử dụng
Mỗi phần phải trả lời: kết quả nào đã có, nó được tạo ra thế nào, người đọc nên hiểu phạm vi ra sao và việc gì có thể làm tiếp. Không mở đầu mọi đoạn bằng cùng một mệnh đề; không gọi một chủ đề trừu tượng là “đọc tận tâm can”. Những câu đẹp nhưng không có tác dụng phải được rút gọn.
Từ “năng lượng” cần xác định là trải nghiệm người dùng, biểu tượng hay đại lượng vật lý. “Tu tập” là thực hành tự quan sát có quyền lựa chọn, không phải điều kiện được đối xử tốt. “Sứ mệnh” là hướng giá trị người dùng chọn và thử, không phải món nợ của linh hồn. Không gán nghĩa một họ tên chỉ bằng từ đồng âm.
## 2. Glossary và dịch thuật
Tiếng Việt là bản biên tập chính; giữ dấu, chuẩn NFC, thống nhất Huyền Nhân Học, Mã đuôi 80, Đồng nhịp sống. Thuật ngữ kỹ thuật Anh được giữ trong schema nhưng giải thích bằng tiếng Việt. Bản dịch dùng termbase, translator và reviewer độc lập cho các đoạn có tác động lớn. Dịch ngược là một kỹ thuật kiểm tra nội dung, không chứng minh validity tâm lý của thang hỏi.
Ngôn ngữ nguồn và ngôn ngữ giao diện là hai registry khác. Có đọc một tài liệu Trung văn không đồng nghĩa sản phẩm tiếng Trung đã đủ legal/culture gate. RTL, dấu tên, lịch, số thập phân, ngày tháng và đồng tiền đều cần locale tests.
## 3. Bốn loại đoạn văn
Đoạn dữ kiện nêu nguồn. Đoạn biểu tượng ghi quy ước. Đoạn tự thuật gắn lời người dùng. Đoạn hành động nói rõ điều kiện và lựa chọn. Không dùng một disclaimer cuối sách để hợp thức hóa hàng chục trang khẳng định tuyệt đối bên trong.
Ví dụ sửa: “Thiếu số 4 nên sức khỏe yếu” thành “Trong biểu đồ này không xuất hiện chữ số 4; phương pháp không cho phép kết luận sức khỏe.” “Cặp đôi khắc số” thành “Hai bảng quy ước tạo chủ đề khác nhau; cách hai người giao tiếp cần dựa trên dữ liệu hai bên đồng ý chia sẻ.”
## 4. Học liệu và bài đánh giá
Câu hỏi tự quan sát do HNH viết không tự được gọi là trắc nghiệm chuẩn hóa. Muốn dùng IPIP/O*NET hoặc công cụ khác phải xác định phiên bản, quyền, ngôn ngữ, cách chấm và đối tượng; không chỉnh wording một thang rồi giữ claim độ tin cậy cũ. Các worksheet của HNH có thể hữu ích mà không cần giả nhận là đo được tính cách bẩm sinh.
## 5. Nghiệm thu
Không lỗi chủ thể/ngày sinh, không lỗi phép tính, không chữ mất dấu do encoding, không nhầm CCDD/CCCD, không bảng 80/81 tráo nhau, không câu khẳng định y khoa. Đánh giá gồm checklist máy và đọc trực quan tài liệu đã render. Mẫu đạt mới được đưa vào report factory.

## Bổ sung thực thi 2026-10-20
Mỗi Level 1–9 có golden/null/conflict/unauthorized/injection/correction fixture và reviewer khác biệt trong `NINE_LEVEL_REPORT_CONTRACTS.*`. Hard-stop case không được che bởi điểm trung bình; mức/ngưỡng mềm phải được quyết trước khi xem kết quả.
