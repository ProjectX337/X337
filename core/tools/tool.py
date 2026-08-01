from __future__ import annotations

from abc import ABC, abstractmethod


class Tool(ABC):
    """
    Base executable capability.
    """

    name: str = ""


    @abstractmethod
    def execute(
        self,
        context,
    ):
        pass
