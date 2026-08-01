from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Architecture:
    """
    Registered architecture.

    Everything about an architecture should be declared
    in plugin metadata instead of hardcoded in the planner.
    """

    name: str

    language: str

    template: str

    tester: str

    dependencies: list[str] = field(default_factory=list)

    default_features: list[str] = field(default_factory=list)

    keywords: list[str] = field(default_factory=list)

    roles: list[str] = field(default_factory=list)

    # NEW
    technology_defaults: dict[str, Any] = field(default_factory=dict)

    metadata: dict[str, Any] = field(default_factory=dict)