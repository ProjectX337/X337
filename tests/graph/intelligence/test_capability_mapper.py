from core.graph.models import (
    ApplicationGraph,
    GraphNode,
    NodeKind,
)

from core.graph.intelligence.capability_mapper import (
    CapabilityMapper,
)


def test_capability_mapper_finds_feature():

    graph = ApplicationGraph()

    graph.add_node(
        GraphNode(
            id="feature.learning",
            type=NodeKind.FEATURE,
            name="adaptive learning",
        )
    )

    result = CapabilityMapper().map(
        graph,
        "adaptive learning",
    )

    assert (
        "feature.learning"
        in result
    )
