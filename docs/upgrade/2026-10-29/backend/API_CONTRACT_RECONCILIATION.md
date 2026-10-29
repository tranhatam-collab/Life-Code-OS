# Đối chiếu hợp đồng API hợp nhất ngày 29/10/2026

**99 operation được giữ; hợp đồng này là thiết kế, chưa cho phép codegen hoặc phát hành.** 64 operation lấy bản local R2, 19 bổ sung V2 và 16 bổ sung V3. CSV nguồn 99 dòng khớp operation ID/method/path với OpenAPI V3. Không có reference nội bộ chưa phân giải trong bản hợp nhất.

65 operation có success schema chung Resource/ResourcePage; 10 operation V3 thiếu success schema; 6 operation V3 dùng ReferenceResult với status cố định REFERENCE_ONLY. 81 operation có blocker ghi riêng. Tên response đề xuất trong bảng là công việc thiết kế cần duyệt, chưa được gắn thành schema hoặc coi là đã có API.

## Quyết định hợp nhất

- Giữ 9 object schema local canonical chính xác và toàn bộ 27 schema mới V2/V3. Giữ các response/error contracts local đã được làm chặt. Component union có 68 schema.
- Chuẩn hóa 16 path V3 bằng cách bỏ prefix /api/v2 trong path, dùng server base /api/v2; source path giữ ở provenance.
- Chuẩn hóa ba extension quyền thành x-lc-authorization, lưu source_extensions nguyên trạng. 16 V3 chưa có permission action/resource cụ thể nên fail closed; policy labels chung chưa thay thế authorization design.
- Idempotency bounds, request context/profile binding, per-field permissions, state machine và generic response fields phải đóng trước production SDK.
- Chưa thay method ID, status code hoặc schema input bằng suy đoán. Các câu hỏi còn mở vẫn là blocker trong JSON.

