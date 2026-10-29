# Gói thiết kế response cho 46 operation generic

Ngày: **2026-10-20**  
Trạng thái: **DESIGN_APPROVAL_PENDING / NOT_IMPLEMENTED / NOT_CODEGEN_READY**

File JSON `API_RESPONSE_DESIGN_PACKETS.json` là registry máy đọc. Tài liệu này trình bày cùng 46 packet để DEV thấy rõ phần nào đã có nguồn và phần nào còn bị chặn. Không packet nào đã được nhập vào `openapi.resolved.yaml`; số blocker canonical vẫn là 46 cho đến khi từng packet có schema, field-level authorization test và receipt phê duyệt đúng artifact.

## Quy tắc chung

- No proposed schema in this registry changes openapi.resolved.yaml.
- A field absent from the applicable whitelist must not be returned.
- Public projection is empty unless explicitly listed per packet.
- Private fields require server-resolved principal, resource lineage, purpose and field scope.
- Server-only fields must never be serialized, logged into public traces or copied into deny responses.
- Named schema proposal is not evidence that the entity, query, authorization or release exists.
- Every approval receipt is missing until an immutable receipt identifies scope, artifact digest, reviewer and decision.

`public_projection`, `authorized_private_projection` và `server_only_never_return` là allowlist tách biệt. Danh sách rỗng là quyết định fail-closed, không phải thiếu sót để DEV tự điền. Nullable phải có semantic duy nhất; nếu không, thêm `missing_reason` enum trước approval.

## Chỉ mục

| # | Operation | Route | Named response đề xuất | Source model |
|---:|---|---|---|---|
| 001 | `catalog` | `GET /catalog` | `CatalogProductPage` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 002 | `methods` | `GET /methods` | `PublishedMethodPage` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 003 | `subjects` | `GET /subjects` | `SubjectSummaryPage` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 004 | `createSubject` | `POST /subjects` | `SubjectRecord` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 005 | `subject` | `GET /subjects/{subjectId}` | `SubjectRecord` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 006 | `overview` | `GET /subjects/{subjectId}/overview` | `SubjectOverview` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 007 | `newHypothesis` | `POST /subjects/{subjectId}/hypotheses` | `DataHypothesis` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 008 | `consents` | `GET /subjects/{subjectId}/consents` | `ConsentRecordPage` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 009 | `consentDecision` | `POST /subjects/{subjectId}/consents` | `ConsentRecord` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 010 | `grants` | `GET /subjects/{subjectId}/grants` | `AccessGrantPage` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 011 | `grant` | `POST /subjects/{subjectId}/grants` | `AccessGrant` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 012 | `observations` | `GET /subjects/{subjectId}/observations` | `ObservationPage` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 013 | `observation` | `POST /subjects/{subjectId}/observations` | `ObservationRecord` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 014 | `questionnaireResponse` | `POST /subjects/{subjectId}/questionnaire-responses` | `QuestionnaireSubmissionReceipt` | BLOCKED_SOURCE_MODEL_GAP |
| 015 | `createPlan` | `POST /subjects/{subjectId}/plans` | `ActionPlan` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 016 | `plans` | `GET /subjects/{subjectId}/plans` | `ActionPlanPage` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 017 | `checkin` | `POST /actions/{actionId}/check-ins` | `ActionOutcome` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 018 | `timeline` | `GET /subjects/{subjectId}/timeline` | `SubjectTimelinePage` | BLOCKED_SOURCE_MODEL_GAP |
| 019 | `analysisStatus` | `GET /analysis-runs/{runId}` | `AnalysisRunStatus` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 020 | `cancelAnalysis` | `POST /analysis-runs/{runId}/cancel` | `AnalysisRunStatus` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 021 | `reports` | `GET /subjects/{subjectId}/reports` | `ReportSnapshotPage` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 022 | `reportRevisions` | `GET /reports/{reportId}/revisions` | `ReportRevisionPage` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 023 | `review` | `POST /reports/{reportId}/reviews` | `ReportReviewReceipt` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 024 | `publish` | `POST /reports/{reportId}/publish` | `ReportPublicationReceipt` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 025 | `order` | `POST /orders` | `CommerceOrder` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 026 | `orderStatus` | `GET /orders/{orderId}` | `CommerceOrder` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 027 | `checkout` | `POST /orders/{orderId}/checkout` | `CommerceOrder` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 028 | `requestRefund` | `POST /orders/{orderId}/refund-requests` | `JobAccepted` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 029 | `paymentWebhook` | `POST /webhooks/payments/{providerId}` | `PaymentWebhookReceipt` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 030 | `entitlements` | `GET /entitlements` | `EntitlementPage` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 031 | `ticket` | `POST /support/tickets` | `SupportTicket` | BLOCKED_SOURCE_MODEL_GAP |
| 032 | `ticketStatus` | `GET /support/tickets/{ticketId}` | `SupportTicketStatus` | BLOCKED_SOURCE_MODEL_GAP |
| 033 | `deletionStatus` | `GET /deletion-jobs/{jobId}` | `DeletionJobStatus` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 034 | `jobStatus` | `GET /jobs/{jobId}` | `JobStatus` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 035 | `newAutomation` | `POST /automations` | `AutomationRecord` | BLOCKED_SOURCE_MODEL_GAP |
| 036 | `cases` | `GET /practice/cases` | `PractitionerCasePage` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 037 | `caseDetail` | `GET /practice/cases/{caseId}` | `PractitionerCase` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 038 | `courses` | `GET /academy/courses` | `CourseReleasePage` | BLOCKED_SOURCE_MODEL_GAP |
| 039 | `assignment` | `POST /academy/assignments` | `AssignmentSubmissionReceipt` | BLOCKED_SOURCE_MODEL_GAP |
| 040 | `verifyCertificate` | `GET /certificates/{certificateId}` | `CertificatePublicVerification` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 041 | `organizationOverview` | `GET /organizations/{organizationId}/overview` | `OrganizationOverview` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 042 | `partner` | `GET /partners/{partnerId}` | `PartnerLicenseView` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 043 | `methodReleaseDraft` | `POST /admin/method-releases` | `MethodRelease` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 044 | `countryPackReview` | `POST /admin/country-packs` | `CountryPackReviewRecord` | GROUNDED_PROPOSAL_REQUIRES_REVIEW |
| 045 | `quality` | `GET /admin/quality` | `QualityMetadataSnapshot` | BLOCKED_SOURCE_MODEL_GAP |
| 046 | `operations` | `GET /admin/operations` | `OperationsMetadataSnapshot` | BLOCKED_SOURCE_MODEL_GAP |

## Packet chi tiết

### RDP-001 catalog

- Route: `GET /catalog`; success `200`; generic hiện tại `#/components/schemas/ResourcePage`.
- Named proposal: `CatalogProductPage` (page); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `product_release`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `items`, `next_cursor`, `items[].product_code`, `items[].version`.
- Public whitelist: `items`, `next_cursor`, `items[].product_code`, `items[].version`.
- Authorized-private whitelist: _rỗng có chủ đích_.
- Server-only, cấm trả: `items[].requirements`, `items[].quota_policy`, `internal_id`.
- Nullable: `next_cursor`; unknown không dùng sentinel.
- Scope: `public` / `public_read`; published_public_projection_only; deny `public_problem`.
- Failure cases: `unpublished_or_nonpublic_resource_is_not_disclosed`, `unpublished_or_suspended_product_is_omitted`, `invalid_cursor_is_rejected`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `PRIVACY_PUBLIC_PROJECTION_RECEIPT`.
- Câu hỏi mở: Chưa có entity/field cho tên hiển thị, mô tả, locale và giá; DEV không được suy từ product_code. Cần quyết định requirements hoặc quota_policy nào thật sự là public projection.

### RDP-002 methods

