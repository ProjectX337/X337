from __future__ import annotations

from core.features.feature_engine import FeatureEngine
from core.planner.models import ParsedPrompt
from core.planner.capability_match import CapabilityMatch
from core.spec.models.feature_spec import FeatureSpec


class FeaturePlanner:
    """
    Converts feature intelligence into canonical FeatureSpec objects.

    Canonical pipeline:

        Prompt
            ↓
        FeatureEngine
            ↓
        FeatureBlueprint
            ↓
        FeatureSpec
            ↓
        downstream planners / generators
    """

    def __init__(self) -> None:
        self.engine = FeatureEngine()

    # ---------------------------------------------------------
    # Blueprint → FeatureSpec
    # ---------------------------------------------------------

    def _to_feature_spec(
        self,
        blueprint,
    ) -> FeatureSpec:

        slug = (
            blueprint.name
            .lower()
            .strip()
            .replace(" ", "-")
            .replace("_", "-")
        )

        routes = [
            f"/{page.lower().replace(' ', '-')}"
            for page in blueprint.pages
        ]

        metadata = {
            "category": blueprint.category,
            "services": list(blueprint.services),
            "ai_capabilities": list(
                blueprint.ai_capabilities
            ),
            "analytics": list(
                blueprint.analytics
            ),
        }

        return FeatureSpec(
            name=blueprint.name,
            slug=slug,
            description=(
                f"{blueprint.name} application capability."
            ),
            routes=routes,
            pages=list(blueprint.pages),
            components=list(blueprint.components),
            state=[],
            api_contracts=list(blueprint.services),
            metadata=metadata,
        )

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

        if prompt is None and parsed is not None:
            prompt = parsed.original

        if prompt is None:
            prompt = ""

        blueprints = self.engine.analyze(prompt)

        return [
            self._to_feature_spec(
                blueprint
            )
            for blueprint in blueprints
        ]

    # ---------------------------------------------------------
    # Compatibility helper
    # ---------------------------------------------------------

    def plan_application(
        self,
        parsed: ParsedPrompt | None = None,
        capabilities: list[CapabilityMatch] | None = None,
        prompt: str | None = None,
    ) -> dict:
        """
        Compatibility adapter for older ApplicationComposer code.

        New code should use plan(), which returns FeatureSpec[].
        """

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
                    else f"/{page_name.lower().replace(' ', '-')}"
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
