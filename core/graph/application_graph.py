from __future__ import annotations

from dataclasses import dataclass, field

from core.graph.nodes import GraphNode
from core.graph.edges import GraphEdge


@dataclass
class ApplicationGraph:

    nodes: dict[str, GraphNode] = field(
        default_factory=dict
    )

    edges: list[GraphEdge] = field(
        default_factory=list
    )

    def add_node(
        self,
        node: GraphNode,
    ):
        self.nodes[node.id] = node

    def add_edge(
        self,
        edge: GraphEdge,
    ):
        self.edges.append(edge)

    def get_node(
        self,
        node_id: str,
    ):
        return self.nodes.get(node_id)
