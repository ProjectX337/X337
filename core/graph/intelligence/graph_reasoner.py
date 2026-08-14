from __future__ import annotations

from core.graph.models import (
    ApplicationGraph,
    NodeKind,
)

from core.graph.intelligence.models import (
    GraphInsight,
)


class GraphReasoner:
    """
    Derives product-level meaning
    from application architecture.
    """

    def analyze(
        self,
        graph: ApplicationGraph,
    ) -> GraphInsight:

        capabilities = [
            node.name
            for node in graph.find_nodes(
                NodeKind.FEATURE
            )
        ]

        user_experiences = [
            node.name
            for node in graph.find_nodes(
                NodeKind.PAGE
            )
        ]

        patterns = []

        if capabilities and user_experiences:
            patterns.append(
                "feature-driven-application"
            )

        return GraphInsight(
            capabilities=capabilities,
            user_experiences=user_experiences,
            architecture_patterns=patterns,
            metadata={
                "source": "application_graph",
            },
        )
