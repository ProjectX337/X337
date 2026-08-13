from __future__ import annotations

from core.capabilities.capability_registry import CapabilityRegistry
from core.intelligence.models import ProductIntent
from core.intelligence.capability_patterns import PRODUCT_PATTERNS


class CapabilityReasoner:
    """
    Converts product intent into capability candidates.

    Uses semantic product patterns first,
    then falls back to capability keywords.
    """

    def __init__(self):
        self.registry = CapabilityRegistry()

    def reason(
        self,
        intent: ProductIntent,
    ) -> list[str]:

        searchable = " ".join(
            [
                intent.domain,
                *intent.goals,
                *intent.workflows,
                *intent.capabilities,
            ]
        ).lower()

        matches = set()

        # semantic product reasoning
        for pattern, capabilities in PRODUCT_PATTERNS.items():

            if pattern in searchable:

                matches.update(
                    capabilities
                )

        # existing capability vocabulary
        for capability in self.registry.all():

            if any(
                keyword.lower() in searchable
                for keyword in capability.keywords
            ):
                matches.add(
                    capability.name
                )

        return sorted(matches)
