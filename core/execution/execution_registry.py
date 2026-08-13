from __future__ import annotations


class ExecutionRegistry:
    """
    Registry of executable capabilities.

    Maps execution actions to handlers.
    """

    def __init__(self):

        self._handlers = {}


    def register(
        self,
        action: str,
        handler,
    ):

        self._handlers[action] = handler


    def get(
        self,
        action: str,
    ):

        return self._handlers.get(action)


    def contains(
        self,
        action: str,
    ) -> bool:

        return action in self._handlers
