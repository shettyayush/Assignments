"""Fraud screening rules for call-detail records."""

from models import CDR


def is_suspicious(cdr: CDR, threshold_sec: int) -> bool:
    """Determine whether a call requires manual fraud review.

    Args:
        cdr: The call-detail record to inspect.
        threshold_sec: International-call duration threshold in seconds.

    Returns:
        True if either configured fraud rule matches.
    """
    return cdr.is_suspicious(threshold_sec)
