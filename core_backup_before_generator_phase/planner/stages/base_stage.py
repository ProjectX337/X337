from __future__ import annotations

from abc import ABC, abstractmethod

from core.planner.planning_context import PlanningContext


class PlanningStage(ABC):
    """
    Base class for every planning stage.
    """

    requires: set[str] = set()

    provides: set[str] = set()

    @abstractmethod
    def run(
        self,
        context: PlanningContext,
    ) -> None:
        """
        Execute the stage.
        """
        raise NotImplementedError
