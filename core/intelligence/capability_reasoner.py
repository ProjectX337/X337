from __future__ import annotations

from core.capabilities.capability_registry import CapabilityRegistry
from core.intelligence.models import ProductIntent


class CapabilityReasoner:
    """
    Converts product intent into capability candidates.

    Initial implementation uses the existing capability
    vocabulary. Future versions can add deeper reasoning.
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

        matches: list[str] = []

        for capability in self.registry.all():

            if any(
                keyword.lower() in searchable
                for keyword in capability.keywords
            ):
                matches.append(
                    capability.name
                )

        return sorted(
            set(matches)
        )
