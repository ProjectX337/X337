from __future__ import annotations

from core.planner.stages.base_stage import PlanningStage
from core.cognition.cognitive_state import CognitiveState
from core.planner.feature_planner import FeaturePlanner


class FeatureStage(PlanningStage):
    """
    Creates FeatureSpec objects from planner outputs.
    """

    requires = {
        "parsed",
        "capabilities",
    }

    provides = {
        "feature_models",
    }

    def __init__(self):

        self.planner = FeaturePlanner()

    def run(
        self,
        context: CognitiveState,
    ) -> None:

        context.feature_models = (
            self.planner.plan(
                parsed=context.parsed,
                capabilities=context.capabilities,
            )
        )
