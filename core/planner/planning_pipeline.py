from __future__ import annotations

from core.cognition.cognitive_state import CognitiveState


class PlanningPipeline:

    def __init__(self, stages):

        self.stages = stages

    def run(
        self,
        state: CognitiveState,
    ):

        for stage in self.stages:

            stage.run(state)
