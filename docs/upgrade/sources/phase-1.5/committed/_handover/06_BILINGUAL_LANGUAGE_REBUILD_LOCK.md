# 06 — UNIVERSAL BILINGUAL LANGUAGE REBUILD LOCK

**Status:** Mandatory
**Priority:** Highest
**Scope:** Toàn bộ website Life Code OS đang redev
**Áp dụng cho:** DEV / Content / QA / Design / AI / Codex / CMS / SEO
**Ban hành:** Founder, 2026-04-26
**Hiệu lực:** Ngay lập tức — gate chặn live mọi page

---

## 1. Bối cảnh

Đây là **mệnh lệnh hệ thống** của Founder, đứng **trên kế hoạch hoàn thiện sản phẩm** trong [02_COMPLETION_PLAN.md](./02_COMPLETION_PLAN.md). Mọi page Life Code OS — bao gồm các page đã live `https://lifecode.iai.one` và mọi page sắp ship — phải pass 4-pass review trước khi được live.

Đây **không phải** nhiệm vụ dịch thuật. Đây là **tái cấu trúc toàn bộ hệ ngôn ngữ, SEO và UI text** của website ở cấp production.

## 2. Mệnh lệnh nguyên văn

> Từ thời điểm này, toàn bộ website phải được rà soát, chuẩn hóa, viết lại và kiểm tra lại toàn bộ ngôn ngữ song ngữ theo chuẩn tuyệt đối trước khi được phép live.
>
> Mục tiêu không phải là "dịch lại nội dung". Mục tiêu là tái cấu trúc toàn bộ hệ ngôn ngữ của website để đạt chuẩn:
>
> 1. Tiếng Việt Nam có dấu đầy đủ, chuẩn chính tả, chuẩn văn bản, rõ nghĩa, thống nhất toàn site.
> 2. Tiếng Anh chuẩn Mỹ quốc tế, tự nhiên, rõ ràng, không dịch máy từng chữ, không sai ngữ pháp, không dùng giọng bán hàng rẻ tiền.
> 3. Mỗi ngôn ngữ có metadata SEO riêng, title riêng, description riêng, alt text riêng, URL logic rõ ràng, không dùng chung bừa bãi.
> 4. Mọi chữ trên site phải đi qua một nguồn nội dung chuẩn, không hard-code rải rác trong component, template, script hay CMS không kiểm soát.
> 5. Không được phép live bất kỳ page nào khi còn chữ sai, chữ thiếu dấu, lệch tông, lẫn ngôn ngữ, sai heading, sai CTA, sai menu, sai meta, sai alt text hoặc sai logic song ngữ.

## 3. Phạm vi rà toàn bộ

Mọi lớp text dưới đây của Life Code OS:

- Menu chính, menu phụ, footer, hero
- Section title, paragraph, CTA, button
- Form label, placeholder, empty state, error message
- Badge/status
- Metadata (`<title>`, meta description), OG title, OG description, Twitter metadata
- Schema name/description (JSON-LD)
- Image filename, image alt text, image caption
- Article title, dek, body, related links
- Legal pages (`chinh-sach-bao-mat.html`, `dieu-khoan-su-dung.html`, `ban-quyen-so-huu-tri-tue.html`)
- Trust pages, newsletter, contact
- CMS fields (nếu mở rộng sau)
- Search results text, system notification text

## 4. Nguyên tắc ngôn ngữ

### 4.1 Tiếng Việt
- Có dấu đầy đủ 100%
- Không viết tắt tùy tiện, không slang, không pha giọng quảng cáo
- Câu rõ, ngắn, đúng nghĩa
- Văn phong **hệ thống nghiêm túc**, không như post mạng xã hội
- Một chuẩn thuật ngữ thống nhất từ đầu đến cuối — tham chiếu `docs/GLOSSARY.md`

### 4.2 Tiếng Anh
- Chuẩn Mỹ quốc tế
- Không dịch từng chữ từ Việt
- Không hype, không sales copy yếu, không cấu trúc máy dịch
- Đọc như nội dung do team quốc tế chuyên nghiệp viết
- Giữ đúng nghĩa hệ thống của bản tiếng Việt

### 4.3 Quy tắc song ngữ
- **Việt là bản chuẩn nguồn nội dung.** Anh là ngôn ngữ quốc tế thứ hai.
- Hai bản tương đương về nghĩa, không lệch định vị.
- Không page nào đúng Việt mà yếu Anh, hoặc ngược lại.
- Không trộn Việt + Anh trong cùng block (trừ khi có lý do rõ).
- Không page nào chỉ hoàn chỉnh 1 ngôn ngữ mà live.

## 5. SEO bắt buộc song ngữ

Mỗi page và mỗi bài:

- H1 duy nhất
- `title` riêng theo ngôn ngữ
- `meta description` riêng theo ngôn ngữ
- `canonical` đúng
- `hreflang` đúng nếu có URL song ngữ tách
- OG title/description/image riêng
- Alt text ảnh riêng theo ngôn ngữ
- Internal link đúng ngôn ngữ đang đọc
- Schema đúng loại trang

