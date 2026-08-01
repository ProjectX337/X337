from __future__ import annotations


class ToolExecutor:
    """
    Runs X337 tools.
    """


    def __init__(
        self,
        tools,
    ):

        self.tools = {
            tool.name: tool
            for tool in tools
        }


    def run(
        self,
        name,
        context=None,
    ):

        tool = self.tools[name]

        return tool.execute(
            context
        )
