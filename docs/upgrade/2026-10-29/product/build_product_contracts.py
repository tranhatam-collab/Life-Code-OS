"""Build additive planning contracts. Reads source data; never executes source code."""
from pathlib import Path
import copy
import csv
import hashlib
import json

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
SOURCES = ROOT / 'docs/upgrade/sources/2026-10-29'
V2 = SOURCES / 'v2/package/LIFE_CODE_OS_V2_2026-10-20'
V3 = SOURCES / 'v3/package/LIFE_CODE_OS_ALL_IN_ONE_V3_2026-10-29'
OLD = ROOT / 'docs/upgrade/2026-10-20'
read_files = set()

def read(p):
    read_files.add(p)
    return p.read_text(encoding='utf-8-sig')

def load(p):
    return json.loads(read(p))

def ref(p):
    return str(p.relative_to(ROOT))

def dump(name, rows):
    (OUT / name).write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')

products_source = load(V3 / '06_PRODUCTS/PRODUCT_CATALOG_ALL_IN_ONE.json')
products_v2 = load(V2 / '03_PRODUCT/PRODUCT_CATALOG_V2.json')
baseline = load(V2 / '03_PRODUCT/PRODUCT_CATALOG_BASELINE.json')
old_products = load(OLD / '01_Chien_luoc_San_pham/PRODUCT_EXECUTION_EXTENSION.json')
old_screens = load(OLD / '05_Frontend_UI/SCREEN_EXECUTION_EXTENSION.json')
old_reports = load(OLD / '06_AI_Bao_cao/NINE_LEVEL_REPORT_CONTRACTS.json')
screens_v2 = load(V2 / '07_UI/SCREEN_REGISTRY_COMBINED.json')
add_v2 = load(V2 / '07_UI/SCREEN_ADDITIONS_V2.json')
add_v3 = load(V3 / '06_PRODUCTS/SCREEN_REGISTRY_V3_ADDITIONS.json')
screens_all = load(V3 / '06_PRODUCTS/SCREEN_REGISTRY_ALL.json')
levels = load(V3 / '06_PRODUCTS/NINE_LEVELS_INTEGRATED_V3.json')
assert screens_all == screens_v2 + add_v3
assert load(V3 / '06_PRODUCTS/SCREEN_REGISTRY_V2_PRESERVED.json') == screens_v2
assert load(V3 / '06_PRODUCTS/PRODUCT_CATALOG_V2_PRESERVED.json') == products_v2
for before, after in zip(baseline, products_v2):
    assert all(after[k] == val for k, val in before.items())
csv_rows = list(csv.DictReader(read(V3 / '06_PRODUCTS/PRODUCT_CATALOG_ALL_IN_ONE.csv').splitlines()))
assert len(csv_rows) == len(products_source) == 28
for a, b in zip(products_source, csv_rows):
    assert all(('' if a.get(k) is None else str(a[k])) == v for k, v in b.items())

openapi_path = V3 / '07_BACKEND/openapi.v3.target.json'
openapi = load(openapi_path)
operations = {o['operationId']: {'source_method': verb.upper(), 'source_path': path}
              for path, verbs in openapi['paths'].items() for verb, o in verbs.items()
              if isinstance(o, dict) and 'operationId' in o}
assert len(operations) == 99

shared_product = {
    'contract_status': 'DESIGN_ONLY_NOT_IMPLEMENTED_OR_RELEASED',
    'approval_status': 'APPROVAL_PENDING',
    'api_contract_ref': 'docs/upgrade/2026-10-29/backend/OPENAPI_UNIFIED_TARGET.json',
    'authority': 'planning proposal; no source document creates release, price, consent or legal approval',
    'workspace_rule': 'server checks account, subject, tenant, purpose, active grant, method release and entitlement where applicable; payer is not data owner',
    'required_states': ['ready', 'partial', 'needs_input', 'not_eligible', 'method_not_released', 'revoked', 'error'],
    'privacy_rights': {'paywalled': False, 'data_export_and_deletion_require_purchase': False, 'service_data_is_training_consent': False},
    'billing': {'amount': None, 'currency': None, 'approved_price_version': None, 'enable_paid_checkout': False,
                'purchase_of_previous_report_required': False, 'order_payment_entitlement_job_report_are_distinct': True},
    'release_evidence': ['approved_scope_and_method_versions', 'typed_input_output_schema', 'server_authorization_negative_receipts',
                         'deterministic_fixture_receipts', 'phone_desktop_a11y_receipts', 'reviewer_receipt_for_exact_snapshot',
                         'correction_withdrawal_and_deletion_receipts', 'separate_staging_runtime_and_release_receipts'],
}

