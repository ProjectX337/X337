from __future__ import annotations

from core.spec.models.ui_layout import UILayoutNode


class LayoutRenderer:
    """
    Converts UILayoutNode trees into React JSX.
    """

    def render(
        self,
        node: UILayoutNode,
        depth: int = 0,
    ) -> str:

        indent = "  " * depth

        children = ""

        for child in node.children:
            children += self.render(
                child,
                depth + 1,
            )

        if node.component:

            return (
                f"{indent}"
                f"<{node.component.name} />\n"
            )

        return (
            f"{indent}<section>\n"
            f"{children}"
            f"{indent}</section>\n"
        )
