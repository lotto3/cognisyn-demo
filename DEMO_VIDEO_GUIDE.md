# COGNISYN Demo Video Production Guide

**Goal:** 3-minute silent screen recording of the Streamlit demo app with AI voiceover
**Format:** MP4, 1080p, under 100MB
**For:** YC Application — "Anything that shows us how the product works"

---

## Phase 1: Generate the AI Voiceover

### Step 1: Go to ElevenLabs
- Open https://elevenlabs.io
- Sign up or log in (free tier gives enough minutes)
- Go to **Text to Speech** (in the left sidebar)

### Step 2: Choose a Voice
- Pick a clear, professional voice — "Rachel" or "Adam" work well
- Set **Stability** to ~60% and **Clarity** to ~80% for a natural, authoritative tone
- Set speed to slightly slower than default — viewers need time to absorb technical content

### Step 3: Generate the Voiceover

**Important:** ElevenLabs supports `<break time="1.5s"/>` tags to insert silence directly into the audio. This is how we build in visual breathing space — the audio itself pauses where you need time to scroll or let the viewer absorb what's on screen.

Paste this script exactly as-is (including the break tags). The `<!-- SCROLL -->` comments are for YOUR reference only — delete them before pasting, or leave them in (ElevenLabs will ignore them). They tell you what to scroll to during each silence.

```
COGNISYN finds solutions where all objectives are high simultaneously. Not trade-offs, but genuine synergies. Classical optimization says pick two out of three. Our Care operator, built on quantum game theory running on classical compute, finds states where all three synergize.

<break time="2.0s"/>
<!-- SCROLL: down to "The Problem" — three material cards -->

Here's the problem. The best known quantum computing host materials each excel at one or two properties, but sacrifice the rest. YVO4 has excellent host quality — but poor optical properties. Y2SiO5 has strong optical performance — but weak spin coherence. Every current material is a compromise.

<break time="2.0s"/>
<!-- SCROLL: down to "How It Works" — three agents + operator tags -->

COGNISYN approaches this differently. Three AI agents — each operating as a mathematical physics operator through the Baba is Quantum grammar. 23 operators access the full H total Hamiltonian. The grammar is compositional: subject, verb, property maps to a mathematical operation. The language emerges bottom-up — agents discover what works through doing.

<break time="2.0s"/>
<!-- SCROLL: down to "LLMs as Strategic Operators" — Most AI vs COGNISYN -->

This is the key distinction. Most AI uses LLMs as knowledge repositories — query in, answer out. COGNISYN uses LLMs as strategic operators. The LLM creates a rule, H total computes the result, and discovery follows.

<break time="2.0s"/>
<!-- SCROLL: down to "Pipeline Output" — SUPERPOSE, FILTER, INTERFERE results -->

The pipeline builds in stages. SUPERPOSE identifies 26 Care equilibria from over a thousand compounds. FILTER and ENTANGLE detect synergies — YbCl3 scores 0.90 for B1, 0.94 for B2, and 0.90 for B3. INTERFERE prunes to 25 top candidates with zero false negatives.

<break time="2.0s"/>
<!-- SCROLL: down to "Care vs Nash" — YbBr2 vs YbCl3 score comparison -->

Compare YbBr2, the Nash equilibrium, with YbCl3, the Care equilibrium. YbBr2 has one strong property and two weak ones — the classical trade-off. YbCl3 has all three above 0.90. That's a synergy beyond the Pareto frontier.

<break time="1.5s"/>
<!-- SCROLL: down to "By the Numbers" — metrics grid -->

1,073 compounds evaluated. Three AI agents. Zero hallucination — the LLM creates the rules, but H total computes the results.

<break time="1.5s"/>
<!-- SCROLL: down to "PID Platform Validation" — red vs green circles -->

The math is domain-agnostic. The same Care operator that discovers quantum materials also tunes PID controllers. Speed, stability, and accuracy — all high.

<break time="2.0s"/>
<!-- SCROLL: down to "Market Expansion" — NOW, NEXT, FUTURE -->

Quantum materials is the first application — a 50 billion dollar market. Next is PID control — 350 billion in industrial and robotics. The same mathematics extends to drug discovery, climate and energy, even foundation model alignment. Today it's 3 agents, 3 properties. The math extends to N.

<break time="2.0s"/>
<!-- SCROLL: down to "Orchestration Monitor" — dashboard screenshots -->

This is the real orchestration pipeline running three agents across five examples each.

<break time="2.0s"/>
<!-- SCROLL: down to "Agent Learning" + "Cumulative Intelligence" -->

The agents don't start over each session. COGNISYN's memory architecture has three layers: episodic memory records what happened, strategic memory amplifies what works, and conceptual memory retains only coherent abstractions. One mechanism delivers learning, prevents overfitting, and enables generalization.

<break time="2.0s"/>
<!-- SCROLL: down to "A Different Mathematics" — hidden premise + annealing analogy -->

Why does classical optimization force these trade-offs? It's a hidden premise — a mathematical assumption, not a physics limit. Just as simulated annealing borrows from metallurgy without molten metal, COGNISYN borrows from quantum mechanics without qubits.

<break time="2.0s"/>
<!-- SCROLL: down to "The Stag Hunt" — game theory explanation -->

The Stag Hunt makes this intuitive. Two hunters can cooperate to catch a stag — high reward, but risky. Or each hunts a hare alone — low reward, but guaranteed. The rational choice is hare. Both end up worse off. That's the Nash equilibrium. COGNISYN's quantum game theory finds the cooperative state — where hunting stag isn't risky, it's the ground state.

<break time="2.0s"/>
<!-- SCROLL: down to "Why Results Can't Be Hallucinated" — 3-stage flow -->

And critically — these results can't be hallucinated. The LLM creates a Baba rule. H total computes the result mathematically. The LLM operates the mathematics — it doesn't generate the answers.

<break time="1.5s"/>
<!-- SCROLL: down to "The Mathematical Foundation" — H_total components -->

The mathematical foundation is real quantum formalism running on classical compute. H total equals H quantum plus H classical plus H coupling plus H care. Hilbert space, Hadamard operations, Hermitian operators, and interference — all implemented in 55,000 lines of production code.

<break time="2.0s"/>
```

