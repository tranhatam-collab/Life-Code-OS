# 03 — Cloudflare Deploy & QA Playbook

**Mục tiêu:** team dev có thể deploy, smoke test, và rollback **trực tiếp trên Cloudflare** mà không cần founder can thiệp.

<a id="local-first-workflow"></a>
## Local-first workflow (workflow chuẩn)

> **Quy tắc Founder:** dev toàn bộ trên máy → test local xanh → commit → deploy thẳng Cloudflare. Không bao giờ debug trên production.

### Vòng dev tiêu chuẩn (mỗi lần đụng code)

```bash
# 1. Sync main + branch
git checkout main && git pull
git checkout -b feat/<slug>

# 2. Run local song song (3 terminal)
npm run worker:dev          # T1 — Worker http://localhost:8787 (D1 local)
npm run dev                 # T2 — Pages http://localhost:8792
# T3 — code

# 3. Sửa code, save → reload trình duyệt → verify visual

# 4. Test local — TẤT CẢ phải xanh trước khi commit
npm run engine:test
npm run report:test
npm run qa:contract
npm run qa:rate-limit
API_BASE=http://localhost:8787 npm run e2e:smoke
```

→ **Bất kỳ test nào fail = KHÔNG commit.** Sửa root cause, không skip test.

### Vòng commit + deploy

```bash
# 5. Commit theo Conventional Commits
git add <files>
git commit -m "feat(<area>): mô tả ngắn"

# 6. Push branch + mở PR
git push -u origin feat/<slug>
# → Mở PR trên GitHub web (hoặc gh CLI sau khi cài)

# 7. CI tự chạy:
#    - .github/workflows/deploy-pages.yml (preview deploy nếu config)
#    - lang-gate.yml (block nếu thiếu lang-ready label)
#    - test workflow (TODO Phase 1)

# 8. Merge PR vào main → CI deploy production tự động:
#    - Pages: lifecode.iai.one cập nhật trong ~2 phút
#    - Worker: life-code-api.tranhatam.workers.dev cập nhật trong ~30s (chỉ khi đụng workers/**)

# 9. Smoke production sau deploy (xem section Smoke test sau deploy)
```

### Fast-path deploy thẳng từ máy (khẩn cấp / preview cá nhân)

Khi cần deploy không qua CI (vd CI đỏ vì lý do hạ tầng, hoặc preview nhanh trước khi merge):

```bash
# Pages
npx wrangler login                   # one-time
npm run build:pages                  # tạo dist/
npm run deploy:preview               # preview URL .pages.dev hash
# hoặc
npm run deploy:pages                 # production (chỉ khi tech lead cho phép)

# Worker
npm run deploy:worker                # production worker
```

⚠️ **Quy tắc fast-path:**
1. Chỉ tech lead/founder dùng deploy production trực tiếp.
2. Sau fast-path **bắt buộc** push code lên `main` ngay để CI và prod đồng bộ.
3. Mọi fast-path log lại trong `_handover/bilingual/DEPLOY_LOG.md` (ngày, người, lý do).
4. Không bao giờ fast-path khi đang có PR `lang-pending` đụng cùng file.

---

## Tài nguyên Cloudflare

| Service | Tên | Vai trò |
|---|---|---|
| Pages project | `life-code-os` | Static site `https://lifecode.iai.one` |
| Workers | `life-code-api` | API `https://life-code-api.tranhatam.workers.dev` |
| D1 | `life-code-db` (id `6bbddd07-…b68d`) | Database persistence |
| Account ID | `f3f9e76222dcb488d5e303e29e8ba192` | Đã hard-code trong `wrangler.toml` và workflows |

## Quy trình deploy chuẩn (qua GitHub Actions)

### Pages (marketing/app)

Trigger: push `main` HOẶC manual `workflow_dispatch`.

```
push main
  → .github/workflows/deploy-pages.yml
    → npm ci
    → npm run build:pages   (= bash scripts/prepare-pages.sh → tạo dist/)
    → wrangler pages deploy dist --project-name=life-code-os --branch=main
```

→ **Production URL:** `https://lifecode.iai.one` cập nhật ngay khi workflow Success.

### Worker API

Trigger: push `main` thay đổi file `workers/life-code-api/**`.

```
push main (paths workers/life-code-api/**)
  → .github/workflows/deploy-worker.yml
    → wrangler deploy --config workers/life-code-api/wrangler.toml
```

→ **Worker URL:** `https://life-code-api.tranhatam.workers.dev` cập nhật ngay khi Success.

> ⚠️ Worker workflow KHÔNG tự chạy migration D1. Migration phải chạy **thủ công** (xem dưới).

## Deploy thủ công (khi cần)

### Pages preview

```bash
cd live-clone
npm ci
npm run deploy:preview   # → wrangler pages deploy dist --branch=preview
```

Preview URL có dạng `https://<hash>.life-code-os.pages.dev` — dùng cho PR review trước khi merge.

### Worker

```bash
cd live-clone
npx wrangler login    # one-time
npm run deploy:worker
```

### D1 migration

```bash
cd live-clone
# Liệt kê migration đã apply
npx wrangler d1 migrations list life-code-db --remote

# Apply migration mới
npx wrangler d1 migrations apply life-code-db --remote

# (Local dev)
npx wrangler d1 migrations apply life-code-db --local
```

