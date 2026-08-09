from __future__ import annotations

from core.planner.models import Intent
from core.planner.capability_match import CapabilityMatch

from core.spec.models.feature_spec import FeatureSpec
from core.spec.models.ui_page import UIPage
from core.spec.models.ui_component import UIComponent
from core.spec.ui_spec import UISpec

from core.planner.design import (
    DesignComposer,
    DesignComposition,
)

from core.planner.design.ui_blueprint_builder import (
    UIBlueprintBuilder,
)


class UIPlanner:
    """
    Converts planner intelligence into the canonical UISpec.

    Pipeline:

        CapabilityMatch
              ↓
        FeatureSpec
              ↓
        DesignComposition
              ↓
        UIBlueprint
              ↓
        Canonical UIPage / UIComponent / UILayoutNode
              ↓
        UISpec
    """

    def __init__(self) -> None:
        self.design_composer = DesignComposer()
        self.blueprint_builder = UIBlueprintBuilder()

    # ---------------------------------------------------------
    # Deduplication
    # ---------------------------------------------------------

    def _dedupe_pages(
        self,
        pages: list[UIPage],
    ) -> list[UIPage]:

        seen: set[str] = set()
        result: list[UIPage] = []

        for page in pages:
            key = page.route.lower().strip()

            if key not in seen:
                seen.add(key)
                result.append(page)

        return result

    def _dedupe_components(
        self,
        components: list[UIComponent],
    ) -> list[UIComponent]:

        seen: set[str] = set()
        result: list[UIComponent] = []

        for component in components:
            key = component.name.lower().strip()

            if key not in seen:
                seen.add(key)
                result.append(component)

        return result

    # ---------------------------------------------------------
    # Main planner
    # ---------------------------------------------------------

    def plan(
        self,
        *,
        intent: Intent,
        capabilities: list[CapabilityMatch],
        features: list[FeatureSpec] | None = None,
    ) -> UISpec:

        application_name = (
            getattr(
                intent,
                "project_name",
                None,
            )
            or "AI Application"
        )

        features = features or []

        # -----------------------------------------------------
        # 1. Design intelligence
        # -----------------------------------------------------

        composition: DesignComposition = (
            self.design_composer.compose(
                application_name
            )
        )

        # -----------------------------------------------------
        # 2. Blueprint
        # -----------------------------------------------------

        blueprint = self.blueprint_builder.build(
            composition,
            application_name,
        )

        pages: list[UIPage] = []
        components: list[UIComponent] = []

        # -----------------------------------------------------
        # 3. Blueprint → canonical UI models
        # -----------------------------------------------------

        for blueprint_page in blueprint.pages:

            pages.append(
                blueprint_page
            )

            components.extend(
                blueprint_page.components
            )

        # -----------------------------------------------------
        # 4. FeatureSpec → canonical UI models
        # -----------------------------------------------------

        for feature in features:

            for index, page_name in enumerate(
                feature.pages
            ):

                if (
                    feature.routes
                    and index < len(feature.routes)
                ):
                    route = feature.routes[index]
                else:
                    route = (
                        f"/{page_name.lower().replace(' ', '-')}"
                    )

                feature_components: list[UIComponent] = []

                for component_name in feature.components:

                    component = UIComponent(
                        name=component_name,
                        component_type="feature",
                        metadata={
                            "feature": feature.slug,
                        },
                    )

                    feature_components.append(
                        component
                    )

                    components.append(
                        component
                    )

                pages.append(
                    UIPage(
                        name=page_name,
                        route=route,
                        layout=(
                            composition.layout.layout_pattern
                        ),
                        components=feature_components,
                        metadata={
                            "feature": feature.slug,
                        },
                    )
                )

        # -----------------------------------------------------
        # 5. Deduplicate
        # -----------------------------------------------------

        pages = self._dedupe_pages(
            pages
        )

        components = self._dedupe_components(
            components
        )

        # -----------------------------------------------------
        # 6. Canonical UISpec
        # -----------------------------------------------------

        return UISpec(
            layout=(
                composition.layout.layout_pattern
            ),
            theme=(
                getattr(
                    composition.design_system,
                    "theme",
                    "modern",
                )
            ),
            navigation=[
                composition.layout.navigation
            ],
            metadata={
                "generated_by":
                    "X337 Design Intelligence",
                "application":
                    application_name,
                "capability_count":
                    len(capabilities),
                "feature_count":
                    len(features),
            },
            page_models=pages,
            component_models=components,
            design_system=composition.design_system,
        )
