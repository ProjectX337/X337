from __future__ import annotations

from dataclasses import dataclass

from core.graph.models import ApplicationGraph


@dataclass(slots=True)
class GraphIssue:
    level: str
    message: str


class GraphValidator:

    def validate(
        self,
        graph: ApplicationGraph,
    ) -> list[GraphIssue]:

        issues: list[GraphIssue] = []

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

        seen = set()

        for edge in graph.edges:

            key = (
                edge.source,
                edge.target,
                edge.type,
            )

            if key in seen:
                issues.append(
                    GraphIssue(
                        "warning",
                        f"Duplicate edge {key}",
                    )
                )

            seen.add(key)

        for edge in graph.edges:

            if edge.source == edge.target:
                issues.append(
                    GraphIssue(
                        "warning",
                        f"Self-loop on {edge.source}",
                    )
                )

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

        if graph.nodes and not graph.edges:

            issues.append(
                GraphIssue(
                    "warning",
                    "Graph contains nodes but no relationships.",
                )
            )

        return issues
