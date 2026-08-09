from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from core.spec.models.ui_component import UIComponent
from core.spec.models.ui_layout import UILayoutNode


@dataclass(slots=True)
class UIPage:
    """
    Canonical frontend page model.
    """

    name: str

    route: str

    layout: str = "default"

    components: list[UIComponent] = field(
        default_factory=list
    )

    composition: UILayoutNode | None = None

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    def as_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "route": self.route,
            "layout": self.layout,
            "components": [
                component.as_dict()
                if hasattr(component, "as_dict")
                else component
                for component in self.components
            ],
            "composition": (
                self.composition.as_dict()
                if self.composition is not None
                and hasattr(self.composition, "as_dict")
                else self.composition
            ),
            "metadata": self.metadata,
        }

    def to_dict(self) -> dict[str, Any]:
        return self.as_dict()
