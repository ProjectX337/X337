from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class UIComponent:
    """
    Canonical frontend component model.
    """

    name: str

    component_type: str = "component"

    props: dict[str, Any] = field(
        default_factory=dict
    )

    variants: list[str] = field(
        default_factory=list
    )

    states: list[str] = field(
        default_factory=list
    )

    children: list[str] = field(
        default_factory=list
    )

    dependencies: list[str] = field(
        default_factory=list
    )

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    def as_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "component_type": self.component_type,
            "props": self.props,
            "variants": self.variants,
            "states": self.states,
            "children": self.children,
            "dependencies": self.dependencies,
            "metadata": self.metadata,
        }

    def to_dict(self) -> dict[str, Any]:
        return self.as_dict()
