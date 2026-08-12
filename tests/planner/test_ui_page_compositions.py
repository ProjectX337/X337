from core.planner.ui_planner import UIPlanner
from core.planner.models import Intent
from core.planner.capability_match import CapabilityMatch
from core.knowledge.product_profile import ProductProfile


def make_multi_page_profile():
    return ProductProfile(
        name="Test SaaS",
        default_pages=[
            "Landing",
            "Dashboard",
            "Settings",
        ],
        default_components=[
            "Navbar",
            "Sidebar",
        ],
        theme="modern",
        layout="dashboard",
        navigation="sidebar",
    )


def test_every_canonical_page_has_composition():
    planner = UIPlanner()

    spec = planner.plan(
        intent=Intent(),
        capabilities=[],
        product_profile=make_multi_page_profile(),
    )

    assert spec.page_models

    for page in spec.page_models:
        assert page.composition is not None, (
            f"{page.name} ({page.route}) has no composition"
        )


def test_page_compositions_are_independent():
    planner = UIPlanner()

    spec = planner.plan(
        intent=Intent(),
        capabilities=[],
        product_profile=make_multi_page_profile(),
    )

    assert len(spec.page_models) >= 2

    first = spec.page_models[0].composition
    second = spec.page_models[1].composition

    assert first is not None
    assert second is not None

    # Each page owns its own structural tree.
    assert first is not second

    # Nested collections must also not be shared.
    assert first.children is not second.children


def test_page_composition_is_structural():
    planner = UIPlanner()

    spec = planner.plan(
        intent=Intent(),
        capabilities=[],
        product_profile=make_multi_page_profile(),
    )

    for page in spec.page_models:
        composition = page.composition

        assert composition is not None
        assert composition.name == "ApplicationShell"
        assert composition.node_type == "container"
        assert composition.children
