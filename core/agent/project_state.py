from __future__ import annotations

from dataclasses import dataclass, field

from core.spec.project_spec import ProjectSpec


@dataclass
class ProjectState:
    """
    Stores the active X337 project.
    """

    project: ProjectSpec | None = None

    changes: list[str] = field(
        default_factory=list
    )


    def update(
        self,
        project: ProjectSpec,
    ):

        self.project = project


    def record_change(
        self,
        change: str,
    ):

        self.changes.append(change)
