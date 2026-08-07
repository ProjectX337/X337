from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from core.planner.models import Intent, ParsedPrompt
from core.planner.capability_match import CapabilityMatch
from core.planner.technology_plan import TechnologyPlan
from core.spec.ui_spec import UISpec
from core.spec.models.feature_spec import FeatureSpec
from core.spec.models.design_spec import DesignSpec


@dataclass(slots=True)
class ProjectSpec:
    """
    Canonical project representation passed through X337.

    This is the bridge between planning,
    architecture, generation, and memory.
    """

    # -----------------------------
    # Planning Input
    # -----------------------------

    prompt: str = ""

    parsed: ParsedPrompt | None = None

    intent: Intent | None = None

    architecture: Any = None

    capabilities: list[CapabilityMatch] = field(
        default_factory=list
    )

    technologies: TechnologyPlan = field(
        default_factory=TechnologyPlan
    )


    # -----------------------------
    # Identity
    # -----------------------------

    name: str = ""

    framework: str = ""

    path: str = ""


    # -----------------------------
    # Product Models
    # -----------------------------

    features: list[str] = field(
        default_factory=list
    )

    feature_models: list[FeatureSpec] = field(
        default_factory=list
    )

    ui_spec: UISpec | None = None

    design_spec: DesignSpec | None = None


    # -----------------------------
    # Engineering
    # -----------------------------

    architecture_name: str = ""

    dependencies: list[str] = field(
        default_factory=list
    )

    files: dict[str, str] = field(
        default_factory=dict
    )


    language: str = "python"

    version: str = "1.0.0"

    _description: str = ""

    author: str = "X337"


    # -----------------------------
    # State
    # -----------------------------

    generated: bool = False

    tested: bool = False

    reviewed: bool = False

    deployed: bool = False


    warnings: list[str] = field(
        default_factory=list
    )

    errors: list[str] = field(
        default_factory=list
    )

    score: int = 0


    # -----------------------------
    # Extra
    # -----------------------------

    plan: dict[str, Any] = field(
        default_factory=dict
    )

    metadata: dict[str, Any] = field(
        default_factory=dict
    )


    @property
    def project_name(self) -> str:
        if self.parsed:
            return self.parsed.project_name
        return self.name


    @property
    def description(self) -> str:
        if self.parsed:
            return self.parsed.description
        return ""


    @property
    def keywords(self) -> list[str]:
        if self.parsed:
            return self.parsed.keywords
        return []


    @property
    def slug(self) -> str:
        return self.project_name.lower().replace(" ", "-")


    # -----------------------------
    # Helpers
    # -----------------------------

    @property
    def description(self) -> str:
        if self.parsed:
            return self.parsed.description
        return self._description


    def add_file(
        self,
        filename: str,
        content: str,
    ):
        self.files[filename] = content


    def add_dependency(
        self,
        dependency: str,
    ):
        if dependency not in self.dependencies:
            self.dependencies.append(
                dependency
            )


    def add_feature(
        self,
        feature: str,
    ):
        if feature not in self.features:
            self.features.append(
                feature
            )





    @property
    def description_text(self) -> str:
        if self.parsed:
            return self.parsed.description
        return self.description

    @property
    def slug(self) -> str:
        return self.project_name.lower().replace(" ", "-")

    @property
    def project_name(self) -> str:
        if self.parsed:
            return self.parsed.project_name
        return self.name


    def as_dict(self):

        return {
            "prompt": self.prompt,
            "name": self.name,
            "framework": self.framework,
            "architecture": self.architecture,
            "features": self.features,
            "feature_models": [
                f.as_dict()
                for f in self.feature_models
            ],
            "technologies":
                self.technologies.as_dict(),

            "dependencies":
                self.dependencies,

            "files":
                self.files,

            "ui_spec":
                self.ui_spec,

            "design_spec":
                self.design_spec,

            "metadata":
                self.metadata,
        }


    def to_dict(self):
        return self.as_dict()
