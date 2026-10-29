-- 007: session_token column now stores SHA-256 hex of the bearer (not the raw token).
-- No schema change required. Legacy plaintext rows are migrated on successful lookup.
-- Apply note for operators; Worker code performs migrate-on-read.
SELECT 1;
