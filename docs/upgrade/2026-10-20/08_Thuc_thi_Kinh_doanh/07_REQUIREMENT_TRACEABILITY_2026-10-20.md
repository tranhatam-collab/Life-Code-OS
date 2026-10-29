# Requirement traceability and evidence rules — amendment 2026-10-20

The machine-readable source is `REQUIREMENT_TRACE_MATRIX.json` with CSV parity. It covers every retained product, all 45 registered screens, all nine report levels and cross-cutting PWA/security/data/commerce/operations requirements. Each row identifies the screen/API/task/test/evidence path; absence is explicit rather than silently treated as not applicable.

## Interpretation

- A requirement is a planned obligation, not proof that implementation exists.
- `operation_id` values reference the retained 64-operation `04_Backend_API/API_OPERATIONS.json`; no route is renamed here.
- A test ID is a required future evidence slot. It is not a passed test until a receipt records command, build/SHA, environment, counts and result.
- `claim_status` follows FPOS vocabulary. Task workflow states remain in the backlog.
- A blank screen or API list is permitted only when the row is not a direct UI/API obligation. It must carry `non_screen_reason` or `non_api_reason`, respectively; the two reasons are not interchangeable.
- Product and report rows may reference multiple screens, operations and tasks. UI rows provide one exact route-to-operation/task join for all 45 screens.
- This matrix guarantees the forward direction requirement → product/screen/API/task/test/evidence. It does not claim that every one of the 156 implementation tasks owns a separate requirement row: 69 unique tasks are directly referenced here, while the complete 156-task decomposition and evidence contracts remain in `EXECUTION_BACKLOG.*` and `TASK_EXECUTION_CONTRACTS.*`.

## Coverage gates

1. Every catalog `product_id` occurs in at least one `PRODUCT` row.
2. Every `screen_id` occurs in exactly one primary `SCREEN` row and resolves to its route/API/task contract.
3. Every Level 1–9 occurs in one `REPORT_LEVEL` row and links reader/review/export operations.
4. Every operation referenced by the screen registry resolves to the API registry; `static` and `local deterministic` are explicitly non-API.
5. Every task reference resolves to the retained or appended backlog and to a work-item contract.
6. Every row has a positive test, relevant negative test and evidence path; no evidence URI is presented as already populated.
7. Release decisions evaluate the exact candidate and applicable custom/FPOS gates; trace coverage alone does not produce `GO`.

Validation output belongs in a generated receipt outside the source-of-truth files, so regenerating evidence cannot silently modify requirements.

