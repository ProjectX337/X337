from __future__ import annotations

from core.knowledge.product_profile_reasoner import ProductProfileReasoner
from core.cognition.cognitive_state import CognitiveState
from core.planner.stages.base_stage import PlanningStage


class ProductProfileStage(PlanningStage):
    """
    Selects the best product archetype.
    """

    requires = {
        "intent",
        "capabilities",
        "feature_models",
    }

    provides = {
        "product_profile",
    }

    def __init__(self):
        self.reasoner = ProductProfileReasoner()

    def run(
        self,
        context: CognitiveState,
    ) -> None:

        context.product_profile = self.reasoner.infer(
            intent=context.intent,
            capabilities=context.capabilities,
            features=context.feature_models,
        )
