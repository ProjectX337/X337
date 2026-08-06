from __future__ import annotations

from core.cognition.cognitive_state import CognitiveState
from core.planner.stages.base_stage import PlanningStage
from core.planner.prompt_parser import PromptParser


class PromptParserStage(PlanningStage):

    requires = set()

    provides = {"parsed_prompt"}

    def __init__(self):

        self.parser = PromptParser()

    def run(
        self,
        state: CognitiveState,
    ):

        state.parsed_prompt = self.parser.parse(
            state.prompt
        )
