from core.execution.action_router import ActionRouter
from core.execution.task import ExecutionTask


def test_action_router_resolves_handler():

    router = ActionRouter()

    handler = object()

    router.register(
        "modify_component",
        handler,
    )

    task = ExecutionTask(
        action="modify_component",
        target="component.authform",
    )

    result = router.resolve(task)

    assert result is handler
