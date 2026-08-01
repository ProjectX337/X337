from __future__ import annotations

from core.generators.base_generator import BaseGenerator
from core.generators.generator_context import GeneratorContext
from core.generators.generation_result import GenerationResult


class PythonGenerator(BaseGenerator):
    """
    Python utility/script generator.
    """

    @property
    def name(self) -> str:
        return "python"

    def generate(
        self,
        context: GeneratorContext,
    ) -> GenerationResult:

        return context.builder.result()
