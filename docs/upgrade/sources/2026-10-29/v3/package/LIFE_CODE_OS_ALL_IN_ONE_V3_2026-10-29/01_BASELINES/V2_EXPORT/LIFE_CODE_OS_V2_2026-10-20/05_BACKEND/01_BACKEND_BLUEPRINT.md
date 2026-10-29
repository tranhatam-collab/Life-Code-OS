# Backend V2: ranh giới mô-đun, đường dữ liệu và bảo đảm tính đúng

**Life Code OS · Bản nâng cấp bảo toàn V2 · 20/10/2026**  
**Trạng thái:** Đặc tả để triển khai và rà soát; không phải chứng nhận production.

## 1. Từ yêu cầu tới báo cáo
Gateway xác thực → resolve subject và grant → kiểm tra purpose/entitlement → khóa profile version → chọn method releases → validate inputs → lập DAG → chạy công cụ → kiểm tra kết quả → tạo claims → tổng hợp → viết nội dung → review → phát hành snapshot. Mỗi bước ghi state transition và trace ID nhưng không ghi nguyên payload nhạy cảm vào log.

Modular monolith được chia miền identity, profiles, knowledge, methods, observations, synthesis, reports, commerce, practice và operations. Mỗi miền có service boundary và data ownership. Không có domain nào được trực tiếp bỏ qua authorization bằng cách truy vấn bảng của domain khác. API layer không chứa công thức; renderer không tính lại.

## 2. Hai API khác nhau phải được ghi đúng
`06_DEMO_LAB` chỉ có local HTTP API không xác thực, bind loopback và dùng dữ liệu tổng hợp. `openapi.target.v2.json` là hợp đồng sản phẩm đích với cookie/session và quyền, chưa được triển khai. Demo không nhận cookie production, không dùng database và không được deploy như API công khai. Mọi tệp và màn hình ghi `REFERENCE_ONLY` để tránh nhập nhằng.

## 3. Khóa phiên bản đầu vào
Run dùng profile_version_id, hypothesis_selection, product_release_id, method_release_ids, purpose_id, access_revision và input_digest. Dữ liệu không được lấy lại từ profile live giữa lúc run đang xử lý. Một người sửa ngày sinh trong khi đang render không làm bản đang dựng đổi một nửa; tạo run mới với snapshot mới.

## 4. Tính đồng bộ và bất đồng bộ
Phép số nguyên ngắn có thể trả đồng bộ. Pipeline nhiều phương pháp hoặc export trả 202 cùng run_id, state và polling/SSE endpoint. Worker xử lý công việc phải kiểm tra lại grant, purpose, quyền phương pháp và trạng thái deletion trước khi đọc input và trước khi publish. Việc queue đã nhận không là bảo đảm được quyền hoàn tất.

## 5. Thiết kế lỗi
Lỗi dùng Problem Details với code ổn định, trace ID và thông báo tiếng Việt dễ hiểu. Phân biệt validation, thiếu phương pháp, thiếu đầu vào, conflict, rate limit và lỗi hạ tầng. Không trả stack trace hoặc câu SQL. Retry chỉ cho lỗi tạm thời, không retry lỗi quyền, dữ liệu hoặc phương pháp chưa phát hành. [N05]

## 6. Tái lập kết quả
Cùng input đã chuẩn hóa, cấu hình, bảng nguồn và dependency version phải trả cùng calculation. Ngày hiện tại phải truyền như tham số as_of chứ không ẩn trong engine. Random chỉ được dùng nếu một phương pháp quy định sự gieo ngẫu nhiên, và phải lưu phương thức cùng dữ kiện tương ứng; tuyệt đối không dùng random để tạo năm rủi ro.

Hash cần bind vào cả input, method version, table/source digest và cấu hình. Dữ liệu cá nhân entropy thấp không được công khai bằng hash trần vì có thể đoán lại; production cần HMAC tenant-scoped hoặc cơ chế tương đương do security duyệt. Demo dùng SHA-256 để tái lập, không gọi đó là ẩn danh hóa. [N06]

**Tra nguồn:** xem `11_SOURCES/SOURCE_ADDENDUM.csv`; các mã Nxx là nguồn đối chiếu chính thức, không phải mọi nhận định của HNH đã được khoa học xác nhận.
