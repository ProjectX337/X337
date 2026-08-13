from core.graph.application_graph import (
    ApplicationGraph,
    GraphNode,
    GraphNodeType,
)

from core.graph.intelligence.capability_mapper import (
    CapabilityMapper,
)


def test_capability_mapper_finds_feature():

    graph = ApplicationGraph()

    graph.add_node(
        GraphNode(
            id="feature.learning",
            type=GraphNodeType.FEATURE,
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
