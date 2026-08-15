from core.planner.project_planner import ProjectPlanner
from core.graph.models import NodeKind


PROMPT = (
    "Build an AI SaaS with authentication, "
    "AI assistant, analytics, dashboard, users, "
    "and search"
)


def test_component_identity_is_normalized():

    spec = ProjectPlanner().plan(
        PROMPT
    )

    graph = spec.application_graph


    components = {
        node.id
        for node in graph.nodes.values()
        if node.kind == NodeKind.COMPONENT
    }


    assert any(
        node_id.endswith(".component.chatpanel")
        for node_id in components
    )

    assert not any(
        node_id.endswith(".component.chat_panel")
        for node_id in components
    )
