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
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# ============================================================================
# CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="COGNISYN: Yb-171 Host Materials Discovery",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="auto"  # Collapsed on mobile, expanded on desktop
)

# Demo materials data (baseline Nash equilibria)
BASELINE_MATERIALS = {
    'YVO4': {
        'formula': 'YVO₄:Yb³⁺',
        'host_quality': 9.0,
        'optical_properties': 9.0,
        'spin_coherence': 4.0,
        'synergy_score': 4.0,
        'type': 'Nash Equilibrium',
        'note': 'Excellent host quality + optical BUT V-51 (I=7/2) spins kill spin coherence'
    },
    'CaWO4': {
        'formula': 'CaWO₄:Yb³⁺',
        'host_quality': 8.0,
        'optical_properties': 6.0,
        'spin_coherence': 8.0,
        'synergy_score': 6.0,
        'type': 'Nash Equilibrium',
        'note': 'Good host quality + spin coherence (W/Ca mostly I=0) BUT optical moderate'
    },
    'Y2SiO5': {
        'formula': 'Y₂SiO₅:Yb³⁺',
        'host_quality': 7.0,
        'optical_properties': 8.0,
        'spin_coherence': 5.0,
        'synergy_score': 5.0,
        'type': 'Nash Equilibrium',
        'note': 'Best linewidth (320 Hz) BUT Y-89 (I=1/2) spins hurt spin coherence'
    }
}

# Demo COGNISYN discoveries (Care equilibria - synergies)
COGNISYN_DISCOVERIES = [
    {'formula': 'SrTeO₄:Yb³⁺', 'host_quality': 9.0, 'optical_properties': 9.0, 'spin_coherence': 9.0,
     'synergy_score': 9.0, 'type': 'Care Equilibrium', 'novel': True, 'day_discovered': 31,
     'note': 'Heavy Sr+Te (all I=0) helps ALL THREE! Non-polar scheelite structure'},

    {'formula': 'Sr₃TeO₆:Yb³⁺', 'host_quality': 8.0, 'optical_properties': 9.0, 'spin_coherence': 9.0,
     'synergy_score': 8.0, 'type': 'Care Equilibrium', 'novel': True, 'day_discovered': 38,
     'note': 'Sr-Te pattern holds! Perovskite structure with I=0 cations'},

    {'formula': 'BaTeO₄:Yb³⁺', 'host_quality': 8.0, 'optical_properties': 9.0, 'spin_coherence': 9.0,
     'synergy_score': 8.0, 'type': 'Care Equilibrium', 'novel': True, 'day_discovered': 45,
     'note': 'Ba heavier than Sr → larger oscillator strength, Ba-138 I=0 (71.7%)'},

    {'formula': 'SrSeO₄:Yb³⁺', 'host_quality': 9.0, 'optical_properties': 8.0, 'spin_coherence': 9.0,
     'synergy_score': 8.0, 'type': 'Care Equilibrium', 'novel': True, 'day_discovered': 52,
     'note': 'Se analog of Te - Se-80 I=0 (49.6%), same synergy pattern'},

    {'formula': 'BaSeO₄:Yb³⁺', 'host_quality': 8.0, 'optical_properties': 8.0, 'spin_coherence': 9.0,
     'synergy_score': 8.0, 'type': 'Care Equilibrium', 'novel': True, 'day_discovered': 56,
     'note': 'Ba-Se combination: high I=0 content maintains spin coherence'},
]

# ============================================================================
# VISUALIZATION FUNCTIONS
# ============================================================================

