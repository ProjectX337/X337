from __future__ import annotations

from core.planner.intent_classifier import IntentClassifier
from core.cognition.cognitive_state import CognitiveState
from core.planner.stages.base_stage import PlanningStage


class IntentClassifierStage(PlanningStage):
    """
    Executes the IntentClassifier and stores the result
    in the CognitiveState.
    """

    requires = {"parsed"}

    provides = {"intent"}

    def __init__(self):

        self.classifier = IntentClassifier()

    # ---------------------------------------------------------

    def run(
        self,
        context: CognitiveState,
    ) -> None:

        context.intent = self.classifier.classify(
            context.parsed,
        )
