from core.runtime.runtime_registry import RuntimeRegistry
from core.runtime.artifact import Artifact


registry = RuntimeRegistry()


artifact = Artifact(
    name="test_app",
    artifact_type="website",
    path="workspace/projects/test_app"
)


registry.register(
    artifact,
    {
        "pid":1234,
        "status":"running"
    }
)


print()

print("GET:")
print(
    registry.get(
        "test_app"
    )
)


print()

print("LIST:")
print(
    registry.list()
)
