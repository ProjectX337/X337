from core.terminal.terminal_manager import TerminalManager
from core.runtime.process_manager import ProcessManager
from core.preview.runtime import PreviewRuntime
from core.runtime.project_runtime import ProjectRuntime

import os
import time


class RuntimeManager:

    def __init__(
        self,
        registry=None,
    ):

        self.terminal = TerminalManager()

        self.process_manager = ProcessManager()

        self.preview_runtime = PreviewRuntime()

        if registry is None:
            raise ValueError(
                "RuntimeManager requires RuntimeRegistry"
            )

        self.runtime_registry = registry


    def launch(
        self,
        artifact
    ):

        processes = []


        if not os.path.isabs(
            artifact.path
        ):

            artifact.path = os.path.abspath(
                artifact.path
            )


        os.makedirs(
            artifact.path,
            exist_ok=True
        )



        for command in artifact.install_commands:

            process = self.terminal.start(
                command,
                artifact.path
            )

            processes.append(
                process
            )




        for command in artifact.run_commands:

            process = self.terminal.start(
                command,
                artifact.path
            )


            processes.append(
                process
            )


            self.process_manager.register(
                artifact.name,
                process,
                artifact.preview_port
            )




        time.sleep(1)


        artifact.status = "running"


        runtime = ProjectRuntime.from_artifact(
            artifact
        )

        runtime.status = "running"

        if artifact.preview_port:

            runtime.preview = self.start_preview(
                artifact.name,
                artifact.preview_port
            )

        runtime.processes = {
            str(process.pid): {
                "pid": process.pid,
                "type": "runtime"
            }
            for process in processes
        }


        self.runtime_registry.register(
            runtime
        )


        result = {

            "artifact": {

                "name": artifact.name,

                "artifact_type": artifact.artifact_type,

                "path": artifact.path,

                "framework": artifact.framework,

                "status": artifact.status,

                "preview_port": artifact.preview_port

            },


            "processes": [

                {
                    "pid": process.pid
                }

                for process in processes

            ],


            "preview":
                runtime.preview,


            "runtime":
                runtime.to_dict()

        }


        return result



    def start_preview(
        self,
        project_slug
    ):

        preview = self.preview_runtime.start(
            project_slug
        )

        return preview



    def stop(
        self,
        artifact_name
    ):

        stopped = self.process_manager.stop(
            artifact_name
        )


        return stopped



    def status(
        self,
        artifact_name
    ):

        return self.runtime_registry.get(
            artifact_name
        )
