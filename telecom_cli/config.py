"""Central configuration values for the telecom CLI."""

RATES: dict[str, float] = {
    "domestic": 1.5,
    "roaming": 8.0,
    "international": 12.0,
}
SECONDS_PER_MINUTE = 60
DEFAULT_FRAUD_THRESHOLD_SEC = 3600
MAX_MALFORMED_RATIO = 0.10
