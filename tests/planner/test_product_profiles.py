from core.knowledge.product_profiles import (
    AI_SAAS,
    PORTFOLIO,
    ENTERPRISE,
    PRODUCT_PROFILES,
)


def test_registry():

    assert "ai_saas" in PRODUCT_PROFILES
    assert "portfolio" in PRODUCT_PROFILES
    assert "enterprise" in PRODUCT_PROFILES

    assert AI_SAAS.default_pages
    assert PORTFOLIO.default_pages
    assert ENTERPRISE.default_pages


if __name__ == "__main__":
    test_registry()
    print("✅ Product profile registry passed")


def test_generic_project_has_profile():
    from core.knowledge.product_profile_reasoner import (
        ProductProfileReasoner,
    )
    from core.planner.models import Intent

    reasoner = ProductProfileReasoner()

    profile = reasoner.infer(
        intent=Intent(),
        capabilities=[],
        features=[],
    )

    assert profile is not None
    assert profile.name
    assert profile.name in {
        candidate.name
        for candidate in PRODUCT_PROFILES.values()
    }


def test_project_management_does_not_crash():
    from core.planner.project_planner import ProjectPlanner

    planner = ProjectPlanner()

    spec = planner.plan(
        "Create a project management application"
    )

    assert spec is not None
    assert spec.ui_spec is not None
    assert spec.ui_spec.page_models
    assert spec.ui_spec.design_system is not None
