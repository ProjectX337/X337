from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TechnologyPlan:
    """
    Complete technology decisions for a generated project.

    This is produced after the ArchitectureStack has been selected.
    It represents implementation choices rather than architectures.
    """

    # ---------------------------------------------------------
    # Backend
    # ---------------------------------------------------------

    database: str | None = None

    orm: str | None = None

    authentication: str | None = None

    authorization: str | None = None

    api_style: str | None = None

    validation: str | None = None

    # ---------------------------------------------------------
    # Frontend
    # ---------------------------------------------------------

    styling: str | None = None

    state_management: str | None = None

    routing: str | None = None

    ui_library: str | None = None

    # ---------------------------------------------------------
    # AI
    # ---------------------------------------------------------

    llm_provider: str | None = None

    vector_database: str | None = None

    embeddings: str | None = None

    # ---------------------------------------------------------
    # Infrastructure
    # ---------------------------------------------------------

    cache: str | None = None

    message_queue: str | None = None

    containerization: str | None = None

    deployment: str | None = None

    ci_cd: str | None = None

    # ---------------------------------------------------------
    # Quality
    # ---------------------------------------------------------

    testing_backend: str | None = None

    testing_frontend: str | None = None

    formatter: str | None = None

    linter: str | None = None

    # ---------------------------------------------------------
    # Package Management
    # ---------------------------------------------------------

    package_manager_backend: str | None = None

    package_manager_frontend: str | None = None

    # ---------------------------------------------------------
    # Extra technologies selected by plugins
    # ---------------------------------------------------------

    technologies: list[str] = field(default_factory=list)
    def as_dict(self):
        return self.__dict__

    def to_dict(self):
        return self.as_dict()

