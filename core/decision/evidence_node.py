from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class EvidenceNode:

    id: str

    source: str

    message: str

    weight: float
