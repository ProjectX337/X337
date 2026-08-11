from __future__ import annotations

from core.graph.models import (
    ApplicationGraph,
    EdgeRelation,
    GraphEdge,
    GraphNode,
    NodeKind,
)


class Graph(ApplicationGraph):
    """
    Backwards-compatible graph façade.

    New code should use ApplicationGraph directly for application
    architecture and a dedicated execution graph for execution state.

    This class exists temporarily so older X337 modules continue
    working during graph migration.
    """

    def contains_kind(
        self,
        kind: NodeKind | str,
    ) -> bool:
        return bool(self.find_by_kind(kind))

    def connected(
        self,
        node_id: str,
        relation: EdgeRelation | str | None = None,
    ) -> list[GraphNode]:
        return (
            self.children(node_id, relation)
            + self.parents(node_id, relation)
        )
