# Thiết kế dữ liệu logic

`SCHEMA_DESIGN_REFERENCE.sql` có 41 bảng làm bản tham chiếu. Không phải migration đã kiểm thử PostgreSQL hoặc patch D1. Không tạo role hay credential. RLS bật FORCE và chưa có policy cho phép; hệ runtime mặc định không được đọc dữ liệu. Cần hoàn thiện policy chi tiết, transaction context đáng tin, database provider, migration plan và integration tests trước thực thi.

JSON fields không miễn trách nhiệm kiểm tra schema: service phải dùng JSON Schema theo release và constraints bổ sung. Nhiều chủ thể trong relationship report cần junction table có grant từng bên trước release; schema tham chiếu hiện ưu tiên một subject cho beta. Country/legal/academy entities là khung mở rộng, không tức là đã triển khai.

`ENTITY_REGISTRY.json` là nguồn field-level để thiết kế ERD tiếp. Những dấu vết nhạy cảm không đưa vào public schema fixtures. Thông số kết nối và tên provider nằm trong quyết định Q15, không có giá trị giả trong gói.

## Bổ sung 2026-10-20

Audit schema gốc xác nhận các khoảng trống: `tenant.country_pack_id` khác type với `country_pack.id`; method release chưa có ba trục computation/evidence/release; report multi-subject thiếu junction; payment event thiếu merchant account trong unique key; chưa có durable job/lease/DLQ; JSON result chưa khóa decimal/null/timezone và dependency. `SCHEMA_DELTA_REFERENCE_2026_10_20.sql` mô tả expand-side target để đội migration tách thành các migration nhỏ sau khi có provider/version/data receipt. File delta không tạo RLS allow policy và không được chạy trực tiếp.
