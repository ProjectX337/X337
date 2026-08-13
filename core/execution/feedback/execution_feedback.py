from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ExecutionFeedback:
    """
    Resulting learning signal from execution.
    """

    action: str

    target: str

    success: bool

    duration_ms: float = 0

    errors: list[str] = field(
        default_factory=list
    )

    metadata: dict = field(
        default_factory=dict
    )
