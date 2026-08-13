from __future__ import annotations

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
        *,
        page_name: str,
        page_components: list[UIComponent],
    ) -> UILayoutNode:
        """Build a page-specific canonical composition tree."""

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

        components_by_name = {
            component.name.lower().strip(): component
            for component in page_components
        }

        for section_name in composition.layout.structure:
            section = UILayoutNode(
                name=section_name,
                node_type="section",
            )

            section_key = section_name.lower().strip()

            matching_component = next(
                (
                    component
                    for name, component
                    in components_by_name.items()
                    if (
                        name in section_key
                        or section_key in name
                    )
                ),
                None,
            )

            if matching_component is not None:
                section.component = matching_component

            root.children.append(section)

        # If no semantic section matched a page component, retain
        # the component in a content section rather than dropping it.
        matched = {
            node.component.name.lower().strip()
            for node in root.children
            if node.component is not None
        }

        unmatched = [
            component
            for component in page_components
            if component.name.lower().strip()
            not in matched
        ]

        if unmatched:
            content = next(
                (
                    node
                    for node in root.children
                    if node.name.lower() == "content"
                ),
                None,
            )

            if content is None:
                content = UILayoutNode(
                    name="Content",
                    node_type="section",
                )
                root.children.append(content)

            for component in unmatched:
                content.children.append(
                    UILayoutNode(
                        name=component.name,
                        node_type="container",
                        component=component,
                    )
                )

        return root


    def build(
        self,
        composition,
        application_name: str,
    ) -> None:
        """
        Build the transitional blueprint.

        The blueprint itself does not own the composition tree.
        Composition belongs to canonical UIPage.composition and is
        attached by the UI planner when canonical pages are created.
        """

        composition_tree = self._build_composition(
            composition,
            page_name=application_name,
            page_components=[],
        )

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



    def build_composition(
        self,
        composition,
        *,
        page_name: str,
        page_components: list[UIComponent],
    ) -> UILayoutNode:
        """
        Build a page-specific canonical layout tree.

        UIPage owns the page components; this builder only arranges
        those canonical components into the design system's structure.
        """
        return self._build_composition(
            composition,
            page_name=page_name,
            page_components=page_components,
        )
