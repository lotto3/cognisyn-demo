#!/usr/bin/env python3
"""
COGNISYN UI/UX Slides — for CodeLaunch "Mockups/Wireframes" upload.
Run locally: streamlit run mockup_slides.py
Screenshot each slide → paste into Google Slides → export as PDF.
Formatted for 16:9 aspect ratio — one screenshot per Google Slide.
"""
import streamlit as st

st.set_page_config(page_title="COGNISYN UI/UX", page_icon="🔬", layout="wide")

st.markdown("""
<style>
.main {background-color: #0e1117;}
h1, h2, h3 {color: #00ffff;}
p, li, .stMarkdown {font-size: 18px !important; line-height: 1.6;}
</style>
""", unsafe_allow_html=True)

# Slide selector
slide = st.sidebar.radio("Slide", [
    "1. Orchestration Monitor — Overview",
    "2. Orchestration Monitor — Agent Detail",
    "3. Pipeline Test Code — Setup & SUPERPOSE",
    "4. Pipeline Test Code — Pipeline & Results",
    "5. System Overview",
    "6. Three-Agent Architecture",
    "7. Baba is Quantum Grammar",
    "8. Pipeline Progression",
    "9. Pipeline Output — SUPERPOSE & ENTANGLE",
    "10. Pipeline Output — INTERFERE & Care vs Nash",
    "11. Care vs Nash Equilibria",
    "12. Agent Learning System",
])

