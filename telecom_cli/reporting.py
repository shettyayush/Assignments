"""Aggregation and presentation of billing results."""

from typing import Any

from fraud import is_suspicious
from models import CDR, Subscriber


def build_report(subscribers: dict[str, Subscriber], cdrs: list[CDR],
                 malformed_rows: int, total_rows: int,
                 fraud_threshold_sec: int) -> dict[str, Any]:
    """Build the complete daily billing and anomaly report."""
    unknown_msisdns: set[str] = set()
    unknown_calls: list[dict[str, Any]] = []
    suspicious_calls: list[dict[str, Any]] = []

    for cdr in cdrs:
        call_summary = {
            "msisdn": cdr.msisdn,
            "call_type": cdr.call_type,
            "duration_sec": cdr.duration_sec,
            "cost": cdr.cost,
        }
        if cdr.msisdn not in subscribers:
            unknown_msisdns.add(cdr.msisdn)
            unknown_calls.append(call_summary)
            continue

        subscribers[cdr.msisdn].calls.append(cdr)
        if is_suspicious(cdr, fraud_threshold_sec):
            suspicious_calls.append(call_summary)

    subscriber_summary = {
        msisdn: {
            "plan_type": subscriber.plan_type,
            "call_count": len(subscriber.calls),
            "total_cost": subscriber.total_cost(),
        }
        for msisdn, subscriber in sorted(subscribers.items())
    }
    return {
        "batch_summary": {
            "total_cdr_rows": total_rows,
            "valid_cdr_rows": len(cdrs),
            "malformed_cdr_rows": malformed_rows,
            "total_billed_cost": round(
                sum(item["total_cost"] for item in subscriber_summary.values()), 2),
        },
        "subscribers": subscriber_summary,
        "anomalies": {
            "unknown_subscribers": sorted(unknown_msisdns),
            "unknown_subscriber_calls": unknown_calls,
            "suspicious_calls": suspicious_calls,
        },
    }


def print_summary(report: dict[str, Any]) -> None:
    """Print the intentional human-readable completion summary."""
    batch = report["batch_summary"]
    anomalies = report["anomalies"]
    print("\nDaily Telecom Billing Summary")
    print("-" * 30)
    print(f"Valid CDRs: {batch['valid_cdr_rows']} of {batch['total_cdr_rows']}")
    print(f"Malformed CDRs: {batch['malformed_cdr_rows']}")
    print(f"Total billed cost: {batch['total_billed_cost']:.2f}")
    print(f"Subscribers billed: {len(report['subscribers'])}")
    print(f"Unknown subscribers: {len(anomalies['unknown_subscribers'])}")
    print(f"Suspicious calls: {len(anomalies['suspicious_calls'])}")
