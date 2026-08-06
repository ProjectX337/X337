from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .graph_types import GraphNodeType


@dataclass(slots=True)
class GraphNode:
    """
    Base node used throughout X337.

    Everything eventually becomes a GraphNode.
    """

    id: str

    kind: GraphNodeType

    label: str

    data: dict[str, Any] = field(default_factory=dict)

    metadata: dict[str, Any] = field(default_factory=dict)
