from __future__ import annotations

from core.capabilities.capability_registry import (
    CapabilityRegistry,
)

from core.planner.capability_match import (
    CapabilityMatch,
)


class ResolvedCapabilityFeatureAdapter:
    """
    Converts intelligence-layer ResolvedCapability
    objects into planner CapabilityMatch objects.

    Compatibility bridge:
        ResolvedCapability
              |
              v
        CapabilityMatch
              |
              v
        FeaturePlanner
    """

    def __init__(self):
        self.registry = CapabilityRegistry()

    def convert(
        self,
        resolved_capabilities,
    ) -> list[CapabilityMatch]:

        matches = []

        for resolved in resolved_capabilities:

            capability = self.registry.get(
                resolved.name
            )

            if capability is None:
                continue

            matches.append(
                CapabilityMatch(
                    capability=capability,
                    score=int(
                        resolved.confidence * 5
                    ),
                    confidence=resolved.confidence,
                )
            )

        return matches
