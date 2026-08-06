from __future__ import annotations

from core.cognition.cognitive_state import CognitiveState
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
        context: CognitiveState,
    ) -> None:

        context.technologies = self.resolver.resolve(
            context.stack,
        )
