from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class FeatureSpec:
    """
    Application feature definition.
    """

    name: str

    description: str = ""

    routes: list[str] = field(
        default_factory=list
    )

    components: list[str] = field(
        default_factory=list
    )

    state: list[str] = field(
        default_factory=list
    )

    api_contracts: list[str] = field(
        default_factory=list
    )

@property
def slug(self) -> str:

    return (
        self.name
        .lower()
        .replace(" ", "_")
        .replace("-", "_")
    )
