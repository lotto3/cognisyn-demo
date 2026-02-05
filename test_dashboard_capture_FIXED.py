#!/usr/bin/env python3
"""
Dashboard capture test — proven orchestration calls from Session 5 tests,
wrapped with session + checkpoint file writing for dashboard verification.
Zero tokens.

FIXED: Each agent now uses its own property (HOST-QUALITY/OPTICAL/COHERENCE)
instead of hardcoding HOST-QUALITY for all agents.
Matches scenarios/quantum_rps.py AGENT_PROPERTIES mapping.
"""
import asyncio
import json
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, '/mnt/cognisyn/COGNISYN_DGX')

from framework.orchestration_engine import OrchestrationBridge, BabaIsQuantumRule
from framework.strategic_mathematics_complete import UnifiedStrategicMathematics
from memory.dynamic_memory_architecture import DynamicMemoryArchitecture
from validation.rule_validation import OrchestrationValidator
from materials_project_adapter_CORRECT import MaterialsProjectAdapter

BASE = Path('/mnt/cognisyn/COGNISYN_DGX')
TODAY = datetime.now().strftime("%m%d")

# Each agent evaluates from its own property perspective (matches scenarios/quantum_rps.py)
AGENT_PROPERTIES = {
    'B1': 'HOST-QUALITY',
    'B2': 'OPTICAL',
    'B3': 'COHERENCE',
}

# COUPLE connects two DIFFERENT properties (matches scenarios/quantum_rps.py COUPLE_TARGETS)
COUPLE_TARGETS = {
    'B1': 'OPTICAL',
    'B2': 'COHERENCE',
    'B3': 'HOST-QUALITY',
}


def setup_bridge(agent_id):
    H = UnifiedStrategicMathematics()
    m = DynamicMemoryArchitecture(agent_id=agent_id)
    v = OrchestrationValidator()
    b = OrchestrationBridge(H, m, v)
    b.materials_adapter = MaterialsProjectAdapter(use_cached=True)
    return b


