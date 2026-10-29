# Language Codex — Life Code OS

**Status:** Skeleton — chờ Editor + Founder điền và khoá
**Áp dụng cho:** Mọi text public của Life Code OS (12 page hiện tại + page mới)
**Cập nhật:** 2026-04-26

> **Quy tắc Founder:** không ai (dev / content / QA) được tạo thuật ngữ mới ngoài Codex này. Mọi đề xuất term mới → mở PR sửa Codex → Founder approve → áp dụng.

## 1. Term registry (khoá thuật ngữ song ngữ)

| Khái niệm | Tiếng Việt | Tiếng Anh | Ghi chú |
|---|---|---|---|
| Tên hệ thống | Life Code OS | Life Code OS | Giữ nguyên không dịch |
| Chỉ số tổng hợp | Chỉ số Life Code (LCI) | Life Code Index (LCI) | Viết tắt LCI dùng chung 2 ngôn ngữ |
| 9 cấp độ | 9 cấp độ Life Code | 9 levels of Life Code | Đặt số trước, không "level 9" mà "cấp 9" trong VI |
| Cấp 1 | Tín hiệu Bản thân | Self Signal | TODO confirm |
| Cấp 2 | Kiến trúc Nội tâm | Inner Architecture | TODO confirm |
| Cấp 3 | Mã Hành vi | Behavior Code | TODO confirm |
| Cấp 4 | Mã Công việc và Tài chính | Work and Wealth Code | TODO confirm |
| Cấp 5 | Trường Quan hệ | Relationship Field | TODO confirm |
| Cấp 6 | Dòng thời gian Cuộc đời | Life Timeline | TODO confirm |
| Cấp 7 | Trí tuệ Cơ thể | Body Intelligence | TODO confirm |
| Cấp 8 | Đường Sứ mệnh | Mission Path | TODO confirm |
| Cấp 9 | Báo cáo Life Code Đầy đủ | Full Life Code Report | TODO confirm |
| Báo cáo | Báo cáo | Report | Không "report" trong VI |
| Hồ sơ | Hồ sơ | Profile | |
| Phiên đăng nhập | Phiên | Session | Không "session" trong VI |
| Bảng điều khiển | Bảng điều khiển | Dashboard | Không "dashboard" trong VI |
| Tài khoản | Tài khoản | Account | |
| Bắt đầu | Bắt đầu | Get Started | CTA chuẩn |

> Editor: bổ sung mọi thuật ngữ xuất hiện trong app. Founder approve trước khi khoá.

## 2. Banned words

### VI cấm
- Slang: "ngon", "đỉnh", "chất", "cực mạnh", "xịn xò"
- Hype: "thay đổi cuộc đời chỉ trong 5 phút", "miễn phí 100%", "giải mã"
- Sales rẻ tiền: "ưu đãi sốc", "đăng ký ngay kẻo lỡ"
- Sai dấu / không dấu: "bao cao", "ho so", "tai khoan" — phải có dấu
- Viết tắt tuỳ tiện: "k thể", "đc", "ko", "cmt"
- Cảm thán: "wow", "ohhh", "yay"

### EN cấm
- Hype: "life-changing in just 5 minutes", "100% free", "decode your life"
- Buzzword rỗng: "synergy", "unlock your potential", "next-level"
- Sales weak: "sign up now", "limited time", "don't miss out"
- Cấu trúc máy dịch: "to make sure that you can…", "in order to…"
- Slang: "awesome", "cool stuff", "you got this"
- Casual lower-case: "hey there", "yo"

## 3. Tone matrix

| Page type | VI tone | EN tone |
|---|---|---|
| Marketing (`index`, `gioi-thieu`, `he-thong-life-code`, `du-an-life-code`, `9-levels`) | Hệ thống — rõ — không hype | Authoritative, calm, system-grade |
| App (`bat-dau`, `dashboard`, `account`, `engine-lab`, `monitor`) | Thực dụng — ngắn — chỉ thị rõ | Functional, concise, instructional |
| Legal (`chinh-sach-bao-mat`, `dieu-khoan-su-dung`, `ban-quyen`) | Trang trọng, đúng pháp lý VN | Standard legal English (US), không AmLaw nặng |
| Form / error / empty state | Bình tĩnh, hướng dẫn cụ thể | Calm, actionable |
| Notification system | Ngắn, không cảm thán | Brief, non-emotional |

## 4. Heading hierarchy

- `H1`: 1 duy nhất per page, là chủ đề chính. Không trùng với `<title>` 100% (title có thể chứa thương hiệu).
- `H2`: section chính (3–6 H2 / page).
- `H3`: subsection (chỉ khi H2 quá dài).
- `H4+`: hạn chế. Nếu cần → cân nhắc tách section.

