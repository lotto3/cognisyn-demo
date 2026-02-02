#!/usr/bin/env python3
"""
COGNISYN Yb-171 Host Materials Discovery - Demo Dashboard
=========================================================

Invitation dashboard showing quantum-inspired AI HOST MATERIALS discovery

Target: Investors, partners, and collaborators
Purpose: Demonstrate COGNISYN's approach - Schedule live demo for full system

Key Message: "Classical methods find trade-offs. COGNISYN discovers synergies."

Scientific Context:
- We're finding HOST CRYSTALS to dope Yb-171 ions INTO
- Notation: CaWO₄:Yb³⁺ means "Yb doped into calcium tungstate"
- Three properties: Host Quality, Optical Properties, Spin Coherence
"""

import streamlit as st

# ============================================================================
# CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="COGNISYN: Yb-171 Host Materials Discovery",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="auto"  # Collapsed on mobile, expanded on desktop
)



# ============================================================================
# MAIN DASHBOARD
# ============================================================================

def main():
    """Main dashboard application"""

    # Custom CSS - larger fonts for Streamlit's low-res rendering
    st.markdown("""
        <style>
        .main {background-color: #0e1117;}
        .stMetric {background-color: #1e2130; padding: 10px; border-radius: 5px;}
        h1, h2, h3 {color: #00ffff;}
        p, li, .stMarkdown {font-size: 20px !important; line-height: 1.7;}
        </style>
    """, unsafe_allow_html=True)

    # ========================================================================
    # HEADER
    # ========================================================================

    st.title("🔬 COGNISYN: Yb-171 Host Materials Discovery")

    st.info("📺 **How COGNISYN works** — Care mathematics on classical hardware, applied to quantum materials discovery.")

    st.markdown("""
    **What are host materials?** Crystals we dope Yb-171 ions into (e.g., `CaWO₄:Yb³⁺` = Yb in calcium tungstate).

    **Mission:** Find hosts where **host quality + optical properties + spin coherence** are ALL high—synergies beyond the Pareto frontier.
    """)


    # ========================================================================
    # THE PROBLEM: PICK TWO
    # ========================================================================

    st.header("The Problem: Current Best Materials")

    st.markdown("""
    **Three Properties:** Host Quality (stability + linewidth) · Optical Properties (band gap) · Spin Coherence (I=0 nuclei)

    Current state-of-the-art materials each sacrifice at least one property:
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div style="background-color: #1e2130; padding: 28px; border-radius: 10px; border-left: 6px solid #ff6b6b; height: 320px;">
            <h4 style="color: #4dabf7; font-size: 26px; margin-bottom: 12px;">YVO₄:Yb³⁺</h4>
            <p style="font-size: 18px; line-height: 2; color: #e0e0e0;"><span style="color: #00d4aa;">✓ Host Quality</span><br/><span style="color: #00d4aa;">✓ Optical Properties</span><br/><span style="color: #ff6b6b;">✗ Spin Coherence</span></p>
            <p style="font-size: 15px; color: #aaa; margin-top: 16px;"><i>V-51 (I=7/2, 99.75%) creates magnetic noise</i></p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style="background-color: #1e2130; padding: 28px; border-radius: 10px; border-left: 6px solid #ff6b6b; height: 320px;">
            <h4 style="color: #4dabf7; font-size: 26px; margin-bottom: 12px;">Y₂SiO₅:Yb³⁺</h4>
            <p style="font-size: 18px; line-height: 2; color: #e0e0e0;"><span style="color: #00d4aa;">✓ Host Quality (320 Hz)</span><br/><span style="color: #aaa;">~ Optical Properties</span><br/><span style="color: #ff6b6b;">✗ Spin Coherence</span></p>
            <p style="font-size: 15px; color: #aaa; margin-top: 16px;"><i>Y-89 (I=1/2, 100%) limits T₂ times</i></p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div style="background-color: #1e2130; padding: 28px; border-radius: 10px; border-left: 6px solid #ffd43b; height: 320px;">
            <h4 style="color: #4dabf7; font-size: 26px; margin-bottom: 12px;">CaWO₄:Yb³⁺</h4>
            <p style="font-size: 18px; line-height: 2; color: #e0e0e0;"><span style="color: #00d4aa;">✓ Host Quality</span><br/><span style="color: #aaa;">~ Optical Properties</span><br/><span style="color: #00d4aa;">✓ Spin Coherence (0.15s)</span></p>
            <p style="font-size: 15px; color: #aaa; margin-top: 16px;"><i>Current best. COGNISYN searches for more.</i></p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: center; padding: 24px; background-color: #1e2130; border-radius: 8px; margin-top: 20px;">
        <span style="color: #00d4aa; font-size: 22px; font-weight: bold;">COGNISYN searches systematically for hosts where ALL THREE are high</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ========================================================================
    # HOW IT WORKS: THREE AGENTS, ONE GRAMMAR
    # ========================================================================

    st.header("How It Works: Three Agents, One Grammar")

    st.markdown("""
    COGNISYN uses **three AI agents** that operate as **mathematical operators**, not chatbots.
    Each agent evaluates materials from a different perspective:
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style="background-color: #1e2130; padding: 28px; border-radius: 10px; border-top: 6px solid #00d4aa; height: 200px;">
            <h4 style="color: #00d4aa; font-size: 24px;">B1: Host Quality</h4>
            <p style="font-size: 16px; color: #e0e0e0;">Crystal stability, site symmetry, phonon properties, optical linewidth</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background-color: #1e2130; padding: 28px; border-radius: 10px; border-top: 6px solid #4dabf7; height: 200px;">
            <h4 style="color: #4dabf7; font-size: 24px;">B2: Optical Properties</h4>
            <p style="font-size: 16px; color: #e0e0e0;">Band gap, transition rates, photon emission quality for quantum networking</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="background-color: #1e2130; padding: 28px; border-radius: 10px; border-top: 6px solid #da77f2; height: 200px;">
            <h4 style="color: #da77f2; font-size: 24px;">B3: Spin Coherence</h4>
            <p style="font-size: 16px; color: #e0e0e0;">Nuclear spin bath (I=0), T2 coherence times, magnetic noise suppression</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("")

    st.markdown("""
    Agents communicate through **Baba is Quantum** -- a compositional grammar where rules ARE mathematical operators:

    ```
    [SUBJECT]  [VERB]      [PROPERTY]
    COMPOUNDS  SUPERPOSE   HOST-QUALITY     # Evaluate all compounds for host quality
    COMPOUNDS  FILTER      I=0              # Keep only zero-spin nuclei hosts
    HOST-QUALITY ENTANGLE  CARE-SYNERGY     # Find where all three properties are high
    ```

    Each rule triggers **H_total** -- a real Hamiltonian that computes quantum properties from
    [Materials Project](https://materialsproject.org/) data for **1,073 Yb-containing compounds**.
    Nothing is hallucinated. Every score is computed.
    """)

    st.markdown("---")

    # ========================================================================
    # REAL RESULTS: 5-EXAMPLE DISCOVERY PIPELINE
    # ========================================================================

    st.header("Real Results: A Discovery Pipeline Emerges")

    st.markdown("""
    Over 5 examples, each agent builds increasingly sophisticated operations.
    The grammar is **compositional** -- agents chain operations into pipelines:
    """)

    examples = [
        ("Ex 1", "Cooperative Parallel Evaluation",
         "[COMPOUNDS] [SUPERPOSE] [HOST-QUALITY]",
         "Evaluate all 1,073 Yb compounds. H_total returns Care scores for each.",
         "#00d4aa"),
        ("Ex 2", "Scale Coupling Analysis",
         "[HOST-QUALITY] [COUPLE] [OPTICAL]",
         "Cross-scale coupling -- how does host quality affect optical properties?",
         "#4dabf7"),
        ("Ex 3", "Nuclear Spin Bath Analysis",
         "[COMPOUNDS] [FILTER] [I=0]  [HOST-QUALITY] [ENTANGLE] [CARE-SYNERGY]",
         "Two-stage pipeline: filter for zero-spin hosts, then find synergies across all three properties.",
         "#da77f2"),
        ("Ex 4", "Interference Pruning",
         "[COMPOUNDS] [INTERFERE] [CARE-GUIDED]",
         "Quantum interference: 1,073 compounds pruned to tractable set. Zero Care equilibria lost.",
         "#ffd43b"),
        ("Ex 5", "Full Pipeline Execution",
         "[COMPOUNDS] [FILTER] [I=0]  [HOST-QUALITY] [COUPLE] [CROSS-SCALE]  [HOST-QUALITY] [ENTANGLE] [CARE-SYNERGY]",
         "Three-stage pipeline: Filter -> Cross-scale coupling -> Care synergy. The full discovery workflow.",
         "#ff6b6b"),
    ]

    for ex_num, title, rule, desc, color in examples:
        st.markdown(f"""
        <div style="background-color: #1e2130; padding: 20px; border-radius: 10px; border-left: 6px solid {color}; margin-bottom: 16px;">
            <h4 style="color: {color}; font-size: 20px; margin-bottom: 8px;">{ex_num}: {title}</h4>
            <code style="font-size: 16px; color: #00ffff; background-color: #0e1117; padding: 8px 12px; border-radius: 4px; display: block; margin-bottom: 12px;">{rule}</code>
            <p style="font-size: 16px; color: #c0c0c0;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: center; padding: 24px; background-color: #1e2130; border-radius: 8px; margin-top: 20px;">
        <span style="color: #ffd43b; font-size: 20px; font-weight: bold;">
            All three agents run these examples in parallel -- each from their own perspective.<br/>
            They converge on the same top compounds. That's Care equilibrium.
        </span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ========================================================================
    # PIPELINE OUTPUT: COMPUTED FROM MATERIALS PROJECT DATA
    # ========================================================================

    st.header("Pipeline Output: Illustrative Examples")

    st.markdown("""
    The following output illustrates how the COGNISYN orchestration pipeline evaluates
    **1,073 Yb-containing compounds** cached from the
    [Materials Project](https://materialsproject.org/).
    Compound names and crystal structures are real. Scores are computed by H_total
    from real structure data. These are illustrative pipeline examples, not experimental discoveries.
    """)

    # SUPERPOSE results
    st.markdown("""
    <div style="background-color: #1e2130; padding: 24px; border-radius: 10px; border-left: 6px solid #00d4aa; margin-bottom: 20px;">
        <h4 style="color: #00d4aa; font-size: 20px; margin-bottom: 12px;">SUPERPOSE: 1,073 Compounds Evaluated</h4>
        <p style="font-size: 15px; color: #c0c0c0; margin-bottom: 12px;">
            H_total identified <span style="color: #00d4aa; font-weight: bold;">26 Care equilibria</span>
            (all three properties high) out of 1,073 compounds.
            The remaining 1,047 are Nash equilibria (trade-offs).
        </p>
        <div style="background-color: #0e1117; padding: 16px; border-radius: 6px; font-family: monospace;">
            <div style="color: #00ffff; font-size: 14px; margin-bottom: 8px;">TOP 5 — Care Equilibria (Beyond Pareto Frontier):</div>
            <div style="font-size: 14px; color: #e0e0e0; line-height: 2;">
                1. <span style="color: #00d4aa;">YbOF</span>: care=0.94 — tetragonal structure<br/>
                2. <span style="color: #00d4aa;">YbSiO₃</span>: care=0.94<br/>
                3. <span style="color: #00d4aa;">YbCl₃</span>: care=0.94<br/>
                4. <span style="color: #00d4aa;">Ba₂YbMoO₆</span>: care=0.93 — Ba-138 I=0 (71.7%) + heavy elements<br/>
                5. <span style="color: #00d4aa;">Cs₂YbCl₄</span>: care=0.93 — tetragonal structure
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # FILTER + ENTANGLE results
    st.markdown("""
    <div style="background-color: #1e2130; padding: 24px; border-radius: 10px; border-left: 6px solid #da77f2; margin-bottom: 20px;">
        <h4 style="color: #da77f2; font-size: 20px; margin-bottom: 12px;">FILTER I=0 → ENTANGLE: Nuclear Spin Bath + Synergy Detection</h4>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
            <div style="background-color: #0e1117; padding: 16px; border-radius: 6px;">
                <div style="color: #00ffff; font-size: 14px; margin-bottom: 8px;">FILTER: I=0 Spin Bath Analysis</div>
                <div style="font-size: 14px; color: #e0e0e0; line-height: 2;">
                    1,073 → <span style="color: #00d4aa;">1,057</span> passed (i_zero &gt; 0.3)<br/>
                    <br/>
                    Top coherence hosts:<br/>
                    • <span style="color: #da77f2;">BaYbCuTe₃</span>: I=0 score=0.90, coherence=0.94<br/>
                    • <span style="color: #da77f2;">Ba₃Yb₂TeO₅</span>: I=0 score=0.90, coherence=0.94<br/>
                    • <span style="color: #da77f2;">BaSrYb₂</span>: I=0 score=0.95, coherence=0.83
                </div>
            </div>
            <div style="background-color: #0e1117; padding: 16px; border-radius: 6px;">
                <div style="color: #00ffff; font-size: 14px; margin-bottom: 8px;">ENTANGLE: Multi-Agent Synergy</div>
                <div style="font-size: 14px; color: #e0e0e0; line-height: 2;">
                    <span style="color: #00d4aa;">26 compounds</span> where ALL THREE benefit<br/>
                    <br/>
                    Top synergy compounds:<br/>
                    • <span style="color: #00d4aa;">YbCl₃</span>: B1=0.90, B2=0.94, B3=0.90<br/>
                    • <span style="color: #00d4aa;">YbSiO₃</span>: B1=0.90, B2=0.94, B3=0.90<br/>
                    • <span style="color: #00d4aa;">CsYbCl₃</span>: B1=0.90, B2=0.92, B3=0.90
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # INTERFERE results
    st.markdown("""
    <div style="background-color: #1e2130; padding: 24px; border-radius: 10px; border-left: 6px solid #ffd43b; margin-bottom: 20px;">
        <h4 style="color: #ffd43b; font-size: 20px; margin-bottom: 12px;">INTERFERE: Quantum Pruning — 1,073 → 25 Compounds</h4>
        <p style="font-size: 15px; color: #c0c0c0; margin-bottom: 12px;">
            Care-guided interference dynamics: high-care compounds receive constructive interference (amplified),
            low-care compounds receive destructive interference (suppressed).
            <span style="color: #00d4aa; font-weight: bold;">All 25 Care equilibria preserved. Zero false negatives.</span>
        </p>
        <div style="background-color: #0e1117; padding: 16px; border-radius: 6px; font-family: monospace;">
            <div style="color: #00ffff; font-size: 14px; margin-bottom: 8px;">TOP 5 — Post-Interference (by interference score):</div>
            <div style="font-size: 14px; color: #e0e0e0; line-height: 2;">
                1. <span style="color: #00d4aa;">YbOF</span>: score=0.937<br/>
                2. <span style="color: #00d4aa;">YbSiO₃</span>: score=0.936<br/>
                3. <span style="color: #00d4aa;">YbCl₃</span>: score=0.935<br/>
                4. <span style="color: #00d4aa;">Ba₂YbMoO₆</span>: score=0.934<br/>
                5. <span style="color: #00d4aa;">Cs₂YbCl₄</span>: score=0.932
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: center; padding: 20px; background-color: #1e2130; border-radius: 8px; margin-top: 10px; margin-bottom: 10px;">
        <span style="font-size: 15px; color: #888;">
            Illustrative pipeline output — compound names and crystal structures are real
            (Materials Project, CC BY 4.0). Scores are computed, not experimental measurements.
        </span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ========================================================================
    # CARE VS NASH
    # ========================================================================

    st.header("The Key Insight: Care vs Nash Equilibria")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="background-color: #1e2130; padding: 28px; border-radius: 10px; border-left: 6px solid #ff6b6b; height: 300px;">
            <h4 style="color: #ff6b6b; font-size: 24px;">Nash Equilibrium (Trade-off)</h4>
            <p style="font-size: 17px; color: #e0e0e0; line-height: 1.8;">
                One property wins, others lose.<br/><br/>
                <b>YbBr₂:</b><br/>
                B2 (Optical) = <span style="color: #00d4aa;">1.0</span><br/>
                B1 (Host) = <span style="color: #ff6b6b;">0.698</span><br/>
                B3 (Coherence) = <span style="color: #ff6b6b;">0.65</span>
            </p>
            <p style="font-size: 14px; color: #aaa; margin-top: 12px;"><i>Great optics, poor host, poor coherence</i></p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background-color: #1e2130; padding: 28px; border-radius: 10px; border-left: 6px solid #00d4aa; height: 300px;">
            <h4 style="color: #00d4aa; font-size: 24px;">Care Equilibrium (Synergy)</h4>
            <p style="font-size: 17px; color: #e0e0e0; line-height: 1.8;">
                ALL three properties are high.<br/><br/>
                <b>YbCl₃:</b><br/>
                B1 (Host) = <span style="color: #00d4aa;">0.90</span><br/>
                B2 (Optical) = <span style="color: #00d4aa;">0.94</span><br/>
                B3 (Coherence) = <span style="color: #00d4aa;">0.90</span>
            </p>
            <p style="font-size: 14px; color: #aaa; margin-top: 12px;"><i>Beyond Pareto -- everyone wins</i></p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: center; padding: 24px; background-color: #1e2130; border-radius: 8px; margin-top: 20px;">
        <span style="color: #00d4aa; font-size: 20px; font-weight: bold;">
            Classical optimization finds Nash equilibria (trade-offs).<br/>
            COGNISYN discovers Care equilibria (synergies beyond the Pareto frontier).
        </span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ========================================================================
    # BY THE NUMBERS
    # ========================================================================

    st.header("By the Numbers")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Compounds Evaluated", "1,073")
    col2.metric("AI Agents", "3")
    col3.metric("Properties Optimized", "3")
    col4.metric("Strategic Patterns", "24+")

    st.markdown("")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Data Source", "Materials Project")
    col2.metric("Computation", "Real H_total")
    col3.metric("Hallucination", "Zero")
    col4.metric("Agent Behavior", "Operator")

    st.markdown("---")

    # ========================================================================
    # ORCHESTRATION MONITOR
    # ========================================================================

    st.header("Orchestration Monitor: The System Running")

    st.markdown("""
    The COGNISYN Test Run Monitor shows the orchestration pipeline in action.
    Three agents — **B1 (Host Quality)**, **B2 (Optical)**, **B3 (Coherence)** — each run
    5 examples in parallel, building from single operations to multi-stage pipelines.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="background-color: #1e2130; padding: 24px; border-radius: 10px; border-left: 6px solid #4dabf7; margin-bottom: 16px;">
            <h4 style="color: #4dabf7; font-size: 20px; margin-bottom: 12px;">System Overview</h4>
            <div style="font-size: 16px; color: #e0e0e0; line-height: 2;">
                Examples: <span style="color: #00d4aa; font-weight: bold;">5/5</span><br/>
                Agents: <span style="color: #00d4aa; font-weight: bold;">3/3</span><br/>
                Checkpoints: <span style="color: #00d4aa; font-weight: bold;">33</span><br/>
                Compounds: <span style="color: #00d4aa; font-weight: bold;">1,073</span><br/>
                Strategic Patterns: <span style="color: #00d4aa; font-weight: bold;">24</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background-color: #1e2130; padding: 24px; border-radius: 10px; border-left: 6px solid #00d4aa; margin-bottom: 16px;">
            <h4 style="color: #00d4aa; font-size: 20px; margin-bottom: 12px;">Pipeline Progression (B1)</h4>
            <div style="font-size: 14px; color: #e0e0e0; line-height: 2.2;">
                Ex 1: <code style="color: #00ffff;">[COMPOUNDS] [SUPERPOSE] [HOST-QUALITY]</code><br/>
                Ex 2: <code style="color: #00ffff;">[HOST-QUALITY] [COUPLE] [OPTICAL]</code><br/>
                Ex 3: <code style="color: #00ffff;">[COMPOUNDS] [FILTER] [I=0] [HOST-QUALITY] [ENTANGLE] [CARE-SYNERGY]</code><br/>
                Ex 4: <code style="color: #00ffff;">[COMPOUNDS] [INTERFERE] [CARE-GUIDED]</code><br/>
                Ex 5: <code style="color: #00ffff;">[FILTER] [I=0] → [COUPLE] [CROSS-SCALE] → [ENTANGLE] [CARE-SYNERGY]</code>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: center; padding: 16px; background-color: #1e2130; border-radius: 8px;">
        <span style="font-size: 15px; color: #888;">
            Each agent runs the same examples from its own perspective (host quality, optical, coherence).
            All three converge on the same top compounds — mathematical convergence through the Care operator.
        </span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ========================================================================
    # CONTACT
    # ========================================================================

    st.header("Contact")

    st.markdown("""
    **Tish Shute** — Founder & CEO

    **Email:** tish@cognisyn.ai

    **55,000 lines of code** · 2 years of AI-human collaboration · Built with Claude
    """)


    # ========================================================================
    # SIDEBAR
    # ========================================================================

    with st.sidebar:
        st.header("ℹ️ About")

        st.markdown("""
        **COGNISYN** discovers Yb-171 host materials through quantum-inspired game theory.

        **Key Innovation:** Care equilibria (synergies) beyond Pareto frontier (trade-offs).

        **Three Properties:**
        - Host Quality
        - Optical Properties
        - Spin Coherence
        """)

        st.markdown("---")

        st.markdown("""
        **Data:** [Materials Project](https://materialsproject.org/)

        **Contact:** tish@cognisyn.ai
        """)

        st.caption("Powered by COGNISYN · Built with Streamlit")


# ============================================================================
# RUN
# ============================================================================

if __name__ == "__main__":
    main()
