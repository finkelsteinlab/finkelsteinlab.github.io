"""Figures for "My token limit". Run with the data-viz env (see skill)."""
import os, sys
import numpy as np, pandas as pd
REPO = "/Users/ilya/projects/dataviz/python"
SKILL = os.path.expanduser("~/.claude/skills/data-viz/scripts")
sys.path.insert(0, REPO if os.path.isdir(REPO) else SKILL)
import dvstyle, palettes
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
OUT = os.path.join(HERE, "..", "figures"); os.makedirs(OUT, exist_ok=True)
TPW = 1.75   # tokens per word, measured on Ilya's manuscripts with cl100k/o200k
dvstyle.set_style("paper")
palettes.set_categorical_cycle()
OI = palettes.OKABE_ITO
CLASS_COLOR = {"read": OI["sky_blue"], "write": OI["vermillion"],
               "edit": OI["bluish_green"], "review": OI["orange"]}

# ---- Figure 1: throughput ladder, tokens/hour, log scale ------------------
df = pd.read_csv(os.path.join(DATA, "throughput.csv"))
df["t_lo"] = df.words_per_hour_low * TPW
df["t_hi"] = df.words_per_hour_high * TPW
df["t_pt"] = df.words_per_hour_point * TPW
df = df.sort_values("t_pt").reset_index(drop=True)

fig, ax = plt.subplots(figsize=(6.8, 5.2))
y = np.arange(len(df))
for i, r in df.iterrows():
    c = CLASS_COLOR[r["class"]]
    ax.plot([r.t_lo, r.t_hi], [i, i], color=c, lw=2.2, solid_capstyle="round", alpha=0.55)
    ax.plot(r.t_pt, i, "o", color=c, ms=6.5, zorder=3)
ax.set_yticks(y); ax.set_yticklabels(df.activity)
ax.set_xscale("log")
ax.set_xlim(300, 60000)
ax.set_xlabel("tokens per hour (1.75 tokens per word)")
ax2 = ax.secondary_xaxis("top", functions=(lambda t: t / TPW, lambda w: w * TPW))
ax2.set_xlabel("words per hour")
for cls, lab in [("read", "read / listen"), ("write", "write"), ("edit", "edit"), ("review", "review")]:
    ax.plot([], [], "o", color=CLASS_COLOR[cls], label=lab)
ax.legend(loc="lower right", frameon=False, title=None)
ax.set_title("Human text throughput by task, from the literature")
ax.grid(axis="x", color="0.9", lw=0.6)
dvstyle.save_both(fig, os.path.join(OUT, "fig1-throughput-ladder"))

# ---- Figure 2: daily budgets vs model context windows -----------------------
db = pd.read_csv(os.path.join(DATA, "daily_budgets.csv"))
db["tokens"] = db.words_per_day * TPW
db = db.sort_values("tokens").reset_index(drop=True)
kind_color = {"measured": OI["bluish_green"], "self-report": OI["vermillion"],
              "observed": OI["vermillion"], "target": OI["gray"], "derived": OI["sky_blue"]}
fig, ax = plt.subplots(figsize=(6.8, 5.6))
ax.barh(np.arange(len(db)), db.tokens, color=[kind_color[k] for k in db.kind], height=0.7)
ax.set_yticks(np.arange(len(db))); ax.set_yticklabels(db.regime)
ax.set_xscale("log"); ax.set_xlim(100, 3e6)
for x, lab in [(200_000, "Haiku 4.5\ncontext"), (1_000_000, "1M-token\ncontext")]:
    ax.axvline(x, color="0.35", lw=1, ls="--")
    ax.text(x * 1.08, len(db) - 0.6, lab, va="top", fontsize=8, color="0.3")
ax.set_xlabel("tokens per day")
ax.set_title("Reported daily output, and what a context window holds")
from matplotlib.patches import Patch
handles = [Patch(color=kind_color[k], label=lab) for k, lab in
           [("measured", "measured"), ("self-report", "self-report / anecdote"),
            ("derived", "derived from rate x hours"), ("target", "target")]]
