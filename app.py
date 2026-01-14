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

    # Custom CSS
    st.markdown("""
        <style>
        .main {background-color: #0e1117;}
        .stMetric {background-color: #1e2130; padding: 10px; border-radius: 5px;}
        h1, h2, h3 {color: #00ffff;}
        </style>
    """, unsafe_allow_html=True)

    # ========================================================================
    # HEADER
    # ========================================================================

    st.title("🔬 COGNISYN: Yb-171 Host Materials Discovery")

    st.info("📺 **Preview demo.** Schedule a live demo below to see real-time discovery.")

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
        <div style="background-color: #1e2130; padding: 20px; border-radius: 10px; border-left: 5px solid #ff6b6b; height: 200px;">
            <h4 style="color: #4dabf7;">YVO₄:Yb³⁺</h4>
            <p>✓ Host Quality<br/>✓ Optical Properties<br/><span style="color: #ff6b6b;">✗ Spin Coherence</span></p>
            <p style="font-size: 12px; color: #888;"><i>V-51 (I=7/2, 99.75%) creates magnetic noise</i></p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style="background-color: #1e2130; padding: 20px; border-radius: 10px; border-left: 5px solid #ff6b6b; height: 200px;">
            <h4 style="color: #4dabf7;">Y₂SiO₅:Yb³⁺</h4>
            <p>✓ Host Quality (320 Hz linewidth)<br/>~ Optical Properties<br/><span style="color: #ff6b6b;">✗ Spin Coherence</span></p>
            <p style="font-size: 12px; color: #888;"><i>Y-89 (I=1/2, 100%) limits T₂ times</i></p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div style="background-color: #1e2130; padding: 20px; border-radius: 10px; border-left: 5px solid #ffd43b; height: 200px;">
            <h4 style="color: #4dabf7;">CaWO₄:Yb³⁺</h4>
            <p>✓ Host Quality<br/>~ Optical Properties<br/>✓ Spin Coherence (0.15s)</p>
            <p style="font-size: 12px; color: #888;"><i>Best so far—W/Ca mostly I=0. Can we find better?</i></p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: center; padding: 16px; background-color: #1e2130; border-radius: 8px; margin-top: 16px;">
        <span style="color: #00d4aa; font-size: 18px; font-weight: bold;">COGNISYN searches systematically for hosts where ALL THREE are high</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ========================================================================
    # SCHEDULE LIVE DEMO
    # ========================================================================

    st.header("🎯 Schedule a Live Demo")

    st.markdown("""
    **In a live demo you'll see:** Real-time quantum operations · 1,073 → 25 → 1 optimal material · 60-day continuous learning

    **Contact:** tish@cognisyn.ai | Virtual (30 min) or In-Person (1 hour)
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
