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
from core.spec.ui_spec import UISpec
from core.graph.graph import Graph
from core.spec.models.feature_spec import FeatureSpec


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

    dependencies: list[str] = field(
        default_factory=list
    )

    files: list[dict[str, str]] = field(
        default_factory=list
    )

    generated: dict[str, Any] = field(
        default_factory=dict
    )

    path: str = ""

    feature_models: list[FeatureSpec] = field(
        default_factory=list
    )

    technologies: TechnologyPlan | None = None

    ui_spec: UISpec | None = None

    task_graph: Graph | None = None

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    # Compatibility fields used by legacy generation pipeline
    name: str = ""
    framework: str = "python"
    plan: dict[str, Any] = field(
        default_factory=dict
    )
    language: str = ""



    # -------------------------------------------------
    # Backwards compatibility layer
    # -------------------------------------------------

    @property
    def name(self) -> str:
        return self.project_name


    @name.setter
    def name(self, value: str):
        self.parsed.project_name = value


    
    
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




    def add_file(
        self,
        path: str,
        content: str = ""
    ) -> None:

        self.files.append(
            {
                "path": path,
                "content": content,
            }
        )



    def as_dict(self) -> dict[str, Any]:

        return {
            "name": self.name,
            "project_name": self.project_name,
            "slug": self.slug,
            "description": self.description,
            "framework": self.framework,
            "language": self.language,
            "features": self.features,
            "dependencies": self.dependencies,
            "files": self.files,
            "generated": self.generated,
            "path": self.path,
            "plan": self.plan,
            "metadata": self.metadata,
        }


    @property
    def keywords(self) -> list[str]:

        return self.parsed.keywords
