# AI evaluation, cost and demo plan — amendment 2026-10-20

## 1. Evaluation sets

Maintain versioned, synthetic evaluation sets for each level and locale. Every case records fixture/source rights, permitted purpose/subject, exact typed inputs, method releases, expected deterministic results, allowed/forbidden claim classes, expected citations/limitations, reviewer rubric and hash. Real customer data is excluded unless a separate lawful, consented and minimized research protocol is approved.

Suites:

1. schema and null/decimal/timezone determinism;
2. claim-to-input/method/source lineage;
3. unsupported-claim and prohibited-domain detection;
4. authorization, tenant/subject/grant and retrieval-filter isolation;
5. prompt injection in VI/EN and source-document instructions;
6. conflicting, stale, withdrawn and revoked method/source cases;
7. correction, version diff and withdrawal propagation;
8. readability, non-coercive Vietnamese and glossary consistency;
9. accessible HTML/export structure;
10. provider timeout/rate limit/malformed output/fallback;
11. token, latency and cost-accounting accuracy;
12. human-review inter-rater disagreement and escalation.

## 2. Evaluation decisions

Before a pilot, Product/Method/Privacy define severity and sample. Proposed hard stops are any unauthorized disclosure; invented fact/source/result; high-risk medical, financial, employment or destiny claim; deterministic mismatch; public auto-publication; or inability to correct/withdraw. Soft quality thresholds require approved denominators and confidence intervals; they cannot be backfilled after seeing results.

Record false positive/negative examples for safety checks. A model/provider change, prompt/policy change, retrieval index change, method release or template release triggers the affected regression set. A green aggregate score cannot mask a hard-stop case.

## 3. Provider and cost contract

Provider selection is Q15 and remains pending. Evaluation uses an adapter with per-purpose allowlist, region/data-retention setting, request/response size limits, timeout, concurrency, retry budget and circuit breaker. Never send credentials, raw payment data, other subjects’ content or fields outside the approved prompt manifest.

Per successful outcome record input/output tokens or provider units, request count, cache use, latency, retry, fallback, render/storage and human review minutes. Cost per completed eligible report is:

`provider + compute + retrieval + render/storage + reviewer time + support allocation`.

Currency and unit prices remain unapproved inputs. When a budget is reached, deterministic content and existing data remain accessible; generation degrades truthfully and does not silently shorten safety/source sections.

## 4. Demo sequence

The offline trace explorer for DEMO-AI-01 loads a synthetic snapshot and renders each claim with type, exact allowed inputs, method/source release, uncertainty, transformation steps, policy decisions and reviewer state. It never calls production providers. DEMO-AI-02 injects a malicious source instruction and shows it quarantined. DEMO-AI-03 removes a grant and proves post-filter retrieval returns no content. DEMO-AI-04 changes a fact and shows a new report revision while the prior snapshot remains immutable. DEMO-AI-05 simulates provider failure and shows bounded retry/fallback without a fabricated report. DEMO-AI-06 exercises all nine differentiated templates and rejects an L7/L9 request when dedicated evidence is missing.

Receipts include fixture/model/provider/prompt/policy/template/method versions; exact test command and counts; cost/latency; redacted trace; reviewer; failures/skips/TODO; and SHA/artifact. A demo video alone is insufficient evidence.

