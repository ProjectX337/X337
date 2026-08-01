from __future__ import annotations

from core.ai.prompt_parser import PromptParser
from core.planner.project_planner import ProjectPlanner


class PlannerAgent:

    def __init__(self):

        self.parser = PromptParser()

        self.planner = ProjectPlanner()


    def build(
        self,
        message: str,
    ):

        intent = self.parser.parse(
            message
        )

        spec = self.planner.plan(
            intent.description
        )

        return spec
