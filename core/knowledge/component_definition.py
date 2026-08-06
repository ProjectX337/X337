from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class ComponentDefinition:

    name: str

    children: list[str] = field(default_factory=list)

    props: dict[str, str] = field(default_factory=dict)
