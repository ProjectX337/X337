from core.planner.stages.base_stage import PlanningStage

from core.intelligence.pipeline.product_intelligence_pipeline import (
    ProductIntelligencePipeline,
)

from core.intelligence.models import ProductIntent

from core.intelligence.reasoning.capability_reasoner import (
    CapabilityReasoner,
)


class ProductIntelligenceStage(PlanningStage):
    """
    Converts cognitive intent into
    product and architecture intelligence.
    """

    requires = {
        "product_intent",
    }

    provides = {
        "product_understanding",
        "product_spec",
        "capability_hypotheses",
    }

    def __init__(self):
        self.pipeline = (
            ProductIntelligencePipeline()
        )

    def run(
        self,
        state,
    ):
        if state.product_intent is None:
            state.product_intent = ProductIntent(
                domain=state.prompt
            )

        result = self.pipeline.run(
            state.product_intent
        )

        state.product_understanding = (
            result["understanding"]
        )

        state.capability_hypotheses = (
            CapabilityReasoner()
            .reason(
                state.product_understanding
            )
        )

        state.product_spec = (
            result["spec"]
        )

        # Compatibility:
        # Direct stage callers historically expected
        # ProductIntelligenceStage to expose a graph.
        # Canonical pipeline ownership belongs to ApplicationGraphStage.
        if not hasattr(state, "application_graph") or not state.application_graph.nodes:
            state.application_graph = (
                result["graph"]
            )

        return state

    # Backward compatibility for direct stage callers.
    # PlanningPipeline uses run().
    def execute(
        self,
        state,
    ):
        return self.run(state)