Cấm:
- Nhiều H1
- Skip cấp (H2 → H4)
- Heading rỗng / chỉ chứa CTA

## 5. CTA registry

| Slot | VI | EN |
|---|---|---|
| Primary marketing | "Bắt đầu Life Code" | "Start your Life Code" |
| Secondary marketing | "Tìm hiểu hệ thống" | "Explore the system" |
| Form submit (bat-dau) | "Tạo báo cáo" | "Generate report" |
| Login / start session | "Đăng nhập" | "Sign in" |
| Logout | "Đăng xuất" | "Sign out" |
| Save profile | "Lưu thay đổi" | "Save changes" |
| Cancel | "Huỷ" | "Cancel" |
| Download PDF | "Tải PDF" | "Download PDF" |
| View report | "Mở báo cáo" | "Open report" |
| Re-run engine | "Chạy lại Engine" | "Re-run engine" |
| Revoke session | "Thu hồi phiên" | "Revoke session" |

> Editor + FE dev đồng bộ với key trong `content/vi.json` `cta.*` và `content/en.json` `cta.*`.

## 6. Form registry

| Field | VI label | VI placeholder | EN label | EN placeholder |
|---|---|---|---|---|
| Họ tên | Họ và tên | Họ và tên đầy đủ | Full name | Your full name |
| Ngày sinh | Ngày sinh | dd/mm/yyyy | Date of birth | mm/dd/yyyy |
| Giờ sinh | Giờ sinh (nếu nhớ) | hh:mm | Time of birth (if known) | hh:mm |
| Nơi sinh | Nơi sinh | Tỉnh / thành phố / quốc gia | Place of birth | City, country |
| Email | Email | ban@vidu.com | Email | you@example.com |
| Mật khẩu | Mật khẩu | Tối thiểu 12 ký tự | Password | Minimum 12 characters |

> Mở rộng khi thêm input level 2–9 (xem ticket LCOS-201, 202, 203).

## 7. Error / empty state registry

| Trạng thái | VI | EN |
|---|---|---|
| Network error | "Mất kết nối. Vui lòng thử lại." | "Connection lost. Please try again." |
| Validation thiếu trường | "Vui lòng điền đầy đủ thông tin bắt buộc." | "Please complete the required fields." |
| Rate limit | "Bạn đang thao tác quá nhanh. Hãy đợi vài giây." | "Too many requests. Please wait a moment." |
| Empty history | "Chưa có báo cáo nào. Hãy tạo báo cáo đầu tiên ở mục Bắt đầu." | "No reports yet. Create your first one from Start." |
| Profile incomplete (gate level cao) | "Cần hoàn thiện hồ sơ Cấp <N> để mở báo cáo này." | "Complete your Level <N> profile to open this report." |
| 404 page | "Không tìm thấy trang." | "Page not found." |
| 5xx | "Hệ thống đang gặp sự cố. Đội ngũ đã được thông báo." | "Service is temporarily unavailable. Our team has been notified." |

## 8. Notification system registry

| Sự kiện | VI | EN |
|---|---|---|
| Lưu hồ sơ thành công | "Đã lưu thay đổi." | "Changes saved." |
| Tạo báo cáo thành công | "Báo cáo đã sẵn sàng." | "Report ready." |
| Phiên hết hạn | "Phiên đăng nhập đã hết hạn. Vui lòng đăng nhập lại." | "Your session has expired. Please sign in again." |
| Webhook alert (internal) | "[ALERT] <metric> vượt ngưỡng <threshold>." | "[ALERT] <metric> exceeded threshold <threshold>." |

## 9. SEO snippet rules

- VI title: `<H1 page> — Life Code OS` (≤ 60 ký tự)
- EN title: `<H1 page> — Life Code OS` (≤ 60 chars)
- Meta description: 130–155 ký tự, không trùng giữa các page, không kết câu bằng dấu chấm than.
- OG image: bắt buộc 1200×630 PNG, không text dày, riêng cho VI/EN nếu khác.

## 10. Quy tắc chốt thuật ngữ

1. Mọi đề xuất term mới mở PR sửa Codex.
2. Founder approve.
3. FE dev cập nhật `content/vi.json` + `content/en.json` cùng PR.
4. CI lang-gate kiểm tra: nếu PR thêm key vào `content/*.json` mà không kèm Codex update → fail.

## 11. TODO Editor + Founder

- [ ] Confirm tên 9 levels EN (đang TODO ở mục 1)
- [ ] Bổ sung term cho `engine-lab`, `monitor`
- [ ] Validate banned-words list với marketing team
- [ ] Decide route song ngữ: A (`/vi/...` `/en/...`) hay B (query/cookie) — quyết định ảnh hưởng LCOS-LANG-105 + LCOS-LANG-106
- [ ] Khoá Codex v1.0 trước khi merge LANG-104
