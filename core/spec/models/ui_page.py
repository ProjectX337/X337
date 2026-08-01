from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class UIPage:

    name: str

    route: str

    layout: str = "default"

    components: list[str] = field(
        default_factory=list
    )
