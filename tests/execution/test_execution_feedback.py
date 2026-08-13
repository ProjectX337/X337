from core.execution.feedback.execution_feedback import (
    ExecutionFeedback,
)


def test_execution_feedback_contract():

    feedback = ExecutionFeedback(
        action="apply_feature_change",
        target="feature.auth",
        success=True,
    )

    assert feedback.success is True
    assert feedback.action == "apply_feature_change"
