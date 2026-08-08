from pathlib import Path
import subprocess
import time
import urllib.request


class BrowserPreview:
    """
    Launches generated React applications
    and manages browser previews.
    """


    def __init__(
        self,
        port=5173
    ):

        self.port = port
        self.process = None



    #
    # Start Vite server
    #
    def start(
        self,
        project_path
    ):

        project_path = Path(project_path)


        self.process = subprocess.Popen(
            [
                "npm",
                "run",
                "dev",
                "--",
                "--host",
                "localhost",
                "--port",
                str(self.port)
            ],
            cwd=project_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )


        url = (
            f"http://localhost:{self.port}"
        )


        self.wait_for_server(
            url
        )


        return {

            "status":
                "running",

            "url":
                url,

            "port":
                self.port,

            "pid":
                self.process.pid

        }



    #
    # Wait until Vite responds
    #
    def wait_for_server(
        self,
        url,
        timeout=30
    ):

        start = time.time()


        while (
            time.time() - start
            < timeout
        ):

            try:

                with urllib.request.urlopen(
                    url,
                    timeout=2
                ) as response:

                    if response.status == 200:

                        return True


            except Exception:

                pass


            time.sleep(
                1
            )


        raise RuntimeError(
            "Preview server failed to start"
        )



    #
    # Stop server
    #
    def stop(self):

        if self.process:

            self.process.terminate()


            return {

                "status":
                    "stopped"

            }


        return {

            "status":
                "not_running"

        }