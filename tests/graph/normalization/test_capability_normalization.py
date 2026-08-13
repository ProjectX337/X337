from core.planner.project_planner import ProjectPlanner
from core.graph.models import EdgeRelation


PROMPT = (
    "Build an AI SaaS with authentication, "
    "AI assistant, analytics, dashboard, users, and search"
)


def test_capability_identity_is_normalized():
    spec = ProjectPlanner().plan(PROMPT)

    graph = spec.application_graph

    capability_nodes = {
        node.id
        for node in graph.nodes.values()
        if node.kind.value == "capability"
    }

    assert "capability.ai" in capability_nodes

    assert (
        "capability.chat"
        not in capability_nodes
    )


def test_capability_normalization_preserves_feature_edges():
    spec = ProjectPlanner().plan(PROMPT)

    graph = spec.application_graph

    assert any(
        edge.source == "capability.ai"
        and edge.target == "feature.ai"
        and edge.relation == EdgeRelation.IMPLEMENTS
        for edge in graph.edges
    )
