import socket
import time
import urllib.request


class PreviewSession:

    def wait_for_ready(
        self,
        port,
        timeout=10
    ):

        start = time.time()

        while time.time() - start < timeout:

            try:
                with socket.create_connection(
                    ("localhost", port),
                    timeout=1
                ):
                    return True

            except OSError:
                time.sleep(0.5)

        return False


    def check_http(
        self,
        url
    ):

        try:
            response = urllib.request.urlopen(
                url,
                timeout=3
            )

            return {
                "ready": True,
                "status": response.status
            }

        except Exception as e:

            return {
                "ready": False,
                "error": str(e)
            }
