-- LIFE CODE OS v2.1 SCHEMA DELTA REFERENCE — 2026-10-20
-- STATUS: DESIGN_APPROVAL_PENDING / NOT A PRODUCTION MIGRATION / NOT EXECUTED.
-- Preconditions intentionally absent: provider/version, existing constraint names,
-- roles, policy functions, data backfill, locks, rollback and receipts must be resolved.
-- Build incremental expand/backfill/validate/contract migrations from this reference;
-- never paste this file into a live database.

-- ---------------------------------------------------------------------------
-- 1. Method family, release classification, source and rights linkage
-- ---------------------------------------------------------------------------

CREATE TABLE lc.method_family (
  family_id text PRIMARY KEY CHECK (family_id ~ '^K(0[1-9]|1[0-9]|20)$'),
  name_vi text NOT NULL,
  research_state text NOT NULL CHECK (research_state IN (
    'inventory_only', 'source_discovery', 'source_review', 'rule_specification',
    'candidate_testing', 'family_blocked'
  )),
  blocker_codes jsonb NOT NULL DEFAULT '[]'::jsonb CHECK (jsonb_typeof(blocker_codes) = 'array'),
  updated_at timestamptz NOT NULL
);

ALTER TABLE lc.method_family ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.method_family FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.method_family FROM PUBLIC;

-- Expand phase only. Backfill and SET NOT NULL happen in later reviewed migrations.
ALTER TABLE lc.method_release
  ADD COLUMN IF NOT EXISTS computation_kind text,
  ADD COLUMN IF NOT EXISTS evidence_class text,
  ADD COLUMN IF NOT EXISTS release_state_v21 text,
  ADD COLUMN IF NOT EXISTS rule_spec_digest text,
  ADD COLUMN IF NOT EXISTS configuration_digest text,
  ADD COLUMN IF NOT EXISTS input_schema_digest text,
  ADD COLUMN IF NOT EXISTS output_schema_digest text,
  ADD COLUMN IF NOT EXISTS independent_review_receipt_id text,
  ADD COLUMN IF NOT EXISTS approval_receipt_id text;

ALTER TABLE lc.method_release
  ADD CONSTRAINT method_release_computation_kind_v21 CHECK (
    computation_kind IS NULL OR computation_kind IN (
      'deterministic', 'symbolic', 'observational', 'validated_model'
    )
  ) NOT VALID,
  ADD CONSTRAINT method_release_evidence_class_v21 CHECK (
    evidence_class IS NULL OR evidence_class IN (
      'unsourced_candidate', 'source_transcribed', 'rule_reproduced',
      'instrument_evaluated', 'model_evaluated'
    )
  ) NOT VALID,
  ADD CONSTRAINT method_release_state_v21 CHECK (
    release_state_v21 IS NULL OR release_state_v21 IN (
      'research_only', 'specified', 'calculation_verified', 'content_reviewed',
      'permitted_for_product', 'suspended', 'retired'
    )
  ) NOT VALID,
  ADD CONSTRAINT method_release_rule_digest_v21 CHECK (
    rule_spec_digest IS NULL OR rule_spec_digest ~ '^[a-f0-9]{64}$'
  ) NOT VALID,
  ADD CONSTRAINT method_release_configuration_digest_v21 CHECK (
    configuration_digest IS NULL OR configuration_digest ~ '^[a-f0-9]{64}$'
  ) NOT VALID,
  ADD CONSTRAINT method_release_input_schema_digest_v21 CHECK (
    input_schema_digest IS NULL OR input_schema_digest ~ '^[a-f0-9]{64}$'
  ) NOT VALID,
  ADD CONSTRAINT method_release_output_schema_digest_v21 CHECK (
    output_schema_digest IS NULL OR output_schema_digest ~ '^[a-f0-9]{64}$'
  ) NOT VALID;

-- The existing method.family_code is free text. The production migration must
-- first reconcile all values before adding this FK as VALID.
ALTER TABLE lc.method
  ADD CONSTRAINT method_family_code_v21_fk
  FOREIGN KEY (family_code) REFERENCES lc.method_family(family_id) NOT VALID;

