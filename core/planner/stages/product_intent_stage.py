from __future__ import annotations

from core.cognition.cognitive_state import CognitiveState
from core.intelligence.intent_analyzer import ProductIntentAnalyzer
from core.planner.stages.base_stage import PlanningStage


class ProductIntentStage(PlanningStage):
    """
    Generates canonical product understanding
    from the parsed prompt.
    """

    requires = {"parsed"}

    provides = {"product_intent"}

    def __init__(self):

        self.analyzer = ProductIntentAnalyzer()

    # ---------------------------------------------------------

    def run(
        self,
        context: CognitiveState,
    ) -> None:

        context.product_intent = self.analyzer.analyze(
            context.parsed,
        )
