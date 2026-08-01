from core.planner.planning_context import PlanningContext
from core.planner.stages.ui_spec_stage import UISpecStage


def test_ui_spec_stage():

    context = PlanningContext(
        prompt="Build an AI SaaS"
    )

    context.intent = None
    context.capabilities = []

    stage = UISpecStage()

    stage.run(context)

    assert context.ui_spec is not None

    assert (
        "Landing"
        in context.ui_spec.pages
    )


if __name__ == "__main__":
    test_ui_spec_stage()
    print("✅ UISpecStage passed")
