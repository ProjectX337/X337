from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from core.spec.models.ui_component import UIComponent


@dataclass(slots=True)
class UILayoutNode:
    """
    Recursive UI composition tree node.

    A node can represent either a layout/container element
    or a concrete UI component.
    """

    name: str

    node_type: str = "container"

    component: UIComponent | None = None

    children: list["UILayoutNode"] = field(
        default_factory=list
    )

    props: dict[str, Any] = field(
        default_factory=dict
    )

    def as_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "node_type": self.node_type,
            "component": (
                self.component.as_dict()
                if self.component is not None
                and hasattr(self.component, "as_dict")
                else self.component
            ),
            "children": [
                child.as_dict()
                for child in self.children
            ],
            "props": self.props,
        }

    def to_dict(self) -> dict[str, Any]:
        return self.as_dict()
