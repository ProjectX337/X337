from core.runtime.runtime_registry import RuntimeRegistry
from core.runtime.process_manager import ProcessManager
from core.runtime.runtime_manager import RuntimeManager
from core.runtime.runtime_factory import RuntimeFactory
from core.preview.runtime import PreviewRuntime
from core.runtime.runtime_service import RuntimeService
from core.runtime.runtime_controller import RuntimeController
from core.preview.runtime import PreviewRuntime


registry = RuntimeRegistry()

process_manager = ProcessManager()

runtime_factory = RuntimeFactory()

preview_runtime = PreviewRuntime(
    process_manager
)

runtime_manager = RuntimeManager(
    registry=registry,
    process_manager=process_manager,
    preview_runtime=preview_runtime,
    runtime_factory=runtime_factory,
)


runtime_service = RuntimeService(
    runtime_manager
)


runtime_controller = RuntimeController(
    runtime_service
)
