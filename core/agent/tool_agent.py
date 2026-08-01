from __future__ import annotations

from core.tools.executor import ToolExecutor
from core.tools.generate_tool import GenerateTool
from core.tools.test_tool import TestTool


class ToolAgent:

    def __init__(self):

        self.executor = ToolExecutor(
            [
                GenerateTool(),
                TestTool(),
            ]
        )


    def run(
        self,
        command,
        context=None,
    ):

        return self.executor.run(
            command,
            context,
        )
