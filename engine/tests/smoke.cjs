const assert = require("node:assert/strict");

const { computeLci, getCoverageStatus } = require("../core/lci.js");
const { buildTimeline } = require("../core/timeline.js");
const { computeRiskWealthMission } = require("../core/risk-wealth-mission.js");
const { buildLifeCodeData } = require("../build-life-code-data.js");

console.log("=== LCI Tests ===");

const lciFull = computeLci([
  { score: 80, weight: 0.5, confidence: 0.8 },
  { score: 60, weight: 0.5, confidence: 0.9 },
]);
assert.equal(lciFull.raw_lci, 70);
assert.equal(lciFull.normalized_lci, 70);
assert.equal(lciFull.status, "full");
console.log("✓ Full data LCI");

const lciEmpty = computeLci([]);
assert.equal(lciEmpty.raw_lci, 0);
assert.equal(lciEmpty.data_coverage, 0);
assert.equal(lciEmpty.status, "insufficient");
console.log("✓ Empty data LCI");

const lciPartial = computeLci([
  { score: 70, weight: 0.4, confidence: 0.7 },
  null,
  { score: 50, weight: 0.6, confidence: 0.5 },
  { score: 60, weight: -1, confidence: 0.8 },
]);
assert.ok(lciPartial.raw_lci > 0);
assert.ok(lciPartial.data_coverage >= 0.9);
console.log("✓ Partial data with invalid layers filtered");

assert.equal(getCoverageStatus(0), "insufficient");
assert.equal(getCoverageStatus(0.24), "insufficient");
assert.equal(getCoverageStatus(0.25), "partial");
assert.equal(getCoverageStatus(0.54), "partial");
assert.equal(getCoverageStatus(0.55), "strong");
assert.equal(getCoverageStatus(0.79), "strong");
assert.equal(getCoverageStatus(0.8), "full");
assert.equal(getCoverageStatus(1), "full");
console.log("✓ Coverage status rules");

console.log("\n=== Timeline Tests ===");

const timeline = buildTimeline({ calibrationSeed: 17 });
assert.equal(timeline.timeline_years.length, 100);
assert.equal(timeline.timeline_events.length, 9);
assert.ok(Array.isArray(timeline.risk_years));
assert.ok(Array.isArray(timeline.opportunity_windows));
assert.ok(Array.isArray(timeline.transformation_windows));
assert.ok(Array.isArray(timeline.mission_activation_years));
console.log("✓ Timeline structure");

const t0 = timeline.timeline_years[0];
assert.equal(t0.year, 0);
assert.equal(t0.stage_id, "stage_0_9");
const t99 = timeline.timeline_years[99];
assert.equal(t99.year, 99);
assert.equal(t99.stage_id, "stage_80_99");
console.log("✓ Timeline year boundaries");

const defaultTimeline = buildTimeline();
assert.equal(defaultTimeline.timeline_years.length, 100);
console.log("✓ Default calibration seed");

console.log("\n=== Risk/Wealth/Mission Tests ===");

const rwmFull = computeRiskWealthMission({
  health_risk: 0.6,
  health_confidence: 0.8,
  behavior_risk: 0.5,
  behavior_confidence: 0.7,
  relationship_risk: 0.4,
  relationship_confidence: 0.6,
  social_risk: 0.3,
  social_confidence: 0.5,
  wealth_base: 0.7,
  wealth_confidence: 0.8,
  work_fit: 0.75,
  work_confidence: 0.8,
  behavior_finance: 0.65,
  mission_base: 0.8,
  mission_confidence: 0.85,
  legacy_fit: 0.7,
  relationship_support: 0.6,
});
assert.ok(rwmFull.risk_score !== null);
assert.ok(rwmFull.wealth_score !== null);
assert.ok(rwmFull.mission_signal !== null);
assert.ok(rwmFull.risk_score <= 1);
assert.ok(rwmFull.wealth_score <= 1);
assert.ok(rwmFull.mission_signal <= 1);
console.log("✓ Full RWM scores in range [0,1]");

const rwmEmpty = computeRiskWealthMission({});
assert.equal(rwmEmpty.risk_score, null);
assert.equal(rwmEmpty.wealth_score, null);
assert.equal(rwmEmpty.mission_signal, null);
console.log("✓ Empty RWM returns null");

console.log("\n=== Build Life Code Data Tests ===");

const fullData = buildLifeCodeData({
  identity_layer: "Test identity",
  analysis_layer: "Test analysis",
  action_layer: "Test action",
  layers: [
    { score: 70, weight: 0.5, confidence: 0.8 },
    { score: 60, weight: 0.5, confidence: 0.7 },
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
});
assert.ok(fullData.life_code_index !== undefined);
assert.ok(fullData.generated_at);
assert.equal(fullData.identity_layer, "Test identity");
assert.ok(Array.isArray(fullData.timeline_events));
assert.ok(Array.isArray(fullData.opportunity_windows));
console.log("✓ Full buildLifeCodeData");

const minimalData = buildLifeCodeData({});
assert.equal(minimalData.life_code_index, 0);
assert.equal(minimalData.status, "insufficient");
assert.equal(minimalData.identity_layer, "Identity layer is missing.");
console.log("✓ Minimal buildLifeCodeData with defaults");

console.log("\n✅ All engine tests passed");
