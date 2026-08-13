from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ExecutionTask:
    """
    Concrete engineering action derived from
    an EngineeringSignal.

    This is the boundary between reasoning
    and mutation.
    """

    action: str

    target: str

    metadata: dict = field(
        default_factory=dict
    )

    status: str = "pending"
