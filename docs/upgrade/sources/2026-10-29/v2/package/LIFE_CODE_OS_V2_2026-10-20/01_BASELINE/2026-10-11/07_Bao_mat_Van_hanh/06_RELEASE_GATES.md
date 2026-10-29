# Mười hai cổng phát hành và yêu cầu bằng chứng

Mã tài liệu: **D34** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Release Authority + QA + Security. Nguồn đối chiếu: S07, S13, S21. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Nguyên tắc
Không kế thừa tỷ lệ3/12 hoặc25% từ audit cũ sang bộ cổng mới. Tất cả gates trong register kèm theo là NOT_CHECKED ở production trong gói này; source evidence có bảng riêng. Không bù lỗi quyền bằng điểm giao diện đẹp. Gate scope được chốt trước, không đánh N/A cho điều cốt lõi chỉ để tăng tỷ lệ.
## 2. Danh sách cổng
G01 Source/Release: source–artifact–runtime–schema liên kết, rollback an toàn. G02 Authentication: xác thực chuẩn, legacy revoked, recovery hợp lệ. G03 Authorization: object/tenant/field/grant kiểm tra và negative tests. G04 Legal/Purpose: phạm vi dịch vụ, mục đích, pháp nhân, notices và country. G05 Retention/Deletion: xóa xuyên hệ và restore không tái sinh dữ liệu. G06 Methods/Claims: passport, rights, rules, null và giới hạn. G07 Legacy/Migration: phân loại quyền và output, đối soát chuyển. G08 Reports/AI: lineage, ngôn ngữ, file và injection tests. G09 Commerce: chữ ký/replay/refund/entitlement. G10 Reliability: tải, retries, backup/restore. G11 Security Review: đánh giá độc lập và retest. G12 Operations/Pilot: support, công suất, incident và phê duyệt scope.
## 3. Bằng chứng mỗi gate
Có người chủ trì, câu hỏi nghiệm thu, môi trường, exact SHA, test run, thời gian, kết quả, người review, ngoại lệ và quyết định. Bằng chứng có PII nằm private, repo chỉ giữ pointer/hash. Link ảnh chụp màn hình không thay toàn bộ test; CI green không thay method review.
## 4. Mở các mức dịch vụ
Containment exit: bề mặt rủi ro đã khóa, không còn output cá nhân giả, tokens cũ vô hiệu, biết deploy và owner incident. Public guest deterministic: thêm bundle privacy, rules tests và copy review. Private alpha: G01–G08 và phần cần thiết G10–G12 theo scope; commerce N/A chỉ nếu thực sự không thu tiền. Paid beta: cả12 gates áp dụng phải pass. Sensitive/children/international: bổ sung cổng riêng, không tự thừa hưởng paid-beta approval.
## 5. Rollback và exception
Exception chỉ dùng cho rủi ro có thể chấp nhận với thời hạn và compensating control; không cho phép bypass quyền chủ thể, giả dữ kiện hoặc tuyên bố sai. Khi không có bản rollback an toàn, chuyển chế độ maintenance/static. Chỉ người được giao quyền mới mở lại. Báo cáo có withdrawn status nếu ảnh hưởng nội dung sau phát hành; người dùng nhận giải thích và quyền xử lý phù hợp.
