from __future__ import annotations

from core.graph.normalization.capability_identity import (
    normalize_capability_slug,
)


class CapabilityNormalizer:
    """
    Canonicalizes capability identities before graph construction.

    Capability normalization collapses semantic aliases while
    preserving the canonical capability object.
    """

    def normalize(
        self,
        capabilities: list,
    ) -> list:

        normalized = []

        seen = set()

        for capability in capabilities:

            slug = normalize_capability_slug(
                capability.slug
            )

            if slug in seen:
                continue

            seen.add(slug)

            normalized.append(
                capability
            )

        return normalized
