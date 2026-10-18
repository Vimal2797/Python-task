"""Optional WhatsApp alert sender using pywhatkit."""

import re


def validate_phone_number(phone_number):
    """Require international format, e.g. +919876543210."""
    phone_number = phone_number.strip()
    if not re.fullmatch(r"\+[1-9]\d{7,14}", phone_number):
        raise ValueError("Enter the number in international format, e.g. +919876543210.")
    return phone_number


def send_whatsapp_alert(phone_number, result, readings):
    """
    Opens WhatsApp Web and attempts to send a message through pywhatkit.
    WhatsApp Web must already be logged in in the default browser.
    """
    phone_number = validate_phone_number(phone_number)

    try:
        import pywhatkit
    except ImportError as exc:
        raise RuntimeError(
            "pywhatkit is not installed. Run: pip install pywhatkit"
        ) from exc

    message = (
        "SMARTDRAIN ALERT\n"
        f"Risk level: {result['level']} ({result['score']}/100)\n"
        f"Rainfall: {readings['rainfall']} mm/hour\n"
        f"Water level: {readings['water_level']}%\n"
        f"Drain blockage: {readings['blockage']}%\n"
        f"Flow rate: {readings['flow_rate']} L/s\n"
        f"Recommendation: {result['advice']}\n"
        "Note: Automated simulation alert; verify conditions locally."
    )

    # This may open a browser window and requires internet + WhatsApp Web login.
    pywhatkit.sendwhatmsg_instantly(
        phone_no=phone_number,
        message=message,
        wait_time=20,
        tab_close=True,
        close_time=3,
    )
    return "WhatsApp Web was asked to send the alert. Verify delivery in WhatsApp."

