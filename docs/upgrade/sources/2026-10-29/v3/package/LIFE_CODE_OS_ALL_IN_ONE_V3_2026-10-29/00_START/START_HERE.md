# HƯỚNG DẪN ĐỌC VÀ ÁP DỤNG V3

## 1. Bản này thay đổi điều gì?

V3 chuyển từ một tập các mô-đun tham khảo sang thiết kế all-in-one: một hồ sơ có phiên bản, nhiều không gian sản phẩm, nhiều phương pháp có nguồn và một bộ kết quả giữ nguyên loại nội dung. Người dùng không phải nhập lại mọi thứ cho từng cấp; chỉ bổ sung dữ liệu cần thiết theo mục tiêu và quyền đã chọn.

Hai sách mới gồm kế hoạch hợp nhất 25 trang và Atlas số–tên–Bát Cực 23 trang. Các đặc tả chi tiết, bảng công thức, dữ liệu tra, API, schema, SQL thiết kế, demo và công việc nằm ở các thư mục chuyên môn. Không lấy độ dài hai sách làm kích thước toàn bộ kế hoạch.

## 2. Thứ tự đọc cho Nhà sáng lập

Đọc sách kế hoạch, sau đó Atlas. Duyệt Q31–Q45 bổ sung, không ghi đè Q1–Q30. Xem bảng đối chiếu yêu cầu để biết yêu cầu nào đã có mã tham chiếu, yêu cầu nào mới đạt mức đặc tả, nguồn nào vẫn thiếu toàn văn.

## 3. Thứ tự đọc cho Tech Lead

Bắt đầu từ `02_RECONCILIATION/GITHUB_BASELINE_2026-10-29.json`; đối chiếu với repository hiện tại trước mọi lần nhập. Tiếp theo là `07_BACKEND/EXECUTION_AND_DATA_SPEC.md`, `openapi.v3.target.json`, schema, `BACKEND_ACCEPTANCE_MATRIX.md` và thiết kế SQL. Kế thừa P0/Trust Core của V1/V2, không bỏ qua vì đã có bộ demo chạy.

## 4. Chạy phòng thử

```bash
cd 08_ALL_IN_ONE_LAB
npm test
npm run test:legacy
npm run demo
npm start
```

Mở `http://127.0.0.1:8788`. Các tab gồm Phòng thử, Một hồ sơ, Chín cấp & dòng đời và Cách đọc. Có 167 tình huống giả lập. Các tình huống lỗi cũng là một phần của kiểm thử, không phải toàn bộ đều phải trả kết quả thành công.

Chạy `npm run demo` sẽ cập nhật receipt cục bộ. Để giữ bản bàn giao khớp manifest, hãy kiểm tra gói trước, giữ một bản nguyên vẹn và chạy demo trong bản sao làm việc. Không nhập nguyên bản đã bị sửa vào repository mà chưa ghi lại thay đổi.

## 5. Kiểm tra và nhập đúng dự án

Từ thư mục gốc gói, chạy `python3 VERIFY_PACKAGE.py`. Dùng một checkout sạch trên nhánh review của `tranhatam-collab/Life-Code-OS`, ngoài thư mục đồng bộ không ổn định. Công cụ nhập mặc định dry-run:

```bash
python3 12_IMPORT/import_into_repo.py --repo /duong/dan/toi/Life-Code-OS
```

Chỉ sau khi kiểm tra danh sách tệp và quyền thực hiện, chạy lại với `--apply`. Công cụ từ chối main/master/production, remote sai, worktree bẩn, checksum sai, symlink và tệp đích khác nội dung. Không ghi đè hoặc xóa tệp. Nó không tự add, commit, push hay deploy.

## 6. Nghiệm thu đúng phạm vi

192 kiểm thử V3 và các bộ cũ đã được chạy cục bộ. HTTP API demo được kiểm thử bằng Node. Trình duyệt của môi trường hiện tại chặn điều hướng loopback; việc rà giao diện dùng render ngoại tuyến với fixture kết quả, không phải integrated browser E2E. Native app, IdP thật, PostgreSQL/RLS, payment, queue cloud, backup/restore và production security vẫn cần kiểm thử staging riêng.

## 7. Nguyên tắc không mất kế hoạch

`01_BASELINES/V2_EXPORT` giữ 307 tệp từ ZIP V2, gồm 149 tệp V1 bên trong. Hai ZIP gốc được giữ riêng. Nội dung cũ có thể chứa công thức hoặc claim đã bị kế hoạch mới cách ly; bảo toàn lịch sử không có nghĩa tiếp tục cho phép các đầu ra đó trên production.

## 8. Thứ tự thực thi

Containment và khóa source → Trust Core → phương pháp được duyệt → sản phẩm nền và kế hoạch hành động → báo cáo có rà soát → paid beta → mở rộng theo cổng. Không triển khai trọn 62 adapter, 99 API hoặc 69 màn hình trong một bước chỉ để đạt nhãn “all-in-one”.