- Route: `GET /methods`; success `200`; generic hiện tại `#/components/schemas/ResourcePage`.
- Named proposal: `PublishedMethodPage` (page); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `method`, `method_release`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `items`, `next_cursor`, `items[].method_code`, `items[].family_code`, `items[].name`.
- Public whitelist: `items`, `next_cursor`, `items[].method_code`, `items[].family_code`, `items[].name`, `items[].release.version`, `items[].release.limitations`.
- Authorized-private whitelist: _rỗng có chủ đích_.
- Server-only, cấm trả: `items[].release.configuration`, `items[].release.source_refs`, `items[].release.approved_by`.
- Nullable: `next_cursor`; unknown không dùng sentinel.
- Scope: `public` / `public_read`; published_public_projection_only; deny `public_problem`.
- Failure cases: `unpublished_or_nonpublic_resource_is_not_disclosed`, `draft_or_blocked_method_is_omitted`, `country_or_product_scope_mismatch_is_omitted`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-001`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `PRIVACY_PUBLIC_PROJECTION_RECEIPT`, `METHOD_GOVERNANCE_APPROVAL_RECEIPT`, `SOURCE_RIGHTS_APPROVAL_RECEIPT`.
- Câu hỏi mở: Chưa chốt có công khai source locator/rights summary hay không. Chỉ release đủ gate permitted_for_product mới được vào projection; receipt cụ thể hiện vẫn thiếu.

### RDP-003 subjects

- Route: `GET /subjects`; success `200`; generic hiện tại `#/components/schemas/ResourcePage`.
- Named proposal: `SubjectSummaryPage` (page); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `profile_subject`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `items`, `next_cursor`, `items[].subject_id`, `items[].display_name`, `items[].subject_kind`, `items[].state`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `items`, `next_cursor`, `items[].subject_id`, `items[].display_name`, `items[].subject_kind`, `items[].state`.
- Server-only, cấm trả: `items[].controller_account_id`, `items[].tenant_id`.
- Nullable: `next_cursor`; unknown không dùng sentinel.
- Scope: `self` / `session_self`; principal_account_from_session_only; deny `401_or_403_without_private_metadata`.
- Failure cases: `missing_or_invalid_session_is_401`, `suspended_account_is_denied_without_private_metadata`, `subject_without_effective_scope_is_not_listed`, `invalid_cursor_is_rejected`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`.
- Câu hỏi mở: Pagination/sort key chưa được chốt; không dùng display_name làm cursor.

### RDP-004 createSubject

- Route: `POST /subjects`; success `201`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `SubjectRecord` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `profile_subject`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `subject_id`, `display_name`, `subject_kind`, `state`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `subject_id`, `display_name`, `subject_kind`, `state`.
- Server-only, cấm trả: `controller_account_id`, `tenant_id`.
- Nullable: _rỗng có chủ đích_; unknown không dùng sentinel.
- Scope: `self` / `session_self`; principal_account_from_session_only; deny `401_or_403_without_private_metadata`.
- Failure cases: `missing_or_invalid_session_is_401`, `suspended_account_is_denied_without_private_metadata`, `missing_or_invalid_csrf_is_403`, `third_party_subject_creation_is_denied_until_released`, `purpose_or_notice_version_invalid_is_rejected`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `CSRF_AND_IDEMPOTENCY_TEST_RECEIPT`, `PRIVACY_SUBJECT_CREATION_RECEIPT`.
- Câu hỏi mở: Beta adult-self có cho tạo subject_kind nào ngoài self hay không cần Founder/privacy approval.

### RDP-005 subject

- Route: `GET /subjects/{subjectId}`; success `200`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `SubjectRecord` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `profile_subject`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `subject_id`, `display_name`, `subject_kind`, `state`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `subject_id`, `display_name`, `subject_kind`, `state`.
- Server-only, cấm trả: `controller_account_id`, `tenant_id`.
- Nullable: _rỗng có chủ đích_; unknown không dùng sentinel.
- Scope: `subject:read` / `subject_scoped`; single_query_tenant_subject_object_lineage; deny `404_for_out_of_scope_object_403_for_disallowed_action`.
- Failure cases: `wrong_tenant_or_subject_is_404`, `wrong_purpose_action_or_field_scope_is_403`, `revoked_grant_is_rechecked`, `wrong_subject_or_tenant_is_404`, `inactive_subject_state_is_handled_without_metadata_leak`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`.
- Câu hỏi mở: Có cần ETag/version cho concurrent update dù endpoint hiện chỉ GET hay không.

### RDP-006 overview

- Route: `GET /subjects/{subjectId}/overview`; success `200`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `SubjectOverview` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `profile_subject`, `profile_version`, `analysis_run`, `report_snapshot`, `action_plan`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `subject`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `subject`, `subject.subject_id`, `subject.display_name`, `subject.subject_kind`, `subject.state`, `current_profile_version_id`, `latest_analysis_run_id`, `latest_report_snapshot_id`, `active_action_plan_ids`.
- Server-only, cấm trả: `controller_account_id`, `tenant_id`, `raw_fields`, `normalized_fields`, `configuration_digest`.
- Nullable: `current_profile_version_id`, `latest_analysis_run_id`, `latest_report_snapshot_id`; unknown không dùng sentinel.
- Scope: `subject:read` / `subject_scoped`; single_query_tenant_subject_object_lineage; deny `404_for_out_of_scope_object_403_for_disallowed_action`.
- Failure cases: `wrong_tenant_or_subject_is_404`, `wrong_purpose_action_or_field_scope_is_403`, `revoked_grant_is_rechecked`, `wrong_subject_or_tenant_is_404`, `revoked_grant_filters_every_nested_reference`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-005`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`.
- Câu hỏi mở: Chưa có rule chọn current/latest; phải định nghĩa theo immutable version/state, không dựa vào updated_at ngầm định. Chưa chốt overview có trả counts, links hay embedded summaries.

### RDP-007 newHypothesis

- Route: `POST /subjects/{subjectId}/hypotheses`; success `201`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `DataHypothesis` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `data_hypothesis`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `hypothesis_id`, `profile_version_id`, `label`, `proposed_fields`, `source_refs`, `state`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `hypothesis_id`, `profile_version_id`, `label`, `proposed_fields`, `source_refs`, `state`.
- Server-only, cấm trả: `tenant_id`, `subject_id`.
- Nullable: _rỗng có chủ đích_; unknown không dùng sentinel.
- Scope: `subject:write` / `subject_scoped`; single_query_tenant_subject_object_lineage; deny `404_for_out_of_scope_object_403_for_disallowed_action`.
- Failure cases: `wrong_tenant_or_subject_is_404`, `wrong_purpose_action_or_field_scope_is_403`, `revoked_grant_is_rechecked`, `missing_or_invalid_csrf_is_403`, `profile_version_out_of_scope_is_404`, `unsupported_or_forbidden_field_path_is_400`, `stale_profile_version_is_409_or_412`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-005`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `CSRF_AND_IDEMPOTENCY_TEST_RECEIPT`, `DATA_FIELD_SCOPE_REVIEW_RECEIPT`.
- Câu hỏi mở: Enum state và transition của hypothesis chưa được khóa trong ENTITY_REGISTRY. Cần field-level allowlist cho proposed_fields theo DATA_FIELD_REGISTRY_120.

### RDP-008 consents

- Route: `GET /subjects/{subjectId}/consents`; success `200`; generic hiện tại `#/components/schemas/ResourcePage`.
- Named proposal: `ConsentRecordPage` (page); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `consent_record`, `processing_purpose`, `policy_version`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `items`, `next_cursor`, `items[].consent_id`, `items[].purpose_id`, `items[].policy_version_id`, `items[].decision`, `items[].scope`, `items[].occurred_at`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `items`, `next_cursor`, `items[].consent_id`, `items[].purpose_id`, `items[].policy_version_id`, `items[].decision`, `items[].scope`, `items[].occurred_at`.
- Server-only, cấm trả: `items[].account_id`, `items[].tenant_id`, `items[].subject_id`.
- Nullable: `next_cursor`; unknown không dùng sentinel.
- Scope: `subject:read` / `subject_scoped`; single_query_tenant_subject_object_lineage; deny `404_for_out_of_scope_object_403_for_disallowed_action`.
- Failure cases: `wrong_tenant_or_subject_is_404`, `wrong_purpose_action_or_field_scope_is_403`, `revoked_grant_is_rechecked`, `wrong_subject_is_404`, `withdrawal_history_is_append_only`, `invalid_cursor_is_rejected`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `PRIVACY_CONSENT_CONTRACT_RECEIPT`.
- Câu hỏi mở: Có trả purpose_code/policy locale projection thay ID hay không chưa chốt.

### RDP-009 consentDecision

