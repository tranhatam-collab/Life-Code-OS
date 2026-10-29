#!/usr/bin/env python3
"""Independent count/link checks of the canonical handoff; no application access."""
import json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'docs/upgrade/2026-10-29'
OUT=BASE/'backend'
def read(path): return json.loads(path.read_text())
def write(name,value): (OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def main():
    backlog=read(BASE/'execution/BACKLOG_UNIFIED.json')
    contracts=read(BASE/'execution/TASK_DEV_CONTRACTS.json')
    graph=read(BASE/'execution/TASK_DEPENDENCY_GRAPH.json')
    trace=read(BASE/'execution/REQUIREMENT_TRACE_UNIFIED.json')
    work=read(BASE/'execution/INTEGRATION_WORK_ORDERS.json')
    ids={r['task_id'] for r in backlog}
    by_id={r['task_id']:r for r in work}
    mapping={
        'BE-WP01':['INT29-010'], 'BE-WP02':['INT29-005'], 'BE-WP03':['INT29-011'],
        'BE-WP04':['INT29-012','INT29-017'], 'BE-WP05':['INT29-006','INT29-012','INT29-013'],
        'BE-WP06':['INT29-006','INT29-007','INT29-008'], 'BE-WP07':['INT29-008'],
        'BE-WP08':['INT29-009'], 'BE-WP09':['INT29-010','INT29-012'],
        'BE-WP10':['INT29-014','INT29-016'], 'BE-WP11':['INT29-005'],
        'BE-WP12':['INT29-015','INT29-018','INT29-020']}
    rows=[]
    for wp,tasks in mapping.items():
        assert set(tasks)<=ids
        rows.append({'work_package_id':wp,'canonical_integration_task_ids':tasks,
            'retained_source_task_ids':sorted({t for task in tasks for t in by_id[task]['source_task_ids']}),
            'estimate_rollup':'REFINEMENT_NOT_AUTOMATICALLY_ADDITIVE_TO_SOURCE_OR_INTEGRATION_ESTIMATES',
            'execution_authorization':'Planning decomposition only; no application/provider/production authority.',
            'detail':'docs/upgrade/2026-10-29/backend/BACKEND_DEV_HANDOFF.md#7-gói-công-việc-dev-phụ-thuộc-và-nghiệm-thu'})
    write('WORK_PACKAGE_BACKLOG_CROSSWALK.json',{'date':'2026-10-29','work_package_count':len(rows),'canonical_backlog_count':len(backlog),'rows':rows})
    topo=graph['topological_order']
    index={n:i for i,n in enumerate(topo)}
    missing_edges=[{'task':n['task_id'],'dependency':d} for n in graph['nodes'] for d in n['task_dependencies'] if d not in ids]
    bad_order=[{'task':n['task_id'],'dependency':d} for n in graph['nodes'] for d in n['task_dependencies'] if d in index and index[d]>=index[n['task_id']]]
    unknown_trace=[{'trace_id':r['trace_id'],'task_id':t} for r in trace for t in r.get('task_ids',[]) if t not in ids]
    checks={
        'backlog316_unique':len(backlog)==len(ids)==316,
        'dev_contracts316_same_ids':len(contracts)==len({r['task_id'] for r in contracts})==316 and {r['task_id'] for r in contracts}==ids,
        'dependency_nodes316_same_ids':len(graph['nodes'])==316 and {r['task_id'] for r in graph['nodes']}==ids,
        'topological_order316_same_ids':len(topo)==len(set(topo))==316 and set(topo)==ids,
        'dependency_missing_and_cycle_free':not missing_edges and not bad_order and not graph['missing_task_edges'] and not graph['cycles'],
        'trace407_unique':len(trace)==len({r['trace_id'] for r in trace})==407,
        'trace_task_ids_resolve':not unknown_trace,
        'integration_work_orders20_present':len(work)==20 and set(by_id)<=ids,
        'method_execution_matrix62':read(OUT/'FORMULA_METHOD_EXECUTION_MATRIX.json')['method_count']==62,
        'api99_and68schemas':read(OUT/'API_CONTRACT_RECONCILIATION.json')['operation_count']==99 and read(OUT/'API_CONTRACT_RECONCILIATION.json')['component_schema_count']==68,
        'codegen_remains_blocked':read(OUT/'OPENAPI_UNIFIED_TARGET.json')['x-lc-codegen-ready'] is False,
        'canonical9_exact_and_new27_exact':all(r['exact_object_match'] for r in read(OUT/'CONTRACT_VALIDATION_RECEIPT.json')['local_canonical_schemas']) and all(r['preserved_exact_object'] for r in read(OUT/'CONTRACT_VALIDATION_RECEIPT.json')['standalone_preservation_and_examples'])}
    report={'date':'2026-10-29','scope':'Independent structural checks of canonical planning artifacts; implementation and release not checked',
        'checks':checks,'all_checks_pass':all(checks.values()),'backlog_origin_counts':dict(Counter(r.get('origin','unknown') for r in backlog)),
        'trace_origin_counts':dict(Counter(r.get('origin','unknown') for r in trace)),
        'missing_dependency_edges':missing_edges,'invalid_topological_edges':bad_order,'unknown_trace_tasks':unknown_trace,
        'production_ready':False,'limitations':['Acyclic dependency links do not mean tasks are complete or their decisions approved.','Backend WP estimates overlap canonical tasks and must not be summed as an additional budget.','No CI/deployment/runtime/provider/live validation performed.']}
    write('CANONICAL_QA_BACKEND.json',report)
    assert all(checks.values()),report
    print(json.dumps({'checks':checks,'backlog_origin_counts':report['backlog_origin_counts'],'trace_origin_counts':report['trace_origin_counts']},ensure_ascii=False))

if __name__=='__main__':main()
