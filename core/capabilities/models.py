from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ComponentTemplate:
    name: str


@dataclass
class PageTemplate:
    name: str
    components: list[str] = field(default_factory=list)


@dataclass
class FeatureTemplate:
    name: str
    slug: str
    description: str
    pages: list[PageTemplate] = field(default_factory=list)
    components: list[ComponentTemplate] = field(default_factory=list)
    api_endpoints: list[str] = field(default_factory=list)


@dataclass
class Capability:
    name: str
    description: str
    keywords: list[str]
    technologies: list[str]
    required_roles: list[str]
    priority: int = 0
    features: list[FeatureTemplate] = field(default_factory=list)
