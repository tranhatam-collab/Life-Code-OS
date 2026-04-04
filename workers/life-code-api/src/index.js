import { buildLifeCodeData, buildTimeline, computeLci } from "./engine.mjs";
import { getSupportedReportLevels, renderLevelReport } from "./report.mjs";

const ALLOWED_ORIGIN_PATTERNS = [
  /^https:\/\/lifecode\.iai\.one$/,
  /^https:\/\/[a-z0-9-]+\.life-code-os\.pages\.dev$/,
  /^http:\/\/localhost:\d+$/,
  /^http:\/\/127\.0\.0\.1:\d+$/,
];

const SESSION_TTL_DAYS = 30;
const AVATAR_URL_MAX = 2000;
const LOCALE_MAX = 40;
const DEFAULT_AUDIT_SPIKE_THRESHOLD = 25;
const DEFAULT_RATE_LIMIT_SPIKE_THRESHOLD = 120;

function corsHeaders(request) {
  const origin = request.headers.get("Origin") || "";
  const allow =
    ALLOWED_ORIGIN_PATTERNS.some((re) => re.test(origin)) || origin === "";
  const headers = {
    "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Authorization",
    "Access-Control-Max-Age": "86400",
  };
  if (allow && origin) {
    headers["Access-Control-Allow-Origin"] = origin;
    headers.Vary = "Origin";
  } else if (!origin) {
    headers["Access-Control-Allow-Origin"] = "*";
  }
  return headers;
}

function jsonResponse(request, status, body) {
  return new Response(`${JSON.stringify(body, null, 2)}\n`, {
    status,
    headers: {
      "content-type": "application/json; charset=utf-8",
      ...corsHeaders(request),
    },
  });
}

async function readJsonBody(request) {
  const text = await request.text();
  if (!text.trim()) return {};
  return JSON.parse(text);
}

function generateId() {
  return crypto.randomUUID();
}

function sessionExpiryIso() {
  const d = new Date();
  d.setDate(d.getDate() + SESSION_TTL_DAYS);
  return d.toISOString();
}

function bearerToken(request) {
  const value = request.headers.get("Authorization") || "";
  const [scheme, token] = value.split(" ");
  if (scheme !== "Bearer" || !token) return null;
  return token;
}

async function resolveSessionUserId(request, db) {
  if (!db) return null;
  const token = bearerToken(request);
  if (!token) return null;
  const session = await db
    .prepare(
      "SELECT user_id, expires_at, revoked_at FROM user_sessions WHERE session_token = ? LIMIT 1"
    )
    .bind(token)
    .first();
  if (!session) return null;
  if (session.revoked_at) return null;
  if (session.expires_at && Date.parse(session.expires_at) < Date.now()) return null;
  return session.user_id || null;
}

async function resolveSession(request, db) {
  if (!db) return null;
  const token = bearerToken(request);
  if (!token) return null;
  const session = await db
    .prepare(
      "SELECT id, user_id, session_token, expires_at, revoked_at FROM user_sessions WHERE session_token = ? LIMIT 1"
    )
    .bind(token)
    .first();
  if (!session) return null;
  if (session.revoked_at) return null;
  if (session.expires_at && Date.parse(session.expires_at) < Date.now()) return null;
  return session;
}

function parseReportLevel(value) {
  const level = Number(value ?? 1);
  if (!Number.isInteger(level) || !getSupportedReportLevels().includes(level)) {
    throw new Error("Unsupported report level");
  }
  return level;
}

function sanitizeProfileMetadata(value) {
  if (!value || typeof value !== "object" || Array.isArray(value)) {
    return {};
  }
  const out = {};
  for (const [k, v] of Object.entries(value)) {
    if (!k) continue;
    if (v === undefined || v === null) continue;
    out[k] = String(v).slice(0, 4000);
  }
  return out;
}

function parseProfileMetadataJson(raw) {
  if (!raw) return {};
  try {
    const parsed = JSON.parse(raw);
    return sanitizeProfileMetadata(parsed);
  } catch {
    return {};
  }
}

function parseJsonSafe(raw, fallback = {}) {
  if (!raw) return fallback;
  try {
    return JSON.parse(raw);
  } catch {
    return fallback;
  }
}

