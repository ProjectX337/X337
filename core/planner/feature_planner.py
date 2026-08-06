from __future__ import annotations

from core.planner.capability_match import CapabilityMatch
from core.spec.models.feature_spec import FeatureSpec


class FeaturePlanner:
    """
    Converts capabilities into structured product features.
    """

    def plan(
        self,
        parsed,
        capabilities: list[CapabilityMatch],
    ) -> list[FeatureSpec]:

        features: list[FeatureSpec] = []

        for match in capabilities:

            capability = match.capability

            definitions = capability.metadata.get(
                "features",
                [],
            )

            for item in definitions:

                features.append(
                    FeatureSpec(
                        name=item["name"],
                        slug=item.get(
                            "slug",
                            item["name"]
                            .lower()
                            .replace(" ", "_")
                        ),
                        description=item.get(
                            "description",
                            "",
                        ),
                        pages=item.get(
                            "pages",
                            [],
                        ),
                        components=item.get(
                            "components",
                            [],
                        ),
                        api_contracts=item.get(
                            "api_endpoints",
                            [],
                        ),
                        metadata={
                            "source_capability": capability.name
                        },
                    )
                )

        return features
