from __future__ import annotations


class AutonomousAgent:
    """
    Full X337 build loop.
    """


    def __init__(
        self,
        executor,
    ):

        self.executor = executor



    def build(
        self,
        context=None,
    ):

        generated = self.executor.run(
            "generate",
            context,
        )


        tested = self.executor.run(
            "test",
            context,
        )


        if tested["passed"]:

            return {
                "status": "complete",
                "generated": generated,
            }


        repaired = self.executor.run(
            "repair",
            context,
        )


        return repaired
