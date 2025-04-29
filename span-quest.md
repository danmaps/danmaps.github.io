### Span Quest — MVP specification (2025-04)

---

#### Purpose  
Span Quest is a **hands-on physics sandbox** that teaches the fundamentals of overhead-line routing:

* **Mechanical insight** Players see how span length, conductor tension, and ground profile control the line’s shape.  
* **Engineering trade-offs** Cost‐per-pole, clearance rules, and departure-angle limits introduce real-world constraints.  
* **Visual intuition** Live geometry, hover read-outs, and draggable terrain let users experiment and immediately observe cause → effect.

The game is equally useful as a quick classroom demo (“Why do we need more poles on steep slopes?”) and as an informal design sketchpad.

---

#### Core loop  

1. **Terrain**  
   * Autogenerates a mix of flat and gently hilly sections.  
   * White *handles* appear on hover; drag vertically to reshape the ground in real time.
2. **Parameters** (checkbox = toggle)  
   * ▢ **Max span** (default 100 ft)  
   * ▢ **Max departure angle** (default 11 °)  
   * ▢ **Ground clearance** (default 25 ft)  
   * ▢ **Budget** (pole cost × count ≤ $20 000)  
   * **Tension slider** 20–100 kN → lower sag; or enable **Straight mode (∞ tension)** for chord-only lines.
3. **Pole placement**  
   * Fixed **start** and **end** poles frame the problem.  
   * Player clicks above the ground to add interior poles; cost and active rules validate instantly.
4. **Live feedback**  
   * Hover a pole: green labels show left/right departure angles and adjacent span lengths.  
   * Optional **Show failures** checkbox overlays red highlights on rule-breaking spans.
5. **Iteration**  
   * Drag terrain, move tension, add/remove poles until every checked rule is satisfied—or uncheck rules to simply explore.

---

#### Key mechanics & visuals  

| Feature | How it works |
|---------|--------------|
| **Departure angle** | Straight-mode → chord slope; finite-tension → tangent of a parabolic sag ( sag ≈ L²/8T ). |
| **Clearance** | Mid-span conductor vs. editable ground profile. |
| **Budget** | Pole cost ($1 k) × (interior poles) must stay ≤ cap. |
| **Handles** | Every 40 px ground vertex; hover to reveal ⬤, drag to reshape. |
| **Straight mode** | Sets T → ∞; conductor renders as neon-blue segments with zero sag. |
| **UI palette** | CAD-style black canvas, cyan poles, blue conductor, green metrics, red violations (toggle). |

---

#### Learning outcomes  

| Concept demonstrated | Player experience |
|----------------------|-------------------|
| **Catenary vs. chord** | Slide the tension slider to watch sag flatten toward the straight-line case. |
| **Span vs. clearance** | Stretch a span over a valley—ground-clearance violations appear first. |
| **Angle limits on switch hardware** | Increase ground slope; departure angles spike past the 11 ° default cap. |
| **Cost optimisation** | Disable clearance, then minimise pole count under the span-length rule; re-enable clearance to see the added cost of safe design. |

---

#### Technical snapshot  

* **HTML + Canvas + Vanilla JS** (≈ 500 LOC).  
* Ground stored as 1-D array; conductor drawn either as quadratic Bézier (parabolic approximation) or straight segment.  
* All geometry runs in < 16 ms per interaction on a 2020-era laptop—no libraries required.

---

#### What’s intentionally *not* in the MVP  

* True catenary math (can replace the parabola later).  
* Wind/temperature loading, differential conductor weights.  
* Automatic pole recommendations or optimisation.  
* Multi-layer vegetation modelling (handles removed for simplicity).

This scope keeps the first deliverable lean, playable in a browser, and rich enough to demonstrate the core physics and planning trade-offs of overhead-line design.