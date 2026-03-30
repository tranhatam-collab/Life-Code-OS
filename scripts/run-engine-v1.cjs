const fs = require("node:fs");
const path = require("node:path");

const { buildLifeCodeData, writeLifeCodeDataJson } = require("../engine/build-life-code-data.js");

const ROOT = path.resolve(__dirname, "..");
const SAMPLE_INPUT_PATH = path.join(ROOT, "engine", "data", "sample-input.json");
const OUTPUT_PATH = path.join(ROOT, "engine", "data", "life_code_data.json");

const input = JSON.parse(fs.readFileSync(SAMPLE_INPUT_PATH, "utf8"));
const lifeCodeData = buildLifeCodeData(input);
const out = writeLifeCodeDataJson(OUTPUT_PATH, lifeCodeData);

console.log(`Generated: ${out}`);
console.log(
  `Status=${lifeCodeData.status}, LCI(raw=${lifeCodeData.raw_lci}, adjusted=${lifeCodeData.adjusted_lci}, normalized=${lifeCodeData.normalized_lci})`
);
