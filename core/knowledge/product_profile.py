from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class ProductProfile:
    """
    Canonical product archetype used throughout the planning engine.
    """

    name: str

    description: str = ""

    layout: str = "default"

    theme: str = "modern"

    navigation: str = "top"

    density: str = "comfortable"

    motion: str = "standard"

    architecture: str = "spa"

    required_features: list[str] = field(default_factory=list)

    recommended_capabilities: list[str] = field(default_factory=list)

    #
    # Default UI architecture
    #

    default_pages: list[str] = field(
        default_factory=list
    )

    default_components: list[str] = field(
        default_factory=list
    )

    navigation_items: list[str] = field(
        default_factory=list
    )

    layout_sections: list[str] = field(
        default_factory=list
    )