- Route: `POST /subjects/{subjectId}/consents`; success `201`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `ConsentRecord` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `consent_record`, `processing_purpose`, `policy_version`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `consent_id`, `purpose_id`, `policy_version_id`, `decision`, `scope`, `occurred_at`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `consent_id`, `purpose_id`, `policy_version_id`, `decision`, `scope`, `occurred_at`.
- Server-only, cấm trả: `account_id`, `tenant_id`, `subject_id`.
- Nullable: _rỗng có chủ đích_; unknown không dùng sentinel.
- Scope: `subject:consent` / `subject_scoped`; single_query_tenant_subject_object_lineage; deny `404_for_out_of_scope_object_403_for_disallowed_action`.
- Failure cases: `wrong_tenant_or_subject_is_404`, `wrong_purpose_action_or_field_scope_is_403`, `revoked_grant_is_rechecked`, `missing_or_invalid_csrf_is_403`, `inactive_purpose_or_policy_version_is_400`, `wrong_subject_is_404`, `duplicate_decision_has_defined_idempotent_semantics`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-004`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `CSRF_AND_IDEMPOTENCY_TEST_RECEIPT`, `PRIVACY_CONSENT_CONTRACT_RECEIPT`.
- Câu hỏi mở: Server timestamp source và idempotency behavior của lặp accept/withdraw cần chốt.

### RDP-010 grants

- Route: `GET /subjects/{subjectId}/grants`; success `200`; generic hiện tại `#/components/schemas/ResourcePage`.
- Named proposal: `AccessGrantPage` (page); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `access_grant`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `items`, `next_cursor`, `items[].grant_id`, `items[].grantee_account_id`, `items[].purpose_id`, `items[].permissions`, `items[].section_scope`, `items[].state`, `items[].expires_at`, `items[].revoked_at`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `items`, `next_cursor`, `items[].grant_id`, `items[].grantee_account_id`, `items[].purpose_id`, `items[].permissions`, `items[].section_scope`, `items[].state`, `items[].expires_at`, `items[].revoked_at`.
- Server-only, cấm trả: `items[].tenant_id`, `items[].subject_id`.
- Nullable: `next_cursor`, `items[].revoked_at`; unknown không dùng sentinel.
- Scope: `subject:share` / `subject_scoped`; single_query_tenant_subject_object_lineage; deny `404_for_out_of_scope_object_403_for_disallowed_action`.
- Failure cases: `wrong_tenant_or_subject_is_404`, `wrong_purpose_action_or_field_scope_is_403`, `revoked_grant_is_rechecked`, `wrong_subject_is_404`, `membership_without_subject_grant_is_denied`, `invalid_cursor_is_rejected`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `PRIVACY_SHARING_APPROVAL_RECEIPT`.
- Câu hỏi mở: Grantee display projection chưa có privacy rule; chỉ account ID được nguồn hóa hiện tại.

### RDP-011 grant

- Route: `POST /subjects/{subjectId}/grants`; success `201`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `AccessGrant` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `access_grant`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `grant_id`, `grantee_account_id`, `purpose_id`, `permissions`, `section_scope`, `state`, `expires_at`, `revoked_at`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `grant_id`, `grantee_account_id`, `purpose_id`, `permissions`, `section_scope`, `state`, `expires_at`, `revoked_at`.
- Server-only, cấm trả: `tenant_id`, `subject_id`.
- Nullable: `revoked_at`; unknown không dùng sentinel.
- Scope: `subject:share` / `subject_scoped`; single_query_tenant_subject_object_lineage; deny `404_for_out_of_scope_object_403_for_disallowed_action`.
- Failure cases: `wrong_tenant_or_subject_is_404`, `wrong_purpose_action_or_field_scope_is_403`, `revoked_grant_is_rechecked`, `missing_or_invalid_csrf_is_403`, `grantee_or_purpose_invalid_is_400`, `grant_beyond_actor_scope_is_403`, `duplicate_or_conflicting_grant_is_409`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `CSRF_AND_IDEMPOTENCY_TEST_RECEIPT`, `PRIVACY_SHARING_APPROVAL_RECEIPT`.
- Câu hỏi mở: Permission enum, section identifiers và minimum/maximum expiry chưa được định nghĩa.

### RDP-012 observations

- Route: `GET /subjects/{subjectId}/observations`; success `200`; generic hiện tại `#/components/schemas/ResourcePage`.
- Named proposal: `ObservationPage` (page); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `observation`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `items`, `next_cursor`, `items[].observation_id`, `items[].purpose_id`, `items[].kind`, `items[].occurred_at`, `items[].payload`, `items[].source_kind`, `items[].instrument_release_ref`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `items`, `next_cursor`, `items[].observation_id`, `items[].purpose_id`, `items[].kind`, `items[].occurred_at`, `items[].payload`, `items[].source_kind`, `items[].instrument_release_ref`.
- Server-only, cấm trả: `items[].tenant_id`, `items[].subject_id`.
- Nullable: `next_cursor`, `items[].instrument_release_ref`; unknown không dùng sentinel.
- Scope: `subject:read` / `subject_scoped`; single_query_tenant_subject_object_lineage; deny `404_for_out_of_scope_object_403_for_disallowed_action`.
- Failure cases: `wrong_tenant_or_subject_is_404`, `wrong_purpose_action_or_field_scope_is_403`, `revoked_grant_is_rechecked`, `wrong_subject_is_404`, `payload_kind_schema_mismatch_is_400`, `invalid_cursor_is_rejected`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-005`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `DATA_FIELD_SCOPE_REVIEW_RECEIPT`.
- Câu hỏi mở: Payload cần discriminated schema theo kind; object mở không được xem là codegen-ready.

### RDP-013 observation

- Route: `POST /subjects/{subjectId}/observations`; success `201`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `ObservationRecord` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `observation`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `observation_id`, `purpose_id`, `kind`, `occurred_at`, `payload`, `source_kind`, `instrument_release_ref`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `observation_id`, `purpose_id`, `kind`, `occurred_at`, `payload`, `source_kind`, `instrument_release_ref`.
- Server-only, cấm trả: `tenant_id`, `subject_id`.
- Nullable: `instrument_release_ref`; unknown không dùng sentinel.
- Scope: `subject:write` / `subject_scoped`; single_query_tenant_subject_object_lineage; deny `404_for_out_of_scope_object_403_for_disallowed_action`.
- Failure cases: `wrong_tenant_or_subject_is_404`, `wrong_purpose_action_or_field_scope_is_403`, `revoked_grant_is_rechecked`, `missing_or_invalid_csrf_is_403`, `wrong_subject_is_404`, `payload_kind_schema_mismatch_is_400`, `inactive_instrument_release_is_400`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-005`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `CSRF_AND_IDEMPOTENCY_TEST_RECEIPT`, `DATA_FIELD_SCOPE_REVIEW_RECEIPT`.
- Câu hỏi mở: Payload cần discriminated schema theo kind và size limit.

### RDP-014 questionnaireResponse

- Route: `POST /subjects/{subjectId}/questionnaire-responses`; success `201`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `QuestionnaireSubmissionReceipt` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `observation`. Trạng thái nguồn: `BLOCKED_SOURCE_MODEL_GAP`.
- Required: _rỗng có chủ đích_.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: _rỗng có chủ đích_.
- Server-only, cấm trả: `raw_answers`, `scoring_output`, `tenant_id`, `subject_id`.
- Nullable: _rỗng có chủ đích_; unknown không dùng sentinel.
- Scope: `subject:write` / `subject_scoped`; single_query_tenant_subject_object_lineage; deny `404_for_out_of_scope_object_403_for_disallowed_action`.
- Failure cases: `wrong_tenant_or_subject_is_404`, `wrong_purpose_action_or_field_scope_is_403`, `revoked_grant_is_rechecked`, `missing_or_invalid_csrf_is_403`, `inactive_instrument_release_is_400`, `answer_schema_mismatch_is_400`, `wrong_subject_is_404`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-001`, `UPG-BE-005`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `CSRF_AND_IDEMPOTENCY_TEST_RECEIPT`, `INSTRUMENT_GOVERNANCE_APPROVAL_RECEIPT`, `DATA_FIELD_SCOPE_REVIEW_RECEIPT`.
- Câu hỏi mở: ENTITY_REGISTRY không có questionnaire_response/submission entity và không định nghĩa ánh xạ sang observation; chưa có field nào đủ nguồn để bắt buộc trong success body. Cần chốt lưu raw answers, derived scoring, instrument release và completion semantics trước khi định schema.

### RDP-015 createPlan

- Route: `POST /subjects/{subjectId}/plans`; success `201`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `ActionPlan` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `action_plan`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `plan_id`, `title`, `goal`, `success_measure`, `horizon_days`, `state`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `plan_id`, `title`, `goal`, `success_measure`, `horizon_days`, `state`.
- Server-only, cấm trả: `tenant_id`, `subject_id`.
- Nullable: _rỗng có chủ đích_; unknown không dùng sentinel.
- Scope: `subject:write` / `subject_scoped`; single_query_tenant_subject_object_lineage; deny `404_for_out_of_scope_object_403_for_disallowed_action`.
- Failure cases: `wrong_tenant_or_subject_is_404`, `wrong_purpose_action_or_field_scope_is_403`, `revoked_grant_is_rechecked`, `missing_or_invalid_csrf_is_403`, `wrong_subject_is_404`, `invalid_horizon_or_measure_is_400`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-005`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `CSRF_AND_IDEMPOTENCY_TEST_RECEIPT`.
- Câu hỏi mở: stop_condition có trong request schema nhưng không có cột trong ENTITY_REGISTRY; phải quyết định persistence/versioning.