ax.legend(handles=handles, loc="lower right", frameon=False)
ax.grid(axis="x", color="0.9", lw=0.6)
dvstyle.save_both(fig, os.path.join(OUT, "fig2-daily-budgets"))

# ---- Figure 3: what degrades: checking, not output (three replicated results)
fig, axes = plt.subplots(1, 3, figsize=(8.0, 2.7), layout="constrained")
ax = axes[0]
ax.plot([0.5, 1.5], [100 - 9.2, 100 - 12.9], "o-", color=OI["sky_blue"])
ax.plot([0.5, 1.5], [73, 39], "o-", color=OI["vermillion"])
ax.text(0.45, 95, "accuracy", ha="left", va="bottom", fontsize=8, color=OI["sky_blue"])
ax.text(0.45, 66, "errors self-corrected", ha="left", va="top", fontsize=8, color=OI["vermillion"])
ax.set_ylim(0, 100); ax.set_xlim(0, 2); ax.set_xticks([0, 1, 2])
ax.set_xlabel("hours on task"); ax.set_ylabel("percent")
ax.set_title("Boksem 2006, 2 h task, n=19", loc="left", fontsize=9)
ax = axes[1]
ax.bar(["hour 1", "hour 4"], [1.00, 1.26], color=[OI["gray"], OI["orange"]], width=0.6)
ax.set_ylim(0, 1.4); ax.set_ylabel("odds ratio, inappropriate\nantibiotic prescribed", fontsize=8)
ax.set_xlabel("position in clinic session")
ax.set_title("Linder 2014, 21,867 visits", loc="left", fontsize=9)
ax = axes[2]
hrs = np.arange(0, 8)
ax.plot(hrs, -0.9 * hrs, "-", color=OI["bluish_green"])
ax.annotate("20-30 min break\nrecovers +1.7", xy=(4, -3.6), xytext=(0.3, -6.3), fontsize=8,
            arrowprops=dict(arrowstyle="->", color="0.4"), color="0.3")
ax.set_xlabel("hours later in the day"); ax.set_ylabel("test score, % of SD")
ax.set_title("Sievertsen 2016, Danish schools", loc="left", fontsize=9)
fig.suptitle("Fatigue shows up as skipped checking before it shows up as worse output",
             x=0.01, ha="left", fontsize=10)
dvstyle.save_both(fig, os.path.join(OUT, "fig3-what-degrades"))
# ---- Figure 4: review budget, hours vs document tokens ---------------------
rb = pd.read_csv(os.path.join(DATA, "review_budget.csv"))
rb["tokens"] = rb.words * TPW
fig, ax = plt.subplots(figsize=(6.4, 4.2))
# reference reading-rate lines: hours = tokens / (wpm*60*TPW)
xs = np.array([5000, 15000])
for wpm, lab, c in [(238, "read at 238 wpm", OI["sky_blue"]), (100, "read for recall, 100 wpm", OI["blue"]),
                    (54, "study at 54 wpm", OI["reddish_purple"])]:
    ax.plot(xs, xs / (wpm * 60 * TPW), "-", color=c, lw=1, alpha=0.8)
    ax.text(xs[-1] * 1.02, xs[-1] / (wpm * 60 * TPW), lab, fontsize=8, color=c, va="center")
rv = rb[~rb.item.str.contains("writing")]
for _, r in rv.iterrows():
    ax.plot([r.tokens, r.tokens], [r.hours_low, r.hours_high], color=OI["orange"], lw=2.2, alpha=0.6)
    ax.plot(r.tokens, r.hours_point, "o", color=OI["orange"], ms=6.5, zorder=3)
    ax.text(r.tokens + 250, r.hours_point + (0.25 if "Black" in r["item"] else 0),
            r["item"], fontsize=8, va="center")
ax.set_xlim(4000, 20000); ax.set_ylim(0, 7)
ax.set_xlabel("document length, tokens (1.75 per word)"); ax.set_ylabel("hours per review")
ax.set_title("Reviewing costs far more than reading: hours per document")
ax.grid(color="0.92", lw=0.6)
dvstyle.save_both(fig, os.path.join(OUT, "fig4-review-budget"))
print("done")
