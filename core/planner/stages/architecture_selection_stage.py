from __future__ import annotations

from core.planner.architecture_selector import ArchitectureSelector
from core.planner.planning_context import PlanningContext
from core.planner.stages.base_stage import PlanningStage


class ArchitectureSelectionStage(PlanningStage):
    """
    Selects candidate architectures based on the detected intent.
    """

    requires = {"intent"}

    provides = {"architecture_candidates"}

    def __init__(self):

        self.selector = ArchitectureSelector()

    # ---------------------------------------------------------

    def run(
        self,
        context: PlanningContext,
    ) -> None:

        context.architecture_candidates = self.selector.select(
            context.intent,
        )
