import json
import os

from datetime import datetime




class WorkflowHistory:


    def __init__(
        self,
        memory=None
    ):

        self.memory = memory

        self.file = (

            "memory/workflow_history.json"

        )

        os.makedirs(

            "memory",

            exist_ok=True

        )


        self.history = self.load()





    def load(
        self
    ):


        if not os.path.exists(
            self.file
        ):

            return []



        try:

            with open(
                self.file,
                "r"
            ) as f:

                return json.load(f)



        except json.JSONDecodeError:


            print(
                "⚠ Corrupted workflow history. Resetting memory."
            )


            return []



    def save(
        self
    ):


        with open(

            self.file,

            "w"

        ) as f:


            json.dump(

                self.history,

                f,

                indent=4

            )





    #
    # Compatibility method
    #
    # Existing Brain uses this
    #

    def record(
        self,
        task,
        workflow,
        success=True,
        score=100
    ):


        if hasattr(task, "title"):

            task_name = task.title

        else:

            task_name = str(task)



        entry = {


            "task": task_name,


            "workflow": workflow,


            "success": success,


            "score": score,


            "timestamp": str(datetime.now())

        }



        self.history.append(

            entry

        )


        self.save()





    def add_workflow(
        self,
        task,
        workflow,
        success=True,
        failures=0,
        score=None
    ):


        self.record(

            task,

            workflow,

            success,

            score if score is not None else 100

        )






    def best_recent_workflow(
        self
    ):


        if not self.history:

            return None



        best = max(

            self.history,

            key=lambda x:

            x.get(

                "score",

                0

            )

        )


        return best.get(

            "workflow"

        )






    def success_percentage(
        self
    ):


        if not self.history:

            return 0



        successes = sum(

            1

            for item in self.history

            if item.get(

                "success"

            )

        )


        return round(

            successes /

            len(self.history)

            *

            100,

            2

        )
