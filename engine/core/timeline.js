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

function buildTimeline({ calibrationSeed = 11 } = {}) {
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
module.exports = {
  buildTimeline,
};
