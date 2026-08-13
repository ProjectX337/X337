from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ProductIntent:
    """
    Canonical product understanding model.

    Represents what the user is trying to create,
    independent of implementation details.
    """

    domain: str = ""

    users: list[str] = field(
        default_factory=list
    )

    goals: list[str] = field(
        default_factory=list
    )

    workflows: list[str] = field(
        default_factory=list
    )

    capabilities: list[str] = field(
        default_factory=list
    )

    constraints: list[str] = field(
        default_factory=list
    )

    quality_attributes: list[str] = field(
        default_factory=list
    )

    entities: list[str] = field(
        default_factory=list
    )

    metadata: dict = field(
        default_factory=dict
    )

    def as_dict(self) -> dict:
        return {
            "domain": self.domain,
            "users": self.users,
            "goals": self.goals,
            "workflows": self.workflows,
            "capabilities": self.capabilities,
            "constraints": self.constraints,
            "quality_attributes": self.quality_attributes,
            "entities": self.entities,
            "metadata": self.metadata,
        }
