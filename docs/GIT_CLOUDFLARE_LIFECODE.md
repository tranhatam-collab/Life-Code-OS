# Kế hoạch Git + Cloudflare cho lifecode.iai.one (Life Code OS)

Ngày cập nhật: 2026-03-31

## 1. Trạng thái hiện tại

| Hạng mục | Trạng thái |
|----------|------------|
| Repo GitHub | `https://github.com/tranhatam-collab/Life-Code-OS` (remote `origin`, nhánh `main`) |
| Nội dung site | Static HTML/CSS/JS ở root repo (đúng mục 28 README — không đưa vào `public/` khi chưa khóa kiến trúc) |
| Build deploy | `npm run build:pages` → thư mục `dist/` (rsync, loại trừ dev/Git/npm) |
| Cloudflare Pages — tên project | `life-code-os` (theo README mục 6.4; Dashboard: Workers & Pages) |
| CI/CD | `.github/workflows/deploy-pages.yml` — push `main` → deploy `dist/` |
| Worker API | `life-code-api` — `workers/life-code-api/`, workflow `deploy-worker.yml` |
| Domain công khai | **lifecode.iai.one** (+ `life-code-os.pages.dev`) |

## 2. Account Cloudflare (đồng bộ các repo iai.one khác)

- **Account ID:** `f3f9e76222dcb488d5e303e29e8ba192`
- Workflow dùng secret **`CF_API_TOKEN`** (Pages Deploy hoặc quyền tương đương: chỉnh sửa Pages + đọc account).

## 3. Việc cần làm một lần trên GitHub

1. Vào **Settings → Secrets and variables → Actions** của repo `Life-Code-OS`.
2. Thêm secret **`CF_API_TOKEN`** = API token Cloudflare (không commit vào git).

## 4. Việc cần làm một lần trên Cloudflare Dashboard

1. **Workers & Pages → Create → Pages** (hoặc để workflow `project create` tạo giúp lần đầu).
2. Đảm bảo project tên **`life-code-os`**, production branch **`main`**.
3. **Custom domains:** **`lifecode.iai.one`** (và tùy chọn `www` nếu cần).
4. Trong **DNS** zone `iai.one`: bản ghi **`lifecode`** trỏ tới target Pages (Cloudflare gợi ý khi attach domain).

### 4b. Cảnh báo "Disconnected from your Git account"

Nếu Dashboard hiện **This project is disconnected from your Git account**:

- **Không chặn** deploy qua **GitHub Actions** + `wrangler pages deploy` + secret `CF_API_TOKEN` (luồng đã cấu hình trong repo).
- Cảnh báo chỉ liên quan **tích hợp Git trực tiếp** trên Cloudflare (build từ repo kết nối trong UI). Bạn có thể **bỏ qua** nếu chỉ dùng Actions, hoặc vào **Settings → Builds** để **Connect** lại GitHub repo `tranhatam-collab/Life-Code-OS` nếu muốn hai luồng (thường chỉ cần một — tránh deploy trùng).

## 5. Luồng Git hằng ngày

```bash
git add -A && git commit -m "..." && git push origin main
```

Sau khi push, Actions build `dist/` và `wrangler pages deploy dist --project-name=life-code-os`.

## 6. Deploy tay từ máy local

```bash
cd "/path/to/Life-Code-OS"
npm install
npm run deploy:pages
```

Cần đăng nhập Wrangler (`wrangler login`) hoặc biến môi trường `CLOUDFLARE_API_TOKEN` + `CLOUDFLARE_ACCOUNT_ID`.

## 7. Dev local (preview Wrangler)

```bash
npm run dev
```

## 8. Domain kỹ thuật (tương lai — Worker / API)

README gốc ghi các hostname dạng `api.life.code.iai.one`. Khi triển khai API thực tế, nên thống nhất một quy ước:

- **Marketing / site tĩnh:** `lifecode.iai.one`
- **API (sau này):** ví dụ `api.lifecode.iai.one` (một cấp subdomain, dễ quản lý DNS hơn `life.code.iai.one`)

Cập nhật README và Worker `wrangler.toml` khi khóa xong tên miền API.

## 9. Kiểm tra sau deploy

```bash
dig lifecode.iai.one +short
curl -sI "https://lifecode.iai.one" | head -5
```

Trên Dashboard Pages: xem deployment mới nhất và trạng thái custom domain (Active / Pending).

## 6. Worker API `life-code-api`

- **Mã nguồn:** `workers/life-code-api/` (`wrangler.toml` + `src/index.js`, engine mirror trong `src/engine.mjs`).
- **Deploy tay:** `npm run deploy:worker` (cần đăng nhập Wrangler hoặc biến `CLOUDFLARE_API_TOKEN`).
- **CI:** `.github/workflows/deploy-worker.yml` — khi push thay đổi trong `workers/life-code-api/**` (hoặc chạy **workflow_dispatch**).
- **URL production:** sau deploy, Dashboard → Workers → `life-code-api` → copy URL dạng `https://life-code-api.<account-subdomain>.workers.dev`. Dán URL đó vào **Engine Lab** (`engine-lab.html`) làm API base. Khi có DNS: route tùy chọn `api.lifecode.iai.one` (khai báo trong `wrangler.toml` hoặc Dashboard).
- **Health:** `GET /health` — kiểm tra nhanh.
- **CORS:** cho phép `https://lifecode.iai.one`, preview `*.life-code-os.pages.dev`, `localhost` / `127.0.0.1` với mọi cổng.
