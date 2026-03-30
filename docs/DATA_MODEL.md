# Data model — 5 hồ sơ nền (README §16)

**Nguồn:** `README.md` mục **16**. Không thay đổi ý nghĩa tại đây mà không sửa README trước.

Life Code dùng **5 profile** làm xương sống dữ liệu:

---

## 1. Identity Profile

| Trường (khái niệm) | Ghi chú |
|--------------------|--------|
| Tên | |
| Ngày sinh | |
| Giờ sinh | |
| Nơi sinh | |
| Giới tính | |
| Vị trí hiện tại | |
| Ngôn ngữ | |

---

## 2. Input Profile

- Questionnaire  
- Ảnh  
- Lịch sử sự kiện (event history)  
- Bối cảnh xã hội (social context)  
- Lifestyle markers  

---

## 3. Analysis Profile

- Kết quả theo layer (`layer results`)  
- Kết quả chỉ số (`index results`)  
- **Confidence**  
- **Insights**  
- **Signals**  

---

## 4. Growth Profile

- Cập nhật hành vi (behavior updates)  
- Nhật ký (journals)  
- Sự kiện follow-up  
- Phân tích định kỳ (periodic re-analysis)  

---

## 5. Event Profile

- Sự kiện đời thô (raw life events)  
- Category  
- Severity  
- Vị trí trên timeline (timeline placement)  
- Trạng thái xác thực (validation status)  

---

## Liên kết

- Output engine từng layer: [schemas/engine-output-v1.schema.json](./schemas/engine-output-v1.schema.json) (đồng bộ README §17)  
- Bốn lớp trong báo cáo: [REPORT_LAYERS.md](./REPORT_LAYERS.md)  
