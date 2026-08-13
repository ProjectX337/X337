from __future__ import annotations

from core.execution.runtime.execution_runtime import (
    ExecutionRuntime,
)

from core.execution.coordinator import (
    ExecutionCoordinator,
)

from core.execution.bootstrap.default_capabilities import (
    create_default_router,
)

from core.execution.evolution.evolution_loop import (
    EvolutionLoop,
)

from core.execution.evolution.evolution_engine import (
    EvolutionEngine,
)

from core.execution.learning.feedback_processor import (
    FeedbackProcessor,
)

from core.execution.memory.execution_memory import (
    ExecutionMemory,
)


def create_execution_runtime():

    router = create_default_router()

    coordinator = ExecutionCoordinator(
        router=router,
    )

    evolution_engine = EvolutionEngine()

    evolution_loop = EvolutionLoop(
        evolution_engine=evolution_engine,
        coordinator=coordinator,
    )

    memory = ExecutionMemory()

    feedback_processor = FeedbackProcessor(
        memory=memory,
    )

    return ExecutionRuntime(
        coordinator=coordinator,
        evolution_loop=evolution_loop,
        feedback_processor=feedback_processor,
    )
