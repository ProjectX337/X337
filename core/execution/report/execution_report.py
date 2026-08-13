from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ExecutionReport:
    """
    Canonical record of one execution cycle.

    Captures:
        plan
        execution result
        feedback
        generated signals
        evolution outcome
        lifecycle events
    """

    execution_id: str

    plan: Any

    result: Any = None

    feedback: Any = None

    signals: list[Any] = field(
        default_factory=list
    )

    evolution_plan: Any = None

    events: list[Any] = field(
        default_factory=list
    )
