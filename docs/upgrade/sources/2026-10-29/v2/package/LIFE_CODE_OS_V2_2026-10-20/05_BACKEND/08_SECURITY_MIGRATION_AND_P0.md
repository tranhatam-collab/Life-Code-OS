# Khống chế P0 và chuyển dữ liệu không mất lịch sử

**Life Code OS · Bản nâng cấp bảo toàn V2 · 20/10/2026**  
**Trạng thái:** Đặc tả để triển khai và rà soát; không phải chứng nhận production.

## 1. V2 không tự sửa production
Gói mới là kế hoạch và mã tham chiếu. Giữ nguyên P0 packet cũ; bổ sung readiness checklist và tests. Các endpoint legacy cần khóa phía server trước khi mở thu dữ liệu. Xác thực phải bắt nguồn từ phiên hợp lệ, không payload.user_id. Chỉ sửa storage token không giải quyết cấp phiên sai danh tính.

## 2. Khoanh vùng legacy
Nhóm A: raw data có nguồn và quyền có thể kiểm tra. Nhóm B: chưa rõ ownership hoặc tính toàn vẹn, cần quarantine. Nhóm C: điểm/timeline/lời luận từ demo, lưu experimental_legacy và không dùng làm sự thật. Chuyển dữ liệu theo bảng mapping từng field với rule transform và lý do. Không chuyển một câu AI từng viết thành sự kiện đời thật.

## 3. Trình tự migration
Inventory→read-only snapshot riêng tư→mapping→dry-run synthetic→rehearsal data được phép→đối soát số lượng và checksum có phạm vi→phê duyệt→write freeze ngắn theo kế hoạch→migrate→reconcile→chuyển traffic→giám sát→decommission theo retention. Không xóa D1 ngay khi thấy PostgreSQL có dữ liệu. Dual-write cần thiết kế nhất quán riêng; không bật cho tiện.

## 4. Build và supply chain
Build public theo allowlist, không sao chép toàn repo rồi bỏ vài thư mục. Bộ V2 và toàn bộ baseline nằm dưới docs để không lẫn vào public assets. Dù vậy pipeline phải kiểm tra dist không có sql, report riêng, archive, test fixture hoặc secrets. Pin dependency/lockfile, kiểm license, SBOM, secret scan và provenance artifact. Không dùng commit-dirty cho production release.

## 5. Phiên và browser
Secure/HttpOnly cookies cùng CSRF phù hợp cho web. Quyền cookie không thay object authorization. Mobile/native có OIDC/PKCE và keychain riêng khi được triển khai; không chia sẻ token qua URL hoặc localStorage. Recovery không dùng tên/ngày sinh làm bí mật. Browser không được chứa admin credential hoặc service role.

## 6. Dữ liệu nghiêm trọng và chuyển giao
Tiếp nhận sức khỏe/ảnh/trẻ em/quan hệ nhiều bên chờ scope gate. Hội đồng phương pháp không có quyền mặc định đọc khách hàng thật. Khi partner rời hệ, cần chuyển hỗ trợ và quyền dữ liệu hợp lệ, không dùng dữ liệu làm đòn bẩy. Những bước này phải có owner và evidence, không chỉ có chính sách công khai.
