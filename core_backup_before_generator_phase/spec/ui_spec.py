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
