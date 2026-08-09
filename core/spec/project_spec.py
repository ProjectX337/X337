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

    ProjectSpec is the bridge between:

        planning
            ↓
        architecture
            ↓
        design
            ↓
        generation
            ↓
        testing
            ↓
        deployment
            ↓
        memory
    """

    # ---------------------------------------------------------
    # Planning input
    # ---------------------------------------------------------

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

    # ---------------------------------------------------------
    # Identity
    # ---------------------------------------------------------

    name: str = ""

    framework: str = ""

    path: str = ""

    # ---------------------------------------------------------
    # Product
    # ---------------------------------------------------------

    features: list[str] = field(
        default_factory=list
    )

    feature_models: list[FeatureSpec] = field(
        default_factory=list
    )

    ui_spec: UISpec | None = None

    design_spec: DesignSpec | None = None

    # ---------------------------------------------------------
    # Engineering
    # ---------------------------------------------------------

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

    # ---------------------------------------------------------
    # Lifecycle state
    # ---------------------------------------------------------

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

    # ---------------------------------------------------------
    # Extra
    # ---------------------------------------------------------

    plan: dict[str, Any] = field(
        default_factory=dict
    )

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    # ---------------------------------------------------------
    # Derived identity
    # ---------------------------------------------------------

    @property
    def project_name(self) -> str:
        if self.parsed and self.parsed.project_name:
            return self.parsed.project_name

        return self.name

    @property
    def description(self) -> str:
        if self.parsed and self.parsed.description:
            return self.parsed.description

        return self._description

    @property
    def description_text(self) -> str:
        return self.description

    @property
    def keywords(self) -> list[str]:
        if self.parsed:
            return self.parsed.keywords

        return []

    @property
    def slug(self) -> str:
        return (
            self.project_name
            .lower()
            .strip()
            .replace(" ", "-")
        )

    # ---------------------------------------------------------
    # Mutation helpers
    # ---------------------------------------------------------

    def add_file(
        self,
        filename: str,
        content: str,
    ) -> None:
        self.files[filename] = content

    def add_dependency(
        self,
        dependency: str,
    ) -> None:
        if dependency not in self.dependencies:
            self.dependencies.append(
                dependency
            )

    def add_feature(
        self,
        feature: str,
    ) -> None:
        if feature not in self.features:
            self.features.append(
                feature
            )

    # ---------------------------------------------------------
    # Serialization
    # ---------------------------------------------------------

    def as_dict(self) -> dict[str, Any]:
        return {
            "prompt": self.prompt,
            "name": self.name,
            "project_name": self.project_name,
            "slug": self.slug,
            "description": self.description,
            "framework": self.framework,
            "path": self.path,
            "architecture": self.architecture,
            "architecture_name": self.architecture_name,
            "features": self.features,
            "feature_models": [
                feature.as_dict()
                for feature in self.feature_models
            ],
            "capabilities": [
                capability
                for capability in self.capabilities
            ],
            "technologies": (
                self.technologies.as_dict()
                if hasattr(
                    self.technologies,
                    "as_dict",
                )
                else self.technologies
            ),
            "dependencies": self.dependencies,
            "files": self.files,
            "language": self.language,
            "version": self.version,
            "author": self.author,
            "generated": self.generated,
            "tested": self.tested,
            "reviewed": self.reviewed,
            "deployed": self.deployed,
            "warnings": self.warnings,
            "errors": self.errors,
            "score": self.score,
            "plan": self.plan,
            "metadata": self.metadata,
            "ui_spec": (
                self.ui_spec.as_dict()
                if self.ui_spec is not None
                else None
            ),
            "design_spec": (
                self.design_spec
                if self.design_spec is not None
                else None
            ),
        }

    def to_dict(self) -> dict[str, Any]:
        return self.as_dict()