### RDP-016 plans

- Route: `GET /subjects/{subjectId}/plans`; success `200`; generic hiện tại `#/components/schemas/ResourcePage`.
- Named proposal: `ActionPlanPage` (page); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `action_plan`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `items`, `next_cursor`, `items[].plan_id`, `items[].title`, `items[].goal`, `items[].success_measure`, `items[].horizon_days`, `items[].state`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `items`, `next_cursor`, `items[].plan_id`, `items[].title`, `items[].goal`, `items[].success_measure`, `items[].horizon_days`, `items[].state`.
- Server-only, cấm trả: `items[].tenant_id`, `items[].subject_id`.
- Nullable: `next_cursor`; unknown không dùng sentinel.
- Scope: `subject:read` / `subject_scoped`; single_query_tenant_subject_object_lineage; deny `404_for_out_of_scope_object_403_for_disallowed_action`.
- Failure cases: `wrong_tenant_or_subject_is_404`, `wrong_purpose_action_or_field_scope_is_403`, `revoked_grant_is_rechecked`, `wrong_subject_is_404`, `invalid_cursor_is_rejected`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`.
- Câu hỏi mở: Sort/cursor và inclusion của closed plans chưa được chốt.

### RDP-017 checkin

- Route: `POST /actions/{actionId}/check-ins`; success `201`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `ActionOutcome` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `action_item`, `action_outcome`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `outcome_id`, `action_item_id`, `observed_at`, `state`, `note`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `outcome_id`, `action_item_id`, `observed_at`, `state`, `note`.
- Server-only, cấm trả: `tenant_id`, `subject_id`.
- Nullable: `note`; unknown không dùng sentinel.
- Scope: `action:write` / `subject_scoped`; single_query_tenant_subject_object_lineage; deny `404_for_out_of_scope_object_403_for_disallowed_action`.
- Failure cases: `wrong_tenant_or_subject_is_404`, `wrong_purpose_action_or_field_scope_is_403`, `revoked_grant_is_rechecked`, `missing_or_invalid_csrf_is_403`, `action_out_of_scope_is_404`, `occurred_at_to_observed_at_mapping_invalid_is_400`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-005`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `CSRF_AND_IDEMPOTENCY_TEST_RECEIPT`.
- Câu hỏi mở: Request dùng occurred_at còn entity dùng observed_at; cần mapping/rename contract rõ ràng. Enum state của outcome chưa được khóa.

### RDP-018 timeline

- Route: `GET /subjects/{subjectId}/timeline`; success `200`; generic hiện tại `#/components/schemas/ResourcePage`.
- Named proposal: `SubjectTimelinePage` (page); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `observation`, `action_outcome`, `analysis_run`, `report_snapshot`. Trạng thái nguồn: `BLOCKED_SOURCE_MODEL_GAP`.
- Required: `items`, `next_cursor`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `items`, `next_cursor`, `items[].event_type`, `items[].source_id`, `items[].occurred_at`, `items[].state`.
- Server-only, cấm trả: `items[].payload`, `items[].content_tree`, `items[].raw_fields`, `tenant_id`, `subject_id`.
- Nullable: `next_cursor`; unknown không dùng sentinel.
- Scope: `subject:read` / `subject_scoped`; single_query_tenant_subject_object_lineage; deny `404_for_out_of_scope_object_403_for_disallowed_action`.
- Failure cases: `wrong_tenant_or_subject_is_404`, `wrong_purpose_action_or_field_scope_is_403`, `revoked_grant_is_rechecked`, `wrong_subject_is_404`, `revoked_or_withdrawn_source_is_filtered`, `invalid_cursor_is_rejected`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-005`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `PRIVACY_TIMELINE_PROJECTION_RECEIPT`.
- Câu hỏi mở: Chưa có timeline entity/union schema; event_type, ordering, tie-breaker và nguồn được phép chưa được chốt. Không được hợp nhất observation/self-report thành fact khi dựng timeline.

### RDP-019 analysisStatus

- Route: `GET /analysis-runs/{runId}`; success `200`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `AnalysisRunStatus` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `analysis_run`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `run_id`, `profile_version_id`, `product_release_id`, `purpose_id`, `state`, `configuration_digest`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `run_id`, `profile_version_id`, `product_release_id`, `purpose_id`, `state`, `configuration_digest`.
- Server-only, cấm trả: `requested_by`, `tenant_id`, `subject_id`.
- Nullable: _rỗng có chủ đích_; unknown không dùng sentinel.
- Scope: `run:read` / `subject_scoped`; single_query_tenant_subject_object_lineage; deny `404_for_out_of_scope_object_403_for_disallowed_action`.
- Failure cases: `wrong_tenant_or_subject_is_404`, `wrong_purpose_action_or_field_scope_is_403`, `revoked_grant_is_rechecked`, `run_out_of_scope_is_404`, `revoked_grant_withholds_result`, `unknown_or_terminal_state_transition_is_handled`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-004`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`.
- Câu hỏi mở: Progress/error/result-link fields chưa tồn tại trong entity registry; không tự thêm trước job contract.

### RDP-020 cancelAnalysis

- Route: `POST /analysis-runs/{runId}/cancel`; success `200`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `AnalysisRunStatus` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `analysis_run`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `run_id`, `profile_version_id`, `product_release_id`, `purpose_id`, `state`, `configuration_digest`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `run_id`, `profile_version_id`, `product_release_id`, `purpose_id`, `state`, `configuration_digest`.
- Server-only, cấm trả: `requested_by`, `tenant_id`, `subject_id`.
- Nullable: _rỗng có chủ đích_; unknown không dùng sentinel.
- Scope: `run:cancel` / `subject_scoped`; single_query_tenant_subject_object_lineage; deny `404_for_out_of_scope_object_403_for_disallowed_action`.
- Failure cases: `wrong_tenant_or_subject_is_404`, `wrong_purpose_action_or_field_scope_is_403`, `revoked_grant_is_rechecked`, `missing_or_invalid_csrf_is_403`, `run_out_of_scope_is_404`, `terminal_run_cancel_is_409_or_idempotent_by_contract`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-004`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `CSRF_AND_IDEMPOTENCY_TEST_RECEIPT`.
- Câu hỏi mở: Cần state machine xác định queued/running/terminal nào cancellable và idempotent repeat.

### RDP-021 reports

