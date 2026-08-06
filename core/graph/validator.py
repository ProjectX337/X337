from __future__ import annotations

from dataclasses import dataclass

from core.graph.graph import Graph


@dataclass(slots=True)
class GraphIssue:
    level: str
    message: str


class GraphValidator:

    def validate(self, graph: Graph) -> list[GraphIssue]:

        issues: list[GraphIssue] = []

        #
        # Missing nodes
        #

        for edge in graph.edges:

            if edge.source not in graph.nodes:
                issues.append(
                    GraphIssue(
                        "error",
                        f"Missing source node: {edge.source}",
                    )
                )

            if edge.target not in graph.nodes:
                issues.append(
                    GraphIssue(
                        "error",
                        f"Missing target node: {edge.target}",
                    )
                )

        #
        # Duplicate edges
        #

        seen = set()

        for edge in graph.edges:

            key = (
                edge.source,
                edge.target,
                edge.relation,
            )

            if key in seen:

                issues.append(
                    GraphIssue(
                        "warning",
                        f"Duplicate edge {key}",
                    )
                )

            seen.add(key)

        #
        # Self loops
        #

        for edge in graph.edges:

            if edge.source == edge.target:

                issues.append(
                    GraphIssue(
                        "warning",
                        f"Self-loop on {edge.source}",
                    )
                )

        #
        # Orphan nodes
        #

        connected = set()

        for edge in graph.edges:
            connected.add(edge.source)
            connected.add(edge.target)

        for node_id in graph.nodes:

            if node_id not in connected:

                issues.append(
                    GraphIssue(
                        "warning",
                        f"Orphan node: {node_id}",
                    )
                )

        #
        # Isolated graph
        #

        if graph.nodes and not graph.edges:

            issues.append(
                GraphIssue(
                    "warning",
                    "Graph contains nodes but no relationships.",
                )
            )

        return issues