extra_specs = {
 'LC-NUM-ATLAS': {
  'owner': 'Product + Method', 'train': 'T1_EXTENSION_PENDING', 'eligible_subject':'adult_self; guest synthetic examples only',
  'screens': ['V3-UI-059','V3-UI-060','V3-UI-061','V3-UI-062','V3-UI-063','V3-UI-064','V3-UI-065'],
  'ops': ['computeNumerologyFull','compareNameVariants','computeBatCuc','getBatCucTable','computePsychomatrix','compareNumberAssets'],
  'methods': ['NUM23','NAME-UNICODE','BCLC64','TAIL80','PSYCHO17'],
  'inputs': ['purpose and active subject grant','versioned name/date hypotheses with Unicode/Y/reduction policy','number string preserving zero and pair position','source table/rule version'],
  'outputs': ['23 indices with intermediate steps and explicit nulls','name variants kept separate','Bat Cuc pair segments and transition matrix','strict versus diagnostic 0/5 differences','tail80 source-row citation','raw versus working matrix and 17 positions'],
  'exclusions': ['unreleased results presented as personal truth','one aggregate good/bad fate score','medical/personality/wealth prediction from number or matrix'],
  'negative': ['empty/Unicode/Y variants','leading zeros','unsupported 0/5 policy','missing source table','mismatched method version','cross-subject access','withdrawn rule'],
  'dependency': 'Extension of retained LC-NUMBERS and report components; no replacement or automatic new entitlement.'},
 'LC-LIFE-MAP': {
  'owner': 'Product + Timeline/Method', 'train': 'T6_EXTENSION_PENDING', 'eligible_subject':'adult_self_or_explicit_scoped_reader',
  'screens': ['UI-19','V3-UI-066','V3-UI-067'], 'ops': ['getLifeDomains','composeLifetime','timeline','createPlan','getScopedProductEligibility'],
  'methods': ['LIFE-DESIGN','NUM-LIFE-CYCLES'],
  'inputs': ['self-selected domains from versioned 18-domain dictionary','sourced events with date precision and timezone','user plans and separate released symbolic cycle inputs','active purpose-specific rights'],
  'outputs': ['history, plan, symbolic cycle and hypothesis/scenario tracks kept distinguishable','100 age intervals as navigable planning grid, empty when unknown','source/precision/filter and change history','reversible next action'],
  'exclusions': ['invented biography','predicted lifespan/death','symbolic cycle treated as historical evidence','mandatory nine life stages'],
  'negative': ['unknown birth date','contradicting events','partial date/timezone','track toggle without label loss','revoked event source','ages 80/99/100/120 retained without truncating global history','plan missing canonical ID/version'],
  'dependency': 'Extends LC-L6 timeline rather than replacing its rich report contract.'},
 'LC-LEGACY': {
  'owner': 'Product + Privacy + Editorial', 'train': 'T6_EXTENSION_PENDING', 'eligible_subject':'adult_owner_or_separately_verified_scoped_recipient',
  'screens': ['V3-UI-068','UI-14','UI-25'], 'ops': ['createKnowledgeLegacyTransfer','grants','grant','revokeGrant','reportRevisions'],
  'methods': ['LINEAGE'],
  'inputs': ['rights-cleared text/audio and source ownership','named recipient and separately verified rights','transfer scope, conditions and expiry','owner review and immutable version'],
  'outputs': ['private knowledge collection and rights manifest','recipient-specific preview without unauthorized content','transfer request receipt and revocation impact','immutable version history'],
  'exclusions': ['automatic legal inheritance or estate execution','payer receives all subject data','unverified recipient notification/content disclosure','unlicensed third-party writing/audio'],
  'negative': ['revoked grant','wrong recipient','expired transfer','unlicensed content','duplicate submission','export after revocation','deleted owner source'],
  'dependency': 'Knowledge-sharing workflow only; legal inheritance and automated posthumous release need dedicated decisions, schema and legal review.'},
 'LC-REGION-KIT': {
  'owner': 'Partner + Legal + Localization', 'train': 'T8_EXTENSION_PENDING', 'eligible_subject':'authorized_partner_and_territory_legal_reviewer',
  'screens': ['V2-S11','UI-41','UI-45'], 'ops': ['countryEligibility','getTerritoryReleaseGates','countryPackReview','partner'],
  'methods': [],
  'inputs': ['territory and product scope','local legal entity and data roles','locale source/license/editor receipts','support/escalation and partner class','brand and contract versions'],
  'outputs': ['territory-by-product release checklist with dated evidence','unresolved restrictions and responsible reviewer','locale parity and support rehearsal receipts','explicit allowed/blocked scope'],
  'exclusions': ['global release implied by a translated UI','franchise grant from software status','local legal opinion invented by AI','country readiness inferred from market size'],
  'negative': ['missing legal entity','wrong territory/product','expired license','minor product requested','partner revoked','unreviewed translation'],
  'dependency': 'Operational kit for retained LC-REGIONAL; referral/practitioner/institution/regional franchise remain distinct agreements.'},
 'LC-RESEARCH-STUDIO': {
  'owner': 'Method + Rights + QA', 'train': 'T0_RESEARCH_PENDING', 'eligible_subject':'authorized_method_editor_reviewer_with_separation_of_duties',
  'screens': ['V3-UI-069','V2-S06','V2-S07','V2-S08','UI-42'],
  'ops': ['getMethodSourceConflicts','getMethodVersionHistory','methodDependencies','methodTestVectors','methodReleaseDraft','releaseImpact'],
  'methods': ['LINEAGE'],
  'inputs': ['licensed source edition and provenance','explicit school/policy variants','typed rule and test vectors','known limits and conflicts','independent reviewer identity'],
  'outputs': ['source conflict comparison without silent winner','versioned rule proposal and reproducible fixtures','downstream impact and withdrawal list','research/reference/released state shown separately'],
  'exclusions': ['editor becomes sole approver','reference code implies production release','unlicensed sources embedded in exports','silent rule changes to published reports'],
  'negative': ['missing source rights','rule conflict','source revoked','cyclic dependency','author self-review','stale approval','private PII search'],
  'dependency': 'Research tools feed method review; no publication/deploy/approval authority is granted by this screen.'},
}

