from pathlib import Path
import subprocess
import os


class PreviewManager:
    """
    Starts and manages generated application previews.
    """

    def __init__(self):
        self.processes = {}


    def create_preview(
        self,
        project_name,
        project_path,
        port=8000
    ):

        path = Path(project_path)


        if not path.exists():
            return {
                "status": "error",
                "message": "Project not found"
            }


        process = subprocess.Popen(
            [
                "npm",
                "run",
                "dev",
                "--",
                "--host",
                "0.0.0.0",
                "--port",
                str(port)
            ],
            cwd=path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )


        self.processes[project_name] = process


        return {

            "name": project_name,

            "url":
                f"http://localhost:{port}",

            "port":
                port,

            "pid":
                process.pid,

            "status":
                "running"

        }



    def stop_preview(
        self,
        project_name
    ):

        process = self.processes.get(
            project_name
        )


        if process:

            process.terminate()

            return {
                "status":
                    "stopped"
            }


        return {
            "status":
                "not_found"
        }
