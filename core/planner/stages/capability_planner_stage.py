from __future__ import annotations

from core.planner.capability_planner import CapabilityPlanner
from core.cognition.cognitive_state import CognitiveState
from core.planner.stages.base_stage import PlanningStage


class CapabilityPlannerStage(PlanningStage):
    """
    Executes the CapabilityPlanner and stores the
    resulting capability matches in the CognitiveState.
    """

    requires = {"parsed"}

    provides = {"capabilities"}

    def __init__(self):

        self.planner = CapabilityPlanner()

    # ---------------------------------------------------------

    def run(
        self,
        context: CognitiveState,
    ) -> None:

        context.capabilities = self.planner.plan(
            context.parsed,
        )
