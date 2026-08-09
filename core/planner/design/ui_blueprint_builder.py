from __future__ import annotations

from core.planner.ui_blueprint import UIBlueprint
from core.spec.models.ui_page import UIPage
from core.spec.models.ui_component import UIComponent
from core.spec.models.ui_layout import UILayoutNode


class UIBlueprintBuilder:
    """
    Converts design intelligence into the canonical UI model.

    The builder is intentionally responsible for creating the
    structural UI composition. It does not generate React code.
    """

    def _build_composition(
        self,
        composition,
    ) -> UILayoutNode:

        root = UILayoutNode(
            name="ApplicationShell",
            node_type="container",
            props={
                "layout": composition.layout.layout_pattern,
                "responsive": composition.layout.responsive_behavior,
                "density": composition.layout.density,
                "navigation": composition.layout.navigation,
            },
        )

        for section_name in composition.layout.structure:

            section = UILayoutNode(
                name=section_name,
                node_type="section",
            )

            matching_component = next(
                (
                    component_name
                    for component_name
                    in composition.components.components
                    if component_name.lower()
                    in section_name.lower()
                    or section_name.lower()
                    in component_name.lower()
                ),
                None,
            )

            if matching_component:
                section.component = UIComponent(
                    name=matching_component,
                    component_type="generated",
                    metadata={
                        "source": "design_intelligence",
                        "section": section_name,
                    },
                )

            root.children.append(section)

        return root

    def build(
        self,
        composition,
        application_name: str,
    ) -> UIBlueprint:

        composition_tree = self._build_composition(
            composition
        )

        components = [
            UIComponent(
                name=component_name,
                component_type="generated",
                metadata={
                    "source": "design_intelligence",
                },
            )
            for component_name
            in composition.components.components
        ]

        page = UIPage(
            name="Dashboard",
            route="/",
            layout=composition.layout.layout_pattern,
            components=components,
            composition=composition_tree,
            metadata={
                "page_type": composition.layout.page_type,
                "layout_pattern": composition.layout.layout_pattern,
                "responsive_behavior": (
                    composition.layout.responsive_behavior
                ),
                "density": composition.layout.density,
                "navigation": composition.layout.navigation,
            },
        )

        return UIBlueprint(
            application=application_name,
            pages=[
                page
            ],
            theme={
                "mode": composition.design_system.theme,
                "style": composition.design_system.visual_style,
            },
        )
