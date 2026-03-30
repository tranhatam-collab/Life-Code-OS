# Levels Architecture v1 — Input / Engine / Output / Report length / Widgets / Unlock flow

**Nguồn:** `README.md`:
- **§10** Mô tả chuẩn 9 Levels (Input/Engines/Output/Report/độ dài)
- **§22** Dashboard widgets theo từng level
- **§19** Rule coverage → `insufficient|partial|strong|full`

**Mục tiêu:** Chốt kiến trúc “9 level” để sau này lập trình engine/API/web/app/report bám đúng cùng một cấu trúc.

---

## A. Unlock flow (gating theo status coverage)

Trong README §19:
- coverage < 0.25 → `insufficient`
- 0.25 đến < 0.55 → `partial`
- 0.55 đến < 0.80 → `strong`
- >= 0.80 → `full`

Trong `app.js`, trạng thái dùng cho Step 1 là `stepOne.outputStatus` với các mức:
`insufficient | partial | strong | full`.

**Quy ước unlock flow (v1, thực hành):**
- Luôn hiển thị Level `n` widget nhập dữ liệu (nền tảng) cho tới khi có thể tính được coverage.
- Chỉ unlock Level `n+1` khi Level `n` đạt **>= `strong`**.
- `insufficient/partial`: chỉ hiển thị phần báo cáo/tiến trình của Level `n` (không mở report Level `n+1`).

Ghi chú: Đây là “gợi ý unlock flow” dùng rule coverage để tránh tự bịa score (README §19).

---

## B. Dashboard widgets theo từng level (README §22)

### Level 1 widgets
- `core identity card`
- `life code index`
- `cycle now`
- `30-day focus`

### Level 2 widgets
- `inner architecture map`
- `risk base map`
- `3-year direction`

### Level 3 widgets
- `behavior radar`
- `stress profile`
- `work rhythm`

### Level 4 widgets
- `wealth pattern`
- `financial leakage map`
- `work archetype`

### Level 5 widgets
- `relationship field`
- `trust/conflict map`

### Level 6 widgets
- `timeline 0–99`
- `risk windows`
- `peak windows`
- `transformation windows`

### Level 7 widgets
- `face map`
- `hand map`
- `foot grounding map`

### Level 8 widgets
- `mission alignment`
- `repeated lessons`
- `service path`

### Level 9 widgets
- `full life dashboard`
- `timeline navigator`
- `strategy navigator`
- `report library`

---

## C. Kiến trúc Input / Engines / Output / Report

### Level 1 — Self Signal
**Input**
- `full_name`
- `date_of_birth`
- `time_of_birth`
- `place_of_birth`
- `gender`
- `current_location cơ bản`

**Engines**
- Birth Chrono Code
- Name Code
- Numerological Base
- Basic Cycle Analysis

**Output**
- `core identity sơ bộ`
- `life code index sơ bộ`
- `điểm mạnh bẩm sinh`
- `vùng rủi ro đầu tiên`
- `chu kỳ hiện tại`
- `tín hiệu nhiệm vụ sơ bộ`
- `hành động 30 ngày`

**Report**
- `Level1_SelfSignal_Report`

**Độ dài**
- 30–50 trang

---

### Level 2 — Inner Architecture
**Input**
- dữ liệu Level 1
- `social context cơ bản`
- `life phase detail`
- `mini questionnaire`

**Engines**
- Level 1 engines
- Birth Matrix mở rộng
- 9-year cycle
- 27-year cycle
- Social Fate Base
- Deep Structure Engine

**Output**
- inner architecture
- deep pattern
- pattern đổi hướng
- risk map sơ bộ
- wealth tendency sơ bộ
- relationship tendency sơ bộ
- 3-year direction
- 90-day focus

**Report**
- `Level2_InnerArchitecture_Report`

**Độ dài**
- 40–60 trang

---

### Level 3 — Behavior Code
**Input**
- dữ liệu Level 2
- questionnaire hành vi đầy đủ
- sleep
- stress
- work
- money
- relationship patterns

