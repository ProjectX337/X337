from core.runtime.manifest_loader import ManifestLoader
from core.runtime.runtime_controller import RuntimeController


loader = ManifestLoader()


artifact = loader.load(
    "create_ai_tutor_website"
)


controller = RuntimeController()


print("STARTING")

controller.start(
    artifact
)


print()

print("STATUS:")

print(
    controller.status(
        "create_ai_tutor_website"
    )
)


print()

print("ALL RUNNING:")

print(
    controller.list_running()
)
