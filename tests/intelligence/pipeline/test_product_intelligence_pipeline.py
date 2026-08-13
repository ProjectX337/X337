from core.intelligence.pipeline.product_intelligence_pipeline import (
    ProductIntelligencePipeline,
)

from core.intelligence.models import (
    ProductIntent,
)

from core.graph.application_graph import (
    GraphNodeType,
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

    entities = result["graph"].find_nodes(
        GraphNodeType.ENTITY
    )

    assert entities[0].name == (
        "student"
    )
