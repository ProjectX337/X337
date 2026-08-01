from __future__ import annotations

import subprocess

from core.tools.tool import Tool


class TestTool(Tool):

    name = "test"


    def execute(
        self,
        context=None,
    ):

        result = subprocess.run(
            [
                "python",
                "-m",
                "pytest",
                "tests/generators",
                "-q",
            ],
            capture_output=True,
            text=True,
        )


        return {
            "passed":
                result.returncode == 0,

            "output":
                result.stdout,
        }
