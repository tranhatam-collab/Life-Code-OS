const assert = require("node:assert/strict");

const { computeLci } = require("../core/lci.js");
const { buildTimeline } = require("../core/timeline.js");
const { computeRiskWealthMission } = require("../core/risk-wealth-mission.js");

const lci = computeLci([
  { score: 80, weight: 0.5, confidence: 0.8 },
  { score: 60, weight: 0.5, confidence: 0.9 },
]);

assert.equal(lci.raw_lci, 70);
assert.equal(lci.normalized_lci, 70);
assert.equal(lci.status, "full");

const timeline = buildTimeline({ calibrationSeed: 17 });
assert.equal(timeline.timeline_years.length, 100);
assert.equal(timeline.timeline_events.length, 9);

const rwm = computeRiskWealthMission({
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

assert.ok(rwm.risk_score !== null);
assert.ok(rwm.wealth_score !== null);
assert.ok(rwm.mission_signal !== null);

console.log("engine smoke tests passed");
