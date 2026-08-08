from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class DesignSystem:
    """
    Defines the visual and interaction language
    used when generating an application.
    """

    name: str = "default"

    # Visual identity
    visual_style: str = "modern"

    theme: str = "light"

    color_palette: list[str] = field(
        default_factory=list
    )

    typography: str = "system"

    spacing_system: str = "standard"


    # UI architecture
    component_library: str = "custom"

    layout_style: str = "responsive"

    navigation_pattern: str = "sidebar"


    # Experience
    animation_level: str = "medium"

    accessibility_level: str = "WCAG"


    # Product context
    product_type: str = "application"


    def to_dict(self):
        return self.__dict__