- Route: `GET /subjects/{subjectId}/reports`; success `200`; generic hiện tại `#/components/schemas/ResourcePage`.
- Named proposal: `ReportSnapshotPage` (page); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `report_snapshot`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `items`, `next_cursor`, `items[].report_id`, `items[].product_release_id`, `items[].content_revision`, `items[].state`, `items[].digest`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `items`, `next_cursor`, `items[].report_id`, `items[].product_release_id`, `items[].content_revision`, `items[].state`, `items[].digest`.
- Server-only, cấm trả: `items[].content_tree`, `items[].source_snapshot`, `items[].reviewer_account_id`, `tenant_id`, `subject_id`.
- Nullable: `next_cursor`; unknown không dùng sentinel.
- Scope: `subject:read` / `subject_scoped`; single_query_tenant_subject_object_lineage; deny `404_for_out_of_scope_object_403_for_disallowed_action`.
- Failure cases: `wrong_tenant_or_subject_is_404`, `wrong_purpose_action_or_field_scope_is_403`, `revoked_grant_is_rechecked`, `wrong_subject_is_404`, `withdrawn_or_deleted_snapshot_state_is_respected`, `invalid_cursor_is_rejected`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`.
- Câu hỏi mở: Report list là summary projection; không nhúng content_tree/source_snapshot.

### RDP-022 reportRevisions

- Route: `GET /reports/{reportId}/revisions`; success `200`; generic hiện tại `#/components/schemas/ResourcePage`.
- Named proposal: `ReportRevisionPage` (page); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `report_snapshot`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `items`, `next_cursor`, `items[].report_id`, `items[].content_revision`, `items[].state`, `items[].digest`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `items`, `next_cursor`, `items[].report_id`, `items[].content_revision`, `items[].state`, `items[].digest`.
- Server-only, cấm trả: `items[].content_tree`, `items[].source_snapshot`, `items[].reviewer_account_id`, `tenant_id`, `subject_id`.
- Nullable: `next_cursor`; unknown không dùng sentinel.
- Scope: `report:read` / `subject_scoped`; single_query_tenant_subject_object_lineage; deny `404_for_out_of_scope_object_403_for_disallowed_action`.
- Failure cases: `wrong_tenant_or_subject_is_404`, `wrong_purpose_action_or_field_scope_is_403`, `revoked_grant_is_rechecked`, `report_out_of_scope_is_404`, `invalid_cursor_is_rejected`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-005`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`.
- Câu hỏi mở: Logical report identity versus snapshot row identity chưa được mô hình hóa rõ.

### RDP-023 review

- Route: `POST /reports/{reportId}/reviews`; success `201`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `ReportReviewReceipt` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `report_snapshot`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `report_id`, `content_revision`, `state`, `digest`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `report_id`, `content_revision`, `state`, `digest`.
- Server-only, cấm trả: `content_tree`, `source_snapshot`, `reviewer_account_id`, `tenant_id`, `subject_id`.
- Nullable: _rỗng có chủ đích_; unknown không dùng sentinel.
- Scope: `report:review` / `reviewer_role`; server_role_assignment_plus_explicit_scope; deny `403_without_role_or_scope`.
- Failure cases: `missing_required_role_or_scope_is_403`, `stale_permission_revision_blocks_state_transition`, `missing_or_invalid_csrf_is_403`, `report_out_of_scope_or_unassigned_is_404`, `stale_revision_is_412`, `invalid_state_transition_is_409`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-005`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `CSRF_AND_IDEMPOTENCY_TEST_RECEIPT`, `REPORT_REVIEW_WORKFLOW_APPROVAL_RECEIPT`.
- Câu hỏi mở: Review decision/history entity chưa có; reviewer_account_id trong snapshot không đủ audit ledger.

### RDP-024 publish

- Route: `POST /reports/{reportId}/publish`; success `200`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `ReportPublicationReceipt` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `report_snapshot`, `report_artifact`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `report_id`, `content_revision`, `state`, `digest`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `report_id`, `content_revision`, `state`, `digest`, `artifact_ids`.
- Server-only, cấm trả: `private_object_key`, `reviewer_account_id`, `tenant_id`, `subject_id`.
- Nullable: _rỗng có chủ đích_; unknown không dùng sentinel.
- Scope: `report:publish` / `reviewer_role`; server_role_assignment_plus_explicit_scope; deny `403_without_role_or_scope`.
- Failure cases: `missing_required_role_or_scope_is_403`, `stale_permission_revision_blocks_state_transition`, `missing_or_invalid_csrf_is_403`, `report_out_of_scope_or_unassigned_is_404`, `stale_revision_is_412`, `missing_approval_record_is_403_or_409`, `artifact_failure_does_not_publish_partial_state`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-004`, `UPG-BE-005`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `CSRF_AND_IDEMPOTENCY_TEST_RECEIPT`, `REPORT_PUBLICATION_APPROVAL_RECEIPT`.
- Câu hỏi mở: Transaction giữa publish state và artifact creation/outbox chưa được chốt. artifact_ids chỉ được thêm sau khi junction/lineage được xác định.

### RDP-025 order

- Route: `POST /orders`; success `201`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `CommerceOrder` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `commerce_order`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `order_id`, `product_release_id`, `amount_minor`, `currency`, `state`, `quote_version`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `order_id`, `product_release_id`, `amount_minor`, `currency`, `state`, `quote_version`.
- Server-only, cấm trả: `account_id`, `tenant_id`, `subject_id`.
- Nullable: _rỗng có chủ đích_; unknown không dùng sentinel.
- Scope: `self` / `session_self`; principal_account_from_session_only; deny `401_or_403_without_private_metadata`.
- Failure cases: `missing_or_invalid_session_is_401`, `suspended_account_is_denied_without_private_metadata`, `missing_or_invalid_csrf_is_403`, `invalid_or_expired_quote_is_400_or_409`, `product_or_country_not_released_is_409`, `subject_scope_mismatch_is_404`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-003`, `UPG-BE-004`, `UPG-BE-005`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `CSRF_AND_IDEMPOTENCY_TEST_RECEIPT`, `COMMERCE_CONTRACT_APPROVAL_RECEIPT`.
- Câu hỏi mở: Quote entity/signature/expiry chưa có trong ENTITY_REGISTRY; server phải xác minh, không tin amount client.

### RDP-026 orderStatus

- Route: `GET /orders/{orderId}`; success `200`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `CommerceOrder` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `commerce_order`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `order_id`, `product_release_id`, `amount_minor`, `currency`, `state`, `quote_version`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `order_id`, `product_release_id`, `amount_minor`, `currency`, `state`, `quote_version`.
- Server-only, cấm trả: `account_id`, `tenant_id`, `subject_id`.
- Nullable: _rỗng có chủ đích_; unknown không dùng sentinel.
- Scope: `order:owner` / `owner_scoped`; single_query_owner_account_object_lineage; deny `404_for_other_owner`.
- Failure cases: `missing_or_invalid_session_is_401`, `other_owner_resource_is_404`, `other_owner_is_404`, `unknown_order_state_is_not_coerced`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-003`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`.
- Câu hỏi mở: Payment/refund summary fields cần named entities trước khi thêm.

### RDP-027 checkout

- Route: `POST /orders/{orderId}/checkout`; success `201`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `CommerceOrder` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `commerce_order`, `payment_event`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `order_id`, `product_release_id`, `amount_minor`, `currency`, `state`, `quote_version`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `order_id`, `product_release_id`, `amount_minor`, `currency`, `state`, `quote_version`.
- Server-only, cấm trả: `account_id`, `tenant_id`, `subject_id`, `provider_payload`, `provider_secret`.
- Nullable: _rỗng có chủ đích_; unknown không dùng sentinel.
- Scope: `order:owner` / `owner_scoped`; single_query_owner_account_object_lineage; deny `404_for_other_owner`.
- Failure cases: `missing_or_invalid_session_is_401`, `other_owner_resource_is_404`, `missing_or_invalid_csrf_is_403`, `other_owner_is_404`, `expired_or_mismatched_quote_is_409`, `idempotency_digest_conflict_is_409`, `provider_failure_does_not_mark_paid`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-003`, `UPG-BE-004`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `CSRF_AND_IDEMPOTENCY_TEST_RECEIPT`, `PAYMENT_PROVIDER_CONTRACT_RECEIPT`, `SECURITY_CHECKOUT_REVIEW_RECEIPT`.
- Câu hỏi mở: Provider checkout session/redirect contract chưa có; không trả URL/token trước security review. Repeat checkout phải chốt idempotency namespace và quote consistency.

### RDP-028 requestRefund

