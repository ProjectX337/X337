from core.execution.coordinator import ExecutionCoordinator
from core.execution.bootstrap.default_capabilities import (
    create_default_router,
)
from core.execution.context.execution_context import ExecutionContext
from core.execution.validation.validator import ExecutionValidator
from core.graph.change_plan import ChangePlan, ChangeRequest
from core.graph.change import ChangeType


class RejectValidator(ExecutionValidator):

    def before(
        self,
        context,
        task,
    ):
        return False


def test_execution_stops_when_validation_fails():

    coordinator = ExecutionCoordinator(
        router=create_default_router(),
        validator=RejectValidator(),
    )

    plan = ChangePlan(
        change=ChangeRequest(
            target_node="feature.auth",
            change_type=ChangeType.ADD,
        )
    )

    report = coordinator.execute(
        plan,
        context=ExecutionContext(),
    )

    assert report.success is False
