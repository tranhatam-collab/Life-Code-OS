# 05 — Backlog Tickets

Danh sách ticket sẵn sàng nhận. Mỗi ticket khi được pick sẽ mở Issue trên GitHub với label tương ứng.

Format ticket: `[ID] Tiêu đề — Owner gợi ý — Effort (S/M/L) — Phase`.

---

## Phase 1.5 — Bilingual Foundation (BẮT BUỘC, gate chặn live)

> Chi tiết spec: [06 — Bilingual Lock](./06_BILINGUAL_LANGUAGE_REBUILD_LOCK.md). Hoàn tất LANG-101 → LANG-105 trước khi mở merge cho Phase 2A.

### LCOS-LANG-101 — Crawl + inventory text public
**Owner:** Tech lead — **Effort:** M — **Phase:** 1.5

**What:** script Node crawl 12 page hiện tại (`*.html` ở root) + parse `<title>`, meta, OG, JSON-LD, mọi text node, image alt, form label/placeholder. Xuất `_handover/bilingual/01_CRAWL_INVENTORY.csv`.

**DoD:** CSV ≥ 12 page × ~30 trường mỗi page; có cả URL production khi compare.

---

### LCOS-LANG-102 — Audit table song ngữ
**Owner:** Editor + SEO lead — **Effort:** M — **Phase:** 1.5

**What:** từ CSV LANG-101 → đánh giá VI/EN/SEO/UI per page, gán P0/P1/P2. File `_handover/bilingual/02_AUDIT_TABLE.csv`.

**DoD:** mọi page có status đầy đủ; danh sách page P0 (cần fix trước khi live) rõ ràng.

---

### LCOS-LANG-103 — Language Codex
**Owner:** Editor (lead) + Founder (approve) — **Effort:** L — **Phase:** 1.5

**What:** `_handover/bilingual/LANGUAGE_CODEX.md` chứa:
- **Term registry** (Life Code, LCI, level 1–9 names, timeline, mission code, …) VI + EN locked
- **Banned words** (slang, hype, máy dịch điển hình)
- **Tone matrix** per page type (marketing / app / legal / form / dashboard)
- **Heading hierarchy** rule
- **CTA registry** (label VI + EN cho mọi nút)
- **Form registry** (label, placeholder, error message)
- **Empty state + system notification registry**

**DoD:** Founder approve. Tham chiếu chéo với `docs/GLOSSARY.md`.

---

### LCOS-LANG-104 — Skeleton `content/vi.json` + `content/en.json`
**Owner:** FE dev — **Effort:** M — **Phase:** 1.5

**What:** tạo `content/vi.json`, `content/en.json` với keys cho:
- `nav.*` (menu chính + phụ)
- `footer.*`
- `pages.<slug>.title`, `.metaDescription`, `.ogTitle`, `.ogDescription`, `.h1`, `.heroDek`
- `cta.*` từ Codex
- `form.*` từ Codex
- `error.*` + `empty.*`

12 page hiện có: `index`, `bat-dau`, `dashboard`, `account`, `monitor`, `engine-lab`, `gioi-thieu`, `he-thong-life-code`, `life-code-index`, `du-an-life-code`, `bao-cao-life-code`, `lien-he`, `cau-hoi-thuong-gap`, `timeline-cuoc-doi`, `9-levels-life-code`, `chinh-sach-bao-mat`, `dieu-khoan-su-dung`, `ban-quyen-so-huu-tri-tue`.

**DoD:** 2 file JSON merge vào main; không có giá trị `null`/`""` cho key bắt buộc.

---

### LCOS-LANG-105 — Refactor HTML render text từ JSON
**Owner:** FE dev — **Effort:** L — **Phase:** 1.5

**What:** loader nhỏ trong `site.js`:
- Detect `lang` (cookie `lcos_lang`, query `?lang=`, hoặc default `vi`)
- Fetch `content/<lang>.json`
- Replace text node theo `data-i18n="key.path"` attribute trong HTML
- Update `<title>`, meta, OG dynamic
- Language switcher button trong header → toggle + reload đúng URL ngôn ngữ

**DoD:** mọi page render đúng cả VI và EN; không còn text public hard-code (verify bằng grep test trong CI).

---

### LCOS-LANG-106 — hreflang + canonical
**Owner:** FE dev — **Effort:** S — **Phase:** 1.5

