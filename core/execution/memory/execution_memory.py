from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ExecutionMemoryEntry:
    action: str
    target: str
    success: bool
    metadata: dict = field(
        default_factory=dict
    )


class ExecutionMemory:
    """
    Stores historical execution outcomes.

    Used by future planning systems to learn
    which execution paths succeed.
    """

    def __init__(self):

        self.entries: list[ExecutionMemoryEntry] = []


    def remember(
        self,
        entry: ExecutionMemoryEntry,
    ):

        self.entries.append(
            entry
        )


    def history(
        self,
    ) -> list[ExecutionMemoryEntry]:

        return self.entries


    def success_rate(
        self,
        action: str,
    ) -> float:

        matches = [
            entry
            for entry in self.entries
            if entry.action == action
        ]

        if not matches:
            return 0.0

        successes = sum(
            entry.success
            for entry in matches
        )

        return successes / len(matches)
