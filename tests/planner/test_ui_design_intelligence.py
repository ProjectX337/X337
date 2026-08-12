from core.planner.ui_planner import UIPlanner
from core.planner.models import Intent


def test_futuristic_ai_design():

    planner = UIPlanner()

    spec = planner.plan(
        intent=Intent(
            ai=True,
            dashboard=True,
        ),
        capabilities=[],
    )

    assert spec.design_system.colors
    assert spec.theme


def test_dashboard_layout_exists():

    planner = UIPlanner()

    spec = planner.plan(
        intent=Intent(
            dashboard=True,
        ),
        capabilities=[],
    )

    assert spec.layout
def test_ai_saas_composition_matches_profile():
    from core.knowledge.product_profiles import PRODUCT_PROFILES
    from core.planner.design.design_composer import DesignComposer

    profile = PRODUCT_PROFILES["ai_saas"]
    composition = DesignComposer().compose(
        product_profile=profile,
    )

    assert composition.layout.layout_pattern == profile.layout
    assert composition.layout.navigation == profile.navigation
    assert composition.layout.density == profile.density
    assert composition.design_system.theme == profile.theme


def test_portfolio_composition_matches_profile():
    from core.knowledge.product_profiles import PRODUCT_PROFILES
    from core.planner.design.design_composer import DesignComposer

    profile = PRODUCT_PROFILES["portfolio"]
    composition = DesignComposer().compose(
        product_profile=profile,
    )

    assert composition.layout.layout_pattern == profile.layout
    assert composition.layout.navigation == profile.navigation
    assert composition.layout.density == profile.density
    assert composition.design_system.theme == profile.theme


def test_enterprise_composition_matches_profile():
    from core.knowledge.product_profiles import PRODUCT_PROFILES
    from core.planner.design.design_composer import DesignComposer

    profile = PRODUCT_PROFILES["enterprise"]
    composition = DesignComposer().compose(
        product_profile=profile,
    )

    assert composition.layout.layout_pattern == profile.layout
    assert composition.layout.navigation == profile.navigation
    assert composition.layout.density == profile.density
    assert composition.design_system.theme == profile.theme


def test_portfolio_does_not_receive_ai_learning_components():
    from core.knowledge.product_profiles import PRODUCT_PROFILES
    from core.planner.design.design_composer import DesignComposer

    composition = DesignComposer().compose(
        product_profile=PRODUCT_PROFILES["portfolio"],
    )

    assert "AITutorChat" not in composition.components.components
    assert "LearningModule" not in composition.components.components
    assert "ProgressCard" not in composition.components.components


def test_portfolio_uses_profile_components():
    from core.knowledge.product_profiles import PRODUCT_PROFILES
    from core.planner.design.design_composer import DesignComposer

    composition = DesignComposer().compose(
        product_profile=PRODUCT_PROFILES["portfolio"],
    )

    for component in PRODUCT_PROFILES["portfolio"].default_components:
        assert component in composition.components.components
