from core.graph.models import ApplicationGraph
from core.graph.models import (
    GraphNode,
    NodeKind,
)
from core.graph.models import (
    GraphEdge,
    EdgeRelation,
)
from core.graph.change import (
    ChangeRequest,
    ChangeType,
)
from core.graph.change_planner import ChangePlanner
from core.graph.signals import SignalType


def test_change_planner_creates_evolution_plan():

    graph = ApplicationGraph()

    graph.add_node(
        GraphNode(
            id="feature.auth",
            type=NodeKind.FEATURE,
            name="Auth",
        )
    )

    graph.add_node(
        GraphNode(
            id="page.login",
            type=NodeKind.PAGE,
            name="Login",
        )
    )

    graph.add_edge(
        GraphEdge(
            source="feature.auth",
            target="page.login",
            type=EdgeRelation.IMPLEMENTS,
        )
    )

    planner = ChangePlanner(graph)

    plan = planner.create_plan(
        ChangeRequest(
            target_node="feature.auth",
            change_type=ChangeType.MODIFY,
        )
    )

    assert (
        "page.login"
        in plan.affected_nodes
    )

    assert any(
        signal.signal_type
        == SignalType.RUN_TESTS
        for signal in plan.signals
    )

    assert (
        "run_tests"
        in plan.validation_steps
    )
