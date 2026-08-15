from core.planner.project_planner import ProjectPlanner
from core.graph.models import (
    NodeKind,
    EdgeRelation,
)


def test_project_planner_builds_application_graph():

    spec = ProjectPlanner().plan(
        "Create an analytics dashboard with charts"
    )

    graph = spec.application_graph

    assert graph is not None

    assert len(graph.nodes) > 0

    node_types = {
        node.kind
        for node in graph.nodes.values()
    }

    assert NodeKind.PAGE in node_types

    assert NodeKind.COMPONENT in node_types

    assert any(
        edge.relation == EdgeRelation.RENDERS
        for edge in graph.edges
    )
