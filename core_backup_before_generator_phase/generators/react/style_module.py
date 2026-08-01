from __future__ import annotations

from core.generators.generator_context import GeneratorContext
from core.generators.modules.base_module import BaseModule


class StyleModule(BaseModule):
    """
    Generates global React styling files.
    """

    @property
    def name(self) -> str:
        return "style"

    def generate(
        self,
        context: GeneratorContext,
    ) -> None:

        context.builder.template(
            template="react/index.css.j2",
            output="frontend/src/index.css",
            language="css",
        )
