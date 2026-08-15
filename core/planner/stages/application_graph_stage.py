from __future__ import annotations

from core.planner.stages.base_stage import PlanningStage
from core.cognition.cognitive_state import CognitiveState
from core.graph.graph_builder import GraphBuilder
from core.graph.normalization.graph_normalizer import GraphNormalizer
from core.graph.normalization.capability_normalizer import CapabilityNormalizer


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
        "capability_models",
        "technologies",
    }

    provides = {
        "application_graph",
    }

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

        normalized_capabilities = (
            CapabilityNormalizer()
            .normalize(
                state.capability_models
            )
        )

        builder.add_capabilities(
            state.application_graph,
            normalized_capabilities,
        )

        builder.add_technologies(
            state.application_graph,
            state.technologies,
        )

        state.application_graph = (
            GraphNormalizer()
            .normalize(
                state.application_graph
            )
        )
