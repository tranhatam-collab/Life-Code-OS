const COVERAGE_STATUS_RULES = [
  { maxExclusive: 0.25, status: "insufficient" },
  { maxExclusive: 0.55, status: "partial" },
  { maxExclusive: 0.8, status: "strong" },
  { maxExclusive: Infinity, status: "full" },
];

function round(num, precision = 4) {
  const factor = 10 ** precision;
  return Math.round(num * factor) / factor;
}

function getCoverageStatus(coverage) {
  const safe = Number.isFinite(coverage) ? coverage : 0;
  return COVERAGE_STATUS_RULES.find((rule) => safe < rule.maxExclusive).status;
}

export function computeLci(layers) {
  const validLayers = layers.filter(
    (layer) =>
      layer &&
      Number.isFinite(layer.weight) &&
      layer.weight > 0 &&
      Number.isFinite(layer.score)
  );

  const weightedScoreSum = validLayers.reduce(
    (sum, layer) => sum + layer.score * layer.weight,
    0
  );

  const adjustedWeightedSum = validLayers.reduce((sum, layer) => {
    const confidence = Number.isFinite(layer.confidence) ? layer.confidence : 0;
    return sum + layer.score * layer.weight * confidence;
  }, 0);

  const validWeightSum = validLayers.reduce((sum, layer) => sum + layer.weight, 0);
  const totalWeightSum = layers.reduce((sum, layer) => {
    if (!layer || !Number.isFinite(layer.weight) || layer.weight <= 0) return sum;
    return sum + layer.weight;
  }, 0);

  const rawLci = round(weightedScoreSum);
  const adjustedLci = round(adjustedWeightedSum);
  const dataCoverage = totalWeightSum > 0 ? round(validWeightSum / totalWeightSum) : 0;
  const normalizedLci = validWeightSum > 0 ? round(weightedScoreSum / validWeightSum) : null;

  return {
    raw_lci: rawLci,
    adjusted_lci: adjustedLci,
    data_coverage: dataCoverage,
    normalized_lci: normalizedLci,
    status: getCoverageStatus(dataCoverage),
  };
}

const STAGE_WINDOWS = [
  { id: "stage_0_9", start: 0, end: 9 },
  { id: "stage_10_19", start: 10, end: 19 },
  { id: "stage_20_29", start: 20, end: 29 },
  { id: "stage_30_39", start: 30, end: 39 },
  { id: "stage_40_49", start: 40, end: 49 },
  { id: "stage_50_59", start: 50, end: 59 },
  { id: "stage_60_69", start: 60, end: 69 },
  { id: "stage_70_79", start: 70, end: 79 },
  { id: "stage_80_99", start: 80, end: 99 },
];

function deterministicSignal(seed, year, bias = 0) {
  const x = Math.sin((seed + 1) * (year + 7) * 12.9898) * 43758.5453;
  const frac = x - Math.floor(x);
  return Math.max(0, Math.min(1, frac + bias));
}

function inRange(year, start, end) {
  return year >= start && year <= end;
}

export function buildTimeline({ calibrationSeed = 11 } = {}) {
  const years = [];
  const riskYears = [];
  const peakYears = [];
  const transformationYears = [];
  const missionActivationYears = [];

  for (let year = 0; year <= 99; year += 1) {
    const stage = STAGE_WINDOWS.find((window) => inRange(year, window.start, window.end));
    const riskSignal = deterministicSignal(calibrationSeed, year, -0.15);
    const peakSignal = deterministicSignal(calibrationSeed + 3, year, -0.1);
    const transformationSignal = deterministicSignal(calibrationSeed + 7, year, -0.2);
    const missionSignal = deterministicSignal(calibrationSeed + 13, year, -0.25);

    if (riskSignal >= 0.7) riskYears.push(year);
    if (peakSignal >= 0.72) peakYears.push(year);
    if (transformationSignal >= 0.75) transformationYears.push(year);
    if (missionSignal >= 0.78) missionActivationYears.push(year);

    years.push({
      year,
      stage_id: stage.id,
      risk_signal: Number(riskSignal.toFixed(4)),
      peak_signal: Number(peakSignal.toFixed(4)),
      transformation_signal: Number(transformationSignal.toFixed(4)),
      mission_signal: Number(missionSignal.toFixed(4)),
    });
  }

  return {
    timeline_years: years,
    timeline_events: STAGE_WINDOWS.map((stage) => ({
      stage_id: stage.id,
      from: stage.start,
      to: stage.end,
    })),
    risk_years: riskYears,
    opportunity_windows: peakYears,
    transformation_windows: transformationYears,
    mission_activation_years: missionActivationYears,
  };
}

function weightedAverage(parts) {
  const valid = parts.filter(
    (part) => Number.isFinite(part.score) && Number.isFinite(part.weight) && part.weight > 0
  );
  const weightSum = valid.reduce((sum, part) => sum + part.weight, 0);
  if (weightSum === 0) return null;
  const weighted = valid.reduce((sum, part) => sum + part.score * part.weight, 0);
  return Number((weighted / weightSum).toFixed(4));
}

function adjustedWeighted(parts) {
  const valid = parts.filter(
    (part) => Number.isFinite(part.score) && Number.isFinite(part.weight) && part.weight > 0
  );
  const weightSum = valid.reduce((sum, part) => sum + part.weight, 0);
  if (weightSum === 0) return null;
  const weighted = valid.reduce((sum, part) => {
    const confidence = Number.isFinite(part.confidence) ? part.confidence : 0;
    return sum + part.score * part.weight * confidence;
  }, 0);
  return Number((weighted / weightSum).toFixed(4));
}

export function computeRiskWealthMission(layerInputs) {
  const riskParts = [
    { score: layerInputs.health_risk, weight: 0.35, confidence: layerInputs.health_confidence },
    { score: layerInputs.behavior_risk, weight: 0.25, confidence: layerInputs.behavior_confidence },
    {
      score: layerInputs.relationship_risk,
      weight: 0.2,
      confidence: layerInputs.relationship_confidence,
    },
    { score: layerInputs.social_risk, weight: 0.2, confidence: layerInputs.social_confidence },
  ];

  const wealthParts = [
    { score: layerInputs.wealth_base, weight: 0.4, confidence: layerInputs.wealth_confidence },
    { score: layerInputs.work_fit, weight: 0.35, confidence: layerInputs.work_confidence },
    { score: layerInputs.behavior_finance, weight: 0.25, confidence: layerInputs.behavior_confidence },
  ];

  const missionParts = [
    {
      score: layerInputs.mission_base,
      weight: 0.45,
      confidence: layerInputs.mission_confidence,
    },
    { score: layerInputs.legacy_fit, weight: 0.3, confidence: layerInputs.social_confidence },
    {
      score: layerInputs.relationship_support,
      weight: 0.25,
      confidence: layerInputs.relationship_confidence,
    },
  ];

  return {
    risk_score: adjustedWeighted(riskParts),
    risk_score_raw: weightedAverage(riskParts),
    wealth_score: adjustedWeighted(wealthParts),
    wealth_score_raw: weightedAverage(wealthParts),
    mission_signal: adjustedWeighted(missionParts),
    mission_signal_raw: weightedAverage(missionParts),
  };
}

export function buildLifeCodeData(input) {
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
