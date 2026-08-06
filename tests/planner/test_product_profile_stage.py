from core.planner.planning_context import PlanningContext
from core.planner.stages.product_profile_stage import ProductProfileStage
from core.planner.models import Intent


def test_product_profile_stage():

    context = PlanningContext(
        prompt="Build an AI SaaS"
    )

    context.intent = Intent(ai=True)

    context.capabilities = []

    context.feature_models = []

    ProductProfileStage().run(context)

    assert context.product_profile is not None
    assert context.product_profile.name == "AI SaaS"


if __name__ == "__main__":
    test_product_profile_stage()
    print("✅ ProductProfileStage passed")
