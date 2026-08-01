from agents.base.base_agent import BaseAgent

from core.models.task_result import TaskResult



class WriterAgent(BaseAgent):


    AGENT_NAME = "Writer"


    DESCRIPTION = (
        "Creates documents using available knowledge."
    )


    CAPABILITIES = [
        "writing"
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
            "Writing document..."
        )



        # Retrieve information from shared memory

        research = task.memory.retrieve(
            "research"
        )



        document = {


            "title": task.title,


            "content": (
                "Generated document "
                "using available research."
            ),


            "source_research": research

        }



        # Store document for later agents

        task.memory.store(

            "document",

            document

        )



        task.history.append(

            "Writer created document using memory"

        )



        return TaskResult(

            success=True,

            agent=self.name,

            task=task.title,

            result=document

        )