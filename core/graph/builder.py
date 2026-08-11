from __future__ import annotations

from core.graph.models import ApplicationGraph
from core.graph.models import (
    EdgeRelation,
    GraphEdge,
    GraphNode,
    NodeKind,
)


class GraphBuilder:
    """
    Compatibility builder for the canonical graph model.
    """

    def __init__(self, graph: ApplicationGraph):
        self.graph = graph

    def add_node(
        self,
        node_id: str,
        kind: NodeKind | str,
        label: str,
        **data,
    ) -> None:

        self.graph.add_node(
            GraphNode(
                id=node_id,
                kind=kind,
                name=label,
                data=data,
            )
        )

    def connect(
        self,
        source: str,
        target: str,
        relation: EdgeRelation | str,
    ) -> None:

        self.graph.add_edge(
            GraphEdge(
                source=source,
                target=target,
                relation=relation,
            )
        )
