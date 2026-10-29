# Bắt đầu sử dụng bộ nâng cấp V2

**Dự án:** tranhatam-collab/Life-Code-OS · **Ngày bàn giao:** 20/10/2026.

## 1. Nhà sáng lập và người phụ trách sản phẩm

Đọc `Life_Code_OS_Master_Upgrade_V2.pdf` (21 trang) để xem phần nâng cấp. Bản tổng hợp V1 47 trang được giữ nguyên trong `../01_BASELINE/2026-10-11/00_Doc_truoc/`; V2 bổ sung, không thay hoặc rút gọn tầm nhìn cũ. Dùng Word tương ứng để ghi ý kiến. Workbook V2 có 20 trang tính, giữ dữ liệu nhập và công thức của 11 trang tính cũ; Q21–Q30 là quyết định mới, chưa tự phê duyệt.

## 2. Tech Lead và đội backend

Đọc `Life_Code_OS_Backend_Formula_Demo_V2.pdf` (36 trang), sau đó dùng tệp nguồn ở `../05_BACKEND/`. Danh mục 32 công thức/adapter phân biệt rõ phần đã có mã tham chiếu và phần thiết kế/nghiên cứu. 83 thao tác API là kiến trúc đích; demo cục bộ chỉ có ba route, chưa có IdP, PostgreSQL, thanh toán, R2 hoặc nhà cung cấp AI.

## 3. Chạy phòng thử

Sau khi giải nén, mở Terminal tại thư mục gốc của gói. Cần Node.js 22 trở lên phù hợp môi trường của đội. Demo không cần cài thư viện npm.

```bash
cd 06_DEMO_LAB
npm test
npm run demo
npm start
```

Mở `http://127.0.0.1:8788`. Chọn tình huống, bấm **Tính và giải thích**, xem kết quả đọc được, đầu vào, dấu vết và JSON. Có 90 tình huống tổng hợp và ba hồ sơ minh họa xuyên suốt. Dừng máy chủ bằng Ctrl+C. Không nhập dữ liệu thật và không đưa máy chủ demo lên Internet.

Dữ liệu sinh giả định, thiếu giờ sinh hoặc có hai ngày sinh khác nhau được giữ đúng trạng thái, không tự chọn hộ. Những phần phương pháp chưa hỗ trợ trả thông báo giới hạn, không thay bằng điểm hoặc lời luận bịa.

## 4. Kiểm tra gói trước khi nhập repository

Nên kiểm tra trên bản giải nén nguyên vẹn trước khi chạy các lệnh tạo lại receipts. Cần Python 3; kiểm tra schema đầy đủ dùng thư viện trong requirements-verifier.txt.

```bash
python3 -m pip install -r requirements-verifier.txt
python3 VERIFY_PACKAGE.py --strict-schema --report /tmp/lifecode-v2-verification.json
python3 09_REPOSITORY/import_into_repo.py --repo /duong/dan/checkout/Life-Code-OS
```

Lệnh cuối chỉ dry-run. Thay đường dẫn ví dụ bằng checkout thật, đúng remote và đang ở nhánh review sạch. Chỉ sau khi đã đọc kết quả, chạy lại với `--apply`. Công cụ không ghi đè, không xóa, không commit, không push và không deploy. Có thể dùng patch đi kèm thay importer, nhưng không dùng cả hai một cách mù quáng trên đích đang nhập dở.

## 5. Trạng thái đồng bộ

GitHub đã cho đọc nguồn nhưng từ chối cả create_tree và create_branch với HTTP 403. **Chưa có thay đổi nào lên GitHub.** Bộ này cung cấp tệp đầy đủ, manifest, công cụ nhập và patch bổ sung để người có quyền thực hiện. Đường dẫn đích: `docs/upgrades/2026-10-20-v2/`.

## 6. Cách nghiệm thu

149 tệp gốc và ZIP gốc phải giữ nguyên SHA-256. Mã tham chiếu hiện có 125 kiểm thử Node/HTTP đạt; bộ gốc có 83 kiểm thử được chạy lại. Những kết quả đó không chứng minh đã sửa production hoặc kiểm định khoa học. Các việc sản xuất vẫn NOT_STARTED và chỉ được đóng khi có bằng chứng phù hợp. Native iOS/Android, xác thực thật, cơ sở dữ liệu, thanh toán, migration, khôi phục và kiểm thử bảo mật độc lập vẫn cần đội triển khai thực hiện.
