from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ChangePlan:

    feature: str

    routes: list[str] = field(
        default_factory=list
    )

    pages: list[str] = field(
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


    def to_dict(self):

        return {
            "feature": self.feature,

            "routes": self.routes,

            "pages": self.pages,

            "components": self.components,

            "state": self.state,

            "api_contracts": self.api_contracts,
        }
