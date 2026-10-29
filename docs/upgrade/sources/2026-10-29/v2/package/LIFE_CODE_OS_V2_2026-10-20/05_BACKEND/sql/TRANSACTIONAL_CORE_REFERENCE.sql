-- LIFE CODE V2 - DESIGN REFERENCE, NOT A PRODUCTION MIGRATION.
-- Isolated PostgreSQL review only. Ends with ROLLBACK deliberately.
-- No deployment role, no real identity provider, no production secrets.
BEGIN;
CREATE SCHEMA lc_v2_reference;
CREATE TABLE lc_v2_reference.subject (
 tenant_id uuid NOT NULL, subject_id uuid NOT NULL,
 permission_revision bigint NOT NULL CHECK(permission_revision > 0),
 state text NOT NULL CHECK(state IN ('active','restricted','deleted')),
 PRIMARY KEY(tenant_id, subject_id)
);
CREATE TABLE lc_v2_reference.access_grant (
 grant_id uuid PRIMARY KEY, tenant_id uuid NOT NULL, subject_id uuid NOT NULL,
 grantee_account_id uuid NOT NULL, purpose text NOT NULL,
 actions text[] NOT NULL CHECK(cardinality(actions)>0),
 permission_revision bigint NOT NULL CHECK(permission_revision>0),
 valid_until timestamptz NOT NULL, state text NOT NULL CHECK(state IN ('active','revoked')),
 FOREIGN KEY(tenant_id,subject_id) REFERENCES lc_v2_reference.subject(tenant_id,subject_id)
);
CREATE INDEX grant_lookup ON lc_v2_reference.access_grant
 (tenant_id,subject_id,grantee_account_id,purpose,state,valid_until);
CREATE TABLE lc_v2_reference.profile_version (
 tenant_id uuid NOT NULL, subject_id uuid NOT NULL, profile_version_id uuid NOT NULL,
 version bigint NOT NULL CHECK(version>0), payload jsonb NOT NULL,
 input_digest text NOT NULL CHECK(input_digest ~ '^[a-f0-9]{64}$'),
 created_at timestamptz NOT NULL DEFAULT now(),
 PRIMARY KEY(tenant_id,subject_id,profile_version_id),
 UNIQUE(tenant_id,subject_id,version),
 FOREIGN KEY(tenant_id,subject_id) REFERENCES lc_v2_reference.subject(tenant_id,subject_id)
);
CREATE TABLE lc_v2_reference.analysis_run (
 tenant_id uuid NOT NULL, subject_id uuid NOT NULL, run_id uuid NOT NULL,
 profile_version_id uuid NOT NULL, access_revision bigint NOT NULL CHECK(access_revision>0),
 product_release text NOT NULL, purpose text NOT NULL, version bigint NOT NULL DEFAULT 1,
 state text NOT NULL CHECK(state IN ('queued','running','blocked','review_required','published','failed','cancelled')),
 PRIMARY KEY(tenant_id,subject_id,run_id),
 FOREIGN KEY(tenant_id,subject_id,profile_version_id)
   REFERENCES lc_v2_reference.profile_version(tenant_id,subject_id,profile_version_id)
);
CREATE TABLE lc_v2_reference.claim (
 tenant_id uuid NOT NULL, subject_id uuid NOT NULL, claim_id uuid NOT NULL,
 run_id uuid NOT NULL, kind text NOT NULL CHECK(kind IN
 ('fact','self_report','observation','symbolic_interpretation','derived_metric','model_probability')),
 body text NOT NULL, evidence_ids jsonb NOT NULL CHECK(jsonb_typeof(evidence_ids)='array' AND jsonb_array_length(evidence_ids)>0),
 probability numeric, model_release_id text, target text, horizon text,
 PRIMARY KEY(tenant_id,subject_id,claim_id),
 FOREIGN KEY(tenant_id,subject_id,run_id) REFERENCES lc_v2_reference.analysis_run(tenant_id,subject_id,run_id),
 CHECK((kind='model_probability' AND probability BETWEEN 0 AND 1
       AND probability IS NOT NULL AND model_release_id IS NOT NULL AND target IS NOT NULL AND horizon IS NOT NULL)
    OR (kind<>'model_probability' AND probability IS NULL AND model_release_id IS NULL))
);
CREATE TABLE lc_v2_reference.idempotency_receipt (
 tenant_id uuid NOT NULL, actor_account_id uuid NOT NULL, operation text NOT NULL,
 idempotency_key text NOT NULL, payload_digest text NOT NULL,
 state text NOT NULL CHECK(state IN ('pending','running','completed','failed')),
 response_ref uuid, created_at timestamptz NOT NULL DEFAULT now(), expires_at timestamptz NOT NULL,
 PRIMARY KEY(tenant_id,actor_account_id,operation,idempotency_key)
);
CREATE TABLE lc_v2_reference.outbox_event (
 event_id uuid PRIMARY KEY, tenant_id uuid NOT NULL, subject_id uuid NOT NULL,
 run_id uuid NOT NULL, event_type text NOT NULL, payload jsonb NOT NULL,
 state text NOT NULL CHECK(state IN ('pending','leased','dispatched','dead_letter')),
 attempts integer NOT NULL DEFAULT 0 CHECK(attempts>=0), next_attempt_at timestamptz NOT NULL,
 lease_token uuid, lease_until timestamptz,
 FOREIGN KEY(tenant_id,subject_id,run_id) REFERENCES lc_v2_reference.analysis_run(tenant_id,subject_id,run_id)
);
CREATE INDEX outbox_due ON lc_v2_reference.outbox_event(state,next_attempt_at);
-- Read policies below are illustrative. Production writes and deletion require
-- separately reviewed policies/commands. No write permission is granted here.
ALTER TABLE lc_v2_reference.access_grant ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc_v2_reference.access_grant FORCE ROW LEVEL SECURITY;
CREATE POLICY own_grants ON lc_v2_reference.access_grant FOR SELECT USING (
 tenant_id = nullif(current_setting('app.tenant_id',true),'')::uuid
 AND grantee_account_id = nullif(current_setting('app.account_id',true),'')::uuid
);
CREATE FUNCTION lc_v2_reference.can_read_subject(t uuid,s uuid,rev bigint)
RETURNS boolean LANGUAGE sql STABLE SECURITY INVOKER AS $$
 SELECT EXISTS (SELECT 1 FROM lc_v2_reference.access_grant g
 WHERE g.tenant_id=t AND g.subject_id=s
 AND g.grantee_account_id=nullif(current_setting('app.account_id',true),'')::uuid
 AND g.purpose=current_setting('app.purpose',true)
 AND 'subject:read'=ANY(g.actions) AND g.state='active'
 AND g.permission_revision=rev AND g.valid_until>statement_timestamp())
