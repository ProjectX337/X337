from types import SimpleNamespace

from core.graph.graph_builder import GraphBuilder
from core.graph.models import EdgeRelation


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
    assert "page.dashboard.component.chart" in graph.nodes

    assert len(graph.edges) == 2

    assert any(
        edge.source == "page.dashboard"
        and edge.target == "page.dashboard.route"
        and edge.relation == EdgeRelation.NAVIGATES_TO
        for edge in graph.edges
    )

    assert any(
        edge.source == "page.dashboard"
        and edge.target == "page.dashboard.component.chart"
        and edge.relation == EdgeRelation.RENDERS
        for edge in graph.edges
    )
