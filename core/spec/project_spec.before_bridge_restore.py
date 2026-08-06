from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from core.planner.technology_plan import TechnologyPlan


@dataclass(slots=True)
class ProjectSpec:
    """
    Canonical representation of a project inside X337.
    """

    # Identity
    name: str = ""
    framework: str = ""
    path: str = ""

    # Planning
    architecture: str = ""
    technologies: TechnologyPlan = field(default_factory=TechnologyPlan)

    features: list[str] = field(default_factory=list)
    dependencies: list[str] = field(default_factory=list)
    files: dict[str, str] = field(default_factory=dict)

    # Metadata
    language: str = "python"
    version: str = "1.0.0"
    description: str = ""
    author: str = "X337"

    # Quality
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    score: int = 0

    # Execution State
    generated: bool = False
    tested: bool = False
    reviewed: bool = False
    deployed: bool = False

    # Optional Data
    plan: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def add_file(self, filename: str, content: str) -> None:
        self.files[filename] = content

    def add_dependency(self, dependency: str) -> None:
        if dependency not in self.dependencies:
            self.dependencies.append(dependency)

    def add_feature(self, feature: str) -> None:
        if feature not in self.features:
            self.features.append(feature)

    def warning(self, message: str) -> None:
        self.warnings.append(message)

    def error(self, message: str) -> None:
        self.errors.append(message)

    def as_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "framework": self.framework,
            "path": self.path,
            "architecture": self.architecture,
            "technologies": self.technologies.as_dict(),
            "features": self.features,
            "dependencies": self.dependencies,
            "files": self.files,
            "language": self.language,
            "version": self.version,
            "description": self.description,
            "author": self.author,
            "warnings": self.warnings,
            "errors": self.errors,
            "score": self.score,
            "generated": self.generated,
            "tested": self.tested,
            "reviewed": self.reviewed,
            "deployed": self.deployed,
            "plan": self.plan,
            "metadata": self.metadata,
        }

    def to_dict(self) -> dict[str, Any]:
        return self.as_dict()
