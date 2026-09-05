"""Figures from my own Claude Code transcripts (sessions.csv, prompts.csv)."""
import os, sys
import numpy as np, pandas as pd
REPO = "/Users/ilya/projects/dataviz/python"
SKILL = os.path.expanduser("~/.claude/skills/data-viz/scripts")
sys.path.insert(0, REPO if os.path.isdir(REPO) else SKILL)
import dvstyle, palettes
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data"); OUT = os.path.join(HERE, "..", "figures")
dvstyle.set_style("paper"); palettes.set_categorical_cycle(); OI = palettes.OKABE_ITO
TPW = 1.75
BUDGET_CAREFUL = 4 * 60 * 100 * TPW    # 4 h at 100 wpm, tokens
BUDGET_SKIM = 4 * 60 * 238 * TPW       # 4 h at 238 wpm

s = pd.read_csv(os.path.join(DATA, "sessions.csv"))
p = pd.read_csv(os.path.join(DATA, "prompts.csv"))
for df, cols in [(s, ["start", "end"]), (p, ["ts"])]:
    for c in cols: df[c] = pd.to_datetime(df[c], utc=True, format="ISO8601").dt.tz_convert("America/Chicago")
WINDOW = pd.Timestamp("2026-08-05", tz="America/Chicago")   # Claude Code logs retained ~30 days
s = s[s.start >= WINDOW].reset_index(drop=True); p = p[p.ts >= WINDOW].reset_index(drop=True)
s["day"] = s.start.dt.date; p["day"] = p.ts.dt.date
for c in ["vis_prose", "vis_toolhdr", "vis_preview"]: s[c + "_tok"] = s[c] / 4
days = pd.date_range(s.day.min(), s.day.max(), freq="D").date
daily = s.groupby("day").agg(sessions=("session", "count"), prose=("vis_prose_tok", "sum"),
                             toolhdr=("vis_toolhdr_tok", "sum"), preview=("vis_preview_tok", "sum"),
                             hidden=("hid_tokens", "sum")).reindex(days, fill_value=0)
prompts_per_day = p.groupby("day").size().reindex(days, fill_value=0)

# ---- Fig S1: sessions and prompts per day ----------------------------------
fig, axes = plt.subplots(2, 1, figsize=(7.2, 4.4), sharex=True, layout="constrained")
x = np.arange(len(days))
axes[0].bar(x, daily.sessions, color=OI["blue"], width=0.8)
axes[0].set_ylabel("sessions started"); axes[0].set_title("Claude Code and Codex sessions per day, Aug 5 to Sep 4 2026", loc="left")
axes[1].bar(x, prompts_per_day, color=OI["gray"], width=0.8)
axes[1].set_ylabel("prompts I typed")
wk = [i for i, d in enumerate(days) if d.weekday() == 0]
axes[1].set_xticks(wk); axes[1].set_xticklabels([days[i].strftime("%b %d") for i in wk])
for ax in axes: ax.grid(axis="y", color="0.92", lw=0.6)
dvstyle.save_both(fig, os.path.join(OUT, "figS1-sessions-per-day"))

# ---- Fig S2: visible tokens per day, stacked, vs reading budgets ------------
fig, ax = plt.subplots(figsize=(7.2, 3.8), layout="constrained")
bottom = np.zeros(len(days))
for col, lab, c in [("prose", "Claude's prose", OI["vermillion"]), ("toolhdr", "tool call headers", OI["orange"]),
                    ("preview", "tool result previews (3 lines)", OI["sky_blue"])]:
    ax.bar(x, daily[col], bottom=bottom, color=c, width=0.8, label=lab); bottom += daily[col].values
ax.axhline(BUDGET_CAREFUL, color="0.3", lw=1, ls="--"); ax.text(len(days) - 0.5, BUDGET_CAREFUL * 1.03, "4 h careful reading (100 wpm)", ha="right", va="bottom", fontsize=8, color="0.3")
ax.axhline(BUDGET_SKIM, color="0.3", lw=1, ls=":"); ax.text(len(days) - 0.5, BUDGET_SKIM * 1.03, "4 h skimming (238 wpm)", ha="right", va="bottom", fontsize=8, color="0.3")
ax.set_xticks(wk); ax.set_xticklabels([days[i].strftime("%b %d") for i in wk])
ax.set_ylabel("tokens shown in the terminal"); ax.set_title("What the terminal showed me per day, against a reading budget", loc="left")
ax.legend(loc="upper left", frameon=False, fontsize=8); ax.grid(axis="y", color="0.92", lw=0.6)
dvstyle.save_both(fig, os.path.join(OUT, "figS2-visible-tokens-per-day"))