$$;
ALTER TABLE lc_v2_reference.subject ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc_v2_reference.subject FORCE ROW LEVEL SECURITY;
CREATE POLICY subject_read ON lc_v2_reference.subject FOR SELECT USING (
 tenant_id=nullif(current_setting('app.tenant_id',true),'')::uuid
 AND state='active' AND lc_v2_reference.can_read_subject(tenant_id,subject_id,permission_revision)
);
ALTER TABLE lc_v2_reference.profile_version ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc_v2_reference.profile_version FORCE ROW LEVEL SECURITY;
CREATE POLICY profile_read ON lc_v2_reference.profile_version FOR SELECT USING (
 EXISTS(SELECT 1 FROM lc_v2_reference.subject s
 WHERE s.tenant_id=profile_version.tenant_id AND s.subject_id=profile_version.subject_id)
);
ALTER TABLE lc_v2_reference.analysis_run ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc_v2_reference.analysis_run FORCE ROW LEVEL SECURITY;
ALTER TABLE lc_v2_reference.claim ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc_v2_reference.claim FORCE ROW LEVEL SECURITY;
ALTER TABLE lc_v2_reference.idempotency_receipt ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc_v2_reference.idempotency_receipt FORCE ROW LEVEL SECURITY;
ALTER TABLE lc_v2_reference.outbox_event ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc_v2_reference.outbox_event FORCE ROW LEVEL SECURITY;
-- Remaining tables deny by default until operation-specific policies are reviewed.
-- Runtime role must NOT be schema owner, superuser, or BYPASSRLS.
-- Set context with parameterized set_config(..., true) in EACH transaction.
-- Reviewer must test as the actual runtime role; no claim of tested RLS here.
ROLLBACK;
