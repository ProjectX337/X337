from core.generators.react.layout_renderer import LayoutRenderer
from core.spec.models.ui_component import UIComponent
from core.spec.models.ui_layout import UILayoutNode


def test_layout_renderer():
    sidebar = UIComponent(
        name="Sidebar",
        component_type="navigation",
    )

    tree = UILayoutNode(
        name="Root",
        node_type="container",
        children=[
            UILayoutNode(
                name="Sidebar",
                node_type="section",
                component=sidebar,
            )
        ],
    )

    output = LayoutRenderer().render(tree)

    print("\n===== RENDERED JSX =====")
    print(output)

    assert "<div>" in output
    assert "<section>" in output
    assert "<Sidebar />" in output
    assert "</section>" in output
    assert "</div>" in output


def test_layout_renderer_application_shell():
    analytics = UIComponent(
        name="AnalyticsPanel",
        component_type="generated",
    )

    tree = UILayoutNode(
        name="ApplicationShell",
        node_type="container",
        children=[
            UILayoutNode(
                name="analytics",
                node_type="section",
                component=analytics,
            )
        ],
    )

    output = LayoutRenderer().render(tree)

    print("\n===== APPLICATION SHELL JSX =====")
    print(output)

    assert "<div>" in output
    assert "<section>" in output
    assert "<AnalyticsPanel />" in output
    assert "</section>" in output
    assert "</div>" in output
