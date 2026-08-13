from core.planner.project_planner import ProjectPlanner
from core.graph.nodes import NodeType
from core.graph.edges import EdgeType


def test_project_planner_builds_application_graph():

    spec = ProjectPlanner().plan(
        "Create an analytics dashboard with charts"
    )

    graph = spec.application_graph

    assert graph is not None

    assert len(graph.nodes) > 0

    node_types = {
        node.node_type
        for node in graph.nodes.values()
    }

    assert NodeType.PAGE in node_types

    assert NodeType.COMPONENT in node_types

    assert any(
        edge.edge_type == EdgeType.RENDERS
        for edge in graph.edges
    )
