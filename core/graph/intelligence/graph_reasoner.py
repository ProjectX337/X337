from __future__ import annotations

from core.graph.application_graph import (
    ApplicationGraph,
    GraphNodeType,
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
                GraphNodeType.FEATURE
            )
        ]

        user_experiences = [
            node.name
            for node in graph.find_nodes(
                GraphNodeType.PAGE
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
