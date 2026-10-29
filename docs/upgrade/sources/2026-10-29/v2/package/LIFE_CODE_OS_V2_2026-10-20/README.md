# Life Code OS — Bộ nâng cấp bảo toàn V2

**Ngày:** 20/10/2026. **Dự án đích:** `tranhatam-collab/Life-Code-OS`.

## Đọc trước

Bộ gốc 149 tệp ngày 11/10/2026 và ZIP gốc nằm nguyên vẹn trong `01_BASELINE`. V2 là lớp bổ sung, không xóa kế hoạch cũ. Xem `02_REVIEW` để đối chiếu từng tệp và các thay đổi.

- Founder: `00_READ_FIRST`, sản phẩm và các quyết định Q21–Q30.
- Tech Lead: `05_BACKEND`, OpenAPI, schema và ma trận nghiệm thu.
- DEV/QA: `06_DEMO_LAB`, 90 tình huống; `10_QA` để đọc bằng chứng.
- UX: `07_UI`, 57 màn hình kế hoạch và ảnh giao diện demo.
- Triển khai: `08_EXECUTION`, giữ 140 việc gốc và thêm 68 việc làm rõ phạm vi; không cộng hai lớp ước lượng một cách máy móc.
- Repository: `09_REPOSITORY`; chỉ nhập vào nhánh review, không main và không deploy.

## Chạy demo cục bộ

Cài Node.js từ phiên bản 22 phù hợp môi trường của đội. Không cần tải thư viện cho demo này.

```bash
cd 06_DEMO_LAB
npm test
npm run demo
npm start
```

Mở `http://127.0.0.1:8788`. Dùng Ctrl+C để dừng. Không đưa dữ liệu thật vào phòng thử. Máy chủ không có tài khoản, PostgreSQL, thanh toán hoặc nhà cung cấp AI. Demo không dùng tài nguyên bên thứ ba và không phải ứng dụng production.

## Mức độ hoàn thành

`REFERENCE_TESTED`: các phép tính và mô phỏng đã có test cục bộ.
`DESIGN_ONLY`: API đích, SQL, auth và hạ tầng cần triển khai và thử riêng.
`RESEARCH_ONLY`: phương pháp nâng cao chưa đủ nguồn hoặc chưa có adapter.
`PRODUCTION_VERIFIED`: chưa cấp cho bất kỳ chức năng nâng cấp nào trong gói này.

Các kết quả sinh từ số là phép tính hoặc nội dung biểu tượng; không xác định sức khỏe, trí tuệ, tài lộc hay định mệnh. Không dùng số lượng test hoặc số trang để quảng bá độ chính xác dự báo.

## Giới hạn đồng bộ dự án

**GitHub từ chối thao tác ghi với HTTP 403: chưa có tệp, commit, nhánh hoặc pull request mới được tạo.** Đọc `09_REPOSITORY/DELIVERY_RECEIPT.json` để xem biên bản. Toàn bộ gói vẫn cần được nhập bởi người có quyền ghi repository. Tệp hoặc ZIP ở cuộc trò chuyện không tự trở thành tệp trong repository. Importer có dry-run, kiểm tra remote, checksum, xung đột và không ghi đè. Không dùng dữ liệu cá nhân của các cuộc trao đổi trước để đưa vào repository public.

## Tính toàn vẹn

`MANIFEST.json` ghi SHA-256 cho các tệp đã bàn giao, trừ chính manifest. `VERIFY_PACKAGE.py` kiểm tra manifest, baseline và cấu trúc chính. Tất cả thay đổi sau bàn giao phải được tạo thành phiên bản tiếp theo.
