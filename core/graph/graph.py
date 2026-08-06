from __future__ import annotations

from dataclasses import dataclass, field

from .edge import GraphEdge
from .graph_types import GraphNodeType
from .node import GraphNode


@dataclass(slots=True)
class Graph:
    """
    Central reasoning graph for X337.

    Every planner, generator and agent should
    eventually operate on this graph.
    """

    nodes: dict[str, GraphNode] = field(default_factory=dict)

    edges: list[GraphEdge] = field(default_factory=list)

    # ---------------------------------------------------------

    def add_node(self, node: GraphNode):
        self.nodes[node.id] = node

    # ---------------------------------------------------------

    def add_edge(self, edge: GraphEdge):
        self.edges.append(edge)

    # ---------------------------------------------------------

    def has_node(self, node_id: str) -> bool:
        return node_id in self.nodes

    # ---------------------------------------------------------

    def get(self, node_id: str) -> GraphNode:
        return self.nodes[node_id]

    # ---------------------------------------------------------

    def remove_node(self, node_id: str):

        if node_id not in self.nodes:
            return

        del self.nodes[node_id]

        self.edges = [
            edge
            for edge in self.edges
            if edge.source != node_id
            and edge.target != node_id
        ]

    # ---------------------------------------------------------

    def neighbors(self, node_id: str):

        return [
            self.nodes[edge.target]
            for edge in self.edges
            if edge.source == node_id
            and edge.target in self.nodes
        ]

    # ---------------------------------------------------------

    def children(
        self,
        node_id: str,
        relation: str | None = None,
    ):

        return [
            self.nodes[edge.target]
            for edge in self.edges
            if edge.source == node_id
            and (
                relation is None
                or edge.relation == relation
            )
            and edge.target in self.nodes
        ]

    # ---------------------------------------------------------

    def parents(
        self,
        node_id: str,
        relation: str | None = None,
    ):

        return [
            self.nodes[edge.source]
            for edge in self.edges
            if edge.target == node_id
            and (
                relation is None
                or edge.relation == relation
            )
            and edge.source in self.nodes
        ]

    # ---------------------------------------------------------

    def connected(
        self,
        node_id: str,
        relation: str | None = None,
    ):

        return (
            self.children(node_id, relation)
            +
            self.parents(node_id, relation)
        )

    # ---------------------------------------------------------

    def contains_kind(
        self,
        kind: GraphNodeType,
    ) -> bool:

        return any(
            node.kind == kind
            for node in self.nodes.values()
        )

    # ---------------------------------------------------------

    def find_by_kind(
        self,
        kind: GraphNodeType,
    ):

        return [
            node
            for node in self.nodes.values()
            if node.kind == kind
        ]

    # ---------------------------------------------------------

    def find_by_label(
        self,
        label: str,
    ):

        return [
            node
            for node in self.nodes.values()
            if node.label == label
        ]
