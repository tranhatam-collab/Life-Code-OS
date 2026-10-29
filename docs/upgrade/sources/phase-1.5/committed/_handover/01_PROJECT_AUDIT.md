# 01 — Project Audit

**Mốc:** 2026-04-26 — HEAD `99b4027`

## Tổng quan kiến trúc

```
Life Code OS
├── Cloudflare Pages: marketing/app site (HTML tĩnh + JS client-side)
│   ├── index.html, gioi-thieu.html, … (12 trang marketing/legal)
│   ├── bat-dau.html         → form nhập liệu user → POST /api/v1/life-code-data
│   ├── dashboard.html       → lấy /api/v1/me, hiển thị kết quả + history
│   ├── account.html         → profile, sessions, audit log
│   ├── engine-lab.html      → test engine + render report + PDF export
│   ├── monitor.html         → ops summary dashboard nội bộ
│   └── app.js / site.js / style.css
│
├── Cloudflare Worker: life-code-api (workers/life-code-api/)
│   ├── src/index.js         → router endpoints
│   ├── src/engine.mjs       → engine v1 (LCI, Timeline, RWM)
│   ├── src/report.mjs       → report renderer Level 1–9
│   ├── migrations/          → 6 migrations D1 (tables, sessions, profile, rate-limit, audit, alert dispatch)
│   └── tests/report-smoke.mjs
│
├── D1 Database: life-code-db
│   ├── user_profiles, life_code_results
│   ├── sessions (token auth + device meta + revoke)
│   ├── audit_logs (account changes)
│   ├── rate_limit_buckets
│   └── alert_dispatch_logs
│
├── Engine library (engine/)
│   ├── core/lci.js, timeline.js, risk-wealth-mission.js
│   ├── data/life_code_data.json (curated content for 9 levels)
│   └── tests/smoke.cjs
│
└── Docs (docs/)
    ├── Specs: GLOSSARY, DATA_MODEL, REPORT_LAYERS, OUTPUT_CONTRACT_V1, CORE_OUTPUT_CODES
    ├── Architecture: LEVELS_ARCHITECTURE_V1, REPORT_GENERATOR_ARCHITECTURE_V1, AUTOMATIC_REPORT_APP_V1
    ├── Formulas: LCI_FORMULA_V1, TIMELINE_ALGORITHM_V1, RISK_WEALTH_MISSION_FORMULAS_V1
    ├── Ops: GIT_CLOUDFLARE_LIFECODE, PRE_CODE_LOCK_CHECKLIST, ETHICS_GUARDRAILS_V1
    ├── schemas/engine-output-v1.schema.json
    └── report-templates/level1..9_template.md
```

## % Hoàn thành theo trục (theo `PROJECT_STATUS_MASTER.md`)

| Trục | Mức | Chi tiết |
|---|---|---|
| **A — Hạ tầng & CI deploy** | **100%** | Repo ✅, Secrets `CF_API_TOKEN` ✅, Workflows pages + worker ✅, Pages domain `lifecode.iai.one` ✅, Wrangler config Worker ✅. |
| **B1 — Khóa chuẩn ngôn ngữ/contract** (README §30) | **~85–90%** | Glossary, data model, report layers, output contract v1, levels architecture, report generator pipeline. |
| **B2 — Công thức** (README §31) | **~75–85%** | LCI, Timeline 0–99, Risk/Wealth/Mission v1 đã chốt. |
| **B3 — Engine + API + App + Report** | **~90–95%** | Engine v1, Worker + D1, session auth, profile CRUD, dashboard, account, monitor, report 1–9, PDF export. |
| **B4 — QA + Ops production** | **~70%** | Contract test ✅, rate-limit smoke ✅, e2e smoke local ✅, monitoring endpoint ✅, alert-check ✅; **thiếu**: webhook URL production, QA E2E production cuối, alert webhook integration test. |

## Lỗ hổng / việc còn lại (rút từ status doc + audit code)

### B1 — Spec & contract
- [ ] Schema validation cho **input theo từng level** (level 2–9 input chi tiết) — hiện form chính ở `bat-dau.html` chỉ Level 1 sâu.
- [ ] Confidence score mapping cho output level 2–9 (giờ trả về template với placeholder, một số chỗ là hardcoded).