**What:** mỗi page render đủ:
- `<link rel="canonical" href="https://lifecode.iai.one/<path>?lang=<lang>" />`
- `<link rel="alternate" hreflang="vi" href="…?lang=vi" />`
- `<link rel="alternate" hreflang="en" href="…?lang=en" />`
- `<link rel="alternate" hreflang="x-default" href="…?lang=vi" />`

**DoD:** Google Rich Results test pass cho 3 page mẫu.

---

### LCOS-LANG-107 — CI lang-gate workflow
**Owner:** Tech lead — **Effort:** M — **Phase:** 1.5

**What:** `.github/workflows/lang-gate.yml`:
- Trigger: pull_request paths `*.html`, `app.js`, `site.js`, `content/**`, `site-templates/**`
- Job:
  - Nếu PR có label `lang-not-applicable` → pass.
  - Nếu PR có label `lang-ready` → pass.
  - Nếu thiếu cả 2 → **fail** với message giải thích 4-pass review.
- Branch protection rule: required status check `lang-gate` cho `main`.

**DoD:** test fail expected case (PR đụng index.html không label) + pass case.

---

### LCOS-LANG-108 — PR template 4-pass checklist
**Owner:** Tech lead — **Effort:** S — **Phase:** 1.5

**What:** `.github/PULL_REQUEST_TEMPLATE.md` với:
```
## Why
## What
## How to verify
## Migration? (Y/N) — kèm revert script nếu Y

## Bilingual 4-pass review (bỏ qua nếu lang-not-applicable)
- [ ] Pass 1 — AI/Codex (chính tả, dấu, ngữ pháp, máy dịch)
- [ ] Pass 2 — Editor (tone, ngữ nghĩa, định vị)
- [ ] Pass 3 — SEO lead (title/meta/OG/hreflang/canonical/alt/schema)
- [ ] Pass 4 — QA lead (render thực tế VI + EN, mobile + desktop)
```

**DoD:** PR mới render đúng template.

---

## Phase 1 — Docs nền

### LCOS-101 — `docs/API_REFERENCE.md`
**Owner:** BE dev — **Effort:** M — **Phase:** 1

**Why:** chưa có tài liệu chính thức về REST endpoints; đang phải đọc `src/index.js` để biết.

**What:**
- Liệt kê toàn bộ endpoints `/api/v1/*`
- Mỗi endpoint: method, path, headers required (e.g. `x-session-token`, `x-monitor-key`), request body schema, response shape, error codes
- Ví dụ `curl` cho mỗi endpoint
- Note rate-limit + auth rules

**DoD:** PR merged; nội dung khớp 100% với `workers/life-code-api/src/index.js`.

---

### LCOS-102 — `docs/ENV_AND_SECRETS.md`
**Owner:** BE dev — **Effort:** S — **Phase:** 1

**What:** liệt kê đầy đủ env biến và secret cần thiết cho Worker:
- `MONITOR_KEY` — bảo vệ `/api/v1/ops/*`
- `ALERT_WEBHOOK_URL` — Slack/Discord webhook (TODO setup)
- Bất kỳ rate-limit threshold biến nào
- Mỗi biến: scope (production/preview), cách set (`wrangler secret put`), khi nào rotate

**DoD:** PR merged; có lệnh exact để set/rotate từng secret.

---

### LCOS-103 — `docs/TESTING.md`
**Owner:** QA dev — **Effort:** S — **Phase:** 1

**What:** hướng dẫn chạy:
- `npm run engine:test`
- `npm run report:test`
- `npm run qa:contract`
- `npm run qa:rate-limit`
- `npm run qa:hardening`
- `npm run e2e:smoke`

Mỗi script: input cần thiết, kỳ vọng output, cách debug khi fail.

**DoD:** dev mới làm theo doc, all script pass.

---

### LCOS-104 — `CONTRIBUTING.md`
**Owner:** Tech lead — **Effort:** S — **Phase:** 1

**What:** branch convention, commit convention, PR rules, review SLA, squash merge policy. Tham chiếu `_handover/04_DEV_ONBOARDING.md`.

**DoD:** PR merged ở root repo; link từ README.md.

---

### LCOS-105 — `docs/RELEASE_RUNBOOK.md`
**Owner:** Tech lead — **Effort:** M — **Phase:** 1

**What:**
- Pre-release checklist (test, version bump nếu cần, changelog)
- Release flow: PR merge → CI deploy → smoke production → tag `prod-vN`
- Hotfix flow
- Rollback flow (Pages từ Cloudflare UI; Worker checkout commit cũ; D1 migration revert)

**DoD:** PR merged.

