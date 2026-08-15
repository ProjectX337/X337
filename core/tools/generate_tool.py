from __future__ import annotations

from core.generators.generation_service import GenerationService
from core.tools.tool import Tool


class GenerateTool(Tool):

    name = "generate"

    def __init__(
        self,
        generation_service: GenerationService | None = None,
    ) -> None:

        self.generation_service = (
            generation_service
            if generation_service is not None
            else GenerationService()
        )

    def execute(
        self,
        context,
    ):

        result = self.generation_service.generate(
            context.spec
        )

        return {
            "status": "generated",
            "files": len(
                result.files
            ),
            "result": result,
        }
