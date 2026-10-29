# Adapter, ma trận demo và cách chuyển mã tham chiếu thành sản phẩm

**Life Code OS · V2 · 20/10/2026**  
**Phạm vi:** Đặc tả triển khai; mã demo chỉ là tham chiếu cục bộ, chưa phải production.

## 1. Hợp đồng adapter
Một adapter nhận input đã kiểm tra, cấu hình bất biến, source artifact và as_of. Nó trả calculation, trace, missing inputs, warnings và limitations. Adapter không truy cập tài khoản, cơ sở dữ liệu production hoặc mô hình AI trực tiếp. Service orchestration chịu trách nhiệm quyền và việc đọc dữ liệu; pure calculation chịu trách nhiệm tính đúng.

Các thông tin số dùng đơn vị cụ thể. Với tiền, minor units là chuỗi số nguyên trong JSON và BigInt trong runtime; không đi qua float. Với ngày, chuỗi ISO là ngày dân dụng theo lịch đã khai báo, không tự parse bằng Date rồi để timezone của máy làm thay đổi ngày.

## 2. Mức độ triển khai trong gói
16 họ công thức LCF-01–LCF-16 có mã tham chiếu. Ba hàm về DAG, impact analysis và cache key là công cụ điều phối; các hàm policy/report/pipeline là mô phỏng nghiệp vụ để thử kết nối. Tổng cộng 27 khóa dispatcher và 90 tình huống có thể chạy tại máy. Không có 27 môn được tuyên bố triển khai khoa học.

Một số phương pháp nâng cao được giữ trong catalog nhưng chưa chạy: Bát tự đầy đủ, Tử Vi, ephemeris/chiêm tinh, Jyotish, Tam thức, lịch âm lịch sử, Psychomatrix nhiều trường phái và phân tích văn tự ngoài Latin. Chúng có điều kiện đầu vào, nguồn phải bổ sung và cách nghiệm thu riêng.

## 3. Các loại demo phải cùng tồn tại
Có ca đúng; ca sai định dạng; ca thiếu dữ liệu; ca mâu thuẫn; ca chưa có quyền; ca bị chính sách cấm; ca phương pháp chưa phát hành; ca xung đột phiên bản; ca lặp yêu cầu; ca đọc và xuất kết quả cho người dùng. Một hệ chỉ minh họa đầu vào đẹp không đủ để DEV biết cách xử lý thực tế.

Ba hồ sơ xuyên suốt là dữ liệu tổng hợp: đủ dữ liệu nền; thiếu giờ sinh; nhiều giả thuyết ngày sinh. Các tên trong demo không dùng để nhận diện người thật. Mỗi hồ sơ trả bốn phần nội dung, dữ liệu còn thiếu và xác suất null. Nội dung gợi ý hành động được gắn vai trò planning_guidance; không giả làm self-report của người dùng.

## 4. Bốn loại kiểm thử
Unit/property tests kiểm số nguyên, Unicode, ngày nhuận, 64 cặp, 64 quẻ × 64 mặt nạ và invariants. HTTP tests kiểm loopback, body limits, định dạng lỗi và static allowlist. Browser tests kiểm các ca hiển thị, dữ liệu máy, tự nhập và các độ rộng màn hình. Production tests về IdP, PostgreSQL, payment, R2, queue và xóa dữ liệu chưa nằm trong demo.

Bản receipt ghi môi trường Node, ICU và tzdb thật. Việc dùng tzdb2025b trong Node tham chiếu không có nghĩa đó là dữ liệu múi giờ mới nhất của thế giới; production phải khóa và cập nhật phiên bản theo chính sách riêng. Phạm vi local-time resolver được công bố, không dùng nó để khẳng định đã giải đúng mọi lịch sử thiên văn.

## 5. Đọc benchmark đúng cách
Benchmark chạy từng phương pháp trong một process, không có mạng, DB, AI hay dựng sách. Thời gian millisecond chỉ mô tả lần chạy đó. Không chuyển kết quả 250 vòng lặp thành SLA, năng lực phục vụ người dùng đồng thời hoặc bằng chứng có thể xuất 600 trang tức thì.

Bài thử staging về sau phải ghi máy, vùng, số người dùng đồng thời, payload, cache hit rate, độ dài nội dung, percentile, lỗi và ngân sách. Tối ưu sau khi biết nút thắt; không bỏ kiểm quyền để giảm latency.

## 6. Chuyển từ reference sang production
Thứ tự: review phương pháp → đưa pure functions vào package canonical → contract tests → tích hợp auth/purpose → transaction/outbox → observability → staging negative tests → pilot có consent → release receipt. Không sao chép server demo lên Worker public vì demo cố ý không có auth, database hay thanh toán.

Mọi adapter mới phải có ít nhất ví dụ nguồn được đối chiếu độc lập, kiểm thử biên, kiểm thử dữ liệu thiếu, câu giải thích ngắn cho người dùng và danh sách nhận định không được phép. Một phương pháp chưa đạt có thể được hiển thị như tài liệu nghiên cứu, nhưng nút “Tính” không được tạo kết quả thay thế.
