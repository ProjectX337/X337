from core.spec.ui_spec import UISpec
from core.spec.models.ui_page import UIPage
from core.spec.models.ui_component import UIComponent


def make_spec() -> UISpec:
    return UISpec(
        page_models=[
            UIPage(
                name="Landing",
                route="/",
            )
        ],
        component_models=[
            UIComponent(
                name="Navbar",
            )
        ],
    )


def test_pages_is_canonical_page_models():
    spec = make_spec()

    assert spec.pages is spec.page_models


def test_components_is_canonical_component_models():
    spec = make_spec()

    assert spec.components is spec.component_models


def test_pages_mutation_updates_page_models():
    spec = make_spec()

    spec.pages.append(
        UIPage(
            name="Dashboard",
            route="/dashboard",
        )
    )

    assert len(spec.pages) == 2
    assert len(spec.page_models) == 2
    assert spec.page_models[-1].name == "Dashboard"


def test_components_mutation_updates_component_models():
    spec = make_spec()

    spec.components.append(
        UIComponent(
            name="Sidebar",
        )
    )

    assert len(spec.components) == 2
    assert len(spec.component_models) == 2
    assert spec.component_models[-1].name == "Sidebar"


def test_legacy_string_membership_for_pages():
    spec = make_spec()

    assert "Landing" in spec.pages


def test_legacy_string_membership_for_components():
    spec = make_spec()

    assert "Navbar" in spec.components


def test_canonical_mutation_updates_compatibility_alias():
    spec = make_spec()

    spec.page_models.append(
        UIPage(
            name="Settings",
            route="/settings",
        )
    )

    spec.component_models.append(
        UIComponent(
            name="SettingsPanel",
        )
    )

    assert "Settings" in spec.pages
    assert "SettingsPanel" in spec.components


def test_serialization_uses_canonical_models():
    spec = make_spec()

    spec.pages.append(
        UIPage(
            name="Dashboard",
            route="/dashboard",
        )
    )

    spec.components.append(
        UIComponent(
            name="Sidebar",
        )
    )

    data = spec.as_dict()

    assert len(data["page_models"]) == 2
    assert len(data["component_models"]) == 2

    assert data["page_models"][1]["name"] == "Dashboard"
    assert data["component_models"][1]["name"] == "Sidebar"
