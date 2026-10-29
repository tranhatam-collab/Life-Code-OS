# Thiết kế giao diện, ngôn ngữ Việt và khả năng tiếp cận

Mã tài liệu: **D19** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Design + Frontend + Editorial. Nguồn đối chiếu: S17, S15. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Nguyên tắc trải nghiệm
Bình tĩnh, ấm, rõ ràng; tránh thị giác định mệnh hoặc gây khẩn cấp. Không phân hạng người dùng bằng màu đỏ/xanh. Dữ kiện, tự khai, biểu tượng và kế hoạch có nhãn chữ; màu chỉ hỗ trợ. Typographic scale và khoảng trắng đủ cho tiếng Việt; không viết hoa toàn bộ đoạn dài.
## 2. Design tokens đề xuất
Light theme nền ngà nhạt, ink xanh đen, accent xanh trầm, màu vàng chỉ dùng nhấn nhá. Bộ tokens JSON xuất kèm có spacing 4/8/12/16/24/32, radius và typography. Không nhúng/chia sẻ file font trong gói. Hệ dùng system sans đã hỗ trợ tiếng Việt; khi triển khai web font phải kiểm tra license và subset dấu đầy đủ.
Breakpoints và component đáp ứng theo nội dung. Mobile có một CTA chính, thanh hành động không che bàn phím/nội dung. Thông báo quota không dùng modal lặp. Form có label thực, mô tả và thông báo lỗi được liên kết bằng aria-describedby. Không dùng placeholder thay label.
## 3. WCAG target
WCAG 2.2 AA là mục tiêu nghiệm thu, không tuyên bố đã đạt chỉ bằng chạy axe. Kiểm tra keyboard, focus visible và không bị overlay che; reflow ở 320 CSS px; zoom; contrast tối thiểu theo loại chữ; target size, error suggestion, accessible authentication và hỗ trợ reduced motion. Screen reader đọc bảng và tabs đúng thứ tự.
## 4. Content states
Dữ liệu thiếu: “Chưa có giờ sinh. Những phương pháp cần giờ chưa được chạy.” Chưa rõ quy tắc: “Bảng hiện tại chưa xử lý cặp chứa 5.” Không đủ quyền: thông điệp không lộ chủ thể. Quá hạn mức: nêu limit và lựa chọn tiếp tục xem dữ liệu miễn phí. Quá trình review: nêu vì sao cần kiểm tra và thời gian mục tiêu, không hứa có chuyên gia đang đọc khi chưa phân công.
## 5. Localization
Ngôn ngữ hiển thị bằng tên đầy đủ; cờ chỉ hỗ trợ nơi thích hợp, không dùng cờ như ngôn ngữ vì một ngôn ngữ có nhiều quốc gia. VI trước, EN sau; NL/FR/ZH/JA/KO/TH/HI/AR là country pack chờ duyệt. Date input có ISO storage, locale display; không hiểu 02/11 theo thói quen trình duyệt. RTL thử riêng, tên riêng không tự phiên âm thành dữ liệu chuẩn.
## 6. Nghiệm thu
30 người dùng không phải ngưỡng khoa học; pilot số lượng cụ thể do đội nghiên cứu chọn. Đánh giá thực hành: người mới tìm được cách tính, biết phần chưa biết, sửa hồ sơ và thu hồi chia sẻ mà không cần admin. Chụp baseline visual cho các trạng thái thật, không chỉ màn hình đẹp có dữ liệu giả.

## Bổ sung thực thi 2026-10-20
Target kiểm thử, reflow, orientation, focus, status, authentication, drag alternative và PWA lifecycle được neo vào WCAG 2.2/WAI/manifest/service-worker sources tại `04_PWA_RESPONSIVE_EXECUTION_PLAN_2026-10-20.md`. `DESIGN_TOKENS.json` bổ sung test viewports và interaction/focus/PWA contract, đều `NOT_CHECKED` cho tới khi có receipt.
