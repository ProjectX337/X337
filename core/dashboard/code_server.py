from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs

from core.dashboard.code_routes import (
    list_files,
    read_file
)


PROJECT_PATH = "workspace/generated/generated_app"



class CodeHandler(BaseHTTPRequestHandler):


    def send_json(self, data):

        self.send_response(200)

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
            "GET, OPTIONS"
        )

        self.send_header(
            "Access-Control-Allow-Headers",
            "*"
        )

        self.end_headers()


        self.wfile.write(
            json.dumps(data).encode()
        )



    def do_OPTIONS(self):

        self.send_response(200)

        self.send_header(
            "Access-Control-Allow-Origin",
            "*"
        )

        self.send_header(
            "Access-Control-Allow-Methods",
            "GET, OPTIONS"
        )

        self.send_header(
            "Access-Control-Allow-Headers",
            "*"
        )

        self.end_headers()



    def do_GET(self):

        parsed = urlparse(
            self.path
        )


        if parsed.path == "/api/files":

            files = list_files(
                PROJECT_PATH
            )

            self.send_json(
                files
            )

            return



        if parsed.path == "/api/file":


            params = parse_qs(
                parsed.query
            )


            path = params.get(
                "path",
                [""]
            )[0]


            result = read_file(
                PROJECT_PATH,
                path
            )


            self.send_json(
                result
            )

            return



        self.send_response(404)

        self.end_headers()





def start_code_server(port=9001):


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

