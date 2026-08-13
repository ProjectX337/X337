from __future__ import annotations

from core.graph.application_graph import (
    ApplicationGraph,
    GraphNodeType,
)


class CapabilityMapper:
    """
    Maps product capabilities to
    application architecture nodes.
    """

    def map(
        self,
        graph: ApplicationGraph,
        capability: str,
    ) -> list[str]:

        matches = []

        for node in graph.find_nodes(
            GraphNodeType.FEATURE
        ):
            if node.name == capability:
                matches.append(node.id)

        return matches
