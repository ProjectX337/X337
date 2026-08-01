from __future__ import annotations

from core.tools.executor import ToolExecutor


class AgentExecutor:
    """
    Adapter between AutonomousAgent and X337 tools.
    """

    def __init__(
        self,
        tools,
    ):
        self.executor = ToolExecutor(
            tools
        )


    @property
    def tools(self):

        return self.executor.tools

    def run(
        self,
        action,
        context=None,
    ):
        return self.executor.run(
            action,
            context,
        )
