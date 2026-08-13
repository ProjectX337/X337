from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class GraphNodeType(str, Enum):
    PRODUCT = "product"
    FEATURE = "feature"
    PAGE = "page"
    COMPONENT = "component"
    STATE = "state"
    ENTITY = "entity"
    API_ENDPOINT = "api_endpoint"
    DATABASE_MODEL = "database_model"
    SOURCE_FILE = "source_file"


class GraphEdgeType(str, Enum):
    REQUIRES = "requires"
    IMPLEMENTS = "implements"
    RENDERS = "renders"
    MUTATES = "mutates"


@dataclass
class GraphNode:
    """
    Represents an architectural entity.
    """

    id: str

    type: GraphNodeType

    name: str

    metadata: dict = field(
        default_factory=dict
    )


@dataclass
class GraphEdge:
    """
    Represents a relationship between
    architectural entities.
    """

    source: str

    target: str

    type: GraphEdgeType

    metadata: dict = field(
        default_factory=dict
    )


@dataclass
class ApplicationGraph:
    """
    Canonical architecture representation.

    Connects product intent to engineering structure.
    """

    nodes: list[GraphNode] = field(
        default_factory=list
    )

    edges: list[GraphEdge] = field(
        default_factory=list
    )

    def add_node(
        self,
        node: GraphNode,
    ):
        self.nodes.append(node)

    def add_edge(
        self,
        edge: GraphEdge,
    ):
        self.edges.append(edge)

    def find_nodes(
        self,
        node_type: GraphNodeType,
    ) -> list[GraphNode]:

        return [
            node
            for node in self.nodes
            if node.type == node_type
        ]

    def as_dict(self) -> dict:
        return {
            "nodes": [
                {
                    "id": node.id,
                    "type": node.type.value,
                    "name": node.name,
                    "metadata": node.metadata,
                }
                for node in self.nodes
            ],
            "edges": [
                {
                    "source": edge.source,
                    "target": edge.target,
                    "type": edge.type.value,
                    "metadata": edge.metadata,
                }
                for edge in self.edges
            ],
        }

    def get_node(self, node_id: str):
        """
        Retrieve a node by id.
        """
        for node in self.nodes:
            if node.id == node_id:
                return node

        return None


    @property
    def node_map(self):
        """
        Dictionary compatibility view.
        """
        return {
            node.id: node
            for node in self.nodes
        }

