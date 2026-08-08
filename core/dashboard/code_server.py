from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from core.dashboard.code_routes import (
    list_files,
    read_file
)


PROJECT_PATH = (
    "workspace/generated/generated_app"
)


class CodeHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/api/files":

            files = list_files(
                PROJECT_PATH
            )

            self.send_response(200)

            self.send_header(
                "Content-Type",
                "application/json"
            )

            self.end_headers()

            self.wfile.write(
                json.dumps(files).encode()
            )

            return


        if self.path.startswith("/api/file"):

            path = (
                self.path
                .replace("/api/file?path=", "")
            )

            result = read_file(
                PROJECT_PATH,
                path
            )

            self.send_response(200)

            self.send_header(
                "Content-Type",
                "application/json"
            )

            self.end_headers()

            self.wfile.write(
                json.dumps(result).encode()
            )

            return


        self.send_response(404)
        self.end_headers()



def start_code_server(
    port=9001
):

    server = HTTPServer(
        (
            "localhost",
            port
        ),
        CodeHandler
    )


    print(
        f"X337 Code Server running at http://localhost:{port}"
    )


    server.serve_forever()
