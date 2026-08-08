import json
import mimetypes
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import urlparse


PROJECT_ROOT = Path(
    "core/generator/generated_projects"
).resolve()


class PreviewHandler(BaseHTTPRequestHandler):

    def send_cors(self):

        self.send_header(
            "Access-Control-Allow-Origin",
            "*"
        )

    def serve_file(self, file_path):

        if not file_path.exists() or not file_path.is_file():

            self.send_response(404)
            self.send_cors()
            self.end_headers()

            self.wfile.write(
                b"File not found"
            )

            return

        content_type, _ = mimetypes.guess_type(
            str(file_path)
        )

        if content_type is None:

            content_type = "text/plain"

        content = file_path.read_bytes()

        self.send_response(200)

        self.send_header(
            "Content-Type",
            content_type
        )

        self.send_header(
            "Content-Length",
            str(len(content))
        )

        self.send_cors()

        self.end_headers()

        self.wfile.write(content)

    def do_GET(self):

        parsed = urlparse(self.path)

        path = parsed.path

        if path == "/api/projects":

            projects = []

            if PROJECT_ROOT.exists():

                for directory in PROJECT_ROOT.iterdir():

                    if directory.is_dir():

                        projects.append(
                            directory.name
                        )

            self.send_response(200)

            self.send_header(
                "Content-Type",
                "application/json"
            )

            self.send_cors()

            self.end_headers()

            self.wfile.write(
                json.dumps(projects).encode()
            )

            return

        parts = path.strip("/").split("/")

        if len(parts) < 2:

            self.send_response(200)

            self.send_cors()

            self.send_header(
                "Content-Type",
                "text/html"
            )

            self.end_headers()

            self.wfile.write(
                b"<h1>X337 Preview Server</h1>"
            )

            return

        project_name = parts[0]

        project_path = (
            PROJECT_ROOT /
            project_name
        )

        if not project_path.exists():

            self.send_response(404)

            self.send_cors()

            self.end_headers()

            self.wfile.write(
                b"Project not found"
            )

            return

        relative_path = "/".join(
            parts[1:]
        )

        target = (
            project_path /
            relative_path
        ).resolve()

        try:

            target.relative_to(
                project_path.resolve()
            )

        except ValueError:

            self.send_response(403)

            self.send_cors()

            self.end_headers()

            return

        self.serve_file(target)


def start_preview_server(
    host="localhost",
    port=9003
):

    server = HTTPServer(
        (
            host,
            port
        ),
        PreviewHandler
    )

    print(
        f"X337 Preview Server running at "
        f"http://{host}:{port}"
    )

    server.serve_forever()


if __name__ == "__main__":

    start_preview_server()
