from core.agent.conversation import Conversation
from core.agent.memory import ProjectMemory

from core.planner.project_planner import ProjectPlanner


class X337Agent:

    def __init__(self):

        self.conversation = Conversation()

        self.memory = ProjectMemory()

        self.planner = ProjectPlanner()


    def run(
        self,
        message: str,
    ):

        self.conversation.add(
            "user",
            message,
        )

        self.memory.last_prompt = message

        spec = self.planner.plan(
            message
        )

        self.memory.project_spec = spec

        return spec
