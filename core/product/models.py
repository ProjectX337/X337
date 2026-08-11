from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ProductRequirement:
    id: str
    description: str
    source: str = "user"
    confidence: float = 1.0
    mandatory: bool = True
    rationale: str = ""


@dataclass
class UserGoal:
    id: str
    description: str
    priority: float = 1.0


@dataclass
class UserFlow:
    id: str
    name: str
    steps: list[str] = field(default_factory=list)
    priority: float = 1.0


@dataclass
class ProductFeature:
    id: str
    name: str
    description: str = ""
    source: str = "explicit"
    confidence: float = 1.0
    mandatory: bool = True
    dependencies: list[str] = field(default_factory=list)


@dataclass
class ProductSpec:
    name: str = ""
    description: str = ""
    product_type: str = ""

    users: list[str] = field(default_factory=list)
    goals: list[UserGoal] = field(default_factory=list)
    requirements: list[ProductRequirement] = field(default_factory=list)
    workflows: list[UserFlow] = field(default_factory=list)
    features: list[ProductFeature] = field(default_factory=list)

    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def explicit_features(self) -> list[ProductFeature]:
        return [
            feature
            for feature in self.features
            if feature.source == "explicit"
        ]

    @property
    def required_features(self) -> list[ProductFeature]:
        return [
            feature
            for feature in self.features
            if feature.mandatory
        ]

    @property
    def optional_features(self) -> list[ProductFeature]:
        return [
            feature
            for feature in self.features
            if not feature.mandatory
        ]