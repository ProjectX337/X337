from __future__ import annotations

from core.capabilities.capability import Capability
from core.graph.normalization.capability_identity import (
    normalize_capability_slug,
)


class CapabilityDependencyNormalizer:
    """
    Normalizes capability dependency relationships.

    Converts depends_on and implies references
    into canonical capability identities.
    """

    def normalize(
        self,
        capabilities: list[Capability],
    ) -> list[Capability]:

        lookup = {
            normalize_capability_slug(
                capability.slug
            ): capability
            for capability in capabilities
        }

        for capability in capabilities:

            capability.depends_on = [
                normalize_capability_slug(dep)
                for dep in capability.depends_on
                if normalize_capability_slug(dep)
                in lookup
            ]

            capability.implies = [
                normalize_capability_slug(imp)
                for imp in capability.implies
                if normalize_capability_slug(imp)
                in lookup
            ]

        return capabilities
