from core.graph.analysis import GraphAnalyzer
from core.graph.models import ApplicationGraph
from core.graph.models import (
    GraphNode,
    NodeKind,
)
from core.graph.models import (
    GraphEdge,
    EdgeRelation,
)


def test_graph_analyzer_summary():

    graph = ApplicationGraph()

    page = GraphNode(
        id="page.login",
        type=NodeKind.PAGE,
        name="Login",
    )

    component = GraphNode(
        id="component.form",
        type=NodeKind.COMPONENT,
        name="Form",
    )

    graph.add_node(page)
    graph.add_node(component)

    graph.add_edge(
        GraphEdge(
            source=page.id,
            target=component.id,
            type=EdgeRelation.RENDERS,
        )
    )

    analyzer = GraphAnalyzer(graph)

    summary = analyzer.summary()

    assert summary["nodes"] == 2
    assert summary["edges"] == 1
    assert summary["types"]["page"] == 1
    assert summary["types"]["component"] == 1
