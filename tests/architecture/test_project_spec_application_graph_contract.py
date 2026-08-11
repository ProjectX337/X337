from core.cognition.cognitive_state import CognitiveState
from core.graph.models import (
    ApplicationGraph,
    EdgeRelation,
    GraphEdge,
    GraphNode,
    NodeKind,
)
from core.planner.stages.project_spec_stage import ProjectSpecStage


def test_project_spec_carries_application_graph():
    state = CognitiveState(
        prompt="Create a test application"
    )

    graph = state.application_graph

    graph.add_node(
        GraphNode(
            id="product",
            kind=NodeKind.PRODUCT,
            name="Test App",
        )
    )

    graph.add_node(
        GraphNode(
            id="feature:test",
            kind=NodeKind.FEATURE,
            name="Test Feature",
        )
    )

    graph.add_edge(
        GraphEdge(
            source="product",
            target="feature:test",
            relation=EdgeRelation.REQUIRES,
        )
    )

    state.parsed.project_name = "Test App"

    ProjectSpecStage().run(state)

    spec = state.project_spec

    assert isinstance(
        spec.application_graph,
        ApplicationGraph,
    )

    assert spec.application_graph is state.application_graph

    assert "product" in spec.application_graph.nodes
    assert "feature:test" in spec.application_graph.nodes

    assert len(spec.application_graph.edges) == 1

    serialized = spec.as_dict()

    assert "application_graph" in serialized

    assert serialized["application_graph"]["nodes"]["product"]["kind"] == (
        "product"
    )

    assert serialized["application_graph"]["nodes"]["feature:test"]["kind"] == (
        "feature"
    )

    assert serialized["application_graph"]["edges"][0]["source"] == (
        "product"
    )

    assert serialized["application_graph"]["edges"][0]["target"] == (
        "feature:test"
    )

    assert serialized["application_graph"]["edges"][0]["relation"] == (
        "requires"
    )

    assert "application_graph" not in spec.metadata
