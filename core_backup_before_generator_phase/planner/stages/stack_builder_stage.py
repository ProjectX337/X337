from __future__ import annotations

from core.planner.planning_context import PlanningContext
from core.planner.stack_builder import StackBuilder
from core.planner.stages.base_stage import PlanningStage


class StackBuilderStage(PlanningStage):
    """
    Builds the final architecture stack from the ranked
    architecture candidates.
    """

    requires = {
        "intent",
        "architecture_candidates",
    }

    provides = {
        "stack",
    }

    def __init__(self):

        self.builder = StackBuilder()

    # ---------------------------------------------------------

    def run(
        self,
        context: PlanningContext,
    ) -> None:

        context.stack = self.builder.build(
            context.architecture_candidates,
            context.intent,
        )
