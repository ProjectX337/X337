from __future__ import annotations

from core.tools.tool import Tool


class RepairTool(Tool):

    name = "repair"


    def __init__(
        self,
        repair_agent,
    ):

        self.agent = repair_agent


    def execute(
        self,
        context=None,
    ):

        return self.agent.run_loop(
            context
        )
