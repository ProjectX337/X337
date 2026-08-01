from dataclasses import dataclass

from core.spec.project_spec import ProjectSpec


@dataclass
class ProjectMemory:

    project_spec: ProjectSpec | None = None

    last_prompt: str = ""
