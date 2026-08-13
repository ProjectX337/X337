from __future__ import annotations

from core.intelligence.models import (
    ProductIntent,
    ProductUnderstanding,
)


class ProductUnderstandingSynthesizer:
    """
    Converts raw product intent into
    a higher-level product understanding artifact.
    """

    def synthesize(
        self,
        intent: ProductIntent,
    ) -> ProductUnderstanding:

        return ProductUnderstanding(
            domain=intent.domain,
            users=list(intent.users),
            goals=list(intent.goals),
            workflows=list(intent.workflows),
            capabilities=list(intent.capabilities),
            quality_attributes=list(
                intent.quality_attributes
            ),
            entities=list(intent.entities),
            business_rules=list(
                intent.business_rules
            ),
            metadata={
                "source": "product_intelligence",
                "derived_from": "ProductIntent",
            },
        )
