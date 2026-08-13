from core.execution.execution_registry import (
    ExecutionRegistry,
)


def test_execution_registry_registers_capability():

    registry = ExecutionRegistry()

    generator = object()

    registry.register(
        "modify_component",
        generator,
    )

    assert registry.contains(
        "modify_component"
    )

    assert registry.get(
        "modify_component"
    ) is generator
