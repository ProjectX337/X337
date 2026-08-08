from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from core.dashboard.dashboard_state import DashboardState


dashboard = DashboardState(
    project_name="generated_app",
    project_path="workspace/generated/generated_app"
)


dashboard.scan_project()


class DashboardHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/api/dashboard":

            response = dashboard.summary()

            self.send_response(200)

            self.send_header(
                "Content-Type",
                "application/json"
            )

            self.end_headers()

            self.wfile.write(
                json.dumps(response).encode()
            )

            return


        self.send_response(404)
        self.end_headers()



def start_dashboard(port=9000):

    server = HTTPServer(
        (
            "localhost",
            port
        ),
        DashboardHandler
    )

    print(
        f"X337 Dashboard running at http://localhost:{port}"
    )

    server.serve_forever()