- Route: `POST /orders/{orderId}/refund-requests`; success `201`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `JobAccepted` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `job_receipt`, `commerce_order`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `job_id`, `status`, `status_url`, `request_id`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `job_id`, `status`, `status_url`, `request_id`.
- Server-only, cấm trả: `request_digest`, `idempotency_key`, `provider_payload`, `account_id`, `tenant_id`.
- Nullable: _rỗng có chủ đích_; unknown không dùng sentinel.
- Scope: `order:owner` / `owner_scoped`; single_query_owner_account_object_lineage; deny `404_for_other_owner`.
- Failure cases: `missing_or_invalid_session_is_401`, `other_owner_resource_is_404`, `missing_or_invalid_csrf_is_403`, `other_owner_is_404`, `order_not_refundable_is_409`, `idempotency_digest_conflict_is_409`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-003`, `UPG-BE-004`, `UPG-BE-005`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `CSRF_AND_IDEMPOTENCY_TEST_RECEIPT`, `REFUND_WORKFLOW_APPROVAL_RECEIPT`, `PAYMENT_PROVIDER_CONTRACT_RECEIPT`.
- Câu hỏi mở: Refund request/state entity và provider lifecycle chưa có; chỉ được dùng JobAccepted cho intake nếu worker contract được duyệt.

### RDP-029 paymentWebhook

- Route: `POST /webhooks/payments/{providerId}`; success `200`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `PaymentWebhookReceipt` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `payment_event`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `state`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `state`, `provider_event_id`, `duplicate`.
- Server-only, cấm trả: `payload_digest`, `commerce_order_id`, `merchant_account_id`, `raw_payload`, `signature_material`, `tenant_id`.
- Nullable: _rỗng có chủ đích_; unknown không dùng sentinel.
- Scope: `webhook_signature` / `signed_webhook`; provider_and_merchant_account_from_server_configuration; deny `generic_2xx_for_verified_duplicate_or_safe_4xx_for_invalid_signature_by_provider_contract`.
- Failure cases: `invalid_signature_has_no_effect`, `replayed_event_has_at_most_one_business_effect`, `invalid_signature_has_no_business_effect`, `verified_duplicate_has_no_second_effect`, `provider_and_merchant_are_server_resolved`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-003`, `UPG-BE-004`, `UPG-BE-005`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `PAYMENT_PROVIDER_CONTRACT_RECEIPT`, `SECURITY_SIGNATURE_REVIEW_RECEIPT`.
- Câu hỏi mở: Exact response body/status cho duplicate và retry phải theo từng provider contract. merchant_account_id được yêu cầu trong migration delta nhưng chưa có trong ENTITY_REGISTRY gốc.

### RDP-030 entitlements

- Route: `GET /entitlements`; success `200`; generic hiện tại `#/components/schemas/ResourcePage`.
- Named proposal: `EntitlementPage` (page); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `entitlement`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `items`, `next_cursor`, `items[].entitlement_id`, `items[].product_release_id`, `items[].state`, `items[].expires_at`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `items`, `next_cursor`, `items[].entitlement_id`, `items[].product_release_id`, `items[].state`, `items[].expires_at`.
- Server-only, cấm trả: `items[].account_id`, `items[].commerce_order_id`, `tenant_id`.
- Nullable: `next_cursor`, `items[].expires_at`; unknown không dùng sentinel.
- Scope: `self` / `session_self`; principal_account_from_session_only; deny `401_or_403_without_private_metadata`.
- Failure cases: `missing_or_invalid_session_is_401`, `suspended_account_is_denied_without_private_metadata`, `session_account_only_no_client_account_filter`, `expired_or_revoked_entitlement_state_is_not_hidden_as_active`, `invalid_cursor_is_rejected`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-003`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`.
- Câu hỏi mở: Có cần product public summary embedded hay chỉ ID/version chưa chốt.

### RDP-031 ticket

- Route: `POST /support/tickets`; success `201`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `SupportTicket` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: _rỗng có chủ đích_. Trạng thái nguồn: `BLOCKED_SOURCE_MODEL_GAP`.
- Required: `ticket_id`, `state`, `topic`, `created_at`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `ticket_id`, `state`, `topic`, `created_at`.
- Server-only, cấm trả: `description`, `related_resource_private_metadata`, `account_id`, `tenant_id`.
- Nullable: _rỗng có chủ đích_; unknown không dùng sentinel.
- Scope: `self` / `session_self`; principal_account_from_session_only; deny `401_or_403_without_private_metadata`.
- Failure cases: `missing_or_invalid_session_is_401`, `suspended_account_is_denied_without_private_metadata`, `missing_or_invalid_csrf_is_403`, `session_account_only`, `related_resource_id_is_not_accepted_without_scope_check`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-005`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `CSRF_AND_IDEMPOTENCY_TEST_RECEIPT`, `SUPPORT_DATA_MODEL_APPROVAL_RECEIPT`, `SUPPORT_PRIVACY_REVIEW_RECEIPT`.
- Câu hỏi mở: ENTITY_REGISTRY không có support_ticket; retention, encryption, ownership và state machine chưa được thiết kế. Có trả description trong create response hay không cần privacy decision.

### RDP-032 ticketStatus

- Route: `GET /support/tickets/{ticketId}`; success `200`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `SupportTicketStatus` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: _rỗng có chủ đích_. Trạng thái nguồn: `BLOCKED_SOURCE_MODEL_GAP`.
- Required: `ticket_id`, `state`, `topic`, `created_at`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `ticket_id`, `state`, `topic`, `created_at`.
- Server-only, cấm trả: `description`, `related_resource_private_metadata`, `account_id`, `tenant_id`.
- Nullable: _rỗng có chủ đích_; unknown không dùng sentinel.
- Scope: `ticket:owner` / `owner_scoped`; single_query_owner_account_object_lineage; deny `404_for_other_owner`.
- Failure cases: `missing_or_invalid_session_is_401`, `other_owner_resource_is_404`, `other_owner_is_404`, `deleted_or_merged_ticket_semantics_are_defined`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-005`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `SUPPORT_DATA_MODEL_APPROVAL_RECEIPT`, `SUPPORT_PRIVACY_REVIEW_RECEIPT`.
- Câu hỏi mở: ENTITY_REGISTRY không có support_ticket hoặc event history; owner lookup query chưa thể đặc tả.

### RDP-033 deletionStatus

- Route: `GET /deletion-jobs/{jobId}`; success `200`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `DeletionJobStatus` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `deletion_job`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `job_id`, `scope`, `state`, `receipt`, `completed_at`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `job_id`, `scope`, `state`, `receipt`, `completed_at`.
- Server-only, cấm trả: `requestor_account_id`, `tenant_id`, `subject_id`, `backup_internal_locations`.
- Nullable: `receipt`, `completed_at`; unknown không dùng sentinel.
- Scope: `job:owner` / `owner_scoped`; single_query_owner_account_object_lineage; deny `404_for_other_owner`.
- Failure cases: `missing_or_invalid_session_is_401`, `other_owner_resource_is_404`, `other_owner_is_404`, `legal_hold_or_partial_completion_has_safe_state`, `restore_tombstone_replay_failure_blocks_completion`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-004`, `UPG-BE-005`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `PRIVACY_DELETION_WORKFLOW_RECEIPT`.
- Câu hỏi mở: Receipt public shape phải redact store identifiers, raw PI và legal-hold reason. Legal hold impact cần safe status without disclosing restricted reason.

### RDP-034 jobStatus

- Route: `GET /jobs/{jobId}`; success `200`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `JobStatus` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `job_receipt`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `job_id`, `state`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `job_id`, `state`, `result_reference`.
- Server-only, cấm trả: `namespace`, `idempotency_key`, `request_digest`, `tenant_id`.
- Nullable: `result_reference`; unknown không dùng sentinel.
- Scope: `job:owner` / `owner_scoped`; single_query_owner_account_object_lineage; deny `404_for_other_owner`.
- Failure cases: `missing_or_invalid_session_is_401`, `other_owner_resource_is_404`, `other_owner_is_404`, `revoked_authorization_withholds_result`, `unknown_job_namespace_is_not_exposed`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-004`, `UPG-BE-005`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `JOB_MODEL_APPROVAL_RECEIPT`.
- Câu hỏi mở: Owner link từ job_receipt đến account/resource chưa có trong entity columns; phải thêm trước query. result_reference phải là authorized route/reference, không phải private object key.

### RDP-035 newAutomation