Cấm:
- Title chung 2 ngôn ngữ
- Description dịch máy
- Thiếu alt text
- URL ngẫu nhiên
- Heading sai cấp
- Bài không có internal link
- Metadata trùng hàng loạt

## 6. Quy tắc kỹ thuật

1. **Nguồn nội dung chuẩn:**
   - `content/vi.json`
   - `content/en.json`
   - Mọi text public render từ 2 file này. Không hard-code public text trong `*.html`, `app.js`, `site.js`, `site-templates/`.

2. **CMS (nếu mở rộng):**
   - Khoá field song ngữ rõ ràng
   - Không cho publish nếu thiếu 1 ngôn ngữ bắt buộc

3. **Route song ngữ:**
   - Phương án A (khuyến nghị): `/vi/...` và `/en/...` — cần config Pages routing.
   - Phương án B (tạm): chưa tách route, nhưng tách metadata, content source, render logic theo ngôn ngữ qua `lang` query/cookie.

4. **Language switcher** phải đưa đúng sang page tương ứng — không reset về home.

## 7. Quy trình thực hiện 7 bước

### Bước 1 — Crawl
Crawl `lifecode.iai.one` + `live-clone/*.html` → xuất:
- Toàn bộ URL
- Mọi text node public
- Metadata
- Image alt
- Form text

→ Output: `_handover/bilingual/01_CRAWL_INVENTORY.csv`

### Bước 2 — Bảng kiểm kê song ngữ

Cột:
- URL
- Page type (marketing / app / legal / form / dashboard)
- Trạng thái VI
- Trạng thái EN
- Lỗi chính tả
- Lỗi ngữ nghĩa
- Lỗi SEO
- Lỗi UI text
- Lỗi metadata
- Lỗi alt text
- Mức ưu tiên sửa (P0/P1/P2)

→ Output: `_handover/bilingual/02_AUDIT_TABLE.csv`

### Bước 3 — Chuẩn hoá Language Codex

`_handover/bilingual/LANGUAGE_CODEX.md` chứa:
- Thuật ngữ khoá (Life Code, LCI, level, timeline, mission code, …) — VI + EN
- Từ cấm (slang, hype, sales rẻ tiền, từ máy dịch điển hình)
- Giọng văn (tone matrix per page type)
- Cấu trúc heading (H1/H2/H3 logic)
- CTA registry
- Form registry
- Error/empty state registry

### Bước 4 — Viết lại theo nguồn chuẩn

- Việt trước → Anh sau
- Đúng role từng page
- Đúng role từng component
- Commit từng page riêng (`docs(content): rebuild VI/EN for <page>`)

### Bước 5 — Rà từng chữ — 4-Pass

| Pass | Owner | Phạm vi |
|---|---|---|
| Pass 1 — AI | AI tool / Codex | Chính tả, dấu, ngữ pháp, lỗi máy dịch |
| Pass 2 — Editor | Human editor | Tone, ngữ nghĩa, định vị thương hiệu |
| Pass 3 — SEO | SEO lead | Title/meta/OG/hreflang/canonical/alt/schema |
| Pass 4 — QA | QA lead | Render thực tế trên cả 2 ngôn ngữ, mobile/desktop |

→ Mỗi page trong `_handover/bilingual/02_AUDIT_TABLE.csv` phải đánh dấu đủ 4 ✅ trước khi gắn label `lang-ready`.

### Bước 6 — Test trước live

- Mobile + desktop
- Metadata + language switcher
- Internal links
- Canonical + hreflang
- Schema (JSON-LD validate)
- Image alt
- Search snippet preview (Google Rich Results test)

### Bước 7 — Gate chặn live

Chỉ được merge PR vào `main` (→ deploy Pages production) khi:

- 100% page public đã pass 4 pass
- Không text sai
- Không thiếu dấu Việt
- Không Anh dịch máy
- Không metadata trùng lỗi
- Không page lệch tông

## 8. Tích hợp vào git workflow

### 8.1 PR label bắt buộc
- `lang-pending` — PR đụng tới text public, chưa pass 4 pass
- `lang-ready` — PR đụng tới text public, đã pass 4 pass (4 reviewer ký)
- `lang-not-applicable` — PR không đụng text public (e.g. chỉ touch engine math, migration)

CI rule: `lang-pending` **không được merge `main`**.

### 8.2 Reviewer mặc định
- AI/Codex: tự động (workflow GitHub Action gọi qua API)
- Editor: 1 human có quyền approve label `lang-pass-2`
- SEO lead: approve `lang-pass-3`
- QA lead: approve `lang-pass-4`

### 8.3 Convention commit
- `content(vi): rebuild homepage hero` — chỉ Việt
- `content(en): rebuild homepage hero` — chỉ Anh
- `content(bi): rebuild homepage hero` — cả 2 cùng PR
- `seo(meta): tách title/description vi+en cho /bat-dau`

## 9. Báo cáo bắt buộc trước khi live

Team nộp **1 báo cáo tổng** `_handover/bilingual/RELEASE_LANGUAGE_REPORT_2026-MM-DD.md` gồm:

