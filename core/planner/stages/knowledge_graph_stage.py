from __future__ import annotations

from core.cognition.cognitive_state import CognitiveState
from core.planner.stages.base_stage import PlanningStage
from core.graph.graph_types import GraphNodeType


class KnowledgeGraphStage(PlanningStage):
    """
    Builds the semantic planning graph.
    """

    requires = {
        "parsed",
        "intent",
        "capabilities",
        "feature_models",
    }

    provides = {
        "task_graph",
    }

    def run(
        self,
        state: CognitiveState,
    ) -> None:

        graph = state.graph

        graph.add_node(
            "prompt",
            GraphNodeType.PROMPT,
            state.prompt,
        )

        graph.add_node(
            "intent",
            GraphNodeType.INTENT,
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
                GraphNodeType.CAPABILITY,
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
                GraphNodeType.FEATURE,
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
                    GraphNodeType.PAGE,
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
                    GraphNodeType.COMPONENT,
                    component,
                )

                graph.connect(
                    feature_id,
                    component_id,
                    "requires",
                )
