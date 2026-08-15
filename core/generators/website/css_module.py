from __future__ import annotations

from core.generators.generator_context import GeneratorContext
from core.generators.modules.base_module import BaseModule


class CSSModule(BaseModule):
    """
    Generates global website CSS.
    """

    @property
    def name(self) -> str:
        return "css"

    def generate(
        self,
        context: GeneratorContext,
    ) -> None:

        context.builder.template(
            template="website/style.css.j2",
            output="website/style.css",
            language="css",
            project_name=context.spec.project_name,
        )
