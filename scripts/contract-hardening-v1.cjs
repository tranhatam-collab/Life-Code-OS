const assert = require("node:assert/strict");

const API_BASE = process.env.LC_API_BASE || "https://life-code-api.tranhatam.workers.dev";

async function jsonFetch(path, options = {}) {
  const res = await fetch(`${API_BASE}${path}`, options);
  const text = await res.text();
  let body;
  try {
    body = JSON.parse(text);
  } catch {
    body = { raw: text };
  }
  return { res, body, text };
}

async function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function fetchWithRateRetry(path, options = {}, attempts = 5) {
  for (let i = 0; i < attempts; i += 1) {
    const out = await jsonFetch(path, options);
    if (out.res.status !== 429) return out;
    const wait = Number(out.body.retry_after_seconds || 2);
    await sleep(Math.min(wait, 5) * 1000);
  }
  return jsonFetch(path, options);
}

async function run() {
  const invalidLocale = await fetchWithRateRetry("/api/v1/session/start", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ name: "Contract Locale", locale: "invalid_locale" }),
  });
  assert.equal(invalidLocale.res.status, 400);
  assert.match(String(invalidLocale.body.error || ""), /locale/i);

  const invalidAvatar = await fetchWithRateRetry("/api/v1/session/start", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ name: "Contract Avatar", avatar_url: "ftp://bad-url" }),
  });
  assert.equal(invalidAvatar.res.status, 400);
  assert.match(String(invalidAvatar.body.error || ""), /avatar_url/i);

  const start = await fetchWithRateRetry("/api/v1/session/start", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({
      name: `Contract User ${Date.now()}`,
      locale: "vi-VN",
      avatar_url: "https://example.com/a.png",
      notification_prefs: { email: true, sms: false, push: true, weekly_report: false },
      device_label: "Contract Device",
    }),
  });
  assert.equal(start.res.status, 200);
  assert.ok(start.body.session_token);
  assert.ok(start.body.session_id);

  const authHeaders = {
    "content-type": "application/json",
    Authorization: `Bearer ${start.body.session_token}`,
  };

  const me = await fetchWithRateRetry("/api/v1/me", { method: "GET", headers: authHeaders });
  assert.equal(me.res.status, 200);
  assert.equal(me.body.profile.locale, "vi-VN");

  const badNotif = await fetchWithRateRetry("/api/v1/profile/update", {
    method: "POST",
    headers: authHeaders,
    body: JSON.stringify({
      full_name: "Contract Updated",
      notification_prefs: { email: "yes" },
    }),
  });
  assert.equal(badNotif.res.status, 400);
  assert.match(String(badNotif.body.error || ""), /notification_prefs/i);

  const audit = await fetchWithRateRetry("/api/v1/account/audit-logs?limit=10", {
    method: "GET",
    headers: authHeaders,
  });
  assert.equal(audit.res.status, 200);
  assert.ok(Array.isArray(audit.body.logs));

  const profileNoAuth = await fetchWithRateRetry("/api/v1/profile/not-a-real-user", {
    method: "GET",
  });
  assert.equal(profileNoAuth.res.status, 401);

  const profileOther = await fetchWithRateRetry("/api/v1/profile/00000000-0000-4000-8000-000000000000", {
    method: "GET",
    headers: authHeaders,
  });
  assert.equal(profileOther.res.status, 403);

  const profileSelf = await fetchWithRateRetry(`/api/v1/profile/${me.body.profile.id}`, {
    method: "GET",
    headers: authHeaders,
  });
  assert.equal(profileSelf.res.status, 200);
  assert.equal(profileSelf.body.profile.id, me.body.profile.id);

  const overwriteAttempt = await fetchWithRateRetry("/api/v1/life-code-data", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({
      user_id: me.body.profile.id,
      name: "Attacker Overwrite",
      layers: [{ score: 10, weight: 1, confidence: 1 }],
    }),
  });
  assert.equal(overwriteAttempt.res.status, 200);
  assert.notEqual(overwriteAttempt.body.user_id, me.body.profile.id);

  const reportNoAuth = await fetchWithRateRetry("/api/v1/report", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ level: 1, result_id: "00000000-0000-4000-8000-000000000001" }),
  });
  assert.equal(reportNoAuth.res.status, 401);

  const monitorNoKey = await fetchWithRateRetry("/api/v1/ops/summary", { method: "GET" });
  assert.ok([401, 403, 503].includes(monitorNoKey.res.status));

  const alertNoKey = await fetchWithRateRetry("/api/v1/ops/alert-check", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ window_minutes: 10, dry_run: true }),
  });
  assert.ok([401, 403, 503].includes(alertNoKey.res.status));

  console.log("contract hardening tests passed");
}

run().catch((err) => {
  console.error(err);
  process.exit(1);
});
