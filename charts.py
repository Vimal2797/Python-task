"""Matplotlib charts embedded in the Tkinter dashboard."""

import matplotlib
matplotlib.use("TkAgg")

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def draw_dashboard(parent, result, readings):
    """Create/replace the dashboard chart and return its canvas widget."""
    for child in parent.winfo_children():
        child.destroy()

    figure = Figure(figsize=(8.2, 4.1), dpi=100)
    ax1 = figure.add_subplot(121)
    ax2 = figure.add_subplot(122)

    score = result["score"]
    level = result["level"]
    if level == "LOW":
        risk_color = "green"
    elif level == "MODERATE":
        risk_color = "goldenrod"
    elif level == "HIGH":
        risk_color = "darkorange"
    else:
        risk_color = "red"

    ax1.bar(["Risk score"], [score], color=risk_color, width=0.55)
    ax1.set_ylim(0, 100)
    ax1.set_ylabel("Score (0–100)")
    ax1.set_title(f"{level} RISK: {score}/100")
    ax1.axhline(25, linestyle="--", linewidth=0.8, color="gray")
    ax1.axhline(50, linestyle="--", linewidth=0.8, color="gray")
    ax1.axhline(75, linestyle="--", linewidth=0.8, color="gray")
    ax1.grid(axis="y", alpha=0.2)

    names = list(result["components"].keys())
    values = list(result["components"].values())
    ax2.barh(names, values, color=["steelblue", "slateblue", "sienna", "teal"])
    ax2.set_xlim(0, 100)
    ax2.set_xlabel("Component score (0–100)")
    ax2.set_title("Risk factors")
    ax2.grid(axis="x", alpha=0.2)

    figure.tight_layout()
    canvas = FigureCanvasTkAgg(figure, master=parent)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)
    return canvas

