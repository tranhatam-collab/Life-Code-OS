# Life Code OS — Team Dev Handover

**Tạo:** 2026-04-26
**Repo gốc:** https://github.com/tranhatam-collab/Life-Code-OS
**Live site:** https://lifecode.iai.one
**Cloudflare Pages project:** `life-code-os` → `life-code-os.pages.dev`
**Worker API:** `life-code-api` → `https://life-code-api.tranhatam.workers.dev`
**D1 database:** `life-code-db` (id `6bbddd07-a644-486b-bc66-a6e35b46b68d`)

## Mục đích

Folder `Life-Code-OS-team-dev/` là **không gian làm việc của team dev**. Bao gồm:

| Thư mục | Vai trò |
|---|---|
| `live-clone/` | Bản clone tươi từ GitHub `main` (HEAD `99b4027`). Đây là **nguồn truth** team dev sẽ checkout, branch và PR từ. |
| `_handover/` | Bộ tài liệu bàn giao: diff report, audit, kế hoạch hoàn thiện, playbook Cloudflare, backlog. |

Bản local cũ `~/Documents/Devnewproject/Life-Code-OS/` **giữ nguyên** làm bản nháp cá nhân (founder), không dùng cho team.

## Index tài liệu handover

1. [00 — Live vs Local Diff Report](./00_LIVE_VS_LOCAL_DIFF_REPORT.md) — đối chiếu GitHub vs bản trên máy.
2. [01 — Project Audit](./01_PROJECT_AUDIT.md) — kiểm kê cấu trúc, % hoàn thành, lỗ hổng.
3. [02 — Completion Plan](./02_COMPLETION_PLAN.md) — kế hoạch khép phần ~8–15% còn lại theo phase (đã chèn Phase 1.5 Bilingual).
4. [03 — Cloudflare Deploy & QA Playbook](./03_CLOUDFLARE_DEPLOY_QA_PLAYBOOK.md) — quy trình **dev local-first → deploy thẳng Cloudflare**.
5. [04 — Dev Onboarding](./04_DEV_ONBOARDING.md) — hướng dẫn dev mới setup, branch, PR.
6. [05 — Backlog Tickets](./05_BACKLOG_TICKETS.md) — danh sách ticket sẵn sàng nhận (gồm 8 ticket LCOS-LANG-* gate live).
7. [06 — Bilingual Language Rebuild Lock](./06_BILINGUAL_LANGUAGE_REBUILD_LOCK.md) — **MANDATORY HIGHEST PRIORITY** — gate chặn live mọi page text public.
8. [bilingual/LANGUAGE_CODEX.md](./bilingual/LANGUAGE_CODEX.md) — codex skeleton (term / banned / tone / heading / CTA / form / error registry) chờ Editor + Founder khoá.

## Skeleton content source (đã tạo trong `live-clone/`)

- `live-clone/content/vi.json` — keys nav/footer/cta/form/error/empty/notification + 18 page metadata (heroDek/title/metaDescription/ogTitle/ogDescription/h1)
- `live-clone/content/en.json` — mirror EN, đã viết draft tone chuẩn Mỹ quốc tế cho phần fixed; phần `pages.*` còn TODO chờ Editor.

→ Đây là **2 file duy nhất** chứa text public sau Phase 1.5. FE dev refactor HTML theo `data-i18n="key.path"` để loader trong `site.js` thay text.

## Workflow chuẩn (Founder lock)

> **Dev toàn bộ trên máy → test local xanh → commit → deploy thẳng Cloudflare.**

1. Code trên `live-clone/` với 2 server local: `npm run worker:dev` (Worker + D1 local) + `npm run dev` (Pages).
2. Chạy đủ test: `engine:test`, `report:test`, `qa:contract`, `qa:rate-limit`, `e2e:smoke` — **tất cả phải xanh** trước khi commit.
3. `git push` → CI GitHub Actions auto-deploy: Pages → `lifecode.iai.one` (~2 phút), Worker → `life-code-api.tranhatam.workers.dev` (~30s).
4. Fast-path (khẩn cấp): `npm run deploy:pages` / `npm run deploy:worker` thẳng từ máy, ghi log `_handover/bilingual/DEPLOY_LOG.md`.
5. **Gate chặn live:** PR đụng text public phải pass 4-pass review (Bilingual Lock §06) — thiếu label `lang-ready` → CI fail.

## Tóm tắt nhanh

- **Trục A (hạ tầng + CI deploy):** 100% — push `main` tự động deploy Pages + Worker.
- **Trục B (sản phẩm):** ~85–95% — còn polish profile CRUD, report production, level 2–9 input chi tiết, E2E QA mở rộng, webhook alert production.
- **Phase 1.5 (Bilingual gate):** 8 ticket LCOS-LANG-* — bắt buộc trước khi mở merge cho text public.
- **Khối lượng còn lại:** 3–4 tuần × team (1 FE, 1 BE, 1 QA, 1 Editor + tech lead part-time, founder review).
