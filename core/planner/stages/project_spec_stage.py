from __future__ import annotations

from core.planner.stages.base_stage import PlanningStage
from core.cognition.cognitive_state import CognitiveState
from core.spec.project_spec import ProjectSpec


class ProjectSpecStage(PlanningStage):

    name = "project_spec"

    requires = {
        "parsed",
        "intent",
        "capabilities",
        "feature_models",
        "technologies",
        "product_spec",
        "product_understanding",
        "application_graph",
    }

    provides = {
        "project_spec",
    }


    def run(
        self,
        context: CognitiveState,
    ) -> None:

        context.project_spec = ProjectSpec(

            name=context.parsed.project_name,

            parsed=context.parsed,

            intent=context.intent,

            architecture=getattr(
            context,
            "stack",
            context.stack,
        ),

            capabilities=context.capabilities,

            technologies=context.technologies,

        application_graph=context.application_graph,
        graph_intelligence=context.graph_intelligence,

            feature_models=context.feature_models,

            product_spec=context.product_spec,

            product_understanding=context.product_understanding,

            ui_spec=context.ui_spec,

            design_spec=context.design_spec,

    

        framework=(
            (
                context.stack.frontend
                or context.stack.backend
                or context.stack.ai
            )
            if context.stack is not None
            else ""
        ),

            metadata={
                "task_graph": getattr(
                    context,
                    "task_graph",
                    None,
                ),
            },

        )
