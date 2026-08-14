from __future__ import annotations
from core.planner.stages.knowledge_graph_stage import KnowledgeGraphStage
from core.planner.stages.technology_resolver_stage import TechnologyResolverStage
from core.cognition.cognitive_state import CognitiveState

from core.planner.planning_pipeline import PlanningPipeline

from core.planner.stages.prompt_parser_stage import PromptParserStage
from core.planner.stages.intent_classifier_stage import IntentClassifierStage
from core.planner.stages.product_intent_stage import ProductIntentStage
from core.planner.stages.capability_resolution_stage import CapabilityResolutionStage
from core.planner.stages.capability_reasoner_stage import CapabilityReasonerStage
from core.planner.stages.resolved_capability_adapter_stage import ResolvedCapabilityAdapterStage
from core.planner.stages.product_intelligence_stage import ProductIntelligenceStage
from core.planner.stages.architecture_selection_stage import ArchitectureSelectionStage
from core.planner.stages.stack_builder_stage import StackBuilderStage
from core.planner.stages.architecture_requirements_stage import ArchitectureRequirementsStage
from core.planner.stages.feature_stage import FeatureStage
from core.planner.stages.product_profile_stage import ProductProfileStage
from core.planner.stages.design_inference_stage import DesignInferenceStage
from core.planner.stages.ui_spec_stage import UISpecStage
from core.planner.stages.application_graph_stage import ApplicationGraphStage
from core.planner.stages.graph_intelligence_stage import GraphIntelligenceStage
from core.planner.stages.change_request_stage import ChangeRequestStage
from core.planner.stages.change_planning_stage import ChangePlanningStage
from core.planner.stages.project_spec_stage import ProjectSpecStage


class ProjectPlanner:
    """
    Converts a user prompt into a ProjectSpec using the CognitiveState.
    """

    def __init__(self):

        self.pipeline = PlanningPipeline(
            [
            PromptParserStage(),
            IntentClassifierStage(),
            ProductIntentStage(),
            ProductIntelligenceStage(),
            CapabilityReasonerStage(),
            CapabilityResolutionStage(),
            ResolvedCapabilityAdapterStage(),
            ArchitectureRequirementsStage(),
            ArchitectureSelectionStage(),
            StackBuilderStage(),
            FeatureStage(),
            KnowledgeGraphStage(),
            TechnologyResolverStage(),
            ProductProfileStage(),
            DesignInferenceStage(),
            UISpecStage(),
            ApplicationGraphStage(),
            GraphIntelligenceStage(),
            ChangeRequestStage(),
            ChangePlanningStage(),
            ProjectSpecStage(),
        ]
        )

    def plan_with_state(
        self,
        message: str,
    ) -> CognitiveState:
        """
        Execute planning and return the full cognitive state.

        Used for introspection, evolution planning,
        debugging, and agent coordination.
        """

        state = CognitiveState(
            prompt=message
        )

        self.pipeline.run(state)

        return state


    def plan(
        self,
        message: str,
    ):

        state = self.plan_with_state(
            message
        )

        return state.project_spec
