# Tham chiếu PostgreSQL V2

Tệp SQL bổ sung minh họa 7 bảng cốt lõi với composite foreign keys, claim constraints, outbox và idempotency. Không thay 41 thực thể của bản cũ; không phải schema sản phẩm đầy đủ. Tệp kết thúc bằng ROLLBACK có chủ ý và chưa được thực thi trên PostgreSQL trong lần bàn giao này.

Trước migration thật: chọn runtime role không owner/BYPASSRLS; chạy trong database cô lập; bổ sung đầy đủ policies theo action/purpose và processing basis; kiểm thử A/B tenant/subject; thử revoke đồng thời; thử xóa/restore; duyệt migration expand-contract. RLS không thay xác thực, entitlement hoặc điều kiện xử lý dữ liệu.

Các policy đọc minh họa không cấp quyền ghi. Schema khác, role khác và grant khác cần test độc lập. Không bỏ ROLLBACK rồi chạy thẳng production.
