# Frontend: điều hướng, trang công khai và không gian ứng dụng

Mã tài liệu: **D18** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Frontend Lead + UX. Nguồn đối chiếu: S01, S02, S03, S04, S06, S18, S19. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Giữ URL công khai, thay trải nghiệm có kiểm soát
Không đổi tên miền hay phá SEO. Home, giới thiệu, hệ thống, chín tầng, LCI, timeline, báo cáo, FAQ, bản quyền, terms, privacy và liên hệ được giữ hoặc 301 một bước tới đường chuẩn. `.html` không tạo nội dung trùng; canonical/hreflang cho từng locale. Engine Lab chuyển khu staging/internal có auth, không chỉ bỏ nav.
Sau P0, marketing dùng static build; app dưới /app dùng route shell riêng. Các route tương tác không được lập chỉ mục. robots/noindex không phải bảo mật; server vẫn kiểm tra quyền. Sitemaps chỉ liệt kê nội dung public được phép, không URL hồ sơ/report hoặc receipt riêng.
## 2. App navigation
Điều hướng chính: Hôm nay, Hồ sơ, Khám phá, Hành động, Báo cáo. Nút hồ sơ luôn hiện chủ thể và không gian cá nhân/tổ chức để tránh thao tác nhầm. Mục Cài đặt gồm quyền chia sẻ, dữ liệu/xóa, bảo mật phiên, thông báo, gói dịch vụ, hỗ trợ và ngôn ngữ. Quota và trạng thái job nhìn được nhưng không chiếm chỗ hành động chính.
## 3. Home mới
Mở đầu bằng giá trị cụ thể: “Hiểu dữ liệu của mình, khám phá góc nhìn có nguồn và xây bước đi phù hợp.” Ba CTA: thử công cụ miễn phí, lập kế hoạch, tìm hiểu chín cấp. Không dùng video autoplay hoặc testimonial giả. Phần phương pháp giải thích loại dữ liệu; trang sản phẩm hiển thị input needed, expected output, limitations, price status và review mode.
## 4. Dashboard mới
Hàng đầu là mục tiêu, hành động kế tiếp và báo cáo đang xử lý. Tiếp theo là thay đổi từ lần trước và điều người dùng muốn cập nhật. Không có đồng hồ “nguy cơ số phận”. Coverage được giải thích bằng các trường còn thiếu cho nhu cầu đang chọn, không áp một con số 38% cho toàn con người. Empty state có mẫu synthetic và CTA phù hợp, không tự điền điểm.
## 5. Screen registry
Bộ kèm `SCREEN_REGISTRY.csv` mô tả route, mục đích, dữ liệu, quyền, loading/empty/error/blocked/ready states và nghiệm thu cho public, user, pro, org, academy, partner và admin. Mọi screen có bản mobile, keyboard và screen-reader. Không vẽ chỉ happy-path rồi để dev tự nghĩ phần lỗi.
## 6. Công nghệ và chuyển đổi
Chưa chuyển framework trong P0. Sau đó chọn Astro marketing, React/Vite app vì ranh giới static/interactive rõ; API shared contract. Không buộc Next.js thêm lớp server không cần thiết. Component library nội bộ có tokens, form primitives, evidence badge và report block renderer. Mỗi PR nhỏ có visual regression và routes smoke.

## Bổ sung thực thi 2026-10-20
`04_PWA_RESPONSIVE_EXECUTION_PLAN_2026-10-20.md` và `SCREEN_EXECUTION_EXTENSION.*` chuẩn hóa đủ 45 route, phone/tablet/desktop transformations, state/offline/cache/a11y/test/evidence. Đây là responsive web/PWA; native app không thuộc deliverable hiện tại.
