-- Life Code OS: schema logical reference 0.1; NOT a production migration.
-- No roles/passwords are created, no GRANTs provided, no permissive RLS policies.
-- All tables RLS enabled + FORCE; runtime must use non-owner, non-superuser roles.
-- Full policy, legacy mapping and PostgreSQL integration rehearsal are REQUIRED before use.
BEGIN;
CREATE SCHEMA IF NOT EXISTS lc;
REVOKE ALL ON SCHEMA lc FROM PUBLIC;

-- Không gian nghiệp vụ, không đồng nghĩa quyền đọc tất cả subject
CREATE TABLE lc.tenant (
  id uuid PRIMARY KEY,
  name text NOT NULL,
  kind text NOT NULL CHECK (kind IN ('personal','organization','partner')),
  country_pack_id text,
  state text NOT NULL DEFAULT 'pending',
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE lc.tenant ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.tenant FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.tenant FROM PUBLIC;

-- Identity binding được server xác minh
CREATE TABLE lc.account (
  id uuid PRIMARY KEY,
  idp_issuer text,
  idp_subject text,
  display_name text,
  status text NOT NULL DEFAULT 'pending',
  UNIQUE (idp_issuer, idp_subject),
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE lc.account ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.account FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.account FROM PUBLIC;

-- Seat/workspace membership không tự cấp PI grants
CREATE TABLE lc.tenant_membership (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  account_id uuid NOT NULL REFERENCES lc.account(id),
  role_code text NOT NULL,
  state text NOT NULL DEFAULT 'pending',
  expires_at timestamptz,
  UNIQUE (tenant_id, account_id, role_code),
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id)
);
ALTER TABLE lc.tenant_membership ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.tenant_membership FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.tenant_membership FROM PUBLIC;

-- Không lưu bearer plaintext
CREATE TABLE lc.auth_session (
  id uuid PRIMARY KEY,
  account_id uuid NOT NULL REFERENCES lc.account(id),
  token_digest bytea NOT NULL UNIQUE,
  expires_at timestamptz NOT NULL,
  revoked_at timestamptz,
  last_seen_at timestamptz,
  device_label text,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE lc.auth_session ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.auth_session FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.auth_session FROM PUBLIC;

-- Mục đích/căn cứ được legal phê duyệt
CREATE TABLE lc.processing_purpose (
  id uuid PRIMARY KEY,
  purpose_code text NOT NULL,
  version text NOT NULL,
  description text NOT NULL,
  lawful_basis_record text,
  status text NOT NULL DEFAULT 'draft',
  UNIQUE(purpose_code,version),
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE lc.processing_purpose ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.processing_purpose FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.processing_purpose FROM PUBLIC;

-- Notice/terms/retention có phiên bản
CREATE TABLE lc.policy_version (
  id uuid PRIMARY KEY,
  policy_code text NOT NULL,
  version text NOT NULL,
  locale text NOT NULL,
  content_digest text NOT NULL,
  approved_at timestamptz,
  UNIQUE(policy_code,version,locale),
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE lc.policy_version ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.policy_version FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.policy_version FROM PUBLIC;

-- Người được phân tích khác account
CREATE TABLE lc.profile_subject (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  controller_account_id uuid NOT NULL REFERENCES lc.account(id),
  display_name text NOT NULL,
  subject_kind text NOT NULL,
  state text NOT NULL DEFAULT 'pending',
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id)
);
ALTER TABLE lc.profile_subject ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.profile_subject FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.profile_subject FROM PUBLIC;

-- Grant cụ thể, server validate và DB enforce
CREATE TABLE lc.access_grant (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  subject_id uuid NOT NULL,
  grantee_account_id uuid NOT NULL REFERENCES lc.account(id),
  purpose_id uuid NOT NULL REFERENCES lc.processing_purpose(id),
  permissions jsonb NOT NULL,
  section_scope jsonb NOT NULL DEFAULT '[]',
  state text NOT NULL DEFAULT 'pending',
  expires_at timestamptz NOT NULL,
  revoked_at timestamptz,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id),
  UNIQUE(tenant_id,subject_id,id),
  FOREIGN KEY(tenant_id,subject_id) REFERENCES lc.profile_subject(tenant_id,id)
);
ALTER TABLE lc.access_grant ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.access_grant FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.access_grant FROM PUBLIC;

-- Ledger quyết định không overwrite
CREATE TABLE lc.consent_record (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  subject_id uuid NOT NULL,
  account_id uuid NOT NULL REFERENCES lc.account(id),
  purpose_id uuid NOT NULL REFERENCES lc.processing_purpose(id),
  policy_version_id uuid NOT NULL REFERENCES lc.policy_version(id),
  decision text NOT NULL CHECK(decision IN ('accept','withdraw')),
  scope jsonb NOT NULL,
  occurred_at timestamptz NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id),
  UNIQUE(tenant_id,subject_id,id),
  FOREIGN KEY(tenant_id,subject_id) REFERENCES lc.profile_subject(tenant_id,id)
);
ALTER TABLE lc.consent_record ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.consent_record FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.consent_record FROM PUBLIC;

-- Không silent fill, hypothesis giữ riêng
CREATE TABLE lc.profile_version (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  subject_id uuid NOT NULL,
  version_number integer NOT NULL CHECK(version_number>0),
  raw_fields jsonb NOT NULL,
  normalized_fields jsonb NOT NULL,
  source_assertions jsonb NOT NULL,
  supersedes_id uuid,
  UNIQUE(tenant_id,subject_id,version_number),
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id),
  UNIQUE(tenant_id,subject_id,id),
  FOREIGN KEY(tenant_id,subject_id) REFERENCES lc.profile_subject(tenant_id,id)
);
ALTER TABLE lc.profile_version ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.profile_version FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.profile_version FROM PUBLIC;