→ **Quy tắc:** thêm migration mới vào `workers/life-code-api/migrations/00N_*.sql`, commit, sau đó chạy `migrations apply` thủ công khi PR đã merge và workflow worker đã deploy code mới.

### Secrets Worker

```bash
# Xem list (tên thôi, không thấy giá trị)
npx wrangler secret list --config workers/life-code-api/wrangler.toml

# Set
npx wrangler secret put MONITOR_KEY --config workers/life-code-api/wrangler.toml
npx wrangler secret put ALERT_WEBHOOK_URL --config workers/life-code-api/wrangler.toml
```

## Smoke test sau deploy

### 1. Pages Smoke (5 trang chính)

```bash
for path in / /bat-dau /dashboard /account /monitor; do
  echo "=== $path ==="
  curl -sI "https://lifecode.iai.one${path}" | head -3
done
```

Kỳ vọng: tất cả `HTTP/2 200`.

### 2. Worker API Smoke

```bash
# Health (nếu có) hoặc public endpoint
curl -s https://life-code-api.tranhatam.workers.dev/api/v1/me | head -5

# Submit life-code-data + report flow (script đã có)
cd live-clone
API_BASE=https://life-code-api.tranhatam.workers.dev npm run e2e:smoke
```

### 3. Ops summary (cần MONITOR_KEY)

```bash
curl -s -H "x-monitor-key: $MONITOR_KEY" \
  https://life-code-api.tranhatam.workers.dev/api/v1/ops/summary | jq .
```

### 4. Report render Level 1–9

```bash
for L in 1 2 3 4 5 6 7 8 9; do
  curl -s -X POST https://life-code-api.tranhatam.workers.dev/api/v1/report \
    -H "Content-Type: application/json" \
    -d "{\"level\": $L, \"profile\": {…sample…}}" | head -3
  echo "--- L$L done ---"
done
```

## Quan sát & debug live

### Cloudflare Dashboard

1. **Pages → life-code-os → Deployments** — xem deployment mới nhất, log build.
2. **Workers → life-code-api → Logs (Real-time)** — stream log Worker (chỉ giữ ngắn).
3. **D1 → life-code-db → Console** — chạy SQL truy vấn nhanh.
4. **Workers → life-code-api → Metrics** — request count, error rate, CPU time.

### Wrangler tail (CLI)

```bash
npx wrangler tail --config workers/life-code-api/wrangler.toml
```

Realtime log từ Worker production. Filter theo status:

```bash
npx wrangler tail --config workers/life-code-api/wrangler.toml --status error
```

## Rollback

### Pages

Cloudflare Dashboard → Pages → `life-code-os` → Deployments → chọn deployment cũ → **Rollback to this deployment**.

### Worker

Không có rollback UI; phải:
1. Checkout commit cũ: `git checkout <SHA>`.
2. `npm run deploy:worker`.
3. Quay lại main: `git checkout main`.

→ **Khuyến nghị:** giữ tag git `prod-vN` cho mỗi release để rollback nhanh.

### D1 migration

D1 migration KHÔNG có rollback tự động. Nếu cần revert:
- Viết migration ngược (DROP/RENAME/UPDATE) như migration mới (`00N_revert_X.sql`).
- Apply.

→ **Quy tắc vàng:** mỗi migration phải có **kèm script revert** trong PR description (kể cả khi không apply).

## Chạy local song song production (khuyến khích trước mỗi PR)

```bash
# Terminal 1 — Pages local
cd live-clone
npm run dev   # http://localhost:8792

# Terminal 2 — Worker local + D1 local
cd live-clone
npm run worker:dev   # http://localhost:8787 (Wrangler default)

# Terminal 3 — Smoke
API_BASE=http://localhost:8787 npm run e2e:smoke
```

`engine-lab.html` mặc định trỏ Worker production; sửa env hoặc query string để trỏ local khi test.

## Checklist trước khi merge PR

```
[ ] CI Pages workflow xanh
[ ] CI Worker workflow xanh (nếu PR động vào workers/)
[ ] CI lang-gate.yml xanh (Phase 1.5)
[ ] Local: npm run engine:test pass
[ ] Local: npm run report:test pass
[ ] Local: npm run e2e:smoke pass (API_BASE=http://localhost:8787)
[ ] Local: npm run qa:contract pass
[ ] Local: npm run qa:rate-limit pass
[ ] Manual smoke trên preview URL Pages (xem deploy:preview)
[ ] Migration D1 (nếu có) đã có script revert kèm PR description
[ ] Tăng/sửa test cho code mới
[ ] Cập nhật docs/API_REFERENCE.md nếu thay đổi endpoint
[ ] PR đụng text public → label lang-ready (4-pass review xong) — xem 06_BILINGUAL_LANGUAGE_REBUILD_LOCK.md
[ ] PR không đụng text public → label lang-not-applicable
```

## Checklist sau khi merge PR vào main

```
[ ] Pages workflow Success (https://github.com/tranhatam-collab/Life-Code-OS/actions)
[ ] Worker workflow Success (nếu trigger)
[ ] Smoke production: curl 5 trang chính
[ ] e2e:smoke trỏ vào URL production pass
[ ] Nếu có migration: chạy `wrangler d1 migrations apply --remote`
[ ] Verify Cloudflare dashboard không có error spike trong 15 phút sau deploy
```
