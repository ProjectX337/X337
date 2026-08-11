from __future__ import annotations

from typing import Any

from core.planner.capability_match import CapabilityMatch
from core.planner.models import ParsedPrompt
from core.spec.models.feature_spec import FeatureSpec


class FeaturePlanner:
    """
    Converts canonical CapabilityMatch objects into canonical FeatureSpec
    objects.

    Canonical flow:

        CapabilityMatch
              ↓
        Capability feature_definitions
              ↓
          FeatureSpec
              ↓
        UI / architecture / generation

    A single capability may produce multiple FeatureSpec objects.
    """

    # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    @staticmethod
    def _route(page: str) -> str:
        return (
            "/"
            + page.lower()
            .strip()
            .replace(" ", "-")
        )

    @staticmethod
    def _slug(value: str) -> str:
        return (
            value.lower()
            .strip()
            .replace("_", "-")
            .replace(" ", "-")
        )

    # ---------------------------------------------------------
    # Capability -> FeatureSpec
    # ---------------------------------------------------------

    def _to_feature_specs(
        self,
        match: CapabilityMatch,
    ) -> list[FeatureSpec]:

        capability = match.capability

        definitions = capability.feature_definitions

        # -----------------------------------------------------
        # Modern canonical representation
        # -----------------------------------------------------

        if definitions:

            features: list[FeatureSpec] = []

            for definition in definitions:

                name = definition.get(
                    "name",
                    capability.name,
                )

                slug = definition.get(
                    "slug",
                    self._slug(name),
                )

                pages = list(
                    definition.get(
                        "pages",
                        [],
                    )
                )

                components = list(
                    definition.get(
                        "components",
                        [],
                    )
                )

                api_contracts = list(
                    definition.get(
                        "api_endpoints",
                        [],
                    )
                )

                metadata: dict[str, Any] = dict(
                    capability.metadata
                )

                metadata.update(
                    {
                        "capability": capability.name,
                        "capability_score": match.score,
                        "capability_confidence": (
                            match.confidence
                        ),
                        "dependencies": list(
                            capability.depends_on
                        ),
                        "implied_capabilities": list(
                            capability.implies
                        ),
                        "conflicts": list(
                            capability.conflicts_with
                        ),
                        "technologies": list(
                            capability.technologies
                        ),
                        "required_roles": list(
                            capability.required_roles
                        ),
                    }
                )

                # Don't duplicate the entire feature list
                # inside each FeatureSpec metadata object.
                metadata.pop(
                    "features",
                    None,
                )

                metadata["feature_definition"] = dict(
                    definition
                )

                features.append(
                    FeatureSpec(
                        name=name,
                        slug=slug,
                        description=definition.get(
                            "description",
                            capability.description,
                        ),
                        routes=[
                            self._route(page)
                            for page in pages
                        ],
                        pages=pages,
                        components=components,
                        state=list(
                            definition.get(
                                "state",
                                [],
                            )
                        ),
                        api_contracts=api_contracts,
                        metadata=metadata,
                    )
                )

            return features

        # -----------------------------------------------------
        # Legacy capability representation
        # -----------------------------------------------------

        pages = list(
            capability.pages
        )

        components = list(
            capability.components
        )

        return [
            FeatureSpec(
                name=capability.name,
                slug=capability.slug,
                description=capability.description,
                routes=[
                    self._route(page)
                    for page in pages
                ],
                pages=pages,
                components=components,
                state=[],
                api_contracts=list(
                    capability.api_endpoints
                ),
                metadata={
                    "capability": capability.name,
                    "capability_score": match.score,
                    "capability_confidence": (
                        match.confidence
                    ),
                    "dependencies": list(
                        capability.depends_on
                    ),
                    "implied_capabilities": list(
                        capability.implies
                    ),
                    "conflicts": list(
                        capability.conflicts_with
                    ),
                    "technologies": list(
                        capability.technologies
                    ),
                    "required_roles": list(
                        capability.required_roles
                    ),
                },
            )
        ]

    # ---------------------------------------------------------
    # Main planner
    # ---------------------------------------------------------

    def plan(
        self,
        *,
        parsed: ParsedPrompt | None = None,
        capabilities: list[CapabilityMatch] | None = None,
        prompt: str | None = None,
    ) -> list[FeatureSpec]:

        matches = capabilities or []

        features: list[FeatureSpec] = []

        for match in matches:
            features.extend(
                self._to_feature_specs(match)
            )

        return features

    # ---------------------------------------------------------
    # Compatibility adapter
    # ---------------------------------------------------------

    def plan_application(
        self,
        parsed: ParsedPrompt | None = None,
        capabilities: list[CapabilityMatch] | None = None,
        prompt: str | None = None,
    ) -> dict:

        features = self.plan(
            parsed=parsed,
            capabilities=capabilities,
            prompt=prompt,
        )

        pages = []
        components = []
        services = []

        for feature in features:

            for index, page_name in enumerate(
                feature.pages
            ):

                route = (
                    feature.routes[index]
                    if index < len(feature.routes)
                    else self._route(page_name)
                )

                pages.append(
                    {
                        "name": page_name,
                        "route": route,
                        "components": list(
                            feature.components
                        ),
                    }
                )

            components.extend(
                feature.components
            )

            services.extend(
                feature.api_contracts
            )

        return {
            "features": features,
            "pages": pages,
            "components": sorted(
                set(components)
            ),
            "services": sorted(
                set(services)
            ),
        }
