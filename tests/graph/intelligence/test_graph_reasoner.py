from core.graph.models import (
    ApplicationGraph,
    GraphNode,
    NodeKind,
)

from core.graph.intelligence.graph_reasoner import (
    GraphReasoner,
)


def test_graph_reasoner_extracts_product_insights():

    graph = ApplicationGraph()

    graph.add_node(
        GraphNode(
            id="feature.learning",
            type=NodeKind.FEATURE,
            name="adaptive learning",
        )
    )

    graph.add_node(
        GraphNode(
            id="page.dashboard",
            type=NodeKind.PAGE,
            name="Dashboard",
        )
    )

    insight = GraphReasoner().analyze(
        graph
    )

    assert (
        "adaptive learning"
        in insight.capabilities
    )

    assert (
        "Dashboard"
        in insight.user_experiences
    )

    assert (
        "feature-driven-application"
        in insight.architecture_patterns
    )