**Before pasting:** Remove the `<!-- SCROLL -->` comment lines — they're instructions for you, not for the AI voice. The final text ElevenLabs sees should just be narration paragraphs separated by `<break>` tags.

### Step 4: Download
- Click **Generate**
- Listen through — if any words sound wrong, adjust the text (e.g., if "YbCl3" sounds garbled, try "Ytterbium Chloride 3" or "Y-b-C-l-3"; if "H total" sounds odd, try "H-total")
- **Check total duration:** Should be approximately 2:45 to 3:00 including the silences
- If it's over 3:00: reduce all break times by 0.5s (to 1.0-1.5s), or speed up voice slightly
- If it's under 2:30: increase breaks by 0.5s each
- Download as MP3
- Save to your Desktop as `cognisyn_voiceover.mp3`

---

## Phase 2: Prepare the Screen

### Step 5: Open the Demo App
```bash
open https://cognisyn-demo.streamlit.app/
```
Wait for it to fully load. If Streamlit Cloud is slow, run locally instead:
```bash
cd /Users/ogl3/repos/cognisyn-demo && python3 -m streamlit run app.py
```

### Step 6: Browser Setup
- Use **Chrome** or **Safari** in full screen (Cmd+Ctrl+F)
- Set zoom to **90%** (Cmd+minus) — this shows more content per screen and reduces scrolling
- Close all other tabs — a single clean tab
- Hide the bookmarks bar (Cmd+Shift+B in Chrome)
- Scroll to the very top of the page
- **Collapse the sidebar** if it's open (click the X)

### Step 7: Clean Your Desktop
- Close all notifications (Do Not Disturb: Focus → Do Not Disturb in Control Center)
- Hide the Dock (System Settings → Desktop & Dock → Automatically hide and show the Dock)
- No other apps visible

---

## Phase 3: Record

### Step 8: Practice with the Voiceover
- Put on headphones
- Play `cognisyn_voiceover.mp3` all the way through
- You'll hear: narration → **silence** → narration → **silence** → ...
- **The silences are your scroll windows.** When the voice goes quiet, that's when you scroll to the next section.
- Practice once with the app open — no recording. Just scroll along to get the feel.

**The rhythm (15 sections, ~3 min total):**
1. Header / mission → **2s** → scroll to The Problem
2. The Problem → **2s** → scroll to How It Works + operator tags
3. How It Works → **2s** → scroll to LLMs as Strategic Operators
4. Strategic Operators → **2s** → scroll to Pipeline Output
5. Pipeline Output → **2s** → scroll to Care vs Nash
6. Care vs Nash → **1.5s** → scroll to By the Numbers
7. By the Numbers → **1.5s** → scroll to PID Platform Validation
8. PID circles → **2s** → scroll to Market Expansion
9. Market Expansion → **2s** → scroll to Orchestration Monitor
10. Orchestration Monitor → **2s** → scroll to Agent Learning + Cumulative Intelligence
11. Cumulative Intelligence → **2s** → scroll to A Different Mathematics
12. A Different Mathematics → **2s** → scroll to Stag Hunt
13. Stag Hunt → **2s** → scroll to Why Can't Hallucinate
14. Why Can't Hallucinate → **1.5s** → scroll to Mathematical Foundation
15. Mathematical Foundation → **2s** → hold, done

