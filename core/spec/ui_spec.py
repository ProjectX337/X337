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

    pages: list[str] = field(
        default_factory=list
    )

    components: list[str] = field(
        default_factory=list
    )

    layout: str = "default"

    theme: str = "modern"

    navigation: list[str] = field(
        default_factory=list
    )

    metadata: dict = field(
        default_factory=dict
    )

    # Expanded UI intelligence

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
    def page_count(self) -> int:
        return len(
            self.pages
        )


    @property
    def component_count(self) -> int:
        return len(
            self.components
        )
