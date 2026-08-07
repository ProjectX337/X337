from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class FeatureSpec:
    """
    Structured product feature definition.

    Used by planners, update agents, and generators.
    """

    name: str

    slug: str

    description: str = ""

    routes: list[str] = field(
        default_factory=list
    )

    pages: list[str] = field(
        default_factory=list
    )

    components: list[str] = field(
        default_factory=list
    )

    state: list[str] = field(
        default_factory=list
    )

    api_contracts: list[str] = field(
        default_factory=list
    )

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    # ==================================================

    def as_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "slug": self.slug,
            "description": self.description,
            "routes": self.routes,
            "pages": self.pages,
            "components": self.components,
            "state": self.state,
            "api_contracts": self.api_contracts,
            "metadata": self.metadata,
        }

    def to_dict(self) -> dict[str, Any]:
        return self.as_dict()

