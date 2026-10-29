# Công cụ tái tạo bộ kế hoạch ngày 20 tháng 10 năm 2026

Các script này chỉ ghi artifact local trong repository, không deploy, migrate, gọi AI trả phí hoặc truy cập dữ liệu thật. Đọc script và xác nhận đúng branch trước chạy. Không chạy lại ingest hoặc governance generator để ghi đè một bản đã được chỉnh thủ công.

## Kiểm tra không cần tài khoản ngoài

Từ `docs/upgrade/2026-10-20`, chạy `python3 VERIFY_PACKAGE.py` để đối chiếu toàn bộ tệp với manifest. Manifest không tự băm chính nó; digest ZIP ngoài gói nằm trong `docs/upgrade/deliverables/DELIVERY_RECEIPT.json`.

Trong `10_Ma_tham_chieu_Kiem_thu`, chạy `npm test`; package chỉ dùng Node built-ins, không cần npm install. Chạy resolver với `--check` theo README backend sau khi cài dependency YAML trong virtualenv riêng. Đây không phải kiểm thử ứng dụng production.

## Tái tạo trong checkout repo này

1. Cài `requirements-validation.txt` vào virtualenv riêng. Không cài vào Python hệ thống. `validate_upgrade_package.py` kiểm tra source preservation, schema/example, registries, CSV parity, dependency DAG, task/decision joins và FPOS; nó ghi `PACKAGE_QA.json`.
2. `build_master_document.py` dùng python-docx để hợp nhất 38 chuyên đề và amendment. Dùng `render_docx.py` của Documents skill để render lại Word/PDF và kiểm tra từng trang trước cập nhật export receipt. Các artifact không được gọi là visually reviewed nếu chưa xem ảnh render thực tế.
3. `build_package_indices.py` tạo coverage, transformations, catalog và portal HTML nhúng nội dung để mở ngoại tuyến. Chạy sau khi nội dung cuối đã ổn định.
4. `build_execution_board.mjs` cần `@oai/artifact-tool` từ bundled runtime đã xác định trong workspace. Script nhập workbook gốc, giữ 11 tab và thêm 3 tab, kiểm tra công thức rồi xuất bản mới. Đường dẫn render QA nằm trong `/private/tmp`; đó không phải nguồn canonical.
5. Sau kiểm tra PDF, Excel, browser và test, cập nhật receipt đúng những gì đã chạy. Rerun indices và validator nếu có thêm tệp. `pack_upgrade_bundle.py` tạo manifest, chạy integrity verifier, đóng ZIP và kiểm tra CRC cùng hash từng entry.

`ingest_upgrade_package.py`, `inspect_source_exports.py`, `preserve_legacy_handover.py` và `upgrade_governance.py` là công cụ của bước tiếp nhận ban đầu. Chúng không thay quyết định thủ công, quyền nguồn hoặc Founder sign-off. Bản portable mang theo script để kiểm tra lịch sử; các builder tổng hợp giả định layout repository này, không phải một ứng dụng tự cài đặt.
