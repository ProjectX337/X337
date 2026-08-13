from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class CapabilityHypothesis:
    """
    Intelligence-derived capability proposal.

    Represents why a capability exists,
    where it came from, and confidence.
    """

    name: str

    rationale: str = ""

    confidence: float = 0.0

    source: str = (
        "product_intelligence"
    )

    evidence: list[str] = field(
        default_factory=list
    )

    metadata: dict = field(
        default_factory=dict
    )
