import psutil
import time

from core.runtime.runtime_process import RuntimeProcess


class ProcessManager:


    def __init__(self):

        self.processes = {}



    def register(
        self,
        artifact_name,
        process,
        port=None
    ):

        self.processes[artifact_name] = {
            "runtime_process": RuntimeProcess(
                name=artifact_name,
                pid=process.pid,
                port=port,
            ),
            "process": process,
        }




    def list_runtime_processes(
        self,
    ):

        return {
            name: record["runtime_process"]
            for name, record in self.processes.items()
        }



    def get(
        self,
        artifact_name
    ):

        return self.processes.get(
            artifact_name
        )




    def is_running(
        self,
        artifact_name
    ):

        record = self.get(
            artifact_name
        )


        if not record:
            return False



        try:

            process = psutil.Process(
                record["runtime_process"].pid
            )


            if process.is_running():

                record["runtime_process"].status = "running"

                return True



        except psutil.NoSuchProcess:

            pass



        record["runtime_process"].status = "dead"

        return False





    def stop(
        self,
        artifact_name
    ):

        record = self.get(
            artifact_name
        )


        if not record:

            return False



        pid = record["runtime_process"].pid



        try:

            process = psutil.Process(
                pid
            )


            process.terminate()



            try:

                process.wait(
                    timeout=5
                )


            except psutil.TimeoutExpired:

                process.kill()



            record["runtime_process"].status = "stopped"

            record["runtime_process"].created_at = (
                record["runtime_process"].created_at
            )


            return True



        except psutil.NoSuchProcess:


            record["status"] = "dead"

            return False
