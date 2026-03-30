# Timeline 0–99 algorithm v1 — chia giai đoạn + sinh windows (Level 6 output)

**Nguồn bám sát:**
- `README.md` **Level 6 – Life Timeline** (Input/Engines/Output)
- `README.md` **§21** (pipeline có bước sinh `life_code_data.json` và inject template)
- `timeline-cuoc-doi.html` (UI copy mô tả 9 giai đoạn: 0–9 … 80–99; các cửa quan trọng: Risk/Peak/Transformation/Mission Activation)

---

## 1. Mục tiêu đầu ra (Level 6)

Engine Timeline 0–99 cần sinh các trường (tương ứng output Level 6):
- `timeline 0–99`: danh sách năm 0..99 với stage/nhãn giai đoạn
- `9 giai đoạn đời`: tổng hợp 9 bucket tuổi 0–9, 10–19, …, 80–99
- `high-risk years`: danh sách năm (hoặc khoảng) có rủi ro cao
- `high-opportunity years`: danh sách năm (hoặc khoảng) có cơ hội cao
- `transformation years`: danh sách năm (hoặc khoảng) buộc phải đổi
- `mission activation years`: danh sách năm (hoặc khoảng) có tín hiệu nhiệm vụ
- `current 12-month forecast`: dự báo 12 tháng tới
- `3-year strategy`, `10-year direction`

---

## 2. Input (tối thiểu)

- dữ liệu Level 1–5
- `life events history`
- `timeline calibration` (có thể là một offset/calibration từ user hoặc admin)
- Các layer kết quả liên quan để tính xác suất/rủi ro/cơ hội (từ engine pipeline)

---

## 3. Bước 1 — Chuẩn hoá trục tuổi 0–99

1. Xác định `age_year` (0..99) theo user (hoặc theo timeline calibration).
2. Tạo 9 bucket tuổi theo đúng UI/README:
   - bucket1: 0–9
   - bucket2: 10–19
   - bucket3: 20–29
   - bucket4: 30–39
   - bucket5: 40–49
   - bucket6: 50–59
   - bucket7: 60–69
   - bucket8: 70–79
   - bucket9: 80–99

Output trung gian:
- `stage_by_year[0..99] = stage_id`
- `stage_summary[1..9]` (tên bucket + mô tả)

---

## 4. Bước 2 — Sinh tín hiệu theo năm (nhẹ, xác suất)

Với mỗi năm `y` từ 0..99:
1. Lấy `stage_id = stage_by_year[y]`
2. Tính các điểm xác suất (không phải mệnh lệnh):
   - `risk_signal(y)` (dùng Risk Window Engine + Event Probability Engine)
   - `peak_signal(y)` (dùng Peak Window Engine)
   - `transformation_signal(y)` (dùng Transformation Window Engine)
   - `mission_signal(y)` (dùng Mission Activation Engine)

Lưu ý ethics:
- Không biến các tín hiệu này thành “định mệnh”.
- Khi thiếu dữ liệu: tín hiệu = null, confidence = 0 và windows rỗng (tham chiếu README §19).

---

## 5. Bước 3 — Trích windows theo ngưỡng (v1)

Khái niệm windows:
- **Risk windows**: các cụm năm có `risk_signal` vượt ngưỡng rủi ro.
- **Peak windows**: các cụm năm có `peak_signal` vượt ngưỡng cơ hội.
- **Transformation windows**: cụm năm mà vừa có pressure (risk_signal) vừa có cơ hội (peak_signal) đủ mạnh để “đổi cách sống”.
- **Mission activation years**: năm mà `mission_signal` đủ mạnh và tương quan ổn với transformation windows.

V1 đề xuất cấu hình ngưỡng bằng `thresholds` (TBD theo tuning):
- `risk_threshold`
- `peak_threshold`
- `transformation_threshold`
- `mission_threshold`

Nguyên tắc tạo cụm:
- Một window là đoạn liên tiếp (hoặc cụm) năm mà tín hiệu vượt ngưỡng.
- Trả về cả danh sách năm hoặc range (tuỳ UI/engine).

---

## 6. Bước 4 — Forecast và chiến lược theo trục 12m/3y/10y

1. `current 12-month forecast`:
   - Lấy khoảng `current_age .. current_age+1`
   - Tổng hợp risk/peak/transformation/mission signals và tạo summary text/markers.

2. `3-year strategy` và `10-year direction`:
   - Gom theo stage/bucket hoặc theo windows nằm trong cửa sổ thời gian.
   - Output là khuyến nghị mang tính xác suất (luôn gắn `confidence` ở contract engine).

---

## 7. Liên kết output contract

Timeline output engine phải tuân contract engine output (README §17):
- `score`, `confidence`, `signals[]`, `insights[]`, `recommendations{stop,start,protect,build}`

Các trường windows nêu ở trên nằm trong `insights`/`signals` hoặc được đóng gói vào `life_code_data.json` (bước §21.3).