**Engines**
- Behavior Engine
- Habit Pattern Engine
- Stress Pattern Engine
- Decision Style Engine
- Recovery Engine

**Output**
- behavior profile
- decision style
- stress pattern
- work behavior
- energy leakage
- recovery mode
- hành vi làm lệch vận
- hành vi nâng vận

**Report**
- `Level3_BehaviorCode_Report`

**Độ dài**
- 50–70 trang

---

### Level 4 — Work & Wealth Code
**Input**
- dữ liệu Level 3
- income history
- work history
- money behavior
- risk tolerance
- ownership style

**Engines**
- Wealth Engine
- Work Pattern Engine
- Career Cycle Engine
- Financial Risk Engine

**Output**
- wealth pattern
- money leakage zones
- suitable work archetype
- financial stress windows
- asset direction
- 1-year work and finance guidance

**Report**
- `Level4_WealthCode_Report`

**Độ dài**
- 50–80 trang

---

### Level 5 — Relationship Field
**Input**
- dữ liệu Level 3
- relationship history
- trust pattern
- marriage / breakup history
- friendship / co-founder pattern

**Engines**
- Relationship Engine
- Trust Pattern Engine
- Conflict Trigger Engine
- Attachment Engine
- Human Field Mapping

**Output**
- relationship style
- attachment tendency
- trust pattern
- conflict triggers
- supportive partner type
- destructive partner type
- healing direction

**Report**
- `Level5_RelationshipField_Report`

**Độ dài**
- 50–80 trang

---

### Level 6 — Life Timeline
**Input**
- dữ liệu Level 1–5
- life events history
- timeline calibration

**Engines**
- Timeline Engine
- Event Probability Engine
- Risk Window Engine
- Peak Window Engine
- Transformation Window Engine
- Mission Activation Engine

**Output**
- timeline 0–99
- 9 giai đoạn đời
- high-risk years
- high-opportunity years
- transformation years
- mission activation years
- current 12-month forecast
- 3-year strategy
- 10-year direction

**Report**
- `Level6_LifeTimeline_Report`

**Độ dài**
- 60–100 trang

---

### Level 7 — Body Intelligence
**Input**
- ảnh mặt chuẩn
- ảnh tay chuẩn
- ảnh chân chuẩn
- ảnh theo thời gian nếu có

**Engines**
- Face Engine
- Hand Engine
- Foot Engine
- Morphology Synthesis Engine

**Output**
- facial stability / tension / openness
- palm resilience / decision power / emotional pattern
- grounding / endurance / survival orientation
- body-life mismatch
- dấu vết áp lực in lên cơ thể

**Report**
- `Level7_BodyIntelligence_Report`

**Độ dài**
- 60–120 trang

---

### Level 8 — Mission Path
**Input**
- dữ liệu Level 1–7 đầy đủ

**Engines**
- Mission Engine
- Repeated Lesson Extractor
- Legacy Orientation Engine
- Transformation Synthesis Engine

**Output**
- mission path
- repeated lessons
- service path
- legacy direction
- stop / build / transform list
- deep 90-day transformation
- 1-year mission plan
- 3-year repositioning roadmap

**Report**
- `Level8_MissionPath_Report`

**Độ dài**
- 80–150 trang

---

### Level 9 — Full Life Code
**Input**
- toàn bộ dữ liệu từ mọi level
- timeline thật
- questionnaire đầy đủ
- ảnh đầy đủ
- event calibration

**Engines**
- toàn bộ 12 layer engines
- fusion layer
- forecast layer
- recommendation layer
- AI-assisted synthesis

**Output**
- full core identity
- full life code index
- adjusted index
- risk / wealth / relationship / mission / health scores
- 12 layer synthesis
- timeline 0–99 full
- 12-month forecast
- 3-year strategy
- 10-year direction
- repeated lessons
- full action system

**Report**
- `Level9_FullLifeCodeBook`

**Độ dài**
- 150–600 trang

