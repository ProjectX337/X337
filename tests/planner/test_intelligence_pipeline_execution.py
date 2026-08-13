from core.planner.planner import Planner


def test_product_intelligence_runs_in_pipeline():

    result = Planner().plan(
        "Create an AI tutor application"
    )

    assert result.product_spec is not None

    assert result.application_graph is not None