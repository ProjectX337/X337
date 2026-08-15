from __future__ import annotations

from dataclasses import dataclass, field

from core.planner.models import ParsedPrompt, Intent
from core.planner.architecture_requirements import ArchitectureRequirements
from core.planner.capability_match import CapabilityMatch
from core.planner.architecture_selector import ArchitectureCandidate
from core.planner.stack_builder import ArchitectureStack
from core.planner.technology_plan import TechnologyPlan

from core.graph.models import ApplicationGraph
from core.graph.change_plan import ChangePlan
from core.graph.evolution.models import EvolutionPlan
from core.intelligence.models import (
    ProductIntent,
    ProductUnderstanding,
)

from core.knowledge.product_profile import ProductProfile
from core.spec.models.design_spec import DesignSpec
from core.spec.ui_spec import UISpec
from core.spec.project_spec import ProjectSpec


@dataclass
class CognitiveState:
    """
    Canonical shared state for X337 planning.

    The state is the execution context passed through every
    planning stage.

    Canonical fields correspond directly to stage contracts:

        prompt
        parsed
        intent
        architecture_candidates
        stack
        capabilities
        feature_models
        application_graph
        technologies
        product_profile
        design_spec
        ui_spec
        project_spec
    """

    # ---------------------------------------------------------
    # Input
    # ---------------------------------------------------------

    prompt: str

    # ---------------------------------------------------------
    # Cognition
    # ---------------------------------------------------------

    parsed: ParsedPrompt = field(
        default_factory=lambda: ParsedPrompt("")
    )

    intent: Intent = field(
        default_factory=Intent
    )

    # Canonical product understanding.
    # Replaces keyword-only intent reasoning over time.
    product_intent: ProductIntent | None = None

    # Synthesized product understanding.
    # Derived from product intent reasoning.
    product_understanding: ProductUnderstanding | None = None

    # Generated product specification.
    product_spec: object | None = None


    # Intelligence-derived capability hypotheses.
    # Produced before concrete capability matching.
    capability_hypotheses: list = field(
        default_factory=list
    )

    # Resolved implementation-ready capabilities.
    #
    # Produced by CapabilityResolutionStage and consumed
    # by ResolvedCapabilityAdapterStage.
    resolved_capabilities: list = field(
        default_factory=list
    )

    # ---------------------------------------------------------
    # Architecture
    # ---------------------------------------------------------

    architecture_requirements: ArchitectureRequirements | None = None

    architecture_candidates: list[ArchitectureCandidate] = field(
        default_factory=list
    )

    stack: ArchitectureStack | None = None

    technologies: TechnologyPlan = field(
        default_factory=TechnologyPlan
    )

    # ---------------------------------------------------------
    # Product planning
    # ---------------------------------------------------------

    # Semantic capability candidates produced by intelligence layer.

    capabilities: list[CapabilityMatch] = field(
        default_factory=list
    )

    # Intelligence-selected product capabilities.
    # Used for ApplicationGraph synthesis.
    capability_models: list = field(
        default_factory=list
    )

    feature_models: list = field(
        default_factory=list
    )

    product_profile: ProductProfile | None = None

    # ---------------------------------------------------------
    # Design
    # ---------------------------------------------------------

    design_spec: DesignSpec | None = None

    ui_spec: UISpec | None = None

    # ---------------------------------------------------------
    # Final planning artifact
    # ---------------------------------------------------------

    project_spec: ProjectSpec | None = None

    # ---------------------------------------------------------
    # Semantic graph
    # ---------------------------------------------------------

    # Canonical application architecture graph.
    #
    # This is the authoritative graph representation of the
    # product/application being planned and evolved.
    application_graph: ApplicationGraph = field(
        default_factory=ApplicationGraph
    )

    # Graph intelligence derived from the canonical
    # application architecture graph.
    graph_intelligence: dict | None = None

    # Architecture evolution intelligence output.
    #
    # Represents recommended changes after graph analysis.
    evolution_plan: EvolutionPlan | None = None

    # Application evolution requests.
    change_requests: list = field(
        default_factory=list
    )

    # Generated evolution plans.
    change_plans: list[ChangePlan] = field(
        default_factory=list
    )

    # ---------------------------------------------------------
    # Reasoning / memory
    # ---------------------------------------------------------

    reasoning_trace: list = field(
        default_factory=list
    )

    memory: dict = field(
        default_factory=dict
    )

    metadata: dict = field(
        default_factory=dict
    )

    # ---------------------------------------------------------
    # Initialization
    # ---------------------------------------------------------

    def __post_init__(self) -> None:
        """
        Initialize canonical runtime state.
        """
        pass

    # ---------------------------------------------------------
    # Compatibility aliases
    # ---------------------------------------------------------

    @property
    def parsed_prompt(self) -> ParsedPrompt:
        """
        Backwards-compatible alias for parsed.
        """
        return self.parsed

    @parsed_prompt.setter
    def parsed_prompt(
        self,
        value: ParsedPrompt,
    ) -> None:
        self.parsed = value

    @property
    def features(self) -> list:
        """
        Backwards-compatible alias for feature_models.
        """
        return self.feature_models

    @features.setter
    def features(self, value: list) -> None:
        self.feature_models = value
