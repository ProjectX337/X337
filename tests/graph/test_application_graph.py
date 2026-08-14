from core.graph.models import (
    ApplicationGraph,
    GraphNode,
    NodeKind,
    GraphEdge,
    EdgeRelation,
)


def test_application_graph_contract():

    graph = ApplicationGraph()

    graph.add_node(
        GraphNode(
            id="dashboard",
            type=NodeKind.PAGE,
            name="Dashboard",
        )
    )

    graph.add_node(
        GraphNode(
            id="lesson_card",
            type=NodeKind.COMPONENT,
            name="LessonCard",
        )
    )

    graph.add_edge(
        GraphEdge(
            source="dashboard",
            target="lesson_card",
            type=EdgeRelation.RENDERS,
        )
    )

    result = graph.as_dict()

    assert len(result["nodes"]) == 2
    assert len(result["edges"]) == 1

    pages = graph.find_nodes(
        NodeKind.PAGE
    )

    assert pages[0].name == "Dashboard"
