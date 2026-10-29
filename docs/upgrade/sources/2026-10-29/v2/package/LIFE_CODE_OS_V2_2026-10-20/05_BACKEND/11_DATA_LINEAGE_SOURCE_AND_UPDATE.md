# Nguồn, phụ thuộc kết quả và cập nhật không làm mất lịch sử

**Life Code OS · V2 · 20/10/2026**  
**Phạm vi:** Đặc tả triển khai; mã demo chỉ là tham chiếu cục bộ, chưa phải production.

## 1. Mỗi kết quả có đường đi ngược
Lineage bắt đầu ở source_assertion hoặc self-report, đi qua profile_version, input manifest, method release, method result, claim, report section và artifact. Mọi cạnh phải có loại quan hệ: used_input, derived_from, interpreted_by, supports, rendered_as hoặc supersedes. Không dùng một chuỗi văn bản “nguồn: HNH” thay cho chuỗi này.

Người dùng có thể đọc một lời giải ngắn; chuyên gia được xem phần nguồn được cấp quyền; người vận hành xem metadata tối thiểu. Một liên kết nguồn không tự cấp quyền đọc dữ liệu gốc của người khác.

## 2. Nguồn không chỉ là URL
source_edition cần tác phẩm, tác giả/đơn vị, phiên bản, ngôn ngữ, vị trí trang/mục, ngày truy xuất, quyền sử dụng và người rà soát. Chỉ mục đa ngôn ngữ giữ thuật ngữ gốc và bản dịch được duyệt. Nếu chỉ có mục lục hoặc bài quảng bá, read_status không được đổi thành full_text_reviewed.

Với bảng số, table artifact có digest và trạng thái. Quy tắc 0→80, cách xử lý số 5 hoặc chính sách Y là cấu hình có ID, không nằm trong câu chữ tùy ý của prompt. Nếu thiếu nguyên văn bảng, nội dung gốc để null; một câu diễn giải mới phải ghi rõ do biên tập HNH, không giả làm lời sách.

## 3. Ảnh hưởng khi dữ liệu hoặc quy tắc đổi
Sửa tên chỉ làm những node sử dụng tên mất hiệu lực. Sửa ngày sinh tác động birth calculation, cycle, timeline và phần report dùng chúng. Sửa giá tiền của SIM không làm đổi modulo80. Sửa lời chú giải nhưng không đổi bảng phân loại chỉ cần dựng lại narrative liên quan, không tính lại mọi node.

Bộ impact analysis đi trên đồ thị phụ thuộc và xuất affected/unaffected, lý do, chi phí dự kiến và mức cần phê duyệt. Không chạy lại hàng loạt trên dữ liệu thật khi chưa có quyền và ngân sách. Danh sách affected là đề xuất công việc, không phải phép tự truy cập.

## 4. Thiết kế bộ nhớ đệm
Khóa cache gồm namespace, tenant_id khi dữ liệu riêng, subject_id, processing_purpose, access_revision, profile_version_id, method_release_id, input digest và cấu hình. Không dùng duy nhất ngày sinh làm khóa cache. Phần dữ liệu nhạy cảm có entropy thấp không được công khai qua hash dễ dò; HMAC và quản lý khóa là thiết kế production cần review riêng.

Cache hit vẫn phải kiểm tra quyền và trạng thái thu hồi. TTL không thay deletion workflow. Một tệp bị gỡ khỏi DB nhưng vẫn có public URL hoặc nằm trong vector index là dữ liệu chưa được xóa đầy đủ.

## 5. Đọc nhiều giả thuyết mà không ép chọn
Ngày sinh giấy tờ và ngày sinh thực tế được lưu thành các giả thuyết riêng có nguồn. Hệ tính từng nhánh và hiển thị phần khác nhau. Không lấy trung bình ngày sinh, không chọn phương án có lời luận đẹp và không dùng nhận xét “đúng hơn” để ghi đè dữ liệu gốc.

Mỗi so sánh nêu method version, trường thay đổi, kết quả thay đổi và phần bất biến. Quyết định chọn giả thuyết phải được ghi bởi người có quyền với lý do. Khi chưa chọn, các kết quả phụ thuộc hiển thị chưa chốt; những phần độc lập vẫn hoạt động.

## 6. Quản trị thu hồi nguồn
Nếu license hết hiệu lực hoặc method bị phát hiện sai, registry chuyển trạng thái phù hợp và chặn run mới. Review board xác định có cần rút báo cáo, bổ sung thông báo hay chỉ chặn phát hành tương lai. Snapshot lịch sử được giữ theo chính sách pháp lý và quyền dữ liệu; không tiếp tục sử dụng như kết quả còn hiệu lực.

Báo cáo đã tải ra ngoài không thể bị thu hồi vật lý bởi phần mềm. Hệ phải nói rõ giới hạn đó và cung cấp phiên bản hiệu chỉnh. Chỉ đổi số version ở footer không đủ nếu nội dung đã gây hiểu sai.
