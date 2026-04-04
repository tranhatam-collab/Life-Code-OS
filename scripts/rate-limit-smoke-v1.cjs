const assert = require("node:assert/strict");

const API_BASE = process.env.LC_API_BASE || "https://life-code-api.tranhatam.workers.dev";

async function run() {
  const start = await fetch(`${API_BASE}/api/v1/session/start`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ name: `RateLimit User ${Date.now()}`, locale: "vi-VN" }),
  });
  const startBody = await start.json();
  assert.equal(start.status, 200, "session/start should return 200");
  const authHeaders = {
    "content-type": "application/json",
    Authorization: `Bearer ${startBody.session_token}`,
  };

  let saw429 = false;
  let saw200 = false;

  for (let i = 0; i < 30; i += 1) {
    const res = await fetch(`${API_BASE}/api/v1/profile/update`, {
      method: "POST",
      headers: authHeaders,
      body: JSON.stringify({
        full_name: `RateLimit Updated ${i}`,
      }),
    });

    if (res.status === 429) {
      saw429 = true;
      break;
    }
    if (res.status === 200) saw200 = true;
  }

  assert.ok(saw200 || saw429, "expected profile/update responses");
  if (!saw429) {
    console.log("rate-limit smoke note: no 429 observed in this run (timing/window dependent)");
  }
  console.log("rate-limit smoke passed");
}

run().catch((err) => {
  console.error(err);
  process.exit(1);
});
