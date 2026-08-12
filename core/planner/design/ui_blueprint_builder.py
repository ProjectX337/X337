from __future__ import annotations

from core.planner.ui_blueprint import UIBlueprint
from core.spec.models.ui_component import UIComponent
from core.spec.models.ui_layout import UILayoutNode


class UIBlueprintBuilder:
    """
    Converts design intelligence into a planner-level UI blueprint.

    Design composition is attached to canonical UIPage objects.
    UIBlueprint remains a transitional transport object containing
    application identity, pages, and theme only.

    The builder owns design/composition intelligence.
    It does not own application page identity or routes.
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
        """
        Build the transitional blueprint.

        The blueprint itself does not own the composition tree.
        Composition belongs to canonical UIPage.composition and is
        attached by the UI planner when canonical pages are created.
        """

        composition_tree = self._build_composition(composition)

        pages = []

        # The design system does not define application page identity.
        # UIPlanner owns that responsibility.
        #
        # We intentionally do not manufacture a page here.
        # The composition tree is returned through the blueprint's
        # canonical page construction path in UIPlanner.
        #
        # Store the composition temporarily in page metadata is NOT
        # appropriate because UILayoutNode is a first-class structural
        # model. The UIPlanner attaches it directly to UIPage.

        blueprint = UIBlueprint(
            application=application_name,
            pages=pages,
            theme={
                "mode": composition.design_system.theme,
                "style": composition.design_system.visual_style,
            },
        )

        # Transitional transport attribute is intentionally avoided.
        #
        # The composition tree is exposed through a private builder
        # result consumed by UIPlanner via build_composition().
        return blueprint

    def build_composition(
        self,
        composition,
    ) -> UILayoutNode:
        """
        Build the canonical layout/composition tree.

        This is intentionally separate from UIBlueprint because
        composition belongs to UIPage, not UIBlueprint.
        """
        return self._build_composition(composition)
