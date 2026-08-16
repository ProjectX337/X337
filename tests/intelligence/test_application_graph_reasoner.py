from core.intelligence.graph_reasoner import (
    GraphReasoner,
)

from core.graph.models import (
    ApplicationGraph,
    GraphNode,
    NodeKind,
)


def test_detects_application_graph_pattern():

    graph = ApplicationGraph()

    graph.add_node(
        GraphNode(
            id="project.demo",
            kind=NodeKind.PROJECT,
            name="demo",
        )
    )

    insight = GraphReasoner().analyze(
        graph
    )

    assert (
        "application_graph"
        in insight.architecture_patterns
    )
