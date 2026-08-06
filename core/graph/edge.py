from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class GraphEdge:
    """
    Directed relationship between two nodes.
    """

    source: str

    target: str

    relation: str

    weight: float = 1.0
