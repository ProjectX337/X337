from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class DesignSystem:
    """
    Canonical visual and interaction system for generated applications.

    This is the single authoritative design-system model used by:

        Product Intelligence
              ↓
        Design Composer
              ↓
        Design Reasoner
              ↓
        UI Planner
              ↓
        UI Blueprint
              ↓
        React Generator

    DesignSystem describes visual language and design tokens.

    Layout/page structure belongs to LayoutStrategy.
    Component composition belongs to ComponentStrategy.
    """

    # ---------------------------------------------------------
    # Identity
    # ---------------------------------------------------------

    name: str = "Neural Glass"

    product_type: str = "application"

    # ---------------------------------------------------------
    # Visual language
    # ---------------------------------------------------------

    visual_style: str = "modern"

    theme: str = "modern"

    component_style: str = "modern"

    animation_style: str = "smooth"

    # ---------------------------------------------------------
    # Design tokens
    # ---------------------------------------------------------

    colors: dict[str, str] = field(
        default_factory=dict
    )

    color_palette: list[str] = field(
        default_factory=list
    )

    typography: dict[str, str] = field(
        default_factory=dict
    )

    spacing: dict[str, str] = field(
        default_factory=dict
    )

    # Density is a semantic design decision such as:
    #
    #   compact
    #   comfortable
    #   spacious
    #
    # It is intentionally separate from the raw spacing tokens.
    density: str = "comfortable"

    # ---------------------------------------------------------
    # Application-level interaction conventions
    # ---------------------------------------------------------

    navigation_pattern: str = "sidebar"

    layout_style: str = "default"

    accessibility_level: str = "WCAG"

    # ---------------------------------------------------------
    # Extensibility
    # ---------------------------------------------------------

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    # ---------------------------------------------------------
    # Serialization
    # ---------------------------------------------------------

    def as_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "product_type": self.product_type,
            "visual_style": self.visual_style,
            "theme": self.theme,
            "component_style": self.component_style,
            "animation_style": self.animation_style,
            "colors": self.colors,
            "color_palette": self.color_palette,
            "typography": self.typography,
            "spacing": self.spacing,
            "density": self.density,
            "navigation_pattern": self.navigation_pattern,
            "layout_style": self.layout_style,
            "accessibility_level": self.accessibility_level,
            "metadata": self.metadata,
        }

    def to_dict(self) -> dict[str, Any]:
        return self.as_dict()
