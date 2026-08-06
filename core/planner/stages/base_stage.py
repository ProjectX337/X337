from __future__ import annotations

from abc import ABC, abstractmethod

from core.cognition.cognitive_state import CognitiveState


class PlanningStage(ABC):
    """
    Base class for every cognitive stage.

    Each stage reads and writes the shared CognitiveState.
    """

    requires: set[str] = set()

    provides: set[str] = set()

    @abstractmethod
    def run(
        self,
        state: CognitiveState,
    ) -> None:
        ...
