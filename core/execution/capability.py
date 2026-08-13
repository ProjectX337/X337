from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ExecutionResult:
    """
    Result returned by an execution capability.
    """

    success: bool

    output: object | None = None

    metadata: dict = field(
        default_factory=dict
    )


class ExecutionCapability:
    """
    Base contract for executable abilities.

    Capabilities mutate or operate on the project.
    """

    name: str = ""

    def execute(
        self,
        task,
    ) -> ExecutionResult:

        raise NotImplementedError
