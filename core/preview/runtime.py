from pathlib import Path
import subprocess


class PreviewRuntime:

    def __init__(self):
        self.processes = {}

    def _project_dir(self, project_slug):
        return (
            Path(__file__).resolve().parent.parent
            / "generator"
            / "generated_projects"
            / project_slug
        )

    def start(self, project_slug, port=9100):

        project_dir = self._project_dir(project_slug)

        if not project_dir.exists():
            raise FileNotFoundError(
                f"Generated project not found: {project_dir}"
            )

        package_json = project_dir / "package.json"

        if not package_json.exists():
            raise FileNotFoundError(
                f"package.json not found: {package_json}"
            )

        if project_slug in self.processes:
            return {
                "project": project_slug,
                "status": "already_running",
                "port": port,
                "url": f"http://localhost:{port}"
            }

        subprocess.run(
            ["npm", "install"],
            cwd=project_dir,
            check=True
        )

        process = subprocess.Popen(
            [
                "npm",
                "run",
                "dev",
                "--",
                "--host",
                "127.0.0.1",
                "--port",
                str(port)
            ],
            cwd=project_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        self.processes[project_slug] = process

        return {
            "project": project_slug,
            "status": "running",
            "port": port,
            "url": f"http://localhost:{port}"
        }

    def stop(self, project_slug):

        process = self.processes.get(project_slug)

        if not process:
            return {
                "project": project_slug,
                "status": "not_running"
            }

        process.terminate()

        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()

        del self.processes[project_slug]

        return {
            "project": project_slug,
            "status": "stopped"
        }


preview_runtime = PreviewRuntime()
