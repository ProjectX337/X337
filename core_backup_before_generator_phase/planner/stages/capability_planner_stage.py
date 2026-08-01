from __future__ import annotations

from core.planner.capability_planner import CapabilityPlanner
from core.planner.planning_context import PlanningContext
from core.planner.stages.base_stage import PlanningStage


class CapabilityPlannerStage(PlanningStage):
    """
    Executes the CapabilityPlanner and stores the
    resulting capability matches in the PlanningContext.
    """

    requires = {"parsed"}

    provides = {"capabilities"}

    def __init__(self):

        self.planner = CapabilityPlanner()

    # ---------------------------------------------------------

    def run(
        self,
        context: PlanningContext,
    ) -> None:

        context.capabilities = self.planner.plan(
            context.parsed,
        )
