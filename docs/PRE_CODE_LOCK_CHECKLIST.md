# Checklist — Khóa chuẩn trước khi code sâu

Nguồn: `README.md` mục **30**, **31**, **32**. Đánh dấu `[x]` khi đã chốt trong docs/code; mọi thay đổi sau đó phải cập nhật README trước (mục 33).

**Tài liệu đã có (tiến độ Trục B):**

- [GLOSSARY.md](./GLOSSARY.md) — bản khóa ngôn ngữ v1 (tên hệ, 9 level, thuật ngữ cấm/dùng, LCI)  
- [DATA_MODEL.md](./DATA_MODEL.md) — 5 profile (README §16)  
- [REPORT_LAYERS.md](./REPORT_LAYERS.md) — 4 lớp report (README §11)  
- [schemas/engine-output-v1.schema.json](./schemas/engine-output-v1.schema.json) — JSON engine output (README §17)  
- [OUTPUT_CONTRACT_V1.md](./OUTPUT_CONTRACT_V1.md) — output contract v1 (README §17)  
- [CORE_OUTPUT_CODES.md](./CORE_OUTPUT_CODES.md) — core output codes (README §18)  
- [LEVELS_ARCHITECTURE_V1.md](./LEVELS_ARCHITECTURE_V1.md) — kiến trúc Input/Engine/Output 9 level + widgets + unlock flow
- [REPORT_GENERATOR_ARCHITECTURE_V1.md](./REPORT_GENERATOR_ARCHITECTURE_V1.md) — pipeline + templates system (README §21)
- [ETHICS_GUARDRAILS_V1.md](./ETHICS_GUARDRAILS_V1.md) — đạo đức/guardrails (README §4 + §26)
- [LCI_FORMULA_V1.md](./LCI_FORMULA_V1.md) — Life Code Index formula v1 (README §19)
- [TIMELINE_ALGORITHM_V1.md](./TIMELINE_ALGORITHM_V1.md) — Timeline 0–99 algorithm v1 (Level 6)

---

## Giai đoạn khóa chuẩn (mục 31 — thứ tự)

- [x] 1. Khóa ngôn ngữ toàn hệ *(chốt bằng [GLOSSARY.md](./GLOSSARY.md) + [CORE_OUTPUT_CODES.md](./CORE_OUTPUT_CODES.md))*  
- [x] 2. Khóa kiến trúc 9 level *(chốt bằng [LEVELS_ARCHITECTURE_V1.md](./LEVELS_ARCHITECTURE_V1.md))*  
- [x] 3. Khóa kiến trúc report generator *(chốt bằng [REPORT_GENERATOR_ARCHITECTURE_V1.md](./REPORT_GENERATOR_ARCHITECTURE_V1.md) + templates 1–9 trong `docs/report-templates/`)*  
- [x] 4. Khóa output contract *(chốt bằng schema + [OUTPUT_CONTRACT_V1.md](./OUTPUT_CONTRACT_V1.md))*  
- [x] 5. Khóa glossary  

---

## A — Ngôn ngữ

- [x] Tên hệ (chuẩn hiển thị + internal)  
- [x] Tên 9 level (đồng bộ UI / report / API)  
- [x] Tên output (từng loại báo cáo / chỉ số)  
- [x] Glossary (thuật ngữ cấm / bắt buộc — xem README mục 7)  

## B — Sản phẩm (theo level)

- [x] Input từng level  
- [x] Engine từng level  
- [x] Output từng level  
- [x] Độ dài / cấu trúc report  
- [x] Widget từng level  
- [x] Unlock flow  

## C — Report system

- [x] 4 lớp report  
- [x] Templates 1–9  
- [x] Quy ước đặt tên file  
- [x] Quy ước placeholder  
- [x] Render pipeline  

## D — Data model

- [x] Identity profile  
- [x] Input profile  
- [x] Analysis profile  
- [x] Growth profile  
- [x] Event profile  

## E — Engine contracts

- [x] Score  
- [x] Confidence  
- [x] Signals  
- [x] Insights  
- [x] Recommendations  

## F — Ethics (đối chiếu README mục 4 + 26)

- [x] Không ngày chết  
- [x] Không phán quyết tuyệt đối  
- [x] Mọi kết luận mạnh có confidence  
- [x] Forecast có điều kiện đúng/sai  
- [x] Output dẫn tới hành động  

---

## Sau khóa chuẩn — 4 bước kỹ thuật (mục 31)

- [x] Life Code Index formula  
- [x] Timeline 0–99 algorithm  
- [ ] Risk / Wealth / Mission formulas  
- [ ] Automatic report app  

---

## Definition of Done (mục 32) — mỗi giai đoạn

- [ ] Docs chuẩn  
- [ ] Code tương ứng  
- [ ] Test chạy được  
- [ ] Output JSON chuẩn  
- [ ] Rule khi thiếu dữ liệu  
- [ ] Có confidence trong output  
- [ ] Không mâu thuẫn README  

---

## Thứ tự lập trình sau cùng (mục 31)

- [ ] Engine  
- [ ] API  
- [ ] Web  
- [ ] App  
- [ ] Report system  