CREATE TABLE lc.method_release_source (
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  method_release_id uuid NOT NULL REFERENCES lc.method_release(id),
  source_record_id uuid NOT NULL REFERENCES lc.source_record(id),
  source_edition_id uuid NOT NULL REFERENCES lc.source_edition(id),
  rights_record_id uuid NOT NULL REFERENCES lc.rights_record(id),
  locator text NOT NULL CHECK (length(locator) BETWEEN 1 AND 1000),
  usage_purpose text NOT NULL,
  territory_codes jsonb NOT NULL CHECK (jsonb_typeof(territory_codes) = 'array'),
  channel_codes jsonb NOT NULL CHECK (jsonb_typeof(channel_codes) = 'array'),
  rights_receipt_id text NOT NULL,
  rights_checked_at timestamptz NOT NULL,
  PRIMARY KEY (method_release_id, source_edition_id, locator)
);

ALTER TABLE lc.method_release_source ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.method_release_source FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.method_release_source FROM PUBLIC;

CREATE TABLE lc.method_release_dependency (
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  method_release_id uuid NOT NULL REFERENCES lc.method_release(id),
  depends_on_method_release_id uuid REFERENCES lc.method_release(id),
  depends_on_field_id text,
  depends_on_policy_version_id uuid REFERENCES lc.policy_version(id),
  dependency_key text GENERATED ALWAYS AS (
    COALESCE(
      depends_on_method_release_id::text,
      depends_on_field_id,
      depends_on_policy_version_id::text
    )
  ) STORED,
  dependency_kind text NOT NULL CHECK (dependency_kind IN (
    'method_release', 'input_field', 'policy', 'country_pack', 'product_release'
  )),
  required boolean NOT NULL,
  purpose_code text NOT NULL,
  introduced_in text NOT NULL,
  retired_in text,
  CHECK (
    ((depends_on_method_release_id IS NOT NULL)::int +
     (depends_on_field_id IS NOT NULL)::int +
     (depends_on_policy_version_id IS NOT NULL)::int) = 1
  ),
  CHECK (method_release_id IS DISTINCT FROM depends_on_method_release_id),
  PRIMARY KEY (method_release_id, dependency_kind, dependency_key)
);

-- ---------------------------------------------------------------------------
-- 2. Exact metric and result dependency
-- ---------------------------------------------------------------------------

CREATE TABLE lc.method_metric (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  method_result_id uuid NOT NULL REFERENCES lc.method_result(id),
  metric_id text NOT NULL,
  value_decimal numeric(38, 12),
  value_scale smallint NOT NULL CHECK (value_scale BETWEEN 0 AND 12),
  rounding_mode text NOT NULL CHECK (rounding_mode IN (
    'half_even', 'half_up', 'floor', 'ceiling', 'truncate'
  )),
  scale_min numeric(38, 12),
  scale_max numeric(38, 12),
  unit_code text NOT NULL,
  direction text NOT NULL CHECK (direction IN ('more', 'less', 'not_ordered')),
  observation_window tstzrange,
  missing_reason text,
  formula_version text NOT NULL,
  CHECK ((value_decimal IS NULL) = (missing_reason IS NOT NULL)),
  CHECK (scale_min IS NULL OR scale_max IS NULL OR scale_min <= scale_max),
  CHECK (value_decimal IS NULL OR scale_min IS NULL OR value_decimal >= scale_min),
  CHECK (value_decimal IS NULL OR scale_max IS NULL OR value_decimal <= scale_max),
  UNIQUE (method_result_id, metric_id)
);

ALTER TABLE lc.method_metric ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.method_metric FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.method_metric FROM PUBLIC;

