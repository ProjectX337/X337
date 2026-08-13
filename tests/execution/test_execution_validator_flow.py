from core.execution.coordinator import ExecutionCoordinator
from core.execution.validation.validator import ExecutionValidator
from core.execution.bootstrap.default_capabilities import (
    create_default_router,
)


class TrackingValidator(ExecutionValidator):

    def __init__(self):
        self.before_called = False
        self.after_called = False

    def before(self, context, task):
        self.before_called = True
        return True

    def after(self, context, result):
        self.after_called = True
        return True


def test_validator_wraps_execution():

    validator = TrackingValidator()

    coordinator = ExecutionCoordinator(
        router=create_default_router(),
        validator=validator,
    )

    assert validator.before_called is False
    assert validator.after_called is False
