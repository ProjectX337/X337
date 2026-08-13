from core.intelligence.pipeline.product_intelligence_pipeline import (
    ProductIntelligencePipeline,
)

from core.intelligence.models import ProductIntent


class ProductIntelligenceStage:
    """
    Converts cognitive intent into
    product and architecture intelligence.
    """

    def __init__(self):
        self.pipeline = (
            ProductIntelligencePipeline()
        )

    def execute(
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

        state.product_spec = (
            result["spec"]
        )

        state.application_graph = (
            result["graph"]
        )

        return state
