"""Rule-based drainage risk estimator. This is a demo model, not a trained ML model."""

from config import RISK_LEVELS, WEIGHTS


def _clamp(value, minimum=0.0, maximum=100.0):
    return max(minimum, min(maximum, float(value)))


def calculate_risk(rainfall, water_level, blockage, flow_rate):
    """
    Inputs:
      rainfall: mm/hour, expected range 0-150
      water_level: percentage of drain capacity, 0-100
      blockage: percentage blocked, 0-100
      flow_rate: litres/second, expected range 0-100

    Returns a dictionary containing the overall score, level and component scores.
    These ranges and weights are illustrative and should be calibrated with real data.
    """
    rainfall_score = _clamp(float(rainfall) / 150 * 100)
    water_score = _clamp(water_level)
    blockage_score = _clamp(blockage)
    # Low flow is a concern; 0 L/s maps to 100 risk and 100 L/s maps to 0 risk.
    low_flow_score = _clamp((100 - float(flow_rate)) / 100 * 100)

    components = {
        "Rainfall": rainfall_score,
        "Water level": water_score,
        "Blockage": blockage_score,
        "Low flow": low_flow_score,
    }

    score = round(
        rainfall_score * WEIGHTS["rainfall"]
        + water_score * WEIGHTS["water_level"]
        + blockage_score * WEIGHTS["blockage"]
        + low_flow_score * WEIGHTS["low_flow"]
    )
    score = int(_clamp(score))

    level = "LOW"
    for name, (lower, upper) in RISK_LEVELS.items():
        if lower <= score <= upper:
            level = name
            break

    advice = {
        "LOW": "Conditions appear normal. Continue routine monitoring.",
        "MODERATE": "Monitor water level and rainfall; inspect the drain soon.",
        "HIGH": "High risk. Inspect/clear the drain and notify the responsible team.",
        "CRITICAL": "Critical simulated risk. Take immediate local safety precautions and contact the responsible authorities.",
    }[level]

    return {
        "score": score,
        "level": level,
        "components": components,
        "advice": advice,
    }

