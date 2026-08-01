from __future__ import annotations

from core.generators.generator_context import GeneratorContext
from core.generators.modules.base_module import BaseModule


class ViteModule(BaseModule):
    """
    Generates the Vite configuration.
    """

    @property
    def name(self) -> str:
        return "vite"

    def generate(
        self,
        context: GeneratorContext,
    ) -> None:

        context.builder.template(
            template="react/vite.config.ts.j2",
            output="frontend/vite.config.ts",
            language="typescript",
        )
