from __future__ import annotations

from core.generators.generator_context import GeneratorContext
from core.generators.modules.base_module import BaseModule


class AppModule(BaseModule):
    """
    Generates the React application entry files.
    """

    @property
    def name(self) -> str:
        return "app"

    def generate(
        self,
        context: GeneratorContext,
    ) -> None:

        context.builder.template(
            template="react/index.html.j2",
            output="frontend/index.html",
            language="html",
        )

        context.builder.template(
            template="react/main.tsx.j2",
            output="frontend/src/main.tsx",
            language="typescript",
        )

        context.builder.template(
            template="react/App.tsx.j2",
            output="frontend/src/App.tsx",
            language="typescript",
        )
