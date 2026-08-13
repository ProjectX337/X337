from core.execution.capabilities.modify_component import (
    ModifyComponentCapability,
)

from core.execution.task import ExecutionTask


def test_modify_component_capability():

    capability = ModifyComponentCapability()

    task = ExecutionTask(
        action="modify_component",
        target="component.authform",
    )

    result = capability.execute(
        task
    )

    assert result.success is True
    assert result.output["action"] == "modify_component"
    assert result.output["target"] == "component.authform"
