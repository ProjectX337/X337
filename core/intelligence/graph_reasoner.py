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
    Produces architectural intelligence
    from an ApplicationGraph.
    """

    def analyze(
        self,
        graph: ApplicationGraph,
    ) -> GraphInsight:

        insight = GraphInsight()

        self._detect_patterns(
            graph,
            insight,
        )

        self._detect_risks(
            graph,
            insight,
        )

        return insight


    def _detect_patterns(
        self,
        graph: ApplicationGraph,
        insight: GraphInsight,
    ) -> None:

        if graph.find_nodes(NodeKind.PROJECT):
            insight.architecture_patterns.append(
                "application_graph"
            )

        if graph.find_nodes(NodeKind.SOURCE_FILE):
            insight.architecture_patterns.append(
                "source_managed_application"
            )

        if graph.find_nodes(NodeKind.COMPONENT):
            insight.architecture_patterns.append(
                "component_based_architecture"
            )

        if graph.find_nodes(NodeKind.PAGE):
            insight.capabilities.append(
                "multi_page_application"
            )


    def _detect_risks(
        self,
        graph: ApplicationGraph,
        insight: GraphInsight,
    ) -> None:

        features = graph.find_nodes(
            NodeKind.FEATURE
        )

        for feature in features:

            pages = [
                node
                for node in graph.children(feature.id)
                if node.kind == NodeKind.PAGE
            ]

            if not pages:
                insight.risks.append(
                    f"feature_without_page:{feature.name}"
                )
