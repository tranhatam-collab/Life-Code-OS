# Chín báo cáo: cấu trúc nội dung để người dùng hiểu và hành động

**Life Code OS · Bản nâng cấp bảo toàn V2 · 20/10/2026**  
**Trạng thái:** Đặc tả để triển khai và rà soát; không phải chứng nhận production.

## 1. Chuẩn chung
Mỗi report có bìa, phạm vi, dữ liệu gốc, điều chưa biết, mục lục, bốn lớp nội dung và phụ lục phép tính/nguồn. Một đoạn luận phải nói nó dựa vào dữ liệu gì. Không thay việc thuyết minh bằng các nhãn “engine”, “confidence” mà người dùng không hiểu. Chữ confidence chưa đủ định nghĩa được bỏ khỏi giao diện thay vì gán 0,8.

## 2. Level 1 — Self Signal
Phần Identity trình bày tên/ngày/giờ và độ chắc dữ liệu. Analysis giải thích từng phép tính, không gán nhân cách từ căn số. Timeline nêu tuổi/chủ đề biểu tượng và phần lịch không có dữ kiện. Action chốt một mục tiêu 30 ngày, ví dụ cụ thể và biểu mẫu theo dõi. Nên có trang “Tôi đồng ý/không đồng ý với điều gì?” để người dùng phản hồi tự do.

## 3. Level 2 — Inner Architecture
Trình bày vai trò, nhu cầu và giá trị do người dùng tự khai; mỗi xung đột cần ít nhất một ví dụ đời thật. So sánh điều muốn, điều đang làm và ràng buộc. Bản đồ không đóng nhãn “bản chất bên trong”; nó là cách hiểu có thể cập nhật. Kế hoạch 90 ngày gồm thử nghiệm, dấu hiệu xem lại và người hỗ trợ.

## 4. Level 3 — Behavior Code
Phân tách mô thức trong ngày thường và lúc áp lực. Ghi cửa sổ quan sát, số lần, dữ liệu thiếu và ngoại lệ. Biểu đồ không tự làm bằng chứng nhân quả. Mỗi mô thức có một hành động nhỏ và cách đo trước/sau phù hợp. Không dùng thiếu chữ số làm chỉ số lười, thiếu trí nhớ hoặc thiếu trách nhiệm.

## 5. Level 4 — Work & Wealth
Dùng bảng kỹ năng có minh chứng, sở thích, điều kiện thị trường do người dùng xác nhận và nguồn lực. Kịch bản tiền bạc phải ghi giả định/currency/date. Hướng nghề là phương án để thử, không phán nghề bắt buộc. Có phần “điều chưa nên quyết chỉ từ báo cáo này”.

## 6. Level 5 — Relationship Field
Nêu rõ đang dùng dữ liệu một người hay nhiều bên. Nếu chỉ một người kể, không kết luận nội tâm người còn lại. Cấu trúc gồm nhu cầu, cách giao tiếp, ranh giới, trách nhiệm và cuộc đối thoại được chuẩn bị. Không đưa kết luận phản bội hoặc tỷ lệ ly hôn từ ngày sinh.

## 7. Level 6 — Life Timeline
Các phần: nguồn sự kiện quá khứ; danh sách khoảng tuổi; cycle track; plan track; scenario track. Mỗi mốc phải có loại dữ liệu và ngày xác nhận. Bản đồ 10 năm là hướng và điểm review; không nhồi 100 năm lời tiên đoán. Các phương án ngày sinh có view riêng.

## 8. Level 7 — Body Intelligence
Nêu điều kiện ảnh/thiết bị, chất lượng và sai số. Mô tả quan sát không suy đạo đức hoặc sức khỏe. Phần đồng nhịp giúp ghi sinh hoạt/môi trường và câu hỏi cần hỏi chuyên gia khi cần. Không coi việc chụp thêm ảnh làm tăng độ đúng của mọi lớp khác.

## 9. Level 8 — Mission Path
Các phần: điều người dùng trân trọng; năng lực có minh chứng; nhóm muốn phục vụ; giới hạn; thử nghiệm phụng sự; kế hoạch 90 ngày; hướng di sản. Tu tập gồm tự quan sát, lòng biết ơn và trách nhiệm; không yêu cầu hy sinh vô hạn hay trung thành với một người hướng dẫn.

## 10. Level 9 — Full Life Code
Biên tập lại theo câu chuyện dữ liệu, không nối nguyên văn tám tập. Có bảng thay đổi, điểm còn khác nhau, các quyết định hiện tại và hệ hành động. Các đoạn hướng dẫn chung tách khỏi kết quả cá nhân. Số trang 150–600 chỉ dùng khi dữ liệu tương xứng; thiếu dữ liệu không được thay bằng nhiều lời đẹp.

## 11. Tệp nguồn và renderer
Content model có block paragraph/table/chart/quote/question/action/citation, ngôn ngữ và supporting_claim_ids. Các bản Web/PDF/Word dùng cùng nội dung đã duyệt. Một sửa lỗi phải phát hành version mới, ghi release note và cho người dùng biết, không âm thầm thay tệp tải về bằng cùng tên mà không history.
