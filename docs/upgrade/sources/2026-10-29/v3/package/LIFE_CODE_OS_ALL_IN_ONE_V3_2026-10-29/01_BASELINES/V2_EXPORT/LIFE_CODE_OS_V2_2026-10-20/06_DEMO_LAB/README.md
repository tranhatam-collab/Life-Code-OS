# Phòng thực hành backend và giao diện

Đây là chương trình tham chiếu độc lập, chạy tại máy. Không kết nối hệ thống đang hoạt động.

```bash
npm test
npm run demo
npm run bench
npm start
```

Trình duyệt mở `http://127.0.0.1:8788`. Có 90 ca từ đúng đến sai, dữ liệu thiếu, giờ lặp, ngày nhuận, nhiều giả thuyết, policy và ba hồ sơ xuyên suốt. `data/demo-cases.json` ghi input và expected subset. `receipts` chứa kết quả lần chạy được bàn giao; chạy lại có thể đổi thời gian và hash receipt nhưng không nên đổi calculation cùng cấu hình.

Máy chủ bind 127.0.0.1; không sửa thành 0.0.0.0 để dùng công khai. Không có persistence, IdP, payment, R2 hoặc AI thật. Policy và idempotency chỉ là mô phỏng trên một process; cần staging riêng để chứng minh bảo đảm production.

`openapi.demo.json` mô tả đúng ba route demo. Hợp đồng 83 operation ở `../05_BACKEND/openapi.target.v2.json` là thiết kế đích, không phải endpoint đã chạy. Chín mẫu báo cáo có trạng thái thiếu dữ liệu rõ; chỉ ba hồ sơ Level 1 giả lập chạy đầy đủ luồng minh họa.

Giao diện dùng textContent, không render HTML từ dữ liệu người nhập. Kết quả JSON có thể lưu về máy. Không lưu input demo phía server. Không nhập giấy tờ, dữ liệu trẻ em, sức khỏe, mật khẩu hoặc token thật.

Kiểm tra browser trong môi trường bàn giao dùng markup cục bộ và transport loopback rõ ràng vì điều hướng HTTP trực tiếp bị hạn chế; HTTP API đã được test riêng. Kết quả này không phải production E2E hoặc chứng nhận WCAG.