CREATE TABLE lc.result_dependency (
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  result_id uuid NOT NULL REFERENCES lc.method_result(id),
  dependency_type text NOT NULL CHECK (dependency_type IN (
    'method_result', 'observation', 'profile_version', 'data_hypothesis', 'grant_snapshot'
  )),
  dependency_id uuid NOT NULL,
  required boolean NOT NULL,
  use_state text NOT NULL CHECK (use_state IN ('used', 'not_used', 'missing', 'withdrawn')),
  missing_reason text,
  created_at timestamptz NOT NULL,
  CHECK ((use_state = 'missing') = (missing_reason IS NOT NULL)),
  CHECK (dependency_id <> result_id),
  PRIMARY KEY (result_id, dependency_type, dependency_id)
);

ALTER TABLE lc.result_dependency ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.result_dependency FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.result_dependency FROM PUBLIC;

-- ---------------------------------------------------------------------------
-- 3. Multi-subject report snapshot junctions
-- ---------------------------------------------------------------------------

CREATE TABLE lc.report_subject (
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  report_snapshot_id uuid NOT NULL REFERENCES lc.report_snapshot(id),
  subject_id uuid NOT NULL REFERENCES lc.profile_subject(id),
  grant_snapshot_id uuid NOT NULL REFERENCES lc.access_grant(id),
  permission_revision bigint NOT NULL CHECK (permission_revision >= 0),
  PRIMARY KEY (report_snapshot_id, subject_id)
);

CREATE TABLE lc.report_profile_version (
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  report_snapshot_id uuid NOT NULL REFERENCES lc.report_snapshot(id),
  profile_version_id uuid NOT NULL REFERENCES lc.profile_version(id),
  PRIMARY KEY (report_snapshot_id, profile_version_id)
);

CREATE TABLE lc.report_method_release (
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  report_snapshot_id uuid NOT NULL REFERENCES lc.report_snapshot(id),
  method_release_id uuid NOT NULL REFERENCES lc.method_release(id),
  PRIMARY KEY (report_snapshot_id, method_release_id)
);

CREATE TABLE lc.report_claim_link (
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  report_snapshot_id uuid NOT NULL REFERENCES lc.report_snapshot(id),
  claim_id uuid NOT NULL REFERENCES lc.claim(id),
  PRIMARY KEY (report_snapshot_id, claim_id)
);

ALTER TABLE lc.report_subject ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.report_subject FORCE ROW LEVEL SECURITY;
ALTER TABLE lc.report_profile_version ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.report_profile_version FORCE ROW LEVEL SECURITY;
ALTER TABLE lc.report_method_release ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.report_method_release FORCE ROW LEVEL SECURITY;
ALTER TABLE lc.report_claim_link ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.report_claim_link FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.report_subject, lc.report_profile_version,
  lc.report_method_release, lc.report_claim_link FROM PUBLIC;

-- ---------------------------------------------------------------------------
-- 4. Durable jobs, outbox and idempotency
-- ---------------------------------------------------------------------------

CREATE TABLE lc.job_execution (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  subject_id uuid REFERENCES lc.profile_subject(id),
  owner_account_id uuid NOT NULL REFERENCES lc.account(id),
  purpose_id uuid NOT NULL REFERENCES lc.processing_purpose(id),
  policy_version_id uuid NOT NULL REFERENCES lc.policy_version(id),
  operation text NOT NULL,
  resource_type text NOT NULL,
  resource_id uuid NOT NULL,
  state text NOT NULL CHECK (state IN (
    'queued', 'leased', 'running', 'succeeded', 'failed', 'cancelled', 'dead_letter'
  )),
  request_digest text NOT NULL CHECK (request_digest ~ '^[a-f0-9]{64}$'),
  permission_revision bigint NOT NULL CHECK (permission_revision >= 0),
  attempt integer NOT NULL DEFAULT 0 CHECK (attempt >= 0),
  max_attempts integer NOT NULL CHECK (max_attempts BETWEEN 1 AND 100),
  lease_owner text,
  lease_expires_at timestamptz,
  next_attempt_at timestamptz,
  last_error_code text,
  created_at timestamptz NOT NULL,
  updated_at timestamptz NOT NULL,
  completed_at timestamptz,
  CHECK ((state IN ('leased', 'running')) = (lease_owner IS NOT NULL AND lease_expires_at IS NOT NULL))
);

