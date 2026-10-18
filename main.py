"""SmartDrain desktop application. Run this file in PyCharm."""

import threading
import tkinter as tk
from tkinter import ttk, messagebox

from risk_engine import calculate_risk
from sound_alert import play_risk_sound
from whatsapp_alert import send_whatsapp_alert
from charts import draw_dashboard


class SmartDrainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SmartDrain | Drainage Failure & Flood Risk Simulator")
        self.root.geometry("1100x760")
        self.root.minsize(900, 650)

        self.last_alert_level = None
        self.last_result = None
        self.last_readings = None
        self.canvas = None

        self._build_ui()

    def _build_ui(self):
        title = ttk.Label(
            self.root,
            text="SmartDrain – Drainage Failure & Flood Risk Simulator",
            font=("Segoe UI", 17, "bold"),
        )
        title.pack(pady=(12, 2))

        subtitle = ttk.Label(
            self.root,
            text="Rule-based educational simulation • Not a certified flood-warning system",
        )
        subtitle.pack(pady=(0, 10))

        content = ttk.Frame(self.root, padding=12)
        content.pack(fill="both", expand=True)

        input_frame = ttk.LabelFrame(content, text="Dynamic sensor inputs", padding=12)
        input_frame.pack(side="left", fill="y", padx=(0, 12))

        self.rainfall_var = tk.StringVar(value="60")
        self.water_var = tk.StringVar(value="55")
        self.blockage_var = tk.StringVar(value="40")
        self.flow_var = tk.StringVar(value="45")
        self.phone_var = tk.StringVar(value="+91")
        self.whatsapp_enabled = tk.BooleanVar(value=False)
        self.sound_enabled = tk.BooleanVar(value=True)

        fields = [
            ("Rainfall (mm/hour, 0–150)", self.rainfall_var),
            ("Water level (% capacity, 0–100)", self.water_var),
            ("Drain blockage (%, 0–100)", self.blockage_var),
            ("Flow rate (L/s, 0–100)", self.flow_var),
        ]
        for label, variable in fields:
            ttk.Label(input_frame, text=label).pack(anchor="w", pady=(8, 2))
            ttk.Entry(input_frame, textvariable=variable, width=28).pack(anchor="w")

        ttk.Separator(input_frame).pack(fill="x", pady=12)
        ttk.Checkbutton(
            input_frame, text="Enable sound alerts", variable=self.sound_enabled
        ).pack(anchor="w", pady=3)
        ttk.Checkbutton(
            input_frame,
            text="Send WhatsApp on HIGH/CRITICAL",
            variable=self.whatsapp_enabled,
        ).pack(anchor="w", pady=3)

        ttk.Label(input_frame, text="WhatsApp number (international format)").pack(
            anchor="w", pady=(10, 2)
        )
        ttk.Entry(input_frame, textvariable=self.phone_var, width=28).pack(anchor="w")
        ttk.Label(
            input_frame,
            text="Example: +919876543210",
            foreground="gray",
        ).pack(anchor="w", pady=(2, 0))

        ttk.Button(
            input_frame, text="Calculate risk", command=self.calculate
        ).pack(fill="x", pady=(14, 5))
        ttk.Button(
            input_frame, text="Send test alert now", command=self.send_test_alert
        ).pack(fill="x", pady=5)

        ttk.Label(
            input_frame,
            text="Alerts are sent only when enabled and the risk level changes to HIGH or CRITICAL.",
            wraplength=230,
            foreground="gray",
        ).pack(anchor="w", pady=(12, 0))

        right = ttk.Frame(content)
        right.pack(side="left", fill="both", expand=True)

        result_frame = ttk.LabelFrame(right, text="Current assessment", padding=12)
        result_frame.pack(fill="x")

        self.level_label = ttk.Label(
            result_frame, text="Risk: Not calculated", font=("Segoe UI", 16, "bold")
        )
        self.level_label.pack(anchor="w")
        self.advice_label = ttk.Label(
            result_frame, text="Enter sensor values and select Calculate risk.",
            wraplength=650,
        )
        self.advice_label.pack(anchor="w", pady=(5, 0))

        chart_frame = ttk.LabelFrame(right, text="Risk visualisation", padding=8)
        chart_frame.pack(fill="both", expand=True, pady=(12, 0))
        self.chart_frame = chart_frame

        footer = ttk.Label(
            self.root,
            text="Demo thresholds/weights are illustrative. Validate with real sensor data before any operational use.",
            foreground="gray",
        )
        footer.pack(pady=(0, 8))

    def _read_inputs(self):
        try:
            readings = {
                "rainfall": float(self.rainfall_var.get()),
                "water_level": float(self.water_var.get()),
                "blockage": float(self.blockage_var.get()),
                "flow_rate": float(self.flow_var.get()),
            }
        except ValueError as exc:
            raise ValueError("All sensor inputs must be numeric.") from exc

        ranges = {
            "rainfall": (0, 150),
            "water_level": (0, 100),
            "blockage": (0, 100),
            "flow_rate": (0, 100),
        }
        for name, value in readings.items():
            low, high = ranges[name]
            if not low <= value <= high:
                raise ValueError(f"{name.replace('_', ' ').title()} must be between {low} and {high}.")
        return readings

    def calculate(self):
        try:
            readings = self._read_inputs()
            result = calculate_risk(
                readings["rainfall"],
                readings["water_level"],
                readings["blockage"],
                readings["flow_rate"],
            )
        except ValueError as exc:
            messagebox.showerror("Invalid input", str(exc))
            return

        previous_level = self.last_result["level"] if self.last_result else None
        self.last_result = result
        self.last_readings = readings

        colors = {
            "LOW": "green",
            "MODERATE": "goldenrod",
            "HIGH": "darkorange",
            "CRITICAL": "red",
        }
        self.level_label.configure(
            text=f"Risk: {result['level']}  |  Score: {result['score']}/100",
            foreground=colors[result["level"]],
        )
        self.advice_label.configure(text=result["advice"])

        self.canvas = draw_dashboard(self.chart_frame, result, readings)

        if self.sound_enabled.get() and result["level"] in ("HIGH", "CRITICAL"):
            # Do not freeze the interface while the sound pattern plays.
            threading.Thread(
                target=play_risk_sound, args=(result["level"],), daemon=True
            ).start()

        # Notify only on a transition into HIGH/CRITICAL, preventing repeated sends
        # every time Calculate is clicked at the same level.
        if (
            self.whatsapp_enabled.get()
            and result["level"] in ("HIGH", "CRITICAL")
            and result["level"] != previous_level
        ):
            self._send_whatsapp_async(readings, result)

    def _send_whatsapp_async(self, readings, result):
        phone = self.phone_var.get().strip()

        def worker():
            try:
                status = send_whatsapp_alert(phone, result, readings)
                self.root.after(0, lambda: messagebox.showinfo("WhatsApp alert", status))
            except Exception as exc:
                self.root.after(
                    0,
                    lambda error=str(exc): messagebox.showerror("WhatsApp alert failed", error),
                )

        threading.Thread(target=worker, daemon=True).start()

    def send_test_alert(self):
        try:
            readings = self._read_inputs()
            result = calculate_risk(
                readings["rainfall"],
                readings["water_level"],
                readings["blockage"],
                readings["flow_rate"],
            )
            send_whatsapp_alert(self.phone_var.get(), result, readings)
            messagebox.showinfo(
                "WhatsApp alert",
                "WhatsApp Web was asked to send the test alert. Check the browser and WhatsApp.",
            )
        except Exception as exc:
            messagebox.showerror("WhatsApp alert failed", str(exc))


if __name__ == "__main__":
    root = tk.Tk()
    app = SmartDrainApp(root)
    root.mainloop()

