from __future__ import annotations

from core.graph.models import ApplicationGraph
from core.graph.models import EdgeRelation


class GraphQuery:

    def __init__(
        self,
        graph: ApplicationGraph,
    ):
        self.graph = graph

    def find_pages_for_feature(
        self,
        feature_id: str,
    ):
        pages = []

        for edge in self.graph.edges:
            if (
                edge.source == feature_id
                and edge.type == EdgeRelation.IMPLEMENTS
            ):
                node = self.graph.get_node(
                    edge.target
                )

                if node:
                    pages.append(node)

        return pages

    def find_components_for_page(
        self,
        page_id: str,
    ):
        components = []

        for edge in self.graph.edges:
            if (
                edge.source == page_id
                and edge.type == EdgeRelation.RENDERS
            ):
                node = self.graph.get_node(
                    edge.target
                )

                if node:
                    components.append(node)

        return components

    def find_dependencies(
        self,
        node_id: str,
    ):
        results = []

        for edge in self.graph.edges:
            if edge.source == node_id:
                node = self.graph.get_node(
                    edge.target
                )

                if node:
                    results.append(node)

        return results

    def find_impact_surface(
        self,
        node_id: str,
    ):
        visited = set()
        queue = [node_id]
        impacted = []

        while queue:

            current = queue.pop(0)

            if current in visited:
                continue

            visited.add(current)

            for edge in self.graph.edges:

                if edge.source == current:
                    target = self.graph.get_node(
                        edge.target
                    )

                    if target:
                        impacted.append(target)
                        queue.append(
                            target.id
                        )

        return impacted
