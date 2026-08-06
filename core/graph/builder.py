from __future__ import annotations

from core.graph.graph import Graph
from core.graph.node import GraphNode
from core.graph.edge import GraphEdge
from core.graph.graph_types import GraphNodeType


class GraphBuilder:

    def __init__(self, graph: Graph):

        self.graph = graph

    def add_node(
        self,
        node_id: str,
        kind: GraphNodeType,
        label: str,
        **data,
    ):

        self.graph.add_node(
            GraphNode(
                id=node_id,
                kind=kind.value,
                label=label,
                data=data,
            )
        )

    def connect(
        self,
        source: str,
        target: str,
        relation: str,
    ):

        self.graph.add_edge(
            GraphEdge(
                source=source,
                target=target,
                relation=relation,
            )
        )