from __future__ import annotations

from core.cognition.cognitive_state import CognitiveState
from core.intelligence.capability_reasoner import CapabilityReasoner
from core.planner.stages.base_stage import PlanningStage


class CapabilityReasonerStage(PlanningStage):
    """
    Generates semantic capability hypotheses
    from product intelligence.
    """

    requires = {"product_intent"}

    provides = {"capability_candidates"}

    def __init__(self):
        self.reasoner = CapabilityReasoner()

    def run(
        self,
        state: CognitiveState,
    ) -> None:

        state.capability_candidates = (
            self.reasoner.reason(
                state.product_intent
            )
        )
