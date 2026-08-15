from __future__ import annotations

from collections import defaultdict

from core.graph.models import ApplicationGraph
from core.graph.models import EdgeRelation
from core.graph.models import NodeKind


class GraphAnalyzer:
    """
    Provides reasoning capabilities over ApplicationGraph.

    This layer does not mutate the graph.
    It extracts intelligence from the application model.
    """

    def __init__(
        self,
        graph: ApplicationGraph,
    ):
        self.graph = graph

    def node_count(
        self,
    ) -> int:
        return len(self.graph.nodes)

    def edge_count(
        self,
    ) -> int:
        return len(self.graph.edges)

    def count_by_type(
        self,
    ) -> dict[NodeKind, int]:

        counts = defaultdict(int)

        for node in self.graph.nodes.values():
            counts[node.kind] += 1

        return dict(counts)

    def find_orphans(
        self,
    ) -> list[str]:

        connected = set()

        for edge in self.graph.edges:
            connected.add(edge.source)
            connected.add(edge.target)

        return [
            node.id
            for node in self.graph.nodes.values()
            if node.id not in connected
        ]

    def find_dependencies(
        self,
        node_id: str,
    ):

        dependencies = []

        for edge in self.graph.edges:

            if (
                edge.source == node_id
                and edge.relation == EdgeRelation.REQUIRES
            ):
                node = self.graph.get_node(
                    edge.target
                )

                if node:
                    dependencies.append(node)

        return dependencies

    def summary(
        self,
    ) -> dict:

        return {
            "nodes": self.node_count(),
            "edges": self.edge_count(),
            "types": {
                key.value: value
                for key, value
                in self.count_by_type().items()
            },
            "orphans": self.find_orphans(),
        }
