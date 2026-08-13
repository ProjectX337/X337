from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, UTC


@dataclass
class ExecutionTrace:
    """
    Persistent record of an execution lifecycle.

    Signal
        |
        v
    Task
        |
        v
    Capability
        |
        v
    Result
    """

    action: str

    target: str

    events: list = field(
        default_factory=list
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )


    def add_event(
        self,
        event,
    ):
        self.events.append(event)
