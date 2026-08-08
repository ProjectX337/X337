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
print(result["artifact"])

print()

print("PROCESS IDS:")
print(result["process_ids"])

print()

print("PREVIEW:")
print(result["preview"])
