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

function computeRiskWealthMission(layerInputs) {
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
module.exports = {
  computeRiskWealthMission,
};
