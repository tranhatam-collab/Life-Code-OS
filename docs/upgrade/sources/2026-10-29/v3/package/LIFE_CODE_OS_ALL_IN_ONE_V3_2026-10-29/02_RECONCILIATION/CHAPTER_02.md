# 02. Bảo toàn V1, V2 và đối chiếu GitHub

Bộ V1 ngày 11/10/2026 có 149 tệp. ZIP V2 ngày 20/10/2026 có 307 mục tệp, trong đó đã chứa bản bảo toàn V1. V3 giữ nguyên toàn bộ nội dung ZIP V2 dưới 01_BASELINES/V2_EXPORT, đồng thời giữ cả hai ZIP gốc. Mỗi tệp có SHA-256 trong manifest bảo toàn. Tài liệu cũ không bị sửa để làm cho các quyết định mới có vẻ luôn tồn tại.

Nguồn GitHub được đọc lại ngày 29/10/2026: main ở 99b402764437f81859fa0cd3a3af860125f7bd52; nhánh audit ở 336ef35a8386a744c6de18a7f7c6e268e89e6dac. Nhánh wip/rescue-20261027-codex-complete-upgrade-plan-2026-10-20 cùng trỏ về commit audit. Điều này chưa chứng minh toàn bộ gói V2 đã được nhập lên remote. Bản local trên máy của Founder và deployed SHA vẫn chưa được tiếp cận trong lần này. [R02, R03, R27]

Các trang công khai được truy xuất chỉ là bằng chứng nội dung ở bề mặt đã đọc; công cụ có thể trả bản crawl. Không dùng nội dung giống nhau để suy ra deployed SHA. Không gọi API hồ sơ người thật hoặc tạo giao dịch trên production để kiểm tra.

Thứ tự ưu tiên khi đọc: dữ kiện nguồn được giữ nguyên; quyết định V3 đang trình duyệt không giả là đã phê duyệt; thay đổi chỉ có hiệu lực sau khi được ghi trong decision register. Nếu tài liệu cũ nói bắt buộc mua level trước hoặc dùng coverage để mở mọi cấp, V3 ghi rõ phương án thay thế, không xóa dòng lịch sử.

Hướng nhập dự án là bổ sung dưới docs/upgrades/2026-10-29-v3/. Không ghi vào engine hiện chạy hoặc thư mục public. Công cụ nhập chỉ kiểm tra và sao chép; không tự commit, push, merge hoặc deploy. Việc nhập và triển khai là hai quyết định riêng.
