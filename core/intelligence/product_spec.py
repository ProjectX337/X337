
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ProductSpec:
    """
    Engineering-ready product definition.

    Represents what should be built,
    independent of implementation.
    """

    name: str = ""

    description: str = ""

    product_type: str = ""

    features: list[str] = field(
        default_factory=list
    )

    pages: list[str] = field(
        default_factory=list
    )

    workflows: list[str] = field(
        default_factory=list
    )

    entities: list[str] = field(
        default_factory=list
    )

    capabilities: list[str] = field(
        default_factory=list
    )

    quality_attributes: list[str] = field(
        default_factory=list
    )

    technical_requirements: list[str] = field(
        default_factory=list
    )

    metadata: dict = field(
        default_factory=dict
    )

    def as_dict(self) -> dict:
        return {
            "name": self.name,
            "description": self.description,
            "product_type": self.product_type,
            "features": self.features,
            "pages": self.pages,
            "workflows": self.workflows,
            "entities": self.entities,
            "capabilities": self.capabilities,
            "quality_attributes": self.quality_attributes,
            "technical_requirements": self.technical_requirements,
            "metadata": self.metadata,
        }
