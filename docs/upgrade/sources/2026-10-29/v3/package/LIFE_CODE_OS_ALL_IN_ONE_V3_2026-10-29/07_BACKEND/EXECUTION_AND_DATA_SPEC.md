# 13. Backend và các ranh giới nghiệp vụ

Giữ kiến trúc khối ứng dụng mô-đun như kế hoạch cũ. Website công khai, ứng dụng và cổng chuyên gia gọi cùng API gateway/BFF. Lõi phương pháp là package độc lập. PostgreSQL quản lý nghiệp vụ; R2 lưu tệp riêng tư; hàng đợi và transactional outbox xử lý công việc dài. Tiến trình xuất sách chạy trong môi trường hạn chế mạng và hệ thống tệp. [R03, R18, R19]

Các miền nghiệp vụ gồm danh tính, quyền chủ thể, mục đích và sự đồng ý, hồ sơ có phiên bản, kho tri thức, thực thi phương pháp, quan sát, đồng nhịp, nhận định, báo cáo, kế hoạch, thương mại, chuyên gia, học viện và lãnh thổ. Không chia một dịch vụ nhỏ cho mỗi môn. Chỉ tách tiến trình khi tải, quyền hoặc vòng đời vận hành cần khác nhau.

Gateway lấy principal từ phiên xác thực. Dữ liệu user_id do trình duyệt gửi không được tạo quyền. Mỗi analysis run chốt phiên bản hồ sơ, giả thuyết ngày sinh, phương pháp, bảng nguồn, cấu hình, mục đích, phiên bản quyền và ngôn ngữ. Kiểm tra quyền diễn ra khi tạo tác vụ, khi worker nhận việc, trước khi phát hành và khi tải kết quả. Tác vụ đang chờ không được tiếp tục công bố sau khi chủ thể rút quyền.

V3 giữ 83 thao tác API V2, bổ sung 16 thao tác đích, tổng cộng 99. Đây là hợp đồng thiết kế. Demo cục bộ chỉ có ba route nghiệp vụ: health, catalog và run; các tệp giao diện là tài nguyên tĩnh. Không lấy số lượng endpoint trong đặc tả làm số lượng chức năng production đã triển khai.

RLS là lớp phòng vệ bổ sung. Tài khoản ứng dụng không là chủ bảng hoặc có quyền BYPASSRLS. Khóa ngoại cho dữ liệu riêng tư cần gắn tenant và subject để ngăn bản ghi con tham chiếu sang chủ thể khác. Mọi chính sách phải được thử bằng tài khoản thực trong staging, không chỉ đọc SQL hoặc nhìn sơ đồ. [R19, R24]

Đường đọc dữ liệu cần giới hạn theo quyền ngay trong truy vấn. Đường ghi dùng schema đóng, chống mass assignment, kiểm tra phiên bản hồ sơ và nhật ký thay đổi. Những tác vụ sửa quyền, xuất dữ liệu, xóa hoặc cấp entitlement phải có audit event không chứa bí mật truy cập.


# 14. Dữ liệu, công thức và ma trận phụ thuộc

Trục dữ liệu giữ các thực thể account, profile_subject, access_grant, consent, processing_purpose, profile_version, data_hypothesis, method_release, source_edition, observation, analysis_run, method_result, claim, report_snapshot, action_plan, order, entitlement, practitioner_case, audit_event và deletion_job. V3 bổ sung số–tên có phiên bản, comparison run, phân đoạn chuỗi số, xung đột nguồn, lĩnh vực đời sống và chuyển giao tri thức.

Mỗi công thức khai báo đầu vào, cách chuẩn hóa, bảng hằng số, phiên bản, độ chính xác, cách xử lý dữ liệu thiếu, đầu ra và kiểm thử. Không cho người biên tập nhập JavaScript tùy ý vào bảng quy tắc production. Điều văn, tài liệu truy xuất và prompt là dữ liệu; công cụ không thực thi chúng như mã hoặc như lệnh đổi quyền.

