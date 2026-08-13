from core.intelligence.models import (
    ProductIntent,
    ProductUnderstanding,
)

from core.intelligence.synthesis import (
    ProductUnderstandingSynthesizer,
)

from core.intelligence.product_spec import (
    ProductSpec,
)

class ProductIntelligencePipeline:
    """
    Converts product reasoning into
    architectural intelligence.

    Prompt
        ->
    ProductIntent
        ->
    ProductUnderstanding
        ->
    ProductSpec
        ->
    ApplicationGraph
    """

    def __init__(self):
        self.synthesizer = (
            ProductUnderstandingSynthesizer()
        )

    def run(
        self,
        intent: ProductIntent,
    ):
        understanding = (
            self.synthesizer.synthesize(
                intent
            )
        )

        spec = ProductSpec(
            name=intent.domain,
            product_type=intent.domain,
            features=(
                understanding.capabilities
            ),
            entities=(
                understanding.entities
            ),
        )

        return {
            "understanding": understanding,
            "spec": spec,
        }
