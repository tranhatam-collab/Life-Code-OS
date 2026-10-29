# Đối chiếu nguồn, nội dung công khai và trạng thái vận hành

Mã tài liệu: **D02** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Tech Lead + Security + QA. Nguồn đối chiếu: G01, G02, G04, G09, G10, S01, S03, S05, S06. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Baseline có thể tái kiểm tra
Remote main: `99b402764437f81859fa0cd3a3af860125f7bd52`. Nhánh kế hoạch mới: `audit/lifecode-os-comprehensive-upgrade-plan-2026-10-11`, SHA `336ef35a8386a744c6de18a7f7c6e268e89e6dac`. Đây là tài liệu chờ Team Audit; không xem việc tồn tại commit là Founder đã phê duyệt Q1–Q12.
Nguồn audit khai báo local phase HEAD `4df9b6efa6601bc113bc51956ed83e076da75657`; phiên này không truy cập máy Mac hoặc xác nhận worktree. Public home, chín tầng, Bắt đầu, Dashboard, Privacy và Engine Lab đọc được qua công cụ web; thông tin crawler không chứng minh byte-level live match. URL `.html` và probe `/health` gặp lỗi từ công cụ. Container không phân giải được các host. Điều này không chứng minh website ngừng hoạt động.
Không có Worker version, Pages deployment ID hay receipt runtime hiện hành. Vì vậy tách VERIFIED_SOURCE, VERIFIED_PUBLIC_CONTENT, REPORTED_BY_PRIOR_AUDIT, NOT_CHECKED và BLOCKED. Không sao chép nhãn VERIFIED_CURRENT của audit cũ sang mọi bảng mới.
## 2. Phát hiện kế thừa
API đọc profile theo ID chưa có kiểm tra session trong nhánh xử lý đã đọc. Session start nhận `user_id` từ payload và ghi hồ sơ. Report đọc result ID chưa khóa theo principal. Frontend gửi điểm cố định, session token lưu client-side. Timeline dùng tín hiệu từ seed/sin thay dữ liệu đánh giá. Những lỗi này được ghi theo SHA source; không tuyên bố đã khai thác hoặc đã xảy ra lộ dữ liệu.
Coverage cũ chia phần hợp lệ cho phần do client gửi nên một mảng nhỏ có thể đạt full. Một nhánh mission trừ 0,25 khỏi phần lẻ nhưng đòi ngưỡng 0,78 không thể kích hoạt theo công thức hiện có. Cách sửa là cách ly mô hình, không hạ ngưỡng cho xuất hiện thêm năm sứ mệnh.
## 3. Phát hiện cần bổ sung
Script Pages dùng rsync với denylist, không loại trừ tổng quát `api/`, `engine/`, `.env*` hoặc mọi loại tệp sẽ được bổ sung sau này. Chưa thấy secret bị lộ; đây là rủi ro thiết kế bundle. Phải chuyển sang public allowlist và kiểm tra artifact trước deploy.
Workflow Pages đọc được có `--commit-dirty=true`, bước tạo project dùng `|| true` và không có chuỗi gate đầy đủ trong workflow này. Không xóa cờ rồi tuyên bố chuỗi cung ứng đã an toàn: phải liên kết SHA, artifact hash, test run và deployment receipt.
## 4. Kết luận vận hành
NO_GO cho mở rộng dữ liệu sâu và báo cáo dựa trên điểm legacy. CONDITIONAL_GO cho trang giới thiệu đã sửa copy và công cụ dùng dữ liệu tổng hợp rõ nhãn. Không quy đổi trạng thái này thành 25%, 90% hoặc một con số cảm tính. Trạng thái từng cổng nằm trong release register; những cổng chưa thực hiện ghi NOT_CHECKED, không ghi pass.
