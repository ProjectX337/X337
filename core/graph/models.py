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


    # ---------------------------------------------------------
    # Legacy compatibility API
    # ---------------------------------------------------------

    @property
    def node_type(self):
        """
        Backwards-compatible alias.

        Canonical field is `kind`.
        """
        return self.kind

    @node_type.setter
    def node_type(self, value):
        self.kind = value

    """
    Canonical X337 graph node.

    `name` is the canonical human-readable identifier.

    `label` remains available as a compatibility alias for
    older graph consumers.
    """

    id: str
    type: NodeKind | str
    kind: NodeKind | str
    name: str
    data: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def relation(self):
        return self.type

    @relation.setter
    def relation(self, value):
        self.type = value

    def __init__(
        self,
        id: str,
        type: NodeKind | str = None,
        name: str | None = None,
        data: dict[str, Any] | None = None,
        metadata: dict[str, Any] | None = None,
        *,
        kind: NodeKind | str = None,
        label: str | None = None,
    ) -> None:

        if type is None:
            type = kind

        if name is None:
            name = label

        if type is None:
            raise TypeError(
                "GraphNode requires 'type' or 'kind'."
            )

        if name is None:
            raise TypeError(
                "GraphNode requires 'name' or 'label'."
            )

        self.id = id
        self.kind = type
        self.type = type
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
    type: EdgeRelation | str
    relation: EdgeRelation | str
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def relation(self):
        return self.type

    @relation.setter
    def relation(self, value):
        self.type = value

    def __init__(
        self,
        source: str,
        target: str,
        type: EdgeRelation | str | None = None,
        metadata: dict[str, Any] | None = None,
        *,
        relation: EdgeRelation | str | None = None,
        weight: float = 1.0,
    ) -> None:

        if type is None:
            type = relation

        if type is None:
            raise TypeError(
                "GraphEdge requires 'type' or 'relation'."
            )

        self.source = source
        self.target = target
        self.type = type
        self.relation = type
        self.metadata = {} if metadata is None else metadata

        if weight != 1.0:
            self.metadata["weight"] = weight


    @property
    def edge_type(self):
        """
        Backwards-compatible alias for legacy graph consumers.

        Canonical field is `relation`.
        """
        return self.relation

    @edge_type.setter
    def edge_type(self, value):
        self.relation = value

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
    Canonical X337 application architecture graph.

    Represents product structure:
    Product -> Features -> Pages -> Components
    plus backend/runtime architecture nodes.
    """

    nodes: dict[str, GraphNode] = field(
        default_factory=dict
    )

    edges: list[GraphEdge] = field(
        default_factory=list
    )


    def add_node(
        self,
        node: GraphNode,
    ) -> None:
        self.nodes[node.id] = node


    def add_edge(
        self,
        edge: GraphEdge,
    ) -> None:
        self.edges.append(edge)


    def get_node(
        self,
        node_id: str,
    ):
        return self.nodes.get(node_id)


    def get(
        self,
        node_id: str,
    ):
        return self.nodes.get(node_id)


    def has_node(
        self,
        node_id: str,
    ) -> bool:
        return node_id in self.nodes


    def get_nodes(self):
        return self.nodes


    def get_edges(self):
        return self.edges


    def find_nodes(
        self,
        node_type: NodeKind,
    ) -> list[GraphNode]:

        return [
            node
            for node in self.nodes.values()
            if node.type == node_type
        ]


    def find_by_kind(
        self,
        kind: NodeKind | str,
    ):

        return [
            node
            for node in self.nodes.values()
            if node.type == kind
        ]


    def outgoing(
        self,
        node_id: str,
        relation=None,
    ):

        return [
            edge
            for edge in self.edges
            if (
                edge.source == node_id
                and (
                    relation is None
                    or edge.type == relation
                )
            )
        ]


    def incoming(
        self,
        node_id: str,
        relation=None,
    ):

        return [
            edge
            for edge in self.edges
            if (
                edge.target == node_id
                and (
                    relation is None
                    or edge.type == relation
                )
            )
        ]


    def find_by_label(
        self,
        label: str,
    ):

        return [
            node
            for node in self.nodes
            if node.name == label
        ]


    def as_dict(
        self,
    ) -> dict[str, Any]:

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


    def to_dict(self):
        return self.as_dict()


# ---------------------------------------------------------
# Compatibility aliases
# ---------------------------------------------------------

GraphNodeType = NodeKind
GraphEdgeType = EdgeRelation


# ---------------------------------------------------------
# Canonical graph naming compatibility aliases
# ---------------------------------------------------------

GraphNodeType = NodeKind
GraphEdgeType = EdgeRelation
