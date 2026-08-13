from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class NodeType(str, Enum):
    FEATURE = "feature"
    PAGE = "page"
    COMPONENT = "component"
    STATE = "state"
    API_ENDPOINT = "api_endpoint"
    DATABASE_MODEL = "database_model"
    SOURCE_FILE = "source_file"


@dataclass
class GraphNode:
    id: str
    name: str
    node_type: NodeType
    metadata: dict = field(
        default_factory=dict
    )


@dataclass
class FeatureNode(GraphNode):
    def __init__(
        self,
        id: str,
        name: str,
        metadata: dict | None = None,
    ):
        super().__init__(
            id=id,
            name=name,
            node_type=NodeType.FEATURE,
            metadata=metadata or {},
        )


@dataclass
class PageNode(GraphNode):
    def __init__(
        self,
        id: str,
        name: str,
        metadata: dict | None = None,
    ):
        super().__init__(
            id=id,
            name=name,
            node_type=NodeType.PAGE,
            metadata=metadata or {},
        )


@dataclass
class ComponentNode(GraphNode):
    def __init__(
        self,
        id: str,
        name: str,
        metadata: dict | None = None,
    ):
        super().__init__(
            id=id,
            name=name,
            node_type=NodeType.COMPONENT,
            metadata=metadata or {},
        )
