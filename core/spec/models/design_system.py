from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class DesignSystem:
    """
    Canonical visual system for generated applications.
    """

    name: str = "Neural Glass"

    colors: dict[str, str] = field(
        default_factory=dict
    )

    typography: dict[str, str] = field(
        default_factory=dict
    )

    spacing: dict[str, str] = field(
        default_factory=dict
    )

    theme: str = "modern"

    component_style: str = "modern"

    animation_style: str = "smooth"

    navigation_pattern: str = "sidebar"

    accessibility_level: str = "WCAG"

    product_type: str = "application"

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    def as_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "colors": self.colors,
            "typography": self.typography,
            "spacing": self.spacing,
            "theme": self.theme,
            "component_style": self.component_style,
            "animation_style": self.animation_style,
            "navigation_pattern": self.navigation_pattern,
            "accessibility_level": self.accessibility_level,
            "product_type": self.product_type,
            "metadata": self.metadata,
        }

    def to_dict(self) -> dict[str, Any]:
        return self.as_dict()
