from __future__ import annotations

from core.planner.planning_context import PlanningContext
from core.planner.prompt_parser import PromptParser
from core.planner.stages.base_stage import PlanningStage


class PromptParserStage(PlanningStage):
    """
    Executes the PromptParser and stores the result
    in the PlanningContext.
    """

    requires = set()

    provides = {"parsed"}

    def __init__(self):

        self.parser = PromptParser()

    # ---------------------------------------------------------

    def run(
        self,
        context: PlanningContext,
    ) -> None:

        context.parsed = self.parser.parse(
            context.prompt,
        )
