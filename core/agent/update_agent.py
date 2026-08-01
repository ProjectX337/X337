from __future__ import annotations

from core.agent.project_state import ProjectState
from core.agent.change_engine import ChangeEngine


class UpdateAgent:
    """
    Applies changes to an existing project.
    """


    def __init__(self):

        self.state = ProjectState()

        self.engine = ChangeEngine()


    def apply(
        self,
        message: str,
    ):

        changes = self.engine.detect(
            message
        )


        for feature in changes["features"]:

            self.state.record_change(
                feature
            )


        return self.state
