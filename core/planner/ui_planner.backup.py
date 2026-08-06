from __future__ import annotations

from core.planner.models import Intent
from core.planner.capability_match import CapabilityMatch
from core.spec.models.feature_spec import FeatureSpec

from core.spec.ui_spec import UISpec
from core.spec.models.ui_page import UIPage
from core.spec.models.ui_component import UIComponent
from core.spec.models.ui_layout import UILayoutNode
from core.spec.models.design_system import DesignSystem


class UIPlanner:
    """
    Converts project intent into a UI blueprint.
    """

    def plan(
        self,
        *,
        intent: Intent,
        capabilities: list[CapabilityMatch],
        features: list[FeatureSpec] | None = None,
    ) -> UISpec:

        page_models = [
            UIPage(
                name="Landing",
                route="/",
                layout="default",
            )
        ]

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

        layout = "default"

        # ---------------------------------------------------------
        # Feature-driven UI generation
        # ---------------------------------------------------------

        if features:

            for feature in features:

                for page in feature.pages:

                    page_models.append(
                        UIPage(
                            name=page,
                            route=f"/{feature.slug}/{page.lower()}",
                            layout="default",
                        )
                    )

                for component in feature.components:

                    component_models.append(
                        UIComponent(
                            name=component,
                            component_type="feature",
                        )
                    )

        capability_names = [
            match.capability.name
            for match in capabilities
        ]

    


        return UISpec(
            layout=layout,
            theme="modern",
            page_models=page_models,
            component_models=component_models,
            design_system=DesignSystem(
                colors={
                    "primary": "cyan",
                    "background": "dark",
                },
                typography={
                    "style": "modern",
                },
                spacing={
                    "scale": "standard",
                },
            ),
        )
