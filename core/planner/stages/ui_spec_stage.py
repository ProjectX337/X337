from __future__ import annotations

from core.planner.stages.base_stage import PlanningStage
from core.cognition.cognitive_state import CognitiveState
from core.planner.ui_planner import UIPlanner


class UISpecStage(PlanningStage):
    """
    Creates UISpec from planner outputs.
    """

    requires = {
        "intent",
        "capabilities",
    }

    provides = {
        "ui_spec",
    }

    def __init__(self):

        self.planner = UIPlanner()


    def run(
        self,
        context: CognitiveState,
    ) -> None:

        context.ui_spec = (
            self.planner.plan(
                intent=context.intent,
                capabilities=context.capabilities,
            features=context.feature_models,
            design=context.design_spec,
            product_profile=context.product_profile,
        graph=context.task_graph,
            )
        )
