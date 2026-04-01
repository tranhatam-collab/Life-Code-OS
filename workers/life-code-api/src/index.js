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
        if (!payload.layers || !Array.isArray(payload.layers) || payload.layers.length === 0) {
          return jsonResponse(request, 400, { error: "Missing or invalid layers" });
        }
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

      if (url.pathname === "/api/v1/report") {
        const resultId = payload.result_id;
        const userId = payload.user_id;
        if (!db) return jsonResponse(request, 503, { error: "Database not configured" });
        if (!userId && !resultId) return jsonResponse(request, 400, { error: "user_id or result_id required" });

        try {
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
          const template = `# Level 1 — Self Signal Report

**Generated:** ${data.generated_at || 'N/A'}
**Status:** ${data.status || 'N/A'}

---

## Core Summary

| Metric | Value |
|--------|-------|
| Life Code Index | ${data.life_code_index ?? 'N/A'} |
| Adjusted LCI | ${data.adjusted_life_code_index ?? 'N/A'} |
| Data Coverage | ${data.data_coverage ?? 'N/A'} |
| Risk Score | ${data.risk_score ?? 'N/A'} |
| Wealth Score | ${data.wealth_score ?? 'N/A'} |
| Mission Signal | ${data.mission_signal ?? 'N/A'} |

---

## 1. Identity Layer

${data.identity_layer || 'N/A'}

---

## 2. Analysis Layer

${data.analysis_layer || 'N/A'}

---

## 3. Timeline Layer

${data.timeline_layer || 'N/A'}

---

## 4. Action Layer

${data.action_layer || 'N/A'}

---

## 5. Key Insights

### Risk Assessment
- Raw Risk Score: ${data.risk_score_raw ?? 'N/A'}
- Adjusted Risk Score: ${data.risk_score ?? 'N/A'}

### Wealth Assessment
- Raw Wealth Score: ${data.wealth_score_raw ?? 'N/A'}
- Adjusted Wealth Score: ${data.wealth_score ?? 'N/A'}

### Mission Assessment
- Raw Mission Signal: ${data.mission_signal_raw ?? 'N/A'}
- Adjusted Mission Signal: ${data.mission_signal ?? 'N/A'}

---

## 6. Timeline Windows

### Opportunity Windows
${(data.opportunity_windows || []).slice(0, 10).join(', ') || 'N/A'}

### Transformation Windows
${(data.transformation_windows || []).slice(0, 6).join(', ') || 'N/A'}

---

*Report generated by Life Code OS Engine v1*`;

          return new Response(template, {
            status: 200,
            headers: {
              "content-type": "text/markdown; charset=utf-8",
              ...corsHeaders(request),
            },
          });
        } catch (e) {
          return jsonResponse(request, 500, { error: e.message || "Report generation failed" });
        }
      }

      return jsonResponse(request, 404, { error: "Unknown API route" });
    } catch (e) {
      return jsonResponse(request, 400, { error: e.message || "Bad request" });
    }
  },
};
