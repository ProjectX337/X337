from agents.base.base_agent import BaseAgent

from core.models.task_result import TaskResult

from core.events.event import Event
from core.events.event_types import EventTypes



class DirectorAgent(BaseAgent):


    AGENT_NAME = "Director"


    DESCRIPTION = (
        "Receives tasks and coordinates workflow initialization."
    )


    CAPABILITIES = [
        "task intake",
        "coordination",
        "workflow initialization"
    ]


    VERSION = "1.0.0"



    def __init__(
        self,
        app=None
    ):

        super().__init__(
            app=app
        )



    def execute(
        self,
        task
    ):


        self.log(
            f"Accepted task: {task.title}"
        )


        task.current_agent = self.name


        task.status = "Accepted"


        task.history.append(
            f"Director accepted task '{task.title}'"
        )



        self.bus.publish(

            Event(

                type=EventTypes.TASK_ACCEPTED,

                source=self.name,

                data={

                    "task": task.title,

                    "task_id": task.id

                }

            )

        )



        return TaskResult(

            success=True,

            agent=self.name,

            task=task.title,

            result={

                "status": "Task accepted",

                "task_id": task.id

            }

        )