-- Ngày/năm/giờ khác nhau giữ thành phương án
CREATE TABLE lc.data_hypothesis (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  subject_id uuid NOT NULL,
  profile_version_id uuid NOT NULL,
  label text NOT NULL,
  proposed_fields jsonb NOT NULL,
  source_refs jsonb NOT NULL,
  state text NOT NULL DEFAULT 'unverified',
  FOREIGN KEY(tenant_id,subject_id,profile_version_id) REFERENCES lc.profile_version(tenant_id,subject_id,id),
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id),
  UNIQUE(tenant_id,subject_id,id),
  FOREIGN KEY(tenant_id,subject_id) REFERENCES lc.profile_subject(tenant_id,id)
);
ALTER TABLE lc.data_hypothesis ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.data_hypothesis FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.data_hypothesis FROM PUBLIC;

-- Nguồn công khai/phương pháp; không lưu PI khách
CREATE TABLE lc.source_record (
  id uuid PRIMARY KEY,
  source_code text NOT NULL UNIQUE,
  title text NOT NULL,
  canonical_url text,
  language_code text,
  access_state text NOT NULL DEFAULT 'not_read',
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE lc.source_record ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.source_record FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.source_record FROM PUBLIC;

-- Đúng lần in/trang/translation
CREATE TABLE lc.source_edition (
  id uuid PRIMARY KEY,
  source_id uuid NOT NULL REFERENCES lc.source_record(id),
  edition_label text NOT NULL,
  content_digest text,
  rights_state text NOT NULL DEFAULT 'pending',
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE lc.source_edition ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.source_edition FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.source_edition FROM PUBLIC;

-- Không mặc định ingest/train/distribute
CREATE TABLE lc.rights_record (
  id uuid PRIMARY KEY,
  source_edition_id uuid NOT NULL REFERENCES lc.source_edition(id),
  rights_scope jsonb NOT NULL,
  state text NOT NULL DEFAULT 'pending',
  expires_at timestamptz,
  legal_reference text,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE lc.rights_record ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.rights_record FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.rights_record FROM PUBLIC;

-- Danh mục K01–K20
CREATE TABLE lc.method (
  id uuid PRIMARY KEY,
  method_code text NOT NULL UNIQUE,
  family_code text NOT NULL,
  name text NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE lc.method ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.method FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.method FROM PUBLIC;

-- Release không edit inplace
CREATE TABLE lc.method_release (
  id uuid PRIMARY KEY,
  method_id uuid NOT NULL REFERENCES lc.method(id),
  version text NOT NULL,
  configuration jsonb NOT NULL,
  source_refs jsonb NOT NULL,
  limitations jsonb NOT NULL,
  state text NOT NULL DEFAULT 'draft',
  approved_by uuid REFERENCES lc.account(id),
  UNIQUE(method_id,version),
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE lc.method_release ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.method_release FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.method_release FROM PUBLIC;

-- Catalog/eligibility requirements server-defined
CREATE TABLE lc.product_release (
  id uuid PRIMARY KEY,
  product_code text NOT NULL,
  version text NOT NULL,
  requirements jsonb NOT NULL,
  method_release_refs jsonb NOT NULL,
  quota_policy jsonb NOT NULL,
  state text NOT NULL DEFAULT 'draft',
  UNIQUE(product_code,version),
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE lc.product_release ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.product_release FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.product_release FROM PUBLIC;

-- Nhật ký/self-report không trở thành fact tự động
CREATE TABLE lc.observation (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  subject_id uuid NOT NULL,
  purpose_id uuid NOT NULL REFERENCES lc.processing_purpose(id),
  kind text NOT NULL,
  occurred_at timestamptz NOT NULL,
  payload jsonb NOT NULL,
  source_kind text NOT NULL,
  instrument_release_ref text,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id),
  UNIQUE(tenant_id,subject_id,id),
  FOREIGN KEY(tenant_id,subject_id) REFERENCES lc.profile_subject(tenant_id,id)
);
ALTER TABLE lc.observation ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.observation FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.observation FROM PUBLIC;

-- Chốt profile/method config và quyền
CREATE TABLE lc.analysis_run (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  subject_id uuid NOT NULL,
  profile_version_id uuid NOT NULL,
  product_release_id uuid NOT NULL REFERENCES lc.product_release(id),
  purpose_id uuid NOT NULL REFERENCES lc.processing_purpose(id),
  requested_by uuid NOT NULL REFERENCES lc.account(id),
  state text NOT NULL DEFAULT 'queued',
  configuration_digest text NOT NULL,
  FOREIGN KEY(tenant_id,subject_id,profile_version_id) REFERENCES lc.profile_version(tenant_id,subject_id,id),
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id),
  UNIQUE(tenant_id,subject_id,id),
  FOREIGN KEY(tenant_id,subject_id) REFERENCES lc.profile_subject(tenant_id,id)
);
ALTER TABLE lc.analysis_run ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.analysis_run FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.analysis_run FROM PUBLIC;

-- Typed results nullable score; schema validated service+constraints
CREATE TABLE lc.method_result (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  subject_id uuid NOT NULL,
  analysis_run_id uuid NOT NULL,
  method_release_id uuid NOT NULL REFERENCES lc.method_release(id),
  result jsonb NOT NULL,
  state text NOT NULL,
  FOREIGN KEY(tenant_id,subject_id,analysis_run_id) REFERENCES lc.analysis_run(tenant_id,subject_id,id),
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id),
  UNIQUE(tenant_id,subject_id,id),
  FOREIGN KEY(tenant_id,subject_id) REFERENCES lc.profile_subject(tenant_id,id)
);
ALTER TABLE lc.method_result ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.method_result FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.method_result FROM PUBLIC;

-- Nhận định có lineage, không probability tượng trưng
CREATE TABLE lc.claim (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  subject_id uuid NOT NULL,
  method_result_id uuid,
  claim_type text NOT NULL CHECK(claim_type IN ('fact','self_report','observation','symbolic_interpretation','derived_metric','model_probability')),
  text_vi text NOT NULL,
  source_refs jsonb NOT NULL,
  probability numeric,
  model_release_ref text,
  state text NOT NULL DEFAULT 'draft',
  CHECK ((claim_type='model_probability' AND probability IS NOT NULL AND probability BETWEEN 0 AND 1 AND model_release_ref IS NOT NULL) OR (claim_type<>'model_probability' AND probability IS NULL AND model_release_ref IS NULL)),
  FOREIGN KEY(tenant_id,subject_id,method_result_id) REFERENCES lc.method_result(tenant_id,subject_id,id),
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id),
  UNIQUE(tenant_id,subject_id,id),
  FOREIGN KEY(tenant_id,subject_id) REFERENCES lc.profile_subject(tenant_id,id)
);
ALTER TABLE lc.claim ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.claim FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.claim FROM PUBLIC;

-- DAG lineage; cycle check tại service/test
CREATE TABLE lc.claim_dependency (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  subject_id uuid NOT NULL,
  claim_id uuid NOT NULL,
  depends_on_claim_id uuid NOT NULL,
  FOREIGN KEY(tenant_id,subject_id,claim_id) REFERENCES lc.claim(tenant_id,subject_id,id),
  FOREIGN KEY(tenant_id,subject_id,depends_on_claim_id) REFERENCES lc.claim(tenant_id,subject_id,id),
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id),
  UNIQUE(tenant_id,subject_id,id),
  FOREIGN KEY(tenant_id,subject_id) REFERENCES lc.profile_subject(tenant_id,id)
);
ALTER TABLE lc.claim_dependency ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.claim_dependency FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.claim_dependency FROM PUBLIC;

-- Approved snapshots không tự sửa; vẫn chịu deletion
CREATE TABLE lc.report_snapshot (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  subject_id uuid NOT NULL,
  product_release_id uuid NOT NULL REFERENCES lc.product_release(id),
  content_revision text NOT NULL,
  content_tree jsonb NOT NULL,
  source_snapshot jsonb NOT NULL,
  state text NOT NULL DEFAULT 'draft',
  reviewer_account_id uuid REFERENCES lc.account(id),
  digest text NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id),
  UNIQUE(tenant_id,subject_id,id),
  FOREIGN KEY(tenant_id,subject_id) REFERENCES lc.profile_subject(tenant_id,id)
);
ALTER TABLE lc.report_snapshot ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.report_snapshot FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.report_snapshot FROM PUBLIC;

