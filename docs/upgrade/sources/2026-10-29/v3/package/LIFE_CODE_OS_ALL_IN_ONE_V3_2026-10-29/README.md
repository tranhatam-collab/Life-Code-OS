# LIFE CODE OS — ALL-IN-ONE V3

Ngày khóa: 29/10/2026. Dự án đích: `tranhatam-collab/Life-Code-OS`.

Đây là bản tích hợp kế hoạch, đặc tả và phòng thử tham chiếu, không phải toàn bộ Life Code OS đã triển khai. V1 và V2 được giữ nguyên từng byte dưới `01_BASELINES/`; không sửa tài liệu cũ để làm mất lịch sử.

## Bắt đầu

1. Đọc `00_START/START_HERE.md` và hai cuốn PDF/Word trong cùng thư mục.
2. Xem `Life_Code_All_In_One_Execution_V3.xlsx`: 21 trang tính hợp nhất.
3. Đối chiếu `02_RECONCILIATION/REQUIREMENTS_TRACE_V3.json`: 62 yêu cầu có đường dẫn và giới hạn.
4. Chạy `python3 VERIFY_PACKAGE.py`, sau đó bộ thử và demo cục bộ.
5. Nhập bổ sung vào nhánh review bằng `12_IMPORT/import_into_repo.py`; không nhập thẳng main.

## Các phần mới

- 23 thành phần bộ số–tên có chính sách và các bước trung gian.
- Bát Cực: 64 cặp, vị trí, chuỗi ba chữ số, ma trận chuyển nhóm 8×8, số lặp, diagnostic 0/5 và nguồn mâu thuẫn.
- 64 câu hỏi HNH chuyển nhóm là nội dung biên tập mới, KHÔNG phải 64 quy tắc cổ đã xác minh.
- Mã đuôi 80 đủ bảng nguồn và phần ứng dụng; Psychomatrix 17 vị trí ở hai chế độ riêng.
- 18 lĩnh vực đời sống, 54 tình huống, 100 khoảng tuổi 0–99, các đường lịch sử/kế hoạch/chu kỳ tách biệt.
- 62 adapter trong 20 họ tri thức; từng adapter ghi rõ phần có mã và phần cần nghiên cứu/triển khai.
- 28 sản phẩm, chín cấp, học viện, chuyên gia, tổ chức và cấp phép theo lãnh thổ.
- 99 thao tác API mục tiêu; máy chủ demo chỉ có ba route API. 10 JSON Schema mới, thiết kế SQL mở rộng chưa thực thi.
- 167 ca demo, 192 kiểm thử V3; đã chạy lại 125 kiểm thử V2 và 83 kiểm thử V1.

## Chạy demo

```bash
cd 08_ALL_IN_ONE_LAB
npm test
npm run demo
npm start
```

Mở `http://127.0.0.1:8788`. Cần Node.js 22 trở lên tương thích; bộ demo không cần tải thư viện npm. Không nhập dữ liệu cá nhân thật. Không có tài khoản, PostgreSQL, thanh toán, R2 hoặc nhà cung cấp AI trong máy chủ demo.

## Ranh giới bàn giao

Không sửa repository từ xa, không commit/push/deploy, không migrate dữ liệu thật. Deployed SHA chưa được xác nhận. Nhánh rescue trên GitHub vẫn trỏ về commit audit khi đối chiếu; việc nhập toàn bộ V2/V3 lên remote chưa được xác nhận.

Bản sách nâng cao Bát Cực trong ảnh chưa được tiếp cận toàn văn. Nguồn công khai được ghi phạm vi trong `13_SOURCES/`. Không gọi các kết quả biểu tượng là phép đo sức khỏe, trí tuệ, nhân cách hoặc dự báo số phận.

Mở `INDEX.html` để tìm tệp ngoại tuyến. SHA-256 của mọi tệp được ghi trong `MANIFEST.json`, trừ chính manifest.
