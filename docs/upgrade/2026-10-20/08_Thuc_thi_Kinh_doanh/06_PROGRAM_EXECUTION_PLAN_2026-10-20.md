# Program execution plan — amendment 2026-10-20

Status of implementation and gate evidence: `NOT_CHECKED`. This plan preserves the complete 2026-10-11 vision and makes sequencing, authority, capacity, cost and evidence explicit. It does not approve deployment, spend, vendors, price, country launch or any Q decision.

## 1. Canonical phase model

| Phase | Objective | Entry | Exit evidence | Products unlocked for next decision |
|---|---|---|---|---|
| P0 Containment | stop unknown legacy exposure and lock source/release identity | named incident/program authority and bounded surfaces | P0-01…10 receipts; clean-source/build allowlist; no unresolved public legacy route | none automatically |
| A Governance | decide claims, legal roles, purposes, methods, vendors and pilot scope | stable source baseline | Q packet outcomes with conditions; terminology/claim/source/right registers | allows B/C design, not intake/sale |
| B Trust/Data | identity, subject/tenant/object authorization, consent/grants and reversible data jobs | P0 controls plus applicable Q decisions | negative auth/RLS tests; export/delete/restore/migration rehearsal receipts | adult/self synthetic flows |
| C Core product | methods, API, responsive PWA, AI contracts and L1 synthetic flow | B contract baselines; method rights/release draft | 64-operation contract suite; 45-screen parity; L1 trace; WCAG critical-flow evidence | private-pilot candidate only |
| D Private paid beta | report factory, commerce consistency, operations and support | G01–G12/FPOS mappings evidenced for exact candidate | payment/entitlement/report reconciliation; reviewer capacity; backup/restore/rollback/incident receipts; decision packet | T3-specific invite cohort |
| E Measured expansion | L2–L5, practice/family foundation and academy foundation | beta metrics and kill rules evaluated | differentiated contracts, legal/privacy review and product-specific evidence | only the approved product/release/market |
| F Advanced/global | L6–L9, organization/API/trainer/regional capabilities | mature operations and each dedicated review | specialist/body, re-identification, partner/country/legal, continuity and exit evidence | only separately approved advanced scope |

Catalog suffixes `F_REVIEW`, `E_F_REVIEW` and `F_LEGAL` are conditional reviews inside this model, not missing phases. Design/research may overlap; data collection, payment, publishing and release cannot bypass the entry/exit gate.

### P0 containment clock and corrected dependency graph

The historical backlog serialized P0-01 through P0-10 as one chain. The current execution graph corrects that ordering while retaining each old value in `original_dependencies`: P0-01 establishes bounded authority; P0-08 verifies the clean source baseline; P0-02 inventories surfaces from that baseline; then P0-03 begins server-side containment while P0-05, P0-06 and P0-07 may proceed from the verified inventory/control points shown in the task contracts. P0-09 builds the allowlisted artifact from the clean baseline. P0-10 remains last and depends on P0-03/04/05/06/07/09 plus separate exact-candidate production authority.

Any 48–72 hour target applies only to the immediately authorized containment subset after a named commander, clean baseline, provider access and capable responders exist. It is not a promise that all ten P0 tasks, data classification, independent verification, provider deployment and rollback evidence will finish inside that window. Until real owners and capacity are assigned, P0 effort remains a planning range and production work remains separately authorized.

## 2. Critical path and parallel lanes

Critical path: P0 source/containment → Q1/Q3/Q4/Q5/Q9/Q12/Q14/Q15/Q20 decisions → identity/authorization/data contracts → method/source/rights release → API/result/job consistency → responsive L1 flow → AI/report verification → payment/entitlement/report reconciliation → security/accessibility/restore/rollback/support evidence → private-pilot decision.

Safe parallel lanes after source lock:

- Product/Method: portfolio contracts, terminology, method passport and synthetic fixtures.
- Trust/Data: identity, authorization, RLS design, profile versioning and migration rehearsal.
- API/Frontend: OpenAPI overlay and responsive components against mocks; no real intake.
- AI/Editorial: nine template contracts/evals on synthetic inputs; no public publishing.
- Commerce/Ops: provider/vendor decisions, sandbox ledgers, observability and recovery plans.
- Legal/Privacy/Academic/Global: rights, lawful purposes, country/curriculum reviews without opening product gates.

Integration checkpoints occur at contract freeze, synthetic vertical slice, private-beta candidate, measured expansion and advanced/global candidate. Every checkpoint reruns changed downstream tests.

## 3. Capacity and schedule model

The retained 140 tasks total 361–852 person-days. The 16 `UPG-*` tasks add 91–187 person-days, producing a planning inventory of 452–1,039 person-days before discovered remediation. With 6–8 core FTE and an explicit planning capacity of 18 productive person-days/FTE-month, this is about 3.1–9.6 raw team-months. Raw capacity is not elapsed delivery time: sequential gates, Founder/provider/legal decisions, independent review, pilot observation and remediation preserve the original conditional 12–24+ month horizon for the full portfolio.

