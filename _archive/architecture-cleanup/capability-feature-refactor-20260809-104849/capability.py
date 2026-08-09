from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Capability:
    """
    Canonical reusable product capability.

    A capability represents a product-level capability that can be
    discovered from user intent and expanded through dependencies
    and implications.
    """

    name: str

    description: str = ""

    keywords: list[str] = field(
        default_factory=list
    )

    technologies: list[str] = field(
        default_factory=list
    )

    required_roles: list[str] = field(
        default_factory=list
    )

    pages: list[str] = field(
        default_factory=list
    )

    components: list[str] = field(
        default_factory=list
    )

    priority: int = 100

    confidence: float = 1.0

    depends_on: list[str] = field(
        default_factory=list
    )

    implies: list[str] = field(
        default_factory=list
    )

    conflicts_with: list[str] = field(
        default_factory=list
    )

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    @property
    def slug(self) -> str:
        return (
            self.name
            .lower()
            .strip()
            .replace("_", "-")
            .replace(" ", "-")
        )

    @property
    def api_endpoints(self) -> list[str]:
        return list(
            self.metadata.get(
                "api_endpoints",
                [],
            )
        )

    @property
    def feature_definitions(self) -> list[dict[str, Any]]:
        return list(
            self.metadata.get(
                "features",
                [],
            )
        )
