from __future__ import annotations

from dataclasses import dataclass, field

from core.planner.models import (
    ParsedPrompt,
    Intent,
)

from core.graph.graph import Graph
from core.graph.builder import GraphBuilder


@dataclass
class CognitiveState:
    """
    Global state shared by every planner,
    reasoner and execution stage.
    """

    prompt: str

    parsed_prompt: ParsedPrompt = field(default_factory=lambda: ParsedPrompt(""))
    intent: Intent = field(default_factory=Intent)

    capabilities: list = field(default_factory=list)
    feature_models: list = field(default_factory=list)

    product_profile = None
    ui_spec = None
    project_spec = None

    reasoning_trace: list = field(default_factory=list)

    task_graph: Graph = field(default_factory=Graph)

    graph: GraphBuilder = field(init=False)
    execution_graph: Graph = field(default_factory=Graph)

    memory: dict = field(default_factory=dict)
    metadata: dict = field(default_factory=dict)

    def __post_init__(self):
        self.graph = GraphBuilder(
            self.task_graph
        )

    # -----------------------------
    # Backwards compatibility
    # -----------------------------

    @property
    def parsed(self):
        return self.parsed_prompt

    @parsed.setter
    def parsed(self, value):
        self.parsed_prompt = value

    @property
    def features(self):
        return self.feature_models

    @features.setter
    def features(self, value):
        self.feature_models = value


    @property
    def knowledge_graph(self):
        return self.task_graph

    @knowledge_graph.setter
    def knowledge_graph(self, value):
        self.task_graph = value


    @property
    def decision_graph(self):
        return self.execution_graph

    @decision_graph.setter
    def decision_graph(self, value):
        self.execution_graph = value
