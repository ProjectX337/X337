from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


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

    design_system: dict[str, Any] = field(
        default_factory=dict
    )

    interactions: list[str] = field(
        default_factory=list
    )

    responsive: dict[str, Any] = field(
        default_factory=dict
    )

    metadata: dict[str, Any] = field(
        default_factory=dict
    )


    @property
    def page_count(self) -> int:
        return len(self.pages)


    @property
    def component_count(self) -> int:
        return len(self.components)
