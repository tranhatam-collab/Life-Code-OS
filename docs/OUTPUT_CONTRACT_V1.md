# Output contract v1 — chuẩn trả về của mọi engine (README §17)

**Nguồn chuẩn:** `README.md` mục **17**.  
**Mục tiêu:** Mọi engine layer phải trả về đúng cấu trúc thống nhất này.

---

## 1. Contract bắt buộc

```json
{
  "score": 78,
  "confidence": 0.81,
  "signals": ["high_cycle_sensitivity", "leadership_potential"],
  "insights": [
    "Người này có xu hướng phát triển mạnh ở các giai đoạn chuyển chu kỳ."
  ],
  "recommendations": {
    "stop": [],
    "start": [],
    "protect": [],
    "build": []
  }
}
```

### Quy tắc bắt buộc

- Không được phá contract key-level như trên.
- `confidence` luôn là giá trị dùng được (README: 0..1).
- `score` có thể là `null` khi thiếu dữ liệu (tham chiếu quy tắc thiếu dữ liệu ở README §19).

---

## 2. Rule khi thiếu dữ liệu (README §19)

Khi không có dữ liệu cho một layer:

- `score = null`
- `confidence = 0`
- `status = "missing"` *(field mở rộng; contract gốc ở §17 vẫn giữ cấu trúc key bắt buộc)*  

---

## 3. Schema tham chiếu (đồng bộ engine-output-v1)

- `docs/schemas/engine-output-v1.schema.json`

