from __future__ import annotations

from core.ai.planner_agent import PlannerAgent
from core.agent.update_agent import UpdateAgent


class ChatAgent:
    """
    Main X337 conversational agent.
    """


    def __init__(self):

        self.planner = PlannerAgent()

        self.updater = UpdateAgent()



    def respond(
        self,
        message: str,
    ):

        if any(
            word in message.lower()
            for word in [
                "add",
                "change",
                "update",
            ]
        ):

            state = self.updater.apply(
                message
            )

            return (
                "Updated project with: "
                + ", ".join(
                    state.changes
                )
            )


        spec = self.planner.build(
            message
        )


        return (
            f"Created project: "
            f"{spec.project_name}"
        )