if slide.startswith("1."):
    # ---- SLIDE 1: ORCHESTRATION MONITOR — OVERVIEW ----
    st.markdown("""
    <div style="padding: 20px 40px 10px;">
        <h2 style="font-size: 36px; color: #00ffff; text-align: center; margin-bottom: 8px;">
            Orchestration Monitor
        </h2>
        <p style="text-align: center; font-size: 18px; color: #aaa; margin-bottom: 20px;">
            Three agents running 1,073 Yb compounds through the discovery pipeline in parallel.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.image("dashboard_overview.png", caption="System overview: 5/5 examples complete, 3/3 agents, 1,073 compounds evaluated, 24 strategic patterns learned")

    col1, col2 = st.columns(2)
    with col1:
        st.image("dashboard_b1_examples.png", caption="B1 (Host Quality): All 5 examples — SUPERPOSE to full 3-stage pipeline")
    with col2:
        st.image("dashboard_b1_b2.png", caption="B1 completes, B2 (Optical) begins — same grammar, different perspective")

    st.markdown("""
    <div style="text-align: center; padding: 12px; background-color: #1e2130; border-radius: 8px; margin-top: 10px;">
        <span style="font-size: 14px; color: #888;">
            Illustrative examples from orchestration pipeline test. Scores computed by H_total from real crystal structure data.
        </span>
    </div>
    """, unsafe_allow_html=True)

elif slide.startswith("2."):
    # ---- SLIDE 2: ORCHESTRATION MONITOR — AGENT DETAIL ----
    st.markdown("""
    <div style="padding: 20px 40px 10px;">
        <h2 style="font-size: 36px; color: #00ffff; text-align: center; margin-bottom: 8px;">
            Orchestration Monitor — Agent Detail
        </h2>
        <p style="text-align: center; font-size: 18px; color: #aaa; margin-bottom: 20px;">
            Each agent evaluates from its own property perspective. When all three score above threshold simultaneously, that's a Care equilibrium.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.image("dashboard_b2_b3.png", caption="B2 complete, B3 (Coherence) begins — each agent evaluates from its own property perspective")
    with col2:
        st.image("dashboard_b3_coherence.png", caption="B3 complete — where all three score above threshold, that's a Care equilibrium")

    st.markdown("""
    <div style="text-align: center; padding: 16px; background-color: #1e2130; border-radius: 8px; margin-top: 16px;">
        <span style="font-size: 16px; color: #00d4aa; font-weight: bold;">
            cognisyn-demo.streamlit.app
        </span>
        <span style="font-size: 14px; color: #888;">
             · 55,000 lines of code · tish@cognisyn.ai
        </span>
        <div style="font-size: 13px; color: #666; margin-top: 8px;">
            Illustrative examples from orchestration pipeline test. Scores computed by H_total from real crystal structure data.
        </div>
    </div>
    """, unsafe_allow_html=True)

elif slide.startswith("3."):
    # ---- SLIDE 3: PIPELINE TEST CODE — SETUP & SUPERPOSE ----
    st.markdown("""
    <div style="padding: 20px 40px 10px;">
        <h2 style="font-size: 36px; color: #00ffff; text-align: center; margin-bottom: 8px;">
            Pipeline Test Code
        </h2>
        <p style="text-align: center; font-size: 16px; color: #aaa; margin-bottom: 16px;">
            Real orchestration calls — zero LLM tokens (orchestration test), real H_total computation.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.code('''# Setup: real mathematics, real memory, real validation
H = UnifiedStrategicMathematics()        # H_total: Hermitian Hamiltonian, 8 components
m = DynamicMemoryArchitecture(agent_id)  # Episodic + strategic memory
v = OrchestrationValidator()             # Rule validation
b = OrchestrationBridge(H, m, v)         # Orchestration engine
b.materials_adapter = MaterialsProjectAdapter(use_cached=True)  # 1,073 Yb compounds

# EXAMPLE 1: SUPERPOSE — evaluate all compounds for host quality
rule = BabaIsQuantumRule(
    subject="COMPOUNDS", verb="SUPERPOSE",
    property="HOST-QUALITY", category="strategy"
)
result = await b.orchestrate_mathematics(rule, ctx, {'day': 6})
# → 1,073 compounds evaluated, 26 Care equilibria found''', language='python')

    st.markdown("""
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin: 16px 40px 0;">
        <div style="background-color: #1e2130; padding: 16px; border-radius: 8px; text-align: center;">
            <div style="font-size: 14px; color: #888;">Codebase</div>
            <div style="font-size: 22px; color: #00d4aa; font-weight: bold;">55,000 lines</div>
        </div>
        <div style="background-color: #1e2130; padding: 16px; border-radius: 8px; text-align: center;">
            <div style="font-size: 14px; color: #888;">LLM Tokens Used</div>
            <div style="font-size: 22px; color: #ffd43b; font-weight: bold;">Zero</div>
            <div style="font-size: 12px; color: #666;">Orchestration test, real math</div>
        </div>
        <div style="background-color: #1e2130; padding: 16px; border-radius: 8px; text-align: center;">
            <div style="font-size: 14px; color: #888;">Data Source</div>
            <div style="font-size: 22px; color: #4dabf7; font-weight: bold;">Materials Project</div>
            <div style="font-size: 12px; color: #666;">CC BY 4.0</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif slide.startswith("4."):
    # ---- SLIDE 4: PIPELINE TEST CODE — PIPELINE & RESULTS ----
    st.markdown("""
    <div style="padding: 20px 40px 10px;">
        <h2 style="font-size: 36px; color: #00ffff; text-align: center; margin-bottom: 8px;">
            Pipeline Test Code — Multi-Stage Operations
        </h2>
    </div>
    """, unsafe_allow_html=True)

    st.code('''# EXAMPLE 3: FILTER → ENTANGLE — two-stage pipeline
rule_filter = BabaIsQuantumRule(
    subject="COMPOUNDS", verb="FILTER",
    property="I=0", category="strategy"       # Zero nuclear spin only
)
r_filter = await b.orchestrate_mathematics(rule_filter, ctx, {'day': 6})
# → 1,073 → 1,057 passed (i_zero > 0.3)

rule_entangle = BabaIsQuantumRule(
    subject="HOST-QUALITY", verb="ENTANGLE",
    property="CARE-SYNERGY", category="strategy"  # Multi-agent synergy
)
r_entangle = await b.orchestrate_mathematics(rule_entangle, ctx, {'day': 6})
# → 26 synergy compounds: YbCl₃ (B1=0.90, B2=0.94, B3=0.90)

# EXAMPLE 4: INTERFERE — quantum pruning
rule = BabaIsQuantumRule(
    subject="COMPOUNDS", verb="INTERFERE",
    property="CARE-GUIDED", category="strategy"
)
result = await b.orchestrate_mathematics(rule, ctx, {'day': 6})
# → 1,073 → 25 compounds, all Care equilibria preserved''', language='python')

    st.markdown("""
    <div style="text-align: center; padding: 16px; background-color: #1e2130; border-radius: 8px; margin: 16px 40px 0;">
        <span style="font-size: 16px; color: #888;">
            The LLM operates the mathematics — it doesn't generate the answers.<br/>
            Baba rules trigger computation, not generation.
        </span>
    </div>
    """, unsafe_allow_html=True)

elif slide.startswith("5."):
    # ---- SLIDE 5: SYSTEM OVERVIEW ----
    st.markdown("""
    <div style="text-align: center; padding: 60px 40px;">
        <h1 style="font-size: 48px; color: #00ffff; margin-bottom: 20px;">🔬 COGNISYN</h1>
        <h2 style="font-size: 32px; color: #e0e0e0; font-weight: normal; margin-bottom: 40px;">
            Yb-171 Host Materials Discovery
        </h2>
        <div style="font-size: 22px; color: #00d4aa; margin-bottom: 40px;">
            Turning LLMs into mathematical physics operators<br/>
            using quantum-inspired game theory
        </div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; max-width: 900px; margin: 0 auto;">
            <div style="background-color: #1e2130; padding: 24px; border-radius: 10px; text-align: center;">
                <div style="font-size: 36px; color: #00d4aa; font-weight: bold;">1,073</div>
                <div style="font-size: 14px; color: #888;">Compounds</div>
            </div>
            <div style="background-color: #1e2130; padding: 24px; border-radius: 10px; text-align: center;">
                <div style="font-size: 36px; color: #4dabf7; font-weight: bold;">3</div>
                <div style="font-size: 14px; color: #888;">AI Agents</div>
            </div>
            <div style="background-color: #1e2130; padding: 24px; border-radius: 10px; text-align: center;">
                <div style="font-size: 36px; color: #da77f2; font-weight: bold;">3</div>
                <div style="font-size: 14px; color: #888;">Properties</div>
            </div>
            <div style="background-color: #1e2130; padding: 24px; border-radius: 10px; text-align: center;">
                <div style="font-size: 36px; color: #ffd43b; font-weight: bold;">26</div>
                <div style="font-size: 14px; color: #888;">Care Equilibria</div>
            </div>
        </div>
        <div style="margin-top: 40px; font-size: 16px; color: #666;">
            Live app: cognisyn-demo.streamlit.app · Data: Materials Project (CC BY 4.0)
        </div>
    </div>
    """, unsafe_allow_html=True)

elif slide.startswith("6."):
    # ---- SLIDE 6: THREE-AGENT ARCHITECTURE ----
    st.markdown("""
    <div style="padding: 40px;">
        <h2 style="font-size: 36px; color: #00ffff; text-align: center; margin-bottom: 30px;">
            Three-Agent Architecture
        </h2>
        <p style="text-align: center; font-size: 18px; color: #aaa; margin-bottom: 30px;">
            Each agent evaluates 1,073 Yb compounds from a different property perspective.<br/>
            When all three score above threshold simultaneously, that's a Care equilibrium.
        </p>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; max-width: 1000px; margin: 0 auto;">
            <div style="background-color: #1e2130; padding: 32px; border-radius: 12px; border-top: 6px solid #00d4aa;">
                <h3 style="color: #00d4aa; font-size: 26px; margin-bottom: 16px;">B1: Host Quality</h3>
                <ul style="font-size: 16px; color: #c0c0c0; line-height: 2;">
                    <li>Crystal stability</li>
                    <li>Site symmetry</li>
                    <li>Phonon properties</li>
                    <li>Optical linewidth</li>
                </ul>
            </div>
            <div style="background-color: #1e2130; padding: 32px; border-radius: 12px; border-top: 6px solid #4dabf7;">
                <h3 style="color: #4dabf7; font-size: 26px; margin-bottom: 16px;">B2: Optical</h3>
                <ul style="font-size: 16px; color: #c0c0c0; line-height: 2;">
                    <li>Band gap analysis</li>
                    <li>Transition rates</li>
                    <li>Photon emission</li>
                    <li>Quantum networking</li>
                </ul>
            </div>
            <div style="background-color: #1e2130; padding: 32px; border-radius: 12px; border-top: 6px solid #da77f2;">
                <h3 style="color: #da77f2; font-size: 26px; margin-bottom: 16px;">B3: Coherence</h3>
                <ul style="font-size: 16px; color: #c0c0c0; line-height: 2;">
                    <li>Nuclear spin bath (I=0)</li>
                    <li>T2 coherence times</li>
                    <li>Magnetic noise</li>
                    <li>Decoherence channels</li>
                </ul>
            </div>
        </div>
        <div style="text-align: center; margin-top: 30px; padding: 20px; background-color: #1e2130; border-radius: 8px; max-width: 700px; margin-left: auto; margin-right: auto;">
            <span style="font-size: 18px; color: #ffd43b; font-weight: bold;">
                H<sub>total</sub> = H<sub>quantum</sub> + H<sub>classical</sub> + H<sub>coupling</sub> + H<sub>care</sub>
            </span><br/>
            <span style="font-size: 15px; color: #888;">
                Care operator C<sub>λ</sub> reweights the energy landscape — cooperation becomes the ground state
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif slide.startswith("7."):
    # ---- SLIDE 7: BABA IS QUANTUM GRAMMAR ----
    st.markdown("""
    <div style="padding: 40px;">
        <h2 style="font-size: 36px; color: #00ffff; text-align: center; margin-bottom: 30px;">
            Baba is Quantum: Compositional Grammar
        </h2>
        <p style="text-align: center; font-size: 18px; color: #aaa; margin-bottom: 30px;">
            Rules ARE mathematical operators. Each accesses H_total — a Hermitian Hamiltonian with 8 components, computed classically.
        </p>
        <div style="background-color: #0e1117; padding: 32px; border-radius: 12px; border: 2px solid #333; max-width: 800px; margin: 0 auto; font-family: monospace;">
            <div style="color: #888; font-size: 16px; margin-bottom: 16px;"># Grammar: [SUBJECT] [VERB] [PROPERTY]</div>
            <div style="font-size: 20px; color: #e0e0e0; line-height: 2.2;">
                <span style="color: #00d4aa;">COMPOUNDS</span>  <span style="color: #ffd43b;">SUPERPOSE</span>   <span style="color: #4dabf7;">HOST-QUALITY</span>     <span style="color: #666;"># Parallel evaluation</span><br/>
                <span style="color: #00d4aa;">COMPOUNDS</span>  <span style="color: #ffd43b;">FILTER</span>      <span style="color: #4dabf7;">I=0</span>              <span style="color: #666;"># Zero-spin nuclei only</span><br/>
                <span style="color: #00d4aa;">HOST-QUALITY</span> <span style="color: #ffd43b;">COUPLE</span>    <span style="color: #4dabf7;">OPTICAL</span>          <span style="color: #666;"># Cross-scale coupling</span><br/>
                <span style="color: #00d4aa;">HOST-QUALITY</span> <span style="color: #ffd43b;">ENTANGLE</span>  <span style="color: #4dabf7;">CARE-SYNERGY</span>     <span style="color: #666;"># Multi-agent synergy</span><br/>
                <span style="color: #00d4aa;">COMPOUNDS</span>  <span style="color: #ffd43b;">INTERFERE</span>   <span style="color: #4dabf7;">CARE-GUIDED</span>      <span style="color: #666;"># Quantum pruning</span>
            </div>
        </div>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; max-width: 800px; margin: 30px auto 0;">
            <div style="background-color: #1e2130; padding: 20px; border-radius: 10px; text-align: center;">
                <div style="font-size: 14px; color: #888;">Operations</div>
                <div style="font-size: 28px; color: #ffd43b; font-weight: bold;">5</div>
                <div style="font-size: 13px; color: #666;">SUPERPOSE · COUPLE · FILTER · ENTANGLE · INTERFERE</div>
            </div>
            <div style="background-color: #1e2130; padding: 20px; border-radius: 10px; text-align: center;">
                <div style="font-size: 14px; color: #888;">Composition</div>
                <div style="font-size: 28px; color: #00d4aa; font-weight: bold;">Chainable</div>
                <div style="font-size: 13px; color: #666;">FILTER → COUPLE → ENTANGLE</div>
            </div>
            <div style="background-color: #1e2130; padding: 20px; border-radius: 10px; text-align: center;">
                <div style="font-size: 14px; color: #888;">Hallucination</div>
                <div style="font-size: 28px; color: #00d4aa; font-weight: bold;">Zero</div>
                <div style="font-size: 13px; color: #666;">Rules trigger computation, not generation</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif slide.startswith("8."):
    # ---- SLIDE 8: PIPELINE PROGRESSION ----
    st.markdown("""
    <div style="padding: 40px;">
        <h2 style="font-size: 36px; color: #00ffff; text-align: center; margin-bottom: 30px;">
            Pipeline Progression: 5 Examples
        </h2>
        <p style="text-align: center; font-size: 18px; color: #aaa; margin-bottom: 30px;">
            Each agent builds increasingly sophisticated operations across 5 examples.
        </p>
    </div>
    """, unsafe_allow_html=True)

    examples = [
        ("1", "SUPERPOSE", "Cooperative Parallel Evaluation", "Evaluate all 1,073 compounds", "#00d4aa"),
        ("2", "COUPLE", "Scale Coupling Analysis", "Cross-scale: host quality ↔ optical", "#4dabf7"),
        ("3", "FILTER → ENTANGLE", "Nuclear Spin Bath + Synergy", "Two-stage: I=0 filter then synergy detection", "#da77f2"),
        ("4", "INTERFERE", "Quantum Pruning", "1,073 → 25 compounds, zero Care equilibria lost", "#ffd43b"),
        ("5", "FILTER → COUPLE → ENTANGLE", "Full Pipeline", "Three-stage discovery workflow", "#ff6b6b"),
    ]

    for num, ops, title, desc, color in examples:
        st.markdown(f"""
        <div style="background-color: #1e2130; padding: 20px 28px; border-radius: 10px; border-left: 6px solid {color}; margin: 0 40px 12px 40px; display: flex; align-items: center; gap: 24px;">
            <div style="font-size: 36px; color: {color}; font-weight: bold; min-width: 40px;">Ex {num}</div>
            <div>
                <div style="font-size: 18px; color: #e0e0e0; font-weight: bold;">{title}</div>
                <code style="font-size: 15px; color: #00ffff;">{ops}</code>
                <div style="font-size: 14px; color: #888; margin-top: 4px;">{desc}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: center; margin: 20px 40px 0; padding: 16px; background-color: #1e2130; border-radius: 8px;">
        <span style="font-size: 17px; color: #ffd43b;">
            All three agents run these same examples — each from their own property perspective.<br/>
            When all three score above threshold simultaneously, that's a Care equilibrium.
        </span>
    </div>
    """, unsafe_allow_html=True)

elif slide.startswith("9."):
    # ---- SLIDE 9: PIPELINE OUTPUT — SUPERPOSE & ENTANGLE ----
    st.markdown("""
    <div style="padding: 30px 40px;">
        <h2 style="font-size: 36px; color: #00ffff; text-align: center; margin-bottom: 10px;">
            Pipeline Output: Illustrative Examples
        </h2>
        <p style="text-align: center; font-size: 15px; color: #888; margin-bottom: 24px;">
            Real compound names and crystal structures from Materials Project. Scores computed by H_total. Not experimental discoveries.
        </p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
            <div style="background-color: #1e2130; padding: 24px; border-radius: 10px; border-left: 5px solid #00d4aa;">
                <h4 style="color: #00d4aa; font-size: 18px; margin-bottom: 12px;">SUPERPOSE: 1,073 → 26 Care Equilibria</h4>
                <div style="font-family: monospace; font-size: 14px; color: #e0e0e0; line-height: 2; background: #0e1117; padding: 12px; border-radius: 6px;">
                    1. <span style="color: #00d4aa;">YbOF</span>: care=0.94<br/>
                    2. <span style="color: #00d4aa;">YbSiO₃</span>: care=0.94<br/>
                    3. <span style="color: #00d4aa;">YbCl₃</span>: care=0.94<br/>
                    4. <span style="color: #00d4aa;">Ba₂YbMoO₆</span>: care=0.93<br/>
                    5. <span style="color: #00d4aa;">Cs₂YbCl₄</span>: care=0.93
                </div>
            </div>
            <div style="background-color: #1e2130; padding: 24px; border-radius: 10px; border-left: 5px solid #da77f2;">
                <h4 style="color: #da77f2; font-size: 18px; margin-bottom: 12px;">ENTANGLE: Multi-Agent Synergy</h4>
                <div style="font-family: monospace; font-size: 14px; color: #e0e0e0; line-height: 2; background: #0e1117; padding: 12px; border-radius: 6px;">
                    <span style="color: #00d4aa;">YbCl₃</span>: B1=0.90 B2=0.94 B3=0.90<br/>
                    <span style="color: #00d4aa;">YbSiO₃</span>: B1=0.90 B2=0.94 B3=0.90<br/>
                    <span style="color: #00d4aa;">CsYbCl₃</span>: B1=0.90 B2=0.92 B3=0.90<br/>
                    <br/>
                    <span style="color: #888;">All three agents score high →</span><br/>
                    <span style="color: #ffd43b;">Care equilibrium (synergy)</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif slide.startswith("10."):
    # ---- SLIDE 10: PIPELINE OUTPUT — INTERFERE & CARE VS NASH ----
    st.markdown("""
    <div style="padding: 30px 40px;">
        <h2 style="font-size: 36px; color: #00ffff; text-align: center; margin-bottom: 10px;">
            Pipeline Output: Pruning & Comparison
        </h2>
        <p style="text-align: center; font-size: 15px; color: #888; margin-bottom: 24px;">
            Illustrative examples from orchestration pipeline test. Scores computed by H_total from real crystal structure data.
        </p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
            <div style="background-color: #1e2130; padding: 24px; border-radius: 10px; border-left: 5px solid #ffd43b;">
                <h4 style="color: #ffd43b; font-size: 18px; margin-bottom: 12px;">INTERFERE: 1,073 → 25 Compounds</h4>
                <div style="font-size: 15px; color: #c0c0c0; line-height: 1.8;">
                    Care-guided quantum pruning:<br/>
                    • High-care → constructive interference<br/>
                    • Low-care → destructive interference<br/><br/>
                    <span style="color: #00d4aa; font-weight: bold;">All 25 Care equilibria preserved</span><br/>
                    <span style="color: #00d4aa;">Zero false negatives</span>
                </div>
            </div>
            <div style="background-color: #1e2130; padding: 24px; border-radius: 10px; border-left: 5px solid #ff6b6b;">
                <h4 style="color: #ff6b6b; font-size: 18px; margin-bottom: 12px;">Care vs Nash</h4>
                <div style="font-size: 15px; color: #c0c0c0; line-height: 1.8;">
                    <b style="color: #ff6b6b;">Nash (YbBr₂)</b>: B2=1.0, B1=0.70, B3=0.65<br/>
                    <span style="color: #888;">One wins, others lose</span><br/><br/>
                    <b style="color: #00d4aa;">Care (YbCl₃)</b>: B1=0.90, B2=0.94, B3=0.90<br/>
                    <span style="color: #ffd43b;">Beyond Pareto — everyone wins</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif slide.startswith("11."):
    # ---- SLIDE 11: CARE VS NASH FULL ----
    st.markdown("""
    <div style="padding: 40px;">
        <h2 style="font-size: 36px; color: #00ffff; text-align: center; margin-bottom: 30px;">
            Care vs Nash Equilibria
        </h2>
        <p style="text-align: center; font-size: 18px; color: #aaa; margin-bottom: 30px;">
            Classical optimization finds trade-offs (Nash). COGNISYN identifies synergies (Care).
        </p>
        <div style="display: grid; grid-template-columns: 1fr 80px 1fr; gap: 0; max-width: 900px; margin: 0 auto; align-items: center;">
            <div style="background-color: #1e2130; padding: 32px; border-radius: 12px; border-left: 6px solid #ff6b6b;">
                <h3 style="color: #ff6b6b; font-size: 26px; margin-bottom: 20px;">Nash Equilibrium</h3>
                <div style="font-size: 18px; color: #e0e0e0; line-height: 2;">
                    <b>YbBr₂</b><br/>
                    B2 (Optical) = <span style="color: #00d4aa; font-size: 22px;">1.0</span><br/>
                    B1 (Host) = <span style="color: #ff6b6b; font-size: 22px;">0.698</span><br/>
                    B3 (Coherence) = <span style="color: #ff6b6b; font-size: 22px;">0.65</span>
                </div>
                <div style="margin-top: 16px; font-size: 15px; color: #888;">One property dominates.<br/>Others are sacrificed.</div>
            </div>
            <div style="text-align: center; font-size: 32px; color: #ffd43b;">→</div>
            <div style="background-color: #1e2130; padding: 32px; border-radius: 12px; border-left: 6px solid #00d4aa;">
                <h3 style="color: #00d4aa; font-size: 26px; margin-bottom: 20px;">Care Equilibrium</h3>
                <div style="font-size: 18px; color: #e0e0e0; line-height: 2;">
                    <b>YbCl₃</b><br/>
                    B1 (Host) = <span style="color: #00d4aa; font-size: 22px;">0.90</span><br/>
                    B2 (Optical) = <span style="color: #00d4aa; font-size: 22px;">0.94</span><br/>
                    B3 (Coherence) = <span style="color: #00d4aa; font-size: 22px;">0.90</span>
                </div>
                <div style="margin-top: 16px; font-size: 15px; color: #888;">All three properties high.<br/>Beyond the Pareto frontier.</div>
            </div>
        </div>
        <div style="text-align: center; margin-top: 30px; padding: 20px; background-color: #1e2130; border-radius: 8px; max-width: 700px; margin-left: auto; margin-right: auto;">
            <span style="font-size: 18px; color: #ffd43b; font-weight: bold;">H<sub>total</sub> = H<sub>quantum</sub> + H<sub>classical</sub> + H<sub>coupling</sub> + H<sub>care</sub></span><br/>
            <span style="font-size: 16px; color: #888;">Care operator C<sub>λ</sub> reweights the energy landscape — cooperation becomes the ground state</span><br/>
            <span style="font-size: 13px; color: #666;">Illustrative examples from orchestration pipeline test. Scores computed by H_total from real crystal structure data.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif slide.startswith("12."):
    # ---- SLIDE 12: AGENT LEARNING ----
    st.markdown("""
    <div style="padding: 40px;">
        <h2 style="font-size: 36px; color: #00ffff; text-align: center; margin-bottom: 30px;">
            Agent Learning: Core Memory Systems
        </h2>
        <p style="text-align: center; font-size: 18px; color: #aaa; margin-bottom: 30px;">
            Agents accumulate episodic memories, discover strategic patterns, and invent new rules.
        </p>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; max-width: 900px; margin: 0 auto;">
            <div style="background-color: #1e2130; padding: 28px; border-radius: 12px; text-align: center;">
                <div style="font-size: 48px; color: #00d4aa; font-weight: bold;">100</div>
                <div style="font-size: 16px; color: #888; margin-top: 8px;">Episodic<br/>Memories</div>
            </div>
            <div style="background-color: #1e2130; padding: 28px; border-radius: 12px; text-align: center;">
                <div style="font-size: 48px; color: #4dabf7; font-weight: bold;">4</div>
                <div style="font-size: 16px; color: #888; margin-top: 8px;">Strategic<br/>Patterns</div>
            </div>
            <div style="background-color: #1e2130; padding: 28px; border-radius: 12px; text-align: center;">
                <div style="font-size: 48px; color: #ffd43b; font-weight: bold;">5</div>
                <div style="font-size: 16px; color: #888; margin-top: 8px;">Rules<br/>Invented</div>
            </div>
            <div style="background-color: #1e2130; padding: 28px; border-radius: 12px; text-align: center;">
                <div style="font-size: 48px; color: #ff6b6b; font-weight: bold;">106</div>
                <div style="font-size: 16px; color: #888; margin-top: 8px;">Total<br/>Memories</div>
            </div>
        </div>
        <div style="max-width: 700px; margin: 30px auto 0; background-color: #1e2130; padding: 24px; border-radius: 10px;">
            <div style="font-size: 16px; color: #c0c0c0; line-height: 1.8;">
                <b style="color: #00d4aa;">Episodic Memory</b> — Each orchestration step recorded. Agents recall what worked.<br/>
                <b style="color: #4dabf7;">Strategic Patterns</b> — Cross-example insights emerge. Agents recognize structure.<br/>
                <b style="color: #ffd43b;">Creative Composition</b> — Agents invent NEW Baba is Quantum rules during orchestration.<br/>
                <b style="color: #ff6b6b;">Cumulative Intelligence</b> — Knowledge persists across examples via DynamicMemoryArchitecture.
            </div>
        </div>
        <div style="text-align: center; margin-top: 20px; font-size: 14px; color: #666;">
            Data from orchestration test run checkpoint files. Illustrative examples.
        </div>
    </div>
    """, unsafe_allow_html=True)
