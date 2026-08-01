class ReflectionManager:


    def __init__(self):

        self.feedback = []



    def analyze(
        self,
        result
    ):


        if result.success:

            return {

                "status": "success",

                "action": "continue"

            }



        feedback = {

            "status": "failure",

            "issue": result.result,

            "action": "retry"

        }


        self.feedback.append(
            feedback
        )


        return feedback



    def history(self):

        return self.feedback