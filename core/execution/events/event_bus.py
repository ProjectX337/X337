from __future__ import annotations

from core.execution.events.execution_event import ExecutionEvent


class ExecutionEventBus:
    """
    Collects execution lifecycle events.
    """

    def __init__(self):
        self.events: list[ExecutionEvent] = []


    def emit(
        self,
        event: ExecutionEvent,
    ):
        self.events.append(
            event
        )


    def all(self) -> list[ExecutionEvent]:
        return self.events
