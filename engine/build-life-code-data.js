const fs = require("node:fs");
const path = require("node:path");

const { computeLci } = require("./core/lci.js");
const { buildTimeline } = require("./core/timeline.js");
const { computeRiskWealthMission } = require("./core/risk-wealth-mission.js");

function buildLifeCodeData(input) {
  const lci = computeLci(input.layers ?? []);
  const timeline = buildTimeline({ calibrationSeed: input.calibration_seed ?? 11 });
  const rwm = computeRiskWealthMission(input.risk_wealth_mission ?? {});

  const lifeCodeIndex = lci.normalized_lci ?? lci.raw_lci;

  return {
    generated_at: new Date().toISOString(),
    identity_layer: input.identity_layer ?? "Identity layer is missing.",
    analysis_layer: input.analysis_layer ?? "Analysis layer is missing.",
    timeline_layer:
      input.timeline_layer ??
      `Timeline coverage status: ${lci.status}; highlighted years: ${timeline.opportunity_windows
        .slice(0, 6)
        .join(", ")}`,
    action_layer: input.action_layer ?? "Action layer requires manual recommendations.",
    life_code_index: lifeCodeIndex,
    adjusted_life_code_index: lci.adjusted_lci,
    ...lci,
    ...rwm,
    timeline_events: timeline.timeline_events,
    opportunity_windows: timeline.opportunity_windows,
    transformation_windows: timeline.transformation_windows,
    mission_activation_years: timeline.mission_activation_years,
  };
}

function writeLifeCodeDataJson(outputPath, data) {
  const fullPath = path.resolve(outputPath);
  fs.mkdirSync(path.dirname(fullPath), { recursive: true });
  fs.writeFileSync(fullPath, `${JSON.stringify(data, null, 2)}\n`, "utf8");
  return fullPath;
}

module.exports = {
  buildLifeCodeData,
  writeLifeCodeDataJson,
};
