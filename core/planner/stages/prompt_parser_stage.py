from __future__ import annotations

from core.cognition.cognitive_state import CognitiveState
from core.planner.stages.base_stage import PlanningStage
from core.planner.prompt_parser import PromptParser


class PromptParserStage(PlanningStage):

    requires = set()

    provides = {"parsed"}

    def __init__(self):

        self.parser = PromptParser()

    def run(
        self,
        state: CognitiveState,
    ):

        state.parsed = self.parser.parse(
            state.prompt
        )
