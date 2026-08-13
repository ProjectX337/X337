from __future__ import annotations

from core.planner.stages.base_stage import PlanningStage
from core.cognition.cognitive_state import CognitiveState
from core.graph.change_planner import ChangePlanner


class ChangePlanningStage(PlanningStage):
    """
    Converts graph evolution requests into ChangePlans.
    """

    name = "change_planning"

    requires = {
        "application_graph",
        "change_requests",
    }

    provides = {
        "change_plans",
    }

    def run(
        self,
        state: CognitiveState,
    ) -> None:

        if not state.application_graph:
            state.change_plans = []
            return

        planner = ChangePlanner(
            state.application_graph
        )

        state.change_plans = [
            planner.create_plan(request)
            for request in state.change_requests
        ]
