from fastapi import FastAPI

from core.api.runtime_api import RuntimeAPI

from core.runtime.runtime_container import (
    runtime_service,
    runtime_controller,
)
from core.runtime.artifact import Artifact


app = FastAPI(
    title="X337 Runtime Server"
)


#
# Runtime dependencies
#

runtime_api = RuntimeAPI(
    runtime_controller
)


#
# Root
#

@app.get("/")
def root():

    return {
        "status": "X337 Runtime Online"
    }


#
# Runtime start
#

@app.post("/runtime/start")
def start_runtime(payload: dict):

    artifact = Artifact(
        name=payload["name"],
        artifact_type=payload["artifact_type"],
        path=payload["path"],
        framework=payload.get(
            "framework"
        ),
        install_commands=payload.get(
            "install_commands",
            []
        ),
        run_commands=payload.get(
            "run_commands",
            []
        ),
        preview_port=payload.get(
            "preview_port"
        )
    )

    print(
        "START ARTIFACT:",
        artifact
    )

    return runtime_api.start(
        artifact
    )


#
# Runtime running
#

@app.get("/runtime/running")
def running():

    return runtime_api.running()


#
# Runtime previews
#

@app.get("/runtime/previews")
def previews():

    return runtime_api.previews()


#
# Runtime status
#

@app.get("/runtime/status/{name}")
def status(name: str):

    return runtime_api.status(
        name
    )


#
# Runtime stop
#

@app.post("/runtime/stop/{name}")
def stop(name: str):

    return runtime_api.stop(
        name
    )


#
# DEBUG ONLY
#

@app.get("/debug/registry")
def debug_registry():

    return registry.instances