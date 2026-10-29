# Hiệu năng, bộ nhớ đệm và vận hành ít thao tác

**Life Code OS · Bản nâng cấp bảo toàn V2 · 20/10/2026**  
**Trạng thái:** Đặc tả để triển khai và rà soát; không phải chứng nhận production.

## 1. Đặt ngân sách theo loại tác vụ
Phép số ngắn nên nhanh và có thể chạy local cho guest; pipeline có dữ liệu riêng chạy qua server; render sách và AI chạy nền. Không đặt một SLA chung cho phép chia 80 và sách 600 trang. Benchmark tham chiếu trong gói chỉ đo CPU cục bộ không mạng, không DB, không AI; cần load test thật trước cam kết.

## 2. Cache có provenance và ACL
Cache key phải gồm tenant/subject hoặc namespace public, input digest, method version, config digest, source/table digest, locale version và policy revision. Không cache kết quả cá nhân theo ngày sinh chung. Cache dữ liệu công khai dùng riêng với cache profile. Dữ liệu thu hồi phải invalidation theo lineage; cache không trở thành nơi chứa bản cũ còn truy cập được.

## 3. Tính gia tăng
Một đổi mục tiêu không làm lại lịch thiên văn; đổi ngày sinh không cần render lại tài liệu nguồn công khai. DAG nêu inputs của từng node, tính hash subtree và chỉ chạy các node bị ảnh hưởng. Khi thay rule table, tạo impact job tìm report phụ thuộc, không sửa PDF lịch sử âm thầm. Chạy lại có trạng thái và quyền, không tự tính phí ngoài phạm vi.

## 4. Quan sát hệ thống
Metrics gồm throughput, latency, queue age, rejection reason, failed grant, method failure, render error, review backlog, cost/token và correction rate. Log là sự kiện kỹ thuật tối thiểu; không log tên, số điện thoại, lời tự thuật hoặc hình ảnh. Trace ID nối gateway/job/report nhưng không được dùng làm token truy cập.

## 5. Circuit breaker và ngân sách
AI provider timeout/quota có fallback về công cụ xác định hoặc báo chưa sẵn sàng. Không đổi sang model chưa được phép xử lý loại dữ liệu đó. Mỗi SKU có token cap, retry cap, render count, storage retention và reviewer budget. Khi vượt ngân sách, pause/notify theo chính sách, không tự mua thêm quota hoặc trừ tiền khách.

## 6. SLO đích và diễn tập
Giữ mục tiêu thiết kế của bộ cũ, nhưng đo lại trên tải thật. Restore phải phục hồi database, object mapping, rule registry, grants, tombstones và báo cáo cùng phiên bản. RPO/RTO không chỉ là dòng trong tài liệu: cần receipt diễn tập, dữ liệu tổng hợp, thời gian đo và sai khác. Rollback về safe mode nếu không có artifact an toàn.
