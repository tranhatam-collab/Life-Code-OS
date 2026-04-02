const assert = require("node:assert/strict");

const API_BASE = process.env.LC_API_BASE || "https://life-code-api.tranhatam.workers.dev";

async function jsonFetch(path, options = {}) {
  const res = await fetch(`${API_BASE}${path}`, options);
  const text = await res.text();
  let body;
  try {
    body = JSON.parse(text);
  } catch {
    body = text;
  }
  return { res, body, text };
}

async function run() {
  const uniqueName = `Smoke User ${Date.now()}`;

  const start = await jsonFetch("/api/v1/session/start", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ name: uniqueName, birth_place: "HN" }),
  });
  assert.equal(start.res.status, 200, "session/start should return 200");
  assert.ok(start.body.session_token, "session token should exist");
  assert.ok(start.body.user_id, "user id should exist");

  const authHeaders = {
    "content-type": "application/json",
    Authorization: `Bearer ${start.body.session_token}`,
  };

  const lifeCode = await jsonFetch("/api/v1/life-code-data", {
    method: "POST",
    headers: authHeaders,
    body: JSON.stringify({
      layers: [
        { score: 74, weight: 0.5, confidence: 0.8 },
        { score: 62, weight: 0.5, confidence: 0.7 },
      ],
      risk_wealth_mission: {
        health_risk: 0.4,
        health_confidence: 0.7,
        behavior_risk: 0.3,
        behavior_confidence: 0.6,
        relationship_risk: 0.35,
        relationship_confidence: 0.65,
        social_risk: 0.3,
        social_confidence: 0.6,
        wealth_base: 0.5,
        wealth_confidence: 0.6,
        work_fit: 0.6,
        work_confidence: 0.65,
        behavior_finance: 0.55,
        mission_base: 0.55,
        mission_confidence: 0.6,
        legacy_fit: 0.5,
        relationship_support: 0.6,
      },
    }),
  });
  assert.equal(lifeCode.res.status, 200, "life-code-data should return 200");
  assert.ok(lifeCode.body.user_id, "life-code-data should include user_id");

  const me = await jsonFetch("/api/v1/me", {
    method: "GET",
    headers: { Authorization: `Bearer ${start.body.session_token}` },
  });
  assert.equal(me.res.status, 200, "/api/v1/me should return 200");
  assert.equal(me.body.profile.id, start.body.user_id, "profile id should match session user");

  const secondSession = await jsonFetch("/api/v1/session/start", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({
      user_id: start.body.user_id,
      name: `${uniqueName} 2`,
    }),
  });
  assert.equal(secondSession.res.status, 200, "second session/start should return 200");

  const sessionsBeforeRevoke = await jsonFetch("/api/v1/sessions", {
    method: "GET",
    headers: { Authorization: `Bearer ${start.body.session_token}` },
  });
  assert.equal(sessionsBeforeRevoke.res.status, 200, "/api/v1/sessions should return 200");
  assert.ok((sessionsBeforeRevoke.body.sessions || []).length >= 2, "should have at least 2 sessions");

  const update = await jsonFetch("/api/v1/profile/update", {
    method: "POST",
    headers: authHeaders,
    body: JSON.stringify({
      full_name: `${uniqueName} Updated`,
      nickname: "smoke-nick",
      birth_place: "HCMC",
      current_location: "Da Nang",
      profile_metadata: {
        level3: "behavior note",
        level6: "timeline note",
      },
    }),
  });
  assert.equal(update.res.status, 200, "profile/update should return 200");
  assert.equal(update.body.profile.full_name, `${uniqueName} Updated`);
  assert.equal(update.body.profile.nickname, "smoke-nick");
  assert.equal(update.body.profile.profile_metadata.level3, "behavior note");

  const report1 = await fetch(`${API_BASE}/api/v1/report`, {
    method: "POST",
    headers: authHeaders,
    body: JSON.stringify({ level: 1 }),
  });
  const report1Text = await report1.text();
  assert.equal(report1.status, 200, "report level 1 should return 200");
  assert.match(report1Text, /^# Level 1/, "report level 1 markdown header");

  const report9 = await fetch(`${API_BASE}/api/v1/report`, {
    method: "POST",
    headers: authHeaders,
    body: JSON.stringify({ level: 9 }),
  });
  const report9Text = await report9.text();
  assert.equal(report9.status, 200, "report level 9 should return 200");
  assert.match(report9Text, /^# Level 9/, "report level 9 markdown header");

  const target = (sessionsBeforeRevoke.body.sessions || []).find((s) => !s.is_current && !s.revoked_at);
  assert.ok(target, "should find non-current session to revoke");

  const revokeSpecific = await jsonFetch("/api/v1/session/revoke", {
    method: "POST",
    headers: authHeaders,
    body: JSON.stringify({ session_id: target.id }),
  });
  assert.equal(revokeSpecific.res.status, 200, "revoke specific session should return 200");

  const sessionsAfterRevoke = await jsonFetch("/api/v1/sessions", {
    method: "GET",
    headers: { Authorization: `Bearer ${start.body.session_token}` },
  });
  assert.equal(sessionsAfterRevoke.res.status, 200);
  assert.ok((sessionsAfterRevoke.body.sessions || []).some((s) => s.revoked_at), "at least one session should be revoked");

  const logout = await jsonFetch("/api/v1/logout", {
    method: "POST",
    headers: authHeaders,
    body: JSON.stringify({ revoke_all_sessions: false }),
  });
  assert.equal(logout.res.status, 200, "logout should return 200");

  const meAfterLogout = await jsonFetch("/api/v1/me", {
    method: "GET",
    headers: { Authorization: `Bearer ${start.body.session_token}` },
  });
  assert.equal(meAfterLogout.res.status, 401, "/api/v1/me should return 401 after logout");

  console.log("e2e smoke flow passed");
}

run().catch((err) => {
  console.error(err);
  process.exit(1);
});
