from __future__ import annotations

from core.capabilities.capability import Capability
from core.graph.normalization.capability_identity import (
    normalize_capability_slug,
)


class CapabilityNormalizer:
    """
    Canonicalizes capability identity and merges aliases.
    """

    def normalize(
        self,
        capabilities: list[Capability],
    ) -> list[Capability]:

        canonical: dict[str, Capability] = {}

        for capability in capabilities:

            slug = normalize_capability_slug(
                capability.slug
            )

            existing = canonical.get(slug)

            if existing is None:
                capability.name = slug
                canonical[slug] = capability
                continue


            # merge dependency relationships

            for dependency in capability.depends_on:
                dependency = normalize_capability_slug(
                    dependency
                )

                if dependency not in existing.depends_on:
                    existing.depends_on.append(
                        dependency
                    )


            for implication in capability.implies:
                implication = normalize_capability_slug(
                    implication
                )

                if implication not in existing.implies:
                    existing.implies.append(
                        implication
                    )


            # merge pages

            for page in capability.pages:
                if page not in existing.pages:
                    existing.pages.append(page)


            # merge components

            for component in capability.components:
                if component not in existing.components:
                    existing.components.append(component)


        return list(
            canonical.values()
        )
