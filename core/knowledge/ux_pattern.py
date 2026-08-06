from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class UXSection:

    name: str

    components: list[str] = field(default_factory=list)


@dataclass(slots=True)
class UXPattern:

    name: str

    sections: list[UXSection] = field(default_factory=list)
