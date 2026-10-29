# Runbook migration D1 → PostgreSQL v2.1

Ngày bổ sung: **2026-10-20**  
Trạng thái: **PLAN_ONLY / DATA_OWNER_AND_SECURITY_APPROVAL_PENDING / NOT_RUN**

## 1. Source receipt đã khóa

Baseline code được dùng để lập plan: `99b402764437f81859fa0cd3a3af860125f7bd52`. Sáu bảng D1 nhìn thấy trong migration source:

1. `user_profiles`
2. `life_code_results`
3. `user_sessions`
4. `rate_limits`
5. `account_audit_logs`
6. `alert_dispatch_logs`

Receipt code: `workers/life-code-api/migrations/001_create_tables.sql` đến `006_alert_dispatch_logs.sql` tại baseline trên. Đây không phải receipt row-count, quyền sở hữu, DB runtime hoặc backup. Không có truy vấn production nào được chạy trong lúc soạn tài liệu này.

## 2. Quyết định theo từng bảng

`MIGRATION_RECONCILIATION_MATRIX.csv` là matrix canonical. Nguyên tắc:

- `user_profiles`: chỉ vào quarantine/raw landing trước. Tên/ngày sinh không chứng minh account owner. Sau verification mới tạo `profile_subject` + immutable `profile_version`.
- `life_code_results`: giữ nguyên payload/hash như historical legacy artifact; mọi LCI/risk/wealth/mission/timeline suy diễn gắn `experimental_legacy`, không nâng thành fact/metric/method result v2.
- `user_sessions`: không migrate token. Revoke/expire toàn bộ theo containment receipt; nếu cần audit chỉ migrate metadata tối thiểu đã review, không token plaintext.
- `rate_limits`: không phải business record; khởi tạo mới theo cutover policy, không copy counter để giả continuity.
- `account_audit_logs`: chỉ map sang audit store sau privacy classification, minimization và identity reconciliation; `user_id` cũ không tự là account v2.
- `alert_dispatch_logs`: payload cần privacy/secret scan; chỉ giữ metadata cần thiết theo retention.

## 3. Các pha không được bỏ qua

### M0 — Authority và freeze plan

Chốt data owner, legal/privacy scope, environment, source DB identifier, target cluster/schema, backup ID, encryption, retention, approver và rollback authority. Chưa đủ thì `BLOCKED_AUTHORITY`, không chạy exporter.

### M1 — Read-only inventory

Lấy schema, declared indexes/FKs, table counts, min/max timestamp, null distribution, duplicate IDs, orphan refs, size và hash manifest. Không log values nhạy cảm. Mỗi query có timestamp, DB ID, tool version và exit code.

### M2 — Immutable extraction

Snapshot nhất quán; chunk theo stable key; mỗi chunk có row count, canonical hash, first/last key, encrypted object ID và retry receipt. Exporter không sửa D1. Canonicalization phải quy định encoding, newline, key order, null và timestamp trước hash.

### M3 — Landing/quarantine

Nạp raw rows vào schema cách ly, không cho app role đọc. Giữ `source_table`, `source_pk`, `source_row_hash`, `extracted_at`, `batch_id`. Malware/secret/privacy review cho JSON/text payload; parse lỗi không được bỏ dòng âm thầm.

### M4 — Transform

Mọi target record có migration ledger: source key → target key, transform version, status, reason, reviewer. Không merge hai profile vì tên/ngày sinh giống. Unknown giữ unknown; time text không offset không tự thành UTC; REAL legacy không được làm exact decimal.

### M5 — Validate

Đối soát theo table và chunk: extracted = loaded + quarantined + intentionally rejected. Kiểm FK/orphan, hash input/output canonical, sample deterministic và quyền. Số row khác chỉ được chấp nhận với reason ledger có tổng khớp.

### M6 — Rehearsal và rollback

Chạy tối thiểu hai lần trên PostgreSQL cô lập với synthetic + sanitized fixture; đo duration/lock/storage; thử rollback code/schema/data. Restore backup và áp lại revocation/deletion tombstone trước mở app.

### M7 — Cutover

Chọn một: write freeze có cửa sổ rõ, hoặc CDC/change capture đã test. Không tự dual-write hai DB nếu chưa có idempotency/outbox và conflict authority. Health 200 không đủ; cần identity/auth/object-negative/read-after-write/report snapshot receipts.

### M8 — Decommission

D1 chỉ chuyển read-only/decommission khi reconciliation, rollback window, retention/deletion và owner sign-off đạt. Xóa/rotate credentials là thay đổi production riêng, không do plan này cấp quyền.

## 4. Quy tắc type và thời gian

- D1 `TEXT` timestamp: parse chỉ khi match format allowlist; thiếu offset giữ raw + `parse_status`, không tự gắn timezone.
- Birth date là civil date; birth time và timezone là các trường riêng; giữ precision/hypothesis.
- D1 `REAL`: giữ raw textual representation và source value; chuyển metric mới chỉ khi có formula contract, range, precision/rounding.
- JSON text: parse bằng schema version cụ thể; invalid → quarantine. Không “sửa” JSON bằng heuristic rồi coi như bản gốc.
- ID: map rõ namespace; không cast ngầm text sang UUID. Target UUID tạo mới và ledger giữ source ID.

## 5. Reconciliation receipt tối thiểu

```json
{
  "batch_id": "uuid",
  "source_db_id": "opaque-provider-id",
  "source_schema_digest": "sha256",
  "source_snapshot_id": "provider-receipt",
  "transform_version": "git-sha+config-digest",
  "target_cluster_id": "opaque-provider-id",
  "counts": {"extracted": 0, "loaded": 0, "quarantined": 0, "rejected": 0},
  "chunk_receipts": [],
  "negative_test_receipt": null,
  "rollback_rehearsal_receipt": null,
  "approvals": [],
  "status": "not_run"
}
```

Mọi số 0 ở ví dụ là schema placeholder, không phải số liệu thực tế. Receipt production chỉ hợp lệ khi các field receipt/approval không rỗng và counts đối soát được.

## 6. Stop conditions

Dừng ngay khi snapshot thay đổi ngoài kế hoạch, hash không khớp, orphan tăng, unknown owner bị auto-link, token xuất hiện trong log, timezone bị tự điền, result legacy vào bảng v2 không có quarantine flag, hoặc rollback rehearsal không khôi phục được. Trạng thái là `BLOCKED`/`FAILED_REHEARSAL`, không tiếp tục vì deadline.

