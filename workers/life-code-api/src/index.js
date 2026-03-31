import { buildLifeCodeData, buildTimeline, computeLci } from "./engine.mjs";

const ALLOWED_ORIGIN_PATTERNS = [
  /^https:\/\/lifecode\.iai\.one$/,
  /^https:\/\/[a-z0-9-]+\.life-code-os\.pages\.dev$/,
  /^http:\/\/localhost:\d+$/,
  /^http:\/\/127\.0\.0\.1:\d+$/,
];

function corsHeaders(request) {
  const origin = request.headers.get("Origin") || "";
  const allow =
    ALLOWED_ORIGIN_PATTERNS.some((re) => re.test(origin)) || origin === "";
  const headers = {
    "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
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

export default {
  async fetch(request) {
    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: corsHeaders(request) });
    }

    const url = new URL(request.url);

    if (request.method === "GET" && url.pathname === "/health") {
      return jsonResponse(request, 200, { ok: true, service: "life-code-api", version: "1" });
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

      if (url.pathname === "/api/v1/life-code-data") {
        return jsonResponse(request, 200, buildLifeCodeData(payload));
      }

      return jsonResponse(request, 404, { error: "Unknown API route" });
    } catch (e) {
      return jsonResponse(request, 400, { error: e.message || "Bad request" });
    }
  },
};
