from core.planner.ui_planner import UIPlanner
from core.planner.models import Intent
from core.knowledge.product_profile import ProductProfile


def test_ui_planner_default():

    planner = UIPlanner()

    spec = planner.plan(
        intent=Intent(),
        capabilities=[],
    )

    assert "Landing" in spec.pages
    assert "Navbar" in spec.components


def test_ui_planner_product_profile():

    planner = UIPlanner()

    profile = ProductProfile(
        name="AI SaaS",
        layout="dashboard",
        theme="futuristic",
        default_pages=[
            "Landing",
            "Dashboard",
            "Settings",
        ],
        default_components=[
            "Navbar",
            "Sidebar",
            "DashboardCard",
        ],
    )

    spec = planner.plan(
        intent=Intent(),
        capabilities=[],
        product_profile=profile,
    )

    assert "Landing" in spec.pages
    assert "Dashboard" in spec.pages

    assert "Sidebar" in spec.components
    assert "DashboardCard" in spec.components

    assert spec.layout == "dashboard"
    assert spec.theme == "futuristic"


if __name__ == "__main__":
    test_ui_planner_default()
    test_ui_planner_product_profile()
    print("✅ UIPlanner passed")
