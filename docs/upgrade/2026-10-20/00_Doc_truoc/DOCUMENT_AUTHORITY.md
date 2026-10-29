# Life Code OS Thứ tự áp dụng tài liệu

Ngày 20/10/2026. Phạm vi thay đổi là bộ kế hoạch chuẩn bị dev, schema thiết kế, registry, demo và tài liệu bàn giao. Không xác nhận trạng thái production hoặc tự sửa một Founder decision.

## Thứ tự và hiệu lực

1. Yêu cầu trực tiếp mới nhất của Founder cùng AGENTS và bốn FPOS authority hiện hành quyết định phạm vi làm việc.
2. Decision có người duyệt, thời gian, phạm vi và artifact cụ thể quyết định sản phẩm/nhà cung cấp/giá/phương pháp. Không dùng một câu đồng ý chung thay nhiều quyết định chưa chốt.
3. Bộ `docs/upgrade/2026-10-20` là bản đề xuất hợp nhất hiện tại để review và chuẩn bị dev. Phần bổ sung đề ngày 20/10 điều chỉnh các phát biểu của bản 11/10 trong đúng phạm vi được chỉ ra. Quyền triển khai sản phẩm thực tế vẫn phải khớp quyết định và task được giao.
4. `docs/audit/LIFE_CODE_OS_COMPREHENSIVE_UPGRADE_PLAN_2026-10-11.md` và 149 tệp gốc nằm trong sources là tài liệu nguồn được bảo toàn. Chúng giải thích lịch sử thiết kế; không được dùng nhãn cũ hoặc phần trăm cũ để đóng gate mới.
5. README, PROJECT_STATUS_MASTER và PRE_CODE_LOCK_CHECKLIST trước 20/10 có những tuyên bố khóa thiết kế/hoàn thành chưa có receipt hiện hành. Các tuyên bố đó cần revalidation. Phần thuật ngữ, quy tắc và tầm nhìn hữu ích vẫn được ánh xạ; không xóa lịch sử.
6. Handover bilingual tại local phase HEAD 4df9b6e là lane riêng. Giữ VI/EN, URL và nội dung có quyền; không tự coi các báo cáo Founder lock trong lane đó là quyết định cho kiến trúc mới. Phase branch không có upstream và 29 thay đổi local được giữ nguyên ngoài checkout này.

## Điều chỉnh có phạm vi

- Bộ gate G01–G12 giữ ID để không làm hỏng trace; bổ sung ánh xạ RG0–RG13 trong `07_Bao_mat_Van_hanh/FPOS_GATE_MAPPING.json`.
- Claim chỉ dùng VERIFIED_CURRENT, VERIFIED_HEAD_ONLY, VERIFIED_WORKTREE_ONLY, REPORTED_UNVERIFIED, CONTRADICTED, NOT_CHECKED, BLOCKED, NOT_APPLICABLE. Nhãn cũ được giữ trong `original_status` khi cần truy vết; không nâng thành verified nếu chưa kiểm tra lại.
- Release verdict dùng GO, CONDITIONAL_GO, HOLD, NO_GO. BLOCKED mô tả gate/evidence; không thay release verdict.
- Task status, method lifecycle, review decision và evidence status là các trường khác nhau. NOT_STARTED và PENDING_FOUNDER được dùng đúng miền, không dùng để thay evidence.
- Các ước lượng ngày công và mốc tháng là proposal. Không quy đổi tổng tài liệu hoặc test reference thành phần trăm hoàn thành sản phẩm.

## Giải quyết mâu thuẫn

Người nhận việc ghi conflict ID, hai nguồn, impact, đề xuất và functional approver. Nếu ảnh hưởng dữ liệu/công thức/quyền/API dùng chung, giữ tính năng đó đóng cho tới quyết định; không chọn tài liệu dễ thực hiện hơn. Khi chốt phải cập nhật registry, schema, test, demo, màn hình, báo cáo và source mapping bị ảnh hưởng trong cùng change set. Hash source gốc không đổi.
