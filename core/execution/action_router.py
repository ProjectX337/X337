from __future__ import annotations

from core.execution.task import ExecutionTask


class ActionRouter:
    """
    Routes execution tasks to implementation handlers.

    Compatibility:
        resolve()
            -> returns capability

    Execution:
        execute()
            -> runs capability
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


    def execute(
        self,
        task: ExecutionTask,
    ):

        handler = self.resolve(
            task
        )

        if handler is None:
            raise ValueError(
                f"No execution handler registered for {task.action}"
            )

        return handler.execute(
            task
        )