- Route: `POST /automations`; success `201`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `AutomationRecord` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: _rỗng có chủ đích_. Trạng thái nguồn: `BLOCKED_SOURCE_MODEL_GAP`.
- Required: `automation_id`, `subject_id`, `purpose_id`, `action`, `timezone`, `schedule`, `expires_at`, `state`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `automation_id`, `subject_id`, `purpose_id`, `action`, `timezone`, `schedule`, `expires_at`, `state`.
- Server-only, cấm trả: `account_id`, `tenant_id`, `internal_scheduler_payload`.
- Nullable: _rỗng có chủ đích_; unknown không dùng sentinel.
- Scope: `subject:automate` / `subject_scoped`; single_query_tenant_subject_object_lineage; deny `404_for_out_of_scope_object_403_for_disallowed_action`.
- Failure cases: `wrong_tenant_or_subject_is_404`, `wrong_purpose_action_or_field_scope_is_403`, `revoked_grant_is_rechecked`, `missing_or_invalid_csrf_is_403`, `wrong_subject_is_404`, `unsupported_schedule_or_timezone_is_400`, `expires_at_or_opt_in_invalid_is_400`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-004`, `UPG-BE-005`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `CSRF_AND_IDEMPOTENCY_TEST_RECEIPT`, `AUTOMATION_DATA_MODEL_APPROVAL_RECEIPT`, `PRIVACY_AUTOMATION_APPROVAL_RECEIPT`.
- Câu hỏi mở: ENTITY_REGISTRY không có automation entity/outbox linkage/state machine. Schedule DSL, DST policy, allowed actions và stop semantics chưa được chốt.

### RDP-036 cases

- Route: `GET /practice/cases`; success `200`; generic hiện tại `#/components/schemas/ResourcePage`.
- Named proposal: `PractitionerCasePage` (page); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `practitioner_case`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `items`, `next_cursor`, `items[].case_id`, `items[].purpose_id`, `items[].scope`, `items[].state`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `items`, `next_cursor`, `items[].case_id`, `items[].purpose_id`, `items[].scope`, `items[].state`.
- Server-only, cấm trả: `items[].practitioner_account_id`, `items[].subject_id`, `tenant_id`, `subject_profile_fields`.
- Nullable: `next_cursor`; unknown không dùng sentinel.
- Scope: `practitioner:assigned` / `assigned_role`; assignment_plus_tenant_plus_resource_scope; deny `404_for_unassigned_resource`.
- Failure cases: `inactive_or_out_of_scope_assignment_is_404`, `membership_or_seat_alone_never_grants_subject_access`, `inactive_assignment_is_404_or_omitted`, `seat_without_subject_grant_returns_no_case`, `invalid_cursor_is_rejected`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `PRACTITIONER_CASE_SCOPE_APPROVAL_RECEIPT`.
- Câu hỏi mở: Có trả pseudonymous subject label hay không cần privacy/use-case approval; hiện không có field nguồn.

### RDP-037 caseDetail

- Route: `GET /practice/cases/{caseId}`; success `200`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `PractitionerCase` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `practitioner_case`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `case_id`, `purpose_id`, `scope`, `state`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `case_id`, `purpose_id`, `scope`, `state`.
- Server-only, cấm trả: `practitioner_account_id`, `subject_id`, `tenant_id`, `subject_profile_fields`.
- Nullable: _rỗng có chủ đích_; unknown không dùng sentinel.
- Scope: `practitioner:assigned` / `assigned_role`; assignment_plus_tenant_plus_resource_scope; deny `404_for_unassigned_resource`.
- Failure cases: `inactive_or_out_of_scope_assignment_is_404`, `membership_or_seat_alone_never_grants_subject_access`, `unassigned_case_is_404`, `expired_grant_or_wrong_purpose_is_404_or_403_by_policy`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `PRACTITIONER_CASE_SCOPE_APPROVAL_RECEIPT`.
- Câu hỏi mở: Embedded subject/report/action fields phải có section_scope riêng; chưa được phép trong proposal này.

### RDP-038 courses

- Route: `GET /academy/courses`; success `200`; generic hiện tại `#/components/schemas/ResourcePage`.
- Named proposal: `CourseReleasePage` (page); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `academy_enrollment`. Trạng thái nguồn: `BLOCKED_SOURCE_MODEL_GAP`.
- Required: `items`, `next_cursor`.
- Public whitelist: `items`, `next_cursor`.
- Authorized-private whitelist: _rỗng có chủ đích_.
- Server-only, cấm trả: `enrollment_id`, `account_id`, `tenant_id`.
- Nullable: `next_cursor`; unknown không dùng sentinel.
- Scope: `public` / `public_read`; published_public_projection_only; deny `public_problem`.
- Failure cases: `unpublished_or_nonpublic_resource_is_not_disclosed`, `unreleased_course_is_omitted`, `invalid_cursor_is_rejected`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-005`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `PRIVACY_PUBLIC_PROJECTION_RECEIPT`, `ACADEMY_CONTENT_RIGHTS_APPROVAL_RECEIPT`.
- Câu hỏi mở: ENTITY_REGISTRY chỉ có academy_enrollment, không có course/course_release catalog; chưa có whitelist item field đáng tin cậy. Cần rights/license/content release model trước khi công khai course.

### RDP-039 assignment

- Route: `POST /academy/assignments`; success `201`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `AssignmentSubmissionReceipt` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `academy_enrollment`. Trạng thái nguồn: `BLOCKED_SOURCE_MODEL_GAP`.
- Required: _rỗng có chủ đích_.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: _rỗng có chủ đích_.
- Server-only, cấm trả: `response_text`, `attachment_ids`, `account_id`, `tenant_id`.
- Nullable: _rỗng có chủ đích_; unknown không dùng sentinel.
- Scope: `enrollment:write` / `owner_scoped`; single_query_owner_account_object_lineage; deny `404_for_other_owner`.
- Failure cases: `missing_or_invalid_session_is_401`, `other_owner_resource_is_404`, `missing_or_invalid_csrf_is_403`, `inactive_or_other_owner_enrollment_is_404`, `unreleased_lesson_or_assignment_is_400`, `attachment_scope_or_scan_failure_is_rejected`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-004`, `UPG-BE-005`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `CSRF_AND_IDEMPOTENCY_TEST_RECEIPT`, `ACADEMY_ASSIGNMENT_MODEL_APPROVAL_RECEIPT`, `ATTACHMENT_SECURITY_REVIEW_RECEIPT`.
- Câu hỏi mở: ENTITY_REGISTRY không có assignment submission, lesson release hoặc attachment entity; không có required success fields đủ nguồn. Cần malware scanning, object authorization, retention và resubmission/version contract.

### RDP-040 verifyCertificate

- Route: `GET /certificates/{certificateId}`; success `200`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `CertificatePublicVerification` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `certificate`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `public_verification_id`, `scope`, `state`, `expires_at`.
- Public whitelist: `public_verification_id`, `scope`, `state`, `expires_at`.
- Authorized-private whitelist: _rỗng có chủ đích_.
- Server-only, cấm trả: `enrollment_id`, `tenant_id`, `account_id`, `learner_name`, `private_course_activity`.
- Nullable: `expires_at`; unknown không dùng sentinel.
- Scope: `public_minimal` / `public_read`; published_public_projection_only; deny `public_problem`.
- Failure cases: `unpublished_or_nonpublic_resource_is_not_disclosed`, `unknown_or_revoked_certificate_has_non_enumerating_public_response`, `expired_certificate_is_not_presented_as_valid`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `PRIVACY_PUBLIC_PROJECTION_RECEIPT`, `ACADEMY_CERTIFICATE_APPROVAL_RECEIPT`.
- Câu hỏi mở: Route certificateId là internal ID hay public_verification_id phải chốt; public endpoint chỉ được nhận public ID. scope phải có schema allowlist tối thiểu; không trả learner identity mặc định.

### RDP-041 organizationOverview

- Route: `GET /organizations/{organizationId}/overview`; success `200`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `OrganizationOverview` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `tenant`, `tenant_membership`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `organization`, `membership`, `organization.tenant_id`, `organization.name`, `organization.kind`, `organization.state`, `membership.role_code`, `membership.state`, `membership.expires_at`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `organization`, `membership`, `organization.tenant_id`, `organization.name`, `organization.kind`, `organization.state`, `organization.country_pack_id`, `membership.role_code`, `membership.state`, `membership.expires_at`.
- Server-only, cấm trả: `other_memberships`, `profile_subjects`, `personal_profile_fields`, `idp_subject`.
- Nullable: `organization.country_pack_id`, `membership.expires_at`; unknown không dùng sentinel.
- Scope: `organization:member` / `assigned_role`; assignment_plus_tenant_plus_resource_scope; deny `404_for_unassigned_resource`.
- Failure cases: `inactive_or_out_of_scope_assignment_is_404`, `membership_or_seat_alone_never_grants_subject_access`, `inactive_membership_is_404`, `membership_never_expands_subject_access`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-005`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `ORGANIZATION_PROJECTION_APPROVAL_RECEIPT`.
- Câu hỏi mở: Overview chỉ được trả current principal membership, không suy quyền đọc subject. Organization ID có trùng tenant_id hay cần entity riêng chưa chốt.

### RDP-042 partner

- Route: `GET /partners/{partnerId}`; success `200`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `PartnerLicenseView` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `partner_license`, `country_pack`, `tenant`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `partner_license_id`, `country_pack_id`, `allowed_capabilities`, `state`, `expires_at`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `partner_license_id`, `country_pack_id`, `allowed_capabilities`, `state`, `expires_at`.
- Server-only, cấm trả: `agreement_reference`, `tenant_id`, `legal_review_ref`, `policy`.
- Nullable: `expires_at`; unknown không dùng sentinel.
- Scope: `partner:assigned` / `assigned_role`; assignment_plus_tenant_plus_resource_scope; deny `404_for_unassigned_resource`.
- Failure cases: `inactive_or_out_of_scope_assignment_is_404`, `membership_or_seat_alone_never_grants_subject_access`, `inactive_assignment_or_license_is_404`, `country_scope_mismatch_is_403`, `license_never_expands_subject_access`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-005`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `PARTNER_LICENSE_APPROVAL_RECEIPT`.
- Câu hỏi mở: partnerId ánh xạ tenant hay partner_license chưa rõ. Capability projection phải exclude agreement/legal reference và không tự cấp subject access.

