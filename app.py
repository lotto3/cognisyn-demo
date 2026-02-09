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
    initial_sidebar_state="collapsed"
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
        /* Hide sidebar toggle for clean layout */
        [data-testid="collapsedControl"] {display: none;}
        </style>
    """, unsafe_allow_html=True)

    # ========================================================================
    # HEADER
    # ========================================================================

    st.title("🔬 COGNISYN")

    st.markdown("<p style='font-size: 1.3em; font-weight: 600; color: #00d4aa;'>AI for materials discovery via quantum game theory</p>", unsafe_allow_html=True)

    st.info("**COGNISYN** turns LLMs into mathematical physics operators. Three AI agents create rules in Baba is Quantum grammar — subject, verb, property. Each rule triggers real Hamiltonian computation. The LLMs build the language through discovery — but results come from the math engine, not generation. No results hallucinated.")

    st.markdown("""
    **First application: quantum computing materials discovery** — finding host crystals for Yb-171 where host quality, optical properties, and spin coherence are ALL high simultaneously, not one at the expense of another.

    **What are host materials?** Crystals that Yb-171 ions are doped into (e.g., `CaWO₄:Yb³⁺` = Yb in calcium tungstate).
    """)

    # ========================================================================
    # THE PROBLEM: PICK TWO
    # ========================================================================

    st.header("The Problem: Current Best Materials")

    st.markdown("""
    **Three Properties:** Host Quality (stability + linewidth) · Optical Properties (band gap) · Spin Coherence (I=0 nuclei)

    Well-known host materials each sacrifice at least one property (illustrative examples):
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div style="background-color: #1e2130; padding: 28px; border-radius: 10px; border-left: 6px solid #ff6b6b; min-height: 320px;">
            <h4 style="color: #4dabf7; font-size: 26px; margin-bottom: 12px;">YVO₄:Yb³⁺</h4>
            <p style="font-size: 18px; line-height: 2; color: #e0e0e0;"><span style="color: #00d4aa;">✓ Host Quality</span><br/><span style="color: #00d4aa;">✓ Optical Properties</span><br/><span style="color: #ff6b6b;">✗ Spin Coherence</span></p>
            <p style="font-size: 15px; color: #aaa; margin-top: 16px;"><i>V-51 (I=7/2, 99.75%) creates magnetic noise</i></p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style="background-color: #1e2130; padding: 28px; border-radius: 10px; border-left: 6px solid #ff6b6b; min-height: 320px;">
            <h4 style="color: #4dabf7; font-size: 26px; margin-bottom: 12px;">Y₂SiO₅:Yb³⁺</h4>
            <p style="font-size: 18px; line-height: 2; color: #e0e0e0;"><span style="color: #00d4aa;">✓ Host Quality (320 Hz)</span><br/><span style="color: #aaa;">~ Optical Properties</span><br/><span style="color: #ff6b6b;">✗ Spin Coherence</span></p>
            <p style="font-size: 15px; color: #aaa; margin-top: 16px;"><i>Y-89 (I=1/2, 100%) limits T₂ times</i></p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div style="background-color: #1e2130; padding: 28px; border-radius: 10px; border-left: 6px solid #ffd43b; min-height: 320px;">
            <h4 style="color: #4dabf7; font-size: 26px; margin-bottom: 12px;">CaWO₄:Yb³⁺</h4>
            <p style="font-size: 18px; line-height: 2; color: #e0e0e0;"><span style="color: #00d4aa;">✓ Host Quality</span><br/><span style="color: #aaa;">~ Optical Properties</span><br/><span style="color: #00d4aa;">✓ Spin Coherence (0.15s)</span></p>
            <p style="font-size: 15px; color: #aaa; margin-top: 16px;"><i>Current best. COGNISYN searches for more.</i></p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: center; padding: 24px; background-color: #1e2130; border-radius: 8px; margin-top: 20px;">
        <span style="color: #00d4aa; font-size: 22px; font-weight: bold;">COGNISYN finds cooperative wins — host materials where ALL THREE are high</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ========================================================================
    # A DIFFERENT MATHEMATICS (from pitch deck slides 2 & 3)
    # ========================================================================

    st.header("A Different Mathematics")

    st.markdown("""
    <div style="background-color: #1e2130; padding: 28px; border-radius: 10px; border-left: 6px solid #ff6b6b; margin-bottom: 20px;">
        <h4 style="color: #ff6b6b; font-size: 22px; margin-bottom: 12px;">The Hidden Premise</h4>
        <p style="font-size: 17px; color: #e0e0e0; line-height: 1.8;">
            Classical optimization forces trade-offs — every gain requires a sacrifice:
        </p>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-top: 16px;">
            <div style="text-align: center; padding: 14px; background-color: #0e1117; border-radius: 8px; border: 1px solid #ff6b6b44;">
                <div style="font-size: 16px; color: #ff6b6b; font-weight: 600;">Drug Discovery</div>
                <div style="font-size: 14px; color: #aaa; margin-top: 6px;">Efficacy OR Safety OR Synthesizability</div>
            </div>
            <div style="text-align: center; padding: 14px; background-color: #0e1117; border-radius: 8px; border: 1px solid #ff6b6b44;">
                <div style="font-size: 16px; color: #ff6b6b; font-weight: 600;">Control Systems (PID)</div>
                <div style="font-size: 14px; color: #aaa; margin-top: 6px;">Speed OR Stability OR Accuracy</div>
            </div>
            <div style="text-align: center; padding: 14px; background-color: #0e1117; border-radius: 8px; border: 1px solid #ff6b6b44;">
                <div style="font-size: 16px; color: #ff6b6b; font-weight: 600;">Foundation Models</div>
                <div style="font-size: 14px; color: #aaa; margin-top: 6px;">Capability OR Alignment OR Efficiency</div>
            </div>
        </div>
        <p style="font-size: 17px; color: #e0e0e0; line-height: 1.8; margin-top: 16px;">
            Classical methods assume objectives must be optimized independently or collapsed into weighted trade-offs.
            <span style="color: #ff6b6b; font-weight: 600;">This assumption creates the competition it claims to solve.</span>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: #1e2130; padding: 28px; border-radius: 10px; border-left: 6px solid #4dabf7; margin-bottom: 20px;">
        <p style="font-size: 20px; color: #4dabf7; font-style: italic; text-align: center;">
            But is this a physics limit... or a mathematical assumption we can change?
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: #1e2130; padding: 28px; border-radius: 10px; border-left: 6px solid #00d4aa; margin-bottom: 20px;">
        <h4 style="color: #00d4aa; font-size: 22px; margin-bottom: 12px;">The Solution: A Different Mathematics</h4>
        <p style="font-size: 17px; color: #e0e0e0; line-height: 1.8;">
            Quantum game theory introduces superposition, interference, and entanglement.
            Three AI agents operate this mathematics through Baba is Quantum grammar and COGNISYN's mathematical physics engine. <span style="color: #00d4aa; font-weight: 700;">The Care operator makes the computation tractable and cooperation the ground state.</span>
        </p>
        <p style="font-size: 17px; color: #e0e0e0; line-height: 1.8; margin-top: 12px;">
            <span style="color: #ffd43b; font-weight: 700;">Mathematical structures transfer without the physical substrate:</span>
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style="background-color: #1e2130; padding: 20px; border-radius: 10px; text-align: center; min-height: 160px;">
            <h4 style="color: #ffd43b; font-size: 18px;">Annealing</h4>
            <p style="font-size: 15px; color: #aaa; margin-top: 8px;">Metallurgy math<br/><b style="color: #e0e0e0;">→ no molten metal</b></p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background-color: #1e2130; padding: 20px; border-radius: 10px; text-align: center; min-height: 160px;">
            <h4 style="color: #da77f2; font-size: 18px;">Genetic Algorithms</h4>
            <p style="font-size: 15px; color: #aaa; margin-top: 8px;">Biology math<br/><b style="color: #e0e0e0;">→ no DNA</b></p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="background-color: #1e2130; padding: 20px; border-radius: 10px; text-align: center; border: 2px solid #00d4aa; min-height: 160px;">
            <h4 style="color: #00d4aa; font-size: 18px;">COGNISYN</h4>
            <p style="font-size: 15px; color: #aaa; margin-top: 8px;">Quantum game theory<br/><b style="color: #e0e0e0;">→ no qubits</b></p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # ========================================================================
    # THE STAG HUNT (from pitch deck slide 4)
    # ========================================================================

    st.header("The Stag Hunt: Game Theory's Classic Cooperation Problem")

    st.markdown("""
    <div style="background-color: #1e2130; padding: 28px; border-radius: 10px; margin-bottom: 20px;">
        <p style="font-size: 15px; color: #aaa; text-align: center; margin-bottom: 16px;">
            How "pick one" becomes "pick both"
        </p>
        <p style="font-size: 17px; color: #e0e0e0; line-height: 1.8;">
            The <b>Stag Hunt</b> is one of game theory's most important problems. Two hunters go out
            separately. Each must choose independently:
        </p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 16px 0;">
            <div style="padding: 16px; background-color: #0e1117; border-radius: 8px; border: 1px solid #ffd43b44;">
                <div style="font-size: 20px; margin-bottom: 6px;">🦌</div>
                <div style="font-size: 17px; color: #ffd43b; font-weight: 600;">Hunt the Stag</div>
                <div style="font-size: 15px; color: #aaa; margin-top: 6px;">
                    High reward — feeds the village for a week.<br/>
                    But it <b style="color: #e0e0e0;">requires both hunters</b>. If the other hunter doesn't show up, you get nothing.
                </div>
            </div>
            <div style="padding: 16px; background-color: #0e1117; border-radius: 8px; border: 1px solid #ff6b6b44;">
                <div style="font-size: 20px; margin-bottom: 6px;">🐰</div>
                <div style="font-size: 17px; color: #ff6b6b; font-weight: 600;">Hunt a Hare</div>
                <div style="font-size: 15px; color: #aaa; margin-top: 6px;">
                    Low reward — a small meal.<br/>
                    But it's <b style="color: #e0e0e0;">guaranteed</b>. You can catch a hare alone, no matter what the other hunter does.
                </div>
            </div>
        </div>
        <p style="font-size: 17px; color: #e0e0e0; line-height: 1.8;">
            The rational choice? <span style="color: #ff6b6b; font-weight: 600;">Hunt hare.</span>
            You can't be sure the other hunter will cooperate, so you play it safe.
            Both hunters reason the same way — and both end up with a small meal when they could have
            feasted. <span style="color: #ff6b6b;">This is the Nash equilibrium: stable, but suboptimal.</span>
            No one can improve by changing alone, yet everyone is worse off.
        </p>
        <p style="font-size: 17px; color: #00d4aa; line-height: 1.8; margin-top: 12px; font-weight: 600;">
            Same principle as Yb-171 host materials discovery: classical optimization forces trade-offs. COGNISYN's three AI agents apply quantum game theory through Baba is Quantum grammar — COGNISYN's mathematical physics engine computes the results, agents evaluate and discover cooperative wins.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="background-color: #1e2130; padding: 28px; border-radius: 10px; border: 2px solid #ff6b6b; min-height: 320px;">
            <h4 style="color: #ff6b6b; font-size: 22px; margin-bottom: 16px;">CLASSICAL (Nash Equilibrium)</h4>
            <div style="background-color: #0e1117; border-radius: 8px; padding: 14px; font-family: monospace; font-size: 15px; margin-bottom: 12px;">
                <div style="color: #4dabf7;">Hunter A</div>
                <div style="color: #aaa; margin-left: 16px;">├── 🦌 Stag (needs both)</div>
                <div style="color: #ff6b6b; margin-left: 16px; font-weight: 600;">└── 🐰 Hare (safe) ✓</div>
                <div style="color: #da77f2; margin-top: 8px;">Hunter B</div>
                <div style="color: #aaa; margin-left: 16px;">├── 🦌 Stag (risky)</div>
                <div style="color: #ff6b6b; margin-left: 16px; font-weight: 600;">└── 🐰 Hare (safe) ✓</div>
            </div>
            <div style="text-align: center; padding: 12px; background-color: #ff6b6b33; border-radius: 6px;">
                <span style="font-size: 16px; color: #ff6b6b; font-weight: 600;">🐰🐰 Both pick Hare — stable but suboptimal</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background-color: #1e2130; padding: 28px; border-radius: 10px; border: 2px solid #00d4aa; min-height: 320px;">
            <h4 style="color: #00d4aa; font-size: 22px; margin-bottom: 16px;">QUANTUM (Cooperative Equilibrium)</h4>
            <div style="background-color: #0e1117; border-radius: 8px; padding: 14px; font-family: monospace; font-size: 15px; margin-bottom: 12px;">
                <div style="color: #4dabf7;">Hunter A</div>
                <div style="color: #4dabf7; margin-left: 16px;">══╦══ 🦌 ╗</div>
                <div style="color: #4dabf7; margin-left: 16px;">  ╚══ 🐰 <span style="color: #00d4aa;">╬══►</span> 🦌🦌</div>
                <div style="color: #da77f2; margin-top: 8px;">Hunter B</div>
                <div style="color: #da77f2; margin-left: 16px;">══╦══ 🦌 ╝</div>
                <div style="color: #da77f2; margin-left: 16px;">  ╚══ 🐰</div>
            </div>
            <div style="text-align: center; padding: 12px; background-color: #00d4aa33; border-radius: 6px;">
                <span style="font-size: 16px; color: #00d4aa; font-weight: 600;">🦌🦌 Both hunt Stag — cooperation is ground state</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-top: 20px; margin-bottom: 20px;">
        <div style="background-color: #1e2130; padding: 20px; border-radius: 10px; text-align: center; border: 1px solid #4dabf7;">
            <div style="font-size: 13px; color: #aaa; font-family: monospace;">══ double lines</div>
            <h4 style="color: #4dabf7; font-size: 18px; margin-top: 6px;">Superposition</h4>
            <p style="font-size: 14px; color: #aaa; margin-top: 8px;">Explore ALL strategies simultaneously</p>
        </div>
        <div style="background-color: #1e2130; padding: 20px; border-radius: 10px; text-align: center; border: 1px solid #da77f2;">
            <div style="font-size: 13px; color: #aaa; font-family: monospace;">╗╝ paths merge</div>
            <h4 style="color: #da77f2; font-size: 18px; margin-top: 6px;">Entanglement</h4>
            <p style="font-size: 14px; color: #aaa; margin-top: 8px;">Agents' choices become correlated</p>
        </div>
        <div style="background-color: #1e2130; padding: 20px; border-radius: 10px; text-align: center; border: 1px solid #00d4aa;">
            <div style="font-size: 13px; color: #aaa; font-family: monospace;">╬══► synergy vertex</div>
            <h4 style="color: #00d4aa; font-size: 18px; margin-top: 6px;">Interference</h4>
            <p style="font-size: 14px; color: #aaa; margin-top: 8px;">Amplify synergy, suppress trade-offs</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: center; padding: 24px; background-color: #1e2130; border-radius: 8px; border: 2px solid #00d4aa;">
        <span style="color: #e0e0e0; font-size: 18px;">
            <span style="color: #ff6b6b; font-weight: bold;">Classical:</span> both pick hare (stable but suboptimal) →
            <span style="color: #00d4aa; font-weight: bold;">Quantum:</span> both hunt stag (cooperation wins)
        </span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ========================================================================
    # HOW IT WORKS: THREE AGENTS, ONE GRAMMAR
    # ========================================================================

    st.header("How It Works: Three Agents, One Grammar")

    st.markdown("""
    COGNISYN is an external framework that turns LLMs into **mathematical physics operators** through their APIs.
    LLMs don't discuss science — they execute operations that trigger real Hamiltonians computing real properties from real data.
    Three agents operate in parallel, each evaluating from a different perspective:
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style="background-color: #1e2130; padding: 28px; border-radius: 10px; border-top: 6px solid #00d4aa; min-height: 200px;">
            <h4 style="color: #00d4aa; font-size: 24px;">B1: Host Quality</h4>
            <p style="font-size: 16px; color: #e0e0e0;">Crystal stability, site symmetry, phonon properties, optical linewidth</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background-color: #1e2130; padding: 28px; border-radius: 10px; border-top: 6px solid #4dabf7; min-height: 200px;">
            <h4 style="color: #4dabf7; font-size: 24px;">B2: Optical Properties</h4>
            <p style="font-size: 16px; color: #e0e0e0;">Band gap, transition rates, photon emission quality for quantum networking</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="background-color: #1e2130; padding: 28px; border-radius: 10px; border-top: 6px solid #da77f2; min-height: 200px;">
            <h4 style="color: #da77f2; font-size: 24px;">B3: Spin Coherence</h4>
            <p style="font-size: 16px; color: #e0e0e0;">Nuclear spin bath (I=0), T2 coherence times, magnetic noise suppression</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("")

    st.markdown("""
    Agents communicate with the mathematical physics engine through **Baba is Quantum** — a compositional grammar where rules ARE mathematical operators.
    23 operators access the full H_total Hamiltonian:
    """)

    st.markdown("""<div style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; margin-bottom: 20px;">
<span style="padding: 8px 16px; background-color: #00d4aa33; border: 1px solid #00d4aa; border-radius: 20px; color: #00d4aa; font-weight: 600; font-size: 15px;">Superpose</span>
<span style="padding: 8px 16px; background-color: #4dabf733; border: 1px solid #4dabf7; border-radius: 20px; color: #4dabf7; font-weight: 600; font-size: 15px;">Interfere</span>
<span style="padding: 8px 16px; background-color: #da77f233; border: 1px solid #da77f2; border-radius: 20px; color: #da77f2; font-weight: 600; font-size: 15px;">Entangle</span>
<span style="padding: 8px 16px; background-color: #ffd43b33; border: 1px solid #ffd43b; border-radius: 20px; color: #ffd43b; font-weight: 600; font-size: 15px;">Care</span>
<span style="padding: 8px 16px; background-color: #ff6b6b33; border: 1px solid #ff6b6b; border-radius: 20px; color: #ff6b6b; font-weight: 600; font-size: 15px;">Boundary</span>
<span style="padding: 8px 16px; background-color: #4dabf733; border: 1px solid #4dabf7; border-radius: 20px; color: #4dabf7; font-weight: 600; font-size: 15px;">Scale Coupling</span>
<span style="padding: 8px 16px; background-color: #00d4aa33; border: 1px solid #00d4aa; border-radius: 20px; color: #00d4aa; font-weight: 600; font-size: 15px;">EQFT</span>
<span style="padding: 8px 16px; background-color: #da77f233; border: 1px solid #da77f2; border-radius: 20px; color: #da77f2; font-weight: 600; font-size: 15px;">Coherence</span>
</div>""", unsafe_allow_html=True)

    st.markdown("""<div style="background-color: #1e2130; padding: 24px; border-radius: 10px; margin-bottom: 16px;">
<div style="text-align: center; font-size: 16px; color: #aaa; margin-bottom: 16px;">Grammar: <span style="color: #da77f2;">[SUBJECT]</span> <span style="color: #4dabf7;">[VERB]</span> <span style="color: #00d4aa;">[PROPERTY]</span> → H_total computes</div>
<div style="display: grid; grid-template-columns: 1fr auto; gap: 8px 20px; font-size: 14px; font-family: monospace; padding: 0 20px;">
<span style="color: #e0e0e0;">[COMPOUNDS] [SUPERPOSE] [<span style="color: #00d4aa;">HOST-QUALITY</span>]</span>
<span style="color: #aaa; font-family: sans-serif;">B1 evaluates all compounds for its property</span>
<span style="color: #e0e0e0;">[COMPOUNDS] [SUPERPOSE] [<span style="color: #4dabf7;">OPTICAL</span>]</span>
<span style="color: #aaa; font-family: sans-serif;">B2 evaluates from its perspective</span>
<span style="color: #e0e0e0;">[<span style="color: #00d4aa;">HOST-QUALITY</span>] [COUPLE] [<span style="color: #4dabf7;">OPTICAL</span>]</span>
<span style="color: #aaa; font-family: sans-serif;">Cross-property scale coupling</span>
<span style="color: #e0e0e0;">[COMPOUNDS] [FILTER] [I=0] → [<span style="color: #da77f2;">COHERENCE</span>] [ENTANGLE] [CARE-SYNERGY]</span>
<span style="color: #aaa; font-family: sans-serif;">B3 multi-stage pipeline</span>
</div>
</div>""", unsafe_allow_html=True)

    st.markdown("""
    Each rule accesses **H_total** — a Hermitian Hamiltonian in Hilbert space with 8 components,
    computed classically from [Materials Project](https://materialsproject.org/) data for **1,073 Yb-containing compounds**.
    The LLMs operate the mathematics — they don't generate the answers.
    """)

    # Why This Runs on Classical Compute (from pitch deck slide 5)
    st.markdown("""
    <div style="padding: 24px; background-color: #1e2130; border: 2px solid #00d4aa; border-radius: 10px; margin-top: 20px;">
        <div style="font-size: 18px; color: #00d4aa; font-weight: 600; margin-bottom: 12px;">Why This Runs on Classical Compute</div>
        <p style="font-size: 17px; color: #e0e0e0; line-height: 1.8;">
            <span style="color: #da77f2; font-weight: 600;">Dimension reduction:</span> Baba rules project exponential
            quantum state spaces onto tractable submanifolds.
            <span style="color: #00d4aa; font-weight: 600;">Care operator C<sub>λ</sub></span> further constrains search
            to synergistic equilibria — not exploring all 2<sup>n</sup> states, just the ones where
            cooperation emerges.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ========================================================================
    # LLMs AS STRATEGIC OPERATORS (from pitch deck slide 10)
    # ========================================================================

    st.header("LLMs as Strategic Operators")

    st.markdown("""
Not knowledge repositories — mathematical physics operators
    """)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("""<div style="background-color: #1e2130; padding: 24px; border-radius: 10px; border: 2px solid #2a2a3a; text-align: center; min-height: 160px;">
<div style="font-size: 22px; color: #da77f2; font-weight: 700; margin-bottom: 10px;">Most AI</div>
<div style="font-size: 16px; color: #aaa;">LLMs as knowledge repositories</div>
<div style="font-size: 17px; color: #e0e0e0; margin-top: 10px;">Query → Answer</div>
</div>""", unsafe_allow_html=True)

    with col2:
        st.markdown("""<div style="background-color: #1e2130; padding: 24px; border-radius: 10px; border: 2px solid #00d4aa; text-align: center; min-height: 160px;">
<div style="font-size: 22px; color: #00d4aa; font-weight: 700; margin-bottom: 10px;">COGNISYN</div>
<div style="font-size: 16px; color: #aaa;">LLMs as strategic operators</div>
<div style="font-size: 17px; color: #e0e0e0; margin-top: 10px;">Rule → H_total → Discovery</div>
</div>""", unsafe_allow_html=True)

    st.markdown("""<div style="text-align: center; padding: 20px; background-color: #1e2130; border: 2px solid #da77f2; border-radius: 10px; margin-top: 20px;">
<span style="color: #da77f2; font-size: 18px; font-style: italic;">
Language emerges bottom-up — AI agents discover what works through doing
</span>
</div>""", unsafe_allow_html=True)

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
            When all three agents score above threshold simultaneously, that's a Care equilibrium — a synergy beyond the Pareto frontier.
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
    # CARE VS NASH — RESULTS COMPARISON
    # ========================================================================

    st.header("The Key Insight: Care vs Nash Equilibria")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div style="background-color: #1e2130; padding: 28px; border-radius: 10px; border: 2px solid #ff6b6b;">
            <h4 style="color: #ff6b6b; font-size: 22px; margin-bottom: 12px;">NASH EQUILIBRIUM</h4>
            <p style="font-size: 15px; color: #e0e0e0; margin-bottom: 10px;">Classical game theory</p>
            <div style="padding: 14px; background-color: #ff6b6b22; border-radius: 6px; margin-bottom: 16px;">
                <p style="font-size: 15px; color: #aaa; line-height: 1.8;">
                    • Agents optimize <span style="color: #ff6b6b;">independently</span><br/>
                    • Properties <span style="color: #ff6b6b;">compete</span><br/>
                    • Result: Trade-offs (Pareto)
                </p>
            </div>
            <p style="font-size: 15px; color: #e0e0e0; margin-bottom: 6px;"><b>Example: YbBr₂</b></p>
            <p style="font-size: 16px; color: #e0e0e0; line-height: 1.8;">
                B2 (Optical) = <span style="color: #00d4aa;">1.0</span><br/>
                B1 (Host) = <span style="color: #ff6b6b;">0.698</span><br/>
                B3 (Coherence) = <span style="color: #ff6b6b;">0.65</span>
            </p>
            <p style="font-size: 14px; color: #aaa; margin-top: 10px;"><i>Great optics, poor host, poor coherence</i></p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background-color: #1e2130; padding: 28px; border-radius: 10px; border: 2px solid #00d4aa;">
            <h4 style="color: #00d4aa; font-size: 22px; margin-bottom: 12px;">CARE EQUILIBRIUM</h4>
            <p style="font-size: 15px; color: #e0e0e0; margin-bottom: 10px;">COGNISYN innovation</p>
            <div style="padding: 14px; background-color: #00d4aa22; border-radius: 6px; margin-bottom: 16px;">
                <p style="font-size: 15px; color: #aaa; line-height: 1.8;">
                    • Care <span style="color: #00d4aa;">reweights</span> energy landscape<br/>
                    • Cooperation = <span style="color: #00d4aa;">ground state</span><br/>
                    • Result: Synergies (beyond Pareto)
                </p>
            </div>
            <p style="font-size: 15px; color: #e0e0e0; margin-bottom: 6px;"><b>Example: YbCl₃</b></p>
            <p style="font-size: 16px; color: #e0e0e0; line-height: 1.8;">
                B1 (Host) = <span style="color: #00d4aa;">0.90</span><br/>
                B2 (Optical) = <span style="color: #00d4aa;">0.94</span><br/>
                B3 (Coherence) = <span style="color: #00d4aa;">0.90</span>
            </p>
            <p style="font-size: 14px; color: #aaa; margin-top: 10px;"><i>Beyond Pareto — everyone wins</i></p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: center; padding: 20px; background-color: #1e2130; border: 2px solid #00d4aa; border-radius: 8px; margin-top: 20px;">
        <span style="color: #00d4aa; font-size: 20px; font-weight: bold;">
            Care > 0.8 = Strong synergy across ALL properties
        </span>
        <div style="font-size: 13px; color: #666; margin-top: 10px;">
            Illustrative examples from orchestration pipeline test. Scores computed by H_total from real crystal structure data.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ========================================================================
    # WHY RESULTS CAN'T BE HALLUCINATED (from pitch deck slide 12)
    # ========================================================================

    st.header("Why Results Can't Be Hallucinated")

    st.markdown("""
    <div style="background-color: #1e2130; padding: 16px; border-radius: 10px; margin-bottom: 20px;">
        <p style="font-size: 17px; color: #aaa; text-align: center;">
            Baba rules trigger computation, not generation
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""<div style="display: flex; justify-content: center; align-items: center; gap: 20px; margin-bottom: 24px; flex-wrap: wrap;">
<div style="width: 240px; padding: 20px; background-color: #da77f215; border: 2px solid #da77f2; border-radius: 12px; text-align: center;">
<div style="font-size: 28px; margin-bottom: 8px;">🧠</div>
<div style="font-size: 17px; color: #da77f2; font-weight: 700;">LLM Creates Baba is Quantum Rule</div>
<div style="font-size: 14px; color: #aaa; margin-top: 8px;">Compositional grammar<br/>maps to operators</div>
</div>
<div style="font-size: 28px; color: #aaa;">→</div>
<div style="width: 240px; padding: 20px; background-color: #4dabf715; border: 2px solid #4dabf7; border-radius: 12px; text-align: center;">
<div style="font-size: 28px; margin-bottom: 8px;">⚙️</div>
<div style="font-size: 17px; color: #4dabf7; font-weight: 700;">H_total Computes</div>
<div style="font-size: 14px; color: #aaa; margin-top: 8px;">Mathematical<br/>operations</div>
</div>
<div style="font-size: 28px; color: #aaa;">→</div>
<div style="width: 240px; padding: 20px; background-color: #00d4aa15; border: 2px solid #00d4aa; border-radius: 12px; text-align: center;">
<div style="font-size: 28px; margin-bottom: 8px;">📊</div>
<div style="font-size: 17px; color: #00d4aa; font-weight: 700;">Results Calculated</div>
<div style="font-size: 14px; color: #aaa; margin-top: 8px;">Not generated—<br/>computed from physics</div>
</div>
</div>""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""<div style="padding: 20px; background-color: #0e1117; border: 1px solid #00d4aa44; border-radius: 10px; min-height: 180px;">
<div style="font-size: 16px; color: #00d4aa; font-weight: 700; margin-bottom: 10px;">✓ Computed by H_total (not LLM):</div>
<div style="font-size: 15px; color: #aaa; line-height: 1.8;">
8 operators — all computed, none generated:<br/>
Care · EQFT · Coherence · Scale Coupling · Boundary · +3
</div>
</div>""", unsafe_allow_html=True)

    with col2:
        st.markdown("""<div style="padding: 20px; background-color: #0e1117; border: 1px solid #2a2a3a; border-radius: 10px; min-height: 180px;">
<div style="font-size: 16px; color: #ff6b6b; font-weight: 700; margin-bottom: 10px;">If Routing Fails:</div>
<div style="font-size: 15px; color: #aaa; line-height: 1.8;">
• Wrong Baba rule → Operation fails visibly<br/>
• No silent errors — immediate feedback<br/>
• System self-corrects on next operation
</div>
</div>""", unsafe_allow_html=True)

    st.markdown("""<div style="text-align: center; padding: 20px; background-color: #1e2130; border: 2px solid #00d4aa; border-radius: 10px; margin-top: 20px;">
<span style="color: #00d4aa; font-size: 20px; font-weight: bold;">
The LLMs operate the mathematics — they don't generate the answers.
</span>
</div>""", unsafe_allow_html=True)

    st.markdown("---")

    # ========================================================================
    # BY THE NUMBERS
    # ========================================================================

    st.header("By the Numbers")

    st.markdown("""
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 16px;">
        <div style="background-color: #1e2130; padding: 20px; border-radius: 10px; text-align: center;">
            <div style="font-size: 14px; color: #888;">Compounds Evaluated</div>
            <div style="font-size: 32px; color: #00d4aa; font-weight: bold;">1,073</div>
        </div>
        <div style="background-color: #1e2130; padding: 20px; border-radius: 10px; text-align: center;">
            <div style="font-size: 14px; color: #888;">AI Agents</div>
            <div style="font-size: 32px; color: #4dabf7; font-weight: bold;">3</div>
        </div>
        <div style="background-color: #1e2130; padding: 20px; border-radius: 10px; text-align: center;">
            <div style="font-size: 14px; color: #888;">Properties Optimized</div>
            <div style="font-size: 32px; color: #da77f2; font-weight: bold;">3</div>
        </div>
        <div style="background-color: #1e2130; padding: 20px; border-radius: 10px; text-align: center;">
            <div style="font-size: 14px; color: #888;">Strategic Patterns</div>
            <div style="font-size: 32px; color: #ffd43b; font-weight: bold;">24+</div>
        </div>
    </div>
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px;">
        <div style="background-color: #1e2130; padding: 20px; border-radius: 10px; text-align: center;">
            <div style="font-size: 14px; color: #888;">Data Source</div>
            <div style="font-size: 18px; color: #e0e0e0; font-weight: bold;">Materials Project</div>
        </div>
        <div style="background-color: #1e2130; padding: 20px; border-radius: 10px; text-align: center;">
            <div style="font-size: 14px; color: #888;">Computation</div>
            <div style="font-size: 18px; color: #e0e0e0; font-weight: bold;">Real H_total</div>
        </div>
        <div style="background-color: #1e2130; padding: 20px; border-radius: 10px; text-align: center;">
            <div style="font-size: 14px; color: #888;">Hallucination</div>
            <div style="font-size: 18px; color: #00d4aa; font-weight: bold;">Zero</div>
            <div style="font-size: 11px; color: #666;">Rules trigger computation,<br/>not generation</div>
        </div>
        <div style="background-color: #1e2130; padding: 20px; border-radius: 10px; text-align: center;">
            <div style="font-size: 14px; color: #888;">Agent Behavior</div>
            <div style="font-size: 18px; color: #e0e0e0; font-weight: bold;">Operator</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ========================================================================
    # PLATFORM VALIDATION: PID CONTROL SYSTEMS (from pitch deck slide 7)
    # ========================================================================

    st.header("Platform Validation: Same Math. Different Domain.")

    st.markdown("""
<div style="font-size: 17px; color: #aaa; margin-bottom: 20px;">
    Speed OR Stability OR Accuracy — COGNISYN finds all three.
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div style="background-color: #1e2130; padding: 20px; border-radius: 10px; border-left: 6px solid #4dabf7; margin-bottom: 20px;">
    <p style="font-size: 17px; color: #e0e0e0; line-height: 1.8;">
        <b style="color: #4dabf7;">PID</b> (Proportional-Integral-Derivative) controllers are everywhere —
        thermostats, cruise control, drones, industrial automation. Every PID system faces the same
        "pick two" trade-off that plagues materials discovery.
    </p>
</div>
""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
<div style="background-color: #1e2130; padding: 28px; border-radius: 10px; border: 2px solid #ff6b6b; min-height: 320px;">
    <h4 style="color: #ff6b6b; font-size: 22px; margin-bottom: 16px;">Traditional PID Tuning</h4>
    <div style="display: flex; justify-content: center; gap: 18px; margin-bottom: 16px;">
        <div style="width: 80px; height: 80px; border-radius: 50%; background: #00d4aa; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <span style="font-size: 11px; color: #0a0a0f; font-weight: 600;">Speed</span>
            <span style="font-size: 13px; color: #0a0a0f; font-weight: 700;">HIGH</span>
        </div>
        <div style="width: 80px; height: 80px; border-radius: 50%; background: #00d4aa; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <span style="font-size: 11px; color: #0a0a0f; font-weight: 600;">Stability</span>
            <span style="font-size: 13px; color: #0a0a0f; font-weight: 700;">HIGH</span>
        </div>
        <div style="width: 80px; height: 80px; border-radius: 50%; background: #ff6b6b; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <span style="font-size: 11px; color: #0a0a0f; font-weight: 600;">Accuracy</span>
            <span style="font-size: 13px; color: #0a0a0f; font-weight: 700;">LOW</span>
        </div>
    </div>
    <div style="text-align: center; padding: 12px; background-color: #ff6b6b33; border-radius: 6px;">
        <span style="font-size: 16px; color: #ff6b6b; font-weight: 600;">"Pick two" — the engineer's dilemma</span>
    </div>
</div>
""", unsafe_allow_html=True)

    with col2:
        st.markdown("""
<div style="background-color: #1e2130; padding: 28px; border-radius: 10px; border: 2px solid #00d4aa; min-height: 320px;">
    <h4 style="color: #00d4aa; font-size: 22px; margin-bottom: 16px;">COGNISYN Care Equilibrium</h4>
    <div style="display: flex; justify-content: center; gap: 18px; margin-bottom: 16px;">
        <div style="width: 80px; height: 80px; border-radius: 50%; background: #00d4aa; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <span style="font-size: 11px; color: #0a0a0f; font-weight: 600;">Speed</span>
            <span style="font-size: 13px; color: #0a0a0f; font-weight: 700;">HIGH</span>
        </div>
        <div style="width: 80px; height: 80px; border-radius: 50%; background: #00d4aa; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <span style="font-size: 11px; color: #0a0a0f; font-weight: 600;">Stability</span>
            <span style="font-size: 13px; color: #0a0a0f; font-weight: 700;">HIGH</span>
        </div>
        <div style="width: 80px; height: 80px; border-radius: 50%; background: #00d4aa; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <span style="font-size: 11px; color: #0a0a0f; font-weight: 600;">Accuracy</span>
            <span style="font-size: 13px; color: #0a0a0f; font-weight: 700;">HIGH</span>
        </div>
    </div>
    <div style="text-align: center; padding: 12px; background-color: #00d4aa33; border-radius: 6px;">
        <span style="font-size: 16px; color: #00d4aa; font-weight: 600;">All three — Care finds the synergy</span>
    </div>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div style="background-color: #0e1117; border: 1px solid #2a2a3a; border-radius: 10px; padding: 16px 20px; margin-top: 16px;">
    <div style="display: grid; grid-template-columns: auto 1fr auto 1fr auto 1fr; gap: 6px 12px; font-size: 15px;">
        <span style="color: #4dabf7; font-weight: 600;">B1:</span>
        <span style="color: #aaa;">P-specialist → Speed</span>
        <span style="color: #da77f2; font-weight: 600;">B2:</span>
        <span style="color: #aaa;">I-specialist → Accuracy</span>
        <span style="color: #00d4aa; font-weight: 600;">B3:</span>
        <span style="color: #aaa;">D-specialist → Stability</span>
    </div>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div style="text-align: center; padding: 20px; background-color: #1e2130; border: 2px solid #da77f2; border-radius: 10px; margin-top: 20px;">
    <span style="color: #da77f2; font-size: 20px; font-weight: bold;">
        Same H_total. Same Care operator. Same Baba is Quantum grammar.<br/>
    </span>
    <span style="color: #aaa; font-size: 17px;">
        The math that discovers quantum materials also tunes control systems.
    </span>
</div>
""", unsafe_allow_html=True)

    st.markdown("---")

    # ========================================================================
    # MARKET EXPANSION: NOW → NEXT → FUTURE (from pitch deck slide 14)
    # ========================================================================

    st.header("Market Expansion: NOW → NEXT → FUTURE")

    st.markdown("""
Same H_total mathematics — different "pick two" problems
    """)

    # NOW
    st.markdown("""<div style="padding: 18px 24px; background-color: #00d4aa15; border: 2px solid #00d4aa; border-radius: 10px; margin-bottom: 16px;">
<div style="display: flex; align-items: center; gap: 16px; flex-wrap: wrap;">
<div style="font-size: 14px; font-weight: 700; background: #00d4aa; color: #0a0a0f; padding: 6px 14px; border-radius: 4px;">NOW</div>
<div style="flex: 1; min-width: 200px;">
<div style="font-size: 20px; color: #00d4aa; font-weight: 700;">Quantum Computing Materials</div>
<div style="font-size: 15px; color: #aaa; margin-top: 4px;">Host quality + Optical properties + Spin coherence — demo running</div>
</div>
<div style="text-align: right;">
<div style="font-size: 26px; color: #00d4aa; font-weight: 700;">$50B+</div>
<div style="font-size: 12px; color: #aaa;">by 2030</div>
</div>
</div>
</div>""", unsafe_allow_html=True)

    # NEXT
    st.markdown("""<div style="padding: 18px 24px; background-color: #4dabf715; border: 2px solid #4dabf7; border-radius: 10px; margin-bottom: 20px;">
<div style="display: flex; align-items: center; gap: 16px; flex-wrap: wrap;">
<div style="font-size: 14px; font-weight: 700; background: #4dabf7; color: #0a0a0f; padding: 6px 14px; border-radius: 4px;">NEXT</div>
<div style="flex: 1; min-width: 200px;">
<div style="font-size: 20px; color: #4dabf7; font-weight: 700;">Control Systems (PID)</div>
<div style="font-size: 15px; color: #aaa; margin-top: 4px;">Speed + Stability + Accuracy — framework designed, same H_total</div>
</div>
<div style="text-align: right;">
<div style="font-size: 26px; color: #4dabf7; font-weight: 700;">$350B+</div>
<div style="font-size: 12px; color: #aaa;">industrial + robotics</div>
</div>
</div>
</div>""", unsafe_allow_html=True)

    # FUTURE
    st.markdown("""
FUTURE — more "pick two" problems:
    """)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""<div style="padding: 16px; background-color: #0e1117; border: 1px solid #da77f244; border-radius: 8px; min-height: 100px;">
<div style="font-size: 16px; color: #da77f2; font-weight: 600;">Drug Discovery</div>
<div style="font-size: 14px; color: #aaa; margin-top: 6px;">Efficacy + Safety + Cost</div>
</div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div style="padding: 16px; background-color: #0e1117; border: 1px solid #ffd43b44; border-radius: 8px; min-height: 100px;">
<div style="font-size: 16px; color: #ffd43b; font-weight: 600;">Climate / Energy</div>
<div style="font-size: 14px; color: #aaa; margin-top: 6px;">Clean + Reliable + Affordable</div>
</div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div style="padding: 16px; background-color: #0e1117; border: 1px solid #00d4aa44; border-radius: 8px; min-height: 100px;">
<div style="font-size: 16px; color: #00d4aa; font-weight: 600;">Foundation Models</div>
<div style="font-size: 14px; color: #aaa; margin-top: 6px;">Capability + Alignment + Efficiency</div>
</div>""", unsafe_allow_html=True)

    st.markdown("""
*Today: 3 agents, 3 properties. **The math extends to N.***
    """)

    st.markdown("""<div style="text-align: center; padding: 20px; background-color: #1e2130; border: 2px solid #da77f2; border-radius: 10px; margin-top: 16px;">
<div style="font-size: 17px; color: #e0e0e0;">World models describe the terrain. Strategic intelligence navigates it.</div>
<div style="font-size: 19px; color: #da77f2; font-weight: 700; margin-top: 8px;">COGNISYN is the navigation layer — Care-guided exploration of possibility spaces.</div>
</div>""", unsafe_allow_html=True)

    st.markdown("---")

    # ========================================================================
    # ORCHESTRATION MONITOR
    # ========================================================================

    st.header("Orchestration Monitor")

    st.markdown("""
    Three agents — **B1 (Host Quality)**, **B2 (Optical)**, **B3 (Coherence)** — each run
    5 examples in parallel, building from single operations to multi-stage pipelines.
    """)

    st.subheader("Pipeline Test Code")
    st.markdown("Real orchestration calls — zero LLM tokens, cached Materials Project data, real H_total computation:")
    st.code('''# Setup: real mathematics, real memory, real validation
H = UnifiedStrategicMathematics()        # H_total Hamiltonian
m = DynamicMemoryArchitecture(agent_id)  # Episodic + strategic memory
v = OrchestrationValidator()             # Rule validation
b = OrchestrationBridge(H, m, v)         # Orchestration engine
b.materials_adapter = MaterialsProjectAdapter(use_cached=True)  # 1,073 Yb compounds

# SUPERPOSE — evaluate all compounds for host quality
rule = BabaIsQuantumRule(
    subject="COMPOUNDS", verb="SUPERPOSE",
    property="HOST-QUALITY", category="strategy"
)
result = await b.orchestrate_mathematics(rule, ctx, {'day': 6})
# → 1,073 compounds evaluated, 26 Care equilibria found

# FILTER → ENTANGLE — two-stage pipeline
rule_filter = BabaIsQuantumRule(
    subject="COMPOUNDS", verb="FILTER",
    property="I=0", category="strategy"
)
r_filter = await b.orchestrate_mathematics(rule_filter, ctx, {'day': 6})
# → 1,073 → 1,057 passed (i_zero > 0.3)

rule_entangle = BabaIsQuantumRule(
    subject="HOST-QUALITY", verb="ENTANGLE",
    property="CARE-SYNERGY", category="strategy"
)
r_entangle = await b.orchestrate_mathematics(rule_entangle, ctx, {'day': 6})
# → 26 synergy compounds: YbCl₃ (B1=0.90, B2=0.94, B3=0.90)

# INTERFERE — quantum pruning
rule = BabaIsQuantumRule(
    subject="COMPOUNDS", verb="INTERFERE",
    property="CARE-GUIDED", category="strategy"
)
result = await b.orchestrate_mathematics(rule, ctx, {'day': 6})
# → 1,073 → 25 compounds, all Care equilibria preserved''', language='python')

    col1, col2 = st.columns(2)
    with col1:
        st.image("dashboard_overview.png", caption="System overview: 5/5 examples, 3/3 agents, 1,073 compounds, 24 patterns")
    with col2:
        st.image("dashboard_b1_examples.png", caption="B1 (Host Quality): All 5 examples — SUPERPOSE through full pipeline")

    col1, col2 = st.columns(2)
    with col1:
        st.image("dashboard_b2_optical.png", caption="B2 (Optical): All 5 examples — evaluating from optical perspective")
    with col2:
        st.image("dashboard_b3_coherence.png", caption="B3 (Coherence): All 5 examples — evaluating from spin coherence perspective")

    st.markdown("""
    <div style="text-align: center; padding: 16px; background-color: #1e2130; border-radius: 8px;">
        <span style="font-size: 15px; color: #888;">
            Each agent evaluates from its own property perspective (host quality, optical, coherence).
            When all three score above threshold simultaneously, that's a Care equilibrium.
        </span>
        <div style="font-size: 13px; color: #666; margin-top: 8px;">
            Illustrative examples from orchestration pipeline test. Scores computed by H_total from real crystal structure data.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("")

    # Agent Learning: Core Memory Systems
    st.subheader("Agent Learning: Core Memory Systems")

    st.markdown("""
    As agents process examples, they accumulate episodic memories, discover strategic patterns,
    and invent new compositional rules — building cumulative intelligence across the pipeline.
    """)

    st.markdown("""
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 16px;">
        <div style="background-color: #1e2130; padding: 20px; border-radius: 10px; text-align: center;">
            <div style="font-size: 14px; color: #888;">Episodic Memory</div>
            <div style="font-size: 32px; color: #00d4aa; font-weight: bold;">100</div>
            <div style="font-size: 12px; color: #666;">episodes</div>
        </div>
        <div style="background-color: #1e2130; padding: 20px; border-radius: 10px; text-align: center;">
            <div style="font-size: 14px; color: #888;">Strategic Patterns</div>
            <div style="font-size: 32px; color: #4dabf7; font-weight: bold;">4</div>
            <div style="font-size: 12px; color: #666;">discovered</div>
        </div>
        <div style="background-color: #1e2130; padding: 20px; border-radius: 10px; text-align: center;">
            <div style="font-size: 14px; color: #888;">Rules Invented</div>
            <div style="font-size: 32px; color: #ffd43b; font-weight: bold;">5</div>
            <div style="font-size: 12px; color: #666;">Baba is Quantum</div>
        </div>
        <div style="background-color: #1e2130; padding: 20px; border-radius: 10px; text-align: center;">
            <div style="font-size: 14px; color: #888;">Total Memories</div>
            <div style="font-size: 32px; color: #ff6b6b; font-weight: bold;">106</div>
            <div style="font-size: 12px; color: #666;">accumulated</div>
        </div>
    </div>
    <div style="text-align: center; padding: 12px; background-color: #1e2130; border-radius: 8px;">
        <span style="font-size: 14px; color: #888;">
            Data from DynamicMemoryArchitecture checkpoint files — agents learn and retain knowledge across examples.
            Illustrative test run data.
        </span>
    </div>
    """, unsafe_allow_html=True)

    # Cumulative Intelligence: Dynamic Memory Architecture (from pitch deck slide 13)
    st.subheader("Cumulative Intelligence")

    st.markdown("""
Not ephemeral sessions — learning that persists
    """)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("""<div style="padding: 18px; background-color: #ff6b6b15; border: 1px solid #ff6b6b44; border-radius: 8px; margin-bottom: 14px;">
<div style="font-size: 17px; color: #ff6b6b; font-weight: 600;">The Problem</div>
<div style="font-size: 15px; color: #aaa; margin-top: 8px; line-height: 1.6;">Every LLM session starts from zero.<br/>Insights, patterns — all lost at context limit.</div>
</div>""", unsafe_allow_html=True)

        st.markdown("""<div style="padding: 18px; background-color: #00d4aa15; border: 1px solid #00d4aa44; border-radius: 8px;">
<div style="font-size: 17px; color: #00d4aa; font-weight: 600;">COGNISYN Solution</div>
<div style="font-size: 15px; color: #aaa; margin-top: 8px; line-height: 1.6;">Base LLM stays frozen.<br/>Learning via external memory + rules.</div>
</div>""", unsafe_allow_html=True)

    with col2:
        st.markdown("""<div style="text-align: center; font-size: 14px; color: #aaa; margin-bottom: 10px;">Dynamic Memory Architecture</div>
<div style="padding: 14px 18px; background-color: #4dabf722; border-left: 3px solid #4dabf7; border-radius: 8px; margin-bottom: 8px;">
<div style="font-size: 15px; color: #4dabf7; font-weight: 600;">Layer 1: Episodic Memory</div>
<div style="font-size: 13px; color: #aaa;">"What happened" — Experiences with amplitudes + phases</div>
</div>
<div style="text-align: center; font-size: 12px; color: #00d4aa; padding: 4px 0;">↓ Constructive: matching patterns reinforce ↓</div>
<div style="padding: 14px 18px; background-color: #00d4aa22; border-left: 3px solid #00d4aa; border-radius: 8px; margin-bottom: 8px;">
<div style="font-size: 15px; color: #00d4aa; font-weight: 600;">Layer 2: Strategic Memory</div>
<div style="font-size: 13px; color: #aaa;">"What works" — Successful patterns amplified</div>
</div>
<div style="text-align: center; font-size: 12px; color: #ff6b6b; padding: 4px 0;">↓ Destructive: conflicting patterns cancel ↓</div>
<div style="padding: 14px 18px; background-color: #da77f222; border-left: 3px solid #da77f2; border-radius: 8px;">
<div style="font-size: 15px; color: #da77f2; font-weight: 600;">Layer 3: Conceptual Memory</div>
<div style="font-size: 13px; color: #aaa;">"What it means" — Only coherent abstractions persist</div>
</div>""", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""<div style="text-align: center; padding: 12px;">
<div style="font-size: 16px; color: #00d4aa; font-weight: 600;">Learning</div>
<div style="font-size: 13px; color: #aaa;">Repeated patterns amplify</div>
</div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div style="text-align: center; padding: 12px;">
<div style="font-size: 16px; color: #ff6b6b; font-weight: 600;">No Overfitting</div>
<div style="font-size: 13px; color: #aaa;">Noise cancels out</div>
</div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div style="text-align: center; padding: 12px;">
<div style="font-size: 16px; color: #da77f2; font-weight: 600;">Generalization</div>
<div style="font-size: 13px; color: #aaa;">Only consistent patterns survive</div>
</div>""", unsafe_allow_html=True)

    st.markdown("""<div style="text-align: center; padding: 12px; margin-top: 8px;">
<span style="font-size: 15px; color: #4dabf7; font-style: italic;">One mechanism delivers all three — no hyperparameter tuning required</span>
</div>""", unsafe_allow_html=True)

    st.markdown("---")

    # ========================================================================
    # THE MATHEMATICAL FOUNDATION (from pitch deck slide 9)
    # ========================================================================

    st.header("The Mathematical Foundation")

    st.markdown("""
    <div style="padding: 24px; background-color: #1e2130; border: 2px solid #4dabf7; border-radius: 10px; margin-top: 20px; margin-bottom: 20px;">
        <div style="font-size: 16px; color: #4dabf7; font-weight: 700; text-align: center; margin-bottom: 16px;">
            MATHEMATICAL FOUNDATION: Real Quantum Formalism, Classical Compute
        </div>
        <div style="text-align: center; font-size: 18px; color: #e0e0e0; margin-bottom: 16px; font-family: 'Times New Roman', serif;">
            H<sub>total</sub> = H<sub>quantum</sub> + H<sub>classical</sub> + H<sub>coupling</sub> + H<sub>care</sub>
        </div>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px;">
            <div style="text-align: center; padding: 12px; background-color: #0e1117; border-radius: 8px; border: 1px solid #4dabf744;">
                <div style="font-size: 14px; color: #4dabf7; font-weight: 600;">Hilbert Space</div>
                <div style="font-size: 12px; color: #aaa; margin-top: 6px;">Complex amplitudes<br/>Normalized states<br/>Inner products</div>
            </div>
            <div style="text-align: center; padding: 12px; background-color: #0e1117; border-radius: 8px; border: 1px solid #da77f244;">
                <div style="font-size: 14px; color: #da77f2; font-weight: 600;">Hadamard Ops</div>
                <div style="font-size: 12px; color: #aaa; margin-top: 6px;">Grover search<br/>Bell states<br/>QFT basis</div>
            </div>
            <div style="text-align: center; padding: 12px; background-color: #0e1117; border-radius: 8px; border: 1px solid #00d4aa44;">
                <div style="font-size: 14px; color: #00d4aa; font-weight: 600;">Hermitian H</div>
                <div style="font-size: 12px; color: #aaa; margin-top: 6px;">H = H†<br/>Eigenvalues<br/>Ground states</div>
            </div>
            <div style="text-align: center; padding: 12px; background-color: #0e1117; border-radius: 8px; border: 1px solid #ffd43b44;">
                <div style="font-size: 14px; color: #ffd43b; font-weight: 600;">Interference</div>
                <div style="font-size: 12px; color: #aaa; margin-top: 6px;">Phase: e<sup>iφ</sup><br/>Constructive<br/>Destructive</div>
            </div>
        </div>
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

    **55,000 lines of code** · 2 years of AI-human collaboration
    """)


    # ========================================================================
    # FOOTER (formerly sidebar)
    # ========================================================================

    st.markdown("---")

    st.markdown("""
**Data Source:** [Materials Project](https://materialsproject.org/) — 150,000+ inorganic compounds, CC BY 4.0
    """)

    st.caption("Powered by COGNISYN · Built with Streamlit")


# ============================================================================
# RUN
# ============================================================================

if __name__ == "__main__":
    main()
