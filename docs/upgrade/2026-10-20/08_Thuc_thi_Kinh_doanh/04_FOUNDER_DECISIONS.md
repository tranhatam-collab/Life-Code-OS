# Quyết định Q1–Q20: nền cũ và phạm vi mở rộng

Mã tài liệu: **D35** | Phiên bản: **2026-10-11.r1** | Trạng thái: **ĐỀ XUẤT BÀN GIAO / CHỜ PHÊ DUYỆT**

Chủ trì dự kiến: Founder + Functional Approvers. Nguồn đối chiếu: G02. Tra mã nguồn tại `09_Doi_chieu_Bang_chung/SOURCE_REGISTRY.csv`.

## 1. Tình trạng phê duyệt
Người dùng đã yêu cầu xuất kế hoạch. Điều đó xác nhận quyền tạo bộ tài liệu này, không tự phê duyệt mọi Q hoặc cho phép deploy. Tất cả Q trong DECISION_REGISTER bắt đầu PENDING_FOUNDER. Quyết định liên quan security/privacy còn cần người phụ trách chức năng ký theo phạm vi.
## 2. Q1–Q12 giữ tương thích kế hoạch audit
Q1 định vị tự hiểu/life design. Q2 giữ9levels/12layers/4reportblocks/12fields/K01–20. Q3 method riêng theo source/version. Q4 entitlement khác eligibility/data. Q5 dừng score giả, cho null. Q6 Numbers là reference không đo số phận. Q7 content model chung, không filler. Q8 mở dòng sản phẩm theo gates. Q9 privacy/auth/delete từ đầu. Q10 xuất tám bộ nền từ baseline đã khóa. Q11 quarantine experimental_legacy. Q12 không release method thiếu passport/rights/tests/limits/approver.
## 3. Q13–Q20 cho phạm vi mới
Q13 Free Essentials: một hồ sơ tự quản, mục tiêu, nhật ký và privacy rights; quota AI/chi phí proposal. Q14 pháp nhân/merchant/controller và mô hình trách nhiệm. Q15 chọn IdP, PostgreSQL host, payment và AI providers qua ADR/vendor assessment. Q16 mức tự chủ A0–A3 và quyền dừng. Q17 Academy/practitioner certification scope và review. Q18 organization privacy boundaries, không high-impact profiling. Q19 country-pack order và mô hình license/franchise. Q20 ngân sách, đội lõi, nghiệm thu và lịch có điều kiện.
## 4. Cách duyệt
Mỗi Q trả APPROVE, APPROVE_WITH_CONDITIONS, REVISE hoặc REJECT; ghi điều kiện, phạm vi, ngày và approver. Câu “đồng ý tiếp tục” chỉ áp dụng cho hành động được nói rõ. Nếu chưa chọn provider, dùng adapter contract và decision TBD thay vì giả vờ đã ký hợp đồng. Không đặt placeholder bí mật trong file để user có thể lỡ chia sẻ credentials.
## 5. Quyết định không thể thay bằng marketing
Không chữ ký nào biến hình thái thành phép đo đạo đức hoặc số học thành bằng chứng bệnh tật. Founder có thể chọn ngôn ngữ biểu tượng và triết lý HNH nhưng sản phẩm vẫn phải gắn đúng loại nhận định. Nội dung thương hiệu công khai cần biên tập trước khi phát hành và kiểm tra trên các locale đã mở.

## Bổ sung thực thi 2026-10-20
Các artifact 2026-10-20 chỉ liên kết dependency Q1–Q20 và không đổi trạng thái `PENDING_FOUNDER`. `DECISION_EXECUTION_PACKETS.json` và `.csv` cung cấp ba phương án loại trừ nhau, phương án khuyến nghị cùng trade-off, dependency, task ảnh hưởng, trạng thái chi phí, vai trò duyệt, sự kiện phải quyết định và hợp đồng receipt cho từng Q. Đây là packet để review, không phải lựa chọn đã được duyệt. Mỗi quyết định vẫn cần baseline, phạm vi, điều kiện, approver thật và thời gian; không suy approval từ việc Founder yêu cầu hoàn thiện kế hoạch.
