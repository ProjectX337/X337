from __future__ import annotations

from core.agent.autonomous_agent import AutonomousAgent
from core.agent.executor import AgentExecutor
from core.agent.repair.repair_agent import RepairAgent

from core.tools.generate_tool import GenerateTool
from core.tools.test_tool import TestTool
from core.tools.repair_tool import RepairTool


def create_autonomous_agent():

    tools = [
        GenerateTool(),
        TestTool(),
    ]

    executor = AgentExecutor(
        tools
    )

    repair_agent = RepairAgent(
        executor
    )

    tools.append(
        RepairTool(
            repair_agent
        )
    )

    executor = AgentExecutor(
        tools
    )

    return AutonomousAgent(
        executor
    )
