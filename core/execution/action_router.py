from __future__ import annotations

from core.execution.task import ExecutionTask


class ActionRouter:
    """
    Routes execution tasks to implementation handlers.

    This layer decides WHAT performs an action.
    It does not perform generation itself.
    """

    def __init__(self):

        self.handlers = {}


    def register(
        self,
        action: str,
        handler,
    ):

        self.handlers[action] = handler


    def resolve(
        self,
        task: ExecutionTask,
    ):

        return self.handlers.get(
            task.action
        )
