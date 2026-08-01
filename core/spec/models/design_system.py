from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class DesignSystem:

    colors: dict[str, str] = field(
        default_factory=dict
    )

    typography: dict[str, str] = field(
        default_factory=dict
    )

    spacing: dict[str, str] = field(
        default_factory=dict
    )
