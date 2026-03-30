# Ethics guardrails v1 — không dự đoán ngày chết, luôn xác suất & hành động (README §4 + §26)

**Nguồn chuẩn:** `README.md`:
- **§4. Tuyên ngôn bắt buộc** (8 nguyên tắc)
- **§26. Bảo mật và đạo đức** → **Đạo đức**

---

## Quy tắc bắt buộc (khớp checklist mục 30F)

1. **Không dự đoán ngày chết / không gắn nhãn phá hủy**
   - Không đưa vào output các tuyên bố “ngày chết” cố định.
   - Không phán quyết theo kiểu “phá hủy/diệt vong” như một nhãn tuyệt đối.

2. **Không phán quyết tuyệt đối**
   - Không viết như lời tiên tri/quyết định số phận.

3. **Mọi kết luận mạnh đều có `confidence`**
   - Nếu không có confidence thì không được dùng kết luận mạnh.

4. **Forecast phải có điều kiện đúng/sai**
   - Mọi forecast cần ghi rõ “khi nào đúng” và “khi nào sai”.

5. **Output dẫn tới hành động**
   - Mọi layer khuyến nghị phải kết thúc ở action: stop/start/protect/build hoặc hướng hành động tương đương.

---

## Gợi ý áp dụng vào contract output (v1)

- Engine output contract luôn có `confidence` (README §17).
- Khi thiếu dữ liệu: `score = null`, `confidence = 0` và dùng trạng thái “missing” (README §19) để tránh suy đoán.
- Recommendations trong template/report chỉ được “đi xa” khi confidence đủ; nếu không, ưu tiên bước action dạng kiểm tra/thu thập dữ liệu.

