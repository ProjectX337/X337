from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class ExecutionEvent:
    """
    Immutable record of runtime execution.

    Tracks:
        planning
        validation
        execution
        completion
    """

    event_type: str

    action: str | None = None

    target: str | None = None

    message: str = ""

    timestamp: datetime = datetime.utcnow()
