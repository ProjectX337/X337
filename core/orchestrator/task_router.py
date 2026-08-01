class TaskRouter:


    def __init__(
        self,
        queue
    ):


        self.queue = queue



    def route(
        self,
        task
    ):


        self.queue.add(

            {

                "agent": "Planner",

                "task": task,

                "reason": "TaskStarted"

            }

        )


        print(

            "⚡ Queue: Planner added"

        )