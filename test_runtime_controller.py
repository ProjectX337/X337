from core.runtime.manifest_loader import ManifestLoader
from core.runtime.runtime_manager import RuntimeManager
from core.runtime.runtime_controller import RuntimeController


loader = ManifestLoader()

artifact = loader.load(
    "create_ai_tutor_website"
)


runtime = RuntimeManager()

controller = RuntimeController(
    runtime
)


result = controller.start(
    artifact
)


print("STARTED")
print(result)


print()

print("STATUS")
print(
    controller.status(
        artifact.name
    )
)


print()

print("PREVIEWS")
print(
    controller.previews()
)


print()

print("STOPPING")

print(
    controller.stop(
        artifact.name
    )
)


print()

print("STATUS AFTER STOP")

print(
    controller.status(
        artifact.name
    )
)