from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class UIComponent:
    name: str

    component_type: str = "component"

    props: dict[str, Any] = field(
        default_factory=dict
    )

    variants: list[str] = field(
        default_factory=list
    )

    states: list[str] = field(
        default_factory=list
    )

    children: list[str] = field(
        default_factory=list
    )

    dependencies: list[str] = field(
        default_factory=list
    )

    metadata: dict[str, Any] = field(
        default_factory=dict
    )
