from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from core.spec.models.ui_page import UIPage
from core.spec.models.ui_component import UIComponent
from core.spec.models.design_system import DesignSystem


@dataclass(slots=True)
class UISpec:
    """
    Canonical frontend specification produced by X337's UI planner.

    UISpec is the contract between planning/design intelligence
    and frontend generation.

    Pipeline:

        Intent
            ↓
        CapabilityMatch
            ↓
        FeatureSpec
            ↓
        UIPlanner
            ↓
        UISpec
            ├── pages
            ├── components
            └── design_system
    """

    layout: str = "default"

    theme: str = "modern"

    navigation: list[str] = field(
        default_factory=list
    )

    metadata: dict[str, Any] = field(
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

    # ---------------------------------------------------------
    # Compatibility helpers
    # ---------------------------------------------------------

    @property
    def pages(self) -> list[UIPage]:
        return self.page_models

    @property
    def components(self) -> list[UIComponent]:
        return self.component_models

    @property
    def page_count(self) -> int:
        return len(self.page_models)

    @property
    def component_count(self) -> int:
        return len(self.component_models)

    # ---------------------------------------------------------
    # Serialization
    # ---------------------------------------------------------

    def as_dict(self) -> dict[str, Any]:
        return {
            "layout": self.layout,
            "theme": self.theme,
            "navigation": self.navigation,
            "metadata": self.metadata,
            "page_models": [
                page.as_dict()
                if hasattr(page, "as_dict")
                else {
                    name: getattr(page, name)
                    for name in page.__dataclass_fields__
                }
                for page in self.page_models
            ],
            "component_models": [
                component.as_dict()
                if hasattr(component, "as_dict")
                else {
                    name: getattr(component, name)
                    for name in component.__dataclass_fields__
                }
                for component in self.component_models
            ],
            "design_system": (
                self.design_system.as_dict()
                if hasattr(self.design_system, "as_dict")
                else {
                    name: getattr(
                        self.design_system,
                        name,
                    )
                    for name in self.design_system.__dataclass_fields__
                }
            ),
        }

    def to_dict(self) -> dict[str, Any]:
        return self.as_dict()
