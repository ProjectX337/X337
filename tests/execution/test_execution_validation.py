from core.execution.validation.validator import (
    ExecutionValidator,
)


def test_execution_validator_defaults():

    validator = ExecutionValidator()

    assert validator.before(
        None,
        None,
    ) is True

    assert validator.after(
        None,
        None,
    ) is True
