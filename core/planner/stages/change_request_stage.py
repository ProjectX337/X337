from __future__ import annotations

from core.planner.stages.base_stage import PlanningStage
from core.cognition.cognitive_state import CognitiveState
from core.graph.change import ChangeRequest, ChangeType


class ChangeRequestStage(PlanningStage):
    """
    Creates initial application evolution requests.

    This stage describes desired changes.
    ChangePlanningStage converts them into executable plans.
    """

    name = "change_requests"

    requires = {
        "feature_models",
        "application_graph",
    }

    provides = {
        "change_requests",
    }

    def run(
        self,
        state: CognitiveState,
    ) -> None:

        state.change_requests = []

        for feature in state.feature_models:

            state.change_requests.append(
                ChangeRequest(
                    target_node=f"feature.{feature.name}",
                    change_type=ChangeType.ADD,
                    description=f"Implement feature {feature.name}",
                )
            )
