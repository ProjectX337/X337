from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ProductUnderstanding:
    """
    Higher-level product intelligence artifact.

    Represents what the system believes
    the product should become.
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

    quality_attributes: list[str] = field(
        default_factory=list
    )

    entities: list[str] = field(
        default_factory=list
    )

    business_rules: list[str] = field(
        default_factory=list
    )

    metadata: dict = field(
        default_factory=dict
    )
