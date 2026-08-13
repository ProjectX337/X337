from core.graph.builders.product_spec_builder import (
    ProductSpecGraphBuilder,
)

from core.intelligence.product_spec import (
    ProductSpec,
)

from core.graph.application_graph import (
    GraphNodeType,
)


def test_product_spec_builds_application_graph():

    spec = ProductSpec(
        name="AI Tutor",
        product_type="education",
        features=[
            "adaptive learning"
        ],
        entities=[
            "student"
        ],
    )

    graph = ProductSpecGraphBuilder().build(spec)

    features = graph.find_nodes(
        GraphNodeType.FEATURE
    )

    entities = graph.find_nodes(
        GraphNodeType.ENTITY
    )

    assert features[0].name == "adaptive learning"
    assert entities[0].name == "student"