### B2 — Công thức
- [ ] Cross-validation các công thức với data sample mở rộng (ngoài `engine/data/sample-input.json`).
- [ ] Văn bản hóa **biên độ tin cậy** (confidence intervals) cho LCI và Timeline.

### B3 — App/Engine
- [ ] Form nhập liệu chi tiết cho từng Level 2–9 (hiện chỉ có Level 1 đầy đủ; level cao dùng dữ liệu suy luận).
- [ ] Save report đã render vào D1 (history rộng hơn `life_code_results` snapshot hiện tại).
- [ ] Multi-language output (hiện tiếng Việt; cần EN tối thiểu cho marketing/preview).
- [ ] Profile completeness gate: chặn render Level cao khi input thiếu (hiện đã có completeness % ở dashboard, chưa gate render).

### B4 — Ops & QA
- [ ] **Webhook URL production** cho `/api/v1/ops/alert-check` (Slack/Discord/email — env binding).
- [ ] E2E production smoke chạy định kỳ (cron Worker hoặc GitHub Action scheduled).
- [ ] Backup D1 định kỳ (export schema + data → R2 hoặc artifact).
- [ ] Pen test cơ bản: SQLi/XSS scan trên endpoints công khai.
- [ ] PII review: audit log không chứa data nhạy cảm (đã có ETHICS_GUARDRAILS, cần kiểm verifier).

### Tài liệu thiếu cho **team dev**
- [ ] **CONTRIBUTING.md** — git flow, commit convention, review rules.
- [ ] **API_REFERENCE.md** — liệt kê đầy đủ endpoints `/api/v1/*` với request/response.
- [ ] **LOCAL_DEV.md** — `npm run worker:dev` + `wrangler pages dev` + D1 local.
- [ ] **ENV_AND_SECRETS.md** — danh sách env biến (`MONITOR_KEY`, `ALERT_WEBHOOK_URL`, `RATE_LIMIT_*`).
- [ ] **TESTING.md** — chạy `qa:contract`, `qa:rate-limit`, `e2e:smoke`, `report:test`.
- [ ] **RELEASE_RUNBOOK.md** — bước release từ branch → PR → main → Pages/Worker deploy → smoke production.

> Các tài liệu này được khởi tạo trong [02 — Completion Plan](./02_COMPLETION_PLAN.md) và [04 — Dev Onboarding](./04_DEV_ONBOARDING.md).

## Endpoints Worker đã có (rút từ `workers/life-code-api/src/index.js`)

> Cần xác minh trực tiếp khi BE dev đọc file. Danh sách dưới đây dựa trên migration + script tests + status doc:

- `POST /api/v1/life-code-data` — submit form Level 1 input → engine → lưu D1.
- `GET /api/v1/profile/:id`
- `POST /api/v1/session/start` — phát session token.
- `GET /api/v1/me` — lấy profile theo session.
- `POST /api/v1/session/revoke` — revoke 1 session.
- `POST /api/v1/profile/update` — cập nhật avatar/locale/notification.
- `POST /api/v1/report` — render báo cáo `level=1..9`.
- `GET /api/v1/ops/summary` — KPI nội bộ (yêu cầu `MONITOR_KEY`).
- `POST /api/v1/ops/alert-check` — đánh giá ngưỡng + ghi `alert_dispatch_logs`.

→ **Action item:** dev BE đọc `src/index.js`, viết `docs/API_REFERENCE.md` chính xác.

## Cấu hình hạ tầng cần xác nhận trước khi team dev nhận

| Hạng mục | Nguồn | Ai giữ |
|---|---|---|
| `CF_API_TOKEN` (GitHub Secret) | GitHub repo settings | Founder |
| `account_id` Cloudflare | `wrangler.toml` (đã commit) | OK |
| D1 `database_id` | `wrangler.toml` (đã commit) | OK |
| `MONITOR_KEY` (Worker secret) | `wrangler secret` | Founder |
| `ALERT_WEBHOOK_URL` (chưa có production) | `wrangler secret` | **TODO** |
| Pages custom domain `lifecode.iai.one` | Cloudflare Pages | OK |
| Worker route (optional) `api.lifecode.iai.one/*` | Cloudflare Workers Routes | **TODO** |
