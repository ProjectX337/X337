from __future__ import annotations

from dataclasses import dataclass, field

from core.execution.capability import ExecutionResult


@dataclass
class ExecutionState:
    """
    Tracks execution outcomes for project evolution.
    """

    results: list[ExecutionResult] = field(
        default_factory=list
    )


    def record(
        self,
        result: ExecutionResult,
    ) -> None:

        self.results.append(
            result
        )


    @property
    def success(self) -> bool:

        return all(
            result.success
            for result in self.results
        )
