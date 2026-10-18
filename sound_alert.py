"""Windows sound alerts with a safe fallback on other operating systems."""

import sys
import time


def play_risk_sound(level):
    """Play a different beep pattern according to the calculated risk level."""
    patterns = {
        "LOW": [(700, 180)],
        "MODERATE": [(700, 180), (900, 180)],
        "HIGH": [(1000, 220), (1000, 220), (1000, 220)],
        "CRITICAL": [(1400, 250), (700, 250), (1400, 250), (700, 250)],
    }
    pattern = patterns.get(level, patterns["LOW"])

    try:
        if sys.platform == "win32":
            import winsound
            for frequency, duration in pattern:
                winsound.Beep(frequency, duration)
                time.sleep(0.08)
        else:
            # Terminal bell fallback; sound depends on terminal/system settings.
            print("\a" * len(pattern), end="", flush=True)
    except Exception as exc:
        print(f"Could not play sound alert: {exc}")

