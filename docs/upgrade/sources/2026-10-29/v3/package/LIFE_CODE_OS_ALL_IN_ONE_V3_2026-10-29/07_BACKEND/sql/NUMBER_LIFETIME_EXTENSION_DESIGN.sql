-- DESIGN REFERENCE ONLY. Does not migrate the existing D1 or production database.
-- Review in an isolated PostgreSQL environment with the actual runtime roles.
-- Ends with ROLLBACK. No real accounts, data, tokens or provider connections.
BEGIN;
CREATE SCHEMA lc_v3_reference;
CREATE TABLE lc_v3_reference.subject (
 tenant_id uuid NOT NULL, subject_id uuid NOT NULL,
 state text NOT NULL CHECK(state IN ('active','restricted','deleted')),
 access_revision bigint NOT NULL CHECK(access_revision>0),
 PRIMARY KEY(tenant_id,subject_id)
);
CREATE TABLE lc_v3_reference.profile_version (
 tenant_id uuid NOT NULL, subject_id uuid NOT NULL, profile_version_id uuid NOT NULL,
 version bigint NOT NULL CHECK(version>0), hypothesis_id uuid,
 payload jsonb NOT NULL CHECK(jsonb_typeof(payload)='object'),
 created_at timestamptz NOT NULL DEFAULT now(),
 PRIMARY KEY(tenant_id,subject_id,profile_version_id),
 UNIQUE(tenant_id,subject_id,version),
 FOREIGN KEY(tenant_id,subject_id) REFERENCES lc_v3_reference.subject
);
CREATE TABLE lc_v3_reference.name_version (
 tenant_id uuid NOT NULL, subject_id uuid NOT NULL, name_version_id uuid NOT NULL,
 profile_version_id uuid NOT NULL, role text NOT NULL CHECK(role IN ('birth','common','given','brand')),
 original_text text NOT NULL, normalized_nfc text NOT NULL,
 transliteration text, transliteration_policy text, vowel_policy text,
 semantic_source jsonb, -- meanings remain sourced alternatives, never traits
 PRIMARY KEY(tenant_id,subject_id,name_version_id),
 FOREIGN KEY(tenant_id,subject_id,profile_version_id) REFERENCES lc_v3_reference.profile_version,
 CHECK((transliteration IS NULL)=(transliteration_policy IS NULL))
);
CREATE TABLE lc_v3_reference.number_asset_version (
 tenant_id uuid NOT NULL, subject_id uuid NOT NULL, asset_version_id uuid NOT NULL,
 profile_version_id uuid NOT NULL, context text NOT NULL
   CHECK(context IN ('phone_vn','identifier_suffix4','generic_sequence')),
 raw_text text NOT NULL, canonical_text text NOT NULL,
 normalization_policy text NOT NULL, owner_verification_state text NOT NULL DEFAULT 'unverified',
 PRIMARY KEY(tenant_id,subject_id,asset_version_id),
 FOREIGN KEY(tenant_id,subject_id,profile_version_id) REFERENCES lc_v3_reference.profile_version,
 CHECK(context<>'identifier_suffix4' OR canonical_text ~ '^[0-9]{4}$')
);
CREATE TABLE lc_v3_reference.analysis_bundle (
 tenant_id uuid NOT NULL, subject_id uuid NOT NULL, bundle_id uuid NOT NULL,
 profile_version_id uuid NOT NULL, purpose text NOT NULL,
 access_revision bigint NOT NULL CHECK(access_revision>0),
 version bigint NOT NULL DEFAULT 1 CHECK(version>0),
 state text NOT NULL CHECK(state IN ('queued','running','partial','review_required','published','cancelled','failed','stale')),
 method_release_ids jsonb NOT NULL CHECK(jsonb_typeof(method_release_ids)='array'),
 PRIMARY KEY(tenant_id,subject_id,bundle_id),
 FOREIGN KEY(tenant_id,subject_id,profile_version_id) REFERENCES lc_v3_reference.profile_version
);
CREATE TABLE lc_v3_reference.method_result (
 tenant_id uuid NOT NULL, subject_id uuid NOT NULL, result_id uuid NOT NULL, bundle_id uuid NOT NULL,
 method_release_id text NOT NULL, source_digest text NOT NULL, input_digest text NOT NULL,
 configuration jsonb NOT NULL, calculation jsonb NOT NULL,
 unresolved_inputs jsonb NOT NULL DEFAULT '[]', status text NOT NULL,
 PRIMARY KEY(tenant_id,subject_id,result_id),
 FOREIGN KEY(tenant_id,subject_id,bundle_id) REFERENCES lc_v3_reference.analysis_bundle,
 CHECK(input_digest ~ '^[a-f0-9]{64}$'), CHECK(source_digest ~ '^[a-f0-9]{64}$')
);
CREATE TABLE lc_v3_reference.sequence_segment (
 tenant_id uuid NOT NULL, subject_id uuid NOT NULL, result_id uuid NOT NULL,
 start_index integer NOT NULL CHECK(start_index>=0), end_exclusive integer NOT NULL,
 segment_kind text NOT NULL CHECK(segment_kind IN ('pair','triple','run','diagnostic_bridge')),
 original_digits text NOT NULL, group_id text, state text NOT NULL,
 PRIMARY KEY(tenant_id,subject_id,result_id,segment_kind,start_index,end_exclusive),
 FOREIGN KEY(tenant_id,subject_id,result_id) REFERENCES lc_v3_reference.method_result,
 CHECK(end_exclusive>start_index), CHECK(original_digits ~ '^[0-9]+$'),
 CHECK(group_id IS NULL OR group_id IN ('SK','TY','DN','PV','TM','NQ','LS','HH'))
);
CREATE TABLE lc_v3_reference.life_event (
 tenant_id uuid NOT NULL, subject_id uuid NOT NULL, event_id uuid NOT NULL,
 kind text NOT NULL CHECK(kind IN ('self_report_history','user_plan','symbolic_cycle')),
 occurred_or_target_date date, date_precision text NOT NULL CHECK(date_precision IN ('day','month','year','unknown')),
 domain_id text NOT NULL, title text NOT NULL, source_ref text NOT NULL,
 created_at timestamptz NOT NULL DEFAULT now(),
 PRIMARY KEY(tenant_id,subject_id,event_id),
 FOREIGN KEY(tenant_id,subject_id) REFERENCES lc_v3_reference.subject
);
CREATE TABLE lc_v3_reference.knowledge_transfer (
 tenant_id uuid NOT NULL, subject_id uuid NOT NULL, transfer_id uuid NOT NULL,
 recipient_account_id uuid NOT NULL, artifact_ids jsonb NOT NULL,
 state text NOT NULL CHECK(state IN ('draft','pending_recipient','active','revoked','expired')),
 purpose text NOT NULL CHECK(purpose='knowledge_legacy_sharing'),
 expires_at timestamptz NOT NULL, expected_access_revision bigint NOT NULL,
 PRIMARY KEY(tenant_id,subject_id,transfer_id),
 FOREIGN KEY(tenant_id,subject_id) REFERENCES lc_v3_reference.subject
);
-- Explicitly deny by default. Real operation-specific policies belong to Trust Core.
-- Runtime role MUST NOT be owner/superuser/BYPASSRLS; transaction-local context only.
DO $$ DECLARE tab record; BEGIN
 FOR tab IN SELECT tablename FROM pg_tables WHERE schemaname='lc_v3_reference' LOOP
  EXECUTE format('ALTER TABLE lc_v3_reference.%I ENABLE ROW LEVEL SECURITY',tab.tablename);
  EXECUTE format('ALTER TABLE lc_v3_reference.%I FORCE ROW LEVEL SECURITY',tab.tablename);
 END LOOP;
END $$;
-- No GRANT or permissive policy included. SQL has not been executed against PostgreSQL here.
ROLLBACK;