Căn cứ kỹ thuật đã đọc ngày 29/10/2026: [OpenAPI 3.1 Paths](https://spec.openapis.org/oas/v3.1.0.html#paths-object), [JSON Schema Core 2020-12](https://json-schema.org/draft/2020-12/json-schema-core), [PostgreSQL 18 RLS](https://www.postgresql.org/docs/18/ddl-rowsecurity.html). OAS ghép path vào server URL; JSON Schema có dialect/reference riêng; RLS phụ thuộc role và policy thực tế. Không nội dung nào ở đây chứng minh runtime đã triển khai.

## Sổ 99 operation

| Operation ID | Method + path sau server base | Nguồn | Permission | Response hiện tại / blocker | Response cần thiết kế |
|---|---|---|---|---|---|
| `health` | `GET /health` | R2 | `public` | NAMED_SCHEMA | Contract đã có; vẫn cần tích hợp/test |
| `catalog` | `GET /catalog` | R2 | `public` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `methods` | `GET /methods` | R2 | `public` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `methodDetail` | `GET /methods/{methodId}` | R2 | `public` | NAMED_SCHEMA | Contract đã có; vẫn cần tích hợp/test |
| `login` | `GET /auth/login` | R2 | `public` | NO_2XX_BODY_CONTRACT | Contract đã có; vẫn cần tích hợp/test |
| `authCallback` | `GET /auth/callback` | R2 | `public` | NO_2XX_BODY_CONTRACT | Contract đã có; vẫn cần tích hợp/test |
| `logout` | `POST /auth/logout` | R2 | `self` | NO_BODY_EXPECTED | Contract đã có; vẫn cần tích hợp/test |
| `subjects` | `GET /subjects` | R2 | `self` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `createSubject` | `POST /subjects` | R2 | `self` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `subject` | `GET /subjects/{subjectId}` | R2 | `subject:read` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `overview` | `GET /subjects/{subjectId}/overview` | R2 | `subject:read` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `newProfileVersion` | `POST /subjects/{subjectId}/profile-versions` | R2 | `subject:write` | NAMED_SCHEMA | Contract đã có; vẫn cần tích hợp/test |
| `profileVersion` | `GET /subjects/{subjectId}/profile-versions/{versionId}` | R2 | `subject:read` | NAMED_SCHEMA | Contract đã có; vẫn cần tích hợp/test |
| `newHypothesis` | `POST /subjects/{subjectId}/hypotheses` | R2 | `subject:write` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `listHypotheses` | `GET /subjects/{subjectId}/hypotheses` | V2+ | `subject:read` | GENERIC_SUCCESS_SCHEMA | HypothesisPage |
| `consents` | `GET /subjects/{subjectId}/consents` | R2 | `subject:read` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `consentDecision` | `POST /subjects/{subjectId}/consents` | R2 | `subject:consent` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `grants` | `GET /subjects/{subjectId}/grants` | R2 | `subject:share` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `grant` | `POST /subjects/{subjectId}/grants` | R2 | `subject:share` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `revokeGrant` | `DELETE /grants/{grantId}` | R2 | `grant:owner` | NO_BODY_EXPECTED | Contract đã có; vẫn cần tích hợp/test |
| `observations` | `GET /subjects/{subjectId}/observations` | R2 | `subject:read` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `observation` | `POST /subjects/{subjectId}/observations` | R2 | `subject:write` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `questionnaireResponse` | `POST /subjects/{subjectId}/questionnaire-responses` | R2 | `subject:write` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `createPlan` | `POST /subjects/{subjectId}/plans` | R2 | `subject:write` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `plans` | `GET /subjects/{subjectId}/plans` | R2 | `subject:read` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `checkin` | `POST /actions/{actionId}/check-ins` | R2 | `action:write` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `timeline` | `GET /subjects/{subjectId}/timeline` | R2 | `subject:read` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `analyze` | `POST /analysis-runs` | R2 | `subject:analyze` | NAMED_SCHEMA | Contract đã có; vẫn cần tích hợp/test |
| `analysisStatus` | `GET /analysis-runs/{runId}` | R2 | `run:read` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `cancelAnalysis` | `POST /analysis-runs/{runId}/cancel` | R2 | `run:cancel` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `analysisResults` | `GET /analysis-runs/{runId}/results` | R2 | `run:read` | NAMED_SCHEMA | Contract đã có; vẫn cần tích hợp/test |
| `methodResult` | `GET /results/{resultId}` | R2 | `result:read` | NAMED_SCHEMA | Contract đã có; vẫn cần tích hợp/test |
| `createReport` | `POST /reports` | R2 | `subject:report` | NAMED_SCHEMA | Contract đã có; vẫn cần tích hợp/test |
| `reports` | `GET /subjects/{subjectId}/reports` | R2 | `subject:read` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `report` | `GET /reports/{reportId}` | R2 | `report:read` | NAMED_SCHEMA | Contract đã có; vẫn cần tích hợp/test |
| `reportRevisions` | `GET /reports/{reportId}/revisions` | R2 | `report:read` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `review` | `POST /reports/{reportId}/reviews` | R2 | `report:review` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `publish` | `POST /reports/{reportId}/publish` | R2 | `report:publish` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `exportReport` | `POST /reports/{reportId}/exports` | R2 | `report:export` | NAMED_SCHEMA | Contract đã có; vẫn cần tích hợp/test |
| `downloadArtifact` | `GET /artifacts/{artifactId}/download` | R2 | `artifact:download` | INLINE_SCHEMA | Contract đã có; vẫn cần tích hợp/test |
| `order` | `POST /orders` | R2 | `self` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `orderStatus` | `GET /orders/{orderId}` | R2 | `order:owner` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `checkout` | `POST /orders/{orderId}/checkout` | R2 | `order:owner` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `requestRefund` | `POST /orders/{orderId}/refund-requests` | R2 | `order:owner` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `paymentWebhook` | `POST /webhooks/payments/{providerId}` | R2 | `webhook_signature` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `entitlements` | `GET /entitlements` | R2 | `self` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `ticket` | `POST /support/tickets` | R2 | `self` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `ticketStatus` | `GET /support/tickets/{ticketId}` | R2 | `ticket:owner` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `privacyExport` | `POST /subjects/{subjectId}/data-exports` | R2 | `subject:privacy` | NAMED_SCHEMA | Contract đã có; vẫn cần tích hợp/test |
| `deleteSubject` | `POST /subjects/{subjectId}/deletion-jobs` | R2 | `subject:privacy` | NAMED_SCHEMA | Contract đã có; vẫn cần tích hợp/test |
| `deletionStatus` | `GET /deletion-jobs/{jobId}` | R2 | `job:owner` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `jobStatus` | `GET /jobs/{jobId}` | R2 | `job:owner` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `newAutomation` | `POST /automations` | R2 | `subject:automate` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `stopAutomation` | `DELETE /automations/{automationId}` | R2 | `automation:owner` | NO_BODY_EXPECTED | Contract đã có; vẫn cần tích hợp/test |
| `cases` | `GET /practice/cases` | R2 | `practitioner:assigned` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `caseDetail` | `GET /practice/cases/{caseId}` | R2 | `practitioner:assigned` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `courses` | `GET /academy/courses` | R2 | `public` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `assignment` | `POST /academy/assignments` | R2 | `enrollment:write` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `verifyCertificate` | `GET /certificates/{certificateId}` | R2 | `public_minimal` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `organizationOverview` | `GET /organizations/{organizationId}/overview` | R2 | `organization:member` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `partner` | `GET /partners/{partnerId}` | R2 | `partner:assigned` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `methodReleaseDraft` | `POST /admin/method-releases` | R2 | `method:editor` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `countryPackReview` | `POST /admin/country-packs` | R2 | `legal:reviewer` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `quality` | `GET /admin/quality` | R2 | `quality:reviewer` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `operations` | `GET /admin/operations` | R2 | `ops:reader` | GENERIC_SUCCESS_SCHEMA | Giữ contract riêng / đóng fields theo resource |
| `compareRuns` | `POST /analysis-runs/compare` | V2+ | `subject:read` | GENERIC_SUCCESS_SCHEMA | RunComparisonView |
| `previewMethod` | `POST /methods/{methodId}/preview` | V2+ | `method:preview` | GENERIC_SUCCESS_SCHEMA | MethodPreviewResult |
| `methodDependencies` | `GET /methods/{methodId}/dependencies` | V2+ | `method:read` | GENERIC_SUCCESS_SCHEMA | MethodDependencyPage |
| `methodTestVectors` | `GET /methods/{methodId}/test-vectors` | V2+ | `method:review` | GENERIC_SUCCESS_SCHEMA | GoldenVectorPage |
| `resolveHypotheses` | `POST /subjects/{subjectId}/hypotheses/resolve` | V2+ | `subject:write` | GENERIC_SUCCESS_SCHEMA | HypothesisResolutionReceipt |
| `runTrace` | `GET /analysis-runs/{runId}/trace` | V2+ | `subject:read` | GENERIC_SUCCESS_SCHEMA | RunTraceView |
| `runDependencies` | `GET /analysis-runs/{runId}/dependencies` | V2+ | `subject:read` | GENERIC_SUCCESS_SCHEMA | RunDependencyPage |
| `claimProvenance` | `GET /claims/{claimId}/provenance` | V2+ | `subject:read` | GENERIC_SUCCESS_SCHEMA | ClaimProvenanceView |
| `reviewReportV2` | `POST /reports/{reportId}/review` | V2+ | `report:review` | GENERIC_SUCCESS_SCHEMA | ReportReviewReceipt |
| `withdrawReportV2` | `POST /reports/{reportId}/withdraw` | V2+ | `report:withdraw` | GENERIC_SUCCESS_SCHEMA | ReportWithdrawalReceipt |
| `reportDiff` | `GET /reports/{reportId}/diff/{previousId}` | V2+ | `subject:read` | GENERIC_SUCCESS_SCHEMA | ReportDiffView |
| `newDeletionV2` | `POST /privacy/deletion-requests` | V2+ | `subject:delete` | GENERIC_SUCCESS_SCHEMA | DeletionAcceptedReceipt |
| `deletionStatusV2` | `GET /privacy/deletion-requests/{requestId}` | V2+ | `subject:read` | GENERIC_SUCCESS_SCHEMA | DeletionStatusView |
| `countryEligibility` | `GET /country-packs/{countryId}/eligibility` | V2+ | `self` | GENERIC_SUCCESS_SCHEMA | CountryEligibilityView |
| `releaseImpact` | `GET /operations/method-releases/{releaseId}/impact` | V2+ | `method:review` | GENERIC_SUCCESS_SCHEMA | MethodImpactPage |
| `freezeMethod` | `POST /operations/method-releases/{releaseId}/freeze` | V2+ | `method:release` | GENERIC_SUCCESS_SCHEMA | MethodFreezeReceipt |
| `resonanceSummaryV2` | `GET /subjects/{subjectId}/resonance/summary` | V2+ | `subject:read` | GENERIC_SUCCESS_SCHEMA | MetricSummaryView |
| `syncOfflineBatch` | `POST /subjects/{subjectId}/offline-batches` | V2+ | `subject:write` | GENERIC_SUCCESS_SCHEMA | OfflineBatchReceipt |
| `computeNumerologyFull` | `POST /numbers/numerology-full` | V3+ | `UNRESOLVED_FAIL_CLOSED` | REFERENCE_ONLY_RESPONSE | NumerologyFullResult wrapped by canonical MethodResult |
| `computeBatCuc` | `POST /numbers/bat-cuc` | V3+ | `UNRESOLVED_FAIL_CLOSED` | REFERENCE_ONLY_RESPONSE | BatCucResult wrapped by canonical MethodResult |
| `computePsychomatrix` | `POST /numbers/psychomatrix` | V3+ | `UNRESOLVED_FAIL_CLOSED` | REFERENCE_ONLY_RESPONSE | PsychomatrixResult wrapped by canonical MethodResult |
| `compareNumberAssets` | `POST /numbers/compare` | V3+ | `UNRESOLVED_FAIL_CLOSED` | REFERENCE_ONLY_RESPONSE | NumberComparisonView |
| `compareNameVariants` | `POST /names/compare` | V3+ | `UNRESOLVED_FAIL_CLOSED` | REFERENCE_ONLY_RESPONSE | NameComparisonView |
| `composeLifetime` | `POST /lifetime/compose` | V3+ | `UNRESOLVED_FAIL_CLOSED` | REFERENCE_ONLY_RESPONSE | LifetimeCompositionView |
| `createAnalysisBundle` | `POST /analysis-bundles` | V3+ | `UNRESOLVED_FAIL_CLOSED` | MISSING_SUCCESS_SCHEMA | AnalysisBundleAcceptedReceipt |
| `getAnalysisBundle` | `GET /analysis-bundles/{bundle_id}` | V3+ | `UNRESOLVED_FAIL_CLOSED` | MISSING_SUCCESS_SCHEMA | AnalysisBundleStatusView |
| `cancelAnalysisBundle` | `POST /analysis-bundles/{bundle_id}/cancel` | V3+ | `UNRESOLVED_FAIL_CLOSED` | MISSING_SUCCESS_SCHEMA | AnalysisBundleCancellationReceipt |
| `getMethodSourceConflicts` | `GET /methods/{method_id}/source-conflicts` | V3+ | `UNRESOLVED_FAIL_CLOSED` | MISSING_SUCCESS_SCHEMA | MethodSourceConflictPage |
| `getBatCucTable` | `GET /numbers/bat-cuc/table` | V3+ | `UNRESOLVED_FAIL_CLOSED` | MISSING_SUCCESS_SCHEMA | VersionedPairTableView |
| `getLifeDomains` | `GET /lifetime/domains` | V3+ | `UNRESOLVED_FAIL_CLOSED` | MISSING_SUCCESS_SCHEMA | VersionedLifeDomainPage |
| `getScopedProductEligibility` | `GET /products/{product_id}/eligibility` | V3+ | `UNRESOLVED_FAIL_CLOSED` | MISSING_SUCCESS_SCHEMA | ScopedProductEligibilityView |
| `createKnowledgeLegacyTransfer` | `POST /legacy-transfers` | V3+ | `UNRESOLVED_FAIL_CLOSED` | MISSING_SUCCESS_SCHEMA | KnowledgeTransferReceipt |
| `getTerritoryReleaseGates` | `GET /territories/{territory_id}/release-gates` | V3+ | `UNRESOLVED_FAIL_CLOSED` | MISSING_SUCCESS_SCHEMA | TerritoryReleaseGateView |
| `getMethodVersionHistory` | `GET /methods/{method_id}/versions` | V3+ | `UNRESOLVED_FAIL_CLOSED` | MISSING_SUCCESS_SCHEMA | MethodVersionPage |

## Bàn giao schema và bằng chứng

Xem API_CONTRACT_RECONCILIATION.json để lấy từng success status/media/schema ref, input refs, Idempotency-Key bounds, quyền nguồn và blocker. OPENAPI_UNIFIED_TARGET.json chứa cùng 99 operation và 68 schemas, không thay source nguyên bản. FORMULA_METHOD_EXECUTION_MATRIX.json tách method register ID, passport cũ, formula ID và demo dispatcher.

WP01 phải viết schema output theo resource, field-level authorization, response examples và negative cases; bind schema sau review. Ví dụ MethodPreview/RunCreate trong thư mục schemas là input contract, không mặc nhiên là output contract. ReferenceResult mô tả reference lab, không dùng như bản production MethodResult.

Kiểm thử hiện tại ở ../evidence/TEST_RECEIPT_BACKEND.json và CONTRACT_VALIDATION_RECEIPT.json có phạm vi synthetic local; chưa có provider/database/live evidence. Không loại blocker hoặc đổi x-lc-codegen-ready sang true chỉ vì schema parse hoặc demo pass.
