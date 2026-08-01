from agents.base.base_agent import BaseAgent

from core.models.task_result import TaskResult



class ResearcherAgent(BaseAgent):


    AGENT_NAME = "Researcher"


    DESCRIPTION = (
        "Researches information and gathers knowledge."
    )


    CAPABILITIES = [
        "research"
    ]


    VERSION = "1.0.0"


    ENABLED = True



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
            "Performing research..."
        )


        research_result = {


            "topic": task.title,


            "findings": [

                "Research completed",

                "Information gathered",

                "Summary created"

            ]

        }



        task.context["research"] = (

            research_result

        )



        task.history.append(

            "Researcher completed research"

        )



        return TaskResult(

            success=True,

            agent=self.name,

            task=task.title,

            result=research_result

        )