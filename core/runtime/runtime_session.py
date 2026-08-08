import time
import uuid


class RuntimeSession:

    def __init__(
        self,
        artifact
    ):

        self.id = (
            "session_"
            + uuid.uuid4().hex[:8]
        )

        self.name = artifact.name

        self.artifact_type = artifact.artifact_type

        self.path = artifact.path

        self.preview_port = artifact.preview_port

        self.status = "created"

        self.started_at = time.time()

        self.updated_at = self.started_at

        self.processes = []

        self.preview = None

        self.health = {
            "status": "unknown",
            "last_check": None
        }


    def add_process(
        self,
        process,
        command
    ):

        self.processes.append(
            {
                "pid": process.pid,
                "command": command,
                "type": "runtime"
            }
        )

        self.updated_at = time.time()


    def set_running(self):

        self.status = "running"

        self.health = {
            "status": "healthy",
            "last_check": time.time()
        }


    def set_stopped(self):

        self.status = "stopped"

        self.health = {
            "status": "offline",
            "last_check": time.time()
        }


    def to_dict(self):

        return {

            "id": self.id,

            "name": self.name,

            "artifact_type":
                self.artifact_type,

            "path":
                self.path,

            "status":
                self.status,

            "started_at":
                self.started_at,

            "updated_at":
                self.updated_at,

            "preview_port":
                self.preview_port,

            "preview":
                self.preview,

            "processes":
                self.processes,

            "health":
                self.health
        }
