from __future__ import annotations

from core.execution.events.execution_event import (
    ExecutionEvent,
)

from core.execution.feedback.execution_feedback import (
    ExecutionFeedback,
)


class RuntimeLifecycle:
    """
    Wraps execution with observation and learning hooks.

    Flow:

        before
          |
          v
      execution
          |
          v
        after
          |
          +--> events
          +--> feedback
    """

    def __init__(
        self,
        event_bus=None,
        metrics=None,
        feedback_processor=None,
    ):
        self.event_bus = event_bus
        self.metrics = metrics
        self.feedback_processor = feedback_processor


    def before(
        self,
        plan,
    ):

        if self.event_bus:

            self.event_bus.emit(
                ExecutionEvent(
                    event_type="execution_started",
                )
            )


    def after(
        self,
        result,
        plan,
    ):

        if self.metrics:

            self.metrics.record(
                result
            )

        if self.event_bus:

            self.event_bus.emit(
                ExecutionEvent(
                    event_type="execution_completed",
                )
            )

        if self.feedback_processor:

            self.feedback_processor.process(
                ExecutionFeedback(
                    action=str(
                        plan.change.target_node
                    ),
                    target=str(
                        plan.change.target_node
                    ),
                    success=result.success,
                )
            )
