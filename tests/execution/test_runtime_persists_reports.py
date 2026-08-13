from core.execution.bootstrap.runtime_factory import (
    create_execution_runtime,
)

from core.graph.change_plan import (
    ChangePlan,
)


def test_runtime_persists_execution_report():

    runtime = create_execution_runtime()

    from core.graph.change import ChangeRequest

    from core.graph.change import ChangeType

    change = ChangeRequest(
        target_node="test-node",
        change_type=ChangeType.ADD,
    )

    plan = ChangePlan(
        change=change,
        signals=[]
    )

    report = runtime.execute(
        plan=plan,
    )

    history = runtime.report_memory_sink.memory.history()

    assert report.execution_id is not None
    assert len(history) == 1
