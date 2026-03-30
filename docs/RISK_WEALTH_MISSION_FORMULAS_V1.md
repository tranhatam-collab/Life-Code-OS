# Risk / Wealth / Mission formulas v1 (contract-aligned)

**Bối cảnh chuẩn (README):**
- Output contract của mọi engine: `score`, `confidence`, `signals[]`, `insights[]`, `recommendations{stop,start,protect,build}` (README §17)
- Core output codes: `risk_score`, `wealth_score`, `mission_signal`, … (README §18)
- Timeline algorithm sinh windows (README “Risk/Peak/Transformation/Mission activation years”)
- Các Level liên quan:
  - Level 4: Wealth Code / Work & Wealth Code (output gồm `wealth_pattern`, `financial_stress_windows`, …)
  - Level 5: Relationship Field (output gồm `trust_pattern`, `conflict_trigger`, …)
  - Level 8: Mission Path (output gồm `mission_path`, `legacy_direction`, …)

---

## 1. Mục tiêu của v1

Sinh ba tín hiệu cốt lõi (dạng xác suất, có `confidence`):
- `risk_score`
- `wealth_score`
- `mission_signal`

Đồng thời ánh xạ sang các mã core outputs để dùng chung giữa engine/API/web/app/report.

---

## 2. Quy ước chung

### 2.1. Dùng “weighted sum” theo style LCI

V1 dùng chung dạng công thức có `LayerConfidence` để đảm bảo mọi kết luận đều có độ tin cậy:

```text
RawMetric = Σ(LayerScore × LayerWeight)
AdjustedMetric = Σ(LayerScore × LayerWeight × LayerConfidence)
```

Trong đó:
- `LayerScore`: score/signal từ từng layer engine thành phần
- `LayerWeight`: trọng số layer cho metric mục tiêu
- `LayerConfidence`: confidence đi kèm layer (0..1)

### 2.2. Khi thiếu dữ liệu

Áp dụng rule thiếu dữ liệu như README §19:
- `score = null`
- `confidence = 0`
- `status = "missing"`

---

## 3. Risk Score (v1)

**Output chính:** `risk_score` + các nhãn hỗ trợ để đóng góp vào `high-risk years`/`risk windows`.

**Tập layer đề xuất cho Risk (v1):**
- Health Risk Code
- Behavior Code (stress/decision stress)
- Relationship Field (conflict trigger / stress under relationship)
- Social Fate Code (xác suất bối cảnh rủi ro)

**Công thức (v1):**

```text
risk_score = AdjustedRiskMetric
```

Trong thực thi:
- `RiskLayerScore` lấy từ kết quả layer tương ứng (Health/Behavior/Relationship/Social)
- `risk_score` chỉ là tín hiệu xác suất (không phải mệnh lệnh)

---

## 4. Wealth Score (v1)

**Output chính:** `wealth_score` + các nhãn để đóng góp vào `wealth pattern`, `money_flow_pattern`.

**Tập layer đề xuất cho Wealth (v1):**
- Wealth Code
- Work Pattern / Career Cycle (thuộc Work & Wealth Code)
- Behavior Code (work behavior / energy leakage)

**Công thức (v1):**

```text
wealth_score = AdjustedWealthMetric
```

---

## 5. Mission Signal (v1)

**Output chính:** `mission_signal` + các nhãn để đóng góp vào `mission activation years` và “service path”.

**Tập layer đề xuất cho Mission (v1):**
- Mission Code
- Social Fate Code (legacy context)
- Relationship Field (support/conflict làm bật/tắt hướng sống)

**Công thức (v1):**

```text
mission_signal = AdjustedMissionMetric
```

---

## 6. Gắn kết với core output codes (README §18)

Các engine tạo signals/insights theo engine contract, và report/app có thể map:
- `risk_score` → core `risk_score`
- `wealth_score` → core `wealth_score`
- `mission_signal` → core `mission_signal`

Các fields khác như `money_flow_pattern`, `career_archetype`, `conflict_trigger`, `legacy_direction`, … được sinh như phần `signals`/`insights` ở layer liên quan, sau đó đóng gói trong `life_code_data.json` (pipeline README §21).

---

## 7. Links

- Output contract: `docs/OUTPUT_CONTRACT_V1.md` + `docs/schemas/engine-output-v1.schema.json`
- Core output codes: `docs/CORE_OUTPUT_CODES.md`

