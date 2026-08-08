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


print("ARTIFACT:")
print(
    result["artifact"]
)


print()

print("PREVIEW:")
print(
    result["preview"]
)


print()

print("ALL PREVIEWS:")
print(
    runtime.preview_registry.list()
)
