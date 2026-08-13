from core.intelligence.pipeline.product_intelligence_pipeline import (
    ProductIntelligencePipeline,
)

from core.intelligence.models import (
    ProductIntent,
)


def test_product_intelligence_pipeline():

    result = ProductIntelligencePipeline().run(
        ProductIntent(
            domain="AI Tutor",
            entities=[
                "student"
            ],
        )
    )

    assert result["understanding"] is not None

    assert result["spec"].name == (
        "AI Tutor"
    )

