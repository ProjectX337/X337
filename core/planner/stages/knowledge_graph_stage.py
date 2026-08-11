from __future__ import annotations

from core.cognition.cognitive_state import CognitiveState
from core.planner.stages.base_stage import PlanningStage
from core.graph.models import NodeKind
from core.graph.models import (
    EdgeRelation,
    GraphEdge,
    GraphNode,
    NodeKind,
)


class KnowledgeGraphStage(PlanningStage):
    """
    Builds X337's semantic planning graph.

    During the graph migration this stage maintains two representations:

    1. ``task_graph`` / ``state.graph``
       Legacy compatibility graph used by existing X337 consumers.

    2. ``application_graph``
       Canonical application architecture graph used by the
       modern planning and generation pipeline.

    The canonical graph is the long-term source of truth.
    """

    requires = {
        "parsed",
        "intent",
        "capabilities",
        "feature_models",
    }

    provides = {
        "task_graph",
        "application_graph",
    }

    def run(
        self,
        state: CognitiveState,
    ) -> None:

        # ---------------------------------------------------------
        # Legacy graph
        # ---------------------------------------------------------

        graph = state.graph

        graph.add_node(
            "prompt",
            NodeKind.PROMPT,
            state.prompt,
        )

        graph.add_node(
            "intent",
            NodeKind.INTENT,
            "Intent",
        )

        graph.connect(
            "prompt",
            "intent",
            "classified_as",
        )

        for match in state.capabilities:

            capability = match.capability

            graph.add_node(
                capability.name,
                NodeKind.CAPABILITY,
                capability.name,
            )

            graph.connect(
                "intent",
                capability.name,
                "requires",
            )

        for feature in state.feature_models:

            feature_id = f"feature:{feature.slug}"

            graph.add_node(
                feature_id,
                NodeKind.FEATURE,
                feature.name,
            )

            source = feature.metadata.get(
                "source_capability"
            )

            if source:
                graph.connect(
                    source,
                    feature_id,
                    "provides",
                )

            for page in feature.pages:

                page_id = (
                    f"page:{feature.slug}:{page.lower()}"
                )

                graph.add_node(
                    page_id,
                    NodeKind.PAGE,
                    page,
                )

                graph.connect(
                    feature_id,
                    page_id,
                    "creates",
                )

            for component in feature.components:

                component_id = (
                    f"component:{feature.slug}:{component.lower()}"
                )

                graph.add_node(
                    component_id,
                    NodeKind.COMPONENT,
                    component,
                )

                graph.connect(
                    feature_id,
                    component_id,
                    "requires",
                )

        # ---------------------------------------------------------
        # Canonical application graph
        # ---------------------------------------------------------

        application = state.application_graph

        # Start fresh if the stage is ever rerun.
        application.nodes.clear()
        application.edges.clear()

        project_name = (
            state.parsed.project_name
            or state.prompt
            or "X337 Application"
        )

        product_id = "product"

        application.add_node(
            GraphNode(
                id=product_id,
                kind=NodeKind.PRODUCT,
                name=project_name,
                data={
                    "prompt": state.prompt,
                    "description": getattr(
                        state.parsed,
                        "description",
                        "",
                    ),
                },
            )
        )

        goal_id = "goal:primary"

        application.add_node(
            GraphNode(
                id=goal_id,
                kind=NodeKind.GOAL,
                name="Primary Product Goal",
                data={
                    "intent": getattr(
                        state.intent,
                        "description",
                        "",
                    ),
                },
            )
        )

        application.add_edge(
            GraphEdge(
                source=product_id,
                target=goal_id,
                relation=EdgeRelation.SUPPORTS,
            )
        )

        for feature in state.feature_models:

            feature_id = f"feature:{feature.slug}"

            application.add_node(
                GraphNode(
                    id=feature_id,
                    kind=NodeKind.FEATURE,
                    name=feature.name,
                    data={
                        "slug": feature.slug,
                        "description": getattr(
                            feature,
                            "description",
                            "",
                        ),
                        "metadata": getattr(
                            feature,
                            "metadata",
                            {},
                        ),
                    },
                )
            )

            application.add_edge(
                GraphEdge(
                    source=goal_id,
                    target=feature_id,
                    relation=EdgeRelation.REQUIRES,
                )
            )

            for page in feature.pages:

                page_id = (
                    f"page:{feature.slug}:{page.lower()}"
                )

                application.add_node(
                    GraphNode(
                        id=page_id,
                        kind=NodeKind.PAGE,
                        name=page,
                        data={
                            "feature": feature.slug,
                        },
                    )
                )

                application.add_edge(
                    GraphEdge(
                        source=feature_id,
                        target=page_id,
                        relation=EdgeRelation.CONTAINS,
                    )
                )

            for component in feature.components:

                component_id = (
                    f"component:{feature.slug}:{component.lower()}"
                )

                application.add_node(
                    GraphNode(
                        id=component_id,
                        kind=NodeKind.COMPONENT,
                        name=component,
                        data={
                            "feature": feature.slug,
                        },
                    )
                )

                application.add_edge(
                    GraphEdge(
                        source=feature_id,
                        target=component_id,
                        relation=EdgeRelation.CONTAINS,
                    )
                )
