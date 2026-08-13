from __future__ import annotations


class PlanningExecutionBridge:
    """
    Connects planning decisions with execution outcomes.

    Flow:

        Plan
         |
         v
      Execute
         |
         v
      Feedback
         |
         v
      Learning
    """

    def __init__(
        self,
        runtime,
    ):

        self.runtime = runtime


    def execute_plan(
        self,
        plan,
        context=None,
    ):

        return self.runtime.execute(
            plan,
            context=context,
        )


    def evolve_from_signal(
        self,
        signal,
        context=None,
    ):

        return self.runtime.evolve(
            signal,
            context=context,
        )
