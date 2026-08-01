from core.generators.react.layout_renderer import LayoutRenderer
from core.spec.models.ui_layout import UILayoutNode
from core.spec.models.ui_component import UIComponent


def test_layout_renderer():

    sidebar = UIComponent(
        name="Sidebar",
        component_type="navigation",
    )

    tree = UILayoutNode(
        name="Root",
        children=[
            UILayoutNode(
                name="Sidebar",
                component=sidebar,
            )
        ],
    )

    output = LayoutRenderer().render(tree)

    assert "<Sidebar />" in output


if __name__ == "__main__":
    test_layout_renderer()
    print("✅ LayoutRenderer passed")
