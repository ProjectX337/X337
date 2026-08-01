from __future__ import annotations

from core.planner.stages.base_stage import PlanningStage
from core.planner.planning_context import PlanningContext
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
        context: PlanningContext,
    ) -> None:

        context.ui_spec = (
            self.planner.plan(
                intent=context.intent,
                capabilities=context.capabilities,
            features=context.feature_models,
            )
        )
