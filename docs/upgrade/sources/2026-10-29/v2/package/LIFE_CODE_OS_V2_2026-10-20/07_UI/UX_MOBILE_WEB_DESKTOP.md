# Giao diện mobile, web và desktop: một dữ liệu, nhiều cách sử dụng

**Life Code OS · Bản nâng cấp bảo toàn V2 · 20/10/2026**  
**Trạng thái:** Đặc tả để triển khai và rà soát; không phải chứng nhận production.

## 1. Nguyên tắc trải nghiệm
Người dùng không cần hiểu thuật ngữ backend để hiểu kết quả. Màn hình đầu hỏi mục tiêu, sau đó chỉ yêu cầu dữ liệu cần thiết. Mỗi trường có lý do thu thập, bắt buộc/tùy chọn, ai có thể xem và cách sửa. Dữ liệu thiếu phải có đường đi tiếp phù hợp, không làm người dùng cảm thấy hồ sơ của họ kém giá trị.

Các câu nhãn nên dùng: “Chưa có giờ sinh”, “Có hai phương án ngày sinh”, “Phép tính đã hoàn tất”, “Phần này chỉ là biểu tượng”, “Cần thêm ví dụ thực tế”. Không dùng “Hồ sơ yếu”, “Vận xấu”, “Bạn chỉ đạt 38% con người” hoặc “mua thêm để tăng độ chính xác”.

## 2. Ba bề mặt
Mobile web: thao tác một tay, form một cột, thanh hành động rõ, bàn phím phù hợp, cho lưu nháp khi đã đăng nhập. Tablet: hai vùng khi đủ rộng, form không kéo dãn quá mức. Desktop: danh sách/chi tiết, so sánh hai kết quả, outline báo cáo và phím tắt có tài liệu. Native app về sau dùng chung API và content model; camera và offline là capability bổ sung, không một bộ engine mới.

## 3. Luồng đầu tiên
Chọn nhu cầu → giải thích phạm vi → nhập dữ liệu tối thiểu → xác nhận cách hiểu ngày/tên → xem phần tính được/chưa tính được → tạo bản đọc → chọn một hành động → lưu hoặc tải theo quyền. Không yêu cầu ảnh mặt, tay, chân ở Level 1. Hình thức tên/giờ/lịch phải được kiểm tra trước khi tính, không đợi cuối báo cáo mới nói kết quả có thể sai.

## 4. Dashboard thực dụng
Ưu tiên mục tiêu đang làm, ba hành động, thay đổi từ lần xem trước và dữ liệu cần bổ sung. Bảng chu kỳ biểu tượng có chú giải và có thể ẩn. Timeline có danh sách đọc được bằng screen reader; không chỉ một biểu đồ màu. Kết quả phép tính có chế độ “Giải thích từng bước” và “Dữ liệu máy”. Không hiển thị một đồng hồ rủi ro cuộc đời như trung tâm giao diện.

## 5. Trạng thái màn hình bắt buộc
Mỗi screen có empty, loading, ready, partial, validation_error, unauthorized, revoked, unsupported_method, quota_exhausted, provider_failure, offline và stale_version khi áp dụng. Nút bị khóa phải giải thích vì sao và bước hợp lệ tiếp theo. Skeleton không được tạo số giả để trang trông hoàn chỉnh. Thông báo lỗi không xóa nội dung người dùng đã nhập.

## 6. WCAG và ngôn ngữ
Mục tiêu WCAG 2.2 AA cho các luồng cốt lõi: focus nhìn rõ, dùng bàn phím, label/error liên kết, contrast, touch target, reduced motion, không chỉ dùng màu. Đặt đúng lang=vi và format ngày theo locale; ngôn ngữ hiển thị bằng tên đầy đủ. Bản dịch không thay claim type. Tên người giữ nguyên Unicode, không buộc đổi sang tiếng Anh. [N01][N07]

## 7. Offline và đồng bộ
Bản demo hiện không cài service worker và không lưu PII. Kế hoạch PWA cho phép cache tài liệu công khai; nội dung cá nhân cần thiết kế mã hóa local, thời hạn, logout purge và thu hồi chia sẻ. Nhật ký offline mang client_event_id, expected_version và trạng thái conflict. Server không tự ghi đè bằng last-write-wins. Người dùng phải thấy xung đột và chọn cách hòa giải.

## 8. Tài nguyên giao diện đã bàn giao
45 màn hình cũ được giữ nguyên, V2 bổ sung bảng đặc tả chi tiết cho core journeys. Demo có thư viện 90 ca, tìm kiếm, chọn nhóm, xem từng bước, tự nhập bốn công cụ và lưu JSON. Kiểm thử ở 360,390,768,1440 px là kiểm thử browser local; không gọi đó là kiểm thử native iOS/Android hoặc production E2E.

**Tra nguồn:** xem `11_SOURCES/SOURCE_ADDENDUM.csv`; các mã Nxx là nguồn đối chiếu chính thức, không phải mọi nhận định của HNH đã được khoa học xác nhận.
