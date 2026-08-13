from core.knowledge.product_profiles import AI_SAAS
from core.planner.ui_planner import UIPlanner
from core.planner.models import Intent


def test_ai_saas_page_components_are_page_specific():
    spec = UIPlanner().plan(
        intent=Intent(ai=True),
        capabilities=[],
        product_profile=AI_SAAS,
    )

    pages = {
        page.name: page
        for page in spec.page_models
    }

    assert [
        component.name
        for component in pages["Landing"].components
    ] == [
        "Navbar",
        "ChatPanel",
    ]

    assert [
        component.name
        for component in pages["Dashboard"].components
    ] == [
        "Navbar",
        "Sidebar",
        "MetricCard",
        "DashboardCard",
        "DataTable",
    ]

    assert [
        component.name
        for component in pages["Settings"].components
    ] == [
        "Navbar",
        "Sidebar",
    ]

    assert [
        component.name
        for component in pages["Billing"].components
    ] == [
        "Navbar",
        "Sidebar",
    ]

    assert [
        component.name
        for component in pages["API"].components
    ] == [
        "Navbar",
        "Sidebar",
    ]
