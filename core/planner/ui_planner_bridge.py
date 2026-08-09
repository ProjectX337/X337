from __future__ import annotations

from core.planner.ui_blueprint import UIBlueprint
from core.spec.models.ui_page import UIPage
from core.spec.models.ui_component import UIComponent


class UIPlannerBridge:
    """
    Compatibility bridge for feature-driven UI planning.

    Produces the canonical UIPage model.
    """

    def build_from_features(
        self,
        feature_spec,
        design_composition,
        application_name,
    ):

        pages: list[UIPage] = []

        for page_name in feature_spec.pages:

            components = [
                UIComponent(
                    name=component_name,
                    component_type="feature",
                    metadata={
                        "feature": feature_spec.slug,
                    },
                )
                for component_name
                in feature_spec.components
            ]

            pages.append(
                UIPage(
                    name=page_name,
                    route=(
                        f"/{page_name.lower().replace(' ', '-')}"
                    ),
                    layout=(
                        design_composition
                        .layout
                        .layout_pattern
                    ),
                    components=components,
                    metadata={
                        "feature": feature_spec.slug,
                    },
                )
            )

        return UIBlueprint(
            application=application_name,
            pages=pages,
            theme={
                "mode": (
                    design_composition
                    .design_system
                    .theme
                ),
                "style": (
                    design_composition
                    .design_system
                    .visual_style
                ),
            },
        )
