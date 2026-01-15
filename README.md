# COGNISYN: Yb-171 Host Materials Discovery

**Live Demo:** [cognisyn-demo.streamlit.app](https://cognisyn-demo.streamlit.app)

## Overview

COGNISYN discovers Yb-171 quantum computing **host materials** through quantum-inspired game theory.

**What are host materials?** Crystals we dope Yb-171 ions into (e.g., CaWO4:Yb3+ = Yb in calcium tungstate).

**Mission:** Find hosts where **host quality + optical properties + spin coherence** are ALL high—synergies beyond the Pareto frontier.

## The Problem

Current state-of-the-art materials each sacrifice at least one property:
- **YVO4:Yb3+** - Good host quality and optical, but V-51 spins kill coherence
- **Y2SiO5:Yb3+** - Good host quality, but Y-89 spins limit coherence
- **CaWO4:Yb3+** - Current best (0.15s coherence), but can we find better?

## Key Innovation

**Care equilibria** (synergies) beyond the Pareto frontier (trade-offs).

Classical methods accept "pick two" as physics. COGNISYN finds where ALL THREE are high.

## Running Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Contact

**Email:** tish@cognisyn.ai

---

**Key Message:** "Classical methods find trade-offs. COGNISYN discovers synergies."
