const http = require("node:http");

const { computeLci } = require("../engine/core/lci.js");
const { buildTimeline } = require("../engine/core/timeline.js");
const { buildLifeCodeData } = require("../engine/build-life-code-data.js");

const PORT = Number(process.env.PORT || 8788);

function sendJson(res, statusCode, body) {
  res.writeHead(statusCode, { "content-type": "application/json; charset=utf-8" });
  res.end(`${JSON.stringify(body, null, 2)}\n`);
}

function readBody(req) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    req.on("data", (chunk) => chunks.push(chunk));
    req.on("end", () => {
      const raw = Buffer.concat(chunks).toString("utf8").trim();
      if (!raw) {
        resolve({});
        return;
      }
      try {
        resolve(JSON.parse(raw));
      } catch (error) {
        reject(new Error("Invalid JSON body"));
      }
    });
    req.on("error", reject);
  });
}

const server = http.createServer(async (req, res) => {
  if (req.method === "GET" && req.url === "/health") {
    sendJson(res, 200, { ok: true, service: "life-code-api-v1" });
    return;
  }

  if (req.method !== "POST") {
    sendJson(res, 404, { error: "Not found" });
    return;
  }

  try {
    const payload = await readBody(req);

    if (req.url === "/api/v1/lci") {
      const result = computeLci(payload.layers ?? []);
      sendJson(res, 200, result);
      return;
    }

    if (req.url === "/api/v1/timeline") {
      const result = buildTimeline({ calibrationSeed: payload.calibration_seed ?? 11 });
      sendJson(res, 200, result);
      return;
    }

    if (req.url === "/api/v1/life-code-data") {
      const result = buildLifeCodeData(payload);
      sendJson(res, 200, result);
      return;
    }

    sendJson(res, 404, { error: "Unknown API route" });
  } catch (error) {
    sendJson(res, 400, { error: error.message || "Bad request" });
  }
});

server.listen(PORT, () => {
  console.log(`life-code-api-v1 listening on http://localhost:${PORT}`);
});
