# 14. Dữ liệu, công thức và ma trận phụ thuộc

Trục dữ liệu giữ các thực thể account, profile_subject, access_grant, consent, processing_purpose, profile_version, data_hypothesis, method_release, source_edition, observation, analysis_run, method_result, claim, report_snapshot, action_plan, order, entitlement, practitioner_case, audit_event và deletion_job. V3 bổ sung số–tên có phiên bản, comparison run, phân đoạn chuỗi số, xung đột nguồn, lĩnh vực đời sống và chuyển giao tri thức.

Mỗi công thức khai báo đầu vào, cách chuẩn hóa, bảng hằng số, phiên bản, độ chính xác, cách xử lý dữ liệu thiếu, đầu ra và kiểm thử. Không cho người biên tập nhập JavaScript tùy ý vào bảng quy tắc production. Điều văn, tài liệu truy xuất và prompt là dữ liệu; công cụ không thực thi chúng như mã hoặc như lệnh đổi quyền.

Đồ thị phụ thuộc — DAG — phải phát hiện nút trùng, thiếu phụ thuộc và vòng lặp trước khi chạy. Các nút độc lập có thể chạy song song với giới hạn tài nguyên. Khi thay bảng tên, các chỉ số tên và nội dung phụ thuộc được đánh dấu cần tính lại; lịch sử do người dùng cung cấp không bị sửa. Khi đổi giả thuyết ngày sinh, chỉ những nút phụ thuộc ngày sinh được tính lại. Báo cáo đã xuất không âm thầm đổi nội dung mà không có phiên bản mới.

Bộ hợp nhất tránh tính trùng. Life Path, năm cá nhân và ma trận ngày sinh đều dùng cùng DOB nên không được xem là ba nguồn chứng minh riêng. Ba bài viết sao chép một sách cũng không phải ba nguồn độc lập. Mỗi nhận định có đồ thị phụ thuộc và danh sách nguồn, ghi rõ quan hệ kế thừa.

Giá trị cần độ chính xác được biểu diễn bằng số nguyên, phân số hoặc chuỗi thập phân theo hợp đồng. Số dư 80 dùng số nguyên. Tiền dùng đơn vị nhỏ nhất kèm mã tiền tệ, không cộng chéo khi thiếu tỷ giá có nguồn. Thiếu mẫu số thì tỷ lệ là null, không gán 0 để bảng trông đầy đủ.

Chỉ số truyền thống có tên như Rational Thought hay Subconscious Confidence không được tự biến thành điểm đo tư duy hoặc độ tự tin thống kê. Bộ máy trả kết quả quy ước, cách tính và giới hạn; lớp biên tập giải thích ý nghĩa của tên gọi và cho phép người dùng không đồng ý với phần tự suy ngẫm.
