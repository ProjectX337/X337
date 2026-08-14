from core.agent.change_engine import ChangeEngine
from core.graph.models import ApplicationGraph


def test_change_engine_creates_plan():

    graph = ApplicationGraph()

    engine = ChangeEngine()

    plan = engine.detect(
        graph,
        "feature.auth",
    )

    assert plan.change.target_node == "feature.auth"
