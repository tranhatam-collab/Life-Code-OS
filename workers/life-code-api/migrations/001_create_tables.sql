-- Migration 001: Create user_profiles table
CREATE TABLE IF NOT EXISTS user_profiles (
  id TEXT PRIMARY KEY,
  full_name TEXT NOT NULL,
  birth_date TEXT,
  birth_time TEXT,
  birth_place TEXT,
  gender TEXT,
  current_location TEXT,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

-- Migration 002: Create life_code_results table
CREATE TABLE IF NOT EXISTS life_code_results (
  id TEXT PRIMARY KEY,
  user_id TEXT NOT NULL REFERENCES user_profiles(id),
  generated_at TEXT NOT NULL,
  identity_layer TEXT,
  analysis_layer TEXT,
  timeline_layer TEXT,
  action_layer TEXT,
  life_code_index REAL,
  adjusted_life_code_index REAL,
  raw_lci REAL,
  adjusted_lci REAL,
  data_coverage REAL,
  normalized_lci REAL,
  status TEXT,
  risk_score REAL,
  risk_score_raw REAL,
  wealth_score REAL,
  wealth_score_raw REAL,
  mission_signal REAL,
  mission_signal_raw REAL,
  timeline_events TEXT,
  opportunity_windows TEXT,
  transformation_windows TEXT,
  mission_activation_years TEXT,
  raw_json TEXT
);
