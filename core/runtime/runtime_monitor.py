import time
import psutil


class RuntimeMonitor:


    def check(
        self,
        runtime
    ):

        alive = True


        for process in runtime.processes.values():

            try:

                p = psutil.Process(
                    process["pid"]
                )


                if not p.is_running():

                    alive = False


            except psutil.NoSuchProcess:

                alive = False



        if alive:

            runtime.health = {

                "status":"healthy",

                "last_check":
                    time.time()

            }


        else:

            runtime.health = {

                "status":"failed",

                "last_check":
                    time.time()

            }


        return runtime.health
