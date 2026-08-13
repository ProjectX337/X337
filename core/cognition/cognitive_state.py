from __future__ import annotations

from dataclasses import dataclass, field

from core.planner.models import ParsedPrompt, Intent
from core.planner.architecture_requirements import ArchitectureRequirements
from core.planner.capability_match import CapabilityMatch
from core.planner.architecture_selector import ArchitectureCandidate
from core.planner.stack_builder import ArchitectureStack
from core.planner.technology_plan import TechnologyPlan

from core.graph.graph import Graph
from core.graph.builder import GraphBuilder
from core.graph.models import ApplicationGraph
from core.graph.change_plan import ChangePlan


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
        task_graph
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

    capabilities: list[CapabilityMatch] = field(
        default_factory=list
    )

    feature_models: list = field(
        default_factory=list
    )

    product_profile = None

    # ---------------------------------------------------------
    # Design
    # ---------------------------------------------------------

    design_spec = None

    ui_spec = None

    # ---------------------------------------------------------
    # Final planning artifact
    # ---------------------------------------------------------

    project_spec = None

    # ---------------------------------------------------------
    # Semantic graph
    # ---------------------------------------------------------

    task_graph: Graph = field(
        default_factory=Graph
    )

    # Canonical application architecture graph.
    #
    # This is distinct from:
    #   task_graph: legacy planner compatibility graph
    #   execution_graph: execution / decision graph

    application_graph: ApplicationGraph = field(
        default_factory=ApplicationGraph
    )

    # Application evolution requests
    change_requests: list = field(
        default_factory=list
    )

    # Generated evolution plans
    change_plans: list[ChangePlan] = field(
        default_factory=list
    )


    graph: GraphBuilder = field(
        init=False
    )

    execution_graph: Graph = field(
        default_factory=Graph
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
        self.graph = GraphBuilder(
            self.task_graph
        )

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

    @property
    def knowledge_graph(self) -> Graph:
        """
        Backwards-compatible alias for task_graph.
        """
        return self.task_graph

    @knowledge_graph.setter
    def knowledge_graph(self, value: Graph) -> None:
        self.task_graph = value

    @property
    def decision_graph(self) -> Graph:
        """
        Backwards-compatible alias for execution_graph.
        """
        return self.execution_graph

    @decision_graph.setter
    def decision_graph(
        self,
        value: Graph,
    ) -> None:
        self.execution_graph = value