-- Chỉ qua authorized proxy/short URL
CREATE TABLE lc.report_artifact (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  subject_id uuid NOT NULL,
  report_snapshot_id uuid NOT NULL,
  format text NOT NULL CHECK(format IN ('pdf','docx','html','markdown')),
  private_object_key text NOT NULL,
  sha256 text NOT NULL,
  expires_at timestamptz,
  FOREIGN KEY(tenant_id,subject_id,report_snapshot_id) REFERENCES lc.report_snapshot(tenant_id,subject_id,id),
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id),
  UNIQUE(tenant_id,subject_id,id),
  FOREIGN KEY(tenant_id,subject_id) REFERENCES lc.profile_subject(tenant_id,id)
);
ALTER TABLE lc.report_artifact ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.report_artifact FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.report_artifact FROM PUBLIC;

-- Quyền lựa chọn người dùng
CREATE TABLE lc.action_plan (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  subject_id uuid NOT NULL,
  title text NOT NULL,
  goal text NOT NULL,
  success_measure jsonb NOT NULL,
  horizon_days integer NOT NULL CHECK(horizon_days>0),
  state text NOT NULL DEFAULT 'draft',
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id),
  UNIQUE(tenant_id,subject_id,id),
  FOREIGN KEY(tenant_id,subject_id) REFERENCES lc.profile_subject(tenant_id,id)
);
ALTER TABLE lc.action_plan ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.action_plan FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.action_plan FROM PUBLIC;

