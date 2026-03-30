# Report generator architecture v1 — pipeline + template system (README §21)

**Nguồn chuẩn:** `README.md` mục **21**.

---

## 1. Pipeline bắt buộc

**Input → Engine → JSON → Template → HTML → PDF**

### Quy trình chuẩn

1. Input user data
2. Run analysis pipeline
3. Sinh `life_code_data.json`
4. Load template theo level
5. Inject data vào placeholder
6. Render markdown
7. Convert sang html
8. Export pdf / web report

---

## 2. Tên file template chuẩn (templates 1–9)

Các template phải dùng đúng tên file (chữ thường + dấu gạch dưới):

- `level1_self_signal_template.md`
- `level2_inner_architecture_template.md`
- `level3_behavior_code_template.md`
- `level4_work_wealth_code_template.md`
- `level5_relationship_field_template.md`
- `level6_life_timeline_template.md`
- `level7_body_intelligence_template.md`
- `level8_mission_path_template.md`
- `level9_full_life_code_template.md`

Repo hiện đặt tại: `docs/report-templates/`

---

## 3. Placeholder convention (để inject step 5)

Do README chỉ nêu “Inject data into placeholder”, v1 dùng convention tối giản:

### 3.1. Syntax

- Placeholder dùng cú pháp: `{{placeholder_name}}`

### 3.2. Bộ placeholder bắt buộc cho mọi template

- `{{identity_layer}}`
- `{{analysis_layer}}`
- `{{timeline_layer}}`
- `{{action_layer}}`

### 3.3. Placeholder cho core outputs

`life_code_data.json` (bước 3) được inject theo key trùng đúng mã output lõi ở README §18.

Ví dụ:
- `{{life_code_index}}`
- `{{adjusted_life_code_index}}`
- `{{data_coverage}}`
- `{{wealth_score}}`
- ...

---

## 4. Output bắt buộc (README §21)

- html
- pdf
- web view
- mobile view

---

## 5. Liên kết

- Template filenames: mục 2
- Engine output contract: `docs/schemas/engine-output-v1.schema.json` (README §17)
- Core output codes: `docs/CORE_OUTPUT_CODES.md` (README §18)

