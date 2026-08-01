from __future__ import annotations

from core.planner.capability_match import CapabilityMatch
from core.planner.models import ParsedPrompt
from core.spec.models.feature_spec import FeatureSpec


class FeaturePlanner:
    """
    Converts capability definitions into structured product features.
    """

    def plan(
        self,
        parsed: ParsedPrompt,
        capabilities: list[CapabilityMatch],
    ) -> list[FeatureSpec]:

        features: list[FeatureSpec] = []

        for match in capabilities:

            capability = match.capability

            definitions = (
                capability.metadata.get(
                    "features",
                    [],
                )
            )

            if definitions:

                for item in definitions:

                    features.append(
                        FeatureSpec(
                            name=item.get(
                                "name",
                                capability.name,
                            ),
                            slug=item.get(
                                "slug",
                                capability.name
                                .lower()
                                .replace(" ", "_")
                                .replace("-", "_"),
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
                            api_endpoints=item.get(
                                "api_endpoints",
                                [],
                            ),
                            metadata={
                                "confidence": match.confidence,
                                "capability": capability.name,
                            },
                        )
                    )

            else:

                features.append(
                    FeatureSpec(
                        name=capability.name,
                        slug=(
                            capability.name
                            .lower()
                            .replace(" ", "_")
                            .replace("-", "_")
                        ),
                        description=(
                            f"{capability.name} capability"
                        ),
                        metadata={
                            "confidence": match.confidence,
                            "capability": capability.name,
                        },
                    )
                )

        return features
