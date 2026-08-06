from __future__ import annotations

from core.planner.models import Intent
from core.planner.capability_match import CapabilityMatch

from core.spec.models.feature_spec import FeatureSpec
from core.spec.models.design_spec import DesignSpec
from core.knowledge.product_profile import ProductProfile
from core.graph.graph import Graph

from core.spec.ui_spec import UISpec
from core.spec.models.ui_page import UIPage
from core.spec.models.ui_component import UIComponent
from core.spec.models.design_system import DesignSystem


class UIPlanner:

    def _dedupe_components(
        self,
        components: list[UIComponent],
    ) -> list[UIComponent]:

        seen = {}

        result = []

        for component in components:

            if component.name not in seen:
                seen[component.name] = True
                result.append(component)

        return result

    """
    Converts planner outputs into a UISpec.
    """

    def plan(
        self,
        *,
        intent: Intent,
        capabilities: list[CapabilityMatch],
        features: list[FeatureSpec] | None = None,
        design: DesignSpec | None = None,
        product_profile: ProductProfile | None = None,
        graph=None,
    ) -> UISpec:

        if product_profile:

            layout = product_profile.layout
            theme = product_profile.theme

        elif design:

            layout = design.layout
            theme = design.theme

        else:

            layout = "default"
            theme = "modern"


        if product_profile and product_profile.default_pages:

            page_models = [
                UIPage(
                    name=page,
                    route="/" if page == "Landing" else f"/{page.lower()}",
                    layout=layout,
                )
                for page in product_profile.default_pages
            ]

        else:

            page_models = [
                UIPage(
                    name="Landing",
                    route="/",
                    layout=layout,
                )
            ]

        if product_profile and product_profile.default_components:

            component_models = [
                UIComponent(
                    name=component,
                    component_type="product",
                )
                for component in product_profile.default_components
            ]

        else:

            component_models = [
                UIComponent(
                    name="Navbar",
                    component_type="navigation",
                ),
                UIComponent(
                    name="Button",
                    component_type="button",
                ),
                UIComponent(
                    name="Card",
                    component_type="card",
                ),
            ]

    
    
        if graph:

            for node in graph.nodes.values():

                if node.kind == "page":

                    page_models.append(
                        UIPage(
                            name=node.label,
                            route=node.id.replace(":", "/"),
                            layout=layout,
                        )
                    )

                elif node.kind == "component":

                    component_models.append(
                        UIComponent(
                            name=node.label,
                            component_type="graph",
                        )
                    )


        component_models = self._dedupe_components(
            component_models
        )

        return UISpec(
            layout=layout,
            theme=theme,
            page_models=page_models,
            component_models=component_models,
            design_system=DesignSystem(
                colors={
                    "primary": (
                        design.primary_color
                        if design
                        else "cyan"
                    ),
                    "background": (
                        design.background
                        if design
                        else "dark"
                    ),
                },
                typography={
                    "style": (
                        design.typography
                        if design
                        else "modern"
                    ),
                },
                spacing={
                    "scale": "standard",
                },
            ),
        )
