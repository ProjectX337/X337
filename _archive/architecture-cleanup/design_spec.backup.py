from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class DesignSpec:
    """
    High-level product design decisions inferred by the planner.
    """

    layout: str = "default"

    theme: str = "modern"

    primary_color: str = "cyan"

    background: str = "dark"

    typography: str = "modern"

    motion: str = "standard"

    density: str = "comfortable"

    glassmorphism: bool = False
