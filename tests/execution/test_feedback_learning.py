from core.execution.learning.feedback_processor import (
    FeedbackProcessor,
)

from core.execution.memory.execution_memory import (
    ExecutionMemory,
)

from core.execution.feedback.execution_feedback import (
    ExecutionFeedback,
)


def test_feedback_processor_updates_memory():

    memory = ExecutionMemory()

    processor = FeedbackProcessor(
        memory
    )

    processor.process(
        ExecutionFeedback(
            action="apply_feature_change",
            target="feature.auth",
            success=True,
        )
    )

    assert memory.success_rate(
        "apply_feature_change"
    ) == 1
