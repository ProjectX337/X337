from __future__ import annotations

from core.agent.intent_router import IntentRouter
from core.agent.planner_bridge import PlannerBridge


class X337Agent:
    """
    Main conversational interface for X337.
    """

    def __init__(self):
        self.router = IntentRouter()
        self.planner = PlannerBridge()

    def chat(
        self,
        message: str,
    ):
        intent = self.router.route(message)

        return self.planner.execute(
            message,
            intent,
        )