---

## Phase 2A — Profile & Input

### LCOS-201 — Form input Level 2 (Inner Architecture)
**Owner:** FE dev — **Effort:** M — **Phase:** 2A

**Why:** Level 2 hiện render dùng dữ liệu suy luận từ Level 1 → confidence thấp.

**What:**
- Section mới trong `account.html` hoặc tab mới `bat-dau.html` cho Level 2 input
- Schema khớp `docs/LEVELS_ARCHITECTURE_V1.md` mục Level 2
- Submit qua `POST /api/v1/profile/level/2` (BE tạo nếu chưa có)
- Render Level 2 report dùng dữ liệu thật

**DoD:** user submit → D1 lưu → render Level 2 report dùng input thật, confidence ≥ ngưỡng.

---

### LCOS-202 — Form input Level 3 (Behavior Code)
**Owner:** FE dev — **Effort:** M — **Phase:** 2A

Tương tự LCOS-201, schema từ `LEVELS_ARCHITECTURE_V1.md` mục Level 3.

---

### LCOS-203 — Form input Level 4 (Work/Wealth)
**Owner:** FE dev — **Effort:** M — **Phase:** 2A

Tương tự, mục Level 4.

---

### LCOS-204 — Profile completeness gate
**Owner:** FE dev — **Effort:** S — **Phase:** 2A

**What:**
- Tính completeness score riêng cho mỗi level
- Disable nút "Mở report Level X" + tooltip lý do khi completeness < ngưỡng (ví dụ 70%)
- Hiển thị "Bạn cần điền X, Y, Z" để unlock

**DoD:** UX không cho user click vào Level mà data thiếu.

---

## Phase 2B — Report production

### LCOS-211 — Migration `report_renders`
**Owner:** BE dev — **Effort:** S — **Phase:** 2B

**What:**
- `workers/life-code-api/migrations/007_report_renders.sql`
- Cột: `id`, `user_id`, `level`, `markdown`, `meta_json`, `created_at`
- Index `(user_id, level, created_at desc)`
- **Kèm script revert trong PR description**

**DoD:** migration apply local + remote thành công; rollback script test pass local.

---

### LCOS-212 — Lưu report sau khi render
**Owner:** BE dev — **Effort:** S — **Phase:** 2B

**What:** trong `POST /api/v1/report`, sau khi render thành công → INSERT `report_renders` row.

**DoD:** mỗi request render → 1 row mới; smoke test verify.

---

### LCOS-213 — Endpoint history
**Owner:** BE dev — **Effort:** S — **Phase:** 2B

**What:** `GET /api/v1/reports/history?level=N` trả về list 20 report mới nhất user hiện tại.

**DoD:** auth qua session token; response array `{id, level, created_at, preview}`.

---

### LCOS-214 — UI dashboard hiển thị history
**Owner:** FE dev — **Effort:** M — **Phase:** 2B

**What:**
- Dashboard có section "Báo cáo đã tạo"
- Click 1 row → mở viewer markdown + nút "Tải PDF"
- Pagination/load-more

**DoD:** flow `tạo report → reload dashboard → thấy trong history → mở lại được`.

---

### LCOS-215 — PDF export cho mọi level từ dashboard
**Owner:** FE dev — **Effort:** S — **Phase:** 2B

**What:** chuyển logic `html2pdf.js` từ `engine-lab.html` sang component dùng chung; gắn vào dashboard report viewer.

**DoD:** user mở report bất kỳ Level nào → click "Tải PDF" → file PDF hợp lệ.

---

## Phase 2C — Ops production

### LCOS-221 — Setup `ALERT_WEBHOOK_URL`
**Owner:** Tech lead + Founder — **Effort:** S — **Phase:** 2C

**What:**
- Tạo Slack incoming webhook (hoặc Discord)
- `wrangler secret put ALERT_WEBHOOK_URL` cho Worker
- Cập nhật `docs/ENV_AND_SECRETS.md`

**DoD:** secret set thành công; verify `wrangler secret list` thấy tên.

---

### LCOS-222 — Alert webhook integration
**Owner:** BE dev — **Effort:** M — **Phase:** 2C

**What:** trong `/api/v1/ops/alert-check`, khi vượt ngưỡng → POST tới `ALERT_WEBHOOK_URL` với payload Slack-format. Ghi `alert_dispatch_logs` (đã có table).

**DoD:** giả lập spike → tin nhắn Slack về.

---