### Step 9: Record the Screen
1. Open **QuickTime Player** (Cmd+Space → "QuickTime")
2. File → **New Screen Recording**
3. Click the **dropdown arrow** next to the record button
4. Set **Microphone: None** (we want silent video — audio gets added in iMovie)
5. Click **Record**
6. Click your screen (to record the full screen, not a selection)
7. **Immediately start playing the voiceover in your headphones** (open the MP3 in another QuickTime window or Music app, press play)
8. **Scroll during the silences:**
   - When the voice is talking → **hold still** on the current section
   - When the voice goes silent → **scroll smoothly** to the next section (trackpad two-finger scroll is smoother than mouse wheel)
   - Arrive at the next section before the voice starts again
   - The built-in 2.5-3 sec silences give you plenty of time to scroll
9. After the final narration, hold on the Orchestration Monitor dashboards for the remaining 3 seconds of silence
10. Press **Cmd+Ctrl+Esc** to stop recording

### Step 10: Review the Raw Recording
- QuickTime will open the video automatically
- Play it through — check that:
  - The scroll pace feels natural, not rushed
  - Each section is visible for long enough to read the key points
  - No UI glitches, loading spinners, or stray notifications appeared
- If anything looks off, re-record — it only costs 3 minutes

---

## Phase 4: Combine Video + Audio

### Step 11: Open iMovie
1. Open **iMovie** (Cmd+Space → "iMovie")
2. Click **Create New** → **Movie**

### Step 12: Import Media
1. File → **Import Media**
2. Select your screen recording (in Movies folder or Desktop — QuickTime saves to Movies by default)
3. Also import `cognisyn_voiceover.mp3` from your Desktop
4. Drag the **video** to the timeline first (top track)
5. Drag the **audio** below it (audio track)

### Step 13: Sync and Trim
- Since you scrolled to match the voiceover in real time, they should already be in sync
- Play through and check. The voice should be describing what's on screen.
- **Align the start:** If you started the voiceover a second or two after the screen recording began, drag the audio track right so the first words line up with the header being visible. Or trim the silent start off the video: click the video clip, drag the left edge inward to cut the dead start.
- **Trim the end:** Drag the end of both clips inward to cut any extra silence after the last section
- **Target total: 2:30 to 3:00**

### Step 14: Optional Polish
- **Fade in:** Select the video clip → click the tiny circle at the start → drag right to create a 0.5s fade-in
- **Fade out:** Same at the end
- **Title card (optional):** You could add a 3-second title at the start: "COGNISYN — Demo" — but the app header already serves this purpose, so skip if short on time

### Step 15: Export
1. File → **Share** → **File**
2. Resolution: **1080p**
3. Quality: **High** (not Best — keeps file size down)
4. Click **Next** → save as `cognisyn_demo_video.mp4`
5. **Check file size** — should be 20-50MB for a 3-minute 1080p video, well under the 100MB limit
6. **Check duration** — must be under 3 minutes

---

## Phase 5: Final Check

### Step 16: Watch the Final Video
- Play `cognisyn_demo_video.mp4` in QuickTime
- Ask yourself:
  - Can someone who's never heard of COGNISYN follow what's happening?
  - Are the pipeline numbers (1,073 → 26 → 25) visible long enough to register?
  - Does the PID section clearly show "this isn't just materials"?
  - Is the ending strong? (Dashboard showing real system running)
- If yes: upload to YC demo video slot

---

## Tips for a Stronger Video

- **Smooth scrolling matters.** Trackpad scroll is smoother than mouse wheel. Practice the full scroll path once before recording.
- **Scroll ONLY during silences.** The break tags create clear windows for scrolling. When the voice is talking, the screen should be still so the viewer can read.
- **Don't scroll during key numbers.** When the voiceover says "1,073 compounds" or "scores 0.90", the viewer should be looking at those exact numbers on screen.
- **The PID section is the wow moment.** It's where the viewer realizes this isn't a single-domain tool. The 3-second silence after it lets the red-vs-green circles sink in.
- **Skip the bottom half.** The educational sections (Stag Hunt, Mathematical Foundation) are for people browsing the app. The demo video should end after the Orchestration Monitor.
- **If the voiceover feels too fast,** regenerate it at 0.85x speed in ElevenLabs. A calm, measured pace is more authoritative than a rushed one.
- **If the silences feel too short for scrolling,** increase the break times from 3.0s to 4.0s and regenerate.
- **Browser zoom at 90%** means fewer scroll stops and smoother transitions between sections.
- **Do a practice run first.** Play the audio in headphones, scroll the app, don't record. Get comfortable with the rhythm. Then record on the second pass.
