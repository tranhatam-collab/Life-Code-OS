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

  const monitorNoKey = await fetchWithRateRetry("/api/v1/ops/summary", { method: "GET" });
  assert.ok([401, 503].includes(monitorNoKey.res.status));

  console.log("contract hardening tests passed");
}

run().catch((err) => {
  console.error(err);
  process.exit(1);
});
