import psutil
import time


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

            "pid": process.pid,

            "port": port,

            "process": process,

            "status": "running"
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
                record["pid"]
            )


            if process.is_running():

                record["status"] = "running"

                return True



        except psutil.NoSuchProcess:

            pass



        record["status"] = "dead"

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



        pid = record["pid"]



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



            record["status"] = "stopped"

            record["stopped_at"] = time.time()


            return True



        except psutil.NoSuchProcess:


            record["status"] = "dead"

            return False
