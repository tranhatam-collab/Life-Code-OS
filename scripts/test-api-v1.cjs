const http = require("node:http");
const { spawn } = require("node:child_process");
const path = require("node:path");

const ROOT = path.resolve(__dirname, "..");
const PORT = 8788;

function postJson(route, body) {
  return new Promise((resolve, reject) => {
    const req = http.request(
      {
        hostname: "127.0.0.1",
        port: PORT,
        path: route,
        method: "POST",
        headers: { "content-type": "application/json" },
      },
      (res) => {
        const chunks = [];
        res.on("data", (chunk) => chunks.push(chunk));
        res.on("end", () => {
          try {
            const json = JSON.parse(Buffer.concat(chunks).toString("utf8"));
            resolve({ statusCode: res.statusCode, body: json });
          } catch (err) {
            reject(err);
          }
        });
      }
    );

    req.on("error", reject);
    req.write(JSON.stringify(body));
    req.end();
  });
}

async function main() {
  const proc = spawn("node", ["api/server.cjs"], {
    cwd: ROOT,
    stdio: "ignore",
    env: { ...process.env, PORT: String(PORT) },
  });

  await new Promise((r) => setTimeout(r, 350));

  try {
    const lciResp = await postJson("/api/v1/lci", {
      layers: [
        { score: 80, weight: 0.5, confidence: 0.8 },
        { score: 60, weight: 0.5, confidence: 0.9 },
      ],
    });

    const timelineResp = await postJson("/api/v1/timeline", { calibration_seed: 17 });

    const dataResp = await postJson("/api/v1/life-code-data", {
      calibration_seed: 17,
      layers: [{ score: 70, weight: 1, confidence: 0.8 }],
      risk_wealth_mission: { wealth_base: 0.7, wealth_confidence: 0.8, work_fit: 0.7, work_confidence: 0.8, behavior_finance: 0.7, behavior_confidence: 0.8, health_risk: 0.5, health_confidence: 0.8, behavior_risk: 0.4, relationship_risk: 0.3, relationship_confidence: 0.7, social_risk: 0.3, social_confidence: 0.7, mission_base: 0.7, mission_confidence: 0.8, legacy_fit: 0.7, relationship_support: 0.7 },
    });

    if (lciResp.statusCode !== 200 || lciResp.body.raw_lci !== 70) {
      throw new Error("LCI endpoint failed");
    }
    if (timelineResp.statusCode !== 200 || !Array.isArray(timelineResp.body.timeline_years)) {
      throw new Error("Timeline endpoint failed");
    }
    if (dataResp.statusCode !== 200 || typeof dataResp.body.data_coverage !== "number") {
      throw new Error("life-code-data endpoint failed");
    }

    console.log("api smoke tests passed");
  } finally {
    proc.kill();
  }
}

main().catch((error) => {
  console.error(error.message);
  process.exit(1);
});
