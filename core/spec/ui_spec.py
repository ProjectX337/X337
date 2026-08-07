from __future__ import annotations

from dataclasses import dataclass, field

from core.spec.models.ui_component import UIComponent
from core.spec.models.ui_page import UIPage
from core.spec.models.design_system import DesignSystem


@dataclass(slots=True)
class UISpec:
    """
    Universal UI blueprint.

    Frontend generators consume this object.
    """

    layout: str = "default"

    theme: str = "modern"

    navigation: list[str] = field(
        default_factory=list
    )

    metadata: dict = field(
        default_factory=dict
    )

    page_models: list[UIPage] = field(
        default_factory=list
    )

    component_models: list[UIComponent] = field(
        default_factory=list
    )

    design_system: DesignSystem = field(
        default_factory=DesignSystem
    )


    @property
    def pages(self) -> list[str]:
        """
        Compatibility accessor.
        """

        return [
            page.name
            for page in self.page_models
        ]


    @property
    def components(self) -> list[str]:
        """
        Compatibility accessor.
        """

        return [
            component.name
            for component in self.component_models
        ]


    @property
    def page_count(self) -> int:

        return len(
            self.page_models
        )


    @property
    def component_count(self) -> int:

        return len(
            self.component_models
        )


    def as_dict(self):
        return {
            "layout": self.layout,
            "theme": self.theme,
            "navigation": self.navigation,
            "metadata": self.metadata,
            "page_models": [
                p.as_dict() if hasattr(p, "as_dict") else vars(p)
                for p in self.page_models
            ],
            "component_models": [
                c.as_dict() if hasattr(c, "as_dict") else vars(c)
                for c in self.component_models
            ],
            "design_system": (
                self.design_system.as_dict()
                if hasattr(self.design_system, "as_dict")
                else vars(self.design_system)
            ),
        }

    def to_dict(self):
        return self.as_dict()
