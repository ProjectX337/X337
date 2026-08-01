from __future__ import annotations

from core.planner.project_planner import ProjectPlanner


class PlannerBridge:

    def __init__(self):
        self.planner = ProjectPlanner()

    def execute(
        self,
        message: str,
        intent: str,
    ):

        if intent == "create_project":

            return self.planner.plan(
                message
            )

        return {
            "intent": intent,
            "message": message,
        }
