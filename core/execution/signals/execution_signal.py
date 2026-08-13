from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ExecutionSignal:
    """
    Architectural signal generated from runtime behavior.

    Examples:

    - repeated_failure
    - unstable_capability
    - slow_execution
    - missing_dependency
    """

    signal_type: str

    action: str

    target: str

    severity: float = 0.0

    message: str = ""
