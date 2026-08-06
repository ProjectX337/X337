from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class DesignSpec:
    """
    High-level visual design decisions inferred by the planner.

    This becomes the single source of truth for every frontend generator.
    """

    # Overall experience
    layout: str = "default"
    theme: str = "modern"

    # Color system
    primary_color: str = "cyan"
    background: str = "dark"

    # Typography
    typography: str = "modern"

    # Layout language
    spacing: str = "comfortable"
    density: str = "comfortable"

    # Visual language
    radius: str = "medium"
    elevation: str = "flat"
    surface_style: str = "solid"

    # Motion
    motion: str = "standard"

    # Icons
    icon_style: str = "outlined"

    # Effects
    glassmorphism: bool = False
