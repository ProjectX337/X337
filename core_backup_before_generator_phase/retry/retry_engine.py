class RetryEngine:


    def __init__(
        self,
        max_attempts=3
    ):

        self.max_attempts = max_attempts



    def should_retry(
        self,
        attempt
    ):

        return attempt < self.max_attempts



    def retry(
        self,
        agent,
        task,
        feedback
    ):


        task.history.append(

            f"Retrying {agent.name}"

        )


        task.memory.store(

            "feedback",

            feedback

        )


        return agent.execute(
            task
        )