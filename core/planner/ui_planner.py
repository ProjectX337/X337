from __future__ import annotations

from core.planner.models import Intent
from core.planner.capability_match import CapabilityMatch

from core.spec.models.feature_spec import FeatureSpec
from core.spec.models.ui_page import UIPage
from core.spec.models.ui_component import UIComponent
from core.spec.ui_spec import UISpec

from core.knowledge.product_profile import ProductProfile

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

        Intent
          ↓
        CapabilityMatch
          ↓
        FeatureSpec
          ↓
        ProductProfile
          ↓
        DesignComposition
          ↓
        UIBlueprint
          ↓
        UIPage / UIComponent
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
    # Product profile defaults
    # ---------------------------------------------------------

    def _profile_pages(
        self,
        product_profile: ProductProfile | None,
    ) -> list[str]:
        if product_profile is not None:
            if product_profile.default_pages:
                return list(product_profile.default_pages)

        return [
            "Landing",
        ]

    def _profile_components(
        self,
        product_profile: ProductProfile | None,
    ) -> list[str]:
        if product_profile is not None:
            if product_profile.default_components:
                return list(product_profile.default_components)

        return [
            "Navbar",
            "Hero",
        ]

    # ---------------------------------------------------------
    # Main planner
    # ---------------------------------------------------------

    def plan(
        self,
        *,
        intent: Intent | None,
        capabilities: list[CapabilityMatch],
        features: list[FeatureSpec] | None = None,
        product_profile: ProductProfile | None = None,
    ) -> UISpec:

        intent = intent or Intent()
        features = features or []

        application_name = (
            getattr(
                intent,
                "project_name",
                None,
            )
            or (
                product_profile.name
                if product_profile is not None
                else None
            )
            or "AI Application"
        )

        # -----------------------------------------------------
        # 1. Resolve product-level design context
        # -----------------------------------------------------

        product_type = (
            product_profile.name
            if product_profile is not None
            else application_name
        )

        composition: DesignComposition = (
            self.design_composer.compose(
                product_type
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
        # 3. Blueprint → canonical models
        # -----------------------------------------------------

        for blueprint_page in blueprint.pages:
            pages.append(blueprint_page)
            components.extend(
                blueprint_page.components
            )

        # -----------------------------------------------------
        # 4. ProductProfile → canonical models
        #
        # ProductProfile is authoritative for default pages.
        # This prevents the design composer from accidentally
        # replacing the application's product structure.
        # -----------------------------------------------------

        profile_pages = self._profile_pages(
            product_profile
        )

        profile_components = self._profile_components(
            product_profile
        )

        existing_routes = {
            page.route.lower().strip()
            for page in pages
        }

        for index, page_name in enumerate(
            profile_pages
        ):
            if index == 0:
                route = "/"
            else:
                route = (
                    f"/{page_name.lower().replace(' ', '-')}"
                )

            if route.lower() in existing_routes:
                continue

            page_components: list[UIComponent] = []

            for component_name in profile_components:
                component = UIComponent(
                    name=component_name,
                    component_type="product",
                    metadata={
                        "source": "product_profile",
                    },
                )

                page_components.append(component)
                components.append(component)

            pages.append(
                UIPage(
                    name=page_name,
                    route=route,
                    layout=(
                        product_profile.layout
                        if product_profile is not None
                        else composition.layout.layout_pattern
                    ),
                    components=page_components,
                    metadata={
                        "source": "product_profile",
                        "product": (
                            product_profile.name
                            if product_profile is not None
                            else application_name
                        ),
                    },
                )
            )

        # -----------------------------------------------------
        # 5. FeatureSpec → canonical UI models
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

                    feature_components.append(component)
                    components.append(component)

                pages.append(
                    UIPage(
                        name=page_name,
                        route=route,
                        layout=(
                            product_profile.layout
                            if product_profile is not None
                            else composition.layout.layout_pattern
                        ),
                        components=feature_components,
                        metadata={
                            "feature": feature.slug,
                        },
                    )
                )

        # -----------------------------------------------------
        # 6. Deduplicate
        # -----------------------------------------------------

        pages = self._dedupe_pages(pages)
        components = self._dedupe_components(
            components
        )

        # -----------------------------------------------------
        # 7. Canonical UISpec
        # -----------------------------------------------------

        design_system = composition.design_system

        if product_profile is not None:
            design_system.theme = (
                product_profile.theme
            )
            design_system.product_type = (
                product_profile.name
            )
            design_system.layout_style = (
                product_profile.layout
            )
            design_system.navigation_pattern = (
                product_profile.navigation
            )

        return UISpec(
            layout=(
                product_profile.layout
                if product_profile is not None
                else composition.layout.layout_pattern
            ),
            theme=(
                product_profile.theme
                if product_profile is not None
                else getattr(
                    design_system,
                    "theme",
                    "modern",
                )
            ),
            navigation=[
                (
                    product_profile.navigation
                    if product_profile is not None
                    else composition.layout.navigation
                )
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
                "product_profile":
                    (
                        product_profile.name
                        if product_profile is not None
                        else None
                    ),
            },
            page_models=pages,
            component_models=components,
            design_system=design_system,
        )
