from __future__ import annotations

from core.planner.stages.base_stage import PlanningStage
from core.cognition.cognitive_state import CognitiveState
from core.graph.graph_builder import GraphBuilder


class ApplicationGraphStage(PlanningStage):
    """
    Builds the canonical ApplicationGraph.

    ApplicationGraph is a derived intelligence model.
    UISpec and FeatureSpec remain the source domains.
    """

    name = "application_graph"

    requires = {
        "ui_spec",
        "feature_models",
    }

    provides = set()

    def run(
        self,
        state: CognitiveState,
    ) -> None:

        builder = GraphBuilder()

        state.application_graph = (
            builder.build(
                state.ui_spec,
                state.feature_models,
            )
        )

        builder.add_capabilities(
            state.application_graph,
            state.capability_models,
        )
