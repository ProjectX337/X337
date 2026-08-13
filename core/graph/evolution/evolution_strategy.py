from __future__ import annotations

from core.graph.evolution.models import (
    EvolutionPlan,
    ImpactReport,
    GraphChangeSet,
)


class EvolutionStrategy:
    """
    Converts graph changes and impacts
    into engineering actions.
    """

    def generate(
        self,
        changes: GraphChangeSet,
        impact: ImpactReport,
    ) -> EvolutionPlan:

        actions = []

        for node in changes.added_nodes:
            actions.append(
                f"implement new architecture surface: {node}"
            )

        for node in changes.removed_nodes:
            actions.append(
                f"remove obsolete architecture surface: {node}"
            )

        if not actions:
            actions.append(
                "no architectural changes required"
            )

        priority = (
            "high"
            if impact.severity == "high"
            else "normal"
        )

        return EvolutionPlan(
            actions=actions,
            priority=priority,
            metadata={
                "source": "evolution_strategy",
            },
        )
