"""
Compatibility exports.

Canonical GraphEdge lives in core.graph.models.
This module preserves legacy edge_type construction.
"""

from core.graph.models import (
    GraphEdge as _GraphEdge,
    EdgeRelation as EdgeType,
)


class GraphEdge(_GraphEdge):
    def __init__(
        self,
        source: str,
        target: str,
        relation=None,
        metadata: dict | None = None,
        *,
        edge_type=None,
    ):
        if relation is None:
            relation = edge_type

        if relation is None:
            raise TypeError(
                "GraphEdge requires either 'relation' or legacy 'edge_type'."
            )

        super().__init__(
            source=source,
            target=target,
            relation=relation,
            metadata=metadata or {},
        )

    @property
    def edge_type(self):
        """
        Backwards-compatible alias.

        Canonical field is `relation`.
        """
        return self.relation

    @edge_type.setter
    def edge_type(self, value):
        self.relation = value


__all__ = [
    "GraphEdge",
    "EdgeType",
]
