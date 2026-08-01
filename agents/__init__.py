from agents.base.base_agent import BaseAgent

from core.models.task_result import TaskResult


class WriterAgent(BaseAgent):


    AGENT_NAME = "Writer"

    DESCRIPTION = (
        "Creates written documents and reports."
    )

    CAPABILITIES = [
        "writing"
    ]

    VERSION = "1.0.0"

    ENABLED = True



    def __init__(self):

        super().__init__()



    def execute(self, task):


        self.log(
            "Writing report..."
        )


        report = {

            "title": task.title,

            "content": (
                "Generated report based "
                "on task requirements."
            )

        }


        task.context["document"] = (
            report
        )


        task.history.append(
            "Writer created document"
        )


        return TaskResult(
            success=True,
            agent=self.name,
            task=task.title,
            result=report
        )