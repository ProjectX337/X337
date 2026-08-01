from __future__ import annotations

from dataclasses import dataclass, field

from core.planner.architecture_selector import ArchitectureCandidate
from core.planner.capability_match import CapabilityMatch
from core.planner.models import (
    Intent,
    ParsedPrompt,
    TechnologyPlan,
)
from core.planner.stack_builder import ArchitectureStack
from core.spec.project_spec import ProjectSpec
from core.spec.ui_spec import UISpec


@dataclass(slots=True)
class PlanningContext:
    """
    Shared planning state for the planning pipeline.
    """

    prompt: str

    parsed: ParsedPrompt | None = None

    intent: Intent | None = None

    capabilities: list[CapabilityMatch] = field(
        default_factory=list
    )

    architecture_candidates: list[ArchitectureCandidate] = field(
        default_factory=list
    )

    stack: ArchitectureStack | None = None

    technologies: TechnologyPlan | None = None

    project_spec: ProjectSpec | None = None

    ui_spec: UISpec | None = None

