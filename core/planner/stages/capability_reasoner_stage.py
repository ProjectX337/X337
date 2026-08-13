from __future__ import annotations

from core.cognition.cognitive_state import CognitiveState
from core.intelligence.capability_reasoner import CapabilityReasoner
from core.planner.stages.base_stage import PlanningStage


class CapabilityReasonerStage(PlanningStage):
    """
    Converts product intent into semantic capability candidates.
    """

    requires = {"product_intent"}

    provides = {"capability_candidates"}

    def __init__(self):

        self.reasoner = CapabilityReasoner()

    def run(
        self,
        context: CognitiveState,
    ) -> None:

        context.capability_candidates = (
            self.reasoner.reason(
                context.product_intent
            )
        )
