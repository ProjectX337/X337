from __future__ import annotations

from core.planner.models import Intent
from core.planner.capability_match import CapabilityMatch

from core.spec.ui_spec import UISpec
from core.spec.models.ui_page import UIPage
from core.spec.models.ui_component import UIComponent
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

        capability_names = [
            capability.name
            for capability in capabilities
        ]

        if "authentication" in capability_names:

            page_models.append(
                UIPage(
                    name="Login",
                    route="/login",
                    layout="default",
                )
            )

        if (
            intent
            and getattr(intent, "category", None) == "saas"
        ):

            page_models.append(
                UIPage(
                    name="Dashboard",
                    route="/dashboard",
                    layout="dashboard",
                    components=[
                        UIComponent(
                            name="Sidebar",
                            component_type="navigation",
                        ),
                        UIComponent(
                            name="DataCard",
                            component_type="data",
                        ),
                    ],
                )
            )

            component_models.extend(
                [
                    UIComponent(
                        name="Sidebar",
                        component_type="navigation",
                    ),
                    UIComponent(
                        name="DataCard",
                        component_type="data",
                    ),
                ]
            )

            layout = "dashboard"

        design_system = DesignSystem(
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
        )

        return UISpec(
            layout=layout,
            theme="modern",
            page_models=page_models,
            component_models=component_models,
            design_system=design_system,
        )