async def run_examples(agent_id):
    """Exact orchestration calls from proven tests."""
    b = setup_bridge(agent_id)
    ctx = {'day': 6, 'agent_id': agent_id}
    prop = AGENT_PROPERTIES[agent_id]
    cross = COUPLE_TARGETS[agent_id]
    results = []

    # EXAMPLE 1: SUPERPOSE — from Examples 1-3 test
    print(f"  Ex1 SUPERPOSE...", end=" ")
    rule = BabaIsQuantumRule(subject="COMPOUNDS", verb="SUPERPOSE", property=prop, category="strategy")
    r = await b.orchestrate_mathematics(rule, dict(ctx), {'day': 6})
    s = r.mathematical_state
    print(f"type={s.get('type')}")
    results.append({
        'num': 1, 'title': 'Cooperative Parallel Evaluation',
        'ops': [{'subject': 'COMPOUNDS', 'verb': 'SUPERPOSE', 'property': prop}],
        'state': s, 'desc': r.mathematical_state_description
    })

    # EXAMPLE 2: COUPLE — from Examples 1-3 test
    print(f"  Ex2 COUPLE...", end=" ")
    rule = BabaIsQuantumRule(subject=prop, verb="COUPLE", property=cross, category="strategy")
    r = await b.orchestrate_mathematics(rule, dict(ctx), {'day': 6})
    s = r.mathematical_state
    print(f"type={s.get('type')}, coupling_strength={s.get('coupling_strength', 'MISSING')}")
    results.append({
        'num': 2, 'title': 'Scale Coupling Analysis',
        'ops': [{'subject': prop, 'verb': 'COUPLE', 'property': cross}],
        'state': s, 'desc': r.mathematical_state_description
    })

    # EXAMPLE 3: FILTER -> ENTANGLE — from Examples 1-3 test + pipeline test
    print(f"  Ex3 FILTER->ENTANGLE...", end=" ")
    rule3a = BabaIsQuantumRule(subject="COMPOUNDS", verb="FILTER", property="I=0", category="strategy")
    r3a = await b.orchestrate_mathematics(rule3a, dict(ctx), {'day': 6})
    compounds = r3a.mathematical_state.get('compounds', [])
    print(f"FILTER:{len(compounds)}", end=" -> ")

    ctx3 = dict(ctx)
    ctx3['compounds'] = compounds
    rule3b = BabaIsQuantumRule(subject=prop, verb="ENTANGLE", property="CARE-SYNERGY", category="strategy")
    r3b = await b.orchestrate_mathematics(rule3b, ctx3, {'day': 6})
    s3 = r3b.mathematical_state
    print(f"synergy={s3.get('synergy_count')}, measure={s3.get('entanglement_measure', 0):.4f}")

    filter_desc = r3a.mathematical_state_description or ''
    entangle_desc = r3b.mathematical_state_description or ''
    results.append({
        'num': 3, 'title': 'Nuclear Spin Bath Analysis',
        'ops': [
            {'subject': 'COMPOUNDS', 'verb': 'FILTER', 'property': 'I=0'},
            {'subject': prop, 'verb': 'ENTANGLE', 'property': 'CARE-SYNERGY'}
        ],
        'state': s3, 'desc': filter_desc + '\n\n' + entangle_desc
    })

    # EXAMPLE 4: INTERFERE — from Example 4 INTERFERE test
    print(f"  Ex4 INTERFERE...", end=" ")
    rule = BabaIsQuantumRule(subject="COMPOUNDS", verb="INTERFERE", property="CARE-GUIDED", category="strategy")
    r = await b.orchestrate_mathematics(rule, dict(ctx), {'day': 6})
    s = r.mathematical_state
    pruned = s.get('pruned_compounds', [])
    print(f"type={s.get('type')}, {s.get('n_original','?')}->{len(pruned)} compounds, care_eq={s.get('care_equilibria_preserved','?')}")
    results.append({
        'num': 4, 'title': 'Interference Pruning',
        'ops': [{'subject': 'COMPOUNDS', 'verb': 'INTERFERE', 'property': 'CARE-GUIDED'}],
        'state': s, 'desc': r.mathematical_state_description
    })

    # EXAMPLE 5: FILTER -> COUPLE -> ENTANGLE — from Example 5 pipeline test
    print(f"  Ex5 FILTER->COUPLE->ENTANGLE...", end=" ")
    r5a = await b.orchestrate_mathematics(
        BabaIsQuantumRule(subject="COMPOUNDS", verb="FILTER", property="I=0", category="strategy"),
        dict(ctx), {'day': 6})
    compounds5 = r5a.mathematical_state.get('compounds', [])

    ctx5 = dict(ctx)
    ctx5['compounds'] = compounds5
    r5b = await b.orchestrate_mathematics(
        BabaIsQuantumRule(subject=prop, verb="COUPLE", property="CROSS-SCALE", category="strategy"),
        ctx5, {'day': 6})

    ctx5c = dict(ctx)
    ctx5c['compounds'] = compounds5
    r5c = await b.orchestrate_mathematics(
        BabaIsQuantumRule(subject=prop, verb="ENTANGLE", property="CARE-SYNERGY", category="strategy"),
        ctx5c, {'day': 6})
    s5 = r5c.mathematical_state
    print(f"synergy={s5.get('synergy_count')}")

    descs = [d for d in [r5a.mathematical_state_description, r5b.mathematical_state_description, r5c.mathematical_state_description] if d]
    results.append({
        'num': 5, 'title': 'Pipeline Execution',
        'ops': [
            {'subject': 'COMPOUNDS', 'verb': 'FILTER', 'property': 'I=0'},
            {'subject': prop, 'verb': 'COUPLE', 'property': 'CROSS-SCALE'},
            {'subject': prop, 'verb': 'ENTANGLE', 'property': 'CARE-SYNERGY'}
        ],
        'state': s5, 'desc': '\n\n'.join(descs)
    })

    return results


