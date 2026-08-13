from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class EdgeType(str, Enum):
    REQUIRES = "requires"
    IMPLEMENTS = "implements"
    RENDERS = "renders"
    CALLS = "calls"
    MUTATES = "mutates"
    GENERATES = "generates"


@dataclass
class GraphEdge:
    source: str
    target: str
    edge_type: EdgeType
    metadata: dict | None = None
