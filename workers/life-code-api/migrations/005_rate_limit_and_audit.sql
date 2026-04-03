CREATE TABLE IF NOT EXISTS rate_limits (
  id TEXT PRIMARY KEY,
  bucket_key TEXT NOT NULL,
  window_start INTEGER NOT NULL,
  window_seconds INTEGER NOT NULL,
  request_count INTEGER NOT NULL,
  created_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_rate_limits_bucket ON rate_limits(bucket_key);

CREATE TABLE IF NOT EXISTS account_audit_logs (
  id TEXT PRIMARY KEY,
  user_id TEXT NOT NULL,
  action TEXT NOT NULL,
  details_json TEXT,
  ip_address TEXT,
  user_agent TEXT,
  created_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_account_audit_user_time ON account_audit_logs(user_id, created_at);