Suggested core role coverage is Product/Program, Tech/Architecture, Backend/Data, Frontend/UX, AI/Knowledge, QA/Automation, with Security/SRE, Editorial/Method, Privacy/Legal, Finance/Commerce, Support/Academic and Partnerships as dedicated or fractional reviewers. One person may cover roles, but the author cannot be the sole verifier of a high-risk control.

## 4. Cost model

No approved day rate, vendor, currency, price or budget exists in this package. Q14/Q15/Q20 therefore block a monetary total. Finance must fill `COST_INPUTS` for low/base/high:

- loaded day rate per accountable role and country/currency;
- identity/database/hosting/AI/payment/storage/render/monitoring vendors and volume tiers;
- independent accessibility, security, privacy/legal and country reviews;
- source/content/translation/trademark licensing;
- customer support, reviewer/trainer capacity and refunds/disputes;
- 15–30% contingency range selected and justified for planning only.

`labor scenario = Σ(role person-days × approved rate)`; `cash scenario = labor + vendor + review/licensing + contingency`. Report both cash and person-days, assumptions, tax treatment, validity date and decision owner. Do not convert missing vendor evidence to zero.

## 5. RACI and authority

| Decision/deliverable | Accountable | Responsible | Consulted/independent verification | Authority boundary |
|---|---|---|---|---|
| product scope/claim | Product Lead | Product + Method/Editorial | Privacy/Legal, QA, users | Founder Q decision; no release implication |
| architecture/integration | Tech Lead | Backend/Data/Frontend/AI | Security/SRE/QA | source/change authority required |
| identity/privacy/data | Privacy/Data owner | Trust/Data engineers | Security/Legal/QA | production data access is separate |
| method/source/right release | Method Council | Method/Editorial | Legal/QA | no method release without source/right/test/approver |
| AI/report release | AI/Editorial lead | AI + Report engineering | Method/Privacy/QA | human review during beta; public auto-publish off |
| payment/commercial | Commerce/Finance owner | Commerce engineering | Legal/Support/QA | price/merchant/refund authority separate |
| deployment/operations | SRE/Release owner | Platform/SRE | Security/QA | exact candidate approval; rollback and restore receipts |
| country/partner/academy | respective Global/Academic owner | Partnerships/Academic | Legal/Privacy/Method/Support | country/product-specific approval only |

Names are intentionally absent until assigned. Assignment must name a real accountable person, backup and time window; this document does not invent approval.

## 6. Decision dependency ledger

The reviewable alternatives, recommendation trade-offs, affected tasks, cost status, approver roles and acceptance-receipt requirements for Q1–Q20 are in `DECISION_EXECUTION_PACKETS.json` and `.csv`. Every packet remains `PENDING_FOUNDER`, with `approval: null` and no production permission.

- Q1–Q8/Q12: product, method, claim and report contracts.
- Q9: identity, consent, privacy rights, offline storage and sharing.
- Q10–Q11: legacy/source/runtime containment and quarantine.
- Q13: free quota and graceful degradation.
- Q14: legal entity, controller/processor, merchant and invoicing.
- Q15: IdP, PostgreSQL, payment and AI provider choices.
- Q16: autonomy levels, reminders and kill switches.
- Q17: academy/practitioner scope, assessment and complaints.
- Q18: organization boundary and high-impact exclusion.
- Q19: country order and license/franchise classification.
- Q20: budget, staffing, thresholds, cohort and roadmap.

Tasks may prepare reversible design/evidence while a decision is pending, but they may not encode the undecided option as approved production behavior.

## 7. Work-item and evidence contract

`EXECUTION_BACKLOG.*` preserves all 140 original task IDs and all source rows remain byte-preserved under `docs/upgrade/sources/2026-10-11/package`. In the current execution copy, the ten P0 rows retain their historical dependency values in `original_dependencies` while `dependencies` uses the corrected Gate-0-first graph above; the other 130 original task records retain their original fields, and only prefixed `UPG-*` tasks are appended. `TASK_EXECUTION_CONTRACTS.*` supplies one contract for every original and added task: allowed paths, current and historical P0 dependencies, decision/gate dependencies, owner/reviewer roles, estimate, tests, negative tests, evidence and rollback. `REQUIREMENT_TRACE_MATRIX.*` links requirements to product/screen/API/task/test/evidence. A task workflow state such as `NOT_STARTED` is not an FPOS claim status.

A work item cannot be called complete until its required tests and receipt exist for the stated SHA/artifact/environment. A document, mock, demo, CI green check, HTTP 200 or self-marked checklist does not independently prove runtime, recovery, approval or release.

## 8. Cadence and stop rules

Weekly: dependency/decision/gate review, estimate variance and evidence quality. At each integration checkpoint: contract diff, privacy/security impact, cross-device/a11y suite, data migration/reconciliation, report regression and rollback/restore review. Pilot dashboard uses only approved denominators and distinguishes unknown from zero.

Stop the affected lane immediately for source identity ambiguity; unauthorized disclosure; unapproved production data/vendor/spend; irreversible migration; payment-entitlement inconsistency; fabricated/unsafe report claim; critical accessibility block; unbounded job/retry; lost correction/deletion/export; or missing rollback for a state-changing candidate. Resume only with owned remediation and new evidence; the plan itself cannot waive a gate.

