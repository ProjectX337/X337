from __future__ import annotations

from core.planner.planning_context import PlanningContext
from core.planner.stages.base_stage import PlanningStage
from core.planner.technology_resolver import TechnologyResolver


class TechnologyResolverStage(PlanningStage):
    """
    Resolves implementation technologies for the selected
    architecture stack.
    """

    requires = {
        "stack",
    }

    provides = {
        "technologies",
    }

    def __init__(self):

        self.resolver = TechnologyResolver()

    # ---------------------------------------------------------

    def run(
        self,
        context: PlanningContext,
    ) -> None:

        context.technologies = self.resolver.resolve(
            context.stack,
        )
