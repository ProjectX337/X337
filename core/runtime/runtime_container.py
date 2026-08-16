from core.runtime.runtime_registry import RuntimeRegistry
from core.runtime.process_manager import ProcessManager
from core.runtime.runtime_manager import RuntimeManager
from core.runtime.runtime_service import RuntimeService
from core.runtime.runtime_controller import RuntimeController


registry = RuntimeRegistry()

process_manager = ProcessManager()

runtime_manager = RuntimeManager(
    registry=registry,
    process_manager=process_manager,
)


runtime_service = RuntimeService(
    runtime_manager,
    registry
)


runtime_controller = RuntimeController(
    runtime_service
)
