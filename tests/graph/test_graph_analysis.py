from core.graph.analysis import GraphAnalyzer
from core.graph.application_graph import ApplicationGraph
from core.graph.nodes import (
    PageNode,
    ComponentNode,
)
from core.graph.edges import (
    GraphEdge,
    EdgeType,
)


def test_graph_analyzer_summary():

    graph = ApplicationGraph()

    page = PageNode(
        id="page.login",
        name="Login",
    )

    component = ComponentNode(
        id="component.form",
        name="Form",
    )

    graph.add_node(page)
    graph.add_node(component)

    graph.add_edge(
        GraphEdge(
            source=page.id,
            target=component.id,
            edge_type=EdgeType.RENDERS,
        )
    )

    analyzer = GraphAnalyzer(graph)

    summary = analyzer.summary()

    assert summary["nodes"] == 2
    assert summary["edges"] == 1
    assert summary["types"]["page"] == 1
    assert summary["types"]["component"] == 1
