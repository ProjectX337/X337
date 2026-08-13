from __future__ import annotations

from core.planner.models import Intent
from core.planner.capability_match import CapabilityMatch

from core.spec.models.feature_spec import FeatureSpec
from core.spec.models.ui_page import UIPage
from core.spec.models.ui_component import UIComponent
from core.spec.ui_spec import UISpec

from core.knowledge.product_profile import ProductProfile
from core.knowledge.product_profile_reasoner import ProductProfileReasoner

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
        UIPage / UIComponent
          ↓
        UISpec
    """

    def __init__(self) -> None:
        self.design_composer = DesignComposer()
        self.blueprint_builder = UIBlueprintBuilder()
        self.product_profile_reasoner = ProductProfileReasoner()

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
        by_name: dict[str, UIComponent] = {}

        for component in components:
            key = component.name.lower().strip()

            existing = by_name.get(key)

            if existing is None:
                by_name[key] = component
                continue

            # Merge canonical component intelligence instead of
            # discarding later declarations.
            if (
                existing.component_type != "feature"
                and component.component_type == "feature"
            ):
                existing.component_type = "feature"

            existing.metadata.update(
                {
                    key: value
                    for key, value in component.metadata.items()
                    if key not in {"features"}
                }
            )

            feature_names = set(
                existing.metadata.get("features", [])
            )

            feature_names.update(
                component.metadata.get("features", [])
            )

            if feature_names:
                existing.metadata["features"] = sorted(
                    feature_names
                )

        return list(by_name.values())

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

    def _page_components(
        self,
        *,
        page_name: str,
        product_profile: ProductProfile | None,
    ) -> list[str]:
        if product_profile is not None:
            page_components = getattr(
                product_profile,
                "page_components",
                {},
            )

            if page_name in page_components:
                return list(
                    page_components[page_name]
                )

            if product_profile.default_components:
                return list(
                    product_profile.default_components
                )

        return self._profile_components(
            product_profile
        )

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
        """
        Convert planner intelligence into the canonical UISpec.

        Ordering is intentional:

            ProductProfile
                  ↓
            canonical pages/components
                  ↓
            DesignComposition / Blueprint
                  ↓
            FeatureSpec
                  ↓
            deduplication
                  ↓
                UISpec

        ProductProfile owns product structure. The blueprint supplies
        design intelligence and is therefore not allowed to replace the
        application's root page.
        """

        intent = intent or Intent()
        features = features or []

        # -----------------------------------------------------
        # Resolve ProductProfile before any design composition.
        #
        # DesignComposer requires a canonical ProductProfile.
        # UIPlanner is responsible for resolving one when the
        # caller has not already supplied it.
        # -----------------------------------------------------

        if product_profile is None:
            product_profile = self.product_profile_reasoner.infer(
                intent=intent,
                capabilities=capabilities,
                features=features,
            )

        application_name = (
            getattr(intent, "project_name", None)
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
                product_profile=product_profile,
            )
        )

        # -----------------------------------------------------
        # 2. Build design blueprint
        #
        # The blueprint provides design/composition intelligence.
        # It does NOT own application page structure.
        # -----------------------------------------------------

        blueprint = self.blueprint_builder.build(
            composition,
            application_name,
        )

        pages: list[UIPage] = []
        components: list[UIComponent] = []

        # -----------------------------------------------------
        # 3. Establish canonical product pages first
        #
        # ProductProfile is authoritative.
        # Without a ProductProfile, the canonical default is:
        #
        #     Landing /
        #
        # This prevents a generic Dashboard blueprint from stealing
        # the root route.
        # -----------------------------------------------------

        profile_pages = self._profile_pages(product_profile)

        page_layout = (
            product_profile.layout
            if product_profile is not None
            else composition.layout.layout_pattern
        )

        product_name = (
            product_profile.name
            if product_profile is not None
            else application_name
        )

        # Build a canonical composition for EVERY canonical page.
        #
        # A UIPage is a self-contained frontend contract. Therefore
        # every canonical page must have a structural composition.
        #
        # Do not reuse the same mutable UILayoutNode instance across
        # pages. Each page receives its own composition tree.
        for index, page_name in enumerate(profile_pages):
            route = (
                "/"
                if index == 0
                else f"/{page_name.lower().replace(' ', '-')}"
            )

            page_components: list[UIComponent] = []

            profile_components = self._page_components(
                page_name=page_name,
                product_profile=product_profile,
            )

            for component_name in profile_components:
                component = UIComponent(
                    name=component_name,
                    component_type="product",
                    metadata={
                        "source": (
                            "product_profile"
                            if product_profile is not None
                            else "default_product"
                        ),
                        "product": product_name,
                        "page": page_name,
                        "features": [],
                    },
                )

                page_components.append(component)
                components.append(component)

            composition_tree = (
                self.blueprint_builder.build_composition(
                    composition,
                    page_name=page_name,
                    page_components=page_components,
                )
            )

            pages.append(
                UIPage(
                    name=page_name,
                    route=route,
                    layout=page_layout,
                    components=page_components,
                    composition=composition_tree,
                    metadata={
                        "source": (
                            "product_profile"
                            if product_profile is not None
                            else "default_product"
                        ),
                        "product": product_name,
                    },
                )
            )

        # -----------------------------------------------------
        # 4. Blueprint → canonical models
        #
        # Blueprint pages are supplemental. If a blueprint page
        # already targets a canonical product route, merge its
        # components into that page instead of creating a second
        # competing page.
        # -----------------------------------------------------

        # -----------------------------------------------------
        # Build route index for canonical pages.
        #
        # FeatureSpec pages merge into existing canonical UIPage
        # objects instead of creating duplicates.
        # -----------------------------------------------------

        pages_by_route = {
            page.route.lower().strip(): page
            for page in pages
        }

        # -----------------------------------------------------
        # 4. Blueprint integration removed
        #
        # UIPage is canonical.
        # UIBlueprintBuilder only supplies structural composition.
        # It does not create or merge application pages.
        # -----------------------------------------------------

        # -----------------------------------------------------
        # 5. FeatureSpec → canonical UI models
        # -----------------------------------------------------

        for feature in features:
            for index, page_name in enumerate(feature.pages):
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
                            "features": [feature.slug],
                        },
                    )

                    feature_components.append(component)
                    components.append(component)

                # -------------------------------------------------
                # Feature pages converge into the same canonical
                # UIPage contract as product-profile pages.
                #
                # A feature may target a page that already exists
                # (for example Billing, Dashboard, or Settings).
                # Merge into the existing canonical page rather than
                # creating a competing page.
                # -------------------------------------------------

                existing_page = pages_by_route.get(
                    route.lower().strip()
                )

                if existing_page is not None:
                    existing_names = {
                        component.name.lower().strip()
                        for component in existing_page.components
                    }

                    for component in feature_components:
                        component_key = component.name.lower().strip()

                        if component_key not in existing_names:
                            existing_page.components.append(component)
                            existing_names.add(component_key)

                    existing_page.metadata.setdefault(
                        "features",
                        [],
                    )

                    if feature.slug not in existing_page.metadata["features"]:
                        existing_page.metadata["features"].append(
                            feature.slug
                        )

                    # Existing canonical pages already have their
                    # own independent composition tree.
                    #
                    # Do not replace it with a generic feature tree.

                else:
                    # Feature-owned pages still require a complete
                    # canonical composition before generation.
                    feature_composition = (
                        self.blueprint_builder.build_composition(
                            composition,
                            page_name=page_name,
                            page_components=feature_components,
                        )
                    )

                    pages.append(
                        UIPage(
                            name=page_name,
                            route=route,
                            layout=page_layout,
                            components=feature_components,
                            composition=feature_composition,
                            metadata={
                                "feature": feature.slug,
                            },
                        )
                    )

                    pages_by_route[
                        route.lower().strip()
                    ] = pages[-1]

        # -----------------------------------------------------
        # 6. Materialize feature components independently
        # -----------------------------------------------------
        #
        # A feature can contain reusable components without owning
        # a page. Those components must still exist in the canonical
        # UISpec.
        #

        component_names = {
            component.name.lower().strip()
            for component in components
        }

        for feature in features:
            for component_name in feature.components:
                if component_name is None:
                    continue

                key = str(component_name).lower().strip()

                if key in component_names:
                    continue

                components.append(
                    UIComponent(
                        name=str(component_name),
                        component_type="feature",
                        metadata={
                            "features": [feature.slug],
                        },
                    )
                )

                component_names.add(key)

        # -----------------------------------------------------
        # 7. Deduplicate
        # -----------------------------------------------------

        pages = self._dedupe_pages(pages)
        components = self._dedupe_components(components)

        # -----------------------------------------------------
        # 8. Rebind page/layout components to canonical models
        # -----------------------------------------------------
        #
        # UIPage.components and UILayoutNode.component must reference
        # the same canonical UIComponent objects as UISpec.component_models.
        # This prevents ownership/import metadata from diverging between
        # page-level declarations and structural composition.
        #

        components_by_name = {
            component.name.lower().strip(): component
            for component in components
        }

        def rebind_layout(node):
            if node is None:
                return

            if node.component is not None:
                canonical = components_by_name.get(
                    node.component.name.lower().strip()
                )

                if canonical is not None:
                    node.component = canonical

            for child in node.children:
                rebind_layout(child)

        for page in pages:
            rebound_components = []

            for component in page.components:
                canonical = components_by_name.get(
                    component.name.lower().strip()
                )

                if canonical is not None:
                    rebound_components.append(canonical)

            page.components = rebound_components

            rebind_layout(page.composition)

        # -----------------------------------------------------
        # 9. Canonical design system
        # -----------------------------------------------------

        design_system = composition.design_system

        if product_profile is not None:
            design_system.theme = product_profile.theme
            design_system.product_type = product_profile.name
            design_system.layout_style = product_profile.layout
            design_system.navigation_pattern = product_profile.navigation

        # -----------------------------------------------------
        # 10. Canonical UISpec
        # -----------------------------------------------------

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
                "generated_by": "X337 Design Intelligence",
                "application": application_name,
                "capability_count": len(capabilities),
                "feature_count": len(features),
                "product_profile": (
                    product_profile.name
                    if product_profile is not None
                    else None
                ),
            },
            page_models=pages,
            component_models=components,
            design_system=design_system,
        )
