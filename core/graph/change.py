from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class ChangeType(str, Enum):
    ADD = "add"
    MODIFY = "modify"
    REMOVE = "remove"


@dataclass
class ChangeRequest:
    """
    Represents an intended application evolution.

    This does not mutate ApplicationGraph.
    It describes a requested transformation.
    """

    target_node: str

    change_type: ChangeType

    description: str = ""

    metadata: dict = field(
        default_factory=dict
    )

