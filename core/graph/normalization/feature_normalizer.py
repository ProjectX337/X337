from __future__ import annotations

from core.spec.models.feature_spec import FeatureSpec
from core.graph.normalization.feature_identity import (
    normalize_feature_slug,
)


class FeatureNormalizer:
    """
    Canonicalizes FeatureSpec identity.

    Ensures semantically equivalent features
    collapse into one canonical feature.
    """

    def normalize(
        self,
        features: list[FeatureSpec],
    ) -> list[FeatureSpec]:

        canonical: dict[str, FeatureSpec] = {}

        for feature in features:

            slug = normalize_feature_slug(
                feature.slug
            )

            existing = canonical.get(slug)

            if existing is None:
                feature.slug = slug
                canonical[slug] = feature
                continue

            self._merge(
                existing,
                feature,
            )

        return list(
            canonical.values()
        )

    def _merge(
        self,
        target: FeatureSpec,
        source: FeatureSpec,
    ) -> None:

        for attr in [
            "pages",
            "routes",
            "components",
            "state",
            "api_contracts",
        ]:
            values = getattr(
                source,
                attr,
                [],
            )

            target_values = getattr(
                target,
                attr,
                [],
            )

            for value in values:
                if value not in target_values:
                    target_values.append(value)

        if (
            not target.description
            and source.description
        ):
            target.description = source.description
