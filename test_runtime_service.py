from core.runtime.runtime_manager import RuntimeManager
from core.runtime.runtime_registry import RuntimeRegistry
from core.runtime.runtime_service import RuntimeService
from core.runtime.runtime_controller import RuntimeController

from core.runtime.manifest_loader import ManifestLoader



loader = ManifestLoader()


artifact = loader.load(
    "create_ai_tutor_website"
)



runtime = RuntimeManager()

registry = RuntimeRegistry()


service = RuntimeService(
    runtime,
    registry
)


controller = RuntimeController(
    service
)



print("START")

result = controller.start(
    artifact
)

print(result)


print()

print("STATUS")

print(
    controller.status(
        artifact.name
    )
)


print()

print("RUNNING")

print(
    controller.list_running()
)


print()

print("STOP")

print(
    controller.stop(
        artifact.name
    )
)