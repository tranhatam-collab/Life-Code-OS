CREATE TABLE IF NOT EXISTS alert_dispatch_logs (
  id TEXT PRIMARY KEY,
  alert_type TEXT NOT NULL,
  severity TEXT NOT NULL,
  payload_json TEXT,
  created_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_alert_dispatch_type_time ON alert_dispatch_logs(alert_type, created_at);
