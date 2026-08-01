from __future__ import annotations

from core.agent.repair.error_analyzer import ErrorAnalyzer


class RepairAgent:
    """
    Self-correction engine.
    """


    def __init__(
        self,
        executor,
    ):

        self.executor = executor

        self.analyzer = ErrorAnalyzer()



    def run_loop(
        self,
        context=None,
        attempts=3,
    ):

        for attempt in range(
            attempts
        ):

            result = self.executor.run(
                "test",
                context,
            )


            if result["passed"]:

                return {
                    "status": "success",
                    "attempt": attempt + 1,
                }


            error = self.analyzer.analyze(
                result
            )


            print(
                "Repair needed:",
                error["type"]
            )


            # Future:
            # LLM modifies files here


        return {
            "status": "failed",
            "attempts": attempts,
        }
