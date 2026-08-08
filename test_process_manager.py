from core.runtime.manifest_loader import ManifestLoader
from core.runtime.runtime_manager import RuntimeManager


loader = ManifestLoader()

artifact = loader.load(
    "create_ai_tutor_website"
)


runtime = RuntimeManager()


result = runtime.launch(
    artifact
)


print("PROCESS:")
print(
    result["process_record"]
)


print()

print("RUNNING:")
print(
    runtime.process_manager.is_running(
        artifact.name
    )
)


print()

print("STOPPING:")
print(
    runtime.process_manager.stop(
        artifact.name
    )
)


print()

print("RUNNING:")
print(
    runtime.process_manager.is_running(
        artifact.name
    )
)
