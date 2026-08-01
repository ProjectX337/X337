from core.planner.ui_planner import UIPlanner
from core.planner.models import Intent


def test_ui_planner():

    planner = UIPlanner()

    spec = planner.plan(
        intent=Intent(),
        capabilities=[],
    )

    assert "Landing" in spec.pages

    assert "Navbar" in spec.components


if __name__ == "__main__":
    test_ui_planner()
    print("✅ UIPlanner passed")
