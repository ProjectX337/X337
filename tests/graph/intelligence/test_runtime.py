from core.planner.project_planner import (
    ProjectPlanner,
)

from core.graph.intelligence.runtime import (
    GraphIntelligenceRuntime,
)


def test_graph_intelligence_runtime():

    spec = ProjectPlanner().plan(
        "Create an analytics dashboard"
    )

    runtime = GraphIntelligenceRuntime(
        spec.application_graph
    )

    result = runtime.analyze()

    assert result["reasoning"] is not None

    assert (
        result["architecture"]
        is not None
    )
