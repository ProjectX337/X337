from core.agent.change_engine import ChangeEngine
from core.graph.application_graph import ApplicationGraph


def test_change_engine_creates_plan():

    graph = ApplicationGraph()

    engine = ChangeEngine()

    plan = engine.detect(
        graph,
        "feature.auth",
    )

    assert plan.change.target_node == "feature.auth"