CREATE TABLE lc.idempotency_receipt (
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  account_id uuid NOT NULL REFERENCES lc.account(id),
  operation text NOT NULL,
  client_key text NOT NULL CHECK (length(client_key) BETWEEN 16 AND 200),
  request_digest text NOT NULL CHECK (request_digest ~ '^[a-f0-9]{64}$'),
  response_status integer CHECK (response_status BETWEEN 100 AND 599),
  resource_type text,
  resource_id uuid,
  state text NOT NULL CHECK (state IN ('processing', 'completed', 'failed_terminal')),
  created_at timestamptz NOT NULL,
  completed_at timestamptz,
  PRIMARY KEY (account_id, operation, client_key)
);

ALTER TABLE lc.outbox_event
  ADD COLUMN IF NOT EXISTS deduplication_key text,
  ADD COLUMN IF NOT EXISTS attempt integer NOT NULL DEFAULT 0,
  ADD COLUMN IF NOT EXISTS max_attempts integer,
  ADD COLUMN IF NOT EXISTS lease_owner text,
  ADD COLUMN IF NOT EXISTS lease_expires_at timestamptz,
  ADD COLUMN IF NOT EXISTS next_attempt_at timestamptz,
  ADD COLUMN IF NOT EXISTS dead_lettered_at timestamptz;

CREATE UNIQUE INDEX outbox_event_deduplication_v21
  ON lc.outbox_event (tenant_id, event_type, deduplication_key)
  WHERE deduplication_key IS NOT NULL;

ALTER TABLE lc.job_execution ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.job_execution FORCE ROW LEVEL SECURITY;
ALTER TABLE lc.idempotency_receipt ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.idempotency_receipt FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.job_execution, lc.idempotency_receipt FROM PUBLIC;

-- ---------------------------------------------------------------------------
-- 5. Merchant-account scoped payment events
-- ---------------------------------------------------------------------------

CREATE TABLE lc.merchant_account (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  provider_code text NOT NULL,
  merchant_reference text NOT NULL,
  country_pack_id uuid NOT NULL REFERENCES lc.country_pack(id),
  currency text NOT NULL CHECK (currency ~ '^[A-Z]{3}$'),
  state text NOT NULL CHECK (state IN ('pending', 'active', 'suspended', 'retired')),
  created_at timestamptz NOT NULL,
  UNIQUE (provider_code, merchant_reference)
);

ALTER TABLE lc.payment_event
  ADD COLUMN IF NOT EXISTS merchant_account_id uuid REFERENCES lc.merchant_account(id),
  ADD COLUMN IF NOT EXISTS raw_body_digest text,
  ADD COLUMN IF NOT EXISTS signature_verified_at timestamptz,
  ADD COLUMN IF NOT EXISTS provider_created_at timestamptz;

CREATE UNIQUE INDEX payment_event_provider_merchant_event_v21
  ON lc.payment_event (provider_code, merchant_account_id, provider_event_id)
  WHERE merchant_account_id IS NOT NULL;

-- The old UNIQUE(provider_code, provider_event_id) must only be dropped after
-- merchant_account_id is backfilled and the v2.1 unique index validates.

ALTER TABLE lc.merchant_account ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.merchant_account FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.merchant_account FROM PUBLIC;

-- ---------------------------------------------------------------------------
-- 6. Known type correction and unresolved RLS work
-- ---------------------------------------------------------------------------

-- Existing mismatch: lc.tenant.country_pack_id is text while lc.country_pack.id
-- is uuid. Executable migration sequence: add country_pack_uuid nullable; map and
-- quarantine invalid text; add FK NOT VALID; validate; switch reads/writes; only
-- then remove the text column in a separate contract release.

-- No CREATE POLICY is included here. Default-deny is intentional until the
-- application roles, trusted transaction-local context functions and 64-operation
-- negative matrix are implemented and tested on the selected PostgreSQL version.

