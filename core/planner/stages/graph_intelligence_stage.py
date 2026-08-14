from __future__ import annotations

from core.cognition.cognitive_state import CognitiveState
from core.planner.stages.base_stage import PlanningStage

from core.graph.intelligence.runtime import (
    GraphIntelligenceRuntime,
)


class GraphIntelligenceStage(PlanningStage):

    name = "graph_intelligence"

    requires = {
        "application_graph",
    }

    provides = {
        "graph_intelligence",
    }

    def run(
        self,
        state: CognitiveState,
    ) -> None:

        runtime = GraphIntelligenceRuntime(
            state.application_graph
        )

        state.graph_intelligence = (
            runtime.analyze()
        )
