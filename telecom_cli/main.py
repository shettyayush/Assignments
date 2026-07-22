"""Command-line entry point for the Telecom CDR & Billing Insights tool."""

import argparse
import datetime
import json
import logging
import sys
from pathlib import Path

from config import DEFAULT_FRAUD_THRESHOLD_SEC, MAX_MALFORMED_RATIO
from io_utils import load_cdrs, load_subscribers, write_report
from models import CDR
from reporting import build_report, print_summary

LOGGER = logging.getLogger(__name__)
BASE_DIR = Path(__file__).resolve().parent


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for a daily batch run."""
    parser = argparse.ArgumentParser(description="Process a telecom CDR batch.")
    parser.add_argument("--subscribers", default=str(BASE_DIR / "subscribers.json"),
                        help="Path to subscriber master JSON.")
    parser.add_argument("--cdrs", default=str(BASE_DIR / "cdrs.csv"),
                        help="Path to CDR CSV.")
    parser.add_argument("--output", default=str(BASE_DIR / "report.json"),
                        help="Path for the output JSON report.")
    parser.add_argument("--fraud-threshold-sec", type=int,
                        default=DEFAULT_FRAUD_THRESHOLD_SEC,
                        help="International-call fraud threshold in seconds.")
    return parser.parse_args()


def configure_logging() -> None:
    """Configure application logging once for the CLI process."""
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(name)s: %(message)s")


def main() -> int:
    """Run the CDR ingestion, billing, screening, and reporting pipeline."""
    configure_logging()
    args = parse_args()
    if args.fraud_threshold_sec < 0:
        LOGGER.error("--fraud-threshold-sec must be non-negative")
        return 2

    try:
        subscribers = load_subscribers(args.subscribers)
        batch = load_cdrs(args.cdrs)
    except (OSError, ValueError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        LOGGER.error("Unable to load input data: %s", exc)
        return 1

    if batch.total_rows and batch.malformed_rows / batch.total_rows > MAX_MALFORMED_RATIO:
        LOGGER.critical("Malformed CDR ratio %.2f%% exceeds permitted %.2f%%; no report written",
                        (batch.malformed_rows / batch.total_rows) * 100,
                        MAX_MALFORMED_RATIO * 100)
        return 1

    cdrs = [CDR(**row) for row in batch]
    report = build_report(subscribers, cdrs, batch.malformed_rows, batch.total_rows,
                          args.fraud_threshold_sec)
    try:
        write_report(report, args.output)
    except OSError as exc:
        LOGGER.error("Unable to write report: %s", exc)
        return 1
    print_summary(report)
    return 0


if __name__ == "__main__":
    today = datetime.date.today()
    print(f"--- Telecom CDR & Billing Insights CLI --- {today}")
    sys.exit(main())