-- Action không tự hoàn thành vì AI viết
CREATE TABLE lc.action_item (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  subject_id uuid NOT NULL,
  action_plan_id uuid NOT NULL,
  description text NOT NULL,
  due_at timestamptz,
  state text NOT NULL DEFAULT 'open',
  FOREIGN KEY(tenant_id,subject_id,action_plan_id) REFERENCES lc.action_plan(tenant_id,subject_id,id),
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id),
  UNIQUE(tenant_id,subject_id,id),
  FOREIGN KEY(tenant_id,subject_id) REFERENCES lc.profile_subject(tenant_id,id)
);
ALTER TABLE lc.action_item ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.action_item FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.action_item FROM PUBLIC;

-- Check-in và review
CREATE TABLE lc.action_outcome (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  subject_id uuid NOT NULL,
  action_item_id uuid NOT NULL,
  observed_at timestamptz NOT NULL,
  state text NOT NULL,
  note text,
  FOREIGN KEY(tenant_id,subject_id,action_item_id) REFERENCES lc.action_item(tenant_id,subject_id,id),
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id),
  UNIQUE(tenant_id,subject_id,id),
  FOREIGN KEY(tenant_id,subject_id) REFERENCES lc.profile_subject(tenant_id,id)
);
ALTER TABLE lc.action_outcome ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.action_outcome FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.action_outcome FROM PUBLIC;