products = []
old_product_map = {x['product_id']: x for x in old_products}
for incoming in products_source:
    pid = incoming['product_id']
    prior = old_product_map.get(pid)
    row = copy.deepcopy(prior) if prior else {
        'amendment_version': '2026-10-29', 'product_id': pid, 'catalog_name_vi': incoming['name_vi'],
        'launch_train': extra_specs[pid]['train'], 'earliest_catalog_phase': incoming['phase'],
        'eligible_subject': extra_specs[pid]['eligible_subject'],
        'delivery_surfaces': ['responsive_web','installable_pwa_progressive_enhancement','desktop_web'],
        'native_app_in_scope': False, 'accountable_role': extra_specs[pid]['owner'],
        'reviewer_roles': ['Product','Method','Privacy','QA'],
        'decision_dependencies': ['Q31','Q39','Q40','Q45'], 'custom_gate_ids': [],
        'primary_screen_ids': extra_specs[pid]['screens'], 'api_operation_ids': extra_specs[pid]['ops'],
        'demo_flow_ids': [], 'estimate_low_person_days_non_additive': None,
        'estimate_high_person_days_non_additive': None, 'estimate_basis': 'Not estimated; break down after schema/route decision',
        'cost_model_id': None, 'currency': None, 'monetary_cost_status': 'PENDING_APPROVED_SCOPE_AND_RATES',
        'success_metric_ids': [], 'kill_metric_ids': ['unauthorized_disclosure','unsupported_claim','silent_source_change'],
        'claim_status': 'NOT_CHECKED', 'evidence_required': shared_product['release_evidence']}
    row['integration_version'] = '2026-10-29'
    row['retention'] = {'old_r2_fields_preserved': prior is not None, 'source_product_id': pid,
                        'incoming_ref': ref(V3 / '06_PRODUCTS/PRODUCT_CATALOG_ALL_IN_ONE.json'), 'incoming_raw': incoming}
    row['v3_execution'] = copy.deepcopy(shared_product)
    row['v3_execution']['unified_entrypoint'] = 'one profile; only separately consented workspaces; clear previous context on switch'
    if not prior:
        row['v3_execution'].update(copy.deepcopy(extra_specs[pid]))
        row['v3_execution']['exit_gates'] = ['input_output_and_authorization_schema_approved','method_and_source_rights_released_where_used','all_listed_negative_cases_pass','phone_desktop_and_assistive_technology_receipts','exact_snapshot_human_review','billing_disabled_until_approved_price_and_provider_reconciliation','runtime_release_separately_authorized']
    else:
        row['v3_execution']['scope'] = 'Keep prior execution contract and enrich with incoming product data; no prior train or estimate is silently replaced.'
    if pid.startswith('LC-L') and pid[4:].isdigit():
        lev = next(x for x in levels if x['product_id'] == pid)
        row['v3_execution']['report_contract_id'] = 'RPT-L' + str(lev['level'])
        row['v3_execution']['method_candidates_register62'] = lev['method_candidates']
        row['v3_execution']['method_release_status'] = 'ALL_CANDIDATES_NOT_PRODUCTION_RELEASED'
    products.append(row)