# ---- Fig S3: per-session distribution, visible vs hidden --------------------
fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.0), layout="constrained")
bins = np.logspace(1.5, 6, 28)
axes[0].hist(s.vis_tokens.clip(lower=40), bins=bins, color=OI["vermillion"], alpha=0.85, label="visible")
axes[0].hist(s.hid_tokens.clip(lower=40), bins=bins, color=OI["gray"], alpha=0.5, label="hidden")
axes[0].set_xscale("log"); axes[0].set_xlabel("tokens per session"); axes[0].set_ylabel("sessions")
axes[0].axvline(s.vis_tokens.median(), color=OI["vermillion"], lw=1, ls="--")
axes[0].set_title(f"{len(s)} sessions; median visible {int(s.vis_tokens.median()):,}", loc="left", fontsize=9)
axes[0].legend(frameon=False, fontsize=8)
axes[1].scatter(s.n_prompts, s.vis_tokens, s=14, color=OI["blue"], alpha=0.6)
axes[1].set_xscale("log"); axes[1].set_yscale("log")
axes[1].set_xlabel("prompts I typed in the session"); axes[1].set_ylabel("visible tokens")
axes[1].set_title("visible tokens scale with turns", loc="left", fontsize=9)
for ax in axes: ax.grid(color="0.92", lw=0.6)
dvstyle.save_both(fig, os.path.join(OUT, "figS3-session-distribution"))

# ---- Fig S4: concurrency and hour of day ------------------------------------
p = p.sort_values("ts").reset_index(drop=True)
W = pd.Timedelta(minutes=15)
conc = []
for i, r in p.iterrows():
    win = p[(p.ts >= r.ts - W) & (p.ts <= r.ts + W)]
    conc.append(win.session.nunique())
p["conc"] = conc; p["hour"] = p.ts.dt.hour
fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.0), layout="constrained")
vc = p.conc.value_counts().sort_index()
axes[0].bar(vc.index, 100 * vc.values / len(p), color=OI["bluish_green"], width=0.7)
axes[0].set_xlabel("distinct sessions I prompted within ±15 min"); axes[0].set_ylabel("% of prompts")
axes[0].set_title(f"{100*(p.conc>=2).mean():.0f}% of prompts sent while juggling ≥2 sessions", loc="left", fontsize=9)
axes[0].set_xticks(range(1, int(vc.index.max()) + 1))
byh = p.groupby("hour").agg(n=("session", "size"), conc=("conc", "mean")).reindex(range(6, 24), fill_value=0)
axes[1].bar(byh.index, byh.n, color=OI["gray"], width=0.8, label="prompts")
ax2 = axes[1].twinx(); ax2.plot(byh.index, byh.conc, "o-", color=OI["vermillion"], ms=4, lw=1.2)
ax2.set_ylabel("mean concurrent sessions", color=OI["vermillion"]); ax2.set_ylim(1, None)
ax2.spines["right"].set_visible(True)
axes[1].set_xlabel("hour of day"); axes[1].set_ylabel("prompts"); axes[1].set_title("prompts and juggling by hour", loc="left", fontsize=9)
for ax in axes: ax.grid(axis="y", color="0.92", lw=0.6)
dvstyle.save_both(fig, os.path.join(OUT, "figS4-concurrency"))
p.to_csv(os.path.join(DATA, "prompts.csv"), index=False)
print("median sessions/active day", s.groupby("day").size().median(),
      "| median visible tokens/active day", int(daily[daily.sessions > 0][["prose", "toolhdr", "preview"]].sum(axis=1).median()),
      "| prose only", int(daily[daily.sessions > 0].prose.median()),
      "| prompts with >=2 concurrent", f"{100*(p.conc>=2).mean():.0f}%", "| >=3", f"{100*(p.conc>=3).mean():.0f}%")
