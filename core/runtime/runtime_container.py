from core.runtime.runtime_registry import RuntimeRegistry
from core.runtime.runtime_manager import RuntimeManager
from core.runtime.runtime_service import RuntimeService


registry = RuntimeRegistry()

runtime_manager = RuntimeManager(
    registry=registry
)

runtime_service = RuntimeService(
    runtime_manager,
    registry
)