screen_specs = {
 'V2-S01': ('/lab/cases','synthetic_lab_user',['cases','caseDetail'],['V2-FE-03'],['NUM23','BCLC64','TAIL80'], 'Browse synthetic cases, filter by known/unknown inputs, inspect expected result before running.', ['real_subject_input_blocked','demo_api_unavailable']),
 'V2-S02': ('/app/profiles/:id/hypotheses','subject_owner',['listHypotheses','newHypothesis','resolveHypotheses','compareRuns'],['V2-FE-02'],[], 'Compare explicit date hypotheses without selecting truth from interpretation.', ['hypothesis_unresolved','resolution_requires_source']),
 'V2-S03': ('/app/runs/:id/trace','scoped_subject_reader',['runTrace','claimProvenance','methodDetail'],['V2-FE-04'],[], 'Expand input, rule, intermediate value and source at each step.', ['source_unavailable','trace_redacted']),
 'V2-S04': ('/app/runs/compare','scoped_subject_reader',['compareRuns','analysisResults'],['V2-FE-04'],[], 'Compare like-for-like runs with explicit changed input/rule version.', ['incomparable_versions','cross_subject_compare_denied']),
 'V2-S05': ('/app/sync/conflicts','subject_owner',['syncOfflineBatch'],['V2-FE-09','V3-INT-06'],[], 'Choose server/local/merge per field after version conflict; retain unsent draft until confirmed.', ['conflict','reauth_required','purge_required']),
 'V2-S06': ('/practice/methods/:id/dependencies','authorized_method_reviewer',['methodDependencies','runDependencies'],['V2-OPS-07'],['LINEAGE'], 'Inspect dependency direction and affected releases, excluding unauthorized source text.', ['cycle_detected','source_rights_redacted']),
 'V2-S07': ('/ops/methods/review','authorized_method_editor_and_separate_reviewer',['methodReleaseDraft','methods','methodTestVectors'],['V2-OPS-07'],[], 'Prepare versioned review packet; separate author, reviewer and publisher.', ['review_conflict','release_blocked','approval_stale']),
 'V2-S08': ('/ops/releases/:id/impact','authorized_method_or_operations_reviewer',['releaseImpact','freezeMethod','withdrawReportV2'],['V2-OPS-07'],['LINEAGE'], 'Preview authorized downstream impact before separately authorized freeze/withdrawal.', ['impact_incomplete','confirmation_required','already_frozen']),
 'V2-S09': ('/app/privacy/sharing','subject_owner',['grants','grant','revokeGrant'],['V2-FE-10'],[], 'Review recipient, purpose, fields and expiry; revoke and inspect propagation receipt.', ['grant_expired','revocation_pending','recipient_denied']),
 'V2-S10': ('/app/privacy/deletions/:id','subject_owner_reauthenticated',['deletionStatus','deletionStatusV2'],['V2-FE-10'],[], 'Track deletion per storage layer and backup expiry without claiming premature completion.', ['legal_hold','partial_failure','backup_expiry_pending']),
 'V2-S11': ('/partners/countries/:code','authorized_partner_and_legal_reviewer',['countryEligibility','getTerritoryReleaseGates'],['V3-INT-07'],[], 'See territory/product eligibility, pending legal/source/editor/support evidence.', ['territory_not_released','evidence_expired']),
 'V2-S12': ('/lab/reports','synthetic_lab_user',[],['V2-AI-05'],[], 'Inspect synthetic full, missing-data and conflicting-date report samples.', ['null_sections_explained','source_rights_blocked']),
 'V3-UI-058': ('/app/home','authenticated_scoped_user',['subjects','overview','getScopedProductEligibility'],['V3-INT-01'],[], 'Choose an authorized subject, purpose and workspace; show only eligible actions.', ['tenant_not_selected','no_authorized_workspace','context_switching']),
 'V3-UI-059': ('/app/numbers/numerology','subject_owner_or_scoped_reader',['computeNumerologyFull','runTrace'],['V3-INT-01'],['NUM23'], 'Read 23 indices with intermediate reductions and original input version.', ['reduction_policy_pending','unknown_input']),
 'V3-UI-060': ('/app/names/variants','subject_owner_or_scoped_reader',['compareNameVariants'],['V3-INT-01'],['NAME-UNICODE','NUM23'], 'Compare original/used names and Y/Unicode policies without silently normalizing away differences.', ['name_variant_missing','y_policy_pending']),
 'V3-UI-061': ('/app/numbers/bat-cuc/segments','subject_owner_or_scoped_reader',['computeBatCuc','getBatCucTable'],['V3-INT-01'],['BCLC64'], 'Inspect digit-pair position and source row, including leading zeros and unsupported segments.', ['unsupported_pair','policy_not_selected']),
 'V3-UI-062': ('/app/numbers/bat-cuc/transitions','subject_owner_or_scoped_reader',['computeBatCuc'],['V3-INT-01'],['BCLC64'], 'Inspect transitions between groups with keyboard-readable table and separate reflective prompts.', ['no_transition','incomplete_segments']),
 'V3-UI-063': ('/app/numbers/bat-cuc/policies','subject_owner_or_scoped_reader',['computeBatCuc','compareNumberAssets'],['V3-INT-01'],['BCLC64'], 'Compare strict and diagnostic 0/5 policies with visibly labeled disagreements.', ['strict_rejects_0_5','diagnostic_not_canonical']),
 'V3-UI-064': ('/app/numbers/tail80','subject_owner_or_scoped_reader',['previewMethod','methodDetail'],['V3-INT-01'],['TAIL80'], 'Inspect tail80 code and exact source table row; zero policy remains explicit.', ['table_not_licensed','zero_policy_pending']),
 'V3-UI-065': ('/app/numbers/psychomatrix','subject_owner_or_scoped_reader',['computePsychomatrix'],['V3-INT-01'],['PSYCHO17'], 'Toggle raw/working matrices, four working values and 17 positions with count derivation.', ['date_policy_pending','raw_working_difference']),
 'V3-UI-066': ('/app/life/domains','subject_owner',['getLifeDomains','composeLifetime'],['V3-INT-02'],['LIFE-DESIGN'], 'Select relevant domains out of 18; leave unchosen domains empty.', ['domain_not_selected','dictionary_version_stale']),
 'V3-UI-067': ('/app/life/tracks','subject_owner_or_scoped_reader',['composeLifetime','timeline'],['V3-INT-02'],['LIFE-DESIGN','NUM-LIFE-CYCLES'], 'Navigate sourced history, plans, cycles and hypotheses/scenarios as distinguishable tracks; retain history ages 100+ outside the initial navigation grid.', ['precision_unknown','event_conflict','cycle_not_released','extended_age_range_required']),
 'V3-UI-068': ('/app/legacy/sharing','subject_owner_or_verified_recipient',['createKnowledgeLegacyTransfer','grants','revokeGrant'],['V3-INT-02'],['LINEAGE'], 'Preview recipient-specific knowledge transfer scope and version before explicit submission.', ['recipient_unverified','transfer_expired','rights_missing']),
 'V3-UI-069': ('/practice/methods/:id/source-conflicts','authorized_method_reviewer',['getMethodSourceConflicts','getMethodVersionHistory'],['V3-INT-03'],['LINEAGE'], 'Read source/school conflicts and unresolved questions; link evidence without silently choosing truth.', ['rights_redacted','source_conflict_unresolved']),
}
universal = ['loading','empty','error','blocked','ready','partial','needs_input','offline','stale','forbidden']
a11y = ['WCAG_2_2_AA_critical_flows','keyboard_and_logical_focus','focus_visible_and_not_obscured','errors_linked_to_labels_and_announced','320px_reflow_and_400_percent_zoom','orientation_and_reduced_motion','screen_reader_table_and_matrix_alternative','not_color_only','prefer_44px_targets_without_misstating_AA_minimum']
screens = []
old_screen_map = {x['screen_id']: x for x in old_screens}
for incoming in screens_all:
    sid = incoming['screen_id']
    prior = old_screen_map.get(sid)
    if prior:
        row = copy.deepcopy(prior)
    else:
        route, principal, ops, tasks, methods, action, specific = screen_specs[sid]
        row = {'amendment_version':'2026-10-29','requirement_id':'REQ-SCREEN-'+sid,'screen_id':sid,
               'target_route':route,'category':'proposed_extension','principal':principal,
               'source_task_id':tasks[0], 'api_contract':'Resolve operationId in normalized OpenAPI; paths not copied from source',
               'operation_id':ops[0] if ops else None,
               'non_api_reason':'Synthetic fixture-only preview; no private production API implied' if not ops else None,
               'universal_states':universal,'specific_states':specific,
               'phone_320_390':'Single-column tasks; sticky actions do not obscure keyboard/focus; matrix has labeled table alternative.',
               'desktop_1280_plus':'Bounded reading width; comparison can use aligned columns without changing permissions or meaning.',
               'parity_rule':'same scope, data, provenance, state, next action and server checks across responsive surfaces',
               'offline_policy':'network-only private operations; permitted drafts require explicit opt-in, TTL, conflict handling and purge',
               'service_worker_cache_policy':'no private API, report, journal, token or grant caching by default',
               'pwa_install_rule':'progressive enhancement after support detection; no native app claim',
               'accessibility_contract':a11y,
               'test_ids':['UIT-'+sid+'-'+t for t in ['PHONE','DESKTOP','A11Y','OFFLINE','NEGATIVE']],
               'fixture_id':'FX-'+sid+'-SYNTHETIC','evidence_path':'evidence/ui/'+sid+'/<sha>/receipt.json','claim_status':'NOT_CHECKED'}
    row['integration_version'] = '2026-10-29'
    row['incoming_source'] = {'ref':ref(V3/'06_PRODUCTS/SCREEN_REGISTRY_ALL.json'),'raw':incoming}
    row['v3_execution'] = {
        'contract_status':'PRESERVED_DESIGN_REQUIREMENT' if prior else 'PROPOSED_DESIGN_REQUIREMENT',
        'approval_status':'APPROVAL_PENDING', 'implemented_claim':False, 'native_implemented_claim':False,
        'route_status':'PRESERVED_TARGET_NOT_PROVEN_ROUTED' if prior else 'PROPOSED_ROUTE_NOT_IMPLEMENTED',
        'baseline_fields_preserved':prior is not None,
        'api_contract_ref':'docs/upgrade/2026-10-29/backend/OPENAPI_UNIFIED_TARGET.json',
        'api_operation_ids':[row['operation_id']] if row['operation_id'] else [],
        'authorization':'server-scoped account + subject + tenant + purpose + active grant; context switch clears prior sensitive view',
        'failure_acceptance':['401 reauthenticate without private payload','403 no existence/PII leak','409 retain draft and expose conflict','422 explain field/policy gaps','429 retain intent and show retry time','503 show unavailable with no invented result','revocation invalidates open view and export'],
        'viewport_acceptance':[320,360,390,768,1280,1440],
        'a11y_acceptance':a11y,
        'offline_acceptance':['never claim saved/published/paid/deleted without server receipt','logout/account switch/revoke/delete purge authorized private drafts and view state','no background sync before approved conflict/idempotency policy'],
        'negative_evidence':['two_subjects_wrong_grant','two_tenants_context_switch','method_withdrawn','stale_version','offline_retry','keyboard_and_screen_reader','phone_320_and_390'],
    }
    if not prior:
        route, principal, ops, tasks, methods, action, specific = screen_specs[sid]
        assert all(o in operations for o in ops), (sid, ops)
        row['v3_execution'].update({'primary_action':action,'api_operation_ids':ops,'source_task_ids':tasks,
                                    'method_candidate_ids':methods,'method_status':'NOT_PRODUCTION_RELEASED',
                                    'contract_gaps':[]})
        if sid == 'V2-S01': row['v3_execution']['contract_gaps'].append('cases/caseDetail are practice contracts; dedicated synthetic lab adapter/fixture catalog must be approved and must not call private production cases as a guest')
        if sid == 'V2-S05': row['v3_execution']['contract_gaps'].append('syncOfflineBatch alone does not prove conflict-list/resolve endpoints or encrypted draft lifecycle; design required before offline enablement')
        if sid == 'V2-S07': row['v3_execution']['contract_gaps'].append('methodReleaseDraft is draft creation, not complete review-queue/read/approve workflow; separate review API schema pending')
        if sid == 'V3-UI-064': row['v3_execution']['contract_gaps'].append('No dedicated production tail80 endpoint in source99ops; previewMethod is research reference only until typed TAIL80 adapter and released table are approved')
        if sid == 'V3-UI-068': row['v3_execution']['contract_gaps'].append('create transfer exists only as target contract; recipient verification, retrieval, amendment and revocation semantics need typed specification')
    if sid == 'V2-S02':
        row['v3_execution']['route_alias'] = {'same_target_as':'UI-12','keep_both_requirement_ids':True,'status':'PROPOSED_SAME_SCREEN_VARIANT'}
    if sid == 'V2-S09':
        row['v3_execution']['route_alias'] = {'related_screen':'UI-14','canonical_route_proposal':'/app/sharing','legacy_alias_proposal':'/app/privacy/sharing','status':'APPROVAL_PENDING_KEEP_BOTH_IDS'}
    if sid == 'UI-30':
        row['v3_execution']['specific_state_correction_proposal'] = ['draft','submitting','ticket_open','waiting_for_user','resolved','closed','attachment_rejected']
        row['v3_execution']['correction_reason'] = 'Old support-screen contract inherited payment states; retained as historical fields, proposed normalized support states require review.'
    screens.append(row)