function sanitizeNotificationPrefs(value) {
  if (!value || typeof value !== "object" || Array.isArray(value)) {
    return {};
  }
  return {
    email: Boolean(value.email),
    sms: Boolean(value.sms),
    push: Boolean(value.push),
    weekly_report: Boolean(value.weekly_report),
  };
}

function validateAvatarUrl(value) {
  if (value === undefined) return undefined;
  if (value === null || value === "") return null;
  const str = String(value).trim();
  if (str.length > AVATAR_URL_MAX) {
    throw new Error("avatar_url is too long");
  }
  let url;
  try {
    url = new URL(str);
  } catch {
    throw new Error("avatar_url must be a valid URL");
  }
  if (!url.protocol || !["https:", "http:"].includes(url.protocol)) {
    throw new Error("avatar_url must use http or https");
  }
  return str;
}

function validateLocale(value) {
  if (value === undefined) return undefined;
  if (value === null || value === "") return "vi-VN";
  const str = String(value).trim();
  if (str.length > LOCALE_MAX) {
    throw new Error("locale is too long");
  }
  const localePattern = /^[a-z]{2,3}(?:-[A-Z]{2})?$/;
  if (!localePattern.test(str)) {
    throw new Error("locale must follow format like vi-VN or en-US");
  }
  return str;
}

function validateNotificationPrefsStrict(value) {
  if (value === undefined || value === null) return undefined;
  if (typeof value !== "object" || Array.isArray(value)) {
    throw new Error("notification_prefs must be an object");
  }
  const allowed = ["email", "sms", "push", "weekly_report"];
  const out = {};
  for (const [key, val] of Object.entries(value)) {
    if (!allowed.includes(key)) {
      throw new Error(`notification_prefs contains unsupported key: ${key}`);
    }
    if (typeof val !== "boolean") {
      throw new Error(`notification_prefs.${key} must be boolean`);
    }
    out[key] = val;
  }
  return out;
}

function requestIp(request) {
  return request.headers.get("CF-Connecting-IP") || "unknown";
}

function requestUserAgent(request) {
  return request.headers.get("User-Agent") || "unknown";
}

function monitorAuthorized(request, env) {
  const key = env.MONITOR_KEY;
  if (!key) return { ok: false, status: 503, error: "Monitoring key not configured" };
  const received = request.headers.get("x-monitor-key") || "";
  if (received !== key) return { ok: false, status: 401, error: "Unauthorized" };
  return { ok: true };
}

async function rateLimitHit(db, bucketKey, limit, windowSeconds) {
  if (!db) return null;
  const now = Math.floor(Date.now() / 1000);
  const windowStart = now - (now % windowSeconds);
  const id = `${bucketKey}:${windowStart}`;
  const createdAt = new Date(windowStart * 1000).toISOString();

  const row = await db
    .prepare("SELECT request_count FROM rate_limits WHERE id = ? LIMIT 1")
    .bind(id)
    .first();

  if (!row) {
    await db
      .prepare(
        `INSERT INTO rate_limits (id, bucket_key, window_start, window_seconds, request_count, created_at)
         VALUES (?, ?, ?, ?, ?, ?)`
      )
      .bind(id, bucketKey, windowStart, windowSeconds, 1, createdAt)
      .run();
    return null;
  }

  const current = Number(row.request_count || 0);
  if (current >= limit) {
    return {
      retry_after_seconds: windowSeconds - (now - windowStart),
      limit,
      window_seconds: windowSeconds,
    };
  }

  await db
    .prepare("UPDATE rate_limits SET request_count = ? WHERE id = ?")
    .bind(current + 1, id)
    .run();
  return null;
}

async function auditLog(db, request, userId, action, details) {
  if (!db || !userId || !action) return;
  const createdAt = new Date().toISOString();
  try {
    await db
      .prepare(
        `INSERT INTO account_audit_logs (id, user_id, action, details_json, ip_address, user_agent, created_at)
         VALUES (?, ?, ?, ?, ?, ?, ?)`
      )
      .bind(
        generateId(),
        userId,
        action,
        JSON.stringify(details || {}),
        requestIp(request),
        requestUserAgent(request),
        createdAt
      )
      .run();
  } catch (_) {
    // Intentionally ignore audit errors to avoid blocking primary flow.
  }
}

function parseNotificationPrefsJson(raw) {
  if (!raw) return {};
  try {
    return sanitizeNotificationPrefs(JSON.parse(raw));
  } catch {
    return {};
  }
}