1. Tổng số URL đã rà
2. Tổng số page đã sửa
3. Tổng số lỗi tiếng Việt đã sửa
4. Tổng số lỗi tiếng Anh đã sửa
5. Tổng số metadata đã chuẩn hoá
6. Tổng số alt text đã chuẩn hoá
7. Tổng số CTA/form/menu/footer đã chuẩn hoá
8. Danh sách page còn treo (nếu có) + lý do
9. Danh sách quyết định ngôn ngữ quan trọng đã khoá (đặt vào `LANGUAGE_CODEX.md`)
10. Xác nhận cuối:
    - ✅ Đủ chuẩn tiếng Việt
    - ✅ Đủ chuẩn tiếng Anh
    - ✅ Đủ chuẩn SEO
    - ✅ Đủ chuẩn live

Founder ký xác nhận. Khi xác nhận xong → mở permission live cho release.

## 10. Định nghĩa "Hoàn thành ngôn ngữ song ngữ"

Một website chỉ hoàn thành khi:

- Mọi URL public có ngôn ngữ rõ ràng
- Mọi chữ public nằm trong `content/vi.json` + `content/en.json`
- Mọi page đúng chuẩn Việt có dấu
- Mọi page đúng chuẩn Anh Mỹ quốc tế
- Mọi page có SEO song ngữ riêng
- Mọi ảnh có alt text đúng
- Mọi CTA, menu, footer, form đồng nhất
- Không còn text rác / placeholder / hard-code / lẫn ngôn ngữ
- Founder rà ngẫu nhiên page bất kỳ — không thấy lỗi

## 11. Mệnh lệnh cuối

> Không được phép coi đây là một nhiệm vụ dịch thuật.
> Đây là nhiệm vụ tái cấu trúc toàn bộ hệ ngôn ngữ, SEO và UI text của website ở cấp production.
>
> Chỉ khi toàn bộ hệ chữ đã đúng, hệ SEO đã đúng, hệ song ngữ đã đúng, website mới được phép live.

---

## Phụ lục A — Mapping vào kế hoạch hiện tại

| Plan section | Tác động |
|---|---|
| `02_COMPLETION_PLAN.md` Phase 1 | Bổ sung Phase **1.5 — Bilingual Foundation** (xem dưới) |
| `02_COMPLETION_PLAN.md` Phase 2A/2B | Mỗi PR đụng UI/text phải có label `lang-ready` |
| `02_COMPLETION_PLAN.md` Phase 3 | Thêm 4-pass review vào QA cuối; mục "Production-Ready" thêm 4 ✅ ngôn ngữ |
| `03_CLOUDFLARE_DEPLOY_QA_PLAYBOOK.md` | Thêm gate: PR có file `*.html` / `app.js` / `site.js` / `content/*` thay đổi → CI block merge nếu không có label `lang-ready` hoặc `lang-not-applicable` |
| `05_BACKLOG_TICKETS.md` | Thêm phase Language (LCOS-LANG-101…); xem cuối |

## Phụ lục B — Phase 1.5 — Bilingual Foundation (chèn vào Completion Plan)

| # | Task | Owner | DoD |
|---|---|---|---|
| 1.5.1 | Crawl toàn bộ page hiện tại + xuất `01_CRAWL_INVENTORY.csv` | Tech lead | File CSV đầy đủ ≥ 12 trang HTML hiện có |
| 1.5.2 | Lập `02_AUDIT_TABLE.csv` đánh giá VI/EN/SEO/UI per page | Editor + SEO lead | Có cột status đầy đủ, P0/P1/P2 |
| 1.5.3 | Viết `LANGUAGE_CODEX.md` (terms / cấm / tone / heading / CTA / form / error registry) | Editor | Approved bởi Founder |
| 1.5.4 | Khởi tạo `content/vi.json` + `content/en.json` với keys cho navigation + footer + 12 page hero/title/meta | FE dev | Skeleton merge vào `main` |
| 1.5.5 | Refactor 12 HTML page render text từ JSON (loader nhỏ trong `site.js`) | FE dev | Page render đúng, không hard-code text public |
| 1.5.6 | Setup hreflang + canonical per page | FE dev | Validate qua Search Console hoặc dev tool |
| 1.5.7 | CI rule: block merge nếu PR đụng text public mà không có label `lang-ready`/`lang-not-applicable` | Tech lead | Workflow `.github/workflows/lang-gate.yml` |
| 1.5.8 | Setup 4-pass review template (PR template) | Tech lead | `.github/PULL_REQUEST_TEMPLATE.md` có checklist 4-pass |

→ **Đây là phase chặn live.** Phase 2/3 trong Completion Plan vẫn chạy song song, nhưng **không PR nào đụng text public được merge** trước khi 1.5.1 → 1.5.5 hoàn tất.

## Phụ lục C — Backlog ticket bilingual (LCOS-LANG-*)

Xem chi tiết trong [05_BACKLOG_TICKETS.md](./05_BACKLOG_TICKETS.md) — đã được cập nhật.
