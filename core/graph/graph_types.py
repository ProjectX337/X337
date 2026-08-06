from __future__ import annotations

from enum import StrEnum


class GraphNodeType(StrEnum):
    """
    Canonical node categories used throughout X337.

    Every reasoning object should map to one of these.
    """

    PROMPT = "prompt"
    INTENT = "intent"
    CAPABILITY = "capability"
    FEATURE = "feature"
    PAGE = "page"
    COMPONENT = "component"
    ROUTE = "route"
    API = "api"
    DATABASE = "database"
    TECHNOLOGY = "technology"
    DESIGN = "design"
    PRODUCT = "product"
    PROJECT = "project"
    FILE = "file"
    TEST = "test"
    TASK = "task"
    DECISION = "decision"
    OBSERVATION = "observation"
    AGENT = "agent"
