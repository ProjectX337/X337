from __future__ import annotations

from dataclasses import dataclass, field

from core.build.build_plan import BuildStep
from core.generators.file_builder import FileBuilder
from core.spec.project_spec import ProjectSpec


@dataclass(slots=True)
class GeneratorContext:
    """
    Context shared with every generator.
    """

    spec: ProjectSpec

    step: BuildStep

    builder: FileBuilder

    # Requested modifications
    changes: list[str] = field(
        default_factory=list
    )

    # Existing project state
    project_state: object | None = None

    is_update: bool = False
