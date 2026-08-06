from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from core.reasoning.decision import Decision


class BaseReasoner(ABC):

    @abstractmethod
    def infer(self, **kwargs) -> Decision:
        """
        Produce a Decision from planner context.
        """
        raise NotImplementedError
