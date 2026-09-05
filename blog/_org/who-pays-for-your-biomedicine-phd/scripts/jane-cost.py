#!/usr/bin/env python3
"""Stacked bar of what a graduate student costs, for the "Who Pays for Your
(Biomedicine) PhD?" post. Regenerate with:

  uv run --with matplotlib --with seaborn --with pandas --with numpy \
    --with cycler --with palettable --with statsmodels --with scipy \
    python3 blog/_org/who-pays-for-your-biomedicine-phd/scripts/jane-cost.py

Writes ../figures/jane-cost.{png,svg}, next to this script. The post references
figures/jane-cost.png; org-to-post.sh copies it into assets/images/blog/.
Needs the data-viz project at /Users/ilya/projects/dataviz/python.
"""
import os, sys; sys.path.insert(0, "/Users/ilya/projects/dataviz/python")
import dvstyle, palettes
import matplotlib.pyplot as plt
import numpy as np

# Assumptions, all from the 27 Aug 2026 ARPA-H STTR budget unless noted:
#   salary   $40,000, escalating 3%/yr (sheet: 40000 -> 41200 -> 42436 -> 43709)
#   fringe   11.9% of salary (sheet cell B52)
#   tuition  $5,277/semester = $10,554/yr, escalating 2%/yr (sheet's own escalation)
#   bench    $17,500/yr, the midpoint of the $15-20k rule of thumb, escalating 3%/yr
YEARS = np.arange(1, 6)
salary = 40000 * 1.03 ** (YEARS - 1)
fringe = salary * 0.119
tuition = 10554 * 1.02 ** (YEARS - 1)
bench = 17500 * 1.03 ** (YEARS - 1)

parts = [
    ("Stipend", salary, palettes.OKABE_ITO["blue"]),
    ("Fringe", fringe, palettes.OKABE_ITO["sky_blue"]),
    ("Tuition", tuition, palettes.OKABE_ITO["orange"]),
    ("Bench fees", bench, palettes.OKABE_ITO["bluish_green"]),
]
total = sum(p[1] for p in parts)

dvstyle.set_style("talk")
fig, ax = plt.subplots(figsize=(9.0, 5.6))

bottom = np.zeros_like(YEARS, dtype=float)
for label, vals, color in parts:
    ax.bar(YEARS, vals, bottom=bottom, width=0.62, color=color, label=label,
           edgecolor="white", linewidth=0.8)
    # in-bar value labels, skipped where the segment is too thin to hold text
    for x, v, b in zip(YEARS, vals, bottom):
        if v > 4000:
            ax.text(x, b + v / 2, f"${v/1000:,.1f}k", ha="center", va="center",
                    color="white", fontsize=10 if v < 8000 else 11, fontweight="bold")
    bottom += vals

for x, t in zip(YEARS, total):
    ax.text(x, t + 1600, f"${t/1000:,.0f}k", ha="center", va="bottom",
            fontsize=13, fontweight="bold")

ax.set_xticks(YEARS)
ax.set_xticklabels([f"Year {y}" for y in YEARS])
ax.set_ylabel("Cost to the advisor's grants")
ax.set_ylim(0, total.max() * 1.13)
ax.set_yticks(np.arange(0, 90001, 20000))
ax.set_yticklabels([f"${v//1000:,.0f}k" for v in np.arange(0, 90001, 20000)])
ax.set_title(f"What Jane costs: ${total.sum()/1000:,.0f}k over five years")

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], loc="upper left", frameon=False,
          bbox_to_anchor=(1.01, 1.0), handlelength=1.1, borderaxespad=0)

FIGURES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")
os.makedirs(FIGURES, exist_ok=True)
dvstyle.save_both(fig, os.path.join(FIGURES, "jane-cost"))
print("year totals:", [f"{t:,.0f}" for t in total])
print("5-year total:", f"{total.sum():,.0f}")