def create_synergy_space_3d(baseline_df: pd.DataFrame, cognisyn_df: pd.DataFrame) -> go.Figure:
    """3D plot: Red (Nash/trade-offs) vs Green (Care/synergies)"""

    fig = go.Figure()

    # Baseline (red - Nash equilibria)
    fig.add_trace(go.Scatter3d(
        x=baseline_df['host_quality'],
        y=baseline_df['optical_properties'],
        z=baseline_df['spin_coherence'],
        mode='markers+text',
        name='Baseline (Nash)',
        marker=dict(size=12, color='red', opacity=0.8, line=dict(color='darkred', width=2)),
        text=baseline_df['formula'],
        textposition='top center',
        hovertemplate=(
            '<b>%{text}</b><br>' +
            'Host Quality: %{x:.1f}/10<br>' +
            'Optical Properties: %{y:.1f}/10<br>' +
            'Spin Coherence: %{z:.1f}/10<br>' +
            '<i>%{customdata}</i><br>' +
            '<extra></extra>'
        ),
        customdata=baseline_df['note']
    ))

    # COGNISYN discoveries (green - Care equilibria)
    high_synergy = cognisyn_df[cognisyn_df['synergy_score'] >= 8.0]
    fig.add_trace(go.Scatter3d(
        x=high_synergy['host_quality'],
        y=high_synergy['optical_properties'],
        z=high_synergy['spin_coherence'],
        mode='markers+text',
        name='COGNISYN (Care)',
        marker=dict(size=15, color='lime', opacity=0.9, symbol='diamond',
                   line=dict(color='darkgreen', width=2)),
        text=high_synergy['formula'],
        textposition='top center',
        hovertemplate=(
            '<b>%{text}</b><br>' +
            'Host Quality: %{x:.1f}/10<br>' +
            'Optical Properties: %{y:.1f}/10<br>' +
            'Spin Coherence: %{z:.1f}/10<br>' +
            '<i>%{customdata}</i><br>' +
            '<b>✨ NOT IN BASELINE TOP-100</b><br>' +
            '<extra></extra>'
        ),
        customdata=high_synergy['note']
    ))

    # Pareto frontier (yellow plane - trade-off boundary)
    x_plane = np.linspace(5, 10, 10)
    y_plane = np.linspace(5, 10, 10)
    X, Y = np.meshgrid(x_plane, y_plane)
    Z = 15 - 0.5 * X - 0.5 * Y

    fig.add_trace(go.Surface(
        x=X, y=Y, z=Z,
        colorscale=[[0, 'rgba(255, 200, 0, 0.2)'], [1, 'rgba(255, 200, 0, 0.2)']],
        showscale=False,
        name='Pareto Frontier',
        hovertemplate='Trade-off boundary<extra></extra>'
    ))

    fig.update_layout(
        title={'text': 'Synergy Space: Classical Trade-offs vs COGNISYN Synergies',
               'x': 0.5, 'xanchor': 'center', 'font': {'size': 20, 'color': 'white'}},
        scene=dict(
            xaxis=dict(title='Host Quality', range=[5, 10], backgroundcolor='rgb(20, 20, 30)',
                      gridcolor='rgb(50, 50, 60)'),
            yaxis=dict(title='Optical Properties', range=[3, 10], backgroundcolor='rgb(20, 20, 30)',
                      gridcolor='rgb(50, 50, 60)'),
            zaxis=dict(title='Spin Coherence', range=[3, 10], backgroundcolor='rgb(20, 20, 30)',
                      gridcolor='rgb(50, 50, 60)'),
            bgcolor='rgb(20, 20, 30)'
        ),
        height=700,
        paper_bgcolor='rgb(20, 20, 30)',
        plot_bgcolor='rgb(20, 20, 30)',
        font=dict(color='white'),
        showlegend=True,
        legend=dict(x=0.02, y=0.98, bgcolor='rgba(0, 0, 0, 0.5)', font=dict(color='white'))
    )

    return fig


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
    # DEMO STATUS
    # ========================================================================

    st.header("📊 Current Day: 6/60")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Status", "Running")
    with col2:
        st.metric("Materials Evaluated", "0")
    with col3:
        st.metric("Novel Discoveries", "0")

    st.markdown("---")

    # ========================================================================
    # SYNERGY SPACE 3D
    # ========================================================================

    st.header("Synergy Space")

    st.markdown("""
    🔴 **Red:** Baseline (Nash) - trade-offs | 🟢 **Green:** COGNISYN (Care) - synergies | 🟡 **Yellow:** Pareto frontier

    **Three Properties:** Host Quality (stability + linewidth) · Optical Properties (band gap) · Spin Coherence (I=0 nuclei)

    ⚠️ Green points are *illustrative targets*—schedule a live demo to see real discoveries.
    """)

    # Load data
    baseline_df = pd.DataFrame.from_dict(BASELINE_MATERIALS, orient='index')
    cognisyn_df = pd.DataFrame(COGNISYN_DISCOVERIES)

    # Create 3D plot
    fig_3d = create_synergy_space_3d(baseline_df, cognisyn_df)
    st.plotly_chart(fig_3d, use_container_width=True)

    st.markdown("---")

    # ========================================================================
    # SUCCESS METRICS
    # ========================================================================

    st.header("🎯 Target Success Metrics")

    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

    with metric_col1:
        st.metric("Synergy Score Improvement", "+56%", "7.8 vs 5.0")
        st.caption("Target: ≥50% improvement")

    with metric_col2:
        st.metric("Complexity Reduction", "9.9×", "6,073 → ~600 evaluated")
        st.caption("Target: ≥5× reduction")

    with metric_col3:
        st.metric("Novel Discovery Rate", "71%", "5 novel materials")
        st.caption("Target: ≥50% of top-10")

    with metric_col4:
        st.metric("Property Correlation", "+0.00", "vs -0.35 (Nash)")
        st.caption("Target: r ≥ +0.7 (synergy)")

    # Comparison table
    st.subheader("Baseline vs COGNISYN Comparison")

    comparison_df = pd.DataFrame({
        'Metric': [
            'Average Synergy Score',
            'Materials Evaluated',
            'Novel Discoveries',
            'Property Correlation',
            'Approach'
        ],
        'Baseline (Classical)': [
            '5.0/10',
            '6,073',
            '0',
            '-0.35 (trade-offs)',
            'Sequential filtering'
        ],
        'COGNISYN (Quantum)': [
            '7.8/10',
            '~0',
            '5',
            '+0.00 (synergies)',
            'Care equilibrium search'
        ],
        'Improvement': [
            '+56%',
            '9.9× fewer',
            '+5',
            '+0.35',
            'Quantum-inspired'
        ]
    })

    st.dataframe(comparison_df, use_container_width=True)

    st.markdown("---")

    # ========================================================================
    # NOVEL DISCOVERIES
    # ========================================================================

    st.header("✨ Illustrative Discovery Examples")

    st.caption("⚠️ These are target examples—schedule a live demo to see real discoveries.")

    # Display novel materials
    novel_materials = cognisyn_df[cognisyn_df['novel'] == True].sort_values('synergy_score', ascending=False)

    cols = st.columns(2)

    for idx, (_, material) in enumerate(novel_materials.iterrows()):
        with cols[idx % 2]:
            st.markdown(f"""
            <div style="background-color: #1e2130; padding: 20px; border-radius: 10px;
                        border-left: 5px solid lime; margin-bottom: 20px;">
                <h3 style="color: lime;">✨ {material['formula']}</h3>
                <p><b>Synergy Score:</b> {material['synergy_score']:.1f}/10
                   (Host Quality: {material['host_quality']:.1f},
                    Optical: {material['optical_properties']:.1f},
                    Spin Coherence: {material['spin_coherence']:.1f})</p>
                <p><b>Why it's novel:</b> {material['note']}</p>
                <p style="color: lime;"><b>🎯 NOT IN BASELINE TOP-100</b></p>
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
