from __future__ import annotations

from core.planner.models import Intent
from core.spec.models.feature_spec import FeatureSpec
from core.planner.capability_match import CapabilityMatch

from core.spec.ui_spec import UISpec
from core.spec.models.ui_page import UIPage
from core.spec.models.ui_component import UIComponent

from core.planner.design import (
    DesignComposer,
    DesignComposition
)

from core.planner.design.ui_blueprint_builder import (
    UIBlueprintBuilder
)


class UIPlanner:
    """
    Converts planner intelligence into
    frontend-consumable UISpec objects.

    Pipeline:

    Capability
        ↓
    FeatureSpec
        ↓
    DesignComposition
        ↓
    UIBlueprint
        ↓
    UISpec
    """

    def __init__(self):

        self.design_composer = DesignComposer()

        self.blueprint_builder = (
            UIBlueprintBuilder()
        )


    # ------------------------------------------------
    # Deduplication
    # ------------------------------------------------

    def _dedupe_pages(
        self,
        pages: list[UIPage]
    ) -> list[UIPage]:

        seen = set()

        result = []

        for page in pages:

            key = (
                page.route
                .lower()
                .strip()
            )

            if key not in seen:

                seen.add(key)

                result.append(page)

        return result



    def _dedupe_components(
        self,
        components: list[UIComponent]
    ) -> list[UIComponent]:

        seen = set()

        result = []


        for component in components:

            key = (
                component.name
                .lower()
                .strip()
            )


            if key not in seen:

                seen.add(key)

                result.append(component)


        return result



    # ------------------------------------------------
    # Main Planner
    # ------------------------------------------------

    def plan(
        self,
        *,
        intent: Intent,
        capabilities: list[CapabilityMatch],
        features: list[FeatureSpec] | None = None,
    ) -> UISpec:


        #
        # 1. Build design intelligence
        #

        application_name = (
            intent.project_name
            if hasattr(intent,"project_name")
            else "AI Application"
        )


        composition: DesignComposition = (
            self.design_composer.compose(
                application_name
            )
        )


        #
        # 2. Generate UI Blueprint
        #

        blueprint = (
            self.blueprint_builder.build(
                composition,
                application_name
            )
        )


        #
        # 3. Convert Blueprint → UISpec
        #

        pages = []


        components = []


        for page in blueprint.pages:


            ui_page = UIPage(
                name=page.name,
                route=(
                    "/"
                    if page.name == "Dashboard"
                    else
                    f"/{page.name.lower()}"
                ),
                layout=page.layout
            )


            pages.append(
                ui_page
            )



            for component_name in page.components:


                components.append(
                    UIComponent(
                        name=component_name,
                        component_type="generated"
                    )
                )



        pages = self._dedupe_pages(
            pages
        )


        components = self._dedupe_components(
            components
        )



        #
        # 4. Return Universal UI Spec
        #

        return UISpec(

            layout=(
                composition
                .layout
                .layout_pattern
            ),

            theme=(
                composition
                .design_system
                .theme
            ),

            navigation=[
                composition
                .layout
                .navigation
            ],

            metadata={

                "generated_by":
                    "X337 Design Intelligence",

                "application":
                    application_name

            },

            page_models=pages,

            component_models=components,

            design_system=(
                composition
                .design_system
            )

        )