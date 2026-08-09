from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class DesignSystem:
    """
    Canonical design-intelligence model used by the UI planning layer.

    This model bridges planner-level visual intelligence and the
    canonical UISpec design-system contract.
    """

    name: str = "X337 Adaptive AI"

    visual_style: str = "modern"

    theme: str = "light"

    colors: dict[str, str] = field(
        default_factory=dict
    )

    typography: dict[str, str] = field(
        default_factory=dict
    )

    spacing: dict[str, str] = field(
        default_factory=dict
    )

    color_palette: list[str] = field(
        default_factory=list
    )

    spacing_system: str = "standard"

    component_library: str = "custom"

    layout_style: str = "responsive"

    navigation_pattern: str = "sidebar"

    animation_level: str = "medium"

    accessibility_level: str = "WCAG"

    product_type: str = "application"

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    def as_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "visual_style": self.visual_style,
            "theme": self.theme,
            "colors": self.colors,
            "typography": self.typography,
            "spacing": self.spacing,
            "color_palette": self.color_palette,
            "spacing_system": self.spacing_system,
            "component_library": self.component_library,
            "layout_style": self.layout_style,
            "navigation_pattern": self.navigation_pattern,
            "animation_level": self.animation_level,
            "accessibility_level": self.accessibility_level,
            "product_type": self.product_type,
            "metadata": self.metadata,
        }

    def to_dict(self) -> dict[str, Any]:
        return self.as_dict()
