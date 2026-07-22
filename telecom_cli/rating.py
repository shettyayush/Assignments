"""Call rating functions."""

from config import RATES, SECONDS_PER_MINUTE


def compute_cost(call_type: str, duration_sec: int) -> float:
    """Return the rounded cost of a call based on its duration in seconds.

    Args:
        call_type: The call category.
        duration_sec: Non-negative call duration in seconds.

    Returns:
        The call cost rounded to two decimal places.

    Raises:
        ValueError: If the duration is negative.
    """
    if duration_sec < 0:
        raise ValueError("duration_sec cannot be negative")
    rate_per_minute = RATES.get(call_type.lower(), RATES["domestic"])
    return round((duration_sec / SECONDS_PER_MINUTE) * rate_per_minute, 2)