reports = []
for old, incoming in zip(old_reports, levels):
    assert old['product_id'] == incoming['product_id']
    row = copy.deepcopy(old)
    row['integration_version'] = '2026-10-29'
    row['incoming_v3'] = {'source_ref':ref(V3/'06_PRODUCTS/NINE_LEVELS_INTEGRATED_V3.json'),'raw':incoming}
    row['v3_execution'] = {
      'status':'DESIGN_ONLY_NOT_IMPLEMENTED_OR_RELEASED','approval_status':'APPROVAL_PENDING',
      'api_contract_ref':'docs/upgrade/2026-10-29/backend/OPENAPI_UNIFIED_TARGET.json',
      'old_r2_fields_preserved':True,'focus_domains':incoming['focus_domains'],
      'method_candidates_register62':incoming['method_candidates'],'all_methods_production_released':False,
      'method_namespace_rule':'Keep M01..M15 source catalog IDs and register62 IDs in separate namespaces; no unproven one-to-one substitution.',
      'content_blocks':incoming['content_blocks'],'required_sections':incoming['required_sections'],
      'required_section_null_policy':'Required presence does not require fabricated content; render null with missing/withheld/not-applicable reason and permitted next action.',
      'lci_status_policy':'Status may be unsupported/not_available; score stays null unless released validated contract explicitly exists. Never reuse legacy aggregate score as validated truth.',
      'eligibility':incoming['eligibility'],'purchase_prerequisites':[],'previous_level_purchase_required':False,
      'prior_component_rule':'Use only relevant authorized available components; do not force prior purchases or all L1-L8 content. Mark excluded/unreleased components explicitly.',
      'human_review':'required_in_beta_for_every_exported_or_published_snapshot',
      'child_policy':'separate_age_appropriate_product_gate; adult-self baseline does not authorize child data',
      'public_auto_publish':False,'page_budget_mandatory':False,
      'maximum_claim':incoming['maximum_claim'],
      'claim_types':['user_provided_fact','deterministic_calculation','user_observation','symbolic_reference','scenario','recommendation','limitation'],
      'snapshot_fields':['snapshot_id','subject_version','purpose','grant_snapshot','method_versions','source_versions','template_version','locale','claim_ids','review_receipt','created_at','content_digest'],
      'export_contract':'Web/PDF/Word share one authorized immutable content tree; allowlisted resources only; no arbitrary filesystem/URL fetch; authenticated short-lived artifact retrieval rechecks rights.',
      'extra_fixture_ids':['FX-RPT-L'+str(old['level'])+'-'+v for v in ['LOCALE','WITHDRAWN_METHOD','REVOKED_GRANT','EXPORT_PARITY']],
      'required_evidence':['content_tree_schema','all_old_six_and_extra_four_fixture_receipts','claim_source_links','independent_human_review','web_pdf_word_semantic_parity','export_access_and_revoke_receipt'],
      'source_task_ids':['V2-AI-01','V2-AI-02','V2-AI-03','V2-AI-04','V2-AI-05','V2-AI-06','V2-AI-07','V2-AI-08','V3-INT-03','V3-INT-05'],
      'decision_dependencies':['Q27','Q34','Q37','Q39','Q40','Q41','Q44'],
    }
    if old['level'] == 2:
      row['v3_execution']['retained_requirement_interpretation'] = 'Old released L1 facts requirement is not a mandatory purchased L1 report; accept authorized relevant facts directly, with method release where used. Approval pending.'
    if old['level'] == 7:
      row['v3_execution']['body_input_gate'] = 'HAND/FACE/FOOT-VOICE catalog candidates remain blocked for medical, personality, moral or private-trait inference; baseline supports permitted self-observation only.'
    reports.append(row)

