import time
import psutil


class RuntimeMonitor:


    def check(
        self,
        session
    ):

        alive = True


        for process in session.processes:

            try:

                p = psutil.Process(
                    process["pid"]
                )


                if not p.is_running():

                    alive = False


            except psutil.NoSuchProcess:

                alive = False



        if alive:

            session.health = {

                "status":"healthy",

                "last_check":
                    time.time()

            }


        else:

            session.health = {

                "status":"failed",

                "last_check":
                    time.time()

            }


        return session.health
