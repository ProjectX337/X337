from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class ArchitectureDefinition:

    name: str

    routing: str

    state: str

    rendering: str

    api_style: str

    deployment: str

    recommended_components: list[str] = field(default_factory=list)

    recommended_patterns: list[str] = field(default_factory=list)