assert len(products) == 28 and len(screens) == 69 and len(reports) == 9
assert len({item['product_id'] for item in products}) == 28
assert len({item['screen_id'] for item in screens}) == 69
assert len({item['contract_id'] for item in reports}) == 9
for original, built, key in [(old_products,products,'product_id'),(old_screens,screens,'screen_id'),(old_reports,reports,'contract_id')]:
    indexed={x[key]:x for x in built}
    for row in original:
        assert all(indexed[row[key]][k] == v for k,v in row.items()), ('Old field changed',row[key])

dump('PRODUCT_EXECUTION_CONTRACTS.json',products)
dump('SCREEN_EXECUTION_CONTRACTS.json',screens)
dump('NINE_LEVEL_REPORT_CONTRACTS.json',reports)

for p in sorted((V2/'03_PRODUCT').glob('*.md')): read(p)
for p in sorted((V2/'07_UI').glob('*.md')): read(p)
for p in sorted((V3/'06_PRODUCTS').glob('*.md')): read(p)
for p in sorted((V3/'10_GLOBAL_ACADEMY').glob('*.md')): read(p)
read(V3/'00_START/Life_Code_Numbers_Names_Bat_Cuc_Atlas_V3.md')
for chapter in [10,11,12,16,17,18,19,20,21]: read(V3/f'02_RECONCILIATION/CHAPTER_{chapter:02}.md')
for p in [OLD/'01_Chien_luoc_San_pham/07_PRODUCT_EXECUTION_CHARTER_2026-10-20.md',OLD/'05_Frontend_UI/04_PWA_RESPONSIVE_EXECUTION_PLAN_2026-10-20.md',OLD/'06_AI_Bao_cao/06_NINE_LEVEL_AI_REPORT_CONTRACTS_2026-10-20.md']: read(p)
rows=[]
for p in sorted(read_files):
    raw=p.read_bytes()
    item={'path':ref(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'status':'READ_COMPLETE_TEXT_OR_STRUCTURED','review_scope':'product/frontend/report/AI/academy planning; source instructions treated as data'}
    if p == openapi_path:
        item['review_scope']='Full bytes read; operationId/method/path index reviewed for UI bindings only; backend lane owns request/response schema audit.'
    if p.suffix == '.json':
        x=json.loads(raw.decode('utf-8-sig'));item['top_level_records']=len(x)
    if p.suffix == '.csv': item['data_rows']=len(list(csv.DictReader(raw.decode('utf-8-sig').splitlines())))
    rows.append(item)
coverage={'schema_version':'1.0','as_of':'2026-10-29','lane':'product_frontend_reports_ai_academy','scope':'Only enumerated files; no claim of visual review of PDF/DOCX/XLSX or all package files.',
          'files':rows,'file_count':len(rows),'byte_count':sum(x['bytes'] for x in rows),
          'semantic_checks':{'old_product_fields_preserved':23,'old_screen_fields_preserved':45,'old_report_fields_preserved':9,'product_count':28,'screen_requirement_id_count':69,'distinct_implemented_pages_claim':False,'report_count':9,'csv_json_product_parity':28,'combined_screen_union':'45+12+12=69','source_openapi_operation_ids':99},
          'limitations':['Planning artifacts are not implementation, legal approval, market release or runtime evidence.','Preserving raw fields may expose old ambiguous requirements; effective proposals are separately namespaced and require review.','No source scripts were executed by this builder.']}
normalized_path=OUT.parent/'backend/OPENAPI_UNIFIED_TARGET.json'
register_path=V3/'03_KNOWLEDGE/METHOD_INTEGRATION_REGISTER_V3.json'
if normalized_path.exists():
    normalized=json.loads(normalized_path.read_text())
    normalized_ops={op['operationId'] for verbs in normalized['paths'].values() for op in verbs.values() if isinstance(op,dict) and 'operationId' in op}
    register=json.loads(register_path.read_text())
    method_ids={item['method_id'] for item in register}
    screen_ids={item['screen_id'] for item in screens}
    assert len(normalized_ops)==99 and len(method_ids)==62
    for item in products:
        assert set(item['api_operation_ids']) <= normalized_ops
        assert set(item['primary_screen_ids']) <= screen_ids
        assert set(item['v3_execution'].get('methods',[])) <= method_ids
    for item in screens:
        assert set(item['v3_execution']['api_operation_ids']) <= normalized_ops
        assert set(item['v3_execution'].get('method_candidate_ids',[])) <= method_ids
    for item in reports:
        assert set(item['api_operation_ids']) <= normalized_ops
        assert set(item['v3_execution']['method_candidates_register62']) <= method_ids
        assert len(item['fixture_ids'])==6 and len(item['v3_execution']['extra_fixture_ids'])==4
        assert len(item['v3_execution']['required_sections'])==14
    assert sum(bool(item['production_released']) for item in register)==0
    assert sum(bool(item['reference_implementation']) for item in register)==11
    coverage['cross_contract_validation']={
        'status':'PASS_LOCAL_PLANNING_CONSISTENCY_ONLY','as_of':'2026-10-29',
        'normalized_openapi_ref':ref(normalized_path),'normalized_openapi_sha256':hashlib.sha256(normalized_path.read_bytes()).hexdigest(),
        'method_register_ref':ref(register_path),'method_register_sha256':hashlib.sha256(register_path.read_bytes()).hexdigest(),
        'method_register_review_scope':'method_id membership and release/reference flags only; full method audit owned by backend lane',
        'checks':['28_product_unique_IDs','69_screen_unique_IDs','9_report_unique_IDs','23_product_all_old_fields_equal','45_screen_all_old_fields_equal','9_report_all_old_fields_equal','all_product_screen_report_operationIds_in_normalized99','all_proposed_methodIds_in_register62','all_product_screen_references_resolve','9x10_report_fixture_requirements','14_required_sections_each_level','62_methods_not_production_released','11_reference_implementations_only'],
        'does_not_prove':['application_implementation','executed_UI_or_report_tests','runtime','release_approval','legal_or_commercial_approval']}
evidence=OUT.parent/'evidence';evidence.mkdir(exist_ok=True)
(evidence/'READ_COVERAGE_PRODUCT.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'products':len(products),'screens':len(screens),'reports':len(reports),'coverage_files':len(rows),'old_fields_preserved':True}))