def write_session_file(agent_id, examples):
    """Same structure as ConversationalLLMAPI.save_conversation()"""
    session_dir = BASE / 'Dailies' / TODAY / 'sessions' / agent_id
    session_dir.mkdir(parents=True, exist_ok=True)

    session_id = f"{agent_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    messages = []

    for ex in examples:
        messages.append({
            'role': 'user',
            'content': f"## Example {ex['num']}: {ex['title']}\n\n[Operational sequence]"
        })
        messages.append({
            'role': 'assistant',
            'content': json.dumps({
                'response': f"We observe that H_total returned {ex['state'].get('type', 'results')} "
                           f"for {len(ex['ops'])} operation(s) on Yb-171 compounds.",
                'operations': ex['ops']
            })
        })
        if ex['desc']:
            messages.append({
                'role': 'system',
                'content': f"[MATHEMATICAL STATE]\n{ex['desc']}"
            })

    session_data = {
        'session_id': session_id,
        'agent_id': agent_id,
        'session_start': datetime.now().isoformat(),
        'messages': messages,
        'total_tokens': len(messages) * 500
    }

    path = session_dir / f"{session_id}.json"
    with open(path, 'w') as f:
        json.dump(session_data, f, indent=2, default=str)
    print(f"  {path}")


def write_checkpoint_files(agent_id, examples):
    """Same structure as DynamicMemoryArchitecture.save_checkpoint()"""
    cp_dir = BASE / 'data' / 'checkpoints'
    cp_dir.mkdir(parents=True, exist_ok=True)

    cumulative_strategies = []
    cumulative_rules = []

    for ex in examples:
        for op in ex['ops']:
            cumulative_strategies.append({
                'pattern': f"{op['verb']}_discovery",
                'description': f"[{op['subject']}] [{op['verb']}] [{op['property']}] evaluated Yb-171 compounds",
                'success_score': 0.85
            })
            cumulative_rules.append(f"[{op['subject']}] [{op['verb']}] [{op['property']}]")

        cp = {
            'episodic': {'episodes': [{'example': ex['num'], 'operation': ex['ops'][0]['verb'], 'success': True}]},
            'strategic': {'strategies': list(cumulative_strategies), 'pattern_count': len(cumulative_strategies)},
            'creative_composition': {'rules_invented': list(cumulative_rules), 'novel_rules_created': [], 'creative_breakthroughs': []},
            'learning_from_struggle': {'mistakes_made': []}
        }
        path = cp_dir / f"day_6_agent_{agent_id}_example_{ex['num']}.json"
        with open(path, 'w') as f:
            json.dump(cp, f, indent=2, default=str)
        print(f"  {path}")

    eod = {
        'episodic': {'episodes': [{'example': i+1, 'success': True} for i in range(5)]},
        'strategic': {'strategies': cumulative_strategies, 'pattern_count': len(cumulative_strategies)},
        'creative_composition': {'rules_invented': cumulative_rules, 'novel_rules_created': [], 'creative_breakthroughs': []},
        'learning_from_struggle': {'mistakes_made': []}
    }
    path = cp_dir / f"day_6_agent_{agent_id}.json"
    with open(path, 'w') as f:
        json.dump(eod, f, indent=2, default=str)
    print(f"  {path}")


async def main():
    print("=" * 60)
    print("DASHBOARD CAPTURE TEST")
    print("Proven orchestration calls + file writing for dashboard")
    print("Zero tokens — cached compounds only")
    print("=" * 60)

    for agent_id in ['B1', 'B2', 'B3']:
        print(f"\n--- {agent_id} ({AGENT_PROPERTIES[agent_id]}) ---")
        examples = await run_examples(agent_id)

        print(f"\n  Writing session file...")
        write_session_file(agent_id, examples)

        print(f"  Writing checkpoint files...")
        write_checkpoint_files(agent_id, examples)

    print("\n" + "=" * 60)
    print("DONE — all files written")
    print("=" * 60)
    print(f"\nLaunch dashboard:")
    print(f"  streamlit run dashboard_monitor.py --server.port 8502")
    print(f"  Date: {TODAY}  |  Day: 6")
    print(f"\nCleanup after:")
    print(f"  rm -rf {BASE}/Dailies/{TODAY}")
    print(f"  rm {BASE}/data/checkpoints/day_6_agent_*_example_*.json")
    print(f"  rm {BASE}/data/checkpoints/day_6_agent_B?.json")
    print("=" * 60)

asyncio.run(main())
