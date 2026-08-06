from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class Decision:

    winner: str

    confidence: float

    evidence: list[str] = field(default_factory=list)

    alternatives: list[tuple[str, float]] = field(default_factory=list)

    warnings: list[str] = field(default_factory=list)

    metadata: dict = field(default_factory=dict)
