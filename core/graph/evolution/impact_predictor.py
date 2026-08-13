from __future__ import annotations

from core.graph.application_graph import ApplicationGraph
from core.graph.evolution.models import (
    GraphChangeSet,
    ImpactReport,
)


class ImpactPredictor:
    """
    Predicts affected architecture surfaces.
    """

    def predict(
        self,
        graph: ApplicationGraph,
        changes: GraphChangeSet,
    ) -> ImpactReport:

        affected = []

        for node_id in changes.added_nodes:
            affected.append(node_id)

        severity = (
            "high"
            if len(affected) > 3
            else "medium"
            if affected
            else "low"
        )

        return ImpactReport(
            affected_nodes=affected,
            severity=severity,
            metadata={
                "source": "impact_predictor",
            },
        )
