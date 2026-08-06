from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class TechnologyDefinition:

    name: str

    category: str

    best_for: list[str] = field(default_factory=list)

    strengths: list[str] = field(default_factory=list)

    weaknesses: list[str] = field(default_factory=list)

    integrates_with: list[str] = field(default_factory=list)

    recommended_architectures: list[str] = field(default_factory=list)
