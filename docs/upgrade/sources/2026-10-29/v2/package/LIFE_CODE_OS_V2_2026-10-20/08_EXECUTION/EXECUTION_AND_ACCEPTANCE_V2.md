# Chuẩn bị chạy dự án: thứ tự thực thi và nghiệm thu

**Life Code OS · Bản nâng cấp bảo toàn V2 · 20/10/2026**  
**Trạng thái:** Đặc tả để triển khai và rà soát; không phải chứng nhận production.

## 1. T0 có điều kiện
T0 là ngày có chủ trì, repo/branch, quyền môi trường, budget và phạm vi đã duyệt. Các ước lượng 4–6 tháng paid beta và 12–18+ tháng tầm nhìn vẫn là kế hoạch có giả định, không ngày hứa cố định. V2 thêm việc backend/demo nhưng không tự tăng mức hoàn thành production.

## 2. Công việc giữ và bổ sung
140 công việc cũ giữ nguyên ID, trạng thái và estimate. `BACKLOG_V2_ADDITIONS.json` chứa việc bổ sung và task cha liên quan; các estimate addition là mức chi tiết tham chiếu, không được cộng chồng toàn bộ với estimate task cha. Khi planning, Tech Lead chọn roll-up hoặc replacement theo decision, không tính hai lần. Mỗi task có input, output, acceptance, test, reviewer và evidence path.

## 3. Các wave
Đợt 0: P0 containment/source receipt, quyền sở hữu và dữ liệu legacy. Đợt 1: contract/schema, time/name/number core, source registry, auth/purpose foundation. Đợt 2: Level 1 pipeline, journal, plan, report factory, frontendcore. Đợt 3: paid beta, payment, entitlement, support, restore. Đợt 4: Level 2–5, resonance/practice. Đợt 5: timeline đầy đủ, academy, organization, API đối tác, native khi đủ lý do. Country/children/health là gate riêng, không theo lịch tự động.

## 4. Nghiệm thu một task
Một task code phải có input/output schema, test đúng/sai/thiếu, quyền, lỗi, log đúng, tài liệu, rollback khi cần. Một task nội dung phải có source, edition, rights, claim type, review và examples. Tạo file không tự là completed. `REFERENCE_TESTED` trong gói V2 không đóng `PRODUCTION_NOT_STARTED` của task triển khai.

## 5. Báo cáo Founder
Bảng theo ngày gồm việc đã hoàn tất có receipt; việc đang làm; blocked; thay đổi scope; quyết định cần chốt. Báo cáo hàng giờ nếu dùng nên tự lấy commit/test/job và nhóm đang hoạt động, không buộc người viết lại. Chưa có automation định kỳ nào được tạo bởi gói này.

## 6. Đóng băng và quay lui
Không thay schema shared khi chưa báo integration owner. Feature flag tắt được theo module/tenant/country. Nếu không có bản an toàn, quay về static/maintenance thay vì mở lại legacy có lỗ hổng. Rollback dữ liệu khác rollback code; migration expand-contract cần kế hoạch riêng. Có diễn tập mới được nói khả năng khôi phục đã chứng minh.
