# Nine-level AI/report execution contracts — amendment 2026-10-20

This document makes the nine retained report levels operationally different without changing their original vision or page budgets. Machine-readable parity is in `NINE_LEVEL_REPORT_CONTRACTS.json` and `.csv`. All implementation, evaluation and reviewer capacity claims are `NOT_CHECKED`.

## Shared non-negotiable contract

Every generated statement is typed as `fact`, `calculated_result`, `user_observation`, `symbolic_interpretation`, `scenario`, `recommendation`, or `limitation`. It references permitted inputs, profile version, method release, source/right where applicable, locale content release and generation/review versions. Unknown, inapplicable and withheld values remain distinct; `null` is not coerced to zero or prose certainty.

AI may organize, explain, translate within approved terminology and draft actions. AI may not invent input, source, consent, method result, professional qualification or approval; diagnose; assert destiny; infer health/ethics/loyalty/work worth from face/hand/name/number; publish publicly; change entitlement; or bypass human review and release gates.

The report pipeline is: typed snapshot → deterministic validations → scoped retrieval after authorization filtering → claim plan → draft → numerical/source/prohibition checks → human review where required → immutable publish snapshot → accessible rendering/export → correction/withdrawal path. Retrieval authorization is applied both before and after search. Provider output is untrusted and cannot carry access control.

## Differentiated level contracts

| Level | Evidence/input boundary | Report emphasis | AI role | Required reviewer | Level-specific rejection |
|---|---|---|---|---|---|
| L1 Self Signal | adult/self, goal, permitted name/date method inputs, precision/timezone and method release | three-minute summary; transparent calculation; unknowns; one 30-day action | explain deterministic output and assemble sourced self-observation questions | editorial + method reviewer during beta | arithmetic/date/name mismatch; fixed-trait or destiny language; no source/limitation |
| L2 Inner Architecture | L1 plus self-described needs, values, roles and 3–5 situations | tensions between stated values/roles and choices; confirm/reject prompts | cluster only user-provided situations and draft alternatives | editorial/behavioral-scope reviewer | “read mind/true self” claim; inferred event or motive; contradiction hidden |
| L3 Behavior Code | contextual journal/check-ins and approved questionnaire releases | behavior by context, frequency/uncertainty and reversible experiment | summarize patterns with denominators/time windows; never diagnose | editorial + questionnaire/method reviewer | clinical label; pattern without minimum observations; causal claim from correlation |
| L4 Work & Wealth | skills/evidence, work history, goals/resources and user-entered scenarios | role/resource trade-offs, cash-flow scenarios and assumptions | calculate scenarios from typed inputs; explain sensitivity | editorial + finance-scope reviewer | investment/credit/employment decision; symbolic cycle used as financial evidence; unstated assumption |
| L5 Relationship Field | each adult’s scoped consent, shared facts and self-reported agreements/conflicts | perspective-separated needs, boundaries and dialogue plan | synthesize only mutually permitted sections; preserve speaker/source | editorial + relationship/consent reviewer | loyalty/compatibility destiny claim; one party’s private content leaked; coerced joint conclusion |
| L6 Life Timeline | dated sourced events, precision/timezone, plans and separately labeled symbolic cycles | four tracks, gaps, version change and scenarios—not lifespan prediction | normalize dates, detect conflicts and draft scenario branches | editorial + timeline/method reviewer | invented event/date; age range presented as lifespan; symbolic/factual track merged |
| L7 Body Intelligence | dedicated approval, explicit purpose/consent, permitted self-observation and environment journal; images/medical data closed by default | environmental/self-care observations and referral boundaries | summarize permitted diary only; no image inference in baseline | specialist + privacy/legal + method reviewer | disease/hormone/personality/morality inference; unapproved image/body field; missing DPIA/specialist gate |
| L8 Mission Path | self-chosen values, evidenced capabilities, desired service experiments, responsibilities/resources | multiple service hypotheses, trade-offs and 90-day experiments | connect evidence to alternatives and expose uncertainty | editorial + method/reviewer appropriate to domain | single destined mission; pressure to sacrifice safety/finance/relationship; capability without evidence |
| L9 Full Life Code | only released and consented components L1–L8; excluded/inapplicable parts explicit | deduplicated synthesis, disagreements between versions/methods, priorities and action system | reconcile references without erasing disagreement; compress repeated content | senior editorial + method + privacy review | filler to page target; unavailable L7 silently included; contradictions flattened; “complete life truth” claim |

## Acceptance dimensions per level

Each level needs its own golden synthetic fixture, boundary/null fixture, contradiction fixture, unauthorized-data fixture, prompt-injection fixture, locale fixture and correction/withdrawal fixture. Tests assert: schema; calculation/date precision; claim-lineage completeness; source/right availability; section-specific allowed input; prohibition taxonomy; stable snapshot/version; accessible HTML; print/PDF/DOCX structure where in scope; token/page budget without filler; cost/latency limits; and reviewer outcome.

A level does not pass because text exists or reaches the page range. The page budgets remain editorial ceilings/reference bands. Empty evidence produces an explicit limitation and safe next step, not generated padding.

## Review and release states

Workflow states are separate from FPOS evidence statuses: `draft`, `automated_checks_failed`, `awaiting_human_review`, `changes_requested`, `approved_for_specific_release`, `published`, `corrected`, `withdrawn`. Only an authorized reviewer can move a report into `approved_for_specific_release`; this file grants nobody that authority.

Public automatic publishing stays disabled. L1–L6/L8/L9 require human review during beta; L7 additionally requires its specialist/privacy/legal gates. Review sampling may be reduced only after a separately approved evidence-based policy, with kill switches and retrospective audit.