Đồ thị phụ thuộc — DAG — phải phát hiện nút trùng, thiếu phụ thuộc và vòng lặp trước khi chạy. Các nút độc lập có thể chạy song song với giới hạn tài nguyên. Khi thay bảng tên, các chỉ số tên và nội dung phụ thuộc được đánh dấu cần tính lại; lịch sử do người dùng cung cấp không bị sửa. Khi đổi giả thuyết ngày sinh, chỉ những nút phụ thuộc ngày sinh được tính lại. Báo cáo đã xuất không âm thầm đổi nội dung mà không có phiên bản mới.

Bộ hợp nhất tránh tính trùng. Life Path, năm cá nhân và ma trận ngày sinh đều dùng cùng DOB nên không được xem là ba nguồn chứng minh riêng. Ba bài viết sao chép một sách cũng không phải ba nguồn độc lập. Mỗi nhận định có đồ thị phụ thuộc và danh sách nguồn, ghi rõ quan hệ kế thừa.

Giá trị cần độ chính xác được biểu diễn bằng số nguyên, phân số hoặc chuỗi thập phân theo hợp đồng. Số dư 80 dùng số nguyên. Tiền dùng đơn vị nhỏ nhất kèm mã tiền tệ, không cộng chéo khi thiếu tỷ giá có nguồn. Thiếu mẫu số thì tỷ lệ là null, không gán 0 để bảng trông đầy đủ.

Chỉ số truyền thống có tên như Rational Thought hay Subconscious Confidence không được tự biến thành điểm đo tư duy hoặc độ tự tin thống kê. Bộ máy trả kết quả quy ước, cách tính và giới hạn; lớp biên tập giải thích ý nghĩa của tên gọi và cho phép người dùng không đồng ý với phần tự suy ngẫm.


# 15. Queue, idempotency, cache và tính lại

Cloudflare Queues có cơ chế giao ít nhất một lần. Cùng một thông điệp có thể được xử lý lại; ứng dụng phải quản lý hiệu ứng nghiệp vụ, không hứa hàng đợi chỉ chạy một lần. [R18]

Tạo run, idempotency receipt và outbox event trong cùng giao dịch cơ sở dữ liệu. Khóa idempotency có phạm vi tài khoản, thao tác và mục đích. Cùng khóa, cùng payload trả lại receipt trước; cùng khóa nhưng khác payload trả lỗi xung đột. Worker cần lease, heartbeat, retry có giới hạn, thời gian chờ tăng dần, hàng đợi lỗi và công cụ rà soát lại. Không giữ một HTTP request để dựng 600 trang trong vòng lặp không có giới hạn.

Cache phải gắn tenant, subject, purpose, access revision, input digest, method release, source digest và locale release. Không tạo cache chung theo ngày sinh rồi trả dữ liệu riêng của người khác. Hash phục vụ tái lập không đồng nghĩa ẩn danh; dữ liệu đầu vào dễ đoán vẫn có thể bị đối chiếu. Nhật ký không ghi tên, ngày sinh, prompt riêng hoặc URL tải nếu không thật sự cần.

Hủy tác vụ là trạng thái có lịch sử. Worker kiểm cờ hủy tại các điểm an toàn. Khi có yêu cầu xóa, deletion barrier chặn tác vụ mới và phát hành mới; khôi phục backup phải áp lại các chỉ thị xóa trước khi mở truy cập. Báo cáo đã tải về không thể thu hồi vật lý từ thiết bị người nhận, vì vậy giao diện không được hứa làm được điều đó.

Giới hạn công việc gồm số phương pháp trong một run, kích thước dữ liệu, số dãy so sánh, thời gian chạy, số lần gọi AI, kích thước tệp xuất và số lần thử lại. Các giới hạn phải trả lỗi đọc hiểu được, không chỉ mã lỗi kỹ thuật.

Hiệu năng được đo theo lớp: phép tính ngắn, tổng hợp hồ sơ, xuất tệp, AI và truy xuất. Benchmark máy cục bộ chỉ mô tả môi trường đó; không được chuyển thành SLA công khai hoặc chứng nhận độ chính xác về cuộc đời.
