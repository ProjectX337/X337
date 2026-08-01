from __future__ import annotations

from dataclasses import dataclass

from core.capabilities.capability import Capability


@dataclass(slots=True)
class CapabilityMatch:
    """
    Represents a capability selected during planning.

    Unlike Capability, this object contains
    runtime planning information.
    """

    capability: Capability

    score: int

    confidence: float
