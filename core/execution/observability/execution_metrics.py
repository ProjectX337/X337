from __future__ import annotations


class ExecutionMetrics:
    """
    Aggregates execution runtime statistics.
    """

    def __init__(self):
        self.total = 0
        self.successful = 0
        self.failed = 0


    def record(
        self,
        result,
    ):

        self.total += 1

        if result.success:
            self.successful += 1
        else:
            self.failed += 1


    @property
    def success_rate(self):

        if self.total == 0:
            return 0

        return self.successful / self.total
