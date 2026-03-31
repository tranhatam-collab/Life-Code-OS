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

function generateId() {
  return crypto.randomUUID();
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

    if (request.method === "GET" && url.pathname.startsWith("/api/v1/profile/")) {
      if (!db) return jsonResponse(request, 503, { error: "Database not configured" });
      const userId = url.pathname.split("/").pop();
      try {
        const profile = await db.prepare("SELECT * FROM user_profiles WHERE id = ?").bind(userId).first();
        if (!profile) return jsonResponse(request, 404, { error: "Profile not found" });
        const results = await db.prepare("SELECT * FROM life_code_results WHERE user_id = ? ORDER BY generated_at DESC LIMIT 1").bind(userId).all();
        return jsonResponse(request, 200, { profile, latest_result: results.results[0] || null });
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

      if (url.pathname === "/api/v1/life-code-data") {
        const result = buildLifeCodeData(payload);

        if (db && payload.name) {
          const userId = payload.user_id || generateId();
          const now = new Date().toISOString();

          await db.prepare(
            `INSERT OR REPLACE INTO user_profiles (id, full_name, birth_date, birth_time, birth_place, gender, current_location, created_at, updated_at)
             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)`
          ).bind(
            userId,
            payload.name || "",
            payload.birth_date || null,
            payload.birth_time || null,
            payload.birth_place || null,
            payload.gender || null,
            payload.current_location || null,
            now,
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

        return jsonResponse(request, 200, result);
      }

      return jsonResponse(request, 404, { error: "Unknown API route" });
    } catch (e) {
      return jsonResponse(request, 400, { error: e.message || "Bad request" });
    }
  },
};
