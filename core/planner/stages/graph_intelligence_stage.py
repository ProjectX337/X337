from __future__ import annotations

from core.planner.stages.base_stage import PlanningStage

from core.intelligence.intelligence_runtime import (
    GraphIntelligenceRuntime,
)


class GraphIntelligenceStage(PlanningStage):
    """
    Runs intelligence analysis over the canonical
    ApplicationGraph.

    Input:
        state.application_graph

    Output:
        state.graph_intelligence
    """

    name = "graph_intelligence"

    def run(self, state):

        runtime = GraphIntelligenceRuntime(
            state.application_graph
        )

        state.graph_intelligence = (
            runtime.analyze()
        )

        return state
