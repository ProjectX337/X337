from __future__ import annotations

from core.planner.intent_classifier import IntentClassifier
from core.planner.planning_context import PlanningContext
from core.planner.stages.base_stage import PlanningStage


class IntentClassifierStage(PlanningStage):
    """
    Executes the IntentClassifier and stores the result
    in the PlanningContext.
    """

    requires = {"parsed"}

    provides = {"intent"}

    def __init__(self):

        self.classifier = IntentClassifier()

    # ---------------------------------------------------------

    def run(
        self,
        context: PlanningContext,
    ) -> None:

        context.intent = self.classifier.classify(
            context.parsed,
        )
