from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class Capability:
    """
    Represents a reusable product capability.
    """

    name: str

    description: str = ""

    keywords: list[str] = field(default_factory=list)

    technologies: list[str] = field(default_factory=list)

    required_roles: list[str] = field(default_factory=list)

    pages: list[str] = field(default_factory=list)

    components: list[str] = field(default_factory=list)

    priority: int = 100

    confidence: float = 1.0

    depends_on: list[str] = field(default_factory=list)

    implies: list[str] = field(default_factory=list)

    conflicts_with: list[str] = field(default_factory=list)

    metadata: dict = field(default_factory=dict)
