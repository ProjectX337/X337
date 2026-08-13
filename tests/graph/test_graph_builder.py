from types import SimpleNamespace

from core.graph.graph_builder import GraphBuilder
from core.graph.edges import EdgeType


def test_ui_spec_builds_application_graph():

    ui_spec = SimpleNamespace(
        pages=[
            SimpleNamespace(
                name="Dashboard",
                route="/",
                layout="dashboard",
                components=[
                    SimpleNamespace(
                        name="Chart",
                        component_type="feature",
                    )
                ],
            )
        ]
    )

    graph = GraphBuilder().build(ui_spec)

    assert "page.dashboard" in graph.nodes
    assert "component.chart" in graph.nodes

    assert len(graph.edges) == 1
    assert (
        graph.edges[0].edge_type
        == EdgeType.RENDERS
    )
