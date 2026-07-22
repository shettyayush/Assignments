"""Domain models used by the telecom CLI."""

from dataclasses import dataclass, field

from rating import compute_cost


@dataclass
class CDR:
    """A validated call-detail record."""

    msisdn: str
    call_type: str
    duration_sec: int

    @property
    def cost(self) -> float:
        """Return this call's rated cost."""
        return compute_cost(self.call_type, self.duration_sec)

    def is_suspicious(self, threshold_sec: int) -> bool:
        """Return whether this call matches either fraud rule."""
        return ((self.duration_sec > 0 and self.cost == 0) or
                (self.call_type == "international" and
                 self.duration_sec > threshold_sec))


@dataclass
class Subscriber:
    """A subscriber and the calls attributed to that subscriber."""

    msisdn: str
    plan_type: str
    calls: list[CDR] = field(default_factory=list)

    def total_cost(self) -> float:
        """Return the total rated cost of all attributed calls."""
        return round(sum(call.cost for call in self.calls), 2)
