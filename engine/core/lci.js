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

function computeLci(layers) {
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
module.exports = {
  computeLci,
  getCoverageStatus,
};
