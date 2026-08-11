from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class NodeKind(str, Enum):
    """
    Canonical graph node categories used by X337.

    Application nodes describe the product being built.
    Planning/execution nodes are retained here temporarily
    so the graph migration can happen incrementally.
    """

    # Product / application architecture
    PRODUCT = "product"
    PROJECT = "project"
    USER = "user"
    GOAL = "goal"
    WORKFLOW = "workflow"
    FEATURE = "feature"
    PAGE = "page"
    COMPONENT = "component"
    STATE = "state"
    ACTION = "action"
    API = "api"
    DATA = "data"
    DATABASE = "database"
    SOURCE_FILE = "source_file"
    FILE = "file"
    ROUTE = "route"
    TECHNOLOGY = "technology"
    DESIGN = "design"

    # Planning / execution compatibility
    PROMPT = "prompt"
    INTENT = "intent"
    CAPABILITY = "capability"
    TASK = "task"
    DECISION = "decision"
    OBSERVATION = "observation"
    AGENT = "agent"
    TEST = "test"
    EVIDENCE = "evidence"


class EdgeRelation(str, Enum):
    """
    Canonical relationship vocabulary.
    """

    REQUIRES = "requires"
    IMPLEMENTS = "implements"
    RENDERS = "renders"
    CONTAINS = "contains"
    DEPENDS_ON = "depends_on"
    MUTATES = "mutates"
    READS = "reads"
    WRITES = "writes"
    NAVIGATES_TO = "navigates_to"
    TRIGGERS = "triggers"
    SUPPORTS = "supports"
    CLASSIFIED_AS = "classified_as"
    PROVIDES = "provides"
    CREATES = "creates"
    WEIGHS = "weighs"


@dataclass(slots=True, init=False)
class GraphNode:
    """
    Canonical X337 graph node.

    `name` is the canonical human-readable identifier.

    `label` remains available as a compatibility alias for
    older graph consumers.
    """

    id: str
    kind: NodeKind | str
    name: str
    data: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def __init__(
        self,
        id: str,
        kind: NodeKind | str,
        name: str | None = None,
        data: dict[str, Any] | None = None,
        metadata: dict[str, Any] | None = None,
        *,
        label: str | None = None,
    ) -> None:
        if name is None:
            name = label

        if name is None:
            raise TypeError(
                "GraphNode requires either 'name' or legacy 'label'."
            )

        self.id = id
        self.kind = kind
        self.name = name
        self.data = {} if data is None else data
        self.metadata = {} if metadata is None else metadata

    @property
    def label(self) -> str:
        """
        Backwards-compatible alias for legacy GraphNode.label.
        """
        return self.name

    @label.setter
    def label(self, value: str) -> None:
        self.name = value

    def as_dict(self) -> dict[str, Any]:
        kind = (
            self.kind.value
            if isinstance(self.kind, Enum)
            else self.kind
        )

        return {
            "id": self.id,
            "kind": kind,
            "name": self.name,
            "data": self.data,
            "metadata": self.metadata,
        }

    def to_dict(self) -> dict[str, Any]:
        return self.as_dict()


@dataclass(slots=True, init=False)
class GraphEdge:
    """
    Canonical directed graph relationship.
    """

    source: str
    target: str
    relation: EdgeRelation | str
    metadata: dict[str, Any] = field(default_factory=dict)

    def __init__(
        self,
        source: str,
        target: str,
        relation: EdgeRelation | str,
        metadata: dict[str, Any] | None = None,
        *,
        weight: float = 1.0,
    ) -> None:
        self.source = source
        self.target = target
        self.relation = relation
        self.metadata = {} if metadata is None else metadata

        if weight != 1.0:
            self.metadata["weight"] = weight

    @property
    def weight(self) -> float:
        """
        Compatibility accessor for legacy decision graphs.
        """
        value = self.metadata.get("weight", 1.0)

        try:
            return float(value)
        except (TypeError, ValueError):
            return 1.0

    @weight.setter
    def weight(self, value: float) -> None:
        self.metadata["weight"] = value

    def as_dict(self) -> dict[str, Any]:
        relation = (
            self.relation.value
            if isinstance(self.relation, Enum)
            else self.relation
        )

        return {
            "source": self.source,
            "target": self.target,
            "relation": relation,
            "metadata": self.metadata,
        }

    def to_dict(self) -> dict[str, Any]:
        return self.as_dict()


@dataclass
class ApplicationGraph:
    """
    Canonical application architecture graph.

    This graph describes the structure and behavior of the
    generated application.

    It is intentionally separate from execution/decision state.
    """

    nodes: dict[str, GraphNode] = field(default_factory=dict)
    edges: list[GraphEdge] = field(default_factory=list)

    def add_node(self, node: GraphNode) -> None:
        self.nodes[node.id] = node

    def add_edge(self, edge: GraphEdge) -> None:
        self.edges.append(edge)

    def has_node(self, node_id: str) -> bool:
        return node_id in self.nodes

    def get(self, node_id: str) -> GraphNode:
        return self.nodes[node_id]

    def remove_node(self, node_id: str) -> None:
        if node_id not in self.nodes:
            return

        del self.nodes[node_id]

        self.edges = [
            edge
            for edge in self.edges
            if edge.source != node_id
            and edge.target != node_id
        ]

    def find_by_kind(
        self,
        kind: NodeKind | str,
    ) -> list[GraphNode]:
        return [
            node
            for node in self.nodes.values()
            if node.kind == kind
        ]

    def find_by_label(
        self,
        label: str,
    ) -> list[GraphNode]:
        return [
            node
            for node in self.nodes.values()
            if node.name == label
        ]

    def outgoing(
        self,
        node_id: str,
        relation: EdgeRelation | str | None = None,
    ) -> list[GraphEdge]:
        return [
            edge
            for edge in self.edges
            if edge.source == node_id
            and (
                relation is None
                or edge.relation == relation
            )
        ]

    def incoming(
        self,
        node_id: str,
        relation: EdgeRelation | str | None = None,
    ) -> list[GraphEdge]:
        return [
            edge
            for edge in self.edges
            if edge.target == node_id
            and (
                relation is None
                or edge.relation == relation
            )
        ]

    def neighbors(
        self,
        node_id: str,
    ) -> list[GraphNode]:
        return [
            self.nodes[edge.target]
            for edge in self.outgoing(node_id)
            if edge.target in self.nodes
        ]

    def children(
        self,
        node_id: str,
        relation: EdgeRelation | str | None = None,
    ) -> list[GraphNode]:
        return [
            self.nodes[edge.target]
            for edge in self.outgoing(
                node_id,
                relation,
            )
            if edge.target in self.nodes
        ]

    def parents(
        self,
        node_id: str,
        relation: EdgeRelation | str | None = None,
    ) -> list[GraphNode]:
        return [
            self.nodes[edge.source]
            for edge in self.incoming(
                node_id,
                relation,
            )
            if edge.source in self.nodes
        ]

    def as_dict(self) -> dict[str, Any]:
        return {
            "nodes": {
                node_id: node.as_dict()
                for node_id, node in self.nodes.items()
            },
            "edges": [
                edge.as_dict()
                for edge in self.edges
            ],
        }

    def to_dict(self) -> dict[str, Any]:
        return self.as_dict()
