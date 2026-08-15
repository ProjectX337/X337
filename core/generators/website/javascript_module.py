from __future__ import annotations

from core.generators.generator_context import GeneratorContext
from core.generators.modules.base_module import BaseModule


class JavaScriptModule(BaseModule):
    """
    Generates website client-side JavaScript.
    """

    @property
    def name(self) -> str:
        return "javascript"

    def generate(
        self,
        context: GeneratorContext,
    ) -> None:

        context.builder.template(
            template="website/app.js.j2",
            output="website/app.js",
            language="javascript",
            project_name=context.spec.project_name,
        )