-- Money integer minor units; no JSfloat authority
CREATE TABLE lc.commerce_order (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  account_id uuid NOT NULL REFERENCES lc.account(id),
  product_release_id uuid NOT NULL REFERENCES lc.product_release(id),
  amount_minor bigint NOT NULL CHECK(amount_minor>=0),
  currency text NOT NULL,
  state text NOT NULL DEFAULT 'pending',
  quote_version text NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id)
);
ALTER TABLE lc.commerce_order ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.commerce_order FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.commerce_order FROM PUBLIC;

-- Verify signature before businessprocessing; state ordering
CREATE TABLE lc.payment_event (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  commerce_order_id uuid,
  provider_code text NOT NULL,
  provider_event_id text NOT NULL,
  payload_digest text NOT NULL,
  signature_verified boolean NOT NULL DEFAULT false,
  state text NOT NULL DEFAULT 'received',
  UNIQUE(provider_code,provider_event_id),
  FOREIGN KEY(tenant_id,commerce_order_id) REFERENCES lc.commerce_order(tenant_id,id),
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id)
);
ALTER TABLE lc.payment_event ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.payment_event FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.payment_event FROM PUBLIC;

-- Không phải access_grant
CREATE TABLE lc.entitlement (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  account_id uuid NOT NULL REFERENCES lc.account(id),
  product_release_id uuid NOT NULL REFERENCES lc.product_release(id),
  commerce_order_id uuid,
  state text NOT NULL DEFAULT 'pending',
  expires_at timestamptz,
  FOREIGN KEY(tenant_id,commerce_order_id) REFERENCES lc.commerce_order(tenant_id,id),
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id)
);
ALTER TABLE lc.entitlement ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.entitlement FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.entitlement FROM PUBLIC;

-- Assignment không tự cho mọi nội dung
CREATE TABLE lc.practitioner_case (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  subject_id uuid NOT NULL,
  practitioner_account_id uuid NOT NULL REFERENCES lc.account(id),
  purpose_id uuid NOT NULL REFERENCES lc.processing_purpose(id),
  scope jsonb NOT NULL,
  state text NOT NULL DEFAULT 'pending',
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id),
  UNIQUE(tenant_id,subject_id,id),
  FOREIGN KEY(tenant_id,subject_id) REFERENCES lc.profile_subject(tenant_id,id)
);
ALTER TABLE lc.practitioner_case ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.practitioner_case FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.practitioner_case FROM PUBLIC;

-- Học liệu version, không chứng chỉ lâm sàng
CREATE TABLE lc.academy_enrollment (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  account_id uuid NOT NULL REFERENCES lc.account(id),
  course_release_ref text NOT NULL,
  state text NOT NULL DEFAULT 'pending',
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id)
);
ALTER TABLE lc.academy_enrollment ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.academy_enrollment FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.academy_enrollment FROM PUBLIC;

-- Public view tối thiểu, revoke/expiry
CREATE TABLE lc.certificate (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  enrollment_id uuid NOT NULL,
  public_verification_id text NOT NULL UNIQUE,
  scope jsonb NOT NULL,
  state text NOT NULL DEFAULT 'pending',
  expires_at timestamptz,
  FOREIGN KEY(tenant_id,enrollment_id) REFERENCES lc.academy_enrollment(tenant_id,id),
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id)
);
ALTER TABLE lc.certificate ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.certificate FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.certificate FROM PUBLIC;

