# Phase 1.5 — Bilingual Foundation — Progress

**Last update:** 2026-04-27
**Owner this pass:** AI agent (foundation pass)
**Next:** Editor / Founder review of Codex; FE dev to roll i18n to remaining 16 pages.

## ✅ Done

### LCOS-LANG-101 — Crawl + inventory
- Script: `scripts/crawl-bilingual-inventory.cjs` (pure Node, no deps)
- Output:
  - `_handover/bilingual/01_CRAWL_INVENTORY.csv` — 1308 text rows × 9 columns
  - `_handover/bilingual/01_CRAWL_INVENTORY.summary.json` — per-page counts
- Auto-flags: `flag_diacritics` (heuristic VI without dấu) + `flag_banned` (hype phrases from Codex)
- Run anytime: `node scripts/crawl-bilingual-inventory.cjs`

### LCOS-LANG-104 — Skeleton content source
- `content/vi.json` and `content/en.json` populated for:
  - `common.*` (brand, taglines, aria labels)
  - `nav.*` (aligned with actual current page strings)
  - `footer.*` (brandLine, exploreHeading, productHeading, legalHeading)
  - `cta.*` (incl. headerStart, switchLanguage)
  - `form.*`, `error.*`, `empty.*`, `notification.*`
  - `pages.index.*` (title, metaDescription, ogTitle, ogDescription, twitterDescription, h1, heroDek) — real strings, not TODO
  - `pages.<other-slug>.*` — still skeleton/TODO awaiting Editor

### LCOS-LANG-105 — i18n loader (pilot)
- Loader: `i18n.js` at root (~6.4 KB, no deps)
- API: `window.LCOS_I18N.{t,lang,switchTo}`
- DOM hooks:
  - `data-i18n="key.path"` → textContent
  - `data-i18n-attr="aria-label:key.path;title:k2"` → multiple attrs
  - `data-i18n-content="key.path"` on `<meta>` → content attr
  - `data-i18n-switch` on `<a>` → click toggles language
- Lang resolution: `?lang=` query → cookie `lcos_lang` → `<html lang>` → fallback `vi`
- `index.html` fully refactored (40 i18n attribute occurrences):
  - `<title>`, `<meta name="description">`, OG, Twitter
  - Brand link + aria-label
  - Menu toggle aria-label
  - Nav (11 links)
  - Header CTA "Bắt đầu"
  - **Language switcher anchor** in header actions (`data-i18n-switch`)
  - Footer brand + 3 column headings + 12 link labels
- Include order in `index.html`: `<script src="./i18n.js">` before `app.js` and `site.js`

### LCOS-LANG-106 — hreflang (pilot scope)
- Added on `index.html` only:
  ```html
  <link rel="alternate" hreflang="vi" href="https://lifecode.iai.one/" />
  <link rel="alternate" hreflang="en" href="https://lifecode.iai.one/?lang=en" />
  <link rel="alternate" hreflang="x-default" href="https://lifecode.iai.one/" />
  ```
- Route choice: **Phương án B** (same URL + `?lang=` query + cookie). Documented in Codex §11.
- 16 other pages: hreflang sweep deferred until each page i18n'd (LCOS-LANG-105 full rollout).

### LCOS-LANG-107 — CI lang-gate
- Workflow: `.github/workflows/lang-gate.yml`
- Trigger: PR touching `*.html`, `app.js`, `site.js`, `content/**`, `site-templates/**`, `sitemap.xml`, `_handover/bilingual/LANGUAGE_CODEX.md`
- Pass: PR has label `lang-ready` or `lang-not-applicable`
- Fail: missing both labels → blocks merge with helpful message

### LCOS-LANG-108 — PR template 4-pass
- File: `.github/PULL_REQUEST_TEMPLATE.md`
- Checklist: Why / What / How to verify / Migration / 4-pass review / label

### Build pipeline hardening
- `scripts/prepare-pages.sh` updated: `--exclude='_handover/'` (internal docs not deployed)

### Production deploy verified
- Deploy `https://fde7db67.life-code-os.pages.dev`
- `lifecode.iai.one/` — 200, 29614 bytes, hreflang correct, 40 data-i18n attrs
- `lifecode.iai.one/i18n.js` — 200, 6433 bytes
- `lifecode.iai.one/content/vi.json` — 200, 9166 bytes
- `lifecode.iai.one/content/en.json` — 200, 8058 bytes
- `lifecode.iai.one/?lang=en` — same HTML served (client-side hydration applies)
- `lifecode.iai.one/_handover/README.md` — falls back to homepage HTML (handover docs NOT served as raw)

## ⏳ Pending — needs Editor / Founder

### LCOS-LANG-102 — Audit table (P0/P1/P2)
- Source CSV ready at `_handover/bilingual/01_CRAWL_INVENTORY.csv`
- Editor + SEO lead review row-by-row, append columns: VI status, EN status, SEO status, UI status, priority
- Output: `_handover/bilingual/02_AUDIT_TABLE.csv`

### LCOS-LANG-103 — Lock Codex
- File: `_handover/bilingual/LANGUAGE_CODEX.md`
- TODO list at end of file:
  - [ ] Confirm 9-level names EN (currently TODO)
  - [ ] Decide route song ngữ — recommended **Phương án B** (already used in pilot); confirm or reject
  - [ ] Add terms for `engine-lab`, `monitor` pages
  - [ ] Founder approve "Codex v1.0"
  - [ ] FE adopts term changes from Codex into JSON

### LCOS-LANG-105 — Full HTML refactor (16 pages)
After Codex locked + Audit table reviewed:
- For each page (`bat-dau`, `dashboard`, `account`, `gioi-thieu`, `he-thong-life-code`, `9-levels-life-code`, `life-code-index`, `timeline-cuoc-doi`, `bao-cao-life-code`, `engine-lab`, `monitor`, `cau-hoi-thuong-gap`, `lien-he`, `chinh-sach-bao-mat`, `dieu-khoan-su-dung`, `ban-quyen-so-huu-tri-tue`, `du-an-life-code`):
  - Populate `pages.<slug>.*` in `vi.json` + `en.json` with real strings (replace TODOs)
  - Add `data-i18n*` attributes mirror of index.html pattern
  - Include `<script src="./i18n.js"></script>` before `site.js`
  - Add hreflang triple per page
  - 4-pass review → label `lang-ready` → merge

### LCOS-LANG-106 — Hreflang sweep (deferred to LANG-105 rollout)
Each page added hreflang at the same time it's i18n'd.

## How team picks up

1. Editor + Founder lock Codex (LANG-103) — review TODOs in `LANGUAGE_CODEX.md`.
2. Editor + SEO lead complete Audit table (LANG-102).
3. FE dev rolls out remaining 16 pages — copy pattern from `index.html`.
4. Each page PR: `lang-pending` → 4-pass → `lang-ready` → merge → CI auto-deploy.

## Quality bar before "Phase 1.5 done"

- [x] Crawl + inventory script + CSV
- [x] CI lang-gate active in repo (after merge)
- [x] PR template active in repo (after merge)
- [x] i18n loader live in production
- [x] Pilot page (`index.html`) fully bilingual
- [ ] Codex v1.0 locked by Founder
- [ ] Audit table P0 issues all green
- [ ] All 17 remaining pages bilingual + hreflang
- [ ] `RELEASE_LANGUAGE_REPORT_2026-MM-DD.md` signed by Founder
