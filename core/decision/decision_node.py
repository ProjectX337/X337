from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class DecisionNode:

    id: str

    decision_type: str

    winner: str

    confidence: float

    alternatives: list[str] = field(default_factory=list)

    metadata: dict = field(default_factory=dict)