### RDP-043 methodReleaseDraft

- Route: `POST /admin/method-releases`; success `201`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `MethodRelease` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `method`, `method_release`, `source_record`, `source_edition`, `rights_record`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `schema_version`, `method_id`, `release_id`, `family_id`, `version`, `computation_kind`, `evidence_class`, `release_state`, `status`, `source_ids`, `edition_locations`, `rights_status`, `input_schema_ref`, `output_schema_ref`, `rule_spec_ref`, `configuration`, `limitations`, `golden_cases_ref`, `test_receipt_ref`, `allowed_claim_types`, `allowed_product_ids`, `allowed_country_packs`, `approved_by`, `approved_at`, `source_rights_receipt_ids`, `release_artifact_digest`, `effective_at`, `expires_at`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `schema_version`, `method_id`, `release_id`, `family_id`, `version`, `computation_kind`, `evidence_class`, `release_state`, `status`, `source_ids`, `edition_locations`, `rights_status`, `input_schema_ref`, `output_schema_ref`, `rule_spec_ref`, `configuration`, `limitations`, `golden_cases_ref`, `test_receipt_ref`, `allowed_claim_types`, `allowed_product_ids`, `allowed_country_packs`, `approved_by`, `approved_at`, `source_rights_receipt_ids`, `release_artifact_digest`, `effective_at`, `expires_at`.
- Server-only, cấm trả: `source_private_notes`, `rights_legal_reference`, `editor_identity_beyond_approved_by`.
- Nullable: `test_receipt_ref`, `approved_by`, `approved_at`, `release_artifact_digest`, `effective_at`, `expires_at`; unknown không dùng sentinel.
- Scope: `method:editor` / `reviewer_role`; server_role_assignment_plus_explicit_scope; deny `403_without_role_or_scope`.
- Failure cases: `missing_required_role_or_scope_is_403`, `stale_permission_revision_blocks_state_transition`, `missing_or_invalid_csrf_is_403`, `client_supplied_approval_or_permitted_state_is_rejected`, `missing_source_rights_or_fixture_gate_keeps_release_blocked`, `duplicate_method_version_is_409`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-001`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `CSRF_AND_IDEMPOTENCY_TEST_RECEIPT`, `METHOD_GOVERNANCE_APPROVAL_RECEIPT`, `SOURCE_RIGHTS_APPROVAL_RECEIPT`.
- Câu hỏi mở: Response dùng canonical MethodRelease v2.1 fields; request hiện cũng trỏ schema này nhưng draft create có thể cần schema riêng để server-owned approval fields không client-set.

### RDP-044 countryPackReview

- Route: `POST /admin/country-packs`; success `201`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `CountryPackReviewRecord` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `country_pack`. Trạng thái nguồn: `GROUNDED_PROPOSAL_REQUIRES_REVIEW`.
- Required: `country_pack_id`, `country_code`, `version`, `policy`, `legal_review_ref`, `state`.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: `country_pack_id`, `country_code`, `version`, `policy`, `legal_review_ref`, `state`.
- Server-only, cấm trả: `reviewer_private_notes`, `tenant_assignments`.
- Nullable: `legal_review_ref`; unknown không dùng sentinel.
- Scope: `legal:reviewer` / `reviewer_role`; server_role_assignment_plus_explicit_scope; deny `403_without_role_or_scope`.
- Failure cases: `missing_required_role_or_scope_is_403`, `stale_permission_revision_blocks_state_transition`, `missing_or_invalid_csrf_is_403`, `unsupported_country_or_revision_is_400`, `missing_legal_reference_cannot_reach_approved_state`, `duplicate_country_version_is_409`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-005`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `CSRF_AND_IDEMPOTENCY_TEST_RECEIPT`, `LEGAL_COUNTRY_REVIEW_RECEIPT`.
- Câu hỏi mở: Request revision versus entity version naming cần thống nhất. data_regions và locale_releases nằm trong request nhưng chưa có typed columns; cần khóa trong policy schema hoặc junction.

### RDP-045 quality

- Route: `GET /admin/quality`; success `200`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `QualityMetadataSnapshot` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `audit_event`. Trạng thái nguồn: `BLOCKED_SOURCE_MODEL_GAP`.
- Required: _rỗng có chủ đích_.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: _rỗng có chủ đích_.
- Server-only, cấm trả: `raw_profile_data`, `claim_text`, `tokens`, `request_payloads`, `actor_account_id`, `resource_id`.
- Nullable: _rỗng có chủ đích_; unknown không dùng sentinel.
- Scope: `quality:reviewer` / `reviewer_role`; server_role_assignment_plus_explicit_scope; deny `403_without_role_or_scope`.
- Failure cases: `missing_required_role_or_scope_is_403`, `stale_permission_revision_blocks_state_transition`, `missing_reviewer_scope_is_403`, `small_cohort_or_sensitive_dimension_is_redacted`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-005`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `QUALITY_METRIC_APPROVAL_RECEIPT`, `OBSERVABILITY_REDACTION_REVIEW_RECEIPT`.
- Câu hỏi mở: Không có quality metric/check registry, window, denominator hoặc snapshot entity; không có success field đủ nguồn. Cần định nghĩa metric IDs, exact numerators/denominators, retention và minimum cohort/redaction trước response schema.

### RDP-046 operations

- Route: `GET /admin/operations`; success `200`; generic hiện tại `#/components/schemas/Resource`.
- Named proposal: `OperationsMetadataSnapshot` (single); **PROPOSED, chưa overlay, chưa codegen**.
- Entity grounding: `job_receipt`, `outbox_event`, `audit_event`. Trạng thái nguồn: `BLOCKED_SOURCE_MODEL_GAP`.
- Required: _rỗng có chủ đích_.
- Public whitelist: _rỗng có chủ đích_.
- Authorized-private whitelist: _rỗng có chủ đích_.
- Server-only, cấm trả: `raw_profile_data`, `tokens`, `idempotency_key`, `request_digest`, `payload_reference`, `actor_account_id`, `resource_id`.
- Nullable: _rỗng có chủ đích_; unknown không dùng sentinel.
- Scope: `ops:reader` / `reviewer_role`; server_role_assignment_plus_explicit_scope; deny `403_without_role_or_scope`.
- Failure cases: `missing_required_role_or_scope_is_403`, `stale_permission_revision_blocks_state_transition`, `missing_ops_scope_is_403`, `sensitive_labels_are_redacted`, `stale_snapshot_is_explicit_not_silently_current`. OpenAPI non-success: `400`, `401`, `403`, `404`, `409`, `412`, `422`, `429`, `503`.
- Dependency tasks: `UPG-BE-006`, `UPG-BE-002`, `UPG-BE-004`, `UPG-BE-005`. Receipt còn thiếu: `DESIGN_APPROVAL_RECEIPT`, `API_SCHEMA_REVIEW_RECEIPT`, `AUTHORIZATION_NEGATIVE_TEST_RECEIPT`, `OPERATIONS_METRIC_APPROVAL_RECEIPT`, `OBSERVABILITY_REDACTION_REVIEW_RECEIPT`.
- Câu hỏi mở: Không có operations metric schema, aggregation window hay redaction policy; không có success field đủ nguồn. Cần queue/outbox/incident metric IDs, units, freshness và cardinality limits trước response schema.


