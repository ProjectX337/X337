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
    def framework(self) -> str:
        if self.technologies:
            return getattr(
                self.technologies,
                "framework",
                "python"
            )

        return self.metadata.get(
            "framework",
            "python"
        )


    @framework.setter
    def framework(self, value: str):
        self.metadata["framework"] = value


    @property
    def plan(self) -> dict:
        return self.metadata.setdefault(
            "plan",
            {}
        )


    @plan.setter
    def plan(self, value):
        self.metadata["plan"] = value


    def add_feature(self, feature):
        if feature not in self.features:
            self.features.append(feature)


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
