"""SmartDrain configuration and risk thresholds."""

RISK_LEVELS = {
    "LOW": (0, 24),
    "MODERATE": (25, 49),
    "HIGH": (50, 74),
    "CRITICAL": (75, 100),
}

# Risk components should total 100%.
WEIGHTS = {
    "rainfall": 0.30,
    "water_level": 0.35,
    "blockage": 0.25,
    "low_flow": 0.10,
}

