from core.graph.application_graph import ApplicationGraph
from core.graph.nodes import (
    PageNode,
    ComponentNode,
)
from core.graph.edges import (
    GraphEdge,
    EdgeType,
)


def test_application_graph_nodes_and_edges():

    graph = ApplicationGraph()

    page = PageNode(
        id="page.dashboard",
        name="Dashboard",
    )

    component = ComponentNode(
        id="component.chart",
        name="Chart",
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

    assert len(graph.nodes) == 2
    assert len(graph.edges) == 1
    assert graph.edges[0].edge_type == EdgeType.RENDERS
