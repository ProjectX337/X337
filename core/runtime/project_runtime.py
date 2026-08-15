from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
import uuid
from pathlib import Path
from typing import Any

from core.spec.project_spec import ProjectSpec
from core.runtime.runtime_process import RuntimeProcess


@dataclass
class ProjectRuntime:
    """
    Runtime representation of a generated X337 project.

    ProjectSpec answers:
        "What is this application?"

    ProjectRuntime answers:
        "Where does this application exist and run?"
    """

    spec: ProjectSpec

    root_path: Path

    id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    created_at: datetime = field(
        default_factory=datetime.now
    )

    generation: dict[str, Any] = field(
        default_factory=dict
    )

    processes: dict[str, RuntimeProcess] = field(
        default_factory=dict
    )

    preview: dict[str, Any] = field(
        default_factory=dict
    )

    health: dict[str, Any] = field(
        default_factory=dict
    )

    status: str = "created"


    @property
    def slug(self) -> str:
        return self.spec.slug


    @property
    def name(self) -> str:
        return self.spec.project_name


    def to_dict(self) -> dict:

        return {
            "id": self.id,
            "name": self.name,
            "slug": self.slug,
            "root_path": str(self.root_path),
            "status": self.status,
            "created_at": (
                self.created_at.isoformat()
            ),
            "generation": self.generation,
            "preview": self.preview,
            "health": self.health,
            "processes": [
                process.to_dict()
                for process in self.processes.values()
            ],
        }
