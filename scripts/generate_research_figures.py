"""Generate conceptual wireless figures; these are not Sionna simulation outputs.

Run with Python and Matplotlib installed: python scripts/generate_research_figures.py
Scene: TX=(0, 0), RX=(40, 0) metres; reflecting walls at y=10 and y=-15.
Only the direct path and one reflection from each wall are shown.
Powers are chosen for illustration, not calculated from materials or path loss.
"""

from pathlib import Path
import math

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

OUT = Path(__file__).resolve().parents[1] / "assets"
COLORS = ["#447de8", "#d49129", "#229b89"]
PATH_LENGTHS = [40, 2 * math.hypot(20, 10), 2 * math.hypot(20, 15)]
DELAYS = [(length - 40) / 299792458 * 1e9 for length in PATH_LENGTHS]
POWERS = [1.0, 0.35, 0.15]

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13,
                     "svg.fonttype": "none", "svg.hashsalt": "wireless-model"})

for theme, bg, fg, muted, border in [
    ("light", "#f7f8fa", "#1a1d23", "#5b6470", "#d7dce4"),
    ("dark", "#171a21", "#e7e9ee", "#a6adba", "#39414e"),
]:
    fig, ax = plt.subplots(figsize=(7.2, 4.6), facecolor=bg)
    ax.set_facecolor(bg)
    ax.set_xlim(-10, 50)
    ax.set_ylim(-23, 20)
    ax.set_aspect("equal")
    ax.axis("off")
    for y in [10, -15]:
        ax.add_patch(Rectangle((-3, y - 0.5), 46, 1, color=border))
    ax.text(20, 13, "Reflecting surface", ha="center", color=muted)
    ax.text(20, -20, "Reflecting surface", ha="center", color=muted)
    ax.plot([0, 40], [0, 0], color=COLORS[0], lw=2.8)
    ax.plot([0, 20, 40], [0, 10, 0], color=COLORS[1], lw=2.8, ls="--")
    ax.plot([0, 20, 40], [0, -15, 0], color=COLORS[2], lw=2.8, ls="-.")
    ax.text(20, 1.5, "Direct · 40 m", ha="center", color=fg)
    ax.text(20, 5.6, "44.7 m", ha="center", color=fg)
    ax.text(20, -10, "50 m", ha="center", color=fg)
    ax.scatter([0, 40], [0, 0], s=150, color=fg, edgecolors=bg, linewidths=2, zorder=5)
    ax.text(-4, -4.8, "TX", ha="center", color=fg, weight="bold")
    ax.text(44, -4.8, "RX", ha="center", color=fg, weight="bold")
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.02, top=0.98)
    fig.savefig(OUT / f"sionna-multipath-{theme}.svg", metadata={"Date": None})
    if theme == "light":
        fig.savefig("/tmp/sionna-multipath-preview.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7.2, 4.6), facecolor=bg)
    ax.set_facecolor(bg)
    ax.set_axisbelow(True)
    ax.grid(axis="y", color=border, lw=0.8)
    for delay, power, color, label in zip(DELAYS, POWERS, COLORS,
                                         ["Direct", "Reflection 1", "Reflection 2"]):
        ax.vlines(delay, 0, power, color=color, lw=3)
        ax.plot(delay, power, "o", color=color, markersize=8)
        ax.annotate(label, (delay, power), xytext=(0, 13),
                    textcoords="offset points", ha="center", color=fg, fontsize=12)
    ax.set(xlim=(-6, 42), ylim=(0, 1.2), xticks=[0, 10, 20, 30, 40],
           yticks=[0, 0.25, 0.5, 0.75, 1.0])
    ax.set_xlabel("Excess delay (ns)", color=fg, labelpad=12)
    ax.set_ylabel("Relative path power", color=fg, labelpad=10)
    ax.tick_params(colors=muted, length=0, pad=9)
    for side in ["top", "right"]:
        ax.spines[side].set_visible(False)
    for side in ["bottom", "left"]:
        ax.spines[side].set_color(border)
    fig.subplots_adjust(left=0.16, right=0.96, bottom=0.20, top=0.94)
    fig.savefig(OUT / f"sionna-delay-profile-{theme}.svg", metadata={"Date": None})
    if theme == "light":
        fig.savefig("/tmp/sionna-delay-profile-preview.png", dpi=160)
    plt.close(fig)

print("Generated light and dark SVG figures.")
print("Excess delays (ns):", [round(delay, 2) for delay in DELAYS])
