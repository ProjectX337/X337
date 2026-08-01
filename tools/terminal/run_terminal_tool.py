import subprocess

from tools.base.base_tool import BaseTool


class RunTerminalTool(BaseTool):

    def __init__(self):
        super().__init__("Run Terminal")

    def execute(self, command: str, cwd: str = "."):

        self.log(f"Running command: {command}")

        result = subprocess.run(
            command,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True,
        )

        self.log("Command complete.")

        return {
            "success": result.returncode == 0,
            "return_code": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }