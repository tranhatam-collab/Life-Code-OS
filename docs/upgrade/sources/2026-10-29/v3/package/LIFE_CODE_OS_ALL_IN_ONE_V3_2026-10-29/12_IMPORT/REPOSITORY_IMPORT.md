# Nhập V3 theo cách bổ sung

Repository: `tranhatam-collab/Life-Code-OS`.
Đích: `docs/upgrades/2026-10-29-v3/`.

Công cụ `import_into_repo.py` không tạo nhánh, commit, push hoặc deploy. Người phụ trách chuẩn bị một nhánh review sạch trước. Remote được kiểm tra chính xác; không dùng thư mục có tên giống dự án làm bằng chứng.

Mặc định dry-run. Khi dùng `--apply`, chỉ những tệp chưa tồn tại được sao chép, tệp giống hệt được bỏ qua, tệp khác nội dung làm toàn bộ tiền kiểm thất bại. Symlink hoặc đường dẫn đi ra ngoài thư mục bị từ chối.

Trong lần bàn giao này chưa thử ghi remote. Lịch sử lần trước có HTTP 403; không coi quyền ấy là đã được cấp lại. Bản local trên máy của Founder và receipt triển khai vẫn chưa được xác nhận.

Các file gói chứa toàn bộ baseline, nên cần kiểm tra chính sách dung lượng repository. Khi dùng Git LFS hoặc artifact storage cho bản nhị phân, phải giữ manifest và đường tham chiếu có kiểm tra hash; không lặng lẽ loại bỏ tệp để làm gói nhỏ hơn.

Trước merge: đối chiếu manifest, chạy test trong bản sao, kiểm tra diff và bảo đảm public build không đóng gói docs, SQL, ZIP, fixture hoặc thông tin nội bộ. P0/Trust Core và triển khai vẫn là công việc riêng.
