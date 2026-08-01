from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from core.planner.models import (
    ParsedPrompt,
    Intent,
    TechnologyPlan,
)
from core.planner.stack_builder import ArchitectureStack
from core.planner.capability_match import CapabilityMatch


@dataclass(slots=True)
class ProjectSpec:
    """
    Canonical project specification produced by the planning pipeline.

    This is the contract between planning and generation.
    """

    prompt: str

    parsed: ParsedPrompt

    intent: Intent

    architecture: ArchitectureStack

    capabilities: list[CapabilityMatch] = field(
        default_factory=list
    )

    features: list[str] = field(
        default_factory=list
    )

    technologies: TechnologyPlan | None = None

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    # ---------------------------------------------------------
    # Normalized Properties
    # ---------------------------------------------------------

    @property
    def project_name(self) -> str:

        name = self.parsed.project_name.strip()

        return name if name else "x337-app"


    @property
    def slug(self) -> str:

        return (
            self.project_name
            .lower()
            .replace(" ", "-")
            .replace("_", "-")
        )


    @property
    def description(self) -> str:

        return self.parsed.description


    @property
    def keywords(self) -> list[str]:

        return self.parsed.keywords
