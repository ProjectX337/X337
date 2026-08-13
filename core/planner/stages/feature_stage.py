from __future__ import annotations

from core.cognition.cognitive_state import CognitiveState
from core.planner.feature_planner import FeaturePlanner
from core.graph.normalization.feature_normalizer import FeatureNormalizer
from core.planner.stages.base_stage import PlanningStage
from core.spec.models.feature_spec import FeatureSpec


class FeatureStage(PlanningStage):
    """
    Creates canonical FeatureSpec objects from capability matches.

    Feature identity is normalized here, at the canonical feature
    boundary. Downstream planners and generators consume only the
    normalized FeatureSpec collection.
    """

    requires = {
        "parsed",
        "capabilities",
    }

    provides = {
        "feature_models",
    }

    # Synonymous capability/feature identities converge here.
    FEATURE_ALIASES = {
        "chat": "ai",
    }

    def __init__(self) -> None:
        self.planner = FeaturePlanner()
        self.normalizer = FeatureNormalizer()

    @classmethod
    def _canonical_slug(cls, slug: str) -> str:
        normalized = (
            str(slug)
            .strip()
            .lower()
            .replace("_", "-")
            .replace(" ", "-")
        )

        return cls.FEATURE_ALIASES.get(
            normalized,
            normalized,
        )

    @staticmethod
    def _merge_unique(
        target: list[str],
        values: list[str],
    ) -> None:
        for value in values:
            if value not in target:
                target.append(value)

    @classmethod
    def _canonicalize(
        cls,
        features: list[FeatureSpec],
    ) -> list[FeatureSpec]:
        canonical: dict[str, FeatureSpec] = {}

        for feature in features:
            slug = cls._canonical_slug(feature.slug)

            existing = canonical.get(slug)

            if existing is None:
                feature.slug = slug
                canonical[slug] = feature
                continue

            cls._merge_unique(
                existing.pages,
                feature.pages,
            )

            cls._merge_unique(
                existing.routes,
                feature.routes,
            )

            cls._merge_unique(
                existing.components,
                feature.components,
            )

            cls._merge_unique(
                existing.state,
                feature.state,
            )

            cls._merge_unique(
                existing.api_contracts,
                feature.api_contracts,
            )

            if (
                not existing.description
                and feature.description
            ):
                existing.description = feature.description

            existing.metadata.setdefault(
                "merged_feature_sources",
                [],
            )

            source_name = (
                feature.name
                or feature.slug
            )

            if source_name not in existing.metadata[
                "merged_feature_sources"
            ]:
                existing.metadata[
                    "merged_feature_sources"
                ].append(source_name)

        return list(canonical.values())

    def run(
        self,
        context: CognitiveState,
    ) -> None:
        features = self.planner.plan(
            parsed=context.parsed,
            capabilities=context.capabilities,
        )

        context.feature_models = self.normalizer.normalize(
            features
        )
