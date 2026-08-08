import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from core.generator.project_generator import ProjectGenerator
from core.preview.runtime import preview_runtime


generator = ProjectGenerator()


class GeneratorHandler(BaseHTTPRequestHandler):

    def _headers(self, status=200):

        self.send_response(status)

        self.send_header(
            "Content-Type",
            "application/json"
        )

        self.send_header(
            "Access-Control-Allow-Origin",
            "*"
        )

        self.send_header(
            "Access-Control-Allow-Methods",
            "GET, POST, OPTIONS"
        )

        self.send_header(
            "Access-Control-Allow-Headers",
            "Content-Type"
        )

        self.end_headers()


    def do_OPTIONS(self):

        self._headers()


    def do_POST(self):

        if self.path != "/api/generate":

            self._headers(404)

            self.wfile.write(
                json.dumps({
                    "error": "Endpoint not found"
                }).encode()
            )

            return


        try:

            length = int(
                self.headers.get(
                    "Content-Length",
                    0
                )
            )

            body = self.rfile.read(length)

            data = json.loads(
                body.decode("utf-8")
            )

            prompt = data.get(
                "prompt",
                ""
            ).strip()


            if not prompt:

                self._headers(400)

                self.wfile.write(
                    json.dumps({
                        "error": "Prompt is required"
                    }).encode()
                )

                return


            # --------------------------------------------------
            # 1. GENERATE PROJECT
            # --------------------------------------------------

            project = {
                "project": prompt
            }

            result = generator.generate(
                project
            )


            # --------------------------------------------------
            # 2. DETERMINE PROJECT NAME
            # --------------------------------------------------

            project_name = result["slug"]


            # --------------------------------------------------
            # 3. START LIVE PREVIEW
            # --------------------------------------------------

            preview = preview_runtime.start(
                project_name
            )


            # --------------------------------------------------
            # 4. RETURN EVERYTHING TO DASHBOARD
            # --------------------------------------------------

            response = {

                "project": project_name,

                "status": "generated",

                "directory":
                    result["directory"],

                "files":
                    result["files"],

                "pages": [
                    "Dashboard",
                    "Practice",
                    "Profile"
                ],

                "components": [
                    "AIChat",
                    "ProgressTracker",
                    "TaskPlanner"
                ],

                "preview": {

                    "status":
                        preview["status"],

                    "url":
                        preview["url"]

                },

                "message":
                    "X337 generated project and started live preview"

            }


            self._headers(200)

            self.wfile.write(
                json.dumps(
                    response
                ).encode()
            )


        except Exception as error:

            self._headers(500)

            self.wfile.write(
                json.dumps({

                    "error":
                        str(error)

                }).encode()
            )


def start_generator_server(
    host="localhost",
    port=9002
):

    server = HTTPServer(
        (
            host,
            port
        ),
        GeneratorHandler
    )


    print(
        f"X337 Generator Server running at "
        f"http://{host}:{port}"
    )


    server.serve_forever()


if __name__ == "__main__":

    start_generator_server()
