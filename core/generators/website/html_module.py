from __future__ import annotations

from core.generators.generator_context import GeneratorContext
from core.generators.modules.base_module import BaseModule


class HTMLModule(BaseModule):
    """
    Generates the website HTML entry point.
    """

    @property
    def name(self) -> str:
        return "html"

    def generate(
        self,
        context: GeneratorContext,
    ) -> None:

        context.builder.template(
            template="website/index.html.j2",
            output="website/index.html",
            language="html",
            project_name=context.spec.project_name,
            description=context.spec.description,
        )
