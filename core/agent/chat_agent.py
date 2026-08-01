from __future__ import annotations

from core.planner.project_planner import ProjectPlanner
from core.agent.memory import ConversationMemory


class ChatAgent:
    """
    Conversational AI layer over X337 planner.
    """

    def __init__(self):

        self.planner = ProjectPlanner()

        self.memory = ConversationMemory()


    def respond(
        self,
        message: str,
    ) -> str:

        self.memory.add(message)

        spec = self.planner.plan(
            message
        )

        return (
            f"Project planned: {spec.project_name}. "
            f"Conversation messages: "
            f"{len(self.memory.history())}"
        )
