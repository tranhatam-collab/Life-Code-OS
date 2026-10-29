# Thiết kế dữ liệu logic

`SCHEMA_DESIGN_REFERENCE.sql` có 41 bảng làm bản tham chiếu. Không phải migration đã kiểm thử PostgreSQL hoặc patch D1. Không tạo role hay credential. RLS bật FORCE và chưa có policy cho phép; hệ runtime mặc định không được đọc dữ liệu. Cần hoàn thiện policy chi tiết, transaction context đáng tin, database provider, migration plan và integration tests trước thực thi.

JSON fields không miễn trách nhiệm kiểm tra schema: service phải dùng JSON Schema theo release và constraints bổ sung. Nhiều chủ thể trong relationship report cần junction table có grant từng bên trước release; schema tham chiếu hiện ưu tiên một subject cho beta. Country/legal/academy entities là khung mở rộng, không tức là đã triển khai.

`ENTITY_REGISTRY.json` là nguồn field-level để thiết kế ERD tiếp. Những dấu vết nhạy cảm không đưa vào public schema fixtures. Thông số kết nối và tên provider nằm trong quyết định Q15, không có giá trị giả trong gói.
