from __future__ import annotations

from pathlib import Path
import socket
import subprocess
import time
import urllib.request


class PreviewRuntime:
    """
    Starts Vite previews for canonical generated X337 applications.

    Canonical generated project layout:

        workspace/generated/<project_slug>/frontend/
    """

    def __init__(
        self,
        process_manager,
    ):
        self.process_manager = process_manager

    def _project_dir(self, project_slug: str) -> Path:
        return (
            Path("workspace")
            / "generated"
            / project_slug
            / "frontend"
        )

    def _find_free_port(self, preferred: int = 9100) -> int:
        port = preferred

        while True:
            with socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM,
            ) as sock:
                try:
                    sock.bind(("127.0.0.1", port))
                except OSError:
                    port += 1
                    continue

            return port

    def start(
        self,
        project_slug: str,
        port: int = 9100,
    ) -> dict:
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

        existing = self.process_manager.get(
            project_slug
        )

        if existing is not None:
            existing = existing["process"]

        if existing is not None:
            if existing.poll() is None:
                existing_port = getattr(
                    existing,
                    "_x337_port",
                    port,
                )

                return {
                    "project": project_slug,
                    "status": "already_running",
                    "port": existing_port,
                    "url": f"http://127.0.0.1:{existing_port}",
                }

            self.process_manager.stop(
                project_slug
            )

        actual_port = self._find_free_port(port)

        subprocess.run(
            ["npm", "install"],
            cwd=project_dir,
            check=True,
        )

        log_path = (
            Path("/tmp")
            / f"x337-preview-{project_slug}.log"
        )

        log_file = log_path.open(
            "w",
            encoding="utf-8",
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
                str(actual_port),
            ],
            cwd=project_dir,
            stdin=subprocess.DEVNULL,
            stdout=log_file,
            stderr=subprocess.STDOUT,
            text=True,
        )

        process._x337_log_path = str(log_path)

        process._x337_port = actual_port

        self.process_manager.register(
            project_slug,
            process,
            port=actual_port,
        )

        url = f"http://127.0.0.1:{actual_port}"

        deadline = time.time() + 30

        while time.time() < deadline:
            if process.poll() is not None:
                log_path = getattr(
                    process,
                    "_x337_log_path",
                    None,
                )

                detail = ""

                if log_path:
                    try:
                        detail = Path(
                            log_path
                        ).read_text(
                            encoding="utf-8",
                        )
                    except OSError:
                        pass

                raise RuntimeError(
                    "Preview server exited before "
                    f"becoming ready.\n{detail}"
                )

            try:
                with urllib.request.urlopen(
                    url,
                    timeout=2,
                ) as response:
                    if response.status == 200:
                        break
            except Exception:
                time.sleep(0.5)

        else:
            log_path = getattr(
                process,
                "_x337_log_path",
                None,
            )

            detail = ""

            if log_path:
                try:
                    detail = Path(
                        log_path
                    ).read_text(
                        encoding="utf-8",
                    )
                except OSError:
                    pass

            raise RuntimeError(
                "Preview server did not become ready "
                f"within 30 seconds.\n{detail}"
            )

        return {
            "project": project_slug,
            "status": "running",
            "port": actual_port,
            "url": f"http://127.0.0.1:{actual_port}",
        }

    def stop(self, project_slug: str) -> dict:
        record = self.process_manager.get(
            project_slug
        )

        if not record:
            return {
                "project": project_slug,
                "status": "not_running",
            }

        self.process_manager.stop(
            project_slug
        )

        return {
            "project": project_slug,
            "status": "stopped",
        }
