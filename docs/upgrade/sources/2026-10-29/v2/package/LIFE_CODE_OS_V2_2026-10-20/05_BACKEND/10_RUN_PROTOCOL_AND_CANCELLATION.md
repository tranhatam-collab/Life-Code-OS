# Giao thức một lần phân tích: từ yêu cầu tới phát hành

**Life Code OS · V2 · 20/10/2026**  
**Phạm vi:** Đặc tả triển khai; mã demo chỉ là tham chiếu cục bộ, chưa phải production.

## 1. Giao dịch nhận yêu cầu
POST analysis-runs không nhận điểm hoặc kết luận từ client. Client gửi subject_id, profile_version_id, hypothesis_ids, product_release_id, selected_method_release_ids và khóa idempotency. Server lấy account từ phiên đã xác thực, kiểm tra grant, purpose, điều kiện sản phẩm và phiên bản hồ sơ. product_release là danh mục do server quản lý; client không được thay danh sách dữ liệu bắt buộc để nâng coverage.

Giới hạn body, số phương pháp, độ dài chuỗi và khoảng thời gian phải được kiểm tra trước khi lập kế hoạch. Nếu hồ sơ thiếu dữ liệu bắt buộc, trả kết quả needs_input có tên trường và lý do; dữ liệu tùy chọn thiếu không biến thành lỗi toàn bộ. Một yêu cầu thay đổi mục đích xử lý không được tái sử dụng sự đồng ý dành cho mục đích cũ.

Trong một transaction: tạo analysis_run ở trạng thái queued; lưu manifest đầu vào bất biến; tạo idempotency receipt; tạo outbox event. Unique constraint trên tenant_id, operation_name và idempotency_key ngăn hai request đồng thời tạo hai nghiệp vụ. Nếu khóa trùng và payload_digest giống nhau, trả receipt của lần trước. Nếu payload khác, trả 409 và không thực hiện phần mới.

## 2. Lập đồ thị phụ thuộc
Mỗi node gồm node_id, method_release_id, input_paths, dependencies, output_schema, cost_budget và timeout_budget. Đồ thị phải được kiểm tra node trùng, phụ thuộc thiếu và chu trình trước khi chạy. Các node độc lập có thể chạy cùng đợt trong giới hạn concurrency; node phụ thuộc chỉ bắt đầu khi đầu ra cần dùng đã hoàn tất và hợp lệ.

Ví dụ: chuẩn hóa tên và chuẩn hóa ngày chạy độc lập. Chu kỳ số phụ thuộc ngày; bản đồ tuổi phụ thuộc ngày và as_of; báo cáo phụ thuộc các kết quả đã được phép dùng. Nếu giờ sinh chưa rõ, node dùng giờ bị chặn, nhưng phép quy đổi tên không bị mất theo. Node thất bại không được thay bằng hằng số đẹp.

## 3. Worker nhận và xử lý
Worker claim job với lease có thời hạn; kiểm tra lại trạng thái chủ thể, grant revision và deletion barrier. Việc một request hợp lệ lúc tạo không bảo đảm nó còn hợp lệ sau khi chờ hàng đợi. Worker chỉ lấy đúng snapshot được ghi trong run, không đọc hồ sơ mới nhất rồi tạo một báo cáo nửa cũ nửa mới.

Mỗi node ghi started_at, finished_at, implementation_version, source_digest, input_digest, output_digest, trạng thái và mã lỗi. Dữ liệu nhạy cảm không được đưa thẳng vào log. Công cụ không có nguồn hoặc chưa phát hành trả METHOD_NOT_RELEASED. Lỗi tạm thời có thể retry theo ngân sách; lỗi dữ liệu, quyền hoặc phương pháp không retry tự động.

## 4. Hủy, thu hồi và hết hạn
Cancel từ người có quyền chuyển run sang cancel_requested. Worker kiểm tra giữa các bước và dừng tại điểm an toàn. Cancel không được tuyên bố đã hoàn tất khi tác vụ bên ngoài còn chạy; trạng thái phải chỉ rõ cleanup_pending nếu cần thu hồi artifact. Khi quyền bị thu hồi, kết quả chưa phát hành không được cấp link tải.

Một run hoàn thành tính toán vẫn có thể chuyển review_required. approve là nghiệp vụ riêng: người duyệt, phạm vi, phiên bản và lý do. Nếu dữ liệu nguồn thay đổi trước phát hành, bản nháp được ghi stale hoặc yêu cầu chạy lại, không âm thầm thay nội dung.

## 5. Phát hành và truy vết
Tạo report_snapshot từ danh sách claim cụ thể. Phát hành phải kiểm tra lại scope, policy revision và quyền phương pháp. Renderer chỉ nhận content tree đã chốt; không tự gọi thêm AI hoặc tính lại công thức. Artifact được ghi hash, MIME, dung lượng, phiên bản renderer và trạng thái riêng tư.

Khi download, kiểm tra quyền của account với chính report. Khóa đoán khó không thay authorization. Chủ sở hữu có thể xem lịch sử phiên bản, lý do hiệu chỉnh và phần nào không còn phù hợp; hệ không ghi đè PDF cũ rồi tiếp tục dùng cùng ID như chưa có thay đổi.

## 6. Bằng chứng nghiệm thu
Đội QA cần chạy tối thiểu: gửi request trùng đồng thời; đổi body trên cùng khóa; hủy khi đang render; thu hồi grant lúc đang chờ; sửa ngày sinh khi node đang chạy; worker chết sau tạo artifact; node con chạy sai thứ tự; phương pháp bị freeze trước publish. Mỗi ca cần kết quả kỳ vọng, trạng thái cuối và bằng chứng không có thêm side effect.

Demo DAG, cache key, policy và ledger trong gói chỉ mô phỏng các phần logic trên một process. Bằng chứng transaction, lease và concurrency nhiều worker phải được tạo bằng PostgreSQL và queue staging thật. [N02, N03, N05]
