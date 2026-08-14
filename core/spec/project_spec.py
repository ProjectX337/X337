from __future__ import annotations

from dataclasses import dataclass, field, fields, is_dataclass
from enum import Enum
from typing import Any

from core.planner.models import Intent, ParsedPrompt
from core.planner.capability_match import CapabilityMatch
from core.planner.technology_plan import TechnologyPlan
from core.planner.stack_builder import ArchitectureStack
from core.graph.models import ApplicationGraph

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

    architecture: ArchitectureStack | None = None

    capabilities: list[CapabilityMatch] = field(
        default_factory=list
    )

    technologies: TechnologyPlan = field(
        default_factory=TechnologyPlan
    )

    application_graph: ApplicationGraph = field(
        default_factory=ApplicationGraph
    )

    graph_intelligence: dict | None = None

    # ---------------------------------------------------------
    # Identity
    # ---------------------------------------------------------

    name: str = ""

    framework: str = ""

    path: str = ""

    # ---------------------------------------------------------
    # Product
    # ---------------------------------------------------------

    feature_models: list[FeatureSpec] = field(
        default_factory=list
    )

    # ---------------------------------------------------------
    # Intelligence
    # ---------------------------------------------------------

    product_spec: object | None = None

    product_understanding: object | None = None

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
        feature: FeatureSpec,
    ) -> None:
        if not isinstance(feature, FeatureSpec):
            raise TypeError(
                "ProjectSpec.add_feature() requires FeatureSpec"
            )

        if not any(
            existing.slug == feature.slug
            for existing in self.feature_models
        ):
            self.feature_models.append(feature)

    # ---------------------------------------------------------
    # Serialization
    # ---------------------------------------------------------

    def _serialize_value(self, value: Any) -> Any:

        if value is None:
            return None

        if isinstance(value, (str, int, float, bool)):
            return value

        if isinstance(value, Enum):
            return value.value

        if isinstance(value, list):
            return [
                self._serialize_value(item)
                for item in value
            ]

        if isinstance(value, tuple):
            return [
                self._serialize_value(item)
                for item in value
            ]

        if isinstance(value, dict):
            return {
                str(key): self._serialize_value(item)
                for key, item in value.items()
            }

        if hasattr(value, "as_dict") and callable(value.as_dict):
            return self._serialize_value(value.as_dict())

        if hasattr(value, "to_dict") and callable(value.to_dict):
            return self._serialize_value(value.to_dict())

        if is_dataclass(value):
            return {
                field.name: self._serialize_value(
                    getattr(value, field.name)
                )
                for field in fields(value)
            }

        raise TypeError(
            f"ProjectSpec cannot serialize "
            f"{type(value).__name__}"
        )


    def as_dict(self) -> dict[str, Any]:

        return {
            "prompt": self.prompt,
            "name": self.name,
            "project_name": self.project_name,
            "slug": self.slug,
            "description": self.description,
            "framework": self.framework,
            "path": self.path,

            "parsed": self._serialize_value(self.parsed),
            "intent": self._serialize_value(self.intent),
            "architecture": self._serialize_value(self.architecture),
            "architecture_name": self.architecture_name,

            "capabilities": self._serialize_value(
                self.capabilities
            ),

            "technologies": self._serialize_value(
                self.technologies
            ),

            "application_graph": self._serialize_value(
                self.application_graph
            ),

            "feature_models": self._serialize_value(
                self.feature_models
            ),

            "ui_spec": self._serialize_value(
                self.ui_spec
            ),

            "design_spec": self._serialize_value(
                self.design_spec
            ),

            "dependencies": self._serialize_value(
                self.dependencies
            ),

            "files": self._serialize_value(
                self.files
            ),

            "language": self.language,
            "version": self.version,
            "author": self.author,

            "generated": self.generated,
            "tested": self.tested,
            "reviewed": self.reviewed,
            "deployed": self.deployed,

            "warnings": self._serialize_value(
                self.warnings
            ),

            "errors": self._serialize_value(
                self.errors
            ),

            "score": self.score,

            "plan": self._serialize_value(
                self.plan
            ),

            "metadata": self._serialize_value(
                self.metadata
            ),
        }

    def to_dict(self) -> dict[str, Any]:
        return self.as_dict()
