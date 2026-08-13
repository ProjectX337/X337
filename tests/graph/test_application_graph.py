from core.graph.application_graph import (
    ApplicationGraph,
    GraphNode,
    GraphNodeType,
    GraphEdge,
    GraphEdgeType,
)


def test_application_graph_contract():

    graph = ApplicationGraph()

    graph.add_node(
        GraphNode(
            id="dashboard",
            type=GraphNodeType.PAGE,
            name="Dashboard",
        )
    )

    graph.add_node(
        GraphNode(
            id="lesson_card",
            type=GraphNodeType.COMPONENT,
            name="LessonCard",
        )
    )

    graph.add_edge(
        GraphEdge(
            source="dashboard",
            target="lesson_card",
            type=GraphEdgeType.RENDERS,
        )
    )

    result = graph.as_dict()

    assert len(result["nodes"]) == 2
    assert len(result["edges"]) == 1

    pages = graph.find_nodes(
        GraphNodeType.PAGE
    )

    assert pages[0].name == "Dashboard"
