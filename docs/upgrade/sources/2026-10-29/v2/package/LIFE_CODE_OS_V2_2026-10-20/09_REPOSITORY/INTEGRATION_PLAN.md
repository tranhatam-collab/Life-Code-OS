# Đưa V2 vào đúng dự án, giữ nguyên kế hoạch cũ

**Life Code OS · V2 · 20/10/2026**  
**Trạng thái:** Bộ bàn giao đầy đủ trong gói; thao tác ghi GitHub bị chặn bởi quyền kết nối.

## 1. Đích cố định
Repository đích là `tranhatam-collab/Life-Code-OS`. Đường dẫn bổ sung là `docs/upgrades/2026-10-20-v2/`. Không đặt kho tài liệu, SQL, tệp nén hoặc dữ liệu kiểm thử vào thư mục được phát hành công khai của website. Không sửa main, quy trình triển khai, migration đang chạy hoặc mã legacy trong bước bàn giao kế hoạch.

## 2. Kết quả thao tác GitHub thực tế
Kết nối cho phép đọc repository, nhưng cả hai thao tác tạo cây tệp và tạo nhánh mới đều trả HTTP 403 với thông báo “Resource not accessible by integration”. Do đó chưa có commit, nhánh hay pull request mới được tạo trong lần bàn giao này. Không được ghi trạng thái “đã đồng bộ toàn bộ”. Chi tiết nằm trong `DELIVERY_RECEIPT.json` cùng thư mục.

## 3. Nhập an toàn từ gói bàn giao
Công cụ `import_into_repo.py` mặc định chỉ kiểm tra và lập danh sách. Nó xác minh remote đúng dự án, nhánh không phải main/master/production, worktree sạch, manifest hợp lệ và không có symbolic link hoặc tệp đích khác nội dung. Chỉ khi thêm `--apply`, công cụ mới sao chép các tệp còn thiếu; không ghi đè, xóa, commit, push hoặc deploy.

Chạy công cụ từ một checkout sạch của nhánh review. Nếu đã chạy demo hoặc thay tệp trong gói, dùng lại bản giải nén nguyên vẹn để kiểm tra manifest. Một tệp có hash khác phải được giải quyết rõ trước khi nhập; không dùng reset hoặc force để xóa thay đổi chưa được bảo toàn.

## 4. Bản vá bổ sung
Tệp patch đi kèm chứa các bổ sung dưới đường dẫn V2. Trước khi áp dụng, kiểm tra `git apply --check` trên nhánh review và đọc danh mục thay đổi. Không áp patch và importer tùy tiện lên một thư mục đang nhập dở. Chỉ dùng một phương án, đối soát đầy đủ rồi mới commit theo quy trình đội dự án.

## 5. Kiểm tra sau nhập
Kiểm lại checksum toàn gói và 149 tệp nền. Chạy kiểm thử Node, 90 tình huống và xem giao diện cục bộ. Rà soát toàn bộ diff trước commit. Không chạy các lệnh deploy trong gói nguồn cũ. Trước khi merge, kiểm tra bản dựng public không chứa tài liệu nội bộ, tệp ZIP, SQL, report riêng hoặc fixture.

## 6. Điều kiện hoàn tất đồng bộ
Chỉ khi mọi tệp manifest tồn tại ở repository đích với hash phù hợp mới được chuyển trạng thái thành FULL_PACKAGE_IMPORTED. Receipt cần commit, branch, danh mục tệp, thời gian, người thực hiện và kết quả kiểm tra. Việc đồng bộ tài liệu cũng không phải phê duyệt triển khai ứng dụng hoặc xác nhận đã khắc phục P0.
