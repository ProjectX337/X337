from __future__ import annotations


class ExecutionValidator:
    """
    Validates execution before and after mutation.

    Runtime boundary:

        Task
          |
          v
        before()
          |
          v
      Capability
          |
          v
        after()
    """

    def before(
        self,
        context,
        task,
    ) -> bool:

        return True


    def after(
        self,
        context,
        result,
    ) -> bool:

        return True