### LCOS-223 — Cron Worker hoặc scheduled GitHub Action
**Owner:** BE dev — **Effort:** S — **Phase:** 2C

**What:** chạy `/api/v1/ops/alert-check` mỗi 15 phút.

**Option A:** Cron trigger trong `wrangler.toml`:
```toml
[triggers]
crons = ["*/15 * * * *"]
```
+ handler `scheduled()` trong Worker.

**Option B:** GitHub Action `schedule:` cron, curl tới endpoint với `MONITOR_KEY`.

**DoD:** chạy ít nhất 4 chu kỳ liên tiếp; log thấy.

---

### LCOS-224 — Backup D1 hằng tuần
**Owner:** BE dev — **Effort:** M — **Phase:** 2C

**What:** workflow `.github/workflows/backup-d1.yml`, cron chủ nhật, chạy `wrangler d1 export life-code-db --remote --output=backup-$(date).sql` → upload R2 hoặc artifact (giữ 4 tuần).

**DoD:** workflow chạy thành công 1 lần thủ công; lịch cron đã set.

---

## Phase 3 — QA production cuối

### LCOS-301 — E2E smoke production tự động
**Owner:** QA dev — **Effort:** M — **Phase:** 3

**What:** mở rộng `scripts/smoke-flow-v1.cjs` thành biến thể `smoke-flow-prod.cjs` trỏ `https://lifecode.iai.one` + `https://life-code-api.tranhatam.workers.dev`. Chạy hằng ngày qua scheduled GitHub Action.

**DoD:** workflow chạy daily; fail → ping Slack.

---

### LCOS-302 — Pen test cơ bản
**Owner:** QA dev — **Effort:** M — **Phase:** 3

**What:**
- SQLi: thử payload kinh điển trên mọi endpoint POST
- XSS: thử reflected/stored vào field profile
- Auth bypass: gọi endpoint cần token mà không có
- Báo cáo trong `docs/SECURITY_REVIEW_2026-04.md`

**DoD:** không lỗi critical; lỗi medium có ticket fix.

---

### LCOS-303 — PII review
**Owner:** Tech lead — **Effort:** S — **Phase:** 3

**What:** đọc `audit_logs` xem có log full name + DoB raw không. Nếu có → hash hoặc cắt.

**DoD:** report `docs/PII_REVIEW_2026-04.md` xác nhận compliance với `ETHICS_GUARDRAILS_V1.md`.

---

### LCOS-304 — Rate-limit production smoke
**Owner:** QA dev — **Effort:** S — **Phase:** 3

**What:** chạy `npm run qa:rate-limit` trỏ vào URL prod (cẩn thận: chỉ test ngoài giờ peak; track rate-limit reset).

**DoD:** pass; không bị block IP do test.

---

### LCOS-305 — Lighthouse Pages mobile ≥ 90
**Owner:** FE dev — **Effort:** M — **Phase:** 3

**What:** chạy Lighthouse mobile cho `index.html`, `bat-dau.html`, `dashboard.html`, fix các issue Performance/Accessibility/Best Practices/SEO.

**DoD:** điểm cả 4 trục ≥ 90 mobile.

---

## Phase 4 — Hậu production (rolling)

- LCOS-401 → LCOS-405: Form input Level 5–9 (mỗi level 1 ticket, owner FE dev, effort M)
- LCOS-411: Đa ngôn ngữ EN cho marketing (FE dev, L)
- LCOS-412: Confidence interval LCI/Timeline (BE + Founder, L)
- LCOS-413: Mobile UI improvements (FE dev, L)

→ Mở khi cần, không block production-ready milestone.

---

## Tổng số ticket

- **Phase 1.5 (Bilingual gate):** 8 tickets (~Tech lead + Editor + SEO + FE × 1 tuần — chặn merge text public)
- Phase 1: 5 tickets (~3 dev × 3 ngày)
- Phase 2A: 4 tickets (~1 FE dev × 1 tuần)
- Phase 2B: 5 tickets (~1 FE + 1 BE × 1 tuần)
- Phase 2C: 4 tickets (~1 BE × 1 tuần)
- Phase 3: 5 tickets (~1 QA + đan xen × 3–4 ngày)
- Phase 4: rolling

**Production-ready estimate:** 3–4 tuần × team (1 FE, 1 BE, 1 QA, 1 Editor + tech lead part-time, founder review). Phase 1.5 chạy song song Tuần 1; Phase 2 mở merge khi 1.5.1–1.5.5 đã merge và `lang-gate` CI active.