-- Locale không đồng nghĩa legal permission
CREATE TABLE lc.country_pack (
  id uuid PRIMARY KEY,
  country_code text NOT NULL,
  version text NOT NULL,
  policy jsonb NOT NULL,
  legal_review_ref text,
  state text NOT NULL DEFAULT 'draft',
  UNIQUE(country_code,version),
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE lc.country_pack ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.country_pack FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.country_pack FROM PUBLIC;

-- License/franchise legal classification riêng
CREATE TABLE lc.partner_license (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  country_pack_id uuid NOT NULL REFERENCES lc.country_pack(id),
  allowed_capabilities jsonb NOT NULL,
  agreement_reference text NOT NULL,
  state text NOT NULL DEFAULT 'pending',
  expires_at timestamptz,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id)
);
ALTER TABLE lc.partner_license ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.partner_license FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.partner_license FROM PUBLIC;

-- Atomic with business transaction
CREATE TABLE lc.outbox_event (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  aggregate_type text NOT NULL,
  aggregate_id uuid NOT NULL,
  event_type text NOT NULL,
  payload_reference text NOT NULL,
  state text NOT NULL DEFAULT 'pending',
  published_at timestamptz,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id)
);
ALTER TABLE lc.outbox_event ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.outbox_event FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.outbox_event FROM PUBLIC;

-- Durable dedup; compare digest; no memoryledger production
CREATE TABLE lc.job_receipt (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  namespace text NOT NULL,
  idempotency_key text NOT NULL,
  request_digest text NOT NULL,
  result_reference text,
  state text NOT NULL DEFAULT 'pending',
  UNIQUE(tenant_id,namespace,idempotency_key),
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id)
);
ALTER TABLE lc.job_receipt ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.job_receipt FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.job_receipt FROM PUBLIC;

-- No raw PII or tokens; policy retention
CREATE TABLE lc.audit_event (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  actor_account_id uuid REFERENCES lc.account(id),
  action_code text NOT NULL,
  resource_type text NOT NULL,
  resource_id uuid,
  minimal_metadata jsonb NOT NULL,
  occurred_at timestamptz NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id)
);
ALTER TABLE lc.audit_event ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.audit_event FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.audit_event FROM PUBLIC;

-- Track all stores and backup tombstone
CREATE TABLE lc.deletion_job (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  subject_id uuid NOT NULL,
  requestor_account_id uuid NOT NULL REFERENCES lc.account(id),
  scope jsonb NOT NULL,
  state text NOT NULL DEFAULT 'requested',
  receipt jsonb,
  completed_at timestamptz,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id),
  UNIQUE(tenant_id,subject_id,id),
  FOREIGN KEY(tenant_id,subject_id) REFERENCES lc.profile_subject(tenant_id,id)
);
ALTER TABLE lc.deletion_job ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.deletion_job FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.deletion_job FROM PUBLIC;

-- Có giới hạn và legal review, không vô thời hạn
CREATE TABLE lc.legal_hold (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  subject_id uuid NOT NULL,
  reason_reference text NOT NULL,
  approved_by uuid NOT NULL REFERENCES lc.account(id),
  expires_at timestamptz NOT NULL,
  state text NOT NULL DEFAULT 'active',
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id),
  UNIQUE(tenant_id,subject_id,id),
  FOREIGN KEY(tenant_id,subject_id) REFERENCES lc.profile_subject(tenant_id,id)
);
ALTER TABLE lc.legal_hold ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.legal_hold FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.legal_hold FROM PUBLIC;

-- Không PI raw; replay trước restoreopening
CREATE TABLE lc.revocation_tombstone (
  id uuid PRIMARY KEY,
  tenant_id uuid NOT NULL REFERENCES lc.tenant(id),
  resource_digest text NOT NULL,
  reason_code text NOT NULL,
  effective_at timestamptz NOT NULL,
  expires_at timestamptz,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE(tenant_id,id)
);
ALTER TABLE lc.revocation_tombstone ENABLE ROW LEVEL SECURITY;
ALTER TABLE lc.revocation_tombstone FORCE ROW LEVEL SECURITY;
REVOKE ALL ON lc.revocation_tombstone FROM PUBLIC;

COMMIT;
-- Do not add a universal tenant_id-only policy for personal data.
-- A service policy must also verify principal, object grant, purpose, expiry and resource state.
