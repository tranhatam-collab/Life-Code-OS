# 22. Nâng cấp hiện trạng: P0 và đồng bộ không mất dữ liệu

Các vấn đề P0 được ghi nhận ở baseline trước vẫn phải đối chiếu với source và runtime hiện hành: điểm hardcode; timeline tạo bằng Math.sin; quyền dựa vào ID do client gửi; session chưa an toàn; coverage lấy mẫu số từ các lớp client đưa lên. Demo mới không tự sửa những đường production ấy.

Bước đầu là khóa các đường dữ liệu chưa an toàn, vô hiệu session cũ theo kế hoạch, giữ bằng chứng riêng tư và chốt source, artifact, runtime. Không tạo yêu cầu đọc hồ sơ người thật để chứng minh lỗi. Một endpoint health trả 200 chỉ thể hiện liveness, không phải kiểm thử phân quyền end-to-end.

Output legacy được gắn experimental_legacy. Không chuyển lời luận AI cũ thành self_report vì nó nằm trong hồ sơ một người. Hồ sơ chưa xác nhận chủ sở hữu phải cách ly; tên và ngày sinh không đủ để phục hồi quyền. Migration có đối soát và chạy thử; backup restore áp lại các chỉ thị xóa để dữ liệu đã xóa không quay lại.

V3 bổ sung dưới docs/upgrades/2026-10-29-v3/. Nhánh review sạch, remote đúng và manifest khớp là điều kiện nhập. Công cụ từ chối ghi đè nội dung khác, đường dẫn vượt thư mục, symlink và worktree có thay đổi chưa xử lý. Nó không tự chạy SQL hoặc script deploy. Rollback chỉ về bản an toàn; nếu chưa có, duy trì chế độ giới thiệu hoặc bảo trì.

Receipt phát hành cần commit SHA, artifact digest, CI run, deployment ID, schema version, method configuration, tests, người duyệt, thời điểm và rollback target. Không dùng việc trang web trông giống một nhánh mã để khẳng định nhánh đó là bản đang chạy.

Các tệp cũ được giữ để truy vết, nhưng không được đưa nhầm vào bundle website. Build production phải có allowlist tài nguyên công khai; loại tài liệu nội bộ, SQL, ZIP, demo, dữ liệu mẫu và receipt nhạy cảm. Đưa kế hoạch vào repository không đồng nghĩa xuất bản tất cả nội dung lên website.
