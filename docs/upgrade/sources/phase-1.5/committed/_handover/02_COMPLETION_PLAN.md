# 02 — Completion Plan

**Mục tiêu:** đóng phần **~8–15% còn lại** để Life Code OS production-ready và bàn giao stable cho team vận hành.

**Phương châm:** **dev local-first** → small commits → test local xanh (`engine:test` + `report:test` + `qa:contract` + `qa:rate-limit` + `e2e:smoke`) → push `main` → **deploy thẳng Cloudflare** Pages + Worker tự động qua GitHub Actions. Khi cần fast-path khẩn cấp, dùng `npm run deploy:pages` / `npm run deploy:worker` từ máy (xem [03 — Playbook §Local-first](./03_CLOUDFLARE_DEPLOY_QA_PLAYBOOK.md#local-first-workflow)).

**Gate chặn live (BẮT BUỘC):** mọi PR đụng text public phải pass 4-pass review theo [06 — Bilingual Lock](./06_BILINGUAL_LANGUAGE_REBUILD_LOCK.md). Phase 1.5 dưới đây là tiền đề cho Phase 2/3.

## Phase 0 — Chuẩn bị (Day 1, founder + tech lead)

| # | Task | Owner | DoD |
|---|---|---|---|
| 0.1 | Founder cấp quyền GitHub repo cho team dev | Founder | Team có write access |
| 0.2 | Founder share `CF_API_TOKEN` scope (đã ở GitHub Secrets, không cần share token thật) | Founder | CI vẫn deploy Pages + Worker được |
| 0.3 | Tech lead chạy thử local `npm ci && npm run worker:dev` | Tech lead | Worker chạy local, gọi được `/api/v1/me` |
| 0.4 | Tech lead chạy `npm run e2e:smoke` | Tech lead | Pass |
| 0.5 | Tech lead viết `docs/LOCAL_DEV.md` | Tech lead | PR merged |

## Phase 1.5 — Bilingual Foundation (BẮT BUỘC, song song Tuần 1)

> **Đây là gate chặn live.** Không page text public được merge vào `main` trước khi 1.5.1 → 1.5.5 hoàn tất + CI gate active. Chi tiết trong [06 — Bilingual Lock](./06_BILINGUAL_LANGUAGE_REBUILD_LOCK.md) Phụ lục B.

| # | Task | Owner | DoD |
|---|---|---|---|
| 1.5.1 | Crawl 12 page hiện tại + xuất `_handover/bilingual/01_CRAWL_INVENTORY.csv` | Tech lead | CSV liệt kê đủ URL + text node + metadata + alt |
| 1.5.2 | Lập `_handover/bilingual/02_AUDIT_TABLE.csv` đánh giá VI/EN/SEO/UI per page (P0/P1/P2) | Editor + SEO lead | Có cột status đầy đủ |
| 1.5.3 | Viết `_handover/bilingual/LANGUAGE_CODEX.md` (terms / cấm / tone / heading / CTA / form / error registry) | Editor | Founder approved |
| 1.5.4 | Khởi tạo `content/vi.json` + `content/en.json` (skeleton nav + footer + 12 page hero/title/meta) | FE dev | Merge `main` |
| 1.5.5 | Refactor 12 HTML page render text từ JSON (loader nhỏ trong `site.js`) | FE dev | Page render đúng, không hard-code text public |
| 1.5.6 | Setup hreflang + canonical per page | FE dev | Validate qua Google Rich Results / dev tool |
| 1.5.7 | CI rule `.github/workflows/lang-gate.yml` block merge nếu PR đụng text public mà thiếu label `lang-ready`/`lang-not-applicable` | Tech lead | Workflow chạy, fail expected case |
| 1.5.8 | Setup `.github/PULL_REQUEST_TEMPLATE.md` có checklist 4-pass | Tech lead | Mọi PR mới có template |

→ Hoàn tất Phase 1.5 trước khi mở merge cho Phase 2A (PR đụng UI level 2/3/4).

## Phase 1 — Tài liệu nền cho dev (Tuần 1)

| # | Task | Owner | DoD |
|---|---|---|---|
| 1.1 | `docs/API_REFERENCE.md` — list đầy đủ endpoints với request/response, error codes | BE dev | PR merged + check toàn bộ endpoint khớp `src/index.js` |
| 1.2 | `docs/ENV_AND_SECRETS.md` — biến môi trường, secret, scope | BE dev | PR merged |
| 1.3 | `docs/TESTING.md` — cách chạy test suite (smoke, contract, rate-limit, e2e) | QA dev | PR merged + CI pass |
| 1.4 | `CONTRIBUTING.md` — git flow, commit convention (feat/fix/chore/docs), review SLA | Tech lead | PR merged |
| 1.5 | `docs/RELEASE_RUNBOOK.md` — flow release từ branch → main → production smoke | Tech lead | PR merged |
| 1.6 | Cập nhật `README.md` thêm link tới các doc trên | Tech lead | PR merged |

## Phase 2 — Đóng các lỗ hổng sản phẩm (Tuần 2)

### 2A — Profile & Input (FE dev)

| # | Task | DoD |
|---|---|---|
| 2A.1 | Form input Level 2 (Inner Architecture) trong `bat-dau.html` hoặc `account.html` | User có thể submit, dữ liệu lưu D1, render report Level 2 dùng dữ liệu thật (không dùng suy luận từ Level 1). |
| 2A.2 | Tương tự cho Level 3 (Behavior Code) | Như trên |
| 2A.3 | Tương tự Level 4 (Work/Wealth) | Như trên |
| 2A.4 | Profile completeness **gate** — disable nút "Mở report level X" khi completeness < ngưỡng | UX rõ ràng, không 500 khi thiếu data |

> Level 5–9 có thể đẩy sang Phase 4 (sau production milestone).

### 2B — Report production polish (FE + BE)

| # | Task | DoD |
|---|---|---|
| 2B.1 | Lưu report đã render vào D1 (`report_renders` table, migration mới) | Mỗi lần render có row mới với `user_id`, `level`, `markdown`, `created_at` |
| 2B.2 | Dashboard hiển thị **report history** (mở report cũ) | UI list, click mở lại |
| 2B.3 | PDF export cho **mọi level** (không chỉ engine-lab) | Nút "Tải PDF" trên dashboard render report |

### 2C — Ops production (BE + QA)

| # | Task | DoD |
|---|---|---|
| 2C.1 | Setup `ALERT_WEBHOOK_URL` (Slack incoming webhook hoặc Discord) | `wrangler secret put ALERT_WEBHOOK_URL` xong |
| 2C.2 | `alert-check` thực sự POST tới webhook khi vượt ngưỡng | Test giả lập spike → nhận alert Slack |
| 2C.3 | Cron Worker hoặc GitHub Action scheduled `*/15 * * * *` gọi `/api/v1/ops/alert-check` | Run trong production |
| 2C.4 | Backup D1 hằng tuần (`wrangler d1 export`) → upload R2 hoặc artifact | Workflow `.github/workflows/backup-d1.yml` |

## Phase 3 — QA production cuối (Tuần 3, đầu)

| # | Task | DoD |
|---|---|---|
| 3.1 | E2E smoke production (`https://lifecode.iai.one`) — script tự động (Playwright hoặc curl-based) | Pass trên CI và chạy được local |
| 3.2 | Pen test cơ bản: SQLi/XSS cho mọi endpoint public | Báo cáo, không lỗi critical |
| 3.3 | PII review: audit log không log data nhạy cảm (full name + ngày sinh) | Sửa nếu có |
| 3.4 | Kiểm tra rate-limit production thực tế (chạy `qa:rate-limit` trỏ vào URL prod) | Pass + log không lỗi |
| 3.5 | Lighthouse Pages ≥ 90 mobile cho `index.html`, `bat-dau.html`, `dashboard.html` | Pass |

## Phase 4 — Hậu production (Tuần 3, sau)

| # | Task | Note |
|---|---|---|
| 4.1 | Form input Level 5–9 chi tiết | Có thể song song với marketing |
| 4.2 | Đa ngôn ngữ — EN tối thiểu cho marketing | Sau khi product team chốt copy EN |
| 4.3 | Confidence interval cho LCI và Timeline | Cần data thực tế để calibrate |
| 4.4 | Mobile-only UI improvements | Trên feedback user thật |

## Tổng quan timeline

```
Tuần 1: Phase 0 (Day 1) + Phase 1 docs
Tuần 2: Phase 2A + 2B + 2C song song (3 dev)
Tuần 3 đầu: Phase 3 QA cuối → release production-ready
Tuần 3 sau: Phase 4 hậu production (rolling)
```

→ ~3 tuần để **đóng dứt điểm** Trục B core. Phase 4 chạy rolling.

## Tiêu chí "Production-Ready"

✅ Tất cả Phase 1, 1.5, 2, 3 hoàn tất.
✅ **Phase 1.5 Bilingual:** mọi page public đã pass 4-pass review (`lang-ready`); báo cáo `RELEASE_LANGUAGE_REPORT_2026-MM-DD.md` ký bởi Founder.
✅ E2E smoke production pass tự động hằng ngày qua scheduled workflow.
✅ Webhook alert active, có ít nhất 1 lần test ngưỡng vượt thành công.
✅ Backup D1 đã chạy ít nhất 2 chu kỳ (1 thủ công + 1 cron).
✅ `PROJECT_STATUS_MASTER.md` cập nhật Trục B = 100%.

## Cách team dev nhận task

- Mỗi task ở Phase 1–3 được mở thành **GitHub Issue** với label `phase-1`, `phase-2`, `phase-3`.
- Branch convention: `phaseN/<short-slug>` (ví dụ `phase-2/save-report-history`).
- PR title format: `feat(area): mô tả ngắn` hoặc `fix(area): …`, `docs(area): …`.
- Mỗi PR: 1 reviewer (tech lead), CI xanh, smoke test pass.

## Backlog ticket sẵn

Xem [05 — Backlog Tickets](./05_BACKLOG_TICKETS.md) để có danh sách ticket đầy đủ kèm description.
