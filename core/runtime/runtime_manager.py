from core.terminal.terminal_manager import TerminalManager
from core.runtime.process_manager import ProcessManager
from core.runtime.preview_registry import PreviewRegistry
from core.runtime.runtime_registry import RuntimeRegistry
from core.runtime.runtime_session import RuntimeSession

import os
import time


class RuntimeManager:

    def __init__(self):

        self.terminal = TerminalManager()

        self.process_manager = ProcessManager()

        self.preview_registry = PreviewRegistry()

        self.runtime_registry = RuntimeRegistry()


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


        session = {

            "name": artifact.name,

            "status": "starting",

            "started_at": time.time(),

            "path": artifact.path,

            "preview_port": artifact.preview_port,

            "processes": []

        }


        for command in artifact.install_commands:

            process = self.terminal.start(
                command,
                artifact.path
            )

            processes.append(
                process
            )


            session["processes"].append(
                {
                    "pid": process.pid,
                    "command": command,
                    "type": "install"
                }
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


            session["processes"].append(
                {
                    "pid": process.pid,
                    "command": command,
                    "type": "runtime"
                }
            )


            if artifact.preview_port:

                self.preview_registry.register(
                    artifact,
                    artifact.preview_port,
                    process.pid
                )


        time.sleep(1)


        artifact.status = "running"

        session["status"] = "running"


        runtime_session = RuntimeSession(
            artifact
        )

        runtime_session.set_running()


        runtime_session.preview = (
            self.preview_registry.get(
                artifact.name
            )
        )


        for process_record in session["processes"]:

            runtime_session.processes.append(
                process_record
            )


        self.runtime_registry.register(
            runtime_session
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
                self.preview_registry.get(
                    artifact.name
                ),


            "session":
                runtime_session.to_dict()

        }


        return result



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
