# 04 — Dev Onboarding

**Đối tượng:** dev mới join Life Code OS — đọc 15 phút là code được.

## Trước khi bắt đầu

Yêu cầu:
- Node.js ≥ 20.x
- npm
- Git
- (Tuỳ chọn) Cloudflare account để deploy preview

Quyền cần xin tech lead:
- Write access GitHub repo `tranhatam-collab/Life-Code-OS`
- (Sau khi pass review đầu) thêm vào Cloudflare team `life-code-os` Pages + `life-code-api` Worker

## Setup local

```bash
# 1. Clone (nếu chưa)
git clone https://github.com/tranhatam-collab/Life-Code-OS.git
cd Life-Code-OS

# 2. Install
npm ci

# 3. Build Pages dist
npm run build:pages

# 4. Test engine
npm run engine:test
npm run engine:sample

# 5. Test report
npm run report:test
```

Tất cả script trên phải pass trước khi commit gì đó. Nếu fail → ping tech lead, đừng force commit.

## Chạy site local

```bash
# Pages dev (Wrangler local server cho dist/)
npm run dev
# → http://localhost:8792
```

Để Worker chạy song song:

```bash
# Terminal 2
npm run worker:dev
# → http://localhost:8787
```

`engine-lab.html` cho phép test engine + report local. Mặc định trỏ Worker production — đổi `apiBase` trong query string hoặc localStorage để trỏ `http://localhost:8787`.

## Cấu trúc thư mục cần biết

```
.
├── *.html                  → trang Pages (route `/<filename>`)
├── style.css, site.js      → asset chung
├── app.js                  → logic chung (engine call, localStorage)
├── api/server.cjs          → Express dev server (chỉ local fallback, không deploy)
├── workers/life-code-api/  → Worker production
│   ├── src/index.js        → router
│   ├── src/engine.mjs      → engine
│   ├── src/report.mjs      → report renderer
│   └── migrations/         → D1 schema
├── engine/                 → engine library node-side (test + build data)
├── docs/                   → spec, contract, formulas
├── docs/report-templates/  → markdown template Level 1–9
├── scripts/                → CI helpers, smoke tests
├── site-templates/         → template render report (engine-lab dùng)
└── .github/workflows/      → CI deploy
```

## Git flow

Branch: `phaseN/<slug>` hoặc `feat/<slug>` hoặc `fix/<slug>` hoặc `docs/<slug>`.

```bash
git checkout main
git pull origin main
git checkout -b phase-2/save-report-history

# … làm việc, commit từng phần
git add <file>
git commit -m "feat(report): save rendered report to D1"

git push -u origin phase-2/save-report-history
gh pr create --base main
```

Commit convention (Conventional Commits):
- `feat(area): …` — tính năng mới
- `fix(area): …` — bug fix
- `chore(area): …` — refactor, dependencies, không thay đổi behavior
- `docs(area): …` — chỉ doc
- `test(area): …` — chỉ test
- `ops(area): …` — CI, infra, deploy

`area` ví dụ: `report`, `engine`, `worker`, `pages`, `monitor`, `ops`, `qa`.

## Test trước khi push

```bash
npm run engine:test      # engine smoke (CJS)
npm run report:test      # report smoke (Worker tests)
npm run qa:contract      # API contract hardening
npm run qa:rate-limit    # rate-limit smoke
npm run e2e:smoke        # bat-dau → D1 → dashboard → report
```

Tất cả phải xanh.

## PR rules

- 1 PR = 1 task. Đừng gộp.
- PR description bắt buộc:
  - **Why** (vấn đề / mục tiêu)
  - **What** (thay đổi chính)
  - **How to verify** (command / URL preview)
  - **Migration?** (Y/N — nếu Y kèm revert script)
- Reviewer: tech lead (mặc định). Founder review nếu thay đổi spec/formula.
- CI bắt buộc xanh.
- Squash merge.

## Khi có conflict với main

```bash
git checkout main && git pull
git checkout phase-2/...
git rebase main
# resolve conflict
git push --force-with-lease   # ⚠️ chỉ trên branch của bạn, KHÔNG main
```

## Cấm và cảnh báo

- ❌ KHÔNG push trực tiếp `main`. Luôn qua PR.
- ❌ KHÔNG commit `node_modules/`, `dist/`, `.wrangler/`, `.env*`.
- ❌ KHÔNG hard-code secret/token. Dùng `wrangler secret`.
- ❌ KHÔNG sửa `wrangler.toml` `database_id`/`account_id` mà không hỏi tech lead.
- ⚠️ Migration D1 **không tự rollback** — luôn kèm revert.
- ⚠️ Worker route production cần Cloudflare Zone access — chỉ founder/tech lead set.

## Checklist onboarding (dev mới)

```
[ ] Đọc README.md (root)
[ ] Đọc PROJECT_STATUS_MASTER.md
[ ] Đọc _handover/01_PROJECT_AUDIT.md
[ ] Đọc _handover/02_COMPLETION_PLAN.md
[ ] Đọc _handover/03_CLOUDFLARE_DEPLOY_QA_PLAYBOOK.md
[ ] Đọc docs/GLOSSARY.md
[ ] Setup local, chạy npm run e2e:smoke pass
[ ] Mở 1 PR docs nhỏ (ví dụ thêm 1 dòng vào CONTRIBUTING.md) để test toàn bộ flow
[ ] Pick ticket trong _handover/05_BACKLOG_TICKETS.md
```

## Kênh hỏi đáp

- Tech lead: …
- Slack channel: … (TODO)
- Founder: …
