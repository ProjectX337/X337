from __future__ import annotations

from core.tools.tool import Tool
from core.generators.react.generator import ReactGenerator


class GenerateTool(Tool):

    name = "generate"


    def execute(
        self,
        context,
    ):

        generator = ReactGenerator()

        result = generator.generate(
            context
        )

        return {
            "status": "generated",
            "files": len(
                result.files
            ),
        }
