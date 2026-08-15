from __future__ import annotations

from core.graph.models import ApplicationGraph
from core.graph.models import (
    GraphNode,
    GraphEdge,
    NodeKind,
    EdgeRelation,
)


class GraphBuilder:
    """
    Converts canonical UI models into an ApplicationGraph.

    The graph is a read-model of the application.
    It does not replace UISpec ownership.
    """

    def build(
        self,
        ui_spec,
        features=None,
    ) -> ApplicationGraph:
        """
        Materialize the canonical application architecture into
        an ApplicationGraph without losing source-model semantics.

        Ownership:

            Feature
                ├── Page
                ├── State
                └── API

            Page
                ├── Route
                └── Component instance

            Component instance
                └── State

        Component identity is page-scoped because the same component
        name may legitimately occur on multiple pages.
        """

        graph = ApplicationGraph()

        def slug(value: str) -> str:
            return (
                str(value)
                .strip()
                .lower()
                .replace(" ", "_")
                .replace("-", "_")
            )

        # ---------------------------------------------------------
        # FEATURES
        # ---------------------------------------------------------

        feature_map = {}

        if features:
            for feature in features:
                feature_id = (
                    f"feature.{feature.slug}"
                )

                feature_map[feature.name] = feature_id

                graph.add_node(
                    GraphNode(
                        id=feature_id,
                        kind=NodeKind.FEATURE,
                        name=feature.name,
                        data=(
                            feature.as_dict()
                            if hasattr(feature, "as_dict")
                            else {}
                        ),
                        metadata={
                            "description": (
                                feature.description
                            ),
                        },
                    )
                )

                # -------------------------------------------------
                # Feature state
                # -------------------------------------------------

                for state in feature.state:
                    state_id = (
                        f"{feature_id}.state.{slug(state)}"
                    )

                    graph.add_node(
                        GraphNode(
                            id=state_id,
                            kind=NodeKind.STATE,
                            name=state,
                            data={
                                "owner": feature.name,
                                "source": "feature",
                            },
                            metadata={
                                "owner": feature_id,
                            },
                        )
                    )

                    graph.add_edge(
                        GraphEdge(
                            source=feature_id,
                            target=state_id,
                            relation=EdgeRelation.CONTAINS,
                        )
                    )

                # -------------------------------------------------
                # Feature API contracts
                # -------------------------------------------------

                for api_contract in feature.api_contracts:
                    api_id = (
                        f"{feature_id}.api."
                        f"{slug(api_contract)}"
                    )

                    graph.add_node(
                        GraphNode(
                            id=api_id,
                            kind=NodeKind.API,
                            name=api_contract,
                            data={
                                "contract": api_contract,
                                "owner": feature.name,
                            },
                            metadata={
                                "owner": feature_id,
                            },
                        )
                    )

                    graph.add_edge(
                        GraphEdge(
                            source=feature_id,
                            target=api_id,
                            relation=EdgeRelation.PROVIDES,
                        )
                    )

        # ---------------------------------------------------------
        # PAGES
        # ---------------------------------------------------------

        for page in ui_spec.pages:

            page_id = (
                f"page.{slug(page.name)}"
            )

            page_node = GraphNode(
                id=page_id,
                kind=NodeKind.PAGE,
                name=page.name,
                data=(
                    page.as_dict()
                    if hasattr(page, "as_dict")
                    else {}
                ),
                metadata={
                    "route": page.route,
                    "layout": page.layout,
                },
            )

            graph.add_node(page_node)

            # -----------------------------------------------------
            # Feature -> Page
            # -----------------------------------------------------

            if features:
                for feature in features:
                    if page.name in feature.pages:
                        feature_id = (
                            f"feature.{feature.slug}"
                        )

                        graph.add_edge(
                            GraphEdge(
                                source=feature_id,
                                target=page_id,
                                relation=EdgeRelation.IMPLEMENTS,
                            )
                        )

            # -----------------------------------------------------
            # Page -> Route
            # -----------------------------------------------------

            route_id = (
                f"{page_id}.route"
            )

            graph.add_node(
                GraphNode(
                    id=route_id,
                    kind=NodeKind.ROUTE,
                    name=page.route,
                    data={
                        "route": page.route,
                        "page": page.name,
                    },
                    metadata={
                        "page": page_id,
                    },
                )
            )

            graph.add_edge(
                GraphEdge(
                    source=page_id,
                    target=route_id,
                    relation=EdgeRelation.NAVIGATES_TO,
                )
            )

            # -----------------------------------------------------
            # Page -> Component instances
            # -----------------------------------------------------

            for component in page.components:

                # IMPORTANT:
                # Component identity belongs to the page instance.
                component_id = (
                    f"{page_id}.component."
                    f"{slug(component.name)}"
                )

                graph.add_node(
                    GraphNode(
                        id=component_id,
                        kind=NodeKind.COMPONENT,
                        name=component.name,
                        data=(
                            component.as_dict()
                            if hasattr(component, "as_dict")
                            else {}
                        ),
                        metadata={
                            "type": (
                                component.component_type
                            ),
                            "page": page_id,
                        },
                    )
                )

                graph.add_edge(
                    GraphEdge(
                        source=page_id,
                        target=component_id,
                        relation=EdgeRelation.RENDERS,
                    )
                )

                # -------------------------------------------------
                # Component state
                # -------------------------------------------------

                for state in getattr(
                    component,
                    "states",
                    [],
                ):
                    state_id = (
                        f"{component_id}.state."
                        f"{slug(state)}"
                    )

                    graph.add_node(
                        GraphNode(
                            id=state_id,
                            kind=NodeKind.STATE,
                            name=state,
                            data={
                                "owner": component.name,
                                "source": "component",
                            },
                            metadata={
                                "owner": component_id,
                            },
                        )
                    )

                    graph.add_edge(
                        GraphEdge(
                            source=component_id,
                            target=state_id,
                            relation=EdgeRelation.CONTAINS,
                        )
                    )

        return graph


    def add_technologies(
        self,
        graph: ApplicationGraph,
        technologies,
    ) -> None:
        """
        Expand TechnologyPlan into canonical graph nodes.

        Technology decisions become part of the
        application architecture model.
        """

        if technologies is None:
            return

        for key, value in technologies.to_dict().items():

            if value is None:
                continue

            if key == "technologies":
                continue

            technology_id = (
                f"technology.{key.lower()}"
            )

            graph.add_node(
                GraphNode(
                    id=technology_id,
                    kind=NodeKind.TECHNOLOGY,
                    name=value,
                    metadata={
                        "category": key,
                        "source": "technology_plan",
                    },
                )
            )

    def add_capabilities(
        self,
        graph: ApplicationGraph,
        capabilities: list,
    ) -> None:
        """
        Expand product capabilities into
        application architecture nodes.
        """

        for capability in capabilities:

            capability_id = (
                f"capability."
                f"{capability.slug}"
            )

            graph.add_node(
                GraphNode(
                    id=capability_id,
                    kind=NodeKind.CAPABILITY,
                    name=capability.name,
                    metadata={
                        "description":
                            capability.description,
                    },
                )
            )

            for dependency in capability.depends_on:
                graph.add_edge(
                    GraphEdge(
                        source=capability_id,
                        target=f"capability.{dependency}",
                        relation=EdgeRelation.REQUIRES,
                    )
                )

            for feature in capability.feature_definitions:

                feature_id = (
                    f"feature.{feature['name'].lower().replace(' ','_')}"
                )

                graph.add_node(
                    GraphNode(
                        id=feature_id,
                        kind=NodeKind.FEATURE,
                        name=feature["name"],
                        metadata=feature,
                    )
                )

                graph.add_edge(
                    GraphEdge(
                        source=capability_id,
                        target=feature_id,
                        relation=EdgeRelation.IMPLEMENTS,
                    )
                )
