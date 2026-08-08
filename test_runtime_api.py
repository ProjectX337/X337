from core.api.runtime_api import RuntimeAPI

from core.runtime.artifact import Artifact


print("\nINITIALIZING API")


api = RuntimeAPI()


artifact = Artifact(
    name="create_ai_tutor_website",
    artifact_type="website",
    path="workspace/projects/create_ai_tutor_website",
    framework="static",
    install_commands=[],
    run_commands=[
        "python3 -m http.server 8000"
    ],
    preview_port=8000,
    status="created"
)


print("\nSTART")

result = api.start(
    artifact
)

print(result)


print("\nSTATUS")

status = api.status(
    artifact.name
)

print(status)


print("\nRUNNING")

running = api.running()

print(running)


print("\nPREVIEWS")

previews = api.previews()

print(previews)


print("\nSTOP")

stopped = api.stop(
    artifact.name
)

print(stopped)