from __future__ import annotations

from core.graph.application_graph import (
    ApplicationGraph,
    GraphNodeType,
    GraphEdgeType,
)

from core.graph.intelligence.architecture_report import (
    ArchitectureReport,
)


class ArchitectureAnalyzer:
    """
    Detects architectural gaps
    in an ApplicationGraph.
    """

    def analyze(
        self,
        graph: ApplicationGraph,
    ) -> ArchitectureReport:

        risks = []
        warnings = []
        recommendations = []

        feature_ids = {
            node.id
            for node in graph.find_nodes(
                GraphNodeType.FEATURE
            )
        }

        implemented_features = {
            edge.source
            for edge in graph.edges
            if edge.type
            in (
                GraphEdgeType.IMPLEMENTS,
                GraphEdgeType.RENDERS,
            )
        }

        for feature_id in feature_ids:
            if feature_id not in implemented_features:
                risks.append(
                    f"incomplete-feature:{feature_id}"
                )

                recommendations.append(
                    f"Add implementation surface for {feature_id}"
                )

        return ArchitectureReport(
            risks=risks,
            warnings=warnings,
            recommendations=recommendations,
            metadata={
                "source": "architecture_analyzer",
            },
        )
