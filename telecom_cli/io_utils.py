"""Input validation and JSON/CSV file operations."""

import csv
import json
import logging
from pathlib import Path
from typing import Any

from models import Subscriber

LOGGER = logging.getLogger(__name__)
REQUIRED_CDR_FIELDS = ("msisdn", "call_type", "duration_sec")


class CDRBatch(list[dict[str, Any]]):
    """Validated CDR rows together with ingestion counts."""

    def __init__(self, rows: list[dict[str, Any]], total_rows: int,
                 malformed_rows: int) -> None:
        """Initialize a batch and its validation statistics."""
        super().__init__(rows)
        self.total_rows = total_rows
        self.malformed_rows = malformed_rows


def parse_cdr_line(row: dict[str, str | None]) -> dict[str, Any]:
    """Validate and normalize one raw CDR row.

    Raises:
        ValueError: If a required field is absent, blank, or invalid.
    """
    missing = [field for field in REQUIRED_CDR_FIELDS
               if not row.get(field) or not str(row[field]).strip()]
    if missing:
        raise ValueError(f"missing required field(s): {', '.join(missing)}")

    try:
        duration_sec = int(str(row["duration_sec"]).strip())
    except (TypeError, ValueError) as exc:
        raise ValueError("duration_sec must be an integer") from exc
    if duration_sec < 0:
        raise ValueError("duration_sec cannot be negative")

    return {
        "msisdn": str(row["msisdn"]).strip(),
        "call_type": str(row["call_type"]).strip().lower(),
        "duration_sec": duration_sec,
    }


def parse_legacy_line(line: str) -> dict[str, Any]:
    """Parse a pipe-delimited legacy CDR line into a normalized dictionary."""
    parts = [part.strip() for part in line.split("|")]
    if len(parts) != 3:
        raise ValueError("legacy CDR line must contain exactly three fields")
    return parse_cdr_line(dict(zip(REQUIRED_CDR_FIELDS, parts)))


def load_subscribers(json_path: str) -> dict[str, Subscriber]:
    """Load subscriber master data keyed by MSISDN."""
    path = Path(json_path)
    with path.open("r", encoding="utf-8") as file_handle:
        records = json.load(file_handle)

    if not isinstance(records, list):
        raise ValueError("subscriber JSON must contain a list")

    subscribers: dict[str, Subscriber] = {}
    for index, record in enumerate(records, start=1):
        try:
            msisdn = str(record["msisdn"]).strip()
            plan_type = str(record["plan_type"]).strip().lower()
        except (KeyError, TypeError) as exc:
            raise ValueError(f"invalid subscriber at position {index}") from exc
        if not msisdn or not plan_type:
            raise ValueError(f"invalid subscriber at position {index}")
        subscribers[msisdn] = Subscriber(msisdn, plan_type)

    LOGGER.info("Loaded %d subscribers from %s", len(subscribers), path)
    return subscribers


def load_cdrs(csv_path: str) -> CDRBatch:
    """Load valid CDRs and log-and-skip malformed CSV rows."""
    path = Path(csv_path)
    valid_rows: list[dict[str, Any]] = []
    malformed_rows = 0
    total_rows = 0

    with path.open("r", encoding="utf-8", newline="") as file_handle:
        reader = csv.DictReader(file_handle)
        if reader.fieldnames is None:
            raise ValueError("CDR CSV is missing a header row")
        for row_number, row in enumerate(reader, start=2):
            total_rows += 1
            try:
                valid_rows.append(parse_cdr_line(row))
            except ValueError as exc:
                malformed_rows += 1
                LOGGER.warning("Skipping malformed CDR row %d: %s", row_number, exc)

    LOGGER.info("Loaded %d valid CDRs; skipped %d malformed rows from %s",
                len(valid_rows), malformed_rows, path)
    return CDRBatch(valid_rows, total_rows, malformed_rows)


def write_report(report: dict[str, Any], output_path: str) -> None:
    """Write an indented JSON report to the requested path."""
    path = Path(output_path)
    with path.open("w", encoding="utf-8") as file_handle:
        json.dump(report, file_handle, indent=2)
        file_handle.write("\n")
    LOGGER.info("Wrote report to %s", path)
