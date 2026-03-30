# Life Code Index formula v1 (README §19)

**Nguồn chuẩn:** `README.md` mục **19**.

---

## 1. Các công thức

### Raw LCI

```text
LCI = Σ(LayerScore × LayerWeight)
```

### Adjusted LCI

```text
AdjustedLCI = Σ(LayerScore × LayerWeight × LayerConfidence)
```

### Data Coverage

```text
DataCoverage = Σ(ValidLayerWeights)
```

### Normalized LCI

```text
NormalizedLCI = Σ(LayerScore × LayerWeight) / Σ(ValidLayerWeights)
```

---

## 2. Status chuẩn

- `insufficient`
- `partial`
- `strong`
- `full`

## 3. Rule coverage

- coverage < 0.25 → `insufficient`
- 0.25 đến < 0.55 → `partial`
- 0.55 đến < 0.80 → `strong`
- ≥ 0.80 → `full`

---

## 4. Rule thiếu dữ liệu (README §19)

Khi không có dữ liệu cho một layer:

- `score = null`
- `confidence = 0`
- `status = "missing"`

Không được tự bịa score.

---

## 5. Liên kết contract & schema

- Engine output contract: `docs/OUTPUT_CONTRACT_V1.md` + `docs/schemas/engine-output-v1.schema.json`

