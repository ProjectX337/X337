from __future__ import annotations

from core.planner.features.feature_planner import FeaturePlanner
from core.planner.planning_context import PlanningContext
from core.planner.stages.base_stage import PlanningStage


class FeaturePlannerStage(PlanningStage):
    """
    Converts capabilities into FeatureSpec models.
    """

    requires = {
        "capabilities",
    }

    provides = {
        "features",
    }

    def __init__(self):
        self.planner = FeaturePlanner()

    def run(
        self,
        context: PlanningContext,
    ) -> None:

        context.features = (
            self.planner.plan(
                context.capabilities
            )
        )
