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