from __future__ import annotations

from core.graph.models import (
    ApplicationGraph,
    NodeKind,
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
            NodeKind.FEATURE
        ):
            if node.name == capability:
                matches.append(node.id)

        return matches
