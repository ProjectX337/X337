from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from core.dashboard.dashboard_state import DashboardState


state = DashboardState(
    "workspace/generated/generated_app"
)


class DashboardHandler(
    BaseHTTPRequestHandler
):

    def do_GET(self):

        if self.path == "/api/dashboard":

            data = state.summary()

            self.send_response(200)

            self.send_header(
                "Content-Type",
                "application/json"
            )

            self.end_headers()

            self.wfile.write(
                json.dumps(data).encode()
            )

            return


        self.send_response(404)

        self.end_headers()



def start_dashboard(
    port=9000
):

    server = HTTPServer(
        (
            "localhost",
            port
        ),
        DashboardHandler
    )


    print(
        f"Dashboard API running on {port}"
    )


    server.serve_forever()