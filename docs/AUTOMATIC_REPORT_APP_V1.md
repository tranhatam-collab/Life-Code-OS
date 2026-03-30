# Automatic report app v1 — tạo báo cáo tự động 300–600 trang (README bước app/engine + §21)

**Nguồn:** `README.md`
- Pipeline report generator (README §21)
- Output contract (README §17)
- Rule missing data / confidence (README §19)
- Level output expectations (README §10, §11)

---

## 1. Mục tiêu

Automatic report app có nhiệm vụ:
- Nhận dữ liệu user (identity + input profile)
- Chạy engine theo pipeline (Level 1 → Level 9 theo unlock flow)
- Sinh `life_code_data.json` để làm nguồn cho template
- Render template theo từng level
- Xuất ra đủ định dạng: html + pdf + web view + mobile view
- Lưu history để người dùng xem lại / xuất lại

Đảm bảo mọi kết luận xuất ra đều có `confidence` và không vi phạm ethics guardrails.

---

## 2. Input / Trigger

Trigger (v1):
- Khi user submit questionnaire + ảnh (nếu có) + event calibration (nếu có)
- Và coverage cho level hiện tại đạt điều kiện unlock (README §19: `strong/full` để unlock cấp tiếp theo)

Input tối thiểu:
- Identity profile (README §16)
- Input profile (README §16)
- Event profile / calibration (nếu người dùng cung cấp)

---

## 3. Luồng xử lý (v1)

1. **Run engine pipeline**
   - Chạy các engine thuộc level tương ứng.
   - Mỗi engine trả về output contract theo README §17.

2. **Build `life_code_data.json`**
   - Map output contract → core output codes (README §18).
   - Map layer results → `identity_layer / analysis_layer / timeline_layer / action_layer` cho template (README §11 + placeholder convention ở `docs/REPORT_GENERATOR_ARCHITECTURE_V1.md`).

3. **Template selection**
   - Chọn đúng template theo level bằng filenames chuẩn (README §21):
     - `level1_self_signal_template.md` … `level9_full_life_code_template.md`

4. **Inject placeholder**
   - Inject `{{identity_layer}}`, `{{analysis_layer}}`, `{{timeline_layer}}`, `{{action_layer}}`
   - Inject core outputs theo key trùng mã (ví dụ `{{life_code_index}}`, `{{risk_score}}`, …)

5. **Render + export**
   - Render markdown → HTML
   - Export PDF
   - Sinh web view và mobile view

6. **Persist & history**
   - Lưu kết quả: metadata + status + confidence + links/IDs tới tài liệu đã export

---

## 4. Output contract app cần lưu (v1)

Đối với mỗi lần generate:
- `status`: `insufficient|partial|strong|full` theo coverage
- `confidence`: tổng/aggregate hoặc confidence level theo pipeline
- `generated_at`
- `level_reports[]`: danh sách report theo từng level đã unlock

---

## 5. Liên kết

- Engine output contract: `docs/schemas/engine-output-v1.schema.json`
- Core outputs: `docs/CORE_OUTPUT_CODES.md`
- Template system + placeholder: `docs/REPORT_GENERATOR_ARCHITECTURE_V1.md` + `docs/report-templates/`
- Unlock/status rule: README §19