function sessionView(row, currentSessionId) {
  if (!row) return null;
  const token = row.session_token || "";
  return {
    id: row.id,
    created_at: row.created_at,
    expires_at: row.expires_at,
    last_seen_at: row.last_seen_at,
    revoked_at: row.revoked_at,
    is_current: row.id === currentSessionId,
    token_tail: token ? token.slice(-8) : null,
    device_label: row.device_label || null,
    ip_address: row.ip_address || null,
    user_agent: row.user_agent || null,
  };
}

function profileView(row) {
  if (!row) return null;
  return {
    ...row,
    profile_metadata: parseProfileMetadataJson(row.profile_metadata_json),
    notification_prefs: parseNotificationPrefsJson(row.notification_prefs_json),
  };
}

export default {
  async fetch(request, env) {
    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: corsHeaders(request) });
    }

    const url = new URL(request.url);
    const db = env.LIFE_CODE_DB;

    if (request.method === "GET" && url.pathname === "/health") {
      return jsonResponse(request, 200, { ok: true, service: "life-code-api", version: "1" });
    }

    if (request.method === "GET" && url.pathname === "/api/v1/me") {
      if (!db) return jsonResponse(request, 503, { error: "Database not configured" });
      const session = await resolveSession(request, db);
      const sessionUserId = session?.user_id;
      if (!sessionUserId) return jsonResponse(request, 401, { error: "Unauthorized" });
      const meRate = await rateLimitHit(db, `me:${sessionUserId}`, 120, 60);
      if (meRate) return jsonResponse(request, 429, { error: "Rate limit exceeded", ...meRate });
      try {
        await db
          .prepare("UPDATE user_sessions SET last_seen_at = ? WHERE id = ?")
          .bind(new Date().toISOString(), session.id)
          .run();

        const profile = await db
          .prepare("SELECT * FROM user_profiles WHERE id = ?")
          .bind(sessionUserId)
          .first();
        if (!profile) return jsonResponse(request, 404, { error: "Profile not found" });
        const latestResult = await db
          .prepare(
            "SELECT * FROM life_code_results WHERE user_id = ? ORDER BY generated_at DESC LIMIT 1"
          )
          .bind(sessionUserId)
          .first();
        return jsonResponse(request, 200, {
          profile: profileView(profile),
          latest_result: latestResult || null,
          session: sessionView(session, session.id),
        });
      } catch (e) {
        return jsonResponse(request, 500, { error: e.message || "Internal error" });
      }
    }

    if (request.method === "GET" && url.pathname === "/api/v1/sessions") {
      if (!db) return jsonResponse(request, 503, { error: "Database not configured" });
      const session = await resolveSession(request, db);
      if (!session?.user_id) return jsonResponse(request, 401, { error: "Unauthorized" });
      const sessionsRate = await rateLimitHit(db, `sessions:${session.user_id}`, 60, 60);
      if (sessionsRate) return jsonResponse(request, 429, { error: "Rate limit exceeded", ...sessionsRate });
      try {
        const rows = await db
          .prepare(
            "SELECT id, session_token, created_at, expires_at, last_seen_at, revoked_at, device_label, ip_address, user_agent FROM user_sessions WHERE user_id = ? ORDER BY created_at DESC LIMIT 50"
          )
          .bind(session.user_id)
          .all();

        return jsonResponse(request, 200, {
          current_session_id: session.id,
          sessions: (rows.results || []).map((row) => sessionView(row, session.id)),
        });
      } catch (e) {
        return jsonResponse(request, 500, { error: e.message || "Internal error" });
      }
    }

    if (request.method === "GET" && url.pathname === "/api/v1/account/audit-logs") {
      if (!db) return jsonResponse(request, 503, { error: "Database not configured" });
      const session = await resolveSession(request, db);
      if (!session?.user_id) return jsonResponse(request, 401, { error: "Unauthorized" });
      const auditRate = await rateLimitHit(db, `audit_logs:${session.user_id}`, 40, 60);
      if (auditRate) return jsonResponse(request, 429, { error: "Rate limit exceeded", ...auditRate });

      const limit = Math.min(Math.max(Number(url.searchParams.get("limit") || 20), 1), 100);
      try {
        const rows = await db
          .prepare(
            "SELECT id, action, details_json, ip_address, user_agent, created_at FROM account_audit_logs WHERE user_id = ? ORDER BY created_at DESC LIMIT ?"
          )
          .bind(session.user_id, limit)
          .all();
        const logs = (rows.results || []).map((row) => ({
          id: row.id,
          action: row.action,
          details: parseJsonSafe(row.details_json, {}),
          ip_address: row.ip_address || null,
          user_agent: row.user_agent || null,
          created_at: row.created_at,
        }));

        return jsonResponse(request, 200, { logs });
      } catch (e) {
        return jsonResponse(request, 500, { error: e.message || "Internal error" });
      }
    }

    if (request.method === "GET" && url.pathname === "/api/v1/ops/summary") {
      if (!db) return jsonResponse(request, 503, { error: "Database not configured" });
      const auth = monitorAuthorized(request, env);
      if (!auth.ok) return jsonResponse(request, auth.status, { error: auth.error });

      try {
        const windowMinutes = Math.min(Math.max(Number(url.searchParams.get("window_minutes") || 10), 1), 60);
        const sinceIso = new Date(Date.now() - windowMinutes * 60 * 1000).toISOString();
        const auditThreshold = Number(env.AUDIT_SPIKE_THRESHOLD || DEFAULT_AUDIT_SPIKE_THRESHOLD);
        const rateLimitThreshold = Number(env.RATE_LIMIT_SPIKE_THRESHOLD || DEFAULT_RATE_LIMIT_SPIKE_THRESHOLD);

        const [users, sessions, results, audits, limits, latestAudit, recentAudits, recentRateWindowCount, recentRateRequestSum, topRateBuckets] = await Promise.all([
          db.prepare("SELECT COUNT(*) AS c FROM user_profiles").first(),
          db.prepare("SELECT COUNT(*) AS c FROM user_sessions").first(),
          db.prepare("SELECT COUNT(*) AS c FROM life_code_results").first(),
          db.prepare("SELECT COUNT(*) AS c FROM account_audit_logs").first(),
          db.prepare("SELECT COUNT(*) AS c FROM rate_limits").first(),
          db.prepare("SELECT created_at FROM account_audit_logs ORDER BY created_at DESC LIMIT 1").first(),
          db.prepare("SELECT COUNT(*) AS c FROM account_audit_logs WHERE created_at >= ?").bind(sinceIso).first(),
          db.prepare("SELECT COUNT(*) AS c FROM rate_limits WHERE created_at >= ?").bind(sinceIso).first(),
          db.prepare("SELECT COALESCE(SUM(request_count), 0) AS c FROM rate_limits WHERE created_at >= ?").bind(sinceIso).first(),
          db
            .prepare(
              "SELECT bucket_key, request_count, window_start, window_seconds FROM rate_limits WHERE created_at >= ? ORDER BY request_count DESC LIMIT 5"
            )
            .bind(sinceIso)
            .all(),
        ]);

        const audit10m = Number(recentAudits?.c || 0);
        const rateLimitWindows10m = Number(recentRateWindowCount?.c || 0);
        const rateLimitRequests10m = Number(recentRateRequestSum?.c || 0);

        const alerts = {
          audit_spike: {
            triggered: audit10m >= auditThreshold,
            current: audit10m,
            threshold: auditThreshold,
            window_minutes: windowMinutes,
          },
          rate_limit_spike: {
            triggered: rateLimitRequests10m >= rateLimitThreshold,
            current: rateLimitRequests10m,
            threshold: rateLimitThreshold,
            window_minutes: windowMinutes,
          },
        };

        const severity = alerts.audit_spike.triggered || alerts.rate_limit_spike.triggered ? "warning" : "normal";

        return jsonResponse(request, 200, {
          ok: true,
          severity,
          counts: {
            user_profiles: Number(users?.c || 0),
            user_sessions: Number(sessions?.c || 0),
            life_code_results: Number(results?.c || 0),
            account_audit_logs: Number(audits?.c || 0),
            rate_limits: Number(limits?.c || 0),
          },
          recent_window: {
            window_minutes: windowMinutes,
            audit_logs: audit10m,
            rate_limit_windows: rateLimitWindows10m,
            rate_limit_requests: rateLimitRequests10m,
            top_rate_buckets: (topRateBuckets.results || []).map((r) => ({
              bucket_key: r.bucket_key,
              request_count: r.request_count,
              window_start: r.window_start,
              window_seconds: r.window_seconds,
            })),
          },
          alerts,
          latest_audit_at: latestAudit?.created_at || null,
          generated_at: new Date().toISOString(),
        });
      } catch (e) {
        return jsonResponse(request, 500, { error: e.message || "Internal error" });
      }
    }

    if (request.method === "GET" && url.pathname.startsWith("/api/v1/profile/")) {
      if (!db) return jsonResponse(request, 503, { error: "Database not configured" });
      const userId = url.pathname.split("/").pop();
      try {
        const profile = await db.prepare("SELECT * FROM user_profiles WHERE id = ?").bind(userId).first();
        if (!profile) return jsonResponse(request, 404, { error: "Profile not found" });
        const results = await db.prepare("SELECT * FROM life_code_results WHERE user_id = ? ORDER BY generated_at DESC LIMIT 1").bind(userId).all();
        return jsonResponse(request, 200, {
          profile: profileView(profile),
          latest_result: results.results[0] || null,
        });
      } catch (e) {
        return jsonResponse(request, 500, { error: e.message || "Internal error" });
      }
    }

    if (request.method !== "POST") {
      return jsonResponse(request, 404, { error: "Not found" });
    }

    try {
      const payload = await readJsonBody(request);

      if (url.pathname === "/api/v1/lci") {
        return jsonResponse(request, 200, computeLci(payload.layers ?? []));
      }

      if (url.pathname === "/api/v1/timeline") {
        return jsonResponse(
          request,
          200,
          buildTimeline({ calibrationSeed: payload.calibration_seed ?? 11 })
        );
      }

      if (url.pathname === "/api/v1/session/start") {
        if (!db) return jsonResponse(request, 503, { error: "Database not configured" });
        if (!payload.name || !String(payload.name).trim()) {
          return jsonResponse(request, 400, { error: "name is required" });
        }
        const startRate = await rateLimitHit(db, `session_start:${requestIp(request)}`, 15, 60);
        if (startRate) return jsonResponse(request, 429, { error: "Rate limit exceeded", ...startRate });
        const userId = payload.user_id || generateId();
        const now = new Date().toISOString();
        const expiresAt = sessionExpiryIso();
        const sessionId = generateId();
        const sessionToken = `${generateId()}${generateId().replace(/-/g, "")}`;
        const profileMetadata = sanitizeProfileMetadata(payload.profile_metadata);
        const nickname = payload.nickname ? String(payload.nickname).trim().slice(0, 120) : null;
        const avatarUrl = validateAvatarUrl(payload.avatar_url);
        const locale = validateLocale(payload.locale);
        const notificationPrefs = validateNotificationPrefsStrict(payload.notification_prefs) || {};
        const ipAddress = requestIp(request);
        const userAgent = requestUserAgent(request);
        const deviceLabel = payload.device_label
          ? String(payload.device_label).trim().slice(0, 120)
          : (userAgent ? userAgent.slice(0, 120) : "Unknown device");

        const current = await db
          .prepare("SELECT created_at, profile_metadata_json, nickname, avatar_url, locale, notification_prefs_json FROM user_profiles WHERE id = ? LIMIT 1")
          .bind(userId)
          .first();
        const createdAt = current?.created_at || now;
        const mergedMetadata = {
          ...parseProfileMetadataJson(current?.profile_metadata_json),
          ...profileMetadata,
        };
        const resolvedNickname = nickname || current?.nickname || null;
        const resolvedAvatarUrl = avatarUrl || current?.avatar_url || null;
        const resolvedLocale = locale || current?.locale || "vi-VN";
        const mergedNotificationPrefs = {
          ...parseNotificationPrefsJson(current?.notification_prefs_json),
          ...notificationPrefs,
        };

        await db
          .prepare(
            `INSERT OR REPLACE INTO user_profiles (id, full_name, nickname, avatar_url, locale, notification_prefs_json, profile_metadata_json, birth_date, birth_time, birth_place, gender, current_location, created_at, updated_at)
             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`
          )
          .bind(
            userId,
            String(payload.name || "").trim(),
            resolvedNickname,
            resolvedAvatarUrl,
            resolvedLocale,
            JSON.stringify(mergedNotificationPrefs),
            JSON.stringify(mergedMetadata),
            payload.birth_date || null,
            payload.birth_time || null,
            payload.birth_place || null,
            payload.gender || null,
            payload.current_location || null,
            createdAt,
            now
          )
          .run();

        await db
          .prepare(
            `INSERT INTO user_sessions (id, user_id, session_token, device_label, ip_address, user_agent, created_at, expires_at, last_seen_at, revoked_at)
             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, NULL)`
          )
          .bind(sessionId, userId, sessionToken, deviceLabel, ipAddress, userAgent, now, expiresAt, now)
          .run();

        await auditLog(db, request, userId, "session_start", {
          session_id: sessionId,
          device_label: deviceLabel,
        });

        return jsonResponse(request, 200, {
          ok: true,
          user_id: userId,
          session_id: sessionId,
          session_token: sessionToken,
          expires_at: expiresAt,
        });
      }

      if (url.pathname === "/api/v1/profile/update") {
        if (!db) return jsonResponse(request, 503, { error: "Database not configured" });
        const session = await resolveSession(request, db);
        if (!session?.user_id) return jsonResponse(request, 401, { error: "Unauthorized" });
        const profileRate = await rateLimitHit(db, `profile_update:${session.user_id}`, 20, 60);
        if (profileRate) return jsonResponse(request, 429, { error: "Rate limit exceeded", ...profileRate });

        const current = await db
          .prepare("SELECT * FROM user_profiles WHERE id = ? LIMIT 1")
          .bind(session.user_id)
          .first();
        if (!current) return jsonResponse(request, 404, { error: "Profile not found" });

        const now = new Date().toISOString();
        const fullName = String(payload.full_name || current.full_name || "").trim();
        if (!fullName) return jsonResponse(request, 400, { error: "full_name cannot be empty" });
        const nickname = payload.nickname === undefined
          ? current.nickname
          : (payload.nickname ? String(payload.nickname).trim().slice(0, 120) : null);
        const avatarUrl = payload.avatar_url === undefined
          ? current.avatar_url
          : validateAvatarUrl(payload.avatar_url);
        const locale = payload.locale === undefined
          ? (current.locale || "vi-VN")
          : validateLocale(payload.locale);
        const mergedNotificationPrefs = {
          ...parseNotificationPrefsJson(current.notification_prefs_json),
          ...(validateNotificationPrefsStrict(payload.notification_prefs) || {}),
        };
        const mergedMetadata = {
          ...parseProfileMetadataJson(current.profile_metadata_json),
          ...sanitizeProfileMetadata(payload.profile_metadata),
        };

        await db
          .prepare(
            `UPDATE user_profiles
             SET full_name = ?, nickname = ?, avatar_url = ?, locale = ?, notification_prefs_json = ?, profile_metadata_json = ?, birth_date = ?, birth_time = ?, birth_place = ?, gender = ?, current_location = ?, updated_at = ?
             WHERE id = ?`
          )
          .bind(
            fullName,
            nickname,
            avatarUrl,
            locale,
            JSON.stringify(mergedNotificationPrefs),
            JSON.stringify(mergedMetadata),
            payload.birth_date ?? current.birth_date,
            payload.birth_time ?? current.birth_time,
            payload.birth_place ?? current.birth_place,
            payload.gender ?? current.gender,
            payload.current_location ?? current.current_location,
            now,
            session.user_id
          )
          .run();

        const updated = await db
          .prepare("SELECT * FROM user_profiles WHERE id = ? LIMIT 1")
          .bind(session.user_id)
          .first();

        await auditLog(db, request, session.user_id, "profile_update", {
          full_name_changed: fullName !== current.full_name,
          nickname_changed: nickname !== current.nickname,
          avatar_changed: avatarUrl !== current.avatar_url,
          locale_changed: locale !== current.locale,
        });

        return jsonResponse(request, 200, { ok: true, profile: profileView(updated) });
      }

      if (url.pathname === "/api/v1/session/update-label") {
        if (!db) return jsonResponse(request, 503, { error: "Database not configured" });
        const session = await resolveSession(request, db);
        if (!session?.user_id) return jsonResponse(request, 401, { error: "Unauthorized" });
        const labelRate = await rateLimitHit(db, `session_label:${session.user_id}`, 40, 60);
        if (labelRate) return jsonResponse(request, 429, { error: "Rate limit exceeded", ...labelRate });

        const sessionId = payload.session_id ? String(payload.session_id) : null;
        const deviceLabel = payload.device_label ? String(payload.device_label).trim().slice(0, 120) : null;
        if (!sessionId) return jsonResponse(request, 400, { error: "session_id is required" });
        if (!deviceLabel) return jsonResponse(request, 400, { error: "device_label is required" });

        const target = await db
          .prepare("SELECT id FROM user_sessions WHERE id = ? AND user_id = ? LIMIT 1")
          .bind(sessionId, session.user_id)
          .first();
        if (!target) return jsonResponse(request, 404, { error: "Session not found" });

        await db
          .prepare("UPDATE user_sessions SET device_label = ? WHERE id = ?")
          .bind(deviceLabel, sessionId)
          .run();

        await auditLog(db, request, session.user_id, "session_label_update", {
          session_id: sessionId,
          device_label: deviceLabel,
        });

        return jsonResponse(request, 200, { ok: true, session_id: sessionId, device_label: deviceLabel });
      }

      if (url.pathname === "/api/v1/session/revoke" || url.pathname === "/api/v1/logout") {
        if (!db) return jsonResponse(request, 503, { error: "Database not configured" });
        const session = await resolveSession(request, db);
        if (!session?.user_id) return jsonResponse(request, 401, { error: "Unauthorized" });
        const revokeRate = await rateLimitHit(db, `session_revoke:${session.user_id}`, 30, 60);
        if (revokeRate) return jsonResponse(request, 429, { error: "Rate limit exceeded", ...revokeRate });

        const now = new Date().toISOString();
        const revokeAll = Boolean(payload.revoke_all_sessions);
        const specificSessionId = payload.session_id ? String(payload.session_id) : null;

        if (revokeAll) {
          await db
            .prepare("UPDATE user_sessions SET revoked_at = ? WHERE user_id = ? AND revoked_at IS NULL")
            .bind(now, session.user_id)
            .run();
        } else if (specificSessionId) {
          const target = await db
            .prepare("SELECT id FROM user_sessions WHERE id = ? AND user_id = ? LIMIT 1")
            .bind(specificSessionId, session.user_id)
            .first();
          if (!target) return jsonResponse(request, 404, { error: "Session not found" });
          await db
            .prepare("UPDATE user_sessions SET revoked_at = ? WHERE id = ?")
            .bind(now, specificSessionId)
            .run();
        } else {
          await db
            .prepare("UPDATE user_sessions SET revoked_at = ? WHERE id = ?")
            .bind(now, session.id)
            .run();
        }

        await auditLog(db, request, session.user_id, "session_revoke", {
          revoke_all_sessions: revokeAll,
          session_id: specificSessionId || session.id,
          mode: revokeAll ? "all" : specificSessionId ? "specific" : "current",
        });

        return jsonResponse(request, 200, {
          ok: true,
          revoked: revokeAll ? "all" : specificSessionId ? "specific" : "current",
        });
      }

      if (url.pathname === "/api/v1/life-code-data") {
        if (!payload.layers || !Array.isArray(payload.layers) || payload.layers.length === 0) {
          return jsonResponse(request, 400, { error: "Missing or invalid layers" });
        }
        const result = buildLifeCodeData(payload);

        if (db) {
          const sessionUserId = await resolveSessionUserId(request, db);
          const userId = payload.user_id || sessionUserId || (payload.name ? generateId() : null);
          if (userId) {
          const now = new Date().toISOString();
          const metadataUpdate = sanitizeProfileMetadata(payload.profile_metadata);
          const nicknameUpdate = payload.nickname ? String(payload.nickname).trim().slice(0, 120) : null;
          const avatarUrlUpdate = payload.avatar_url ? String(payload.avatar_url).trim().slice(0, 2000) : null;
          const localeUpdate = payload.locale ? String(payload.locale).trim().slice(0, 40) : null;
          const notificationPrefsUpdate = sanitizeNotificationPrefs(payload.notification_prefs);

          const profile = await db
            .prepare("SELECT created_at, full_name, nickname, avatar_url, locale, notification_prefs_json, profile_metadata_json FROM user_profiles WHERE id = ? LIMIT 1")
            .bind(userId)
            .first();
          const createdAt = profile?.created_at || now;
          const fullName = String(payload.name || profile?.full_name || "Life Code User").trim();
          const mergedMetadata = {
            ...parseProfileMetadataJson(profile?.profile_metadata_json),
            ...metadataUpdate,
          };
          const mergedNotificationPrefs = {
            ...parseNotificationPrefsJson(profile?.notification_prefs_json),
            ...notificationPrefsUpdate,
          };
          const resolvedNickname = nicknameUpdate || profile?.nickname || null;
          const resolvedAvatarUrl = avatarUrlUpdate || profile?.avatar_url || null;
          const resolvedLocale = localeUpdate || profile?.locale || "vi-VN";

          await db.prepare(
            `INSERT OR REPLACE INTO user_profiles (id, full_name, nickname, avatar_url, locale, notification_prefs_json, profile_metadata_json, birth_date, birth_time, birth_place, gender, current_location, created_at, updated_at)
             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`
          ).bind(
            userId,
            fullName,
            resolvedNickname,
            resolvedAvatarUrl,
            resolvedLocale,
            JSON.stringify(mergedNotificationPrefs),
            JSON.stringify(mergedMetadata),
            payload.birth_date || null,
            payload.birth_time || null,
            payload.birth_place || null,
            payload.gender || null,
            payload.current_location || null,
            createdAt,
            now
          ).run();

          await db.prepare(
            `INSERT INTO life_code_results (id, user_id, generated_at, identity_layer, analysis_layer, timeline_layer, action_layer,
             life_code_index, adjusted_life_code_index, raw_lci, adjusted_lci, data_coverage, normalized_lci, status,
             risk_score, risk_score_raw, wealth_score, wealth_score_raw, mission_signal, mission_signal_raw,
             timeline_events, opportunity_windows, transformation_windows, mission_activation_years, raw_json)
             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`
          ).bind(
            generateId(),
            userId,
            result.generated_at,
            result.identity_layer,
            result.analysis_layer,
            result.timeline_layer,
            result.action_layer,
            result.life_code_index,
            result.adjusted_life_code_index,
            result.raw_lci,
            result.adjusted_lci,
            result.data_coverage,
            result.normalized_lci,
            result.status,
            result.risk_score,
            result.risk_score_raw,
            result.wealth_score,
            result.wealth_score_raw,
            result.mission_signal,
            result.mission_signal_raw,
            JSON.stringify(result.timeline_events || []),
            JSON.stringify(result.opportunity_windows || []),
            JSON.stringify(result.transformation_windows || []),
            JSON.stringify(result.mission_activation_years || []),
            JSON.stringify(result)
          ).run();

          result.user_id = userId;
          }
        }

        return jsonResponse(request, 200, result);
      }

      if (url.pathname === "/api/v1/report") {
        const resultId = payload.result_id;
        let userId = payload.user_id;
        let level;
        if (!db) return jsonResponse(request, 503, { error: "Database not configured" });

        try {
          level = parseReportLevel(payload.level);
          if (!userId) {
            userId = await resolveSessionUserId(request, db);
          }
          if (!userId && !resultId) {
            return jsonResponse(request, 401, { error: "Unauthorized: user session required" });
          }
          let rawJson;
          if (resultId) {
            const row = await db.prepare("SELECT raw_json FROM life_code_results WHERE id = ?").bind(resultId).first();
            if (!row) return jsonResponse(request, 404, { error: "Result not found" });
            rawJson = row.raw_json;
          } else {
            const row = await db.prepare("SELECT raw_json FROM life_code_results WHERE user_id = ? ORDER BY generated_at DESC LIMIT 1").bind(userId).first();
            if (!row) return jsonResponse(request, 404, { error: "No results found for user" });
            rawJson = row.raw_json;
          }

          const data = JSON.parse(rawJson);
          const template = renderLevelReport(level, data);

          return new Response(template, {
            status: 200,
            headers: {
              "content-type": "text/markdown; charset=utf-8",
              "x-life-code-report-level": String(level),
              ...corsHeaders(request),
            },
          });
        } catch (e) {
          if (String(e.message || "").includes("Unsupported report level")) {
            return jsonResponse(request, 400, { error: "Unsupported report level" });
          }
          return jsonResponse(request, 500, { error: e.message || "Report generation failed" });
        }
      }

      return jsonResponse(request, 404, { error: "Unknown API route" });
    } catch (e) {
      return jsonResponse(request, 400, { error: e.message || "Bad request" });
    }
  },
};
