from __future__ import annotations

from core.spec.models.ui_component import UIComponent
from core.spec.models.ui_layout import UILayoutNode


class LayoutRenderer:
    """
    Converts UILayoutNode trees into React JSX.

    Structural nodes always preserve their semantic HTML
    container. A component attached to a node is rendered
    inside that container.
    """

    _TAGS = {
        "container": "div",
        "section": "section",
        "header": "header",
        "footer": "footer",
        "main": "main",
        "nav": "nav",
        "aside": "aside",
        "article": "article",
    }

    def render(
        self,
        node: UILayoutNode,
        *,
        indent: int = 0,
    ) -> str:
        return self._render_node(node, indent)

    def _render_node(
        self,
        node: UILayoutNode,
        indent: int,
    ) -> str:

        prefix = "  " * indent
        tag = self._TAGS.get(
            node.node_type,
            "div",
        )

        lines = [
            f"{prefix}<{tag}>",
        ]

        child_indent = indent + 1

        if node.component is not None:
            lines.append(
                self._render_component(
                    node.component,
                    child_indent,
                )
            )

        for child in node.children:
            lines.append(
                self._render_node(
                    child,
                    child_indent,
                )
            )

        lines.append(
            f"{prefix}</{tag}>",
        )

        return "\n".join(lines)

    def _render_component(
        self,
        component: UIComponent,
        indent: int,
    ) -> str:
        prefix = "  " * indent

        return (
            f"{prefix}"
            f"<{component.name} />"
        )
