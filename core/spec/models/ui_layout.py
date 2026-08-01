from __future__ import annotations

from dataclasses import dataclass, field

from core.spec.models.ui_component import UIComponent


@dataclass(slots=True)
class UILayoutNode:
    """
    Recursive UI composition tree node.
    """

    name: str

    node_type: str = "container"

    component: UIComponent | None = None

    children: list["UILayoutNode"] = field(
        default_factory=list
    )

    props: dict = field(
        default_factory=dict
    )
