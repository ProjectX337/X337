from __future__ import annotations

from core.cognition.cognitive_state import CognitiveState
from core.planner.stages.base_stage import PlanningStage
from core.planner.design_reasoner import DesignReasoner


class DesignInferenceStage(PlanningStage):
    """
    Infers product design decisions.
    """

    requires = {
        "intent",
    }

    provides = {
        "design_spec",
    }

    def __init__(self):
        self.reasoner = DesignReasoner()

    def run(
        self,
        context: CognitiveState,
    ) -> None:

        context.design_spec = self.reasoner.infer(
            intent=context.intent,
            capabilities=context.capabilities,
            features=context.feature_models,
            product_profile=context.product_profile,
            architecture=context.stack,
            technologies=context.technologies,
        )
