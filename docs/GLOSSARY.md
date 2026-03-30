# Glossary — Life Code OS (khóa ngôn ngữ v1)

**Nguồn chuẩn:** `README.md` mục **6–8** (và mục 7 thuật ngữ).  
**Quy tắc:** Mọi thay đổi thuật ngữ → sửa **README trước**, rồi cập nhật file này.

---

## Tên hệ & positioning

| Ngữ cảnh | Chuẩn |
|----------|--------|
| Tên sản phẩm (EN) | **Life Code OS** |
| Tagline (VI) | **Mật Mã Đời Người** |
| Mô tả học thuật | **Huyền Nhân Học – Human Life Intelligence System** |

---

## Domain & hạ tầng (tham chiếu)

| Mục | Giá trị |
|-----|---------|
| Web | `lifecode.iai.one` |
| API (dự kiến) | `api.lifecode.iai.one` |
| Admin (dự kiến) | `admin.lifecode.iai.one` |
| Repo | `life-code-os` |
| Pages project | `life-code-os` |
| Worker API | `life-code-api` |

Chi tiết D1/R2/binding: README mục **6.6–6.8**.

---

## Thuật ngữ — không dùng

| Tránh |
|-------|
| Chapter |
| Lesson |
| Fate reading |
| Fortune telling |

---

## Thuật ngữ — dùng thống nhất

Level, Life Layer, Insight Layer, Signal, Pattern, Field, Direction, Window, Strategy, Mission.

---

## 9 Levels — tên hiển thị & mã kỹ thuật

| # | Tên (EN — chuẩn README) | `code` (app/API) | Gợi ý tên file báo cáo |
|---|-------------------------|------------------|-------------------------|
| 1 | Self Signal | `level1` | `Level1_SelfSignal_Report` |
| 2 | Inner Architecture | `level2` | `Level2_InnerArchitecture_Report` |
| 3 | Behavior Code | `level3` | `Level3_BehaviorCode_Report` |
| 4 | Work & Wealth Code | `level4` | `Level4_WealthCode_Report` |
| 5 | Relationship Field | `level5` | `Level5_RelationshipField_Report` |
| 6 | Life Timeline | `level6` | `Level6_LifeTimeline_Report` |
| 7 | Body Intelligence | `level7` | `Level7_BodyIntelligence_Report` |
| 8 | Mission Path | `level8` | `Level8_MissionPath_Report` |
| 9 | Full Life Code | `level9` | `Level9_FullLifeCodeBook` |

Đồng bộ với `app.js` → `window.LIFE_CODE_APP.levels`.

---

## Chỉ số & trạng thái output (Step 1 / LCI)

| Thuật ngữ | Ghi chú |
|-----------|---------|
| Raw LCI / Normalized LCI / Adjusted LCI | Công thức README mục **25** |
| `raw_lci`, `normalized_lci`, `adjusted_lci`, `data_coverage` | Khóa trong `app.js` → `stepOne.formulas` |
| `insufficient` / `partial` / `strong` / `full` | `stepOne.outputStatus` — mức đủ dữ liệu |

---

## Engine output — trường hợp hợp đồng (mục 30E)

Mọi engine layer nên có thể map sang: **score**, **confidence**, **signals**, **insights**, **recommendations**.  
Schema JSON tham chiếu: [schemas/engine-output-v1.schema.json](./schemas/engine-output-v1.schema.json).

---

## Ethics — từ khóa kiểm (mục 30F)

Không đưa vào output: tuyên bố **ngày chết** cố định, **phán quyết tuyệt đối** định mệnh.  
Luôn có: **confidence**, **xác suất / điều kiện**, **hành động** gợi ý.
