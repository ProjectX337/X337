from __future__ import annotations

from dataclasses import dataclass, field

from core.spec.project_spec import ProjectSpec
from core.graph.change_plan import ChangePlan


@dataclass
class ProjectState:
    """
    Stores the active X337 project.
    """

    project: ProjectSpec | None = None

    changes: list[ChangePlan] = field(
        default_factory=list
    )


    def update(
        self,
        project: ProjectSpec,
    ):

        self.project = project


    def record_change(
        self,
        change: ChangePlan,
    ):

        self.changes.append(
            change
        )
