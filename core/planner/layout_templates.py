from core.spec.models.ui_layout import UILayoutNode
from core.spec.models.ui_component import UIComponent


def create_landing_layout():

    return UILayoutNode(
        name="LandingPage",
        children=[

            UILayoutNode(
                name="Hero",
                children=[

                    UILayoutNode(
                        name="Badge",
                        component=UIComponent(
                            name="Badge"
                        )
                    ),

                    UILayoutNode(
                        name="Headline",
                        component=UIComponent(
                            name="Headline"
                        )
                    ),

                    UILayoutNode(
                        name="Subheadline",
                        component=UIComponent(
                            name="Subheadline"
                        )
                    ),

                    UILayoutNode(
                        name="CTA",
                        component=UIComponent(
                            name="MagneticButton"
                        )
                    ),

                    UILayoutNode(
                        name="DashboardPreview",
                        component=UIComponent(
                            name="DashboardPreview"
                        )
                    ),

                ]
            ),

            UILayoutNode(
                name="FeatureGrid",
                component=UIComponent(
                    name="FeatureGrid"
                )
            ),

            UILayoutNode(
                name="PricingSection",
                component=UIComponent(
                    name="PricingSection"
                )
            ),

        ]
    )
