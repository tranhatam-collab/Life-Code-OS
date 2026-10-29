# P0 — Dữ liệu legacy và đánh giá sự cố
**Trạng thái: chưa truy cập cơ sở dữ liệu hoặc log người dùng thật.**

Lỗi mã không tự chứng minh đã xảy ra rò rỉ. Cần người được ủy quyền xem logs, phạm vi route, thời gian, số bản ghi ảnh hưởng và tính toàn vẹn. Lưu câu hỏi chưa trả lời, không ghi “không có sự cố” chỉ vì chưa thấy bằng chứng.

## Ba nhóm dữ liệu
1. Dữ liệu gốc có nguồn và quyền xác định: xem xét migration có đối soát.
2. Dữ liệu chưa rõ quyền/chủ thể: cách ly; không gắn lại bằng tên hoặc ngày sinh khớp.
3. Score/timeline/biography do engine hoặc AI tạo chưa có căn cứ: experimental_legacy; không dùng làm self_report hoặc training truth.

## Chủ thể và thu hồi
Session được cấp qua luồng legacy yếu không đủ chứng minh quyền sở hữu. Quy trình khôi phục cần review riêng. Các file đã tải khỏi hệ thống không thể bị thu hồi vật lý; có thể đánh dấu bản cũ không còn hiệu lực và giải thích việc hiệu chỉnh.

## Lưu giữ và thông báo
Privacy/Legal xác định nghĩa vụ, thời hạn và ngoại lệ đúng tình huống/quốc gia. Bằng chứng được tối thiểu hóa, mã hóa, có quyền và thời hạn. Không phát cảnh báo vi phạm công khai trước khi người phụ trách rà soát, cũng không dùng phê duyệt truyền thông để trì hoãn nghĩa vụ bắt buộc.

## Thông tin phải bàn giao
Chủ trì sự cố, nguồn phát hiện, mốc thời gian, trạng thái xác minh, ảnh hưởng có thể có, biện pháp chặn, điều cần làm rõ, quyết định thông báo và kế hoạch không tái diễn.


## Bổ sung ngày 20 tháng 10 năm 2026

Thêm reconciliation bucket cho source không đủ quyền và account/subject ambiguous. Mỗi row rejected có reason và owner xử lý trong kho riêng tư; raw legacy output không chuyển thành observed fact